# Hexaghost

- **Type:** Boss
- **Act:** 1
- **HP:** 250 (A0), 264 (A9)

## Pattern

Always starts with Activate (no damage, setup), then Divider. After that, repeats a 7-move cycle: Sear -> Tackle -> Sear -> Inflame -> Tackle -> Sear -> Inferno.

## Attacks

| Move | Damage | Effect |
|------|--------|--------|
| Activate | -- | Setup turn |
| Divider | (player max HP / 12 + 1) x 6 | At 80 max HP = 7x6 = 42. At 70 = 6x6 = 36 |
| Sear | 6 | Adds 1 Burn to discard (2 Burns at A19) |
| Tackle | 5x2 = 10 (6x2 = 12 at A4) | -- |
| Inflame | -- | Gains 12 Block + 2 [[buffs/Strength]] (3 Str at A19) |
| Inferno | 2x6 = 12 (3x6 = 18 at A4) | Adds 3 Burns to discard. Upgrades all existing Burns to Burns+. |

## Mechanics

**Burn Cards:** Unplayable status cards. Deal 2 damage per Burn in hand at end of turn. Clog hand (fewer real cards). Burns+ (upgraded by Inferno) deal 4 damage each.

**Burns are DOUBLE-LETHAL:** Burns eat block at end of turn (reducing to zero), AND THEN the next Hexaghost attack hits with no block remaining. Effective incoming = Burns + attack combined.

**[[buffs/Strength]] Scaling:** Gains [[buffs/Strength]] on Inflame turns, making subsequent attacks stronger.

**Inferno Damage:** Multi-hit means each hit is checked against block individually. Without [[debuffs/Weak]]: near-impossible to survive. With [[debuffs/Weak]]: 28 total (survivable).

**Turn 1 Free:** Activate does nothing.

**Fight Length:** ~13 turns with adequate damage. Can extend to 23+ turns without damage scaling.
