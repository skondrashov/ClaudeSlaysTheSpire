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
- Some cards exhaust after use (like Slimed, Shockwave). Others don't (like Bash, Strike).
- Exhaust is permanent for the combat — the card will not be drawn again
- True Grit+ can exhaust a card from your hand as an additional effect (observed in Run 0)
- Confidence: HIGH (standard mechanic, confirmed across Run 0 and Run 1)

## Ethereal

- Ethereal cards are automatically exhausted at end of turn if they are still in your hand (not played)
- This means you MUST play them or lose them permanently
- Always play Ethereal cards if they're in hand, even if you don't need the effect — permanent loss is worse than wasted block/damage
- Observed: Ghostly Armor in Run 1 — player correctly identified "must play or lose it"
- Confidence: MEDIUM (observed in Run 1, standard mechanic)

## Potions

### Fruit Juice
- Effect: Gain +5 Max HP (permanent)
- Best used at the start of a long fight (like a boss) for maximum value — the extra HP is available immediately
- Observed: Run 1, used at start of Slime Boss fight
- Confidence: MEDIUM (used once in Run 1)

### Speed Potion
- Effect: Gain Dexterity (adds block to all block-gaining cards for the rest of combat)
- Observed: Run 1, used against Slime Boss. Player used it to boost block against 35 incoming damage. Defend went from 5 to 10 block (5 Dexterity).
- Confidence: LOW (used once, exact Dexterity amount needs confirmation — may be +5)

## Relics

### Golden Idol
- Source: Golden Idol event (Act 1). Choose to take the idol, then choose a cost (lose 21 HP, lose 6 max HP, or gain a curse).
- Effect: Unknown. The player took 21 HP damage to acquire it (Run 1, floor 4) but we never observed what it does.
- Confidence: LOW (acquired in Run 1, effect not observed)

### Burning Blood
- Ironclad starter relic.
- Effect: Heal HP after every combat (amount unknown, probably 6).
- Observed: Referenced in Run 1 reasoning ("Burning Blood will heal some back")
- Confidence: LOW (referenced but exact heal amount not confirmed)

## Curl Up (Enemy Passive)

- Some enemies (Louses) have a passive shield that triggers when they are first hit
- Gives the enemy block (5-7 observed in Run 1)
- The first attack that hits them is partially or fully absorbed by this block
- Strategy: Hit them with a small attack first to trigger the block, then follow up with big attacks
- Or: Apply Vulnerable first with Bash to get value over more turns, accepting the first attack is partially absorbed
- Confidence: MEDIUM (observed in multiple Louse fights in Run 1)
