# Coverage Guidance — STS1

How to decide what needs entries in the STS1 knowledge system.

## Ontology Coverage Target

Aim for complete coverage of all game entities. Every card, enemy, boss, relic, event, potion, buff, debuff should have an ontology entry. Even a minimal entry (name, type, effect) is valuable because agents encountering the entity can look it up mid-session.

Current state: ~95%+ across most categories. Remaining gaps are obscure buffs/debuffs and edge-case encounters. See `ontology/book-sts1/coverage.md` for specifics.

## Heuristics Coverage Target

Heuristic coverage is intentionally incomplete. The rule:

**Create a heuristic when there's a non-obvious decision to make.**

| Situation | Create heuristic? | Why |
|-----------|-------------------|-----|
| Entity involves a complex decision | Yes | Agent needs guidance beyond what ontology provides |
| Agent made a costly mistake with this entity | Yes | Prevent the mistake from recurring |
| Entity is straightforward to use | No | Agent can derive correct behavior from ontology |
| Entity is rarely encountered | Usually no | Low ROI; create if the rare encounter is punishing |
| Entity is passive (no decision) | No | Nothing actionable to write |

## Priority for New Heuristics

1. **Entities that killed the agent or caused significant damage** — the lesson is fresh and the consequence is clear
2. **Entities encountered frequently without guidance** — high ROI, many opportunities to apply
3. **Entities with complex interactions** — multi-card combos, conditional boss patterns, events with hidden outcomes
4. **Expanding character coverage** — when a new character is being played, its card pool needs heuristics

## What NOT to Write Heuristics For

- Starter cards (Strike, Defend) — trivial
- Status/Curse cards — the ontology entry (effect description) is sufficient
- Passive relics with no decision point — nothing to advise on
- Small mobs that die in 1-2 turns — encounter-level guidance covers these
