# Heuristics Layer

The strategic layer. Every entry describes what to DO — decisions, priorities, algorithms, warnings — grounded in gameplay evidence.

## Categories

Per-entity heuristics live in category subdirectories mirroring the ontology: `cards`, `relics`, `enemies`, `events`, `potions`, `bosses`, `characters`, plus `development` (interface notes). Coverage is intentionally partial — not every ontology entity has a heuristic (see below). Live counts are on the site.

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
- `combat.md` — Full block algorithm, arithmetic checklist, potion timing
- `drafting.md` — Tier lists, healing priority, readiness checklists, gap-filling
- `archetypes.md` — Proven winning deck formulas
- `map.md` — Routing, elite targeting, act transitions

### Coverage gaps are mostly intentional
Not every ontology entity needs a heuristic. Entities get heuristics when:
- There's a non-obvious decision to make
- An agent made a mistake involving that entity
- A Curate pass identified it as a gap worth filling

Straightforward entities (Strike, Defend) and rare entities may never need heuristics.

## Properties

- **Provisional.** Every heuristic is a current best guess. It can be wrong. It gets updated when evidence contradicts it.
- **Evidence-grounded — evidence lives in the analyst layer.** A heuristic is grounded in observed gameplay, but it never cites a run number or labels an outcome "fatal." It states the lesson and its confidence; the run logs, audits, and win/loss record that justify it stay in the analyst layer. Express stakes in game terms — what damage you take, when HP reaches 0 — not as a verdict on a past run. So: "Don't play Fiend Fire while the enemy has Thorns — it exhausts your whole hand and each card triggers Thorns, often for lethal damage," NOT "NEVER use Fiend Fire vs Thorns — confirmed Run 182 death."
- **Conditional.** Good heuristics specify when they apply and when they don't. "ALWAYS rest below 40% HP... UNLESS the upgrade is Bash+ and no boss in 3 floors."
- **Actionable.** Every sentence should help make a decision. "Be careful with Fiend Fire" is not actionable. Specific conditions and outcomes are.
- **Honest about uncertainty.** "I think" when evidence is thin, not "clearly."
- **Game-only (no meta).** Same rule as ontology (see `ontology.md` → Game-only): no run numbers, no win/loss record, no "fatal"/outcome labels, no file paths or layer/structure references, no verification provenance. A heuristic says what to DO in the game and why — the evidence behind it lives in the analyst layer, not in the prose.
