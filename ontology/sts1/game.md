# Slay the Spire

Deckbuilder roguelike. Build a deck of cards, fight enemies, defeat bosses across 3 acts.

## Structure

Each run plays through [[acts/Act 1]], [[acts/Act 2]], [[acts/Act 3]], then an optional Act 4. Each act has a map of floors containing Monster rooms, Elite rooms, Events, Shops, Rest Sites, and Unknown rooms. A boss fight ends each act.

## Game Systems

- [[combat]] — Turn structure, intents, how damage/block/energy/draw interact in a fight
- [[rules/energy]] — 3E per turn (base). Cards cost energy to play.
- [[rules/block]] — Prevents damage. Resets to 0 at start of your turn.
- [[rules/damage]] — Attack cards deal damage modified by [[buffs/Strength]] and [[debuffs/Vulnerable]].
- [[rules/card-draw]] — Draw 5 cards per turn (base). Draw pile → hand → discard pile → reshuffle.
- [[rules/buffs-and-debuffs]] — Status effects applied during combat.

## Entity Categories

**Cards** — [[types/Attack]], [[types/Skill]], [[types/Power]], [[types/Status]], [[types/Curse]]. Character-specific pools + colorless. Individual entries at `ontology/sts1/cards/<name>.md`.

**Enemies** — Hallway fights and elites per act. Individual entries at `ontology/sts1/enemies/<name>.md`. See [[acts/Act 1]], [[acts/Act 2]], [[acts/Act 3]] for encounter lists.

**Bosses** — One per act, visible from floor 1. Entries at `ontology/sts1/bosses/<name>.md`.

**Relics** — Passive effects. Sources: elites (guaranteed), bosses (choice of 3), shops, events. Entries at `ontology/sts1/relics/<name>.md`.

**Potions** — Single-use consumables. 3 slots (base). Entries at `ontology/sts1/potions/<name>.md`.

**Events** — Choice encounters. Outcomes vary by act. Entries at `ontology/sts1/events/<name>.md`.

**Buffs/Debuffs** — Combat status effects. Entries at `ontology/sts1/buffs/<name>.md` and `ontology/sts1/debuffs/<name>.md`.

## Characters

- [[characters/Ironclad]] — Strength-based. Starter relic heals 6 HP/fight.
- [[characters/Silent]] — Poison and Shiv-based. Starter relic draws 2 extra on turn 1.
- [[characters/Defect]] — Orb-based. Starter relic channels 1 Lightning at combat start.
- [[characters/Watcher]] — Stance-based. Starter relic adds Miracle to hand at combat start.

## Analysis Methodology

For run analysis, see [[analysis/index]] — prediction errors, attribution, file conventions, observation lifecycle.

## Strategic Guidance

Heuristics — cached reasoning about how to play — live in `heuristics/sts1/`. The directory mirrors the ontology structure: `heuristics/sts1/cards/`, `heuristics/sts1/enemies/`, `heuristics/sts1/bosses/`, etc. For any entity, check whether a heuristic file exists alongside the ontology entry.

Topic-level heuristics for cross-cutting concerns:
- `heuristics/sts1/combat.md` — Combat execution, the full block algorithm, arithmetic checklist
- `heuristics/sts1/map.md` — Map routing, elite targeting, relic economy
- `heuristics/sts1/drafting.md` — Card evaluation, deck building, Act 2 readiness
- `heuristics/sts1/rest-sites.md` — Upgrade vs rest decisions
- `heuristics/sts1/hp-management.md` — HP thresholds, when to avoid combat
- `heuristics/sts1/exhaust.md` — Exhaust strategy
- `heuristics/sts1/archetypes.md` — Proven winning deck formulas

Per-character heuristics: `heuristics/sts1/characters/<name>.md`

## Interface

Game interaction tools live in `interface/sts1/` (separate from ontology). See `interface/sts1/tools.md` for setup and commands, `interface/sts1/stream.md` for streaming overlay.
