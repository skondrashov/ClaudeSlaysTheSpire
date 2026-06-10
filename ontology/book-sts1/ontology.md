# Ontology Layer

The factual database. Every entry describes what something IS — mechanics, numbers, behavior patterns — with no strategic interpretation.

## Game-only (no meta)

An ontology entry describes the **game**, as if our book, our runs, our tooling, and our verification did not exist. The game has no concept of any of these, so neither does its ontology. Never appears in an entry:

- **Run numbers or our win/loss record** — "Run 182", "confirmed in 3 runs", "0 wins in 14". The game has no past run.
- **Outcome labels** — "fatal", "death", "cost the run". The only thing fatal in the game is damage that takes HP to 0; say *that* in game terms (damage, HP), not as a verdict on a run.
- **The book's own structure** — file paths, layer names, "its own entity under `upgrades/`", "a phenomenon of", "base ⊕ delta". How we *organize* knowledge is `book`/`praxis` ontology, not the game's.
- **How a fact was verified** — "verified in the game jar", code internals like `Eruption.use()` or `INFERNO_DMG`. Provenance is the analyst's job; the entry states the fact plainly.

All of the above describe *our process*. They live in the analyst layer (evidence, provenance) or the `book`/`praxis` domains (framework structure) — never in game knowledge.

## Categories

| Category | Contents |
|----------|----------|
| cards | Cost, type, character, rarity, effect — the base form only; the upgrade is its own entity |
| upgrades | Per-card upgrade delta (base card, the Upgrade mechanic, the change). Composed with the base card, it yields the resolved `+` form — which lives in the phenomena layer, not here |
| relics | Rarity, effect description |
| enemies | HP, attack pattern algorithm, move table — A0 values; per-level changes live in `ascension` |
| encounters | Enemy group compositions per act |
| buffs | Effect description, directionality |
| events | Act, choice options and outcomes |
| potions | Rarity, effect description |
| debuffs | Effect description, directionality |
| bosses | HP, attack cycle, move table — A0 values; per-level changes live in `ascension` |
| rules | Core mechanics (energy, block, damage, card draw, buffs/debuffs) |
| types | Card type definitions (Attack, Skill, Power, Status, Curse) |
| characters | Starting deck, relic, HP, card pool description |
| acts | Floor count, encounter lists, boss options, card rewards |
| ascension | Per-level modifiers — the rule change each Ascension level applies |
| shop | Shop mechanics and pricing |

*(Live entry counts are shown on the site, not tracked here — hand-maintained counts only drift.)*

Plus 2 top-level files: `game.md` (entry point), `combat.md` (turn structure and mechanics).

## Entry Format

Entries are minimal and consistent within category. A typical card entry holds the base form only:

```markdown
# Bash

- **Cost:** 2E
- **Type:** [[types/Attack]]
- **Character:** Ironclad
- **Rarity:** Starter
- **Effect:** Deal 8 damage. Apply 2 [[debuffs/Vulnerable]].
```

Its upgrade is a separate entity in `upgrades/`:

```markdown
# Upgrade: Bash

- **Base:** [[cards/Bash]]
- **Mechanic:** [[rules/upgrade]]
- **Delta:** +2 damage, +1 Vulnerable
```

The resolved Bash+ (absolute values) is a generated *phenomenon* (`phenomena/sts1/cards/bash-plus.md`), not an ontology entry. All three are produced by `tools/regen` from canonical card data.

A typical enemy entry adds HP ranges (by ascension), pattern algorithm with transition probabilities, and a move table.

A typical buff/debuff entry is 3-4 lines: name, effect, directionality.

## Properties

- **Closure-checked.** An ontology entry is either correct or incomplete. It never needs "revision" in the sense of changing its mind — only extension with new ascension-level data, additional mechanics, or missing interactions.
- **Composable.** Entries reference each other via wiki-links. Two atomic facts can be composed to derive a third — but the derived result is never stored here. Stable, reused derivations materialize in the *phenomena* layer (e.g. an upgraded card's resolved values); everything else is computed at decision time.
- **No strategic language.** No "should," "always," "never," "prioritize." If strategic advice leaks into an ontology entry, it belongs in heuristics.
- **A0 baseline.** Numeric values are Ascension 0. Each level's rule change is its own entry in the `ascension` category, composed at play time.
