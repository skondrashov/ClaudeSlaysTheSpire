# Enemies

Enemy mechanics documented from actual runs. Entries cite the run where they were observed.

## Slime Boss

Act 1 boss. HP: ~140 (observed).

- **Pre-split behavior**: Has debuff-only turns (no attack) alternating with high-damage attacks (35 damage observed in Run 1). The debuff turns are safe windows for damage.
- **Split**: When reduced to ~50% HP, Slime Boss splits into Spike Slime (L) and Acid Slime (L). This is the most dangerous part of the fight — you go from one enemy to two, both with significant HP and damage.
- **Slimed cards**: Both large slimes add Slimed cards to your deck. Slimed is a status card that costs 1 energy and exhausts when played, doing nothing useful. These clog your hand badly — we saw 3 out of 5 cards be Slimed in a single hand.
- **Pre-split strategy**: You want to prepare for the split. Front-loading damage before the split is less important than having the tools to handle two enemies afterward. Use debuff turns to deal damage without blocking.
- **Post-split priority**: After the split, you're fighting two enemies that each attack for 11-16+ damage per turn. AOE or the ability to kill one quickly is critical. Without either, the combined damage overwhelms your block.
- **Post-split debuffs**: Spike Slime (L) applies Frail (block reduced 25%). Acid Slime (L) applies Weak (damage reduced 25%). Getting both debuffs simultaneously is devastating — reduced offense AND defense.
- **What you need**: (1) AOE for split damage. (2) Burst single-target to kill one slime fast. (3) Exhaust tools to handle Slimed cards. (4) Enough block/HP to survive 2-3 turns of combined 25-36 damage.
- Confidence: MEDIUM (1 run observed, died to this boss — detailed fight data from Run 1)

### Spike Slime (L)
- Attacks for ~16 damage
- Applies Frail (reduces block gained from cards by 25%)
- Adds Slimed cards to deck
- **May split into medium slimes**: On floor 11 (Run 1), a Spike Slime (L) fight ended with Spike Slime (M) enemies appearing. The large slime likely splits when reduced to low HP, similar to Slime Boss splitting. This extends the fight significantly.
- Confidence: MEDIUM (observed in Run 1, split behavior needs confirmation)

### Acid Slime (L)
- Attacks for ~11-12 damage
- Applies Weak (reduces your attack damage by 25%)
- Has its own Split ability — can split into smaller slimes
- Adds Slimed cards to deck
- Confidence: MEDIUM (observed in Run 1)

## The Guardian

Act 1 boss. HP: unknown exact, but was at 34 HP mid-fight in Run 0.

- **Mode-switching boss**: The Guardian alternates between offensive and defensive modes. In one mode it attacks, in the other it uses debuffs/other intents.
- **Debuff turns**: The Guardian has turns where its intent is "debuff" rather than attack. These turns are safe windows to play damage without blocking.
- **Damage output**: At least 20 and 32 damage observed in different turns (Run 0). Can hit very hard.
- **Strategy**: The Guardian fight is about managing its offensive/defensive cycles. Block on attack turns, damage on debuff turns. The Run 0 player did this successfully with block cards (Shrug It Off+, True Grit+) and burst damage (Pommel Strike).
- **Run 0 beat this boss.** The deck had: Shrug It Off+, True Grit+, Pommel Strike, plus unknown other cards. The exhaust + block + cycle package worked well. The fight ended with the Guardian at 2 HP, killed by Pommel Strike.
- Confidence: LOW (only 1 fight observed, log is partial — only last few turns visible)

## Jaw Worm

Act 1 hallway enemy. HP: ~40-44 (estimated from Run 1 — took 4 turns to kill with Strikes and Bash).

- **Turn 1 behavior**: Unknown intent on turn 1 (player hedged with Strike + Defend). May attack or buff.
- **Buff/defend turn**: Has a turn where it curls up (gains block) and/or buffs strength. This is a safe turn to go all-in on damage.
- **Damage output**: 7 damage observed (Run 1, turn 2).
- **Strategy**: Apply Vulnerable with Bash, then burst damage during buff turns. Straightforward fight.
- Confidence: LOW (1 fight observed, incomplete data)

## Cultist

Act 1 hallway enemy. HP: ~50 (estimated from Run 1).

- **Turn 1**: Uses Ritual (gains Strength each turn, stacking buff). Does NOT attack turn 1.
- **Ritual stacking**: Gains +3 Strength per Ritual stack. Attacks get progressively more dangerous each turn. Kill fast.
- **Strategy**: Turn 1 is free damage (no attack incoming). Apply Vulnerable with Bash, then burst down. Every turn the fight goes on, the Cultist hits harder.
- Observed: Run 1, floor 7. Killed in 3 turns with Bash + Hemokinesis + Strike.
- Confidence: MEDIUM (1 fight, but Ritual mechanic is well-known)

## Louse (Small / Generic)

Act 1 hallway enemy. HP: ~11-17 (varies).

- **Curl Up**: Has a passive that gives it block when first attacked. Observed as 5-7 block in Run 1.
- **Damage output**: ~5-7 damage per attack.
- **In groups**: 2-3 Louses together. Combined damage adds up. Focus fire to reduce enemy count.
- Observed: Run 1, floors 3 and 10.
- Confidence: MEDIUM (seen in multiple fights in Run 1)

## Looter

Act 1 hallway enemy. HP: ~44-48 (estimated from Run 1).

- **Steals gold**: Steals 15 gold per turn (observed in Run 1 — player recovered 45 stolen gold after 3 turns of stealing).
- **Damage output**: 10+ damage per attack.
- **Escape**: May try to escape after stealing enough gold.
- **Strategy**: Kill fast to minimize gold theft. Prioritize over non-stealing enemies in multi-enemy fights.
- Observed: Run 1, floor 14 (paired with Spike Slime M).
- Confidence: LOW (1 fight observed)

## Spike Slime (M)

Medium Spike Slime. HP: ~28 (estimated from Run 1, floor 11 split + floor 14).

- **Damage output**: ~8 damage per attack.
- **Debuff turns**: Has turns where it only applies Frail instead of attacking.
- **Slimed cards**: Adds Slimed status cards to deck.
- **Split from Large**: Spike Slime (L) splits into medium slimes when killed or at low HP (observed in Run 1, floor 11 — fight started with Spike Slime (L) and later showed Spike Slime (M) enemies).
- Confidence: LOW (limited data, split behavior needs confirmation)

## General Notes

### Frail
- Reduces block gained from cards by 25%. This is multiplicative with the card's block value.
- Defend gives 5 base → 3 when Frail (observed in Run 1, Defend giving only 3 block)
- Shrug It Off gives 8 base → 6 when Frail
- Frail is extremely punishing when fighting multiple enemies because you need more block total but each block card gives less
- Confidence: HIGH (game mechanic, observed consistently in Run 1)

### Weak
- Reduces attack damage dealt by the affected entity by 25%
- Formula: floor(base_damage * 0.75)
- When applied to enemies (via Clothesline, Shockwave): reduces THEIR attacks by 25%. Very valuable survivability tool.
- When applied to yourself (via enemy debuffs): reduces YOUR Strikes/attacks by 25%. Strike goes from 6 to floor(6*0.75) = 4.
- Direction matters: Weak on the ENEMY reduces incoming damage. Weak on YOU reduces outgoing damage. Don't confuse with Vulnerable.
- Confidence: MEDIUM (observed in Run 1 — Clothesline applied Weak to enemies, player was Weakened by slimes)

### Vulnerable
- The Vulnerable entity takes 50% more damage from attacks
- Formula: floor((base + strength) * 1.5)
- When applied to enemies (via Bash, Shockwave): YOUR attacks deal 50% more to them. Strike 6 -> 9.
- When applied to yourself (via Berserk, enemy abilities): ENEMY attacks deal 50% more to you. An attack that would deal 20 hits you for 30.
- Direction matters: Vulnerable on the ENEMY = you deal more damage. Vulnerable on YOU = you take more damage. The player in Run 1 confused Vulnerable with Weak — they are different debuffs.
- Self-Vulnerable (from Berserk) is extremely dangerous against multiple enemies — the 50% bonus applies to ALL incoming attacks.
- Confidence: MEDIUM (observed in Run 1 — Bash applied to enemies, Berserk applied to self. Math verified: Strike 6 * 1.5 = 9 damage observed.)
