# Enemies

Enemy mechanics documented from actual runs. Entries cite the run where they were observed.

## Slime Boss

Act 1 boss. HP: ~140 (observed).

- **Pre-split behavior**: Alternates between STRONG_DEBUFF turns (no attack, safe to go all-in) and high-damage ATTACK turns (35 damage observed in Run 1). The debuff turns are safe windows for damage.
- **Split**: When reduced to ~50% HP, Slime Boss splits into Spike Slime (L) and Acid Slime (L). This is the most dangerous part of the fight — you go from one enemy to two, both with significant HP and damage. In Run 4, split triggered when boss hit ~58 HP.
- **Slimed cards**: Both large slimes add Slimed cards to your deck. Slimed is a status card that costs 1 energy and exhausts when played, doing nothing useful. These clog your hand badly — we saw 3 out of 5 cards be Slimed in a single hand.
- **Pre-split strategy**: You want to prepare for the split. Front-loading damage before the split is less important than having the tools to handle two enemies afterward. Use debuff turns to deal damage without blocking.
- **Post-split priority**: After the split, you're fighting two enemies that each attack for 11-16+ damage per turn. AOE or the ability to kill one quickly is critical. Without either, the combined damage overwhelms your block.
- **Post-split debuffs**: Spike Slime (L) applies Frail (block reduced 25%). Acid Slime (L) applies Weak (damage reduced 25%). Getting both debuffs simultaneously is devastating — reduced offense AND defense.
- **What you need**: (1) AOE for split damage. (2) Burst single-target to kill one slime fast. (3) Exhaust tools to handle Slimed cards. (4) Enough block/HP to survive 2-3 turns of combined 25-36 damage.
- **Run 4 victory**: Beat Slime Boss at ~17 HP. Key differences from Run 1 death: (1) Had Thunderclap for mass Vulnerable on split, (2) Had Whirlwind for AOE damage, (3) Used Fiend Fire for burst + Slimed exhaust, (4) Killed attacking slime first while exhausting Slimed on free debuff turns, (5) Spike Slime (L) split into 2x Spike Slime (M) which were easier to clean up. Fight lasted 9 turns. Plated Armor 4 from potion provided passive block every turn.
- Confidence: MEDIUM -> HIGH (2 runs — Run 1 death, Run 4 victory. Pre-split pattern and post-split mechanics well-documented.)

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
- **Run 5 victory**: Beat Guardian at 69/80 HP entry. 15-card deck, 3 upgrades (Bash+, Shrug It Off+, Carnage+). Key plays: (1) Skill Potion -> Impervious on turn 2 for 30 block vs 32 attack. (2) Carnage+ + Headbutt loop dealt 28-42 damage every other turn. (3) Fairy in a Bottle revived on turn 11 after taking 32 damage. (4) Killed turn 12 with Strike at 2 HP remaining on Guardian. Mode Shift confirmed at 30 on cycle 1 (player noted Mode Shift 30->18 after 12 damage turn 1).
- **Winning formula confirmed**: (1) One big block card for 32-damage turn (Impervious ideal). (2) High burst damage for fast Mode Shift triggering (Carnage+ at 28-42). (3) Headbutt for deck manipulation (guarantee Carnage+ draw). (4) Safety net (Fairy in a Bottle).
- Confidence: MEDIUM -> HIGH (3 fights observed — Runs 0 and 5 victories, Run 2 death. Winning formula now identified across 2 victories.)

## Jaw Worm

Act 1 hallway enemy. HP: ~40-44 (estimated from Run 1 — took 4 turns to kill with Strikes and Bash).

- **Turn 1 behavior**: Unknown intent on turn 1 (player hedged with Strike + Defend in Run 1, Defend + 2 Strikes in Run 4). May attack or buff.
- **Buff/defend turn**: Has a turn where it curls up (gains block ~5) and/or buffs strength. This is a safe turn to go all-in on damage.
- **Damage output**: 7 damage (Run 1), 11 damage (Run 4 turn 3 attack). Damage increases over time, possibly from Strength buffs.
- **Strategy**: Apply Vulnerable with Bash on turn 2, then burst damage during buff turns. 4-turn kill typical.
- Run 4: Killed in 4 turns. T1: 5 block + 12 damage. T2: Bash (8+Vuln) + Strike (9 Vuln) = 17. T3: Thunderclap (6 Vuln) + 2 Defends (10 block) vs 11 attack. T4: 2 Strikes (18 Vuln) for kill.
- Confidence: LOW -> MEDIUM (2 fights across Runs 1 and 4, attack patterns partially observed)

## Cultist

Act 1 hallway enemy. HP: ~50 (estimated from Run 1).

- **Turn 1**: Uses Ritual (gains Strength each turn, stacking buff). Does NOT attack turn 1.
- **Ritual stacking**: Gains +3 Strength per Ritual stack. Attacks get progressively more dangerous each turn. Kill fast.
- **Strategy**: Turn 1 is free damage (no attack incoming). Apply Vulnerable with Bash, then burst down. Every turn the fight goes on, the Cultist hits harder.
- Observed: Run 1, floor 7. Killed in 3 turns with Bash + Hemokinesis + Strike.
- Run 4: Floor 1. Killed in 4 turns. T1 (free): Bash (8+Vuln) + Strike (9 Vuln) = 17. T2: 2 Strikes (18 Vuln) + Defend (5 block), took 1 damage. T3: Strike (6) + 3 Defends (15 block), took 0. T4: 2 Strikes (12) for kill. Cultist had 9 damage by turn 2 (Ritual +3 Str, so base 6 + 3 = 9).
- Confidence: MEDIUM (2 fights across Runs 1 and 4, Ritual mechanic confirmed)

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

Medium Spike Slime. HP: ~28 (estimated from Run 1, floor 11 split + floor 14). ~11 HP observed in Run 4 Slime Boss fight (post-split from Spike Slime L).

- **Damage output**: ~8 damage per attack.
- **Debuff turns**: Has turns where it only applies Frail instead of attacking. These are free damage turns.
- **Slimed cards**: Adds Slimed status cards to deck.
- **Split from Large**: Spike Slime (L) splits into 2x Spike Slime (M) when killed (confirmed in Run 4 Slime Boss fight — Spike Slime L was killed and 2x Spike Slime M appeared with ~11 HP each). Also observed in Run 1, floor 11.
- Confidence: LOW -> MEDIUM (split behavior confirmed in Run 4 Slime Boss fight, HP varies by context)

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
- **Run 4 experience**: Fought at 60/79 HP. Used Strength Potion for +2 Str on turn 1 (free BUFF turn). Bash + Iron Wave (both Attacks) for 20 damage turn 1. Turn 2: Thunderclap (Attack, refreshes Vuln) + Strike for 31 damage with Vuln+Str. Turn 3: 3 Strikes for 36 damage (Vuln+Str), killing Nob. Clean 3-turn kill, zero Skills. Took only 14 damage. Strength Potion on turn 1 maximized value since every Attack got +2 damage.
- **Lesson confirmed across 3 runs**: Zero Skills is the correct approach. Run 2 played 3 Skills (+6 Str to Nob), nearly died. Runs 3 and 4 played 0 Skills, clean victories.
- **Run 5 experience**: Fought at 75/80 HP. Zero Skills. Turn 1 (free BUFF): Bash+ (10 dmg + 3 Vuln) + Headbutt (13 dmg Vuln) = 23 damage. Put Bash+ on top of draw. Turn 2: Searing Blow (18 Vuln) + Strike (9 Vuln) = 27 damage. Turn 3: 2 Strikes (18 Vuln). Turn 4: Bash+ (10 Vuln) + Strike (9 Vuln) = 19 for kill. Total 4-turn kill, took ~20 damage (75->~55 HP). Anchor relic + Carnage as elite reward.
- **Lesson confirmed across 4 runs**: Zero Skills is the correct approach. Run 2 played 3 Skills (+6 Str to Nob), nearly died. Runs 3, 4, and 5 played 0 Skills, clean victories.
- Confidence: HIGH (4 fights across Runs 2, 3, 4, and 5 — Run 2 near-death from Skills, Runs 3-5 clean kills from Attacks-only)

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
- **Run 5 improvement**: 7-turn fight (vs 12 in Run 3). Key differences: (1) Carnage+ (28 damage, halved to ~14) nearly one-shot a Byrd turn 1 after Thunderclap stripped 1 Flight + applied Vulnerable. (2) Killed first Byrd turn 2, reducing incoming by 33%. (3) Impervious used turn 2 for massive block safety margin. (4) Dropkick provided free cycling on Vulnerable Byrds. HP cost: ~20 HP (vs 58 HP in Run 3). Dramatically better result from having Carnage+ and better card quality.
- Confidence: MEDIUM (2 fights across Runs 3 and 5, 12-turn and 7-turn experiences. Carnage+ / high burst significantly reduces fight length.)

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

## Centurion + Mystic

Act 2 hallway enemy pair. Centurion HP: ~65 (estimated from Run 4). Mystic HP: ~41 (estimated from Run 4).

- **Mystic heals Centurion**: Mystic heals ~12 HP per turn to Centurion and gains ~15 block. This makes Centurion nearly unkillable while Mystic is alive — you deal 15 damage and it heals back 12.
- **KILL MYSTIC FIRST**: This is the critical rule. If you attack Centurion while Mystic is alive, you're in an unwinnable attrition war. Focus all damage on Mystic despite Centurion being the bigger threat per-turn.
- **Centurion attacks**: 12 damage per attack (observed in Run 4, possibly multi-hit 6x3 based on player reasoning referencing "each 6 becomes floor(6*0.75)=4, x3=12"). Can also attack for 18 (observed when player had 18 incoming).
- **Mystic behavior**: Alternates between heal/buff turns (healing Centurion + gaining block) and other actions. Mystic gains significant block (15 observed) making it tanky despite lower HP.
- **Free turns**: Both enemies can have turns where they defend/buff without attacking. These are critical windows to burst Mystic.
- **Run 4 death**: Player entered at 42/84 HP. Used Whirlwind turn 1 (15 AOE) to damage both. Correctly targeted Mystic with Fiend Fire (burst) and Bash+ (Vuln). Killed Mystic on turn 5 but was at 7 HP by then. Centurion's attacks (12-18 per turn) whittled HP while player focused Mystic. Died turn 8 at 1 HP — couldn't block 18 incoming with only 10 block available.
- **Strategy**: (1) KILL MYSTIC FIRST. (2) Use AOE on turn 1 to damage both while you figure out intents. (3) Save burst damage (Fiend Fire, Whirlwind) for Mystic. (4) Apply Weak to Centurion to reduce incoming while you kill Mystic. (5) Once Mystic is dead, Centurion is a straightforward single-target fight. (6) Enter with 50+ HP — this fight drains HP fast even with correct play.
- Confidence: MEDIUM (2 fights across Runs 4 and 5 — died in Run 4, survived in Run 5 but dropped to 4 HP. See Run 5 update below.)

## Spheric Guardian

Act 2 hallway enemy. HP: ~20 (estimated from Run 4). Extremely tanky despite low HP due to persistent block.

- **Barricade**: Block does NOT expire at start of turn. Block accumulates turn over turn, making the enemy effectively much tankier than its HP suggests.
- **Starting Block**: Starts with 40 block (observed in Run 4). Combined with Barricade, this means you need to deal 40+ damage just to start dealing HP damage.
- **Artifact 3**: Starts with 3 Artifact charges. First 3 debuffs applied are negated. This means Bash's Vulnerable, Uppercut's Weak+Vulnerable, etc. are all wasted on stripping Artifact. Plan 3 "throwaway" debuffs before your real debuffs stick.
- **Frail 5**: Applies Frail 5 to the player. With 5 turns of Frail, block cards give 25% less block for a very long time. Defend goes from 5 to 3.
- **Attacks 10x2**: Deals 10 damage twice per attack turn (20 total). Significant damage when combined with Frail reducing your block.
- **Gains block each turn**: Adds more block each turn on top of Barricade. Block of 46+ observed on turn 2.
- **Strategy**: (1) Strip Artifact first with cheap debuffs (Thunderclap is ideal — 1 energy strips 1 charge from each enemy). (2) Once Artifact is gone, apply Vulnerable for 50% more damage. (3) Use Burning Pact/draw to cycle to high-damage cards. (4) Pen Nib (double damage on 10th Attack) is extremely valuable here. (5) Fiend Fire with hand full of cards can burst through remaining block + HP. (6) This fight is a DPS check — if your deck can't deal 60+ damage fast, you'll take too much from Frail + 10x2 attacks.
- **Run 4 experience**: 6-turn fight. Lost 30+ HP. Player stripped 3 Artifact charges over 3 turns (Uppercut for 2, Bash for 1). Used Pen Nib double-damage Strike (18 damage) + Iron Wave to break through block. Finished with Thunderclap + Fiend Fire. Headbutt was used to place Bash on top of draw pile (excellent for this enemy since you need to find specific cards).
- Confidence: MEDIUM (1 fight in Run 4, mechanics observed but block amounts may vary)

## Sentry

Act 1 elite. HP: ~42 each (estimated from Run 4). Appears as a group of 3.

- **Attack pattern**: Two Sentries attack while one uses a Beam ability (adds Dazed status cards to your deck). The attacking pair rotates each turn.
- **Attack damage**: 9 damage per attacking Sentry (observed in Run 4). With 2 attacking, that's 18 incoming per turn.
- **Dazed cards**: The non-attacking Sentry adds Dazed (Unplayable, Ethereal) status cards to your discard. These clog draws — Run 4 player had 3 Dazed in a 5-card hand on turn 5.
- **Artifact**: Each Sentry starts with Artifact (observed — Thunderclap's Vulnerable was negated). Strips are needed before debuffs stick.
- **Strategy**: (1) AOE is king — Whirlwind for 15 damage to all 3 (45 total) is the best turn 1. (2) Focus fire one Sentry at a time to reduce incoming attack count. (3) Thunderclap strips Artifact + applies Vulnerable once Artifact is gone. (4) Block on turns when 2 Sentries attack (18 damage). (5) Kill them before Dazed cards overwhelm your draws.
- **Run 4 experience**: 7-turn fight. Whirlwind turn 1 for 45 total AOE. Then focused Sentries one at a time. Took ~22 HP damage total (59->37 HP before Burning Blood).
- Confidence: MEDIUM (1 fight in Run 4, mechanics observed)

## Gremlin Leader

Act 2 elite. HP: unknown (high — fight lasted 8 turns before death). Appears with summoned Sneaky Gremlins.

- **Summons Gremlins**: Gremlin Leader summons Sneaky Gremlins (small, ~10-12 HP each). At fight start, 1-2 gremlins may already be present. Leader summons more over time.
- **DEFEND_BUFF (Rally)**: The most dangerous mechanic. When the Leader uses DEFEND_BUFF, it gives ALL enemies (including itself and all gremlins) +3 Strength. This is PERMANENT and STACKING. After 2 rallies, every gremlin attacks for base+6. After 3 rallies, base+9.
- **Strength scaling is the kill condition**: Unlike most enemies where HP is the threat, the Leader's damage scales exponentially with each rally. By turn 8 in Run 5, total incoming damage was 49 (from Leader + 3 gremlins with accumulated Strength). The fight becomes mathematically unwinnable once Strength stacks too high.
- **Gremlin types observed**: Sneaky Gremlins (low HP, attack for ~9 base damage). More types may exist.
- **Run 5 death**: Entered at 11 HP (13% of max). Fight was unwinnable from the start — even with Impervious turn 1 (30 block), Disarm on Leader turn 3 (-2 Str), and Shockwave turn 5 (mass Weak+Vuln), the incoming damage scaled faster than block could handle. By turn 8, 49 incoming damage vs ~21 block = death.
- **Key cards exhausted too early**: Impervious (turn 1), Shockwave (turn 5), Disarm (turn 3), Reaper (turn 6), Carnage+ (played but eventually exhausted via Ethereal), Strikes (exhausted by True Grit+). By late fight, the deck was too thin to generate both damage and block.
- **Strategy**: (1) KILL GREMLINS FIRST. Each dead gremlin is one fewer recipient of rally Strength buffs. (2) AOE is critical — Thunderclap, Whirlwind strip gremlin count fast. (3) Disarm on Leader reduces rally effectiveness but only by 2 Str (rally gives +3 to ALL, not just Leader). (4) DO NOT enter this fight below 50% HP. The Strength scaling means even 80% HP may not be enough. (5) Kill fast — every turn the fight goes on, rally makes it worse. (6) Shockwave is the single best card (mass Weak + Vuln).
- **HP THRESHOLD**: This is the hardest Act 2 elite observed. Entering at 11 HP was suicide. Minimum entry HP should be 60%+ with a strong deck. If HP is below 50%, take any alternative path.
- Confidence: MEDIUM (1 fight in Run 5, died — DEFEND_BUFF +3 Str to all confirmed, exact HP/attack values need more data)

## Snake Plant

Act 2 hallway enemy. HP: ~60-75 (estimated from Run 5 — fight lasted 4 turns with heavy burst).

- **Attack pattern**: Attacks for significant damage. Exact values not recorded (reasoning fields empty in Run 5 log).
- **Weak debuff observed**: Player used Shockwave turn 1 for mass Weak+Vuln, suggesting Snake Plant attacks are dangerous enough to warrant Shockwave.
- **Strategy**: Apply Vulnerable, burst down. Impervious + Dropkick + Carnage+ used in Run 5 to kill in 4 turns.
- Run 5: Fought on floor 23. Shockwave opener, then Impervious for block, Dropkick for cycling, Carnage+ for burst, Bash+ for Vuln refresh, Searing Blow for kill. Took some damage but survived.
- Confidence: LOW (1 fight in Run 5, limited data — reasoning fields were empty)

## Centurion + Mystic (Run 5 Update)

- Run 5: Second encounter. Player entered at unknown HP (higher than Run 4's 42 HP). Fight lasted 12 turns.
- **Headbutt does 9 damage, not 11**: Player's Run 5 reasoning mentioned Headbutt doing 9 damage. Previous Centurion+Mystic entry estimated Mystic HP at ~41. Headbutt left Mystic at 1 HP — Mystic healed back. This suggests Mystic HP may be higher than estimated, or block absorbed more than expected.
- **KILL MYSTIC FASTER**: The 12-turn fight drained massive HP. Key issue: Headbutt (9 dmg) is not enough burst vs Mystic's ~15 block per turn. Need Carnage+ or Searing Blow for burst through block.
- **Correct target priority maintained**: Player correctly focused Mystic with Searing Blow, Headbutt, Carnage+ while using Thunderclap for AOE Vulnerable and Bash+ on Centurion for Weak/damage reduction.
- **Dropped to 4 HP**: Even with correct play, the fight went 12 turns and drained HP to 4. The player survived but entered the next fights critically low.
- Confidence: MEDIUM (2 fights across Runs 4 and 5 — died in Run 4, survived in Run 5 but badly damaged)



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
