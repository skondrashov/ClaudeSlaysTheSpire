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
- **Run 8 victory**: Beat Slime Boss (floor 13). Deck included Shockwave+, Feed, Seeing Red+, Power Through, Reaper, Thunderclap, Pommel Strike+, Bash+. Feed killed Spike Slime during split phase for +3 Max HP. Used Shockwave+ for mass Weak+Vuln on split. This is the second successful Slime Boss kill.
- Confidence: HIGH (3 runs — Run 1 death, Run 4 victory, Run 8 victory. Pre-split pattern and post-split mechanics well-documented.)

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
- **Run 6 victory**: Beat Guardian at 10 HP. Entered at 67/80 HP after resting. Deck had Metallicize x2, Headbutt+, Pommel Strike+, Bash+, Thunderclap+, Intimidate, Letter Opener relic. Key plays: (1) Double Metallicize setup turn 1 (6 block/turn for rest of fight). (2) Intimidate (0E, Weak ALL) reduced 32-damage turn to 24. (3) Snecko Oil potion on a critical turn gave 0-cost Strikes and Pommel Strike+ for massive free damage. (4) Letter Opener relic dealt 5 damage whenever a Skill was played — significant chip damage over 12+ turns. (5) 0-cost cards from Snecko Oil dealt 18+ damage in free hits during Defensive Mode. Final kill: all-in with Bash+ Vuln + 3 free Strikes (9 each Vuln) for 37 damage, reducing Guardian from 44 to 0. Survived at 10 HP.
- **Third victory formula**: Double Metallicize (6/turn passive block) + Headbutt+ loop (guaranteed draw manipulation) + Snecko Oil (free cards for burst). The double Metallicize is the standout — 6 block/turn handles many attack patterns without spending cards.
- Confidence: HIGH (4 fights — Runs 0, 5, 6 victories, Run 2 death. Winning formula well-established: burst damage + big block source for 32-damage turn + passive block for sustain.)

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

### 3 Cultists (Act 2 hallway fight)

Act 2 multi-enemy fight. 3 Cultists, each with Ritual 3.

- **Turn 1**: ALL three use Ritual (free turn — 0 damage incoming). This is the ONLY free turn.
- **Damage escalation**: Each Cultist gains +3 Str per turn. With 3 Cultists, that's +9 total Str per turn across all enemies. By turn 4, each Cultist attacks for ~15 damage (base 6 + 3*3 = 15). By turn 6, each attacks for ~21 (base 6 + 3*5 = 21). Combined damage from 2 surviving Cultists on turn 7: ~42 damage.
- **This is one of the fastest-scaling fights in the game.** Unlike Gremlin Leader (where Rally gives +3 to ALL enemies periodically), Cultists EACH independently gain +3 Str EVERY turn. The damage ramp is steeper than any other observed enemy.
- **Kill order matters**: Focus fire on one Cultist at a time. Each dead Cultist removes one source of scaling damage. Going from 3 to 2 Cultists removes 33% of incoming damage AND one scaling threat.
- **Shockwave+ timing is CRITICAL**: In Run 8, Shockwave+ was saved until turn 4. By then, each Cultist was already attacking for 15+. Shockwave+ should be played turn 2 (first attack turn) to reduce damage during the critical turns 2-4 when you're killing the first Cultist.
- **Damage timeline (observed Run 8)**:
  - Turn 1: 0 incoming (all Ritual)
  - Turn 2: ~9 each = ~27 total (3 Cultists)
  - Turn 3: ~12 each = ~36 total (3 Cultists) or ~24 (2 Cultists)
  - Turn 4: ~15 each (with Weak from Shockwave: ~11 each)
  - Turn 7: ~21 each (1 surviving Cultist: 21, with only 10 block = dead)
- **Run 8 death**: Entered at 37/95 HP with 0 potions. Turn 1 free — used Cleave + Pommel Strike for AOE damage. Played Reaper turn 2 for healing. Killed first Cultist turn 3 with Seeing Red+ + Thunderclap + Bash+ + Strike. Played Shockwave+ turn 4 (TOO LATE — already taken massive damage). Killed second Cultist turn 6 with Feed (+3 Max HP). Died turn 7 — last Cultist attacked for 15, player had only 10 block at 1 HP.
- **What went wrong**: (1) Shockwave+ delayed to turn 4 instead of turn 2. (2) Entered at 37/95 HP (39%) — too low for this fight. (3) Zero potions available. (4) Reaper on turn 2 was correct for healing but didn't deal enough damage to shorten the fight.
- **Correct strategy**: (1) Turn 1 (free): AOE damage + Vulnerable setup. (2) Turn 2: Shockwave+ IMMEDIATELY for mass Weak + Vuln. (3) Turns 2-4: Focus fire one Cultist to death as fast as possible. (4) Turns 4-6: Kill second Cultist. (5) One remaining Cultist is manageable even at high Str.
- **HP threshold**: Enter with 50%+ HP minimum. At 39% HP, the fight was unwinnable even with Shockwave+ and Reaper available.
- Confidence: MEDIUM (1 fight in Run 8, died — damage scaling confirmed, Shockwave+ timing lesson clear)

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
- **Run 6 experience**: 7-turn fight. Player entered at ~66 HP. Opened with Metallicize + Bash+ (woke Lagavulin immediately). Used Weak Potion to reduce 18 damage to 13. Headbutt+ Vuln dealt 18 damage. Pommel Strike+ Vuln dealt 15. Used Headbutt+ to put Bash+ on top for Vuln refresh. Kill on turn 7 with Headbutt+ Vuln (16 damage at -1 Str) + Thunderclap+ (8 kills). Took ~20 HP damage (66->~46 before Burning Blood). Much cleaner than Run 2 thanks to Headbutt+ deck manipulation and Metallicize passive block.
- **Headbutt+ with Lagavulin Str debuff**: At -1 Strength, Headbutt+ does floor((12-1)*1.5) = 16 damage with Vulnerable. The Strength debuffs compound: plan around reduced damage values.
- Confidence: MEDIUM -> HIGH (2 fights across Runs 2 and 6, mechanics well-documented, Weak Potion strategy confirmed effective)

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
- **Run 7 DEATH**: Ironclad A0, died floor 16 to Hexaghost. This was a REGRESSION after 3 consecutive Act 1 boss victories (Runs 4, 5, 6).
  - **Entry HP**: ~50/80 HP. No Pantograph relic to heal to full. Low HP entry without mass Weak for Inferno was fatal.
  - **Deck**: Bash+, Twin Strike, Iron Wave, Pommel Strike+, Thunderclap, Brutality, Shrug It Off, Ghostly Armor + starters. 14 cards. NO Shockwave, NO Metallicize, NO mass Weak source.
  - **Brutality self-damage**: Brutality (Power, 0E, draw 1 extra card/turn, lose 1 HP/turn) was played early. The 1 HP/turn self-damage compounded with Burns (2-4 HP/turn from unplayable Burn cards). By turn 6+, player was losing 3-5 HP/turn from Brutality + Burns alone.
  - **No Weak for Inferno**: The 7x6=42 Inferno attack hit for full damage. Without Shockwave, Clothesline, or any Weak source, there was no way to reduce this multi-hit attack. This is the #1 lesson: Weak is MANDATORY for Hexaghost.
  - **Burns attrition**: Burns accumulated over 9 turns, dealing end-of-turn damage and clogging hand (fewer real cards drawn = fewer block cards). Combined with Brutality's 1 HP/turn, the attrition was overwhelming.
  - **Scrap Ooze event**: Lost 25 HP total to Scrap Ooze event (3 HP per attempt, no relic found). This meant entering the boss at ~50 HP instead of ~75 HP. The event was a trap at that HP level.
  - **Death**: Turn 9, Hexaghost at 61 HP remaining. Player could not survive combined Inferno + Burns + Brutality damage.
  - **What was missing vs Run 3 victory**: (1) No Pantograph to heal to full at boss start. (2) No Shockwave/Weak for Inferno (Run 3 used Skill Potion -> Shockwave). (3) No Metallicize for passive block. (4) Brutality was actively harmful (self-damage in a long fight). (5) Scrap Ooze wasted 25 HP that Run 3 didn't lose (Run 3 got Lantern from Scrap Ooze on first try for only 3 HP).
- **CRITICAL LESSON from Run 7**: Hexaghost WITHOUT Weak is near-unwinnable. The 42-damage Inferno multi-hit cannot be fully blocked without Impervious. Weak reduces it to 28, which is survivable. If your deck has NO Weak source (Shockwave, Clothesline, Intimidate, Weak Potion), do NOT fight Hexaghost at low HP. Pantograph makes HP entry irrelevant, but without Pantograph, you need 70%+ HP AND Weak.
- Confidence: MEDIUM -> HIGH (2 fights — Run 3 victory at 1 HP, Run 7 death at 61 HP remaining. Weak is confirmed mandatory. No-Weak + low HP + Brutality self-damage = guaranteed death.)

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
- **Run 6 update**: 10-turn fight (3 Byrds). Player entered at ~61 HP. Used Thunderclap+ for AOE + Vuln + Flight stripping. Feed killed Byrd 1 on turn 4 for +3 max HP (80->83). Blood Potion used mid-fight (healed 16 HP). Exited at ~19 HP + Burning Blood = 25 HP. HP cost: ~36 HP. Without Carnage+ (which Run 5 had), the fight reverted to a slow attrition grind. Feed as a kill card was clever — combining damage with max HP gain.
- Confidence: MEDIUM -> HIGH (3 fights across Runs 3, 5, and 6. Fight length: 12, 7, 10 turns. Carnage+ dramatically shortens the fight. Without it, expect 10+ turns and 36-58 HP lost.)

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
- **Run 6 update**: Third encounter. Player entered at 25 HP (after Fairy revive from Byrd fight). Correctly killed Mystic first using Bash+ Vuln + Pommel Strike+ + Headbutt+ + Thunderclap+. Killed Mystic in ~6 turns. Double Metallicize (6 block/turn) kept player alive vs Centurion. Fairy in a Bottle consumed during this fight (player deliberately took 24 damage with only 6 Metallicize block, knowing Fairy would revive at ~24 HP). After Mystic died, used Feed to kill Centurion for +3 max HP. Exited fight at ~5 HP + Burning Blood = ~11 HP.
- **Lesson confirmed across 3 runs**: Kill Mystic first is absolutely correct and was executed well in Run 6. But the fight STILL drains massive HP (25->~5 even with correct play and double Metallicize). The double Metallicize (6 block/turn) is a significant upgrade over single (3/turn) and was critical for surviving.
- Confidence: MEDIUM -> HIGH (3 fights across Runs 4, 5, and 6 — died in Run 4, survived in Runs 5 and 6 but badly damaged both times. Kill Mystic first confirmed as correct strategy.)

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

## Centurion + Mystic (Run 5 and 6 Updates)

- Run 5: Second encounter. Player entered at unknown HP (higher than Run 4's 42 HP). Fight lasted 12 turns.
- **Headbutt does 9 damage (unupgraded), 12 damage (upgraded)**: Player's Run 5 had unupgraded Headbutt (9 damage), which left Mystic at 1 HP. Run 6 had Headbutt+ (12 damage, 13 Vuln through block), which was significantly more effective.
- **KILL MYSTIC FASTER**: The 12-turn fight drained massive HP. Key issue: unupgraded Headbutt (9 dmg) is not enough burst vs Mystic's ~15 block per turn. Headbutt+ (12 dmg, 13 Vuln) is better but still doesn't punch through 15 block in one hit. Need Carnage+ or Searing Blow for burst through block.
- **Correct target priority maintained**: Player correctly focused Mystic in both Runs 5 and 6.
- **Run 6**: Third encounter. Player entered at 25 HP. Killed Mystic in ~6 turns using Bash+ Vuln + Headbutt+ 13 Vuln + Pommel Strike+ 15 Vuln + Thunderclap+ 12 Vuln. Double Metallicize (6 block/turn) helped survive Centurion's attacks. Fairy consumed during fight (24 incoming, 6 block only). Used Feed to kill Centurion for +3 Max HP. Exited at ~5 HP.
- **Mystic HP revised**: Observed Mystic at 49 HP in Run 6 (Pommel Strike+ 10 damage, 49->39). Previous estimate was ~41. Mystic HP is likely ~49-50.
- Confidence: MEDIUM -> HIGH (3 fights across Runs 4, 5, and 6 — died in Run 4, survived in Runs 5 and 6 but heavily damaged. Kill Mystic first is confirmed. Mystic HP ~49.)



## Book of Stabbing

Act 2 elite. HP: 161 (confirmed in Run 6).

- **Multi-hit attacks that scale**: Book of Stabbing attacks multiple times per turn. The number of hits INCREASES each turn. Run 6 observed: Turn 1: ~8 damage (Weakened). Turn 2: 6x3 = 18. Turn 3: 6x3.5? ~21. Turn 4: 6x4 = 24. Turn 5: ~21 (with only 1 Metallicize). The hits-per-turn escalation is the core threat.
- **Painful Stabs (Wound cards)**: Each attack adds Wound status cards to the player's deck. Wounds are Unplayable — they sit in hand and waste card slots. Unlike Burns (deal damage), Wounds just clog draws. Over 5 turns, Wounds accumulate and dilute the deck, making it impossible to draw both damage AND block cards in the same hand.
- **Wound + scaling = death spiral**: Wounds clog draws -> fewer block cards per hand -> take more damage -> need more block -> draws are clogged with Wounds. By turn 5 in Run 6, the player had Wounds in hand and couldn't draw enough Defend+ cards to survive 21+ incoming.
- **HP is high (161)**: This is a long fight. Even with strong burst (Dropkick+ free cycling, Pommel Strike+ 15 Vuln, Headbutt+ 13 Vuln), the player dealt 140 damage in 5 turns and still had 21 HP remaining on the Book when they died.
- **Vulnerable synergy is critical**: Dropkick+ was the best card in this fight — effectively free (refunds energy + draws) when target is Vulnerable. The player dealt significant damage via Dropkick+ cycles.
- **Run 6 death**: Entered at 6 HP after resting. Book at 161 HP. Player dealt 140 damage in 5 turns (Bash+, Headbutt+ Vuln, Dropkick+ free cycles, Pommel Strike+, Strike+). Intimidate applied Weak turn 1 reducing first attack. Double Metallicize (6 block/turn) was insufficient against scaling multi-hit. Died with Book at 21 HP.
- **Strategy**: (1) Enter with HIGH HP — minimum 60% for this elite. (2) Apply Vulnerable immediately for Dropkick+ cycling. (3) Weak reduces each individual hit. (4) Front-load damage — every turn the fight goes on, attacks get worse AND Wounds clog draws. (5) Exhaust tools (True Grit+, Burning Pact) help remove Wounds. (6) Double Metallicize (6/turn) is good but insufficient against 4+ hit attacks.
- **HP THRESHOLD**: At 6 HP, this fight was unwinnable. Even with perfect play, 5 turns of scaling multi-hit damage overwhelms any amount of block. Enter with 50+ HP minimum.
- Confidence: MEDIUM (1 fight in Run 6, died — HP, attack scaling, and Wound mechanic confirmed)

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
