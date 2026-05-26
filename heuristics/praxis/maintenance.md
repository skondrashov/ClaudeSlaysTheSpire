# Maintenance

Ongoing operations for keeping the knowledge system healthy.

## When to Create an Entry

**Ontology:** Create when an entity is encountered that doesn't have an entry. Don't wait — even a stub (name, type, basic stats) is better than nothing. The agent encountering it is in the best position to write it.

**Heuristics:** Create when:
- An agent made a mistake involving this entity (the lesson needs a home)
- An Audit flagged an entity-specific error pattern
- A Curate pass identified it as a coverage gap worth filling
- The entity has a non-obvious decision associated with it

Do NOT create heuristic stubs. Either write something actionable or don't create the file.

## When to Update an Entry

- **New evidence.** A run revealed something not in the entry. Add it with a run citation.
- **Counter-evidence.** A run contradicted the entry. Soften language, add the exception.
- **Ascension change.** Playing at a new ascension level reveals mechanics that differ. Add ascension-specific values.
- **Curate flag.** The Curate agent identified an issue (absolutist language, missing conditions, stale content).

## When to Split an Entry

- A topic file has grown past ~150 lines and covers distinct sub-topics. Split into a main file and sub-topic files.
- A per-entity entry is covering territory that applies to multiple entities. Extract the general part to a topic file.

## When to Merge Entries

- Two entries cover the same ground with slightly different framing. Keep the better one.
- An entity entry has been reduced to "see [topic file]" — just delete it if the topic file covers everything.

## When to Delete an Entry

- The entry is wrong and there's nothing correct to replace it with.
- The entry duplicates content that lives elsewhere (and the elsewhere version is better).
- The heuristic has been superseded by the model's ability to derive the answer from ontology facts alone (rare — verify before deleting).

## Red Flags During Maintenance

- **Entry inflation.** Adding sentences to an entry without removing any. Entries should stay focused.
- **Citation rot.** Run citations from 100+ runs ago that may no longer reflect current play level or strategy.
- **Orphaned advice.** Heuristic advice that references ontology facts that have changed or entries that no longer exist.
- **Format drift.** Entries in the same category using different structures. Periodically normalize.
