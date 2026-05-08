# The Guardian (Act 1, HP: 240)

PATTERN:
- **Attack Mode**: Cycles through ATTACK (5x4=20), ATTACK (32 single hit), ATTACK_BUFF (8x2=16), DEFEND (gains block, no damage), STRONG_DEBUFF (no damage). Mode Shift counter tracks total damage dealt to Guardian. When counter reaches 0, switches to Defensive Mode. Counter values by cycle: 30 (first), 40 (second), 50 (third). Triggering Mode Shift mid-attack CANCELS the current attack.
- **Defensive Mode (Sharp Hide)**: Guardian gains Sharp Hide 3 -- deals 3 damage to player per Attack card played. Has its own attacks (9 damage, 8x2=16). After some turns, switches back to Attack Mode with higher Mode Shift counter.

KEY MECHANICS:
- **32-damage attack**: The Guardian's biggest single hit. Must have 32+ block capability in one turn or you die. Impervious (30 block) handles this. Double Metallicize (6/turn) + Intimidate (Weak, reduces to 24) also works.
- **Sharp Hide 3**: 3 damage to player per Attack card in Defensive Mode. Either block before playing Attacks to absorb retaliation, or play only Skills.
- **Mode Shift counter**: Cycle values are 30, 40, 50. Triggering Mode Shift mid-attack cancels the attack -- this is the primary way to survive the 32-damage and 5x4=20 attacks. Fast burst (Carnage+ at 28-42 damage) triggers Mode Shift quickly. Plan damage output to trigger Mode Shift on lethal attack turns, not on free turns where it is wasted. CONFIRMED (Run 107): Only HP damage counts toward Mode Shift -- damage absorbed by block does NOT reduce the counter. Mode Shift was triggered twice in Run 107 to cancel attacks, confirming cancellation is reliable and repeatable.
- **Long fight**: 240 HP means 12-14 turns minimum. Strength scaling and passive block pay off enormously.
- **Free turns**: DEFEND and STRONG_DEBUFF intents deal no damage. Use these for Bash+ (refresh Vulnerable), Inflame, Metallicize setup.

PREPARATION CHECKLIST:
1. One big block source for the 32-damage turn (Impervious, double Metallicize + Weak, or mass block cards)
2. Burst damage for fast Mode Shift triggering (Bludgeon at 32-48, Carnage+ at 28-42, Headbutt+ loops)
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
- Use Fiend Fire as your primary exhaust engine. Fiend Fire exhausts 4+ cards (28+ damage) but thins the deck catastrophically. In Defensive Mode with Sharp Hide, the 9-card hand shrinks after one Fiend Fire, leaving insufficient block cards for 32-damage turns. Fiend Fire is excellent on free turns or for burst, but building the deck around it causes thin-deck syndrome mid-fight.
- Play Sever Soul. It exhausts ALL non-Attack cards in hand, including Defend cards. In a 12-14 turn fight, losing Defend cards permanently is catastrophic for block density on later turns. Even using Sever Soul to trigger Mode Shift is a bad trade if it costs 2+ Defend cards.
- Enter with fewer than 2 reliable block cards. Run 103: Pandora's Box removed all Defends, deck had only Iron Wave (5 block) and Flame Barrier (12 block, 2E) as block sources. Maximum block per turn was ~12, which cannot survive the 32-damage attack or sustain over 12+ turns. Disarm (-2 Str) and Dark Shackles (-9 Str, 1 turn) are damage reduction, not block -- they help but cannot substitute for actual block cards. If block density is this low before the boss, the run is likely unwinnable against Guardian.
- **Play Corruption or Corruption+ without Dead Branch or Feel No Pain.** Run 107: Corruption+ played on turn 9. Every Skill played after that point exhausted. By turn 14, ALL block Skills were gone -- zero Defends, zero Shrug It Off, zero Ghostly Armor, Impervious already used. Only Iron Wave (5 block) remained. Guardian was at 10/240 HP but the player died unable to block in the final turns. Corruption is a TRAP in this fight because the Guardian fight lasts 14+ turns and Corruption burns through all Skills in 5-6 turns. Without exhaust payoffs (Dead Branch replaces exhausted cards, Feel No Pain generates block per exhaust), Corruption leaves you defenseless for the second half of the fight.
- **Waste Impervious on small attacks.** Run 107: Impervious (30 block) was played on a 16-damage Sharp Hide turn (turn 6). This wasted 14 block. When the 32-damage turn came later, Impervious was already exhausted and unavailable. Save Impervious exclusively for the 32-damage attack or the 5x4=20 attack. Playing it against Sharp Hide attacks (9-16 damage) is a misallocation that can cost the fight.

CRITICAL DECK DENSITY WARNING:
The Guardian is a 12-14 turn fight. An exhaustion-heavy deck (Fiend Fire, Dark Embrace, Charon's Ashes) front-loads power into turns 1-5, but leaves a thin deck for turns 6-12. When the deck is reduced to 9-10 cards by turn 7, you cannot generate 20+ block on 32-damage turns. Fiend Fire + True Grit (unupgraded) is particularly dangerous: True Grit's random exhaust removes key cards, Fiend Fire exhausts the remainder, and the mid-fight deck becomes unplayable. Entered at 62 HP with Bash+, True Grit (unupgraded), and Fiend Fire. By turn 7, True Grit had randomly exhausted Bash+, and Fiend Fire had exhausted 3+ cards. On a 32-damage turn with only 5 playable cards left, maximum block was 9 (Defend + Shrug It Off). Died at 5 HP unable to block the final 32.

CORRUPTION DECK DENSITY DEATH (Run 107): Corruption+ played on turn 9 at 46 HP. The deck had 7 Skills (4 Defend, Shrug It Off, Ghostly Armor, Impervious -- Shockwave+ already used). Over turns 9-13, all Skills were played for free and exhausted. By turn 14, zero block Skills remained in the deck. Guardian was at 10/240 HP -- the closest near-win yet -- but the player had only Attacks and Iron Wave (5 block) left. Took 18+ unblocked damage per turn and died. KEY LESSON: Corruption is a different exhaustion mechanism than Fiend Fire but produces the same result -- no block cards in the second half. The player recognized the danger (reasoning: "DO NOT play Defends on free turn - they would exhaust for no value under Corruption!") but still ran out of Skills because the fight lasted longer than the Skill supply. This is now the SECOND Guardian death from deck-thinning (Run 103: Pandora's Box, Run 107: Corruption+).

TWO-DEATH GUARDIAN PATTERN (Runs 103, 107): Both Guardian deaths share the same root cause -- insufficient block density in the second half of the fight. Run 103: Pandora's Box removed Defends before the fight started. Run 107: Corruption+ exhausted all Skills mid-fight. The Guardian punishes ANY mechanism that reduces block card count below sustainable levels for a 14-turn fight.

---
