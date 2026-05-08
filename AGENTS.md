# Slay the Spire

Deckbuilder roguelike. CommunicationMod reads game state and executes actions. Claude Code CLI plays via TCP relay.

**DO NOT AUTOPLAY.** No scripts, loops, or automation that sends game actions without reasoning. Every action is a deliberate choice. In combat, plan the full turn, then execute as a batch — but still with explicit reasoning.

## Architecture

```
CommunicationMod (in-game Java mod, stdin/stdout)
        |
    relay.py (TCP server on localhost:19284)
        |
    Claude Code CLI (via cmd.py functions)
        |
    stream.py (WebSocket :3001 + HTTP :3002)
        |
    overlay/index.html (OBS browser source)
```

## Agents

### Player (`agents/player.md`)
Plays the game. Makes every decision with reasoning. In combat, fills out a combat plan template for the full turn, then executes with `turn()`. Outside combat, uses `send()` one action at a time.

Key traits:
- **Humble.** Says "I think" not "clearly." Admits uncertainty. Doesn't rationalize deaths.
- **Plans full turns.** Doesn't play one card at a time. Thinks about the whole hand, threats, energy, and expected outcome before acting.
- **Plans full fights.** At combat start, calls `plan()` to load playbook context, then writes a FIGHT STRATEGY (win condition, survival plan, key cards, risks) and posts it via `think()`.
- **References playbook.** Calls `plan()` at act/combat start, `reason("topic")` for targeted lookups. Playbook has 149+ files covering every card, enemy, boss, event, relic, and potion.
- **Always explains.** Every `send()` and `turn()` call includes `reason=`. The stream overlay shows this reasoning to viewers.

### Analyst (`agents/analyst.md`)
Runs after a completed run (victory or defeat). Reads the event log, identifies what went well and what went wrong, and updates playbook files.

Output directories:
- `playbook/` — Individual files per card, enemy, boss, event, potion, relic. Plus `mechanics.md` and `strategy.md` for general reference.
- `analyst/` — Working notes: `run_log.md` (brief per-run summaries), `observations.md` (uncertain items pending more data)

No confidence tags. If it's confirmed, it goes in `playbook/`. If uncertain, it goes in `analyst/observations.md`.

### Strategist (`agents/strategist.md`)
Runs every ~10 runs. Steps back and evaluates whether the whole system is working.

Key questions:
- **Are we improving?** Floor-reached trends, recurring deaths, plateaus and their causes.
- **Is the playbook serving the player?** Dead weight, missing coverage, signal-to-noise, structural fitness.
- **Cross-run patterns.** Things the analyst misses because it only sees one run at a time.
- **Architecture review.** Is the combat plan template helping? Is playbook loading effective? Is the analyst producing useful output?
- **Cleanup.** Dedup, trim bloat, promote observations, fix contradictions, archive stale data.

Has authority to reshape the playbook structure — consolidate files, rewrite sections, delete what isn't working.

## Commands (cmd.py)

```python
from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, plan, reason, think, start

state()                          # See current game state
plan()                           # Load strategic context (auto-detects combat vs act)
think(reasoning, label)          # Post strategic analysis to stream overlay
reason("topic")                  # Look up a specific playbook entry
send("play Bash 0", reason="...") # Single action — reason= is REQUIRED
turn(["play Bash Jaw Worm", "play Strike Jaw Worm", "play Defend", "end"],
     reason="...")               # Full combat turn — reason= is REQUIRED
choose(2, reason="...")          # Choose option — reason= is REQUIRED
choose("smith", reason="...")    # Choose by name (rest site)
proceed()                        # Confirm/proceed (auto-reason)
skip(reason="...")               # Skip/cancel/leave
potion_use(0, 1, reason="...")   # Use potion slot 0 on enemy 1 — reason= REQUIRED
potion_discard(0, reason="...")  # Discard potion slot 0
start("IRONCLAD", 5)             # Start Ironclad A5 run
```

**Card names preferred over indices.** `play Bash 0` resolves "Bash" against the current hand. Avoids index-shift bugs when playing multiple cards.

**Enemy names work for distinct enemies.** `play Bash Jaw Worm` resolves to the correct target. For same-name enemies (Byrds, Cultists), use numeric indices.

**Enemy indices are absolute** — they don't shift when enemies die. If Byrd [0] dies, remaining Byrds stay at [1] and [2].

## Mod Stack (all Steam Workshop)

1. ModTheSpire — mod loader
2. BaseMod — modding API
3. CommunicationMod — game state + action protocol
4. SuperFastMode — speed up animations for bot play

## Learning Loop

```
Player plays run → stream_events.jsonl captures every decision
    ↓
Run ends (victory or defeat) → player STOPS
    ↓
Analyst reads log, updates playbook/ files
    ↓
Every ~10 runs: Strategist reviews the arc, reshapes playbook, identifies bottlenecks
    ↓
Next run: player reads updated playbook before first action
    ↓
Player makes better decisions → repeat
```

The site (claudeslaysthespire.org) tracks every playbook diff over time — what changed, what was learned, how the system evolved. Two kinds of changes show up:
- **Pipeline changes** — dev restructures to improve how the system works
- **Playbook changes** — analyst updates from gameplay experience

## Repository

This directory (`games/sts1/`) is its own git repo pushing to `github.com/skondrashov/ClaudeSlaysTheSpire`. The parent `autoplay/` repo is a separate project that contains all games. **Do not add autoplay's remote to this directory, and do not add this directory's files to autoplay's git.** They are separate repos that happen to share a filesystem.

The site (claudeslaysthespire.org) deploys via GitHub Actions from this repo. Pushing to `main` with changes to `playbook/` or `site/` triggers a rebuild.

## How to Run

This is the full startup procedure. Follow it from the top when starting a new session.

### 1. Launch the game

Check if the relay is already up:
```python
python -c "from cmd import state; print(state())"
```

If you get "Cannot connect to relay", the game isn't running. Launch it:
```powershell
pwsh scripts/launch.ps1
```

This starts Slay the Spire via ModTheSpire, presses Enter to load mods, and waits until relay.py is online (port 19284). Prints "Ready." when done.

### 2. Start stream.py

```powershell
Start-Process -FilePath "python" -ArgumentList "stream.py" -WorkingDirectory "C:\Users\tkond\projects\autoplay\games\sts1" -WindowStyle Hidden
```

Verify: `Test-NetConnection 127.0.0.1 -Port 3001`. Provides the WebSocket overlay for streaming. Independent of relay — can restart without affecting gameplay.

### 3. Run the player/analyst loop

Spawn the **player** as a background subagent (Agent tool, `run_in_background: true`). Include the full contents of `agents/player.md` in the prompt. The player plays one complete run, then stops and reports the outcome.

When the player finishes:
1. Delete `data/player.lock`.
2. Switch the overlay to agent mode (see below).
3. Spawn the **analyst** as a subagent. Include `agents/analyst.md` in the prompt. It reads the run log, updates `playbook/` and `analyst/` files.
4. When analyst completes, switch overlay back to game mode.
5. Commit and push playbook changes (triggers site rebuild on claudeslaysthespire.org).
6. Spawn the next player.

Repeat until interrupted.

### Overlay switching for analyst/strategist

When spawning a non-player agent (analyst, strategist), the overlay should show their streaming output instead of the game. The agent's JSONL conversation file is at:

```
~/.claude/projects/C--Users-tkond-projects-autoplay/<session-id>/subagents/agent-<agent-task-id>.jsonl
```

**Start agent mode** (right after spawning the agent — use Python to avoid curl encoding issues):
```python
python -c "
import json, urllib.request
data = json.dumps({
    'action': 'start',
    'title': 'POST-GAME ANALYSIS',
    'jsonl_path': '<path-to-agent-jsonl>',
    'run_summary': '<player summary text with newlines>'
}).encode('utf-8')
req = urllib.request.Request('http://127.0.0.1:3002/agent', data=data, headers={'Content-Type': 'application/json'})
urllib.request.urlopen(req)
"
```

Titles: `"POST-GAME ANALYSIS"` for analyst, `"STRATEGIC REVIEW"` for strategist.
The `run_summary` field is shown in the bottom bar's action feed area during agent mode (replaces action log with a last-run summary from the player).

**Stop agent mode** (after the agent completes):
```bash
curl -s http://127.0.0.1:3002/agent -X POST -H "Content-Type: application/json" \
  -d '{"action":"stop"}'
```

The JSONL path requires the current Claude Code session ID and the agent's task ID (returned by the Agent tool). To find the session ID, check the most recently modified directory:
```bash
ls -td ~/.claude/projects/C--Users-tkond-projects-autoplay/*/ | head -1
```
Then construct the path as:
```
C:/Users/tkond/.claude/projects/C--Users-tkond-projects-autoplay/<SESSION_ID>/subagents/agent-<TASK_ID>.jsonl
```

stream.py watches the JSONL, parses assistant text blocks and tool_use blocks, and broadcasts them to the overlay. The overlay covers the game area with an opaque panel showing the agent's reasoning in real time.

### Rules

- **One player at a time.** Enforced by `data/player.lock` (see lock mechanism below).
- **Analyst runs between runs.** Never simultaneously with the player.
- **Overlay switches for analyst/strategist.** Always activate agent mode before spawning, deactivate after completion.
- **Commit after analyst.** The site changelog tracks every playbook diff.
- **If this session crashes**, the loop stops. Re-read this section and resume from wherever it left off. The game state persists in relay — nothing is lost.

### Player lock mechanism

Each Bash tool call is a separate Python process. The orchestrator gives the agent a unique token in its prompt. The agent must set `PLAYER_SESSION` env var to this token in every Bash call before importing cmd.py. The lock file stores which token is authorized.

**Before spawning a player agent:**
```python
import uuid, os
token = str(uuid.uuid4())
# Clear the old lock — previous agent is dead
if os.path.exists("data/player.lock"):
    os.remove("data/player.lock")
```

Then include in the agent prompt:
```
Your session token is: <token>
In every Bash call, before importing cmd, set:
    import os; os.environ["PLAYER_SESSION"] = "<token>"
```

**How it works:**
- cmd.py reads `PLAYER_SESSION` env var on import. Refuses to run without it.
- Lock file (`data/player.lock`) stores the token of whoever acquired it first.
- Same token → proceed. Different token → crash immediately.
- Orchestrator deletes lock file before spawning a new agent. That's the handoff.
- If the agent forgets to set the env var → import fails → agent dies. Orchestrator spawns a new one.

