# Combat

A combat encounter against one or more enemies. All card play, damage, and blocking happens within combat.

## Turn Structure

Each turn follows this sequence:

1. **Player turn start** — Block resets to 0 (unless [[buffs/Barricade]], [[relics/Calipers]], or [[cards/Blur]]). Draw cards from draw pile (default 5). Gain energy (default 3).
2. **Player plays cards** — Spend energy to play cards from hand. Cards resolve immediately (damage, block, buffs, debuffs, draw, exhaust).
3. **Player ends turn** — Remaining hand cards go to discard pile (except [[rules/retain]]ed cards). End-of-turn effects trigger.
4. **Enemy turn** — Each enemy acts according to its displayed intent. Damage is dealt, buffs/debuffs are applied. Enemy block resets at the START of the enemy's next turn, not at the end.

## Intents

Each enemy displays an intent icon showing what it will do this turn:
- **Attack** — displays the exact final damage number (includes enemy [[buffs/Strength]], [[debuffs/Weak]] on the enemy, [[debuffs/Vulnerable]] on the player). Multi-hit attacks show `NxM` (N damage, M times).
- **Block/Buff** — the enemy will gain block or apply a buff to itself.
- **Debuff** — the enemy will apply a debuff to the player.
- **Unknown** — intent is hidden (rare, specific enemies only).

Intent damage numbers are FINAL — use them directly for block calculations. Do not re-apply modifiers.

## Damage and Block

See [[rules/damage]] for the damage formula and [[rules/block]] for block mechanics.

Key interactions:
- Block absorbs damage first. Excess damage hits HP.
- [[relics/Fossilized Helix]] and [[buffs/Buffer]] prevent HP loss, not damage. Block is consumed BEFORE the prevention check. Against multi-hit attacks, block is depleted by hit 1 (Helix/Buffer catches overflow), then subsequent hits land with no block.
- [[buffs/Thorns]] and [[cards/Flame Barrier]] deal damage back to attackers per hit received (including hits absorbed by block).

## Energy and Card Costs

See [[rules/energy]]. Cards cost 0-5 energy. X-cost cards ([[cards/Whirlwind]], [[cards/Malaise]], [[cards/Skewer]]) consume ALL remaining energy when played.

## Draw

See [[rules/card-draw]]. Cards that draw ([[cards/Backflip]], [[cards/Shrug It Off]], [[cards/Pommel Strike]], [[cards/Battle Trance]], [[cards/Offering]]) add new cards to hand immediately during the player's turn.

## Strength

[[buffs/Strength]] adds to ALL attack damage for the rest of the combat. Sources:
- **Per-combat** (resets between fights): [[cards/Inflame]], [[cards/Spot Weakness]], [[cards/Demon Form]], [[potions/Strength Potion]], [[cards/Limit Break]]
- **Persistent** (across combats): [[relics/Vajra]] (+1 permanent)

Enemy Strength works the same way — visible in intent damage numbers.

## Exhaust

When a card is exhausted, it goes to the exhaust pile and cannot be played again this combat (unless retrieved by [[cards/Exhume]]). See [[rules/exhaust]] for full mechanics, sources, and on-exhaust payoffs. [[cards/Corruption]] makes all Skills exhaust after play. Ethereal cards exhaust if still in hand at end of turn.
