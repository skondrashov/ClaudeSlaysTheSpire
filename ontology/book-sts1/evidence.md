# Evidence System

How heuristic claims get grounded in gameplay — and where that grounding lives. The short version: **evidence lives in the analyst layer; the heuristic carries only the resulting confidence, never a citation.** The game has no concept of a past run, so neither does its knowledge.

## Evidence Sources

All in the analyst layer:

- **Run logs** (`analyst/runs/run_NNN.json`) — Every decision, reasoning, and resulting state from a completed run. Primary evidence for what happened.
- **Audit reports** (`analyst/audits/run_NNN.md`) — Per-decision correctness assessment from Audit sessions.
- **Observations** (`analyst/observations.md`) — Pending lessons awaiting confirmation before they reach a heuristic.
- **Run statistics** (`data/run_stats.json`) — Aggregate data: wins, deaths, floors, character stats.
- **Seed replays** — Same seed played with different strategy, isolating strategy from card/enemy variance.

## Evidence Standards

Curate enforces a minimum amount of evidence — **held in the analyst layer** — before a heuristic is allowed a given strength of language. The evidence gates the *language*; it is never written into the heuristic.

| Claim strength | Minimum evidence (in the analyst layer) |
|-----------|-----------------|
| "don't do X" (strong warning) | A clear losing line caused by X — the game consequence understood, not just one bad run |
| "always do X" | Multiple runs where X led to success, no counter-evidence |
| "prefer X over Y" | Direct comparison in similar contexts, ≥3 confirming instances |
| "X is viable" | At least one win using X (existence proof) |
| "X is the best" | Multiple wins + evidence the alternatives do worse |

A claim whose evidence doesn't meet the bar for absolute language uses **conditional language instead** ("usually," "I think," "in my experience") — that is how uncertainty shows up in the prose. Strength of evidence becomes strength of wording; it never becomes a run citation.

## Attribution

When a run produces a lesson, it goes on the entity that CAUSED the outcome, not the context where it happened.

**Test:** "Would this lesson apply in a different fight?" If yes, it doesn't belong on the fight.

Example: Fiend Fire exhausting critical block cards during a fight → the lesson goes on **Fiend Fire's heuristic**, not the boss's. The boss didn't cause it.

## Lifecycle

```
Observation (run log) → Analysis (audit) → Claim (heuristic draft) → Validation (explore) → Confirmed heuristic
```

- An **observation** starts in `analyst/observations.md`, with its run/audit provenance.
- It becomes a **heuristic claim** written in game terms, with confidence matched to the evidence — provisional (conditional language) until validated.
- On validation, the claim's language firms up. The provenance — which runs, which audits — **stays in the analyst layer**. It is never promoted into the heuristic prose.

So a heuristic never says "confirmed Run 182." It says the lesson, as confidently as the analyst-layer evidence warrants, and the trail back to that evidence lives where the evidence does.
