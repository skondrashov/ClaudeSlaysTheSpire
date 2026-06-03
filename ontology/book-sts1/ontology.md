# Ontology Layer

The factual database. Every entry describes what something IS — mechanics, numbers, behavior patterns — with no strategic interpretation.

## Categories

| Category | Contents |
|----------|----------|
| cards | Cost, type, character, rarity, effect, upgraded effect |
| relics | Rarity, effect description |
| enemies | HP (by ascension), attack pattern algorithm, move table |
| encounters | Enemy group compositions per act |
| buffs | Effect description, directionality |
| events | Act, choice options and outcomes |
| potions | Rarity, effect description |
| debuffs | Effect description, directionality |
| bosses | HP (by ascension), attack cycle, move table |
| analysis | Analysis methodology (attribution, prediction errors, patterns) |
| rules | Core mechanics (energy, block, damage, card draw, buffs/debuffs) |
| types | Card type definitions (Attack, Skill, Power, Status, Curse) |
| characters | Starting deck, relic, HP, card pool description |
| acts | Floor count, encounter lists, boss options, card rewards |
| shop | Shop mechanics and pricing |

*(Live entry counts are shown on the site, not tracked here — hand-maintained counts only drift.)*

Plus 2 top-level files: `game.md` (entry point), `combat.md` (turn structure and mechanics).

## Entry Format

Entries are minimal and consistent within category. A typical card entry:

```markdown
# Bash

- **Cost:** 2E
- **Type:** [[types/Attack]]
- **Character:** Ironclad
- **Rarity:** Starter
- **Effect:** 8 damage, apply 2 [[debuffs/Vulnerable]]
- **Upgraded:** 10 damage, apply 3 [[debuffs/Vulnerable]]
```

A typical enemy entry adds HP ranges (by ascension), pattern algorithm with transition probabilities, and a move table.

A typical buff/debuff entry is 3-4 lines: name, effect, directionality.

## Properties

- **Closure-checked.** An ontology entry is either correct or incomplete. It never needs "revision" in the sense of changing its mind — only extension with new ascension-level data, additional mechanics, or missing interactions.
- **Composable.** Entries reference each other via wiki-links. Two atomic facts can be composed to derive a third — but the composition is done by a heuristic; the derived result is not stored here as its own entry.
- **No strategic language.** No "should," "always," "never," "prioritize." If strategic advice leaks into an ontology entry, it belongs in heuristics.
- **Ascension-aware.** Numeric values include ascension variants where they differ (HP, damage, pattern changes).
