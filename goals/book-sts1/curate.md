# Goal: Curate the Book

Evaluate the knowledge system's structure, coverage, quality, and internal consistency. You are not playing the game — you are assessing whether the book is serving the agents well.

## Entry Points

- `ontology/book-sts1/index.md` — What the book is, its components
- `ontology/book-sts1/coverage.md` — Current coverage state
- `heuristics/book-sts1/` — Meta-strategy for book maintenance (this is your reference standard)

## What to Evaluate

1. **Coverage.** Are there entities the agents encounter frequently that lack entries? Check recent run logs for entity references that don't resolve to existing entries.
2. **Quality.** Read a sample across categories. Do ontology entries contain strategic language? Do heuristic entries lack evidence? Are there stubs that add no value?
3. **Consistency.** Are entries in the same category structurally similar? Do wiki-links resolve? Are there contradictions between entries?
4. **Overfitting.** See `heuristics/book-sts1/overfitting.md`. Check drafting.md and archetypes.md for absolutist claims without sufficient evidence.
5. **Attribution.** Are lessons on the right entries? See `heuristics/book-sts1/attribution.md`.

## Output

1. Assessment (10-15 lines)
2. Specific issues found with file paths
3. Recommended fixes (direct edits for clear problems, exploration directives for uncertain ones)
4. Updated coverage.md if counts have changed
