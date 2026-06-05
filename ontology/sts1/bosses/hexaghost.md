# Hexaghost

- **Type:** Boss
- **Act:** 1
- **HP:** 250

## Pattern

Always starts with Activate (no damage, setup), then Divider. After that, repeats a 7-move cycle: Sear -> Tackle -> Sear -> Inflame -> Tackle -> Sear -> Inferno.

## Attacks

| Move | Damage | Effect |
|------|--------|--------|
| Activate | -- | Setup turn |
| Divider | (player current HP / 12 + 1) x 6 | -- |
| Sear | 6 | Add 1 [[cards/Burn]] to discard |
| Tackle | 5x2 = 10 | -- |
| Inflame | -- | Gains 12 Block + 2 [[buffs/Strength]] |
| Inferno | (2 + Str) x 6 — **24 first, 36 second** | Add 3 [[cards/Burn]] to discard. Upgrade all existing [[cards/Burn]] in deck to [[cards/Burn]]+ |

**Strength scaling (block for the realized number, not the base):** Inflame gives Hexaghost +2 [[buffs/Strength]] each 7-move cycle, raising the damage of ALL its attacks (Sear, Tackle, Inferno) by 2 per hit per stack. Because Inflame fires *before* Inferno within the same cycle, the base 2x6 = 12 Inferno never actually occurs: the **first Inferno hits at 24** (4x6, after one Inflame), the **second at 36** (6x6, after two). Verified vs game jar: `INFERNO_DMG=2`, `infernoHits=6`, `STR_AMT=2`.
