# Autoplay

LLM-powered game-playing system. Claude watches a game, reasons about it, and plays it — through mods, APIs, or whatever interface the game exposes. The goal is autonomous play that's good enough to be interesting on a Twitch stream.

## How it works

Every game follows the same brain-body split:

1. **Perception** — something reads game state and turns it into text Claude can reason about
2. **Reasoning** — Claude looks at the state, consults learned knowledge, decides what to do
3. **Execution** — something translates Claude's decision into game input (clicks, API calls, mod commands)

The perception and execution layers are completely game-specific. A Lua mod for one game, a C# mod for another, a Python SDK for a third, PostMessage clicks for a fourth. This is where most of the hard engineering lives, and it's different every time.

The reasoning layer and the knowledge management are where games share DNA. How Claude structures its thinking about a game state, how it builds and references a playbook over time, how it learns from mistakes — that's transferable.

## Games

### Balatro
Card-based roguelike. Lua/Steamodded mod reads game state and executes actions over TCP (port 19283). Python client (`cmd.py`) sends one action at a time — Claude reasons, calls a command, sees the result, repeats. Playbook built from ~25 runs, reached Ante 8 Boss. Strong foundation.

**Interaction layer:** Lua mod (server.lua, state_reader.lua, action_executor.lua) ↔ TCP JSON protocol ↔ Python client
**Knowledge:** `games/balatro/playbook/` — mechanics, strategy, jokers, consumables, blinds, bosses, mistakes
**Status:** Working. Interaction layer solid, knowledge growing.

### Slay the Spire (`games/sts1/`)
Deckbuilder roguelike. CommunicationMod (Java mod, Steam Workshop) handles all game state reading and action execution via stdin/stdout. A thin Python relay bridges this to TCP so Claude Code can play via `cmd.py` functions.

**Interaction layer:** CommunicationMod (stdin/stdout) ↔ relay.py (TCP :19284) ↔ Claude Code CLI (cmd.py)
**Mod stack:** ModTheSpire + BaseMod + CommunicationMod + SuperFastMode (all Steam Workshop, zero custom mod code)
**Streaming:** stream.py (WebSocket :3001 + HTTP :3002) → overlay/index.html (OBS browser source). Broadcasts game state, decisions, and reasoning to overlay clients in real time.
**Agents:** Player (plays), Analyst (post-run review → playbook updates), Steward (playbook quality + context hygiene). Definitions in `agents/`. See `AGENTS.md` in the game directory for full details.
**Knowledge:** `playbook/` — 130+ individual files organized by type: cards/, enemies/, bosses/, events/, potions/, relics/, plus mechanics.md and strategy.md. Each entry has mechanics + strategy + decision prompts. Built from 17 runs of gameplay.
**Site:** claudeslaysthespire.org — browsable playbook + changelog showing what Claude learned over time. Deploys via GitHub Actions.
**Status:** Active. 17 runs (Ironclad A0), best floor 28, 0 wins. Pipeline working end-to-end. Own git repo at github.com/skondrashov/ClaudeSlaysTheSpire.

### Slay the Spire 2
Deckbuilder roguelike. C# mod (Godot/Harmony patches) with two competing architectures that were never reconciled:

1. **Documented:** .NET 9 bot talks to mod via MCP over named pipe. Complex, fragile, partially working.
2. **Actual (bot_vm/):** Mod writes game state to JSON file. Python bot reads it, calls Claude API, writes decision. Mod executes via PostMessage clicks. Simpler, more reliable, but never documented or committed properly.

Mothballed at cycle 37 (2026-03-14) because of this mismatch. The bot_vm approach is probably the one to carry forward — it's the one that actually works.

**Interaction layer:** C# mod (StateFileWriter) + JSON files + PostMessage window messages
**Knowledge:** `games/sts2/knowledge.py` has full Ironclad card database + strategy. Memory files document the architecture pivot.
**Status:** Mothballed. Needs architecture decision committed before resuming.

### ARC-AGI-3
Interactive puzzle solving. Unlike the other games, this is 1-shot — you see a puzzle, figure out the rules from examples, and solve it. No iterative learning across runs, but the perception and reasoning patterns still overlap.

Three operational modes were built:
1. **Claude-as-player** — Claude Code CLI session plays directly via TCP
2. **LLM-as-API** — Anthropic Messages API with in-process game manager
3. **Pipeline** — 7 specialized agents (analyst, perception, explorer, planner, reviewer, troubleshooter, skeptic)

The pipeline mode is the most developed. Best scores: ft09 ~45.93, vc33 ~35.71.

**Interaction layer:** Python SDK (arc-agi Arcade), grid observation via numpy arrays → text descriptions
**Knowledge:** Per-game dossiers in `games/arc-agi/knowledge/`, general playbook
**Status:** Mothballed (2026-04-18). Code works, needs external validation against leaderboard.

## Shared infrastructure

### Streaming (`shared/streaming/`)
Not yet shared — currently game-specific. STS1 has a working implementation (stream.py + overlay). The aspiration is to extract common patterns:
- OBS browser source overlay showing Claude's reasoning + game state
- WebSocket server broadcasting state to overlay clients
- Twitch chat integration (reading chat, responding, taking suggestions)

### Core patterns (`shared/core/`)
Not yet extracted — currently embedded in each game. Shared patterns to extract:
- Playbook format and conventions (individual files per entry, decision prompts)
- Run logging and post-run analysis
- Decision framework (how Claude structures game reasoning)
- Common agent roles (player, analyst, steward)

## Directory structure

```
autoplay/
├── shared/
│   ├── streaming/       # Twitch + OBS overlay infrastructure
│   └── core/            # Shared reasoning patterns, knowledge management
├── games/
│   ├── balatro/         # Lua mod, TCP protocol, playbook
│   ├── sts1/            # CommunicationMod relay, cmd.py, playbook
│   ├── sts2/            # C# mod, bot_vm, knowledge
│   └── arc-agi/         # Python SDK, pipeline, dossiers
```

## Principles

- **One action at a time.** Claude reasons about the current state and sends one command. No autonomous loops, no background automation. The human can always see what's happening and intervene.
- **Evidence-based knowledge.** Playbook entries are grounded in actual gameplay. If it's confirmed, it goes in the playbook. If uncertain, it goes in analyst working notes. Wrong entries get corrected, not buried.
- **The interaction layer is the hard part.** Don't underestimate how much work goes into reliably reading game state and executing actions. This is where balatro succeeded and sts2 struggled. Budget accordingly.
- **Simpler is better for the body.** The sts2 lesson: a JSON file + PostMessage clicks beat a complex MCP/named-pipe architecture. The dumbest reliable interface wins.
- **Stream-worthy means explainable.** If Claude can't articulate why it's making a decision clearly enough for a Twitch viewer to follow, the reasoning isn't good enough.
