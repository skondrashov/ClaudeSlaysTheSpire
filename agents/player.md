# Agent — Prompt Composition

This file tells the orchestrator how to assemble the agent prompt. It is NOT sent to the agent directly.

## Architecture

One generic agent. It doesn't know what domain it's operating in until it receives a task. The domain's ontology tells it what exists. The domain's heuristics tell it how to navigate. The goal tells it what to achieve.

## Prompt Structure

1. **`agents/core.md`** — The agent itself. Domain-agnostic. Describes how it interacts with knowledge (ontology + heuristics + [[links]]), behavioral properties (honesty, knowledge gaps, one-decision-at-a-time). Always loaded.

2. **Goal heuristic** — What the agent should do this session. One of:
   - `heuristics/goals/play.md` — Play a run (combat framework, act pathing, card rewards, when to query)
   - `heuristics/goals/analyze.md` — Analyze a completed run (review log, update knowledge)
   - `heuristics/goals/review.md` — Review system health (10-run retrospective)

3. **Session context** — Task-specific parameters:
   - Session token (PLAYER_SESSION env var)
   - Starting command (e.g., `start("IRONCLAD", 0)` for play, run number for analyze)
   - Any recent context the orchestrator wants to surface

The agent discovers everything else by querying:
- `plan()` loads domain ontology + heuristics relevant to the current situation
- `reason("topic")` looks up any entity in the knowledge web
- `[[links]]` in loaded entries point to related knowledge

## What goes where

| Content | Location | Why |
|---------|----------|-----|
| Agent behavior (honesty, knowledge gaps) | `agents/core.md` | Domain-agnostic |
| Domain facts (cards, enemies, buffs, rules) | `ontology/` | Formally closed, composable |
| Tool interface (what commands exist) | `ontology/interface/` | Facts about the environment |
| Strategic reasoning (how to fight, build, path) | `heuristics/` | Cached conclusions, provisional |
| Goal procedures (combat framework, analysis steps) | `heuristics/goals/` | Task-specific cached reasoning |

## Rules

1. **Read core.md and the goal heuristic with the Read tool every time.** Don't rely on memory.
2. **Include their complete, unmodified contents.** Every section exists because its absence caused a regression.
3. **Don't duplicate knowledge in the prompt.** Everything domain-specific is in ontology/ and heuristics/, loaded dynamically via `plan()` and `reason()`.
