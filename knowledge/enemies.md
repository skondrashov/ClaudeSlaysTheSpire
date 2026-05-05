# Enemies

Enemy mechanics documented from actual runs. Entries cite the run where they were observed.

## Slime Boss

Act 1 boss. HP: ~140 (observed).

- **Split**: When reduced to ~50% HP, Slime Boss splits into Spike Slime (L) and Acid Slime (L). This is the most dangerous part of the fight — you go from one enemy to two, both with significant HP and damage.
- **Slimed cards**: Both large slimes add Slimed cards to your deck. Slimed is a status card that costs 1 energy and exhausts when played, doing nothing useful. These clog your hand badly — we saw 3 out of 5 cards be Slimed in a single hand.
- **Pre-split strategy**: You want to prepare for the split. Front-loading damage before the split is less important than having the tools to handle two enemies afterward.
- **Post-split priority**: After the split, you're fighting two enemies that each attack for 11-16+ damage per turn. AOE or the ability to kill one quickly is critical. Without either, the combined damage overwhelms your block.
- Confidence: MEDIUM (1 run observed, died to this boss)

### Spike Slime (L)
- Attacks for ~16 damage
- Applies Frail (reduces block gained from cards by 25%)
- Adds Slimed cards to deck
- Confidence: MEDIUM (observed in Run 1)

### Acid Slime (L)
- Attacks for ~11-12 damage
- Applies Weak (reduces your attack damage by 25%)
- Has its own Split ability — can split into smaller slimes
- Adds Slimed cards to deck
- Confidence: MEDIUM (observed in Run 1)

## General Notes

### Frail
- Reduces block gained from cards by 25%. This is multiplicative with the card's block value.
- Defend gives 5 base → 3 when Frail (observed in Run 1, Defend giving only 3 block)
- Shrug It Off gives 8 base → 6 when Frail
- Frail is extremely punishing when fighting multiple enemies because you need more block total but each block card gives less
- Confidence: HIGH (game mechanic, observed consistently in Run 1)

### Weak
- Reduces your attack damage by 25%
- Confidence: MEDIUM (game mechanic, need to verify exact math)

### Vulnerable
- Target takes 50% more damage from attacks
- Formula: (base + strength) * 1.5, rounded down
- Confidence: MEDIUM (standard game mechanic, should verify)
