# Goal: Extend the Book

Add new entries for entities that lack coverage. Focus on the highest-value gaps first.

## Entry Points

- `ontology/book-sts1/coverage.md` — Current coverage state and prioritized gaps
- `heuristics/book-sts1/entry-quality.md` — Quality standards for new entries
- `heuristics/book-sts1/splits.md` — What goes in ontology vs. heuristics

## Priority Order

1. **Entities the agent encounters frequently but has no entry for.** Check recent run logs for gaps.
2. **Entities with ontology but no heuristic, where a decision exists.** Not every entity needs a heuristic — only those where the agent has a non-trivial choice to make.
3. **Categories with low overall coverage.** Non-Ironclad cards, common relics without heuristics.

## How to Write

- **Ontology entries:** Look up the actual game mechanics. Be factual, complete, minimal. Include ascension variants if known.
- **Heuristic entries:** Only if there's something non-obvious to say. Ground claims in evidence. If you haven't seen the entity in gameplay, mark claims as theoretical.
- **Always create the ontology entry first.** Then decide if a heuristic is warranted.

## Output

- New ontology and/or heuristic files
- Updated coverage.md with new counts
