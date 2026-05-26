# Linking System

How entries reference each other within and across layers.

## Wiki-Links

Syntax: `[[category/Name]]`

Resolves to an entry within the same layer:
- In ontology: `[[debuffs/Vulnerable]]` → `ontology/sts1/debuffs/vulnerable.md`
- In heuristics: `[[enemies/Gremlin Nob]]` → `heuristics/sts1/enemies/gremlin-nob.md`

Links enable composition: an entry about Bash can reference Vulnerable's mechanics without restating them.

## Companion Entries

Many entities have entries in BOTH ontology and heuristics at the same path:
- `ontology/sts1/cards/bash.md` — what Bash does
- `heuristics/sts1/cards/bash.md` — when and how to play Bash

The website generates cross-links ("View strategy" / "View facts") between companions.

Not all entries have companions:
- Buffs, debuffs, rules, types, acts → ontology only (no strategic guidance needed)
- Topic files (combat.md, drafting.md, archetypes.md) → heuristics only (no corresponding fact)
- Goals → goals only (agent instructions)

## Filename Convention

- Files: `lowercase-with-hyphens.md`
- Entity titles: `# Title Case Name`
- Cross-references: `[[category/Title Case Name]]`
- Name → filename: lowercase, spaces → hyphens, strip apostrophes and periods

## Entry Points

Each layer has an entry-point file that links to everything else:
- `ontology/sts1/game.md` — overview of the game with links to all categories
- `heuristics/sts1/combat.md` + `drafting.md` + `map.md` + `archetypes.md` — the core strategic documents
- `goals/sts1/next.md` — decision logic for which goal to run next
