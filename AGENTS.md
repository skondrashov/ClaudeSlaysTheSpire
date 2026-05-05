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
- **References playbook.** Reads `playbook/` files (individual files per card, enemy, boss, etc.). Leans toward documented knowledge over instinct.
- **Always explains.** Every `send()` and `turn()` call includes `reason=`. The stream overlay shows this reasoning to viewers.

### Analyst (`agents/analyst.md`)
Runs after a completed run (victory or defeat). Reads the event log, identifies what went well and what went wrong, and updates playbook files.

Output directories:
- `playbook/` — Individual files per card, enemy, boss, event, potion, relic. Plus `mechanics.md` and `strategy.md` for general reference.
- `analyst/` — Working notes: `run_log.md` (brief per-run summaries), `observations.md` (uncertain items pending more data)

No confidence tags. If it's confirmed, it goes in `playbook/`. If uncertain, it goes in `analyst/observations.md`.

### Steward (`agents/steward.md`)
Runs between sessions or when context is cluttered. Keeps the project clean and efficient.

Key responsibilities:
- **Playbook quality.** Verifies accuracy, removes duplicates, ensures card entries have DECISION POINTS and enemy entries have PATTERN/WHAT THIS MEANS sections.
- **Context hygiene.** Trims bloated run logs, promotes confirmed observations to reference/playbook, cleans up agent files.
- **Run data cleanup.** Archives processed run logs, verifies run_stats.json, removes stale temp files.

Does not play, analyze runs, write code, or make architectural decisions.

## Commands (cmd.py)

```python
from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, start

state()                          # See current game state
send("play 1 0", reason="...")   # Single action with reasoning
turn(["play 3", "play 1 0", "play 2", "end"],
     reason="Block first, then damage")  # Full combat turn
choose(2)                        # Choose option by index
choose("smith")                  # Choose by name (rest site)
proceed()                        # Confirm/proceed
skip()                           # Skip/cancel/leave
potion_use(0, 1)                 # Use potion slot 0 on enemy 1
start("IRONCLAD", 5)             # Start Ironclad A5 run
```

**Card indices are 1-indexed. Enemy indices are 0-indexed.**

**Card indices shift when you play cards!** Playing card 3 makes card 4 become card 3. Plan accordingly.

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

## Spawning Agents

Player and analyst agents are spawned as Claude Code subagents. Their role definitions are in `agents/player.md` and `agents/analyst.md`. When spawning an agent, include the full role definition in the agent prompt so it has all the context it needs — the subagent doesn't see the parent conversation.

Key rules:
- **One player agent at a time.** The lock file in `data/player.lock` enforces this, but don't rely on it — just don't spawn two.
- **Analyst runs after the run ends.** Don't run analyst and player simultaneously.
- **Commit playbook after analyst.** The analyst writes to `playbook/` and `analyst/`. Commit and push those changes so the site updates and the changelog tracks the diff.

## Key Differences from Balatro

- No custom mod needed — CommunicationMod does everything
- stdin/stdout, not TCP (relay bridges to TCP)
- Synchronous lock-step — mod waits for our command
- 1-indexed card positions
- Full turn planning with `turn()` instead of card-by-card
