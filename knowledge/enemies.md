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

Act 1 boss. HP: 240 (confirmed in Run 2).

- **Mode-switching boss**: The Guardian alternates between Attack Mode and Defensive Mode based on the Mode Shift mechanic.
- **Mode Shift**: In Attack Mode, the Guardian has a Mode Shift counter that tracks damage dealt. When you deal enough total damage to reduce Mode Shift to 0, it switches to Defensive Mode. The counter resets higher each cycle (observed starting at 27 in Run 2, then increasing). Counter increases each cycle, making Defensive Mode harder to trigger later in the fight.
- **Attack Mode intents**: ATTACK (5x4 = 20 damage), ATTACK (32 damage), ATTACK_BUFF (8x2 = 16 damage), DEFEND (gains block, no damage), STRONG_DEBUFF (no damage). The Guardian cycles through these in Attack Mode.
- **Defensive Mode (Sharp Hide)**: Guardian gains Sharp Hide 3 — deals 3 damage to the player every time the player plays an Attack card. Also has its own attack pattern (9 damage, 8x2 = 16). After some turns, switches back to Attack Mode with Mode Shift counter reset (higher than before).
- **Free turns**: DEFEND and STRONG_DEBUFF intents deal no damage — use these to go all-out on damage. BUFF intent in defensive mode is also free.
- **32 damage attack**: The Guardian's biggest single hit. At 3 energy with basic cards, maximum block is ~17-20. This attack can one-shot you if your deck is too thin or if you lack enough block cards.
- **Strategy**: Block on attack turns, damage on free turns. Sharp Hide punishes Attack cards, so during Defensive Mode either (1) block before playing attacks to absorb Sharp Hide damage, or (2) play only Skills for pure block. Need enough block cards to survive 32-damage turns.
- **Run 0 beat this boss** with block+cycle strategy (True Grit+, Shrug It Off+, Pommel Strike).
- **Run 2 died to this boss** at 123/240 HP. Deck was exhausted down to 3 cards (Defend, Iron Wave, True Grit) and could only generate 20 block per turn. The 32-damage attack was unsurvivable. Root cause: over-exhausting with unupgraded True Grit (random exhaust) destroyed key cards.
- Confidence: MEDIUM (2 fights observed — Run 0 victory, Run 2 death. Mode Shift and Sharp Hide mechanics well-documented.)

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

## Lagavulin

Act 1 elite. HP: 110 (confirmed in Run 2).

- **Sleeping phase**: Starts asleep with 8 block per turn. Does not attack while sleeping. Wakes up when attacked OR after 3 turns of sleeping.
- **Debuff turns**: After waking, alternates between attack and debuff. Debuff turn applies -1 Strength and -1 Dexterity (reduces player's attack damage and block gained). These stack and are permanent for the combat.
- **Attack damage**: 18 damage per attack turn (observed in Run 2).
- **Strategy**: Wake it immediately with Bash (Vulnerable helps more than 3 turns of chipping through 8 block). Front-load damage on debuff turns (free turns). Kill before Strength debuffs accumulate — each -1 Strength makes every attack card worse.
- **Run 2 experience**: 7-turn fight. Player correctly woke it turn 1 with Bash, went all-in on free turns. Took 36 HP damage total (82->35 after Burning Blood heal to 35+6=41... actually player ended at 35 HP before Burning Blood). The fight's length caused significant Strength loss (-2 or -3 Strength by end).
- **Math warning**: After multiple debuff turns, recalculate damage. Strike goes from 6 to 5 to 4. Pommel Strike 9 to 8 to 7. Iron Wave 5 to 4 to 3. Plans made with base damage values will overestimate output.
- Confidence: MEDIUM (1 fight in Run 2, mechanics observed)

## Gremlin Nob

Act 1 elite. HP: 85 (observed in Run 2).

- **Enrage**: When the player plays a Skill card, Gremlin Nob gains +2 Strength (permanent). This makes playing Defend, True Grit, or any Skill card actively dangerous — each one makes Nob's attacks hit harder.
- **Turn 1**: Buffs (Skull Bash or similar — gains Vulnerable on player?). No attack turn 1.
- **Attack damage**: Starts at ~14 damage, increases with Enrage stacks. By turn 3 in Run 2, attacks were dealing 21+ damage.
- **CRITICAL RULE**: Do NOT play Skills against Gremlin Nob. Only play Attacks. Powers do NOT trigger Enrage (confirmed in Run 2 — Dark Embrace played without triggering Enrage).
- **Strategy**: All-out Attacks. Kill before Enrage stacks make attacks unsurvivable. Use potions if needed to burst it down. Bash (Attack card) is safe and applies Vulnerable.
- **Run 2 experience**: Player fought at 29 HP. Turn 1: 21 damage with Attacks only. Turn 2: Dark Embrace (Power, safe) + Iron Wave. Turn 3: Snecko Oil for desperate card draw, played 2x True Grit for block (each triggered Enrage +2 Str, making Nob stronger). Used second Snecko Oil turn 4 and killed Nob at 27 HP with Vulnerable Pommel Strike + Strikes. Survived at 3 HP.
- **Lesson from Run 2**: Even when desperate for block, playing Skills feeds Enrage. The player played 2x True Grit (Skills) and a Defend, giving Nob +6 Strength total. With hindsight, those Skills turned a 14-damage attack into a 20+ damage attack.
- Confidence: MEDIUM (1 fight in Run 2, Enrage confirmed, Power-exception confirmed)

## Red Slaver

Act 1 hallway enemy. HP: ~50 (estimated from Run 2, floors 7 and 11).

- **Attack damage**: 12 damage (observed in Run 2, floor 7), 13 damage (floor 11).
- **Debuff turns**: Has turns where it applies Entangle (player cannot play Attack cards for 1 turn?) or other debuffs instead of attacking.
- **Strategy**: Kill fast with Attacks. Apply Vulnerable and burst. Straightforward fight.
- **Run 2**: Fought on floor 7 (3 turns, took 5 damage) and floor 11 (3 turns, deliberately took lethal relying on Fairy in a Bottle revive).
- Confidence: LOW (2 fights, limited data)

## Fungi Beast

Act 1 hallway enemy. HP: ~19 (observed in Run 2, floor 11).

- **Spore Cloud**: On death, applies Vulnerable 2 to the player. This means killing a Fungi Beast makes the player take 50% more damage from surviving enemies.
- **Buff turns**: Has turns where it buffs (gains Strength?) instead of attacking. These are free damage turns.
- **Attack damage**: ~9 damage per attack (inferred from Run 2 calculation: "floor(9*1.5)-5=8" implies 9 base attack).
- **Strategy**: Kill one at a time, but be aware that Spore Cloud Vulnerable applies after the kill. Block accordingly on the turn you expect to kill one. In multi-Fungi fights, kill when the other Fungi is NOT attacking.
- **Run 2**: Fought 2x Fungi Beasts at floor 11 at 9 HP. Player used True Grit exhaust engine (Charon's Ashes 3 AOE damage). Survived at 1 HP. Spore Cloud Vulnerable was correctly accounted for: player blocked to absorb the Vulnerable-boosted attack.
- Confidence: LOW (1 fight in Run 2)

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
