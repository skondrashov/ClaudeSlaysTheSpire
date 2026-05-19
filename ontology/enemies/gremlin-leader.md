# Gremlin Leader

- **Type:** Elite
- **Act:** 2
- **HP:** 140-148 (A0), 145-155 (A8)

Starts with 2 gremlins already present. Maximum 3 small gremlins active at a time.

## Pattern

Move selection depends on gremlin count:
- 0 gremlins: Rally! 75% / Stab 25%
- 1 gremlin (last was Encourage): Rally! 50% / Stab 50%
- 1 gremlin (last was Stab): Rally! 62.5% / Encourage 37.5%
- 2+ gremlins: Encourage 66% / Stab 34%

Cannot use any intent twice in a row.

## Attacks

| Move | Damage | Effect |
|------|--------|--------|
| Stab | 6x3 = 18 | -- |
| Encourage | -- | All enemies gain 3 Strength + other gremlins gain 6 Block (Str scales to 4-5, Block to 10-18 at higher Ascensions) |
| Rally! | -- | Summons 2 random Gremlins |

## Mechanics

**Rally Strength Scaling:** Encourage gives +3 Str to ALL enemies (Leader + all gremlins). Permanent and stacking. Fires roughly every other turn.

**Rally Scaling Math:**
- Turn 3: all enemies have +3 Str
- Turn 5: all enemies have +6 Str
- Turn 7: all enemies have +9 Str
- With 2 gremlins alive at +9 Str, gremlins alone deal (9+9)*2 = 36, plus Leader's own attacks. Total incoming by turn 7-8 exceeds 50/turn.

**Gremlin Respawn:** Leader re-summons gremlins when they die -- killing gremlins is temporary relief, not permanent removal.

**Gremlin Wizard:** If present, charges for a massive 28-damage nuke. Must be killed before it fires.
