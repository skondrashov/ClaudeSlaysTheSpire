# Entries

The atomic unit of knowledge in Praxis. Each entry is a single markdown file describing one entity, concept, or topic.

## Anatomy

Every entry has:
- **Title** — `# Name` on line 1
- **Content** — facts (ontology) or guidance (heuristics) about that entity
- **Links** — `[[category/Name]]` references to related entries

## Categories

Entries are organized into **categories** — subdirectories within a domain. A category groups entries of the same type (cards, enemies, relics, etc. in a game domain; layers, entries, linking in the praxis domain).

A domain may also have **top-level files** — entries that don't fit a category or cover cross-cutting topics.

## Companion Entries

An entity may have entries in multiple layers at the same relative path:
- `ontology/sts1/cards/bash.md` — what Bash does (fact)
- `heuristics/sts1/cards/bash.md` — how to play Bash (strategy)

Not every entry needs a companion:
- Many ontology entries have no corresponding heuristic (the fact is self-explanatory, no decision involved)
- Some heuristic entries have no corresponding ontology entry (topic files covering cross-cutting strategy)

## Linking

A wiki-link's address is `category/id` — the **id** is what resolves, `category` annotates its type. Resolution is **ontology-canonical**: a bare `[[category/id]]` always points at the *ontology* entry, in the **current page's domain**, no matter which layer the link is written in. A fact has one canonical home, and a mention of it means that home.

To point anywhere else, spell out the qualifier(s) — `layer:`, `domain:` (and, rarely, `category:`) — lowercase, comma-separated, in any order:

- In `ontology/sts1/cards/bash.md`, `[[debuffs/vulnerable]]` → `ontology/sts1/debuffs/vulnerable.md` (ontology, current domain — the default).
- In `heuristics/sts1/cards/bash.md`, `[[debuffs/vulnerable]]` *still* resolves to the **ontology** fact (ontology-canonical), not a heuristics page.
- To reach a heuristic deliberately: `[[layer:heuristics, enemies/gremlin-nob]]`.
- To reach a goal (a flat layer, no category): `[[layer:goals, next]]`.
- To cross domains: `[[domain:praxis, layers]]`.

A bare `[[word]]` with no category and no qualifier is left as literal text, not a link.

## Naming Convention

- Files: `lowercase-with-hyphens.md`
- Titles: `# Title Case Name`
- Wiki-links: `[[category/Title Case Name]]`
