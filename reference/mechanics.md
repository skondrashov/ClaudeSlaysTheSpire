# Game Mechanics

Core game systems and how they interact.

---

## Damage Formula

Base formula: `floor((card_base_damage + strength) * multipliers)`

Order of operations:
1. Add Strength to base damage.
2. Apply multipliers (Weak, Vulnerable).
3. Floor the result (round down).

### Multipliers

- **Vulnerable** (on target): x1.5 damage taken from attacks.
- **Weak** (on attacker): x0.75 damage dealt by attacks.
- These stack multiplicatively: `floor(base * 0.75 * 1.5)`

### Examples

| Scenario | Formula | Result |
|---|---|---|
| Strike (6) | 6 | 6 |
| Strike + Vulnerable | floor(6 * 1.5) | 9 |
| Strike + 2 Str | 6 + 2 | 8 |
| Strike + 2 Str + Vulnerable | floor((6+2) * 1.5) | 12 |
| Strike + 2 Str + Weakened | floor((6+2) * 0.75) | 6 |
| Strike + Weakened + Vuln target | floor(6 * 0.75 * 1.5) | 6 |

---

## Status Effects

### Vulnerable
- Target takes 50% more damage from attacks.
- Duration: N turns, decrements at start of affected entity's turn.
- When on enemies (from Bash, Thunderclap): YOUR attacks deal 50% more.
- When on YOU (from Berserk, enemy abilities): ENEMY attacks deal 50% more. Extremely dangerous against multiple enemies.
- Direction matters: Vulnerable on enemy = you deal more. Vulnerable on you = you take more.

### Weak
- Affected entity deals 25% less attack damage.
- Duration: N turns.
- Formula: `floor((base + strength) * 0.75)` -- Strength is added BEFORE the Weak multiplier.
- When on enemies (from Shockwave, Clothesline): THEIR attacks deal 25% less.
- When on YOU (from enemy debuffs): YOUR attacks deal 25% less.
- Direction matters: Weak on enemy = they deal less. Weak on you = you deal less.

### Frail
- Block gained from cards is reduced by 25%.
- Duration: N turns, decrements at start of your turn.
- Math: `floor(block * 0.75)`. Defend 5 -> 3. Shrug It Off 8 -> 6.
- Extremely punishing against multiple enemies where you need more total block but each block card gives less.

### Strength
- Each point of Strength adds 1 damage to every Attack card played.
- Permanent within combat (unless modified by Disarm or enemy debuffs).
- Negative Strength (from Lagavulin debuffs): reduces all attack damage by that amount. Strike goes from 6 to 5 to 4.
- IMPORTANT: Recalculate all damage values after Strength changes.

### Dexterity
- Each point of Dexterity adds block to all block-gaining cards.
- Negative Dexterity (from Lagavulin debuffs): reduces block from all block cards.

---

## Block Mechanics

- Block absorbs damage before HP.
- Block expires at the start of your turn (resets to 0).
- Exception: Barricade (enemy passive) -- block does NOT expire. Accumulates turn over turn.
- Metallicize and Plated Armor add block at end of turn (before enemy attacks resolve).
- Plated Armor decreases by 1 each time you take unblocked damage.

---

## Status Cards

| Card | Cost | Effect | Source | Persistence |
|---|---|---|---|---|
| Slimed | 1E | Exhaust (does nothing else) | Slime enemies | Cycles in deck until played for 1E to exhaust |
| Burn | Unplayable | 2 damage at end of turn if in hand | Hexaghost | Cycles in deck permanently (cannot be played) |
| Dazed | Unplayable | Ethereal (exhausts at end of turn if in hand) | Chosen (via Hex), Sentries | Self-exhausts via Ethereal; but new ones keep being added |
| Wound | Unplayable | Nothing -- pure hand clog | Book of Stabbing | Cycles in deck permanently (most persistent status) |

**Removal methods:**
- True Grit+ can exhaust any of these from hand.
- Burning Pact exhausts a chosen card from hand.
- Fiend Fire exhausts ALL cards in hand (converts them to 7 damage each).
- Slimed can be played for 1E to exhaust it (always correct -- removes it permanently).
- Dazed self-exhausts via Ethereal at end of turn.

**Status card severity ranking:** Wound (most persistent, no self-removal) > Burn (deals damage + clogs) > Slimed (costs 1E to remove) > Dazed (auto-exhausts but Hex keeps adding more).

---

## Keywords

### Exhaust
Removes a card from THIS COMBAT ONLY. The card goes to the exhaust pile and will not be drawn again for the rest of this fight. Your full deck resets between fights — exhausted cards return.

WHAT THIS MEANS: Exhaust has zero long-term cost. If Shockwave would help this fight, play it — you'll have it again next fight. Never "save" an exhausting card for a later fight. Cards that exhaust after use (Shockwave, Impervious, Fiend Fire) are meant to be played freely every fight they're drawn.

Exhaust is NOT card removal. Permanent card removal only happens at shops (remove service) or certain events (like Peace Pipe rest option). That's a completely different mechanic.

### Ethereal
- Ethereal cards exhaust at end of turn if still in hand (not played).
- ALWAYS play Ethereal cards if possible -- permanent loss is worse than wasted block/damage.
- Examples: Ghostly Armor, Carnage, Dazed.

### Innate
- Innate cards are always in your opening hand (turn 1 draw).
- Not observed frequently in current card pool.

### Retain
- Retained cards stay in hand at end of turn instead of being discarded.
- Not observed frequently in current card pool.

---

## Energy System

- Base energy: 3 per turn (Ironclad, no modifiers).
- Energy resets each turn -- unspent energy is WASTED.
- Energy modifiers: Lantern (+1E turn 1), Ancient Tea Set (+2E turn 1 after rest), Berserk (+1E/turn permanently), Seeing Red+ (+2E one time), Happy Flower (+1E every 3 turns).
- X-cost cards (Whirlwind) use ALL remaining energy. Play LAST.

---

## Card Draw

- Standard draw: 5 cards per turn.
- Cards that draw (Shrug It Off, Pommel Strike) add to hand mid-turn.
- When planning with draw cards: play the draw card first, then reassess with the new card(s).
- Brutality adds +1 card per turn (6 total) at the cost of 1 HP/turn.
- Dark Embrace draws 1 card per exhaust.

---

## Enemy Mechanics

### Artifact
- Artifact N: next N debuffs applied to the enemy are negated (consumed instead of applying).
- Each debuff application consumes 1 charge: Bash's Vulnerable = 1 charge, Uppercut's Weak + Vulnerable = 2 charges.
- Once all charges are consumed, subsequent debuffs apply normally.
- Strategy: Strip with cheap debuffs (Thunderclap at 1E), then apply real debuffs.

### Barricade (enemy)
- Block does NOT expire at start of enemy's turn. Accumulates.
- Makes enemies effectively much tankier. A 20 HP enemy with 40 block is a 60+ HP enemy.
- Need burst or sustained high damage to break through.

### Mode Shift (Guardian)
- Damage counter in Attack Mode. When enough damage dealt, Guardian switches to Defensive Mode.
- Counter starts at ~27-30, increases each cycle.
- Tracks total HP damage, not damage to block.

### Sharp Hide (Guardian Defensive Mode)
- Deals N damage (N=3 observed) to player per Attack card played.
- Damage applies to block first (if player has block).
- Strategy: Block before playing Attacks, or play only Skills for pure block.

### Flight (Byrds)
- Flight N: all damage halved while N > 0. Each hit decrements Flight by 1.
- Multi-hit attacks strip Flight faster. AOE counts as separate hits per enemy.
- Byrds can regain Flight on buff turns.

### Hex (Chosen debuff)
- When you play a Skill card, a Dazed is added to your draw pile.
- Punishes defensive play. Minimize Skill usage against Chosen.

### Curl Up (Louse passive)
- When first attacked, gains 5-7 block.
- First attack is partially absorbed. Follow up with more attacks same turn.

### Ritual (Cultist)
- Gains +3 Strength per Ritual activation. Permanent and stacking.
- Cultists activate Ritual every turn. Kill fast before damage escalates.
