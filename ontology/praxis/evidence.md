# Evidence

How heuristic claims get grounded in observed outcomes.

## Evidence Sources

Domain-specific, but generally:
- **Action logs** — record of every decision and its outcome
- **Analysis reports** — per-decision correctness assessments from the analyst
- **Aggregate statistics** — win/loss rates, performance trends
- **Controlled comparisons** — same conditions, different strategy, comparing outcomes

## Evidence Strength

From weakest to strongest:

1. **Theory** — "This should work because of these mechanics." Generates hypotheses, not heuristics.
2. **Single observation** — "This happened once." Existence proof only.
3. **Repeated observation** — "This happened several times." Pattern, possibly confounded.
4. **Controlled comparison** — "Same conditions, different approach, different outcome." Eliminates variance.
5. **Multiple controlled comparisons** — General causal claim.

## Lifecycle

```
Observation (action log) → Analysis (analyst review) → Claim (heuristic draft) → Validation (explorer test) → Confirmed heuristic
```

Unvalidated claims stay marked as provisional with appropriate hedging language.

## Attribution

Lessons go on the entity that CAUSED the outcome, not the context where it happened.

**Test:** "Would this lesson apply in a different context?" If yes, it doesn't belong on the context.
