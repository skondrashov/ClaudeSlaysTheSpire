# Coverage

Current state of the knowledge system's completeness.

## Ontology Coverage

The ontology aims for complete coverage of game entities. Current state:

| Category | Entries | Estimated total game entities | Coverage |
|----------|---------|------------------------------|----------|
| cards | 350 | ~350 (all characters + colorless) | ~100% |
| relics | 173 | ~173 | ~100% |
| enemies | 48 | ~50 | ~96% |
| encounters | 42 | ~45 | ~93% |
| buffs | 37 | ~40 | ~93% |
| events | 33 | ~33 | ~100% |
| potions | 26 | ~26 | ~100% |
| debuffs | 18 | ~20 | ~90% |
| bosses | 12 | 12 | 100% |

Ontology is near-complete. Remaining gaps are obscure buffs/debuffs and edge-case encounters.

## Heuristics Coverage

Heuristics coverage is intentionally incomplete. Not every entity needs strategic guidance.

| Category | Heuristic entries | Ontology entries | Coverage | Assessment |
|----------|------------------|-----------------|----------|------------|
| events | 33 | 33 | 100% | Every event has a decision → every event needs guidance |
| potions | 26 | 26 | 100% | Every potion has usage timing questions |
| enemies | 41 | 48 | 85% | Missing: small mobs with trivial strategy |
| bosses | 9 | 12 | 75% | Missing: Act 4 bosses (Heart, Spire Shield/Spear) |
| relics | 92 | 173 | 53% | Many relics are passive with no decision |
| cards | 130 | 350 | 37% | Lowest coverage — most cards are character-specific, only Ironclad deeply covered |

## Coverage Gaps Worth Filling

Priority order:
1. **Act 4 bosses** — 3 missing boss heuristics, all for endgame content
2. **Non-Ironclad cards** — Silent, Defect, Watcher card pools have sparse heuristic coverage
3. **Common relics without heuristics** — Any relic the agent sees frequently but has no guidance on

## Coverage Gaps Acceptable to Leave

- **Starter cards** (Strike, Defend) — trivial to play, no decision
- **Rare colorless cards** — encountered too infrequently to justify entries
- **Small enemy mobs** — no individual strategy needed, handled by encounter-level guidance
- **Passive relics** — if there's no decision to make, there's no heuristic to write
