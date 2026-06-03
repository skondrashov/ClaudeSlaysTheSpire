# Goal Cycle

The agent cycles through goals to maintain the knowledge system. Each goal reads from the same ontology but loads different heuristics. The cycle prevents the system from converging on local optima.

## Goals

| Goal | Purpose | Reads | Writes |
|------|---------|-------|--------|
| Win | Play to win | Full ontology + game heuristics | Run logs, margin notes |
| Explore | Test hypotheses | Full ontology + exploration heuristics | Run logs, experiment results |
| Audit | Review execution | Full ontology + audit heuristics + run logs | Audit reports, curation flags |
| Curate | Evaluate strategy | Full ontology + full heuristics + audit reports | Directives, playbook edits |
| Develop | Improve interface | Ontology + interface docs | Code changes, interface docs |

## Cycle

```
Win (play) → Audit (check execution) → Curate (check strategy) → Explore (test alternatives) → Win
```

Default cadence:
- **Win** runs most of the time
- **Audit** triggers every ~3 runs
- **Curate** triggers every ~10 runs
- **Explore** triggers when Curate writes directives

## Information Flow

- Win drops **margin notes** — interesting patterns noticed during play but not pursued
- Audit produces **error reports** — specific mistakes with floor/turn/card detail
- Curate produces **exploration directives** — hypotheses to test, with specific instructions
- Explore produces **experiment results** — evidence confirming/refuting hypotheses
- Results flow back into heuristic updates

## Pipeline State

Tracked in `data/pipeline_state.json` (relative to `games/sts1/`):
- `last_agent` — which goal last ran
- `last_run` — which run completed
- `next_recommended` — what the last session suggested
- `runs_since_last_audit` and `runs_since_last_curate` — cadence tracking
- `outstanding_directives` — exploration directives waiting for Explore
- `reason`, `character`, `ascension` — context for the last run

## Critical Property

**All four phases of the play cycle are required** (Win, Audit, Curate, Explore; Develop is an auxiliary interface mode, not part of the cycle). Only running Win causes the system to overfit to its current strategy. Only running Curate without Explore means replacing one form of overconfidence with another. The cycle exists because no single goal session can simultaneously play well, check its own work, evaluate its own strategy, AND test alternatives.
