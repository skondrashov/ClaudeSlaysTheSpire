# Heuristics Layer

The strategic layer. Every entry describes what to DO — decisions, priorities, algorithms, warnings — grounded in gameplay evidence.

## Categories

| Category | Count | Coverage vs Ontology |
|----------|-------|---------------------|
| cards | 130 | 37% of 350 cards |
| relics | 92 | 53% of 173 relics |
| enemies | 41 | 85% of 48 enemies |
| events | 33 | 100% of 33 events |
| potions | 26 | 100% of 26 potions |
| bosses | 9 | 75% of 12 bosses |
| characters | 4 | 100% of 4 characters |
| goals | 6 | Agent operating modes |

Plus 7 topic files that have no ontology counterpart: `combat.md`, `drafting.md`, `map.md`, `archetypes.md`, `rest-sites.md`, `hp-management.md`, `exhaust.md`.

## Entry Types

### Per-entity heuristics
One file per game entity (card, enemy, boss, relic, event, potion). Describes how to use/fight/handle that specific entity. Typical card heuristic:
- When to play
- Upgrade priority
- Synergies
- Matchup-specific notes

### Topic heuristics
Cross-cutting strategic documents covering a whole domain. These are the most valuable files in the system:
- `combat.md` (156 lines) — Full block algorithm, arithmetic checklist, potion timing
- `drafting.md` (216 lines) — Tier lists, healing priority, readiness checklists, gap-filling
- `archetypes.md` — Proven winning deck formulas with run citations
- `map.md` (80 lines) — Routing, elite targeting, act transitions

### Coverage gaps are mostly intentional
Not every ontology entity needs a heuristic. Entities get heuristics when:
- There's a non-obvious decision to make
- An agent made a mistake involving that entity
- A Curate pass identified it as a gap worth filling

Straightforward entities (Strike, Defend) and rare entities may never need heuristics.

## Properties

- **Provisional.** Every heuristic is a current best guess. It can be wrong. It gets updated when evidence contradicts it.
- **Evidence-grounded.** Claims cite run numbers. "NEVER use Fiend Fire against Thorns enemies — confirmed Run 182 death."
- **Conditional.** Good heuristics specify when they apply and when they don't. "ALWAYS rest below 40% HP... UNLESS the upgrade is Bash+ and no boss in 3 floors."
- **Actionable.** Every sentence should help make a decision. "Be careful with Fiend Fire" is not actionable. Specific conditions and outcomes are.
- **Honest about uncertainty.** "I think" when evidence is thin, not "clearly."
