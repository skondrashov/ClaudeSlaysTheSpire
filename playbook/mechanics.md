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
- When on enemies (from Shockwave, Clothesline, Intimidate): THEIR attacks deal 25% less. YOUR attacks are UNAFFECTED.
- When on YOU (from enemy debuffs like Acid Slime Corrosive Spit): YOUR attacks deal 25% less.
- Direction matters: Weak on enemy = they deal less, you deal normal. Weak on you = you deal less.
- **CRITICAL: Applying Weak to enemies does NOT reduce YOUR damage.** After playing Shockwave or Intimidate, your attacks deal FULL damage. The 0.75 multiplier applies ONLY to the Weakened entity's own attacks. Do not apply 0.75 to your own damage calculations when enemies are Weakened -- this is a recurring prediction error that causes underestimation of player damage output.

### Frail
- Block gained from cards is reduced by 25%.
- Duration: N turns, decrements at start of your turn.
- Math: `floor(block * 0.75)`. Defend 5 -> 3. Shrug It Off 8 -> 6.
- Extremely punishing against multiple enemies where you need more total block but each block card gives less.

### Strength
- Each point of Strength adds 1 damage to every Attack card played.
- Permanent within combat (unless modified by Disarm or enemy debuffs).
- **RESETS BETWEEN COMBATS.** Strength from Inflame, Spot Weakness, Demon Form, and Strength Potion does NOT carry over to the next fight. Only relic Strength (Vajra +1) persists. At the start of each new combat, Strength is 0 (plus relic bonuses). This is a confirmed recurring error -- the player has carried Strength values from previous fights into new fight calculations, overestimating damage.
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
- Plated Armor decreases by 1 each time you take unblocked HP damage (damage that gets through block). Multiple hits in one attack (e.g., Book of Stabbing 7x4) each count separately -- if block runs out mid-attack, each subsequent hit that deals HP damage reduces Plated Armor by 1. Plated Armor from multiple sources stacks additively (e.g., two Plated Armor 3 = 6 block/turn).
- Flame Barrier / Thorns: Counter damage triggers AFTER each individual hit that strikes you (whether blocked or hitting HP). Against multi-hit attacks, counter fires once per hit. Example: Book of Stabbing 7x4 with Flame Barrier+ active = 4 triggers of 6 counter damage = 24 total counter damage dealt to the attacker. Counter damage ignores the attacker's block -- it deals direct HP damage. Flame Barrier's block is applied once at play time and absorbs across all hits; the counter triggers per hit regardless of whether the hit was blocked or not.
- Pen Nib: Tracks total Attack cards played across ALL combats. Every 10th Attack card deals double damage. The counter persists between fights and does NOT reset. The counter is visible on the relic tooltip. Track it by counting Attack card plays (Strikes, Bash, Rampage, Cleave, Immolate, etc. -- any card with the Attack type). Skills and Powers do not increment the counter. Double Tap causes the repeated attack to count as a separate play for Pen Nib.

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
- Bottled Flame relic makes a chosen Attack card Innate (always in opening hand). Best target: Bash+ for guaranteed turn 1 Vulnerable.

### Retain
- Retained cards stay in hand at end of turn instead of being discarded.
- Not observed frequently in current card pool.

---

## Card Index Shifting (CRITICAL — RECURRING FATAL ERROR)

When you play a card by numeric index, all cards after it shift down by 1. This means multi-card commands using numeric indices will play WRONG CARDS if the indices aren't adjusted for each prior play.

**Example:** Hand is [1]Strike [2]Defend [3]Bash [4]Iron Wave [5]Fiend Fire
- You plan: "play 3 0; play 5 0" (Bash, then Fiend Fire)
- After Bash plays, hand becomes: [1]Strike [2]Defend [3]Iron Wave [4]Fiend Fire
- "play 5 0" now targets NOTHING (only 4 cards) or errors
- "play 4 0" would hit Fiend Fire (the correct adjusted index)

**THE FIX: USE CARD NAMES, NOT NUMBERS.**
- "play Bash 0; play Fiend Fire 0" always works regardless of shifting
- Card names are resolved against the current hand at execution time
- This eliminates the entire class of index shift errors

**KNOWN KILLS FROM THIS BUG:**
- Played Defend instead of Strike due to shift. Chosen survived at 6 HP, killed player next turn.
- Final turn planned Fiend Fire (would have killed Cultist for 39 damage) but index shift caused Strike to play instead (only 12 damage). Could not kill second Cultist, died next turn.
- Bought Sever Soul instead of Flame Barrier at shop due to index confusion. Sever Soul then exhausted 2 Defend cards during Guardian fight, directly reducing survivability.
- Throughout an entire run, consistently played Defends when intending Strikes and vice versa due to numeric index usage. Four confirmed deaths caused by this bug across multiple runs.

**RULE: NEVER use numeric indices in multi-card turn commands. Always use card names.** The only exception is when two copies of the same card are in hand and you need a specific one — in that case, use the index for ONLY that card and names for everything else.

**THIS ALSO APPLIES TO SHOP PURCHASES.** Use card names when buying from shops, not numeric indices. Index confusion at shops has caused purchasing the wrong card, which cascaded into a boss death.

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
- **Draw pile reshuffle**: When a draw effect triggers and the draw pile is empty, the discard pile is shuffled and becomes the new draw pile. This happens mid-turn if a card draw (Pommel Strike, Flash of Steel, Shrug It Off) triggers with an empty draw pile. This means playing draw cards late in a turn can effectively cycle through the entire deck.

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
- Counter values by cycle: 30 (first), 40 (second), 50 (third).
- Tracks total HP damage, not damage to block.
- Triggering Mode Shift mid-attack CANCELS the current attack -- this is the primary defensive tool against the 32-damage and 5x4=20 attacks.

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

### Malleable (Snake Plant)
- Gains increasing block each time it is attacked within a single turn.
- First attack in a turn: gains ~3 block. Subsequent attacks in the same turn: gains more block (amount increases).
- Resets at the start of each turn.
- Counter-strategy: Use one large hit per turn instead of multiple small hits. Rampage (40+ damage) is better than Whirlwind (5 per hit, each triggering more Malleable block).
- Applies to Snake Plant in Act 2.
