# Run Analysis

Review a completed run to extract what was learned and improve the knowledge base for future runs.

## Inputs

- **Run log** at `analyst/runs/run_NNN.json` — decision log with game state after each action
- **Ontology** at `ontology/` — facts about the game
- **Heuristics** at `heuristics/` — strategic guidance
- **Working notes** at `analyst/observations.md`

Read the run JSON first. It has everything.

## Priorities

1. **[[analysis/prediction-errors]]** — Before analyzing strategy, analyze understanding. Prediction errors reveal broken mental models. More important than bad strategy because they're upstream.

2. **[[analysis/strategic-patterns]]** — Decisions that were technically correct (math right) but strategically wrong (plan bad).

## Outputs

The analyst writes to three locations, each with different rules:

- **[[analysis/heuristic-updates]]** — Strategic guidance in `heuristics/`
- **[[analysis/ontology-corrections]]** — Factual fixes in `ontology/`
- **[[analysis/observations]]** — Uncertain findings in `analyst/observations.md`

## Core Principle

**[[analysis/attribution]]** — Attribute lessons to the mechanic that caused the mistake, not the fight where it happened.

## Process

1. Read the run JSON. First pass: prediction errors. Second pass: strategic mistakes.
2. Read existing heuristic files for entities encountered.
3. Make surgical updates to `heuristics/`. Fix wrong info, add new entries, refine existing.
4. Fix ontology only if facts are wrong.
5. Add uncertain items to `analyst/observations.md`.
6. Promote confirmed observations.
