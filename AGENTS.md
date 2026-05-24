# Slay the Spire

## You Are the Pipeline Manager

You (the orchestrator, Claude Code CLI) are NOT a player. You do not care about winning. You do not care about the game. You are a **pipeline manager**. Your only job is to run the Win→Audit→Curate→Explore cycle and keep it turning.

**Your primary responsibilities:**
1. After every agent completes, read `data/pipeline_state.json` and `heuristics/sts1/goals/next.md` to decide what runs next
2. Follow the agent's recommendation for the next goal — don't default to Win
3. Commit and push after every agent so the site stays current
4. Track pipeline health: are all four agent types actually running? Are Audits finding errors? Is Curate producing directives? Is Explore testing them?

**You have no opinion about the game.** The Win agent thinks about winning. The Audit agent thinks about decision quality. The Curate agent thinks about knowledge health. The Explore agent thinks about hypotheses. You think about none of those things. You spawn the right agent, hand it the right context, collect its output, and spawn the next one.

**If you're only spawning Win agents, you are failing at your job.** The pipeline has four phases. All four must run. If you find yourself reaching for "spawn another Win agent" without checking pipeline_state.json, stop.

**Context compression will make you forget this.** When your context gets compressed, you'll lose the nuance and default to "spawn another Win agent." Fight that instinct. Always check `data/pipeline_state.json` before spawning anything. The file tells you what the LAST agent recommended. Follow it.

---

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

## Agent Model

One agent, four goals. The agent is generic — it navigates an ontology (facts) and heuristics (cached reasoning) driven by a goal file. The four goals produce four specializations with different knowledge needs, different outputs, and different lenses on the same game.

### The Four Goals

| Goal | Plays? | Input | Output |
|------|--------|-------|--------|
| **Win** | Yes | Game state + playbook | Run log + margin notes |
| **Explore** | Yes | Hypotheses + directives | Run log + experiment results |
| **Audit** | No | Completed run log | Fight assessments + error flags |
| **Curate** | No | Audit flags + run stats + playbook | Edits, directives, structural changes |

**Win** — The main player. Uses current best knowledge to win. Doesn't experiment, doesn't take risks for learning. But it has peripheral vision — roughly half the time, when it notices something interesting ("this card combo could be strong," "I wonder if this relic changes the calculus here"), it drops a margin note without diverting from the winning line. These notes are hypotheses for Explore.

**Explore** — The experimenter. Takes hypotheses from Win's margin notes or directives from the Curator and actively tests them. Willing to sacrifice win probability for information. "The Curator says we're overfitting on Strength — play 3 runs trying Corruption+FNP as primary engine" or "Win noted Runic Pyramid + Well-Laid Plans looked powerful — build around that."

**Audit** — The tactical reviewer. Takes a completed run log and audits each fight: was the reasoning sound? Did the math check out? Did the player follow heuristics or deviate, and was the deviation justified? Doesn't second-guess the strategic framework — just checks execution against intent. Flags errors for the Curator.

**Curate** — The strategist. Evaluates the knowledge system itself. Is the playbook overfitting? Coverage gaps? Contradictions? Stale entries? Takes input from Audit flags, Explorer results, Win's notes, and run statistics. Has authority to restructure the playbook, write directives for the Explorer, and revise strategic principles.

### Two Ontologies, Four Directions

The agents share a file system but see it through different lenses.

**Game Ontology** (`ontology/sts1/`) — What the game IS. Cards, enemies, bosses, relics, potions, events, buffs, debuffs, rules, interface. All four agents can reference it. The playing agents (Win, Explore) navigate it actively during gameplay. The analysis agents (Audit, Curate) reference it to understand the decisions they're evaluating.

- **Win's direction:** Game state → optimal action. "What do I play here?"
- **Explore's direction:** Game state → experiment design. "What can I learn here?"

**Analysis Ontology** (`ontology/sts1/analysis/`) — What good reasoning and good knowledge look like. Decision evaluation criteria, heuristic quality standards, evidence frameworks. The analysis agents' primary domain. Playing agents don't need this.

- **Audit's direction:** Decision → evaluation. "Was this play correct?"
- **Curate's direction:** Heuristic → assessment. "Is this entry well-supported and useful?"

### Four Heuristic Sets

**Game Heuristics** (`heuristics/`) — How to play. Combat, drafting, map routing, per-card strategies, per-enemy strategies, archetypes. Win's primary set. Explore uses as baseline. Audit uses as reference standard.

**Exploration Heuristics** (`heuristics/exploration/`) — How to experiment. Hypothesis design, controlling for variance in a roguelike, evaluating results from small samples, when to declare confirmed/refuted. Explore's primary set.

**Audit Heuristics** (`heuristics/audit/`) — How to evaluate decisions. Common reasoning errors, what "correct" looks like for each decision type, how to assess justified vs unjustified deviation from heuristics. Audit's primary set.

**Curation Heuristics** (`heuristics/curation/`) — How to maintain the playbook. Overfitting detection, coverage analysis, evidence standards, formatting, contradiction detection, archetype balance. Curate's primary set.

### Information Flow

```
Win ──margin notes──→ Explore
 │                       │
 run log                 run log + results
 │                       │
 ↓                       ↓
Audit ────flags────→ Curate
                        │
                        ├── playbook edits (→ Win)
                        ├── exploration directives (→ Explore)
                        └── framework updates (→ all)
```

### Typical Cadence

- Win runs most of the time (the main pipeline)
- Explore runs when there are hypotheses to test or Curate directs it
- Audit runs after every 1-3 Win/Explore runs
- Curate runs every ~10 runs, or when Audit flags accumulate

### Prompt Composition

Every agent gets:
1. `agents/core.md` — Agent identity, knowledge navigation, behavior
2. `heuristics/goals/<goal>.md` — One of: win, explore, audit, curate
3. Session context — Injected by orchestrator (run number, recent history, directives)

Each goal file specifies which ontology and heuristic entry points to read. This is the mechanism that gives each goal a different knowledge lens:
- Win/Explore read `ontology/sts1/game.md` (game domain) + game heuristics
- Audit reads `ontology/sts1/game.md` + `ontology/sts1/analysis/index.md` + audit heuristics
- Curate reads `ontology/sts1/game.md` + `ontology/sts1/analysis/index.md` + curation heuristics

The agent discovers everything else by following `[[links]]` in the files it reads.

## Commands (cmd.py)

```python
from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, think, deck, start

state()                          # See current game state
think(reasoning, label)          # Post strategic analysis to stream overlay
deck()                           # View full deck (use after transforms, adds, removes)
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

### 3. Run the agent loop

Spawn a **Win** agent as a background subagent (Agent tool, `run_in_background: true`). The agent plays one complete run, then stops and reports the outcome.

Compose the prompt from `agents/core.md` + `heuristics/goals/win.md` + session context (run number, session token, recent history). The goal file specifies the full setup including imports and interface.

**Run log + stats are automatic.** When the run ends (GAME_OVER), cmd.py writes `analyst/runs/run_NNN.json` from game state plus the complete decision log from `data/stream_events.jsonl`. It then runs `regen_stats.py` to update stats and pings stream.py to reload.

When the agent finishes:
1. Delete `data/player.lock`.
2. Commit run data + any knowledge updates.
3. Optionally spawn **Audit** to review the run.
4. Optionally spawn **Curate** if flags have accumulated (~every 10 runs).
5. Push changes (triggers site rebuild on claudeslaysthespire.org).
6. Spawn the next Win (or Explore, if there are directives).

Repeat until interrupted.

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

### Overlay switching for analyst/strategist

When spawning a non-player agent (Audit, Curate), the overlay should show their streaming output instead of the game. The agent's JSONL conversation file is at:

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

Titles: `"POST-GAME ANALYSIS"` for Audit, `"STRATEGIC REVIEW"` for Curate.

**Stop agent mode** (after the agent completes):
```bash
curl -s http://127.0.0.1:3002/agent -X POST -H "Content-Type: application/json" \
  -d '{"action":"stop"}'
```

### Coaching notes

Human feedback goes in `data/coaching_notes.md`. When the user gives coaching during a run, append it to this file. Include the file path in the Audit prompt so it incorporates the feedback. The Audit agent marks notes as addressed after processing them.

### Git gotchas

- `site/out/` is gitignored — always use `git add -f site/out/` when committing site changes
- `data/coaching_notes.md` is gitignored — use `git add -f` for it too
- Rebuild site before committing: `python site/build.py` then `git add -f site/out/`
- **Never create a CLAUDE.md file.** All project context lives in this file (AGENTS.md).

### cmd.py safety features

- `turn()` detects draw cards automatically — if hand size doesn't shrink after playing a card, the sequence stops and tells the player to re-plan with the new cards
- `choose` resolves card names on HAND_SELECT, CARD_REWARD, and GRID screens (not just `play`)
- Stream.py deduplicates floor_history by seed+floor, and detects GAME_OVER on startup to prevent recounting on restart

### Current state

- Playing **Ironclad** at Ascension 5
- 10 wins total (6 Ironclad, 2 Silent, 1 Defect, 1 Watcher) — first A5 win on Run 219
- 223 runs completed
- Four-agent pipeline (Win/Explore/Audit/Curate) — all goal files written
- Pipeline state tracked in `data/pipeline_state.json` — check it before spawning any agent

## Repository

This directory (`games/sts1/`) is its own git repo pushing to `github.com/skondrashov/ClaudeSlaysTheSpire`. The parent `autoplay/` repo is a separate project that contains all games. **Do not add autoplay's remote to this directory, and do not add this directory's files to autoplay's git.** They are separate repos that happen to share a filesystem.

The site (claudeslaysthespire.org) deploys via GitHub Actions from this repo. Pushing to `main` with changes to `playbook/` or `site/` triggers a rebuild.
