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
- **Run 3 experience**: Fought at 72/80 HP. Player correctly played zero Skills. Turn 1: Pommel Strike + 2x Strike (21 damage) while Nob buffed. Turn 2: Flex Potion (+2 Str) + Bash+ (12 dmg, 3 Vuln) + Iron Wave+ (dealt damage + provided block). Turn 3: 1 Strike (9 w/Vuln). Turn 4: Pommel Strike + Strike for exact lethal (22 damage vs 22 HP). Clean 4-turn kill. Took ~9 damage total. Vastly better than Run 2 (survived at 3 HP).
- **Lesson confirmed across runs**: Zero Skills is the correct approach. Run 2 played 3 Skills (+6 Str to Nob), nearly died. Run 3 played 0 Skills, clean victory.
- Confidence: HIGH (2 fights across Runs 2 and 3 — Run 2 near-death from Skills, Run 3 clean kill from Attacks-only)

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

## Hexaghost

Act 1 boss. HP: 250 (confirmed in Run 3).

- **Turn 1**: Does NOT attack. Intent shown as UNKNOWN. Safe to set up (play Thunderclap for Vulnerable, play damage cards). Pantograph heals to full at the start of boss fights, so even low HP entry is compensated.
- **Big attack (Inferno)**: 7x6 = 42 damage. This is multi-hit, meaning each hit is checked against block individually. Weak reduces each hit: floor(6*0.75)=4 per hit = 28 total with Weak. This is the most dangerous attack.
- **Burn cards**: Hexaghost adds Burn status cards to your deck on certain turns (ATTACK_DEBUFF intent). Burns deal 2 damage at end of turn if they are in your hand (they are Unplayable — you cannot play them, they just sit in hand and deal damage). Burns clog your hand (fewer real cards) AND deal damage. Over time, Burns accumulate and drain HP through attrition.
- **DEFEND_BUFF turns**: Hexaghost gains block and Strength. No attack. Free turns for damage. However, the Strength gain makes subsequent attacks stronger.
- **Low damage turns**: Some turns deal only 4-8 damage. Use these to set up (play Metallicize, refresh Vulnerable with Bash+).
- **Medium attack turns**: 14 and 24 damage observed on attack turns that are not the big Inferno.
- **Block**: Hexaghost can gain block (12 block observed). Plan damage accordingly — don't assume all damage goes to HP.
- **Fight length**: ~13 turns observed in Run 3. Long fight. Metallicize and Strength scaling pay off massively.
- **Strategy**: (1) Use turn 1 to set up — Thunderclap for Vulnerable, play damage. (2) Save Shockwave for the first Inferno turn to apply Weak and reduce 42 to ~28. (3) Play Metallicize early for cumulative block value. (4) Reapply Vulnerable with Bash+ on DEFEND_BUFF (free) turns. (5) Manage Burns — they deal end-of-turn damage and reduce effective hand size.
- **Run 3 experience**: Beat Hexaghost at 250 HP, survived at 1 HP. Used Shockwave + Regen Potion to survive first Inferno. Metallicize 3 provided passive block. Burns accumulated and nearly killed the player on late turns. Pantograph relic healed from 56 to 80 HP at fight start.
- Confidence: MEDIUM (1 fight in Run 3, survived at 1 HP — detailed turn-by-turn data)

## Byrd

Act 2 hallway enemy. Appears in groups of 3. HP: ~25-30 per Byrd (estimated).

- **Flight**: Byrds have the Flight mechanic. Flight N means damage is halved (rounded down?) and Flight decrements by 1 each time the Byrd is hit. Once Flight reaches 0, all damage goes through normally. Flight resets after some turns (Byrds "take flight" again).
- **Flight interaction with damage**: With Flight 3 and a 9-damage Strike: damage is halved to ~4-5. Each hit also reduces Flight by 1. So hitting a Byrd 3 times (3 separate attacks) reduces Flight from 3 to 0, then subsequent attacks deal full damage.
- **Multi-hit matters**: Cards that hit multiple times (like Thunderclap hitting all enemies) each reduce Flight by 1. AOE is especially valuable because it strips Flight from multiple Byrds simultaneously.
- **Buff turns**: Byrds have turns where they buff (gain Strength) instead of attacking. Free damage turns.
- **Attack damage**: Individual Byrd attacks: ~5-10 damage each. But with 3 Byrds, combined incoming can be 15-36+ damage per turn, especially after Strength buffs.
- **Fight duration**: Extremely long. Run 3 Byrd fight lasted 12 turns. This is a massive HP drain — player went from 80 HP (post-Burning Blood) to 22 HP.
- **Strategy**: (1) Use Thunderclap to strip Flight from all Byrds and apply Vulnerable simultaneously. (2) Focus fire one Byrd at a time — reducing from 3 to 2 enemies is the biggest damage reduction. (3) Once Flight is at 0, burst with Vulnerable attacks to kill. (4) Metallicize is critical for the long fight — passive block every turn. (5) Consider using Reaper mid-fight for healing sustain.
- **CRITICAL WARNING**: This fight is an HP sponge. Even with good play, expect to lose 40-60 HP. If entering Act 2 with low HP, Byrds can end the run through sheer attrition. Prioritize healing before Act 2.
- Confidence: MEDIUM (1 fight in Run 3, 12 turns of detailed data, Flight mechanic observed but exact formula uncertain)

## Chosen

Act 2 hallway enemy. HP: ~95 (estimated from Run 3).

- **Hex**: On certain turns, the Chosen applies Hex to the player. Hex adds a Dazed status card to your draw pile every time you play a Skill card. This means Defend, Shrug It Off, True Grit, Shockwave, etc. all add a dead card to your deck. Over time, this clogs your draws badly.
- **Weakened**: The Chosen applies Weak to the player, reducing attack damage by 25%. With Weak, Strike goes from 6 to floor(6*0.75)=4 damage. With +2 Strength and Weak, Strike does floor((6+2)*0.75)=6.
- **Strength gain**: The Chosen gains +3 Strength over the course of the fight (exact timing unconfirmed). This makes its attacks escalate from ~13 to ~16+ damage.
- **Debuff-only turns**: Has turns where it only applies debuffs (Hex or Weak), no attack. These are free damage turns.
- **Attack damage**: Base ~13, scaling to 16+ with Strength buffs. Late-fight attacks can hit for 36+ if combined with player Vulnerable.
- **CRITICAL INTERACTION**: Hex punishes Skill-heavy play. Every Defend you play adds a Dazed card. This means blocking is actively costly. Attack-heavy decks handle Chosen much better. Ironclad with Inflame + Strikes (all Attacks) is naturally suited, but if you need to play Defends to survive, each one dilutes your deck.
- **Death scenario (Run 3)**: Player entered at 28 HP. Dealt 77 damage in 5 turns but couldn't finish the last 6 HP because Weakened reduced Strikes from 6 to 4 damage (without Strength) or 6 (with +2 Strength). The critical error was playing a Defend card targeting Chosen (deals 0 damage) instead of a third Strike, wasting 1 energy and adding a Dazed from Hex.
- **Strategy**: (1) Minimize Skill usage to avoid Hex/Dazed clogging. (2) Front-load damage with Attacks. (3) Apply Vulnerable early (Bash+ is an Attack, safe from Hex). (4) Inflame for Strength helps overcome the Weakened penalty. (5) Kill before Strength buffs make attacks lethal.
- Confidence: MEDIUM (1 fight in Run 3, died to this enemy, mechanics partially observed)

## General Notes

### Frail
- Reduces block gained from cards by 25%. This is multiplicative with the card's block value.
- Defend gives 5 base → 3 when Frail (observed in Run 1, Defend giving only 3 block)
- Shrug It Off gives 8 base → 6 when Frail
- Frail is extremely punishing when fighting multiple enemies because you need more block total but each block card gives less
- Confidence: HIGH (game mechanic, observed consistently in Run 1)

### Weak
- Reduces attack damage dealt by the affected entity by 25%
- Formula: floor((base_damage + strength) * 0.75) — Strength is added BEFORE the Weak multiplier is applied
- When applied to enemies (via Clothesline, Shockwave): reduces THEIR attacks by 25%. Very valuable survivability tool.
- When applied to yourself (via enemy debuffs): reduces YOUR Strikes/attacks by 25%. Strike goes from 6 to floor(6*0.75) = 4. With +2 Strength: floor((6+2)*0.75) = floor(6.0) = 6.
- Direction matters: Weak on the ENEMY reduces incoming damage. Weak on YOU reduces outgoing damage. Don't confuse with Vulnerable.
- **Run 3 confirmation**: Player was Weakened by Chosen and had +2 Strength from Inflame. Strikes dealt floor((6+2)*0.75) = 6 damage each. 2 Strikes dealt exactly 12 damage (Chosen 18->6 HP). Formula confirmed: Strength is added to base BEFORE Weak multiplier.
- Confidence: HIGH (confirmed in Runs 1, 3 — formula with Strength verified in Run 3)

### Vulnerable
- The Vulnerable entity takes 50% more damage from attacks
- Formula: floor((base + strength) * 1.5)
- When applied to enemies (via Bash, Shockwave): YOUR attacks deal 50% more to them. Strike 6 -> 9.
- When applied to yourself (via Berserk, enemy abilities): ENEMY attacks deal 50% more to you. An attack that would deal 20 hits you for 30.
- Direction matters: Vulnerable on the ENEMY = you deal more damage. Vulnerable on YOU = you take more damage. The player in Run 1 confused Vulnerable with Weak — they are different debuffs.
- Self-Vulnerable (from Berserk) is extremely dangerous against multiple enemies — the 50% bonus applies to ALL incoming attacks.
- Confidence: MEDIUM (observed in Run 1 — Bash applied to enemies, Berserk applied to self. Math verified: Strike 6 * 1.5 = 9 damage observed.)
