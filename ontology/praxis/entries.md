# Entries

The atomic unit of knowledge in Praxis. Each entry is a single markdown file describing one entity, concept, or topic.

## Anatomy

Every entry has:
- **Title** — `# Name` on line 1
- **Content** — facts (ontology) or guidance (heuristics) about that entity
- **Links** — `[[category/Name]]` references to related entries

## Categories

Entries are organized into **categories** — subdirectories within a node. A category groups entries of the same type (cards, enemies, relics, etc. in a game domain; layers, entries, linking in the praxis domain).

A node may also have **top-level files** — entries that don't fit a category or cover cross-cutting topics.

## Companion Entries

An entity may have entries in multiple layers at the same relative path:
- `ontology/sts1/cards/bash.md` — what Bash does (fact)
- `heuristics/sts1/cards/bash.md` — how to play Bash (strategy)

Not every entry needs a companion:
- Many ontology entries have no corresponding heuristic (the fact is self-explanatory, no decision involved)
- Some heuristic entries have no corresponding ontology entry (topic files covering cross-cutting strategy)

## Linking

`[[category/Name]]` links resolve **within the same layer and node**.

In `ontology/sts1/cards/bash.md`: `[[debuffs/Vulnerable]]` → `ontology/sts1/debuffs/vulnerable.md`
In `heuristics/sts1/cards/bash.md`: `[[enemies/Gremlin Nob]]` → `heuristics/sts1/enemies/gremlin-nob.md`

Cross-layer references use explicit paths when needed.

## Naming Convention

- Files: `lowercase-with-hyphens.md`
- Titles: `# Title Case Name`
- Wiki-links: `[[category/Title Case Name]]`
