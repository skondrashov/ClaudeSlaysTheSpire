# Bosses

Act 1 bosses with full strategy guides.

---

## Slime Boss (Act 1, HP: ~140)

PATTERN:
- Pre-split: Alternates between STRONG_DEBUFF turns (no attack, safe to go all-in) and high-damage ATTACK turns (35 damage). Debuff turns are safe windows for damage.
- Split: At ~50% HP (~58 HP observed), splits into Spike Slime (L) + Acid Slime (L). This is the most dangerous transition.
- Post-split: Two enemies each with significant HP and damage. Spike Slime (L) attacks for ~16 and applies Frail. Acid Slime (L) attacks for ~11-12 and applies Weak. Combined 25-36 damage per turn. Both add Slimed cards to deck.

KEY MECHANICS:
- **Split transition**: Going from 1 enemy to 2 with combined 25-36 damage/turn is the hardest moment.
- **Slimed cards**: Cost 1E to exhaust, do nothing. Clog hand badly (3 of 5 cards being Slimed observed).
- **Dual debuffs**: Frail (block reduced 25%) + Weak (damage reduced 25%) simultaneously is devastating.
- **Spike Slime (L) splits again**: When killed, splits into 2x Spike Slime (M) at ~11 HP each.

PREPARATION CHECKLIST:
1. AOE for the split (Thunderclap, Whirlwind) -- MANDATORY
2. Burst single-target to kill one slime fast (Fiend Fire, Carnage+)
3. Exhaust tools for Slimed cards (Fiend Fire turns Slimed into 7 damage each, True Grit+, Burning Pact)
4. Enough block/HP to survive 2-3 turns of 25-36 combined damage

STRATEGY:
- **Pre-split**: Use debuff turns (free turns) to deal damage. Apply Vulnerable with Bash+. Don't worry about killing fast -- prepare for the split.
- **At split**: Use Thunderclap for mass Vulnerable on both slimes. AOE with Whirlwind.
- **Post-split**: Kill the ATTACKING slime first. Exhaust Slimed cards on FREE turns (debuff-only turns). If Spike Slime (L) dies and splits into mediums, clean them up.
- **Slimed management**: Exhaust Slimed cards as priority. Each one exhausted is one fewer dead draw for the rest of combat. Fiend Fire is ideal -- converts Slimed cards to 7 damage each.

WHAT NOT TO DO:
- Enter without AOE. Single-target damage cannot handle the split.
- Ignore Slimed cards. They accumulate and destroy hand quality.
- Play Berserk. Self-Vulnerable against 2 enemies doing 25-36 combined is suicidal.
- Split damage between both slimes. Focus fire one to reduce enemy count.
- Use Hemokinesis at low HP during split phase. The 2 HP self-damage compounds with split damage. One run died because Hemokinesis self-damage at low HP left no margin for the split's combined attacks.
- Enter below 50% HP. Even with a strong deck (Shockwave, Metallicize, Impervious), low entry HP leaves no buffer for the split transition.

---

## The Guardian (Act 1, HP: 240)

PATTERN:
- **Attack Mode**: Cycles through ATTACK (5x4=20), ATTACK (32 single hit), ATTACK_BUFF (8x2=16), DEFEND (gains block, no damage), STRONG_DEBUFF (no damage). Mode Shift counter tracks total damage dealt to Guardian. When counter reaches 0, switches to Defensive Mode. Counter starts at ~27-30 and increases each cycle.
- **Defensive Mode (Sharp Hide)**: Guardian gains Sharp Hide 3 -- deals 3 damage to player per Attack card played. Has its own attacks (9 damage, 8x2=16). After some turns, switches back to Attack Mode with higher Mode Shift counter.

KEY MECHANICS:
- **32-damage attack**: The Guardian's biggest single hit. Must have 32+ block capability in one turn or you die. Impervious (30 block) handles this. Double Metallicize (6/turn) + Intimidate (Weak, reduces to 24) also works.
- **Sharp Hide 3**: 3 damage to player per Attack card in Defensive Mode. Either block before playing Attacks to absorb retaliation, or play only Skills.
- **Mode Shift counter**: Increases each cycle, making Defensive Mode harder to trigger. Fast burst (Carnage+ at 28-42 damage) triggers Mode Shift quickly.
- **Long fight**: 240 HP means 12-14 turns minimum. Strength scaling and passive block pay off enormously.
- **Free turns**: DEFEND and STRONG_DEBUFF intents deal no damage. Use these for Bash+ (refresh Vulnerable), Inflame, Metallicize setup.

PREPARATION CHECKLIST:
1. One big block source for the 32-damage turn (Impervious, double Metallicize + Weak, or mass block cards)
2. Burst damage for fast Mode Shift triggering (Carnage+ at 28-42, Headbutt+ loops)
3. Passive block for the long fight (Metallicize is the best card; double Metallicize is exceptional)
4. Safety net (Fairy in a Bottle) -- not required but very helpful
5. Deck manipulation (Headbutt+ to guarantee key cards when needed)
6. Enough cards in deck to last 12+ turns -- do NOT over-exhaust

STRATEGY:
- **Turn 1 setup**: Play Metallicize, Inflame, or other Powers on the first free turn.
- **Attack Mode**: Block on attack turns (especially the 32-damage turn). Damage on free turns. Refresh Vulnerable with Bash+ on free turns.
- **Defensive Mode**: Block first to absorb Sharp Hide retaliation, then play Attacks. Or play only Skills for pure block. Powers are safe (no Sharp Hide trigger).
- **Headbutt loops**: Headbutt places key cards on top of draw pile. Guarantee Carnage+ for burst turns, Bash+ for Vulnerable refresh, or Impervious for the 32-damage turn.
- **Know your block ceiling**: Calculate maximum block your remaining cards can produce. If that's less than 32, stop exhausting immediately.

WHAT NOT TO DO:
- Over-exhaust. A 3-card deck cannot block 32 damage. Keep enough cards to survive.
- Play unupgraded True Grit. Random exhaust can destroy key cards. True Grit+ (chosen exhaust) is mandatory.
- Ignore Sharp Hide. Playing 3 Attack cards in Sharp Hide mode costs 9 HP. Block first.
- Enter without a plan for the 32-damage turn. If your maximum block is under 25, you will die.

---

## Hexaghost (Act 1, HP: 250)

PATTERN:
- **Turn 1**: Does NOT attack. Intent UNKNOWN. Free setup turn.
- **Inferno**: 7x6 = 42 damage (multi-hit). Weak reduces each hit: floor(6*0.75)=4 per hit = 28 total. This is the most dangerous attack.
- **ATTACK_DEBUFF**: Moderate damage + adds Burn status cards to deck.
- **DEFEND_BUFF**: Gains block and +Strength. No attack. Free turn for damage and Vulnerable refresh.
- **Medium attacks**: 4-8 and 14-24 damage on non-Inferno attack turns.
- **Block**: Can gain 12+ block.
- **Fight length**: ~13 turns. Long fight.

KEY MECHANICS:
- **Inferno (42 damage)**: Multi-hit means each hit is checked against block individually. Without Weak, this is near-impossible to survive. With Weak: 28 total, which is survivable.
- **Burn cards**: Unplayable status cards. Deal 2 damage per Burn in hand at end of turn AND clog hand (fewer real cards). Burns accumulate over the fight and create a death spiral.
- **Strength scaling**: Hexaghost gains Strength on DEFEND_BUFF turns, making subsequent attacks stronger. Long fight = more Strength = more dangerous.
- **Turn 1 free**: Use this for setup: Thunderclap (Vulnerable ALL), Metallicize, Powers.

PREPARATION CHECKLIST (must have at least 2 of 3):
1. Weak source (Shockwave, Clothesline, Intimidate, Weak Potion) -- reduces Inferno from 42 to 28. MANDATORY.
2. HP above 70% OR Pantograph relic (heals to full at boss start).
3. Passive block (Metallicize) OR Impervious for the Inferno turn.

If you have 0-1 of these, Hexaghost will likely kill you.

DAMAGE OUTPUT MATTERS: Weak and block keep you alive, but insufficient damage is equally fatal. In 13+ turn fights, Burns accumulate to 3-5 cards dealing 6-10 HP/turn in self-damage alone. Two runs died with Weak sources (Clothesline, Disarm) because they lacked the damage output to end the fight before Burns overwhelmed them. Damage scaling cards (Rampage, Inflame, Reaper) shorten the fight and reduce total Burns damage.

WHAT WORKS:
- Disarm (-2 Str permanently) -- reduces all Hexaghost attacks including each Inferno hit. Very effective.
- Rampage+ -- scales over the long fight to 40-60+ damage per play. One of the best Hexaghost-killing cards.
- Torii relic -- reduces each 2-damage Burn to 1 damage (halves Burns attrition). Does not save the fight alone but significantly extends survivability.

STRATEGY:
- **Turn 1 (free)**: Set up. Play Thunderclap for mass Vulnerable. Play Metallicize. Play Powers.
- **Save Weak for Inferno**: Apply Shockwave/Clothesline/Intimidate on the first Inferno turn to reduce 42 to ~28.
- **Play Metallicize early**: 3 block/turn over 13 turns = 39 free block. Set up as soon as possible.
- **Reapply Vulnerable with Bash+**: Use DEFEND_BUFF (free) turns to refresh Vulnerable without spending block resources.
- **Burns management**: Exhaust Burns with True Grit+ if available. Burns deal cumulative damage -- 3 Burns = 6 damage/turn + 3 fewer real cards.
- **Kill speed matters**: Shorter fight = fewer Burns accumulated = less attrition damage. Inflame (+2 Str) on turn 1 shortens the fight by 2-3 turns.

WHAT NOT TO DO:
- Fight without a Weak source. Inferno at full power (42) is near-unsurvivable.
- Play Brutality. Burns + Brutality self-damage = 3-5 HP/turn death spiral.
- Play Berserk. Self-Vulnerable + Inferno = death.
- Enter below 70% HP without Pantograph. The 250 HP + Inferno + Burns demands a large HP buffer.
- Waste Shockwave on a non-Inferno turn.
