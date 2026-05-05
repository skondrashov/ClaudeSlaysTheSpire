# Game Mechanics

Mechanics documented from actual runs. Focus on things we got wrong or needed to learn.

## Status Cards

### Slimed
- Cost: 1 energy
- Effect: Exhaust (that's it — it does nothing except waste energy and a card slot)
- Source: Slime enemies add these to your deck
- Impact: Devastating to hand quality. In a 5-card hand, each Slimed card is -20% of your resources. We saw hands with 3 Slimed cards in Run 1, leaving only 2 playable cards.
- Playing Slimed is usually correct even if you have nothing else to do with the energy, because it exhausts the card permanently. Leaving it means it recycles into your deck.
- Confidence: HIGH (observed extensively in Run 1)

## Debuffs

### Frail
- Effect: Block gained from cards is reduced by 25%
- Duration: N turns, decrements at start of your turn
- Math: Defend 5 → 3 block (observed). Shrug It Off 8 → 6 block (observed).
- This is rounding: floor(5 * 0.75) = 3, floor(8 * 0.75) = 6
- Confidence: HIGH (observed in Run 1, math verified)

### Vulnerable
- Effect: Take 50% more damage from attacks
- Duration: N turns
- Berserk card applies this TO YOURSELF — extremely dangerous. 2 turns of Vulnerable in a multi-enemy fight can be fatal.
- Confidence: MEDIUM (observed in Run 1 — Berserk applied Vulnerable to self)

## Energy

- Base energy: 3 per turn (Ironclad, no relics modifying it)
- Energy resets each turn — unspent energy is wasted
- Confidence: HIGH (standard mechanic)

## Card Draw

- Standard draw: 5 cards per turn
- Cards that draw (like Shrug It Off) add to your hand mid-turn
- When planning a turn with draw cards, you can't predict the full turn — play the draw card first, then reassess
- Confidence: HIGH (standard mechanic)

## Damage Calculation

- Base formula: (card_base_damage + strength) * multipliers
- Vulnerable multiplier: 1.5x (on target)
- Weak multiplier: 0.75x (on attacker)
- These stack multiplicatively
- Confidence: MEDIUM (standard mechanics, need to verify interaction ordering)

## Exhaust

- Exhausted cards are removed from the deck for the rest of combat
- They go to the exhaust pile, not the discard pile
- Some cards exhaust after use (like Slimed, Bash doesn't)
- Confidence: HIGH (standard mechanic)
