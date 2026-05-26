# Agent Pipeline

Four agent roles cycle through the knowledge system. Each reads from the same ontology but different heuristic subsets. The cycle prevents the system from converging on local optima.

## Agents

| Agent | Purpose | Reads | Writes |
|-------|---------|-------|--------|
| Win | Play to win | Full ontology + game heuristics | Run logs, margin notes |
| Explore | Test hypotheses | Full ontology + exploration heuristics | Run logs, experiment results |
| Audit | Review execution | Full ontology + audit heuristics + run logs | Audit reports, Curator flags |
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

Tracked in `data/pipeline_state.json`:
- `last_agent` — which agent last ran
- `last_run` — which run completed
- `next_recommended` — what the last agent suggested
- `runs_since_last_audit` and `runs_since_last_curate` — cadence tracking
- `outstanding_directives` — exploration directives waiting for Explore

## Critical Property

**All four phases are required.** Only running Win causes the system to overfit to its current strategy. Only running Curate without Explore means replacing one form of overconfidence with another. The pipeline exists because no single agent can simultaneously play well, check its own work, evaluate its own strategy, AND test alternatives.
