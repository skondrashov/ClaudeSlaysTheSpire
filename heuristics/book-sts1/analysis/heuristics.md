# Heuristic Updates

Heuristics live in `heuristics/`. Each entity can have a heuristic file mirroring the ontology structure (`heuristics/cards/`, `heuristics/enemies/`, `heuristics/bosses/`, etc.). Topic-level heuristics cover cross-cutting concerns (`heuristics/combat.md`, `heuristics/map.md`, etc.).

Write like an expert — clear, direct, actionable.

## Rules

1. **No run numbers.** State conclusions, not history.
2. **No confidence tags.** If confident, state it. If uncertain, put it in [[layer:heuristics, analysis/observations]].
3. **Surgical updates.** One file per entry. Add a note, refine a threshold, adjust language.
4. **Wrong info gets fixed.** Don't flag it — correct it.
5. **Expert voice.** Reader should get exactly what they need.

## Don't

- Don't rewrite heuristic files from scratch
- Don't speculate beyond evidence — uncertain goes in observations
- Don't update for things that didn't come up in the run
