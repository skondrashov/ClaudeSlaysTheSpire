# Evidence System

How claims in the heuristics layer get grounded in gameplay.

## Evidence Sources

- **Run logs** (`analyst/runs/run_NNN.json`) — Every decision, reasoning, and resulting state from a completed run. Primary evidence for what happened.
- **Audit reports** (`analyst/audits/run_NNN.md`) — Per-decision correctness assessment from Audit sessions.
- **Run statistics** (`data/run_stats.json`) — Aggregate data: wins, deaths, floors reached, character stats.
- **Seed replays** — Same seed played with different strategy, eliminating card/enemy variance as a confounder.

## Evidence Standards

Curate enforces these standards on heuristic claims:

| Claim type | Minimum evidence |
|-----------|-----------------|
| "NEVER do X" | Confirmed fatal outcome from X, with run citation |
| "ALWAYS do X" | Multiple runs where X led to success, no counter-evidence |
| "Prioritize X over Y" | Direct comparison in similar contexts, ≥3 confirming instances |
| "X is viable" | At least 1 win using X (existence proof) |
| "X is the best" | Multiple wins + evidence that alternatives perform worse |

Claims that don't meet their evidence standard get conditional language ("usually," "I think," "in my experience") instead of absolute language.

## Attribution

When a run produces a lesson, it goes on the entity that CAUSED the outcome, not the context where it happened.

**Test:** "Would this lesson apply in a different fight?" If yes, it doesn't belong on the fight.

Example: "Fiend Fire exhausted critical block cards during The Champ fight" → lesson goes on **Fiend Fire's heuristic**, not The Champ's. The Champ didn't cause the problem.

## Lifecycle

```
Observation (run log) → Analysis (audit) → Claim (heuristic draft) → Validation (explore) → Confirmed heuristic
```

Unvalidated claims stay marked as provisional. Confirmed claims get run citations.
