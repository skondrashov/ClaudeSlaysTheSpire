# Slime Boss

- **Type:** Boss
- **Act:** 1
- **HP:** 140 (A0), 150 (A9)

## Pattern

Fixed repeating cycle: Goop Spray -> Preparing -> Slam. Splits at 50% HP or below.

## Attacks

| Move | Damage | Effect |
|------|--------|--------|
| Goop Spray | -- | Adds 3 Slimed cards to discard pile (5 at A19) |
| Preparing | -- | Does nothing |
| Slam | 35 (38 at A4) | -- |
| Split | -- | At 50% HP (70 remaining at A0), spawns 1 [[enemies/Acid Slime L]] + 1 [[enemies/Spike Slime L]], each with boss's current HP |

## Mechanics

**Split at 50% HP:** Disappears and spawns [[enemies/Spike Slime L]] + [[enemies/Acid Slime L]] with current HP each. Excess damage past 70 HP is wasted AND makes the fight harder (lower HP = lower split HP for each slime).

**Slimed Cards:** Cost 1E to exhaust, do nothing. Clog hand (3 of 5 cards being Slimed observed).

**Post-Split Large Slimes Split Again:** Both [[enemies/Spike Slime L]] and [[enemies/Acid Slime L]] split into 2 medium slimes when killed at 50% HP. Killing one large slime creates a 3-enemy situation.

**Post-Split Damage:** Combined 25-36 damage per turn from two large slimes. [[debuffs/Frail]] (Spike Slime) + [[debuffs/Weak]] (Acid Slime) applied simultaneously.

## Pre-Split Phase

Alternates between debuff turns (Goop Spray + Preparing = safe to go all-in) and Slam (35 damage). Debuff turns are safe windows for damage.
