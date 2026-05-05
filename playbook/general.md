# General Strategy

Strategy principles learned from runs. Updated by the analyst after each run.

## Deck Building

### Take cards that solve problems, not cards that are generically good

A card's value depends on what your deck needs right now. Questions to ask before taking a card:
- What fights am I struggling with?
- Do I have enough damage? Enough block? AOE?
- Will this card dilute my draws (bigger deck = less likely to draw key cards)?

A mediocre card that fills a gap in your deck is better than a strong card that duplicates what you already have.

Confidence: MEDIUM (based on Run 1 death — deck lacked AOE for Slime Boss)

### Prepare for the Act boss

By floor 12-15, you should be thinking about the boss. Each act boss has specific threats you need to handle:
- **Slime Boss**: Need AOE for the split, burst single-target to kill one slime fast, exhaust tools for Slimed cards. Combined post-split damage is 25-36 per turn. Run 4 victory used Thunderclap (mass Vuln), Whirlwind (AOE), and Fiend Fire (burst + Slimed exhaust). Plated Armor potion helped survive the split phase.
- **The Guardian**: Mode-switching boss with heavy attacks (5x4=20, single 32). Need block cards that can reach 32+ total per turn. Sharp Hide (3 damage per Attack played) in Defensive Mode means you need block before playing Attacks. Long fight (240 HP) rewards Strength scaling and efficient multi-purpose cards. DO NOT over-exhaust — keep enough cards to block 32 damage.
- **Hexaghost**: 250 HP. 7x6=42 Inferno attack is the biggest threat. Need Weak (Shockwave, Clothesline) to reduce it to ~28. Metallicize is excellent for the long fight. Burns accumulate and deal end-of-turn damage — exhaust tools help. Turn 1 is free (no attack). Pantograph negates low HP entry.

If you don't have the tools to handle the boss, prioritize getting them from card rewards, shops, and events over minor deck improvements.

Confidence: MEDIUM (7 boss encounters across Runs 0-6 — 3 Guardian victories, 1 Slime Boss death, 1 Guardian death, 1 Hexaghost victory, 1 Slime Boss victory)

## Combat

### Kill attacking enemies before debuffing enemies

When facing multiple enemies, prioritize killing the ones that are attacking this turn. A dead enemy deals no damage — that's better than any amount of block. An enemy that's only debuffing you this turn can wait.

Exception: if the debuff will be devastating (heavy Frail before a big turn, or Weak when you need a kill), consider removing that enemy first.

Confidence: LOW (hypothesis from Run 1 — the player didn't always do this, and it might have helped)

### Exhaust status cards early

Status cards (Slimed, Wound, Burn, Dazed, Void) are dead draws. Every turn they're in your deck is a turn they might show up and waste a card slot. Prioritize exhausting them when you have spare energy.

Confidence: MEDIUM (Run 1 — Slimed cards were the primary reason for losing tempo against slimes)

## Rest Sites

### Upgrade before heal unless you're in danger

Upgrading a key card gives you permanent value for the whole run. Healing gives you HP that you'll probably lose again. Only heal when your HP is low enough that the next fight could kill you.

What counts as "in danger": HP below 35% before an elite or boss. HP below 25% before normal monster rooms. At 45-50% HP before unknowns or normal fights, you should UPGRADE, not rest.

Run 1 data: Rested at floor 6 (63/85 HP after taking 21 damage from Golden Idol trap — correct, needed HP buffer). Smithed at floor 8 (full HP — correct, upgraded Bash). Smithed at floor 13 (76/85 HP — upgraded Shockwave, good call for boss prep). Rested at floor 15 (65/85 HP — correct, full heal before boss).

**Run 4 FAILURE**: Rested 3 times, upgraded ONCE in 28 floors. Rest site decisions: Floor 8 (46% HP, rested), Floor 14 (45% HP, rested), Floor 27 (50% HP, FINALLY smithed Bash+). The player rested at 45-50% HP every time, which is too conservative. This led to entering Act 2 with zero upgrades, making every fight harder and draining more HP — a death spiral.

**Revised rule**: At 45-50% HP with a rest site before unknowns/normal fights, UPGRADE. Rest only at 35% HP or lower, or immediately before an elite/boss. The earlier you upgrade, the more fights benefit from it. One upgrade on floor 8 pays dividends for 20+ floors.

**Upgrade priority**: Bash (3 Vuln vs 2 is huge), Iron Wave (7/7 vs 5/5), Whirlwind (8 per hit vs 5), Thunderclap (7 vs 4), Shrug It Off (11 block vs 8), Uppercut (2 turns debuffs vs 1).

Confidence: HIGH (Run 1 correct upgrades vs Run 4 catastrophic under-upgrading — the contrast is stark)

## Boss Preparation

### Save one-time-use cards for the boss

Exhaust cards like Shockwave+ are single-use per combat. Don't waste them on hallway fights unless the fight is genuinely dangerous. The player in Run 1 correctly saved Shockwave+ for the boss.

Confidence: MEDIUM (Run 1 — player explicitly reasoned about saving Shockwave+ for the boss, correct decision)

### Use stat-boost potions at the start of boss fights

Potions like Fruit Juice (+5 max HP) and Speed Potion (Dexterity) are best used at the start of a boss fight where they provide maximum value. The player in Run 1 used Fruit Juice before turn 1 for immediate max HP, and Speed Potion on turn 3 when block was critical.

Confidence: MEDIUM (Run 1 — both potions used at good times)

## Pathing

### Prioritize rest sites before bosses

In Run 1, the player had a rest site on floor 15 (directly before the boss on floor 16) and healed to full. Having a rest site before the boss is extremely valuable for topping off HP. When choosing paths, prefer routes that include a rest site in the last 1-2 floors before the boss.

Confidence: LOW (1 run, but the logic is sound)

### Don't take unnecessary damage from events

In Run 1, the Golden Idol event cost 21 HP (floor 4). While the relic may be valuable, 21 HP is a lot — especially when we don't know what Golden Idol does. Before taking damage from events, consider whether the reward is worth the HP cost.

Confidence: LOW (1 event, outcome unclear since we never confirmed what Golden Idol does)

## What Worked in Run 0 (Guardian Boss Victory)

The Run 0 deck beat The Guardian (Act 1 boss) with a block-and-cycle strategy:
- **True Grit+** provided block + exhaust (removing bad cards from hand)
- **Shrug It Off+** provided 11 block + card draw
- **Pommel Strike** provided damage + card draw

This is a "quality over quantity" deck — each card does two things (block+exhaust, block+draw, damage+draw). The card draw keeps cycling to find the right answers. This is a model to aim for: cards that do double duty rather than just one thing.

Confidence: LOW (partial log, can't see full deck or full fight)

## What Went Wrong in Run 2 (Guardian Boss Death)

The Run 2 deck had strong synergy potential (Dark Embrace + Charon's Ashes + True Grit = exhaust engine) but two fatal flaws:
1. **True Grit was unupgraded** — random exhaust destroyed Whirlwind, Bash, and Pommel Strike, the deck's best cards.
2. **Too much exhausting** — the deck thinned to 3 cards, which couldn't generate enough block to survive Guardian's 32-damage attack.

Key takeaways:
- **True Grit upgrade is mandatory** before using it as an exhaust engine. Random exhaust is suicide.
- **Know your block ceiling**: Calculate the maximum block your remaining cards can produce. If that's less than the enemy's biggest attack, stop exhausting.
- **Iron Wave + Metallicize carried the fight** for 14 turns. Iron Wave (damage + block) and Metallicize (passive block every turn) are the kind of efficient, multi-purpose cards that win long fights.
- **The Guardian has a 32-damage attack**. Any deck that can't block 32 in a single turn will eventually die. You need at minimum ~6 block cards or equivalent to survive this.
- **Entry HP was ~46, not 16**: The player entered at approximately 46 HP after resting. The "16 HP" figure may refer to HP during the fight. Still low for a 240-HP boss.

Confidence: MEDIUM (Run 2 death, confirmed mechanics)

## Exhaust Strategy

### Exhaust is powerful but has a breakpoint

Exhaust synergy (Dark Embrace draw + Charon's Ashes 3 damage) is a strong engine: every exhaust draws a card AND deals damage. But there's a critical breakpoint: once your deck is too thin, you can't survive big attacks.

**Before exhausting a card, ask:**
1. Can my remaining deck survive the enemy's biggest attack? (Calculate max block from remaining block cards + Metallicize/passive sources)
2. Is the card I'm exhausting truly expendable? (Strikes and Defends early — yes. Core damage/block cards — no.)
3. Am I in the first half of the fight (thin deck = good, draws key cards more often) or the second half (thin deck = not enough block cards)?

**Safe exhaust targets**: Strikes, extra Defends, status cards (Slimed, Wound, etc.)
**Never exhaust**: Your last copy of your best damage card, your last copy of a high-block card

Confidence: HIGH (Run 2 death was caused by exhausting key cards)

## Guardian-Specific Strategy

The Guardian is a long fight (240 HP) with alternating modes:
1. **Attack Mode**: Mode Shift counter tracks damage dealt. When counter reaches 0, switches to Defensive Mode. Attacks include 5x4=20, 32 single hit, 8x2=16. Also has DEFEND (gains block, no damage) and STRONG_DEBUFF (no damage) turns.
2. **Defensive Mode (Sharp Hide)**: Deals 3 damage to player per Attack card played. Has its own attack pattern. Switches back to Attack Mode after some turns.

**What you need for Guardian**:
- Block cards that can reach 32+ per turn (Defend + Defend + True Grit + Iron Wave + Metallicize = 20-25 minimum)
- Damage that works around Sharp Hide (Skills, or enough block to absorb Sharp Hide + enemy attack)
- A deck thick enough to not get exhausted into oblivion over 14+ turns
- Strength scaling helps since fight is long (even +2 Str adds up over many turns)

**Run 5 Guardian Victory** (second victory):
- Entered at 69/80 HP, 15-card deck, 3 upgrades (Bash+, Shrug It Off+, Carnage+), 3 potions (Skill, Fear, Fairy).
- **Skill Potion -> Impervious** on turn 2: 30 block absorbed 32-damage attack (took 2). Game-saving play.
- **Carnage+ + Headbutt loop**: Headbutt placed Carnage+ on top of draw repeatedly. Every other turn dealt 28-42 damage.
- **Fairy in a Bottle** triggered on turn 11 (took 32 damage at 18 HP). Revived at ~24 HP. Kill on turn 12 with Shrug It Off+ (block for Sharp Hide) + Strike (6 damage on 2 HP Guardian).
- **Key difference from Run 2**: Had Carnage+ for massive burst (42 with Vuln). Run 2 relied on chipping with Strikes/Iron Wave. The burst allowed faster kill (12 turns vs 14) and triggered fewer Mode Shifts.
- **12-turn fight, HP: 69 -> 0 (Fairy) -> 24 -> kill**. Guardian is still an HP drain even with good play.

**Run 6 Guardian Victory** (third victory):
- Entered at 67/80 HP after resting. Deck: 13 cards, 4 upgrades (Bash+, Pommel Strike+, Headbutt+, Thunderclap+), Metallicize x2, Intimidate, Letter Opener relic.
- **Double Metallicize** turn 1: 6 block/turn for the entire fight. This handled many attack patterns (9 damage, 8x2=16 damage) with only 1 Defend needed.
- **Intimidate** (0E, Weak ALL): Reduced 32 attack to 24. Free play, no downside.
- **Snecko Oil** clutch: On a dangerous turn, drew 5 cards with randomized costs. Got 0-cost Strikes and Pommel Strike+, enabling massive free damage output during Defensive Mode despite Sharp Hide.
- **Letter Opener** relic: Every Skill played dealt 5 chip damage. Over 12+ turns, contributed ~40+ total damage passively.
- Killed Guardian at 10 HP remaining. The Snecko Oil turn was decisive — without it, the fight would have been much closer.

**Winning formula refined across 3 victories (Runs 0, 5, 6)**:
1. One big block source for 32-damage turn (Impervious, double Metallicize + Defend, Intimidate Weak)
2. Burst damage for Mode Shift (Carnage+, Snecko Oil free cards, Headbutt+ Vuln loops)
3. Passive block scaling for the long fight (Metallicize is the best card; double Metallicize is exceptional)
4. Safety net (Fairy in a Bottle) — triggered in Run 5, not needed in Run 6
5. Deck manipulation (Headbutt+ placing key cards on top)

Confidence: HIGH (4 fights — 3 victories in Runs 0, 5, 6; 1 death in Run 2. Winning formula well-established.)

## Gremlin Nob Strategy

Gremlin Nob punishes Skills with Enrage (+2 Strength per Skill played). Strategy:
1. **Only play Attacks.** No Defend, no True Grit, no Shrug It Off. Every Skill card buffs Nob permanently.
2. **Powers are safe.** Dark Embrace, Inflame, Metallicize are NOT Skills — they do not trigger Enrage.
3. **Potions can substitute for block.** Use potions (Block Potion, Fairy in a Bottle) instead of playing Skill block cards.
4. **Kill fast.** The longer the fight, the more turns Nob accumulates Strength from inevitable Skills. Even if you play only Attacks, Nob's base damage is dangerous.
5. **Bash is safe.** It's an Attack card that applies Vulnerable. Open with Bash for +50% damage.

Run 2 example: Player played 2x True Grit + 1x Defend (3 Skills = +6 Strength to Nob) during the desperation phase. Even though the block was needed, those Skills made the next attack ~6 damage stronger.

Confidence: MEDIUM (Run 2, 1 fight, Enrage/Power-exception confirmed)

## Elites: Risk Assessment

Before fighting an elite, check:
1. **HP threshold**: Below 30 HP for Act 1 elites is very dangerous. Lagavulin deals 18/turn, Gremlin Nob scales indefinitely.
2. **Deck vs elite matchup**: Gremlin Nob punishes Skill-heavy decks. Lagavulin punishes slow decks (debuffs accumulate). 3 Sentinels require AOE.
3. **Potions available**: Potions can compensate for bad matchups. Snecko Oil, Fairy in a Bottle, and Block Potions saved the Run 2 Gremlin Nob fight.
4. **Path alternatives**: If a safer path exists with similar value, take it. Run 2 had "forced" elite paths but verify this — sometimes there are alternative routes.

Run 2: Both elite fights nearly killed the player. Lagavulin (82->35 HP), Gremlin Nob (29->3 HP, saved by Fairy). The relics gained (Charon's Ashes, Ancient Tea Set) were excellent but the HP cost almost ended the run before the boss.

Confidence: MEDIUM (Run 2, 2 elite fights observed)

## Card Evaluation Heuristic: Unknown Cards

Run 1 lesson was "don't take cards you don't understand" (Berserk disaster). But Run 2 applied this too broadly, skipping Reaper (a strong card).

**Refined rule:**
- **Skip unknown cards** that might have hidden self-damage or self-debuff (words like "lose," "take damage," "Vulnerable to self," curses)
- **Take unknown cards** that seem purely beneficial (damage + heal, damage + draw, block + effect). The upside of discovering a strong card outweighs the risk.
- **Especially take** unknown cards that fill a known gap in your deck (e.g., Reaper fills "need healing" gap, AOE fills "need multi-target" gap)

Confidence: MEDIUM (Runs 1 and 2 — one overcorrection observed)

## Turn Planning: Never Skip Reasoning

In Run 2, the player stopped filling in reasoning for turns 7-14 of the Guardian fight. These were the turns where the deck was thinning from True Grit exhaust and every decision mattered most.

**Rule: Always reason about the current turn, especially when:**
1. Your deck has fewer than 8 cards remaining
2. You're playing exhaust cards that thin the deck further
3. The enemy's biggest attack exceeds your maximum block
4. You're below 30% HP

The absence of reasoning in Run 2's late turns correlated directly with the failure to notice the deck was approaching an unsurvivable state.

Confidence: HIGH (Run 2 — empty reasoning fields correlated with death)

## Prepare for Act boss (updated after Run 4)

By floor 12-15, you should be thinking about the boss. Each act boss has specific threats:
- **Slime Boss**: Need AOE for the split (Thunderclap, Whirlwind), burst single-target to kill one slime fast (Fiend Fire), exhaust tools for Slimed cards. Combined post-split damage is 25-36 per turn. Run 4 victory confirmed: AOE + exhaust + Plated Armor potion = win.
- **The Guardian**: Mode-switching boss with heavy attacks (5x4=20, single 32). Need block cards that can reach 32+ total per turn. Sharp Hide (3 damage per Attack played) in Defensive Mode. Long fight (240 HP). DO NOT over-exhaust.
- **Hexaghost**: 250 HP, 7x6=42 Inferno attack. Need (1) Weak to reduce Inferno to ~28, (2) Metallicize for passive block in long fight, (3) way to handle Burns (exhaust tools). Pantograph makes HP entry irrelevant. Shockwave is the single best card for this boss. Turn 1 is free (no attack).

Confidence: MEDIUM (7 boss encounters across Runs 0-6 — 3 Guardian wins, 1 Slime Boss death, 1 Guardian death, 1 Hexaghost win, 1 Slime Boss win)

## Hexaghost Strategy (Run 3 Victory)

Run 3 deck beat Hexaghost at 250 HP, surviving at 1 HP:
- **Pantograph** healed from 56 to 80 HP at fight start
- **Thunderclap** applied Vulnerable on turn 1 (free turn, no attack)
- **Regen Potion** used turn 2 for sustained healing (~15 HP total)
- **Skill Potion -> Shockwave** applied Weak for the first Inferno, reducing 42 to ~28
- **Metallicize** set up on turn 4 for 3 passive block per turn (provided ~27 block over 9 remaining turns)
- **Bash+** refreshed Vulnerable every 3 turns on free turns (DEFEND_BUFF intent)
- **Burns nearly killed**: By turn 12, multiple Burns were dealing end-of-turn damage and clogging hands. The fight was won with exactly 1 HP remaining.

**What this deck needed more of**: (1) A way to exhaust Burns (True Grit+ would have been perfect). (2) More block — only 4 Defends + Iron Wave+ was barely enough for Inferno turns. (3) Faster damage — the fight was 13 turns, which allowed Burns to accumulate dangerously.

Confidence: MEDIUM (Run 3, 1 victory)

## Act 2 Preparation

Act 2 enemies are significantly harder than Act 1. Key threats observed in Runs 3 and 4:

### Byrds (Flight)
- Flight halves all damage. A 12-card deck with Strikes and Defends takes 12+ turns to kill 3 Byrds.
- **What you need**: AOE to strip Flight from all Byrds simultaneously (Thunderclap, Whirlwind). Strength scaling to make even halved damage meaningful. Metallicize for the long fight.
- **HP cost**: Even with good play, expect 40-60 HP lost. If entering Act 2 below 50% HP, Byrds can end the run.

### Chosen (Hex)
- Hex punishes Skills. Every Defend adds a Dazed card.
- **What you need**: Attack-heavy deck. Iron Wave (Attack that also blocks) is excellent. Inflame for Strength to overcome Weakened. Fast kill before Strength buffs escalate damage.
- **What NOT to do**: Don't play Defend cards unless you absolutely must survive this turn. Each Defend clogs the deck.

### Centurion + Mystic (NEW from Run 4)
- Mystic heals Centurion ~12 HP/turn and gains ~15 block. Centurion attacks for 12-18 per turn.
- **KILL MYSTIC FIRST**: Absolutely non-negotiable. You cannot out-damage Mystic's healing on Centurion.
- **What you need**: Burst damage to break through Mystic's block (Fiend Fire, Whirlwind). Weak on Centurion to reduce incoming while you focus Mystic. Enough HP to absorb Centurion's attacks for 4-5 turns.
- **HP threshold**: Enter with 50+ HP. Run 4 entered at 42 HP and died. Even with correct target priority (killed Mystic on turn 5), Centurion's attacks drained HP too fast.

### Spheric Guardian (NEW from Run 4)
- 20 HP but starts with 40 block + Barricade (block persists) + 3 Artifact + Frail 5. Effective HP is 60+.
- **What you need**: Strip Artifact first (3 cheap debuffs), then apply Vulnerable, then burst through block with high-damage cards. Pen Nib double damage is excellent here.
- **HP cost**: Expect 20-30 HP lost from Frail-reduced blocking against 10x2 attacks.

### Gremlin Leader (NEW from Run 5)
- DEFEND_BUFF rallies give ALL enemies +3 Str permanently. The fight's damage scales exponentially with each rally turn.
- **What you need**: AOE to kill gremlins fast (Thunderclap, Whirlwind), mass debuff (Shockwave), Strength reduction (Disarm). Non-exhaust damage to sustain after one-time-use cards are gone.
- **HP threshold**: Enter with 60%+ HP. Run 5 entered at 13% and died despite Impervious, Disarm, and Shockwave.
- **Critical warning**: Exhaust-heavy decks are dangerous here. Once Impervious/Shockwave/Disarm are gone (turns 1-5), you need enough remaining cards to survive 3+ more turns of 30-50 incoming damage.

### Book of Stabbing (NEW from Run 6)
- 161 HP elite with scaling multi-hit attacks and Wound card generation. Attacks increase in hit count each turn (observed: 8, 18, 21, 24 over 4 turns).
- **What you need**: High burst damage to end the fight quickly (Dropkick+ cycling, Headbutt+ Vuln). Exhaust tools for Wound removal (True Grit+, Burning Pact). Block cards that handle multi-hit (Metallicize for passive, Impervious for one big turn). Vulnerable application for Dropkick+ synergy.
- **What kills you**: Wound accumulation clogs draws -> can't draw block cards -> take full multi-hit damage -> die. The fight is a race between your damage output and the Book's escalating attacks + Wound flood.
- **HP threshold**: Enter with 50+ HP. Run 6 entered at 6 HP and died with Book at 21 HP despite dealing 140 damage in 5 turns. At low HP, the scaling attacks overwhelm any block strategy.

### General Act 2 Rule
- Enter Act 2 at or near full HP. The Pantograph relic should heal you before the Act 1 boss, but hallway fights in Act 2 hit much harder than Act 1. The Byrd fight in Run 3 drained 58 HP.
- Having healing sustain (Reaper, Feed) is critical for surviving the HP drain of Act 2 multi-enemy fights. Feed is especially good because it provides permanent Max HP scaling.
- **Upgrades matter more in Act 2**: Run 4 entered Act 2 with ZERO upgrades and only upgraded Bash on floor 27 (1 upgrade in 28 floors). Unupgraded cards are much weaker against Act 2 enemies. Prioritize upgrading at rest sites over resting when HP is above 60%.
- **Run 5 improvement**: 3 upgrades by Act 2 (Bash+, Shrug It Off+, Carnage+). This made a significant difference — Carnage+ carried the Guardian fight and was useful in Act 2. But the deck still lacked sustained answers for long fights.
- **Run 6 improvement**: Entered Act 2 at full HP (80/80) for the first time. Had 4+ upgrades (Bash+, Pommel Strike+, Headbutt+, Thunderclap+) plus Ancient Writing event upgraded all Strikes and Defends. Despite this strong position, Act 2 still killed the run through the Byrd -> Centurion+Mystic -> Elite HP drain cascade.
- **Fairy in a Bottle management**: In Runs 5 and 6, Fairy was consumed in hallway fights (Centurion+Mystic), leaving no safety net for elites. Consider: if Fairy is your only death insurance, avoid fights that might trigger it before the elite/boss.

Confidence: MEDIUM (4 partial Act 2 experiences in Runs 3, 4, 5, and 6, died floors 20, 28, 25, and 24)

## Slime Boss Strategy (Run 4 Victory)

Run 4 deck beat Slime Boss at ~140 HP, surviving at 17 HP:
- **Neow choice**: Lost 8 Max HP for Fiend Fire (rare card). Perfect boss prep — Fiend Fire exhausts Slimed cards AND deals burst damage.
- **Card choices**: Thunderclap (mass AOE + Vuln), Whirlwind (X-cost AOE), Uppercut (Weak + Vuln), all taken specifically for Slime Boss.
- **Plated Armor 4** from Essence of Steel potion provided passive block every turn.
- **Pre-split**: 4 turns. Dealt ~76 damage using free STRONG_DEBUFF turns. Bash for Vuln setup, Thunderclap to refresh Vuln, Strikes for damage. Boss split at ~58 HP.
- **Post-split**: Spike Slime (L) + Acid Slime (L) appeared. Used Thunderclap for mass Vuln on both. Exhausted 3 Slimed cards on free debuff turns. Fire Potion on Acid Slime for burst. Killed Spike Slime (L) which split into 2x Spike Slime (M). Cleaned up mediums in 2 turns.
- **Key success factors**: (1) Dedicated AOE cards (Thunderclap, Whirlwind). (2) Fiend Fire for burst + Slimed exhaust. (3) Plated Armor for sustained blocking. (4) Killing attacking slime first while exhausting Slimed on free turns. (5) Proper debuff turn identification.

**What this deck had that Run 1 lacked**: (1) Mass AOE (Thunderclap + Whirlwind vs nothing). (2) Exhaust for Slimed (Fiend Fire vs nothing). (3) Dual debuffs (Uppercut for Weak + Vuln vs Shockwave only). The Run 1 lesson about needing AOE for Slime Boss was directly applied.

Confidence: MEDIUM (Run 4, 1 victory — first successful Slime Boss kill)

## Gremlin Nob Strategy (Refined after Run 3)

Run 3 demonstrated the correct approach vs Run 2's mistakes:
1. **Zero Skills.** Not one Defend, not one Shrug It Off, nothing. Every Skill gives Nob +2 Strength permanently.
2. **Turn 1 is free.** Nob buffs, does not attack. Go all-in on damage: Pommel Strike + Strike + Strike = 21 damage for 0 HP lost.
3. **Bash+ turn 2 with Flex Potion.** Apply Vulnerable early for 50% more damage on all subsequent attacks. Flex Potion's +2 Str is consumed this turn so use it when playing the most Attack cards.
4. **4-turn kill.** With Bash+ Vulnerable and focused Attacks, Nob dies in 4 turns. Taking only ~9 HP damage total.

Run 2 fought Nob with Skills (3 Skills = +6 Str, survived at 3 HP). Runs 3 and 4 fought with 0 Skills (survived at 63 HP and 46 HP respectively). The difference is massive.

**Run 4 optimization**: Strength Potion on turn 1 (free BUFF turn) maximized value — every Attack for rest of fight got +2 damage. Combined with Bash Vuln, Strikes dealt 12 each. Clean 3-turn kill (vs Run 3's 4-turn kill). Using a Strength Potion on the free turn is the optimal Nob opener.

Confidence: HIGH (confirmed across Runs 2, 3, 4, and 5 — four fights, night-and-day results between Skills and no-Skills approaches)

## Gremlin Leader Strategy (Run 5 Death)

Gremlin Leader is the hardest Act 2 elite observed. DEFEND_BUFF rallies give ALL enemies +3 Strength permanently. This means the fight's damage scales exponentially with turn count.

**Why it's deadly:**
- Unlike Centurion+Mystic (kill the healer) or Spheric Guardian (DPS check), the Leader's threat compounds: each rally makes EVERY enemy stronger.
- By turn 8 in Run 5, total incoming was 49 damage (Leader + 3 gremlins, each with accumulated Str buffs).
- Exhaust cards (Impervious, Shockwave, Disarm) are one-time use. Once they're gone, you have no answers for the scaling.

**Strategy:**
1. **KILL GREMLINS FAST.** Dead gremlins don't benefit from rally. AOE (Thunderclap, Whirlwind) is critical.
2. **Apply Shockwave early** for mass Weak (reduces all incoming by 25%) AND mass Vulnerable (50% more damage to all = faster kills).
3. **Disarm on Leader** removes 2 Str permanently, partially offsetting one rally.
4. **DO NOT enter below 60% HP.** Run 5 entered at 11 HP (13%) and it was unwinnable. Even correct play (Impervious opener, Disarm, Shockwave) couldn't overcome the starting HP deficit.
5. **Avoid if deck is exhaust-heavy.** Exhaust cards are used once. In a long fight like this, once Impervious/Shockwave/Disarm are gone, you're playing with a thin deck of Strikes and Defends against enemies with +9 Strength.

**Pre-fight checklist:**
- HP above 60%? If no, AVOID.
- Have AOE for gremlins? If no, very dangerous.
- Have mass debuff (Shockwave)? Critical.
- Have Strength reduction (Disarm)? Helpful.
- Have enough non-exhaust cards to sustain a 6+ turn fight? If deck is mostly exhaust cards, AVOID.

Confidence: MEDIUM (1 fight in Run 5, died — mechanics clear but more data needed on timing and thresholds)

## Exhaust-Heavy Decks: The Long Fight Problem (Run 5 Lesson)

Exhaust cards (Impervious, Shockwave, Disarm, Carnage+ via Ethereal, True Grit+ exhausting others) are extremely powerful — but they are one-time-use. In long fights (8+ turns), an exhaust-heavy deck runs out of answers.

**Run 5 Gremlin Leader fight:**
- Turn 1: Impervious (30 block, exhausted)
- Turn 3: Disarm (-2 Str on Leader, exhausted)
- Turn 5: Shockwave (mass debuff, exhausted)
- Turn 6: Reaper (damage + heal, exhausted — wait, Reaper doesn't exhaust? It was played again turn 6)
- Turn 7: True Grit+ (exhausted a Strike)
- By turn 8: Key tools gone. Deck was Strikes, Defends, and a few attack cards vs enemies with +6-9 Strength. 49 incoming, ~21 block available. Death.

**The tradeoff:**
- Exhaust cards win SHORT fights (1-5 turns) decisively: Impervious + Shockwave + Carnage+ = massive burst + total defense.
- Exhaust cards LOSE LONG fights (8+ turns): once exhausted, the remaining deck is anemic.
- The inflection point is around turn 6-7. If the fight isn't over by then, an exhaust-heavy deck is in trouble.

**When to build exhaust-heavy:**
- Against bosses with known mechanics and turn counts (Guardian 12 turns, Hexaghost 13 turns — you can plan which turns to use each card).
- When the deck has a strong non-exhaust core (Bash+, Strikes, Defends, Iron Wave, Headbutt).

**When exhaust-heavy is dangerous:**
- Against enemies that summon reinforcements (Gremlin Leader).
- Against enemies with Strength scaling (Gremlin Leader DEFEND_BUFF, Cultist Ritual).
- When you don't know how long the fight will last.

Confidence: MEDIUM (Run 5 death from exhaust depletion, consistent with Run 2 over-exhaust lesson)

## HP Management Into Elites (Cross-Run Pattern)

Entering fights at critically low HP is a recurring cause of death. This is the #1 cause of death across all runs:
- **Run 3**: Entered Chosen at 28 HP (35%) after Byrd drain. Died with Chosen at 6 HP. 22 more HP would have survived.
- **Run 4**: Entered Centurion+Mystic at 42 HP (50%). Died at 1 HP. Barely insufficient.
- **Run 5**: Entered Gremlin Leader at 11 HP (13%). Completely unwinnable regardless of play quality.
- **Run 6**: Entered Book of Stabbing at 6 HP (7%) after Centurion+Mystic drain. Book at 21 HP when player died. Unwinnable at that HP.

**The pattern is now 4 runs deep**: Runs 3, 4, 5, and 6 all died from entering Act 2 fights at dangerously low HP. The root cause is the same every time: a long Act 2 fight (Byrds, Centurion+Mystic) drains HP to critical levels, and then the next fight is entered without healing.

**HP thresholds for Act 2 fights:**
| Fight Type | Minimum HP | Notes |
|---|---|---|
| Hallway (easy) | 25% | Byrds/Chosen can still drain 40-60 HP |
| Hallway (hard) | 40% | Centurion+Mystic, Snake Plant |
| Elite | 60% | Gremlin Leader, Book of Stabbing |
| Boss | 70% or Pantograph | Act 2 boss has massive damage |

**Decision at low HP:**
- Below the threshold for the next fight? Take a DIFFERENT PATH. Event rooms, rest sites, shops — anything but the dangerous fight.
- If forced into a fight below threshold, use all potions aggressively. Don't save them for "later" — there may not be a later.
- If there's a rest site before the elite, REST (don't upgrade). HP > upgrades when you're below threshold.

**Run 6 specific failure**: Player rested at rest site before elite (went from ~5 HP to ~6 HP? Or from higher and the rest brought them to a slightly better state). But the rest site was immediately before the elite — at 6 HP, even resting wasn't enough. The player needed to take an alternative path entirely. The Fairy in a Bottle was consumed during the Centurion+Mystic fight, leaving no safety net for the elite.

**What actually causes the HP drain (cross-run analysis)**:
1. **Byrd fights** (Runs 3, 6): 36-58 HP lost per fight. Flight mechanic makes fights 10-12 turns long. This is the primary Act 2 HP drain source.
2. **Centurion+Mystic** (Runs 4, 5, 6): 25-42 HP lost per fight. Mystic's healing extends the fight, Centurion attacks for 12-18/turn.
3. **No healing between fights**: Burning Blood (+6) cannot compensate for 30-50 HP fights. Reaper and Feed are the only in-combat healing options.
4. **Fairy consumed in wrong fight**: In Runs 5 and 6, Fairy in a Bottle was consumed in a hallway fight, leaving no safety net for the elite. Save Fairy for elites/bosses when possible.

Confidence: HIGH (pattern across Runs 3, 4, 5, and 6 — four deaths from low HP entry, root causes now identified)
