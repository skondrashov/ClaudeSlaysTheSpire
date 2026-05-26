# Ontology Layer

The factual database. Every entry describes what something IS — mechanics, numbers, behavior patterns — with no strategic interpretation.

## Categories

| Category | Count | Contents |
|----------|-------|----------|
| cards | 350 | Cost, type, character, rarity, effect, upgraded effect |
| relics | 173 | Rarity, effect description |
| enemies | 48 | HP (by ascension), attack pattern algorithm, move table |
| encounters | 42 | Enemy group compositions per act |
| buffs | 37 | Effect description, directionality |
| events | 33 | Act, choice options and outcomes |
| potions | 26 | Rarity, effect description |
| debuffs | 18 | Effect description, directionality |
| bosses | 12 | HP (by ascension), attack cycle, move table |
| analysis | 7 | Analysis methodology (attribution, prediction errors, patterns) |
| rules | 6 | Core mechanics (energy, block, damage, card draw, buffs/debuffs) |
| types | 5 | Card type definitions (Attack, Skill, Power, Status, Curse) |
| characters | 4 | Starting deck, relic, HP, card pool description |
| acts | 3 | Floor count, encounter lists, boss options, card rewards |
| shop | 1 | Shop mechanics and pricing |

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
- **Composable.** Entries reference each other via wiki-links. Two atomic facts can be composed to derive a third without a separate entry.
- **No strategic language.** No "should," "always," "never," "prioritize." If strategic advice leaks into an ontology entry, it belongs in heuristics.
- **Ascension-aware.** Numeric values include ascension variants where they differ (HP, damage, pattern changes).
