# The Guardian

- **Type:** Boss
- **Act:** 1
- **HP:** 240 (A0), 250 (A9)

## Pattern

**Offensive Mode** (repeating cycle): Charging Up (9 Block) -> Fierce Bash (32 damage) -> Vent Steam (2 [[debuffs/Weak]] + 2 [[debuffs/Vulnerable]]) -> Whirlwind (5x4 = 20 damage).

**[[buffs/Mode Shift]]:** After taking 30 HP of damage (first cycle; 40 second, 50 third, +10 each), gains 20 Block and switches to Defensive Mode. Triggering [[buffs/Mode Shift]] mid-attack CANCELS the current attack.

**Defensive Mode:** [[buffs/Sharp Hide]] 3 (deal 3 damage to player per [[types/Attack]] card played) -> Roll Attack (9 damage) -> Twin Slam (8x2 = 16 damage, Removes [[buffs/Sharp Hide]], resets [[buffs/Mode Shift]] counter) -> returns to Offensive Mode.

## Attacks

| Move | Damage | Effect |
|------|--------|--------|
| Charging Up | -- | Gains 9 Block |
| Fierce Bash | 32 | -- |
| Vent Steam | -- | Applies 2 [[debuffs/Weak]] + 2 [[debuffs/Vulnerable]] |
| Whirlwind | 5x4 = 20 | -- |
| [[buffs/Sharp Hide]] | -- | Player takes 3 damage per [[types/Attack]] card played |
| Roll Attack | 9 | -- |
| Twin Slam | 8x2 = 16 | Removes [[buffs/Sharp Hide]], resets [[buffs/Mode Shift]] counter |

## Mechanics

**[[buffs/Mode Shift]]:** Counter values are 30, 40, 50 (+10 each cycle). Only HP damage counts (damage absorbed by block does NOT reduce counter). Triggering mid-attack cancels the attack -- primary survival mechanic.

**[[buffs/Sharp Hide]] 3:** 3 damage to player per [[types/Attack]] card played in Defensive Mode. Powers are safe (no trigger).

**32-Damage Attack:** The Guardian's biggest single hit. Must have 32+ block capability in one turn.

**Fight Length:** 240 HP means 12-14 turns minimum.

**Free Turns:** DEFEND and STRONG_DEBUFF intents deal no damage.
