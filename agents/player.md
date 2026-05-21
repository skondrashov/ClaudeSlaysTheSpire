# Agent — Prompt Composition

This file tells the orchestrator how to assemble the agent prompt. It is NOT sent to the agent directly.

## Architecture

One generic agent. It doesn't know what domain it's operating in until it receives a task. The domain's ontology tells it what exists. The domain's heuristics tell it how to navigate. The goal tells it what to achieve.

## Four Goals

| Goal file | Agent role | Plays game? |
|-----------|-----------|-------------|
| `heuristics/goals/win.md` | Play to win | Yes |
| `heuristics/goals/explore.md` | Play to learn | Yes |
| `heuristics/goals/audit.md` | Audit a run | No |
| `heuristics/goals/curate.md` | Curate the playbook | No |

See `AGENTS.md` for the full architecture: information flow, ontology split, heuristic sets.

## Prompt Structure

1. **`agents/core.md`** — The agent itself. Domain-agnostic. Describes how it navigates knowledge (ontology + heuristics + [[links]] via file reads), behavioral properties (honesty, knowledge gaps, one-decision-at-a-time). Always loaded.

2. **Goal file** — What the agent should do this session. One of the four above. The goal file specifies setup (imports, tools), output format, AND which ontology/heuristic entry points to read. This is how different goals get different knowledge lenses.

3. **Session context** — Task-specific parameters:
   - Session token (PLAYER_SESSION env var) — for playing agents only
   - Starting command (e.g., `start("IRONCLAD", 0)` for play, run number for audit)
   - Recent run history and any specific context
   - Exploration directives — for Explore agent only (from `analyst/directives.md`)

The agent discovers everything else by reading files:
- `[[category/Name]]` links → read `ontology/sts1/category/name.md` (domain + category + name)
- Per-entity heuristics → read `heuristics/category/name.md`
- Topic heuristics → referenced from the goal file (combat.md, drafting.md, etc.)

## What goes where

| Content | Location | Why |
|---------|----------|-----|
| Agent behavior (honesty, knowledge gaps) | `agents/core.md` | Domain-agnostic |
| Domain facts (cards, enemies, buffs, rules) | `ontology/` | Formally closed, composable |
| Game domain overview | `ontology/sts1/game.md` | Starting point for game navigation |
| Analysis methodology | `ontology/sts1/analysis/` | Facts about evaluation, not strategy |
| Tool interface (what commands exist) | `ontology/sts1/interface/` | Facts about the environment |
| Game strategy (how to fight, build, path) | `heuristics/` | Win agent's primary heuristics |
| Exploration methodology | `heuristics/exploration/` | Explore agent's primary heuristics |
| Audit methodology | `heuristics/audit/` | Audit agent's primary heuristics |
| Curation methodology | `heuristics/curation/` | Curate agent's primary heuristics |
| Goal procedures | `heuristics/goals/` | Task-specific entry points |

## Rules

1. **Read core.md and the goal file with the Read tool every time.** The goal file specifies which ontology/heuristic entry points to read. Don't rely on memory.
2. **Include their complete, unmodified contents.** Every section exists because its absence caused a regression.
3. **Don't duplicate knowledge in the prompt.** Everything domain-specific is in ontology/ and heuristics/, navigated via file reads and [[links]].
