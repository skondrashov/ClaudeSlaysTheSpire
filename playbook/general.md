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
- **Slime Boss**: Need AOE for the split, burst single-target to kill one slime fast, exhaust tools for Slimed cards. Combined post-split damage is 25-36 per turn.
- **The Guardian**: Mode-switching boss with heavy attacks (5x4=20, single 32). Need block cards that can reach 32+ total per turn. Sharp Hide (3 damage per Attack played) in Defensive Mode means you need block before playing Attacks. Long fight (240 HP) rewards Strength scaling and efficient multi-purpose cards. DO NOT over-exhaust — keep enough cards to block 32 damage.
- **Hexaghost**: 250 HP. 7x6=42 Inferno attack is the biggest threat. Need Weak (Shockwave, Clothesline) to reduce it to ~28. Metallicize is excellent for the long fight. Burns accumulate and deal end-of-turn damage — exhaust tools help. Turn 1 is free (no attack). Pantograph negates low HP entry.

If you don't have the tools to handle the boss, prioritize getting them from card rewards, shops, and events over minor deck improvements.

Confidence: MEDIUM (4 boss encounters across Runs 0, 1, 2, 3 — 1 Guardian victory, 1 Slime Boss death, 1 Guardian death, 1 Hexaghost victory)

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

What counts as "in danger" depends on what's ahead — if you're about to fight an elite or a boss, you need more HP than if you're about to fight a normal enemy.

Run 1 data: Rested at floor 6 (63/85 HP after taking 21 damage from Golden Idol trap — correct, needed HP buffer). Smithed at floor 8 (full HP — correct, upgraded Bash). Smithed at floor 13 (76/85 HP — upgraded Shockwave, good call for boss prep). Rested at floor 15 (65/85 HP — correct, full heal before boss).

Pattern: the player correctly alternated between rest and smith based on HP, with a bias toward smithing. 3 out of 4 rest site decisions were correct. This principle holds.

Confidence: MEDIUM (tested in Run 1 — 4 rest site decisions, all reasonable)

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

Confidence: MEDIUM (Run 0 victory, Run 2 14-turn death — both inform this strategy)

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

## Prepare for Act boss (updated after Run 3)

By floor 12-15, you should be thinking about the boss. Each act boss has specific threats:
- **Slime Boss**: Need AOE for the split, burst single-target to kill one slime fast, exhaust tools for Slimed cards. Combined post-split damage is 25-36 per turn.
- **The Guardian**: Mode-switching boss with heavy attacks (5x4=20, single 32). Need block cards that can reach 32+ total per turn. Sharp Hide (3 damage per Attack played) in Defensive Mode. Long fight (240 HP). DO NOT over-exhaust.
- **Hexaghost**: 250 HP, 7x6=42 Inferno attack. Need (1) Weak to reduce Inferno to ~28, (2) Metallicize for passive block in long fight, (3) way to handle Burns (exhaust tools). Pantograph makes HP entry irrelevant. Shockwave is the single best card for this boss. Turn 1 is free (no attack).

Confidence: MEDIUM (4 boss encounters across Runs 0, 1, 2, 3 — 1 Guardian win, 1 Slime Boss death, 1 Guardian death, 1 Hexaghost win)

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

Act 2 enemies are significantly harder than Act 1. Key threats observed in Run 3:

### Byrds (Flight)
- Flight halves all damage. A 12-card deck with Strikes and Defends takes 12+ turns to kill 3 Byrds.
- **What you need**: AOE to strip Flight from all Byrds simultaneously (Thunderclap, Whirlwind). Strength scaling to make even halved damage meaningful. Metallicize for the long fight.
- **HP cost**: Even with good play, expect 40-60 HP lost. If entering Act 2 below 50% HP, Byrds can end the run.

### Chosen (Hex)
- Hex punishes Skills. Every Defend adds a Dazed card.
- **What you need**: Attack-heavy deck. Iron Wave (Attack that also blocks) is excellent. Inflame for Strength to overcome Weakened. Fast kill before Strength buffs escalate damage.
- **What NOT to do**: Don't play Defend cards unless you absolutely must survive this turn. Each Defend clogs the deck.

### General Act 2 Rule
- Enter Act 2 at or near full HP. The Pantograph relic should heal you before the Act 1 boss, but hallway fights in Act 2 hit much harder than Act 1. The Byrd fight in Run 3 drained 58 HP.
- Having healing sustain (Reaper) is critical for surviving the HP drain of Act 2 multi-enemy fights.

Confidence: LOW (1 partial Act 2 experience in Run 3, died floor 20)

## Gremlin Nob Strategy (Refined after Run 3)

Run 3 demonstrated the correct approach vs Run 2's mistakes:
1. **Zero Skills.** Not one Defend, not one Shrug It Off, nothing. Every Skill gives Nob +2 Strength permanently.
2. **Turn 1 is free.** Nob buffs, does not attack. Go all-in on damage: Pommel Strike + Strike + Strike = 21 damage for 0 HP lost.
3. **Bash+ turn 2 with Flex Potion.** Apply Vulnerable early for 50% more damage on all subsequent attacks. Flex Potion's +2 Str is consumed this turn so use it when playing the most Attack cards.
4. **4-turn kill.** With Bash+ Vulnerable and focused Attacks, Nob dies in 4 turns. Taking only ~9 HP damage total.

Run 2 fought Nob with Skills (3 Skills = +6 Str, survived at 3 HP). Run 3 fought with 0 Skills (survived at 63 HP). The difference is massive.

Confidence: HIGH (confirmed across Runs 2 and 3 — night-and-day results)
