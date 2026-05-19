# Slay the Spire

Deckbuilder roguelike. Build a deck of cards, fight enemies, defeat bosses across 3 acts.

## Structure

Each run plays through [[acts/Act 1]], [[acts/Act 2]], [[acts/Act 3]], then an optional Act 4. Each act has a map of floors containing Monster rooms, Elite rooms, Events, Shops, Rest Sites, and Unknown rooms. A boss fight ends each act.

## Game Systems

- [[rules/energy]] — 3E per turn (base). Cards cost energy to play.
- [[rules/block]] — Prevents damage. Resets to 0 at start of your turn.
- [[rules/damage]] — Attack cards deal damage modified by [[buffs/Strength]] and [[debuffs/Vulnerable]].
- [[rules/card-draw]] — Draw 5 cards per turn (base). Draw pile → hand → discard pile → reshuffle.
- [[rules/buffs-and-debuffs]] — Status effects applied during combat.

## Entity Categories

**Cards** — [[types/Attack]], [[types/Skill]], [[types/Power]], [[types/Status]], [[types/Curse]]. Character-specific pools + colorless. Individual entries at `ontology/cards/<name>.md`.

**Enemies** — Hallway fights and elites per act. Individual entries at `ontology/enemies/<name>.md`. See [[acts/Act 1]], [[acts/Act 2]], [[acts/Act 3]] for encounter lists.

**Bosses** — One per act, visible from floor 1. Entries at `ontology/bosses/<name>.md`.

**Relics** — Passive effects. Sources: elites (guaranteed), bosses (choice of 3), shops, events. Entries at `ontology/relics/<name>.md`.

**Potions** — Single-use consumables. 3 slots (base). Entries at `ontology/potions/<name>.md`.

**Events** — Choice encounters. Outcomes vary by act. Entries at `ontology/events/<name>.md`.

**Buffs/Debuffs** — Combat status effects. Entries at `ontology/buffs/<name>.md` and `ontology/debuffs/<name>.md`.

## Characters

- [[characters/Ironclad]] — Strength-based. Starter relic heals 6 HP/fight.
- [[characters/Silent]] — Poison and Shiv-based. Starter relic draws 2 extra on turn 1.
- [[characters/Defect]] — Orb-based. Starter relic channels 1 Lightning at combat start.
- [[characters/Watcher]] — Stance-based. Starter relic adds Miracle to hand at combat start.

## Strategic Guidance

Heuristics — cached reasoning about how to play — live in `heuristics/`. The directory mirrors the ontology structure: `heuristics/cards/`, `heuristics/enemies/`, `heuristics/bosses/`, etc. For any entity, check whether a heuristic file exists alongside the ontology entry.

Topic-level heuristics for cross-cutting concerns:
- `heuristics/combat.md` — Combat execution, the full block algorithm, arithmetic checklist
- `heuristics/map.md` — Map routing, elite targeting, relic economy
- `heuristics/drafting.md` — Card evaluation, deck building, Act 2 readiness
- `heuristics/rest-sites.md` — Upgrade vs rest decisions
- `heuristics/hp-management.md` — HP thresholds, when to avoid combat
- `heuristics/exhaust.md` — Exhaust strategy
- `heuristics/archetypes.md` — Proven winning deck formulas

Per-character heuristics: `heuristics/characters/<name>.md`

## Interface

See [[interface/tools]] for how to interact with the game.
