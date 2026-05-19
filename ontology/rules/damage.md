# Damage

## Formula

`floor((card_base_damage + strength) * multipliers)`

Order of operations:
1. Add [[Strength]] to base damage
2. Apply multipliers ([[Weak]] on attacker: x0.75, [[Vulnerable]] on target: x1.5)
3. Floor the result (round down)

Multipliers stack multiplicatively: `floor(base * 0.75 * 1.5)`

## Examples

| Scenario | Formula | Result |
|---|---|---|
| Strike (6) | 6 | 6 |
| Strike + Vuln on target | floor(6 * 1.5) | 9 |
| Strike + 2 Str | 6 + 2 | 8 |
| Strike + 2 Str + Vuln | floor((6+2) * 1.5) | 12 |
| Strike + 2 Str + Weak on self | floor((6+2) * 0.75) | 6 |

## Enemy Intent Display

Enemy intent numbers show the FINAL damage including all modifiers (Vulnerable on player, Weak on enemy, enemy Strength). Use the displayed number directly for block calculations — do not recalculate modifiers on top of it.
