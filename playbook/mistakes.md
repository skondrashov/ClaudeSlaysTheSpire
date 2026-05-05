# Mistakes

Documented mistakes from actual runs. Each entry explains what went wrong and what to do differently.

## Run 1: No AOE for Slime Boss split

- Floor 16, died to Slime Boss (Ironclad, A0)
- After Slime Boss split into Spike Slime (L) + Acid Slime (L), we had no way to damage both at once. Each turn we could only damage one enemy while the other attacked freely.
- Combined incoming damage was 25-35 per turn from both slimes, and Frail reduced our block cards. We couldn't keep up.
- Lesson: Before the Act 1 boss, look for AOE damage cards (Cleave, Whirlwind, Immolate, etc.). Slime Boss split is one of the hardest things to deal with without AOE.
- Confidence: MEDIUM (one run, but the cause of death is clear)

## Run 1: Berserk in a dangerous fight

- Played Berserk during the Slime Boss fight, applying Vulnerable to ourselves
- At 23 HP against two enemies dealing 25+ damage per turn, making ourselves take 50% more damage was nearly suicidal
- The extra energy from Berserk didn't help because we spent it all trying to survive the extra damage we were taking
- Lesson: Berserk is only safe when enemies are not attacking (debuff-only turns) or when you have enough block to absorb all incoming damage including the Vulnerable penalty. In a desperate fight, it's a trap.
- Confidence: MEDIUM (one run, but the logic is sound)

## Run 1: Slimed cards overwhelmed the hand

- Against the slime enemies, Slimed cards accumulated in the deck and regularly showed up 2-3 per hand
- With 5 card draw and 3 Slimed, only 2 real cards to work with
- We did try to exhaust them when possible (playing them for 1 energy each), but it wasn't enough
- Lesson: Exhaust Slimed cards as a priority — every Slimed card exhausted is one fewer dead draw for the rest of combat. Cards that exhaust multiple cards (like Fiend Fire, Burning Pact) are very strong against slimes.
- Confidence: MEDIUM (one run, clear pattern)

## Run 1: Confused Weak and Vulnerable math (floor 10)

- On floor 10 (3 Louses), after playing Berserk (which makes YOU Vulnerable), the player said "4 dmg each while Weakened" to describe their own Strikes. But the player was Vulnerable (takes more damage), not Weakened (deals less damage). The player was not Weakened at all — no enemy had applied Weak.
- Additionally, Strike base damage is 6, and being Weakened would make it floor(6 * 0.75) = 4. But being Vulnerable doesn't affect YOUR damage output — it affects damage you TAKE. The player's Strikes should still deal 6 damage.
- The player may have been confusing debuff directions: Vulnerable on yourself = you take 50% more damage from enemies. Weak on yourself = you deal 25% less damage. They are different debuffs with different effects.
- Lesson: Always track which debuffs are on you vs. on the enemy. Vulnerable on self = incoming damage danger. Weak on self = outgoing damage reduction. Don't confuse them.
- Confidence: HIGH (the log clearly shows the player said "Weakened" when they had Vulnerable)

## Run 1: Took Berserk without understanding it (floor 7)

- The player took Berserk as a card reward saying "I dont know exactly what it does but rare powers tend to be game-defining." This is a dangerous heuristic — Berserk's self-Vulnerable makes it one of the most punishing Ironclad cards if misused.
- Later, on floor 10, the player played Berserk in a 3-Louse fight to "see the effect." Testing a card in a real fight against 3 enemies is risky — if the self-Vulnerable had coincided with all 3 attacking, it could have been fatal.
- On floor 16 (Slime Boss), Berserk was played at 23 HP against split slimes dealing 36 damage combined. The self-Vulnerable was near-fatal.
- Lesson: Don't take cards you don't understand just because they're rare. And don't test unknown cards in dangerous fights. If you must test, do it against a single weak enemy.
- Confidence: HIGH (directly contributed to death in Run 1)

## Run 1: Fight against Spike Slime (L) took too long (floor 11)

- The Spike Slime (L) fight took 8+ turns (floor 11). This is a single hallway enemy — fights this long drain HP through attrition even when individual turns are survivable.
- The deck at this point was mostly Strikes and Defends with Bash, Hemokinesis, and Berserk. Not enough damage density to close out fights quickly.
- The slime also split into medium slimes during the fight, extending it further.
- Lesson: If hallway fights are taking 6+ turns, the deck needs more damage or better damage quality. Long fights against debuff enemies (Frail from Spike Slime) are especially punishing because the debuff accumulates.
- Confidence: MEDIUM (1 fight, but the pattern of "too slow = death by attrition" is clear)

## Run 1: Deck too thick at boss time

- By floor 16 (Slime Boss), the deck had accumulated many cards: 4 Strikes, 4 Defends, Bash+, Berserk, Hemokinesis, Clothesline, Shockwave+, Shrug It Off, Ghostly Armor (15 cards). Only 1 Strike was removed (Neow).
- With a 15-card deck and 5-card draw, key cards like Shockwave+ and Bash+ appear every 3 shuffles on average. Against the boss split, the player needed specific cards (Shockwave for mass debuff, block cards) and couldn't reliably draw them.
- Slimed cards added during the fight made this worse — a 15-card deck diluted by 3-4 Slimed cards becomes ~19 cards, with ~20% being dead draws.
- Lesson: Deck thinning is important. Remove Strikes (and Defends if you have better block) at shops and events. A 10-12 card deck draws key cards much more reliably than a 15+ card deck. The Run 0 deck that beat The Guardian seemed to have higher-quality cards doing double duty.
- Confidence: MEDIUM (comparing Run 0 success vs Run 1 failure — thinner deck with multi-purpose cards won, thicker deck with basic cards lost)

## Run 1: No damage plan for post-split (floor 16)

- Before the boss fight, the player had Shockwave+ as their main tool for handling the split. But Shockwave+ applies debuffs — it doesn't deal damage or provide block.
- After the split, the player had no way to kill one slime quickly. Strike deals 6 damage per card against ~65 HP enemies. At that rate, killing one slime takes 5+ turns of dedicated attacks.
- Lesson: For Slime Boss, you need both mass debuff AND the ability to kill one slime fast after the split. A single big attack (like Hemokinesis with Vulnerable) helps, but the deck needed more burst — something like Bludgeon, Carnage, or Uppercut to delete one slime before the combined damage overwhelms you.
- Confidence: MEDIUM (1 boss attempt, but the arithmetic is clear — Strike spam can't kill fast enough)

## Run 2: Unupgraded True Grit destroyed the deck (Guardian fight)

- True Grit (unupgraded) exhausts a RANDOM card from hand. Over the course of the Guardian fight, True Grit randomly exhausted Whirlwind, Bash, and Pommel Strike — three of our best cards.
- By turn 12, the deck was down to 3 cards (Defend, Iron Wave, True Grit). This could only generate 17 block from cards + 3 Metallicize = 20 block per turn. The Guardian's 32-damage attack was lethal.
- True Grit+ (upgraded) lets you CHOOSE which card to exhaust. This is one of the most important upgrades in the game. The difference between random and controlled exhaust is the difference between winning and losing the boss fight.
- Lesson: NEVER play unupgraded True Grit in a thin deck where it could exhaust irreplaceable cards. If True Grit is in your deck, upgrading it should be the #1 priority at every rest site. Alternatively, only play True Grit when you have expendable cards in hand (Strikes, Defends, status cards).
- Confidence: HIGH (directly caused death in Run 2)

## Run 2: Over-exhausted during Guardian fight

- The exhaust synergy (Dark Embrace + Charon's Ashes + True Grit) seemed powerful — every exhaust drew a card and dealt 3 AOE damage. But exhausting too many cards left the deck too thin to survive the Guardian's high-damage attacks.
- The deck went from ~12 cards to 3 cards over 14 turns. A 3-card deck generates maximum 17 block per turn (Defend 5 + Iron Wave 5 + True Grit 7). The Guardian's 32-damage attack overwhelms this.
- Lesson: Exhaust synergy is powerful but has diminishing returns. Stop exhausting when your remaining deck can no longer survive the biggest enemy attack. Calculate the "survival floor" — minimum block you need — and make sure you keep enough block cards to reach it.
- Confidence: HIGH (Run 2 death, clear cause)

## Run 2: Entered Guardian fight at 16 HP

- Going into the Act 1 boss at 16/85 HP left almost no margin for error. The Guardian has attacks of 20 and 32 damage. At 16 HP, even one turn of imperfect blocking is fatal.
- The low HP was accumulated from Act 1 hallway fights and an elite (Gremlin Nob at floor 12 left us at 29 HP, and we continued taking damage).
- CORRECTION: Player entry says "Gremlin Nob at floor 12" but log shows Gremlin Nob was floor 10 (second elite). Lagavulin was floor 6 (first elite). HP trace: 82 HP -> Lagavulin fight -> 35 HP (+6 Burning Blood = 41 HP?) -> Slaver floor 7 -> ... -> Gremlin Nob floor 10 at 29 HP -> survived at 3 HP -> Fairy revived at 25 HP -> Slaver floor 11 -> Fungi floor 11 -> ... -> Rested at floor 15 to ~46 HP. Wait, player says they entered Guardian at 46 HP after resting (line 551), not 16 HP. The 16 HP figure needs verification — it may refer to HP partway through the Guardian fight, not at the start.
- ANALYST NOTE: The player actually entered the Guardian fight at approximately 46 HP after resting (player's own reasoning at line 551: "46 HP, 14 cards"). The "16 HP" in the run summary may refer to HP during the fight after taking damage, not entry HP. The entry HP of 46/85 (54%) is still low but more survivable than 16 HP.
- Lesson: Path planning should avoid elites when HP is low. If HP is below 30% going into the boss, the run is already compromised. Consider whether to fight the elite or take a safer path. Rest sites before the boss are critical.
- Confidence: MEDIUM (Run 2 — HP trace partially corrected, entry HP was ~46 not 16)

## Run 2: Skipped Reaper because of "don't take unknown cards" rule

- Floor 5 card reward offered Reaper, Flex, and Rage. Player skipped all three, citing the Run 1 lesson: "don't take cards you don't understand."
- Reaper is one of the strongest Ironclad cards — it deals damage to ALL enemies and heals based on damage dealt. It would have provided badly-needed sustain throughout Act 1.
- The "don't take unknown cards" rule was learned from Run 1 (Berserk disaster), but it's too broad. Berserk was dangerous because it had a hidden downside (self-Vulnerable). Reaper is unlikely to have a hidden downside — it's a straightforward healing attack.
- Lesson: Refine the rule to "don't take unknown cards that might have hidden costs (self-damage, self-debuffs, curses)." Unknown cards that seem purely beneficial (damage + heal) are worth taking. If unsure, check whether the card has the word "lose," "take damage," or applies a debuff to yourself.
- Confidence: MEDIUM (Run 2 — skipping Reaper was likely a strategic error, though we can't be certain without playing it)

## Run 2: Living Wall event — removed Strike instead of upgrading True Grit

- Floor 8 Living Wall event offered [Grow] Upgrade a card, [Change] Transform a card, and [Remove] Remove a card (exact options uncertain). Player initially reasoned they would upgrade True Grit to True Grit+ (the #1 priority), but instead chose to remove a Strike.
- The player's own reasoning said "upgrade True Grit to True Grit+ which lets you CHOOSE the exhaust target instead of random" — they knew this was critical. But then the event presented a card removal option and they pivoted: "Even though I wanted to upgrade True Grit, free card removal is still excellent."
- This was the single most consequential mistake of the run. True Grit+ (chosen exhaust) vs True Grit (random exhaust) was literally the difference between Run 0 (Guardian victory with True Grit+) and Run 2 (Guardian death from True Grit randomly exhausting key cards).
- The rest site on floor 15 was the last upgrade opportunity, but at 21 HP the player correctly prioritized resting over smithing.
- Lesson: Upgrading True Grit is ALWAYS higher priority than removing a Strike. A 12-card deck with True Grit+ beats an 11-card deck with unupgraded True Grit. Upgrade before remove when the upgrade is this impactful.
- Confidence: HIGH (Run 2 — this directly caused the death; Run 0 confirmed True Grit+ wins the Guardian fight)

## Run 2: Player stopped reasoning during Guardian fight (turns 7-14)

- Starting from approximately turn 7 of the Guardian fight, all reasoning fields in the log are empty strings (""). The player played 8+ turns of the most critical fight of the run with zero documented reasoning.
- The late-game turns (10-14) were when the deck was thinning dangerously from True Grit random exhaust. Without reasoning, the player had no framework to notice "my deck is now 5 cards and True Grit might exhaust my last damage card."
- The exhaust-counting and block-ceiling calculations that could have saved the run required explicit reasoning. Playing on autopilot guaranteed the player would miss the tipping point.
- Lesson: NEVER stop reasoning during a boss fight. The later turns are MORE important than the early turns — that's when resources are depleted and mistakes are fatal. If anything, the reasoning should get MORE detailed as the fight progresses.
- Confidence: HIGH (Run 2 log confirms empty reasoning fields from turn 7 onward)

## Run 2: Wasted 1 energy on Guardian turn 1

- Turn 1 of the Guardian fight: 5E available (3 base + 2 Ancient Tea Set). Player spent: Metallicize (0E, from potion) + Dark Embrace (2E) + True Grit (1E) + Strike (1E) = 4E. 1E was wasted.
- That 1E could have been a Defend (5 block) which would have reduced damage taken on a subsequent turn. Over a 14-turn fight, every HP matters — especially when the player entered at ~46 HP.
- Lesson: On high-energy turns (Ancient Tea Set, Snecko Oil), always count total energy and plan to spend ALL of it. Wasted energy in boss fights is wasted survival.
- Confidence: MEDIUM (Run 2 — 1E wasted is minor but the principle matters)

## Run 3: Played Defend targeting Chosen instead of a third Strike (floor 20, death turn)

- The player needed to deal 18 damage to kill Chosen at 18 HP. With Inflame (+2 Str) and Weakened, each Strike deals floor((6+2)*0.75) = 6 damage. Three Strikes = 18 = exact lethal.
- The player executed: `play 6; play 4 0; play 3 0; play 2 0` which translated to Inflame (Power, 0E), Strike (1E), **Defend** (1E), Strike (1E). The second card played was a Defend, not a Strike.
- Defend is a Skill card. It deals 0 damage even when "targeting" an enemy. It also triggered Hex (adding a Dazed to draw pile). The player wasted 1 energy on 0 damage and 0 useful block (Chosen was about to deal 36 damage — 5 block is meaningless).
- Result: Only 2 Strikes landed = 12 damage. Chosen survived at 6 HP. Next turn, Chosen dealt 36 damage (28 after 8 block) and killed the player at 14 HP.
- **Root cause**: Card indices shift when you play cards. After playing Inflame (card 6) and Strike (card 4 -> now shifted), the next "card 3" was a Defend, not a Strike. The player did not re-index after each play.
- Lesson: ALWAYS re-count card indices after each card play. When a card is played from position N, all cards at positions > N shift down by 1. Plan the full sequence with shifted indices, or use the `turn()` batch command which handles this.
- **Secondary lesson**: When Hex is active, playing a Defend that doesn't save your life is double-punished — you lose 1 energy AND add a Dazed.
- Confidence: HIGH (Run 3 — directly caused death, card index shifting confirmed as root cause)

## Run 3: Byrd fight drained 58 HP (floor 16, Act 2)

- The Byrd fight lasted 12 turns. Player entered at 80 HP (post-Burning Blood heal) and exited at 22 HP. This is a 58 HP loss from a single hallway fight.
- Flight mechanic halves all damage, making Byrds extremely tanky. With 3 Byrds, each regenerating Flight on buff turns, the fight becomes an attrition war the player cannot win quickly.
- The deck lacked efficient ways to strip Flight. Thunderclap (4 AOE + Vulnerable) is the only AOE and it strips only 1 Flight per Byrd per use.
- The player correctly played Metallicize early (turn 3) for passive block, but 3 block/turn against 15-36 incoming from 3 Byrds is insufficient.
- Reaper was used once for 6 HP healing — helpful but not enough to offset 58 HP drain.
- Lesson: Act 2 Byrds require (1) more AOE to strip Flight efficiently, (2) multi-hit attacks to decrement Flight faster, (3) Strength scaling to make halved damage still meaningful. If the deck can't handle Flight enemies, consider pathing to avoid monster fights in early Act 2 until the deck improves.
- Confidence: MEDIUM (Run 3, 1 fight — devastating HP cost even with correct play)

## Run 3: Entered Chosen fight at 28 HP after Byrd attrition

- After the Byrd fight (22 HP + 6 Burning Blood = 28 HP), the player went directly into a Chosen fight with no rest site.
- At 28 HP, the player had very little margin. Chosen attacks escalate to 16+ damage per turn, and Weakened reduces the player's damage output. The fight lasted 6 turns and the player dealt 89 of 95 HP of damage — dying with Chosen at 6 HP.
- If the player had entered at 50+ HP, the extra 22 HP would have allowed surviving the final Chosen attack (28 damage after block) and killing it next turn.
- Lesson: After a brutally expensive fight like Byrds, prioritize healing (rest site, Reaper) before engaging the next monster. If no healing is available, consider event rooms or other non-combat paths.
- Confidence: MEDIUM (Run 3 — low HP entry directly contributed to death)

## Run 3: Hexaghost fight survived at 1 HP — nearly fatal Burns

- While the Hexaghost fight was a victory, surviving at 1 HP means any small optimization would have made the difference between winning and losing.
- Burns accumulated over the fight and dealt 2+ damage per turn in the late game. The deck had no way to exhaust Burns (no True Grit, no Burning Pact).
- The player used Skill Potions reactively during the fight. Using the Regen Potion earlier (turn 1 instead of turn 2) would have gained 1 additional HP of healing.
- The fight was 13 turns. If the player had Inflame (taken later from Power Potion in Act 2), every attack would have dealt 2 more damage, potentially shortening the fight by 2-3 turns and reducing Burn accumulation.
- Lesson: Against Hexaghost, (1) take Inflame or other Strength scaling BEFORE the boss for a shorter fight, (2) take burn-removal tools (True Grit+, Burning Pact) for late-fight safety, (3) use healing potions as early as possible in long fights.
- Confidence: MEDIUM (Run 3 — victory but dangerously close to death)

## Run 4: Only 1 upgrade in 28 floors — catastrophic upgrade discipline

- The player reached floor 28 with only a SINGLE upgrade (Bash+ on floor 27). In 28 floors, they visited 3 rest sites and rested at ALL of them instead of upgrading.
- Rest site decisions: Floor 8 (46% HP, rested to 60%), Floor 14 (45% HP, rested to ~59%), Floor 27 (50% HP, smithed Bash+). Only the final rest site was used for upgrading.
- The consequences were devastating throughout Act 2: unupgraded Iron Wave dealt 5+5 instead of 7+7. Unupgraded Bash applied 2 Vulnerable instead of 3. Unupgraded Uppercut applied 1 turn of debuffs instead of 2. Unupgraded Thunderclap dealt 4 instead of 7.
- Against Spheric Guardian (40 block + Barricade), unupgraded cards couldn't break through fast enough, costing 30+ HP. Against Centurion+Mystic, unupgraded attacks couldn't kill Mystic fast enough before Centurion's damage accumulated.
- **Root cause**: The player consistently chose to rest at 45-50% HP instead of upgrading. While resting at 45% HP before an elite is reasonable, resting at 45% HP before an unknown room is overly conservative. The HP threshold for "must rest" should be 35-40%, not 45-50%.
- **Compounding effect**: Each missed upgrade made subsequent fights harder, which drained more HP, which made the next rest site a "forced rest" too. This is a death spiral — not upgrading leads to harder fights leads to more HP loss leads to not upgrading.
- Lesson: (1) Upgrade at rest sites unless HP is below 35% or the next room is a known dangerous fight (elite, boss). (2) At 45-50% HP with a rest site before unknowns, UPGRADE. (3) Prioritize upgrades over everything at the first rest site — the earlier an upgrade is applied, the more fights it improves. (4) Target upgrade priority: Bash > Iron Wave > Whirlwind > Thunderclap > Shrug It Off > others.
- Confidence: HIGH (Run 4 — 1 upgrade in 28 floors is the worst upgrade record across all 5 runs, directly contributed to Act 2 death)

## Run 4: Shop bug — exited shop without buying anything (395 gold wasted)

- Floor 22 (Act 2): Player entered a Shop with 395 gold. The shop screen appeared empty (no items displayed). Player sent `proceed` and exited the shop immediately without buying anything.
- The shop could have provided: card removal (75g removes a Strike), key cards (Inflame, Shrug It Off, etc.), relics, or potions. With 395 gold, the player could have afforded 2-3 purchases.
- **Root cause**: Likely a bug in cmd.py or state_formatter where the shop screen_state was not properly populated. The player saw an empty screen and assumed there was nothing to do.
- **Lesson**: If a shop screen appears empty, do NOT send `proceed`. Instead: (1) call `state` to inspect the raw screen_state, (2) try `choose 0`, `choose 1`, etc. to see if items exist but are not displayed, (3) the shop may have loaded but the display layer failed. `proceed` exits the shop and wastes the opportunity.
- **Impact**: 395 gold unspent is equivalent to ~5 card removals or 2 relics. This was one of the biggest missed opportunities in the entire run.
- Confidence: HIGH (Run 4, lines 735-737 in log — player entered shop, sent proceed, was on map screen next frame)

## Run 4: Entered Centurion+Mystic fight at 42/84 HP after no upgrades

- Floor 28 (Act 2): Player entered Centurion+Mystic fight at 42/84 HP (50%) with only 1 card upgrade (Bash+). The fight required 8 turns to kill Mystic, during which Centurion dealt ~22 damage unblocked. Player died at 1 HP unable to block 18 incoming.
- Contributing factors: (1) Spheric Guardian fight on floor 26 drained 30+ HP. (2) No healing between fights (only Burning Blood +6). (3) Unupgraded cards couldn't deal enough damage to kill Mystic quickly. (4) Missed shop meant no card improvements.
- If the player had 2-3 upgrades and the shop purchases, the deck would have been significantly stronger — likely killing Mystic 2-3 turns faster and surviving with HP to spare.
- Lesson: Act 2 is a gear check. If your deck enters Act 2 with 0 upgrades and 17+ cards of mostly basic quality, monster fights will drain HP faster than Burning Blood can recover. Upgrade discipline in Act 1 directly determines Act 2 survival.
- Confidence: HIGH (Run 4 — death was a direct consequence of accumulated underinvestment in deck quality)

## Run 4: Correct play — applied Run 1 lessons successfully

- NOTE: Not a mistake. Documenting what went RIGHT for reference.
- **Gremlin Nob**: Zero Skills played, clean 3-turn kill (applying Run 2/3 lesson). Strength Potion on free turn 1 maximized damage.
- **Slime Boss**: AOE cards (Thunderclap, Whirlwind) prepared for split (applying Run 1 lesson). Fiend Fire handled Slimed cards. First successful boss kill.
- **Card selection**: Every card taken was chosen with Slime Boss in mind (Thunderclap for AOE+Vuln, Uppercut for dual debuffs, Whirlwind for X-cost AOE). This is correct boss-prep deck building.
- **Target priority**: Correctly killed attacking slimes first, exhausted Slimed on free turns, targeted Mystic first in Centurion+Mystic.
- The run failed not from tactical errors but from strategic resource management (not upgrading, missing the shop).
- Confidence: HIGH (Run 4 — player demonstrably applied lessons from Runs 1-3)

## Run 5: Shop bug hit AGAIN — second time, 157g lost (floor 20)

- Floor 20 (Act 2): Player entered a Shop with 157+ gold. The shop screen appeared empty (same bug as Run 4). Player sent `proceed` and exited without buying anything.
- This is the SECOND occurrence in 5 runs (also happened Run 4 floor 22 with 395g). The player has now lost 550+ gold across two runs to this bug.
- **Root cause**: Same as Run 4 — likely bug in cmd.py or state_formatter. The player did not attempt the workaround documented after Run 4 (try `state`, then `choose` commands). The reasoning fields were empty at this point in the run (lines 631-634), suggesting the player may not have noticed the bug was recurring.
- **Lesson**: The workaround from Run 4 MUST be followed. Before entering ANY shop: call `state`, then probe with `choose` commands. NEVER send `proceed` as the first action in a shop. This is now documented twice and should be a hard rule.
- Confidence: HIGH (2 occurrences across Runs 4 and 5 — confirmed recurring bug)

## Run 5: Entered Gremlin Leader elite at 11 HP (13%) — unwinnable

- Floor 25: Player entered Gremlin Leader elite at 11 HP (13% of ~80 max). The fight was mathematically unwinnable from the start.
- **Why 11 HP**: The Centurion+Mystic fight (floor 22) drained HP to 4. Burning Blood +6 = 10 HP. Snake Plant fight (floor 23) drained some more. Joust event (floor 24) gave no healing. By the elite, HP was 11.
- **Despite excellent tactical play**: Impervious turn 1 (30 block), Disarm on Leader turn 3 (-2 Str), Shockwave turn 5 (mass Weak+Vuln on all enemies), gremlins killed efficiently — none of it mattered. DEFEND_BUFF rallies added +3 Str to all enemies each time. By turn 8, 49 incoming damage vs ~21 block.
- **The decision to fight the elite was the mistake**: At 11 HP, any Act 2 elite is suicide. The player should have taken an alternative path. If no alternative existed, using the rest site before the elite (if available) or drinking all potions for the fight.
- **Pattern**: This is the third run where low HP entry into an Act 2 fight caused death (Run 3: 28 HP into Chosen, Run 4: 42 HP into Centurion+Mystic, Run 5: 11 HP into Gremlin Leader). The pattern is clear and must be broken.
- Lesson: (1) Never enter an Act 2 elite below 60% HP. (2) If HP is below 30%, take ANY alternative path, even if it means skipping the elite entirely. (3) After a brutal fight (Centurion+Mystic), prioritize healing before the next combat room. (4) If the path forces an elite and HP is low, drink all potions at the start of the fight.
- Confidence: HIGH (Run 5 — third death from low HP entry into Act 2 fights)

## Run 5: Exhaust-heavy deck ran out of answers vs Gremlin Leader

- The Run 5 deck had 5 exhaust/ethereal cards: Impervious (Exhaust), Shockwave (Exhaust), Disarm (Exhaust), Carnage+ (Ethereal), True Grit+ (exhausts other cards). These are all excellent cards — but they are all one-time-use.
- In the Gremlin Leader fight (8 turns), all of these were consumed by turn 7. The remaining deck was: Strikes, Defends, Bash+, Headbutt, Searing Blow, Dropkick, Shrug It Off+, Thunderclap, Reaper. Against enemies with +6-9 Strength, this wasn't enough.
- **The core issue**: Exhaust cards front-load power into the first 5 turns. After that, the deck plays like a basic starter deck. Against enemies that scale (Gremlin Leader rallies), the first 5 turns aren't enough to win, and the remaining deck can't handle scaled enemies.
- **Contrast with Run 2**: Run 2 over-exhausted with True Grit (random exhaust thinned the deck to 3 cards). Run 5 had controlled exhaust (True Grit+ chose what to exhaust) but still ran out of tools. The lesson is similar but distinct: Run 2's problem was RANDOM exhaust destroying key cards. Run 5's problem was INTENDED exhaust leaving no answers for a long fight.
- Lesson: (1) Count your exhaust cards before a long fight. If more than 30% of your deck exhausts/is ethereal, the fight MUST be won in 5-6 turns or you'll be playing a weakened deck. (2) Against scaling enemies (Gremlin Leader, Cultist), avoid exhaust-heavy strategies unless you can kill before the scaling overwhelms. (3) Non-exhaust damage and block cards are the backbone of long fights — don't neglect them in favor of flashy exhaust cards.
- Confidence: MEDIUM (Run 5 — first clear example of exhaust depletion in a controlled exhaust deck, distinct from Run 2's random exhaust problem)

## Run 5: Centurion+Mystic took 12 turns — Headbutt 9 dmg left Mystic at 1 HP

- Floor 22: The Centurion+Mystic fight took 12 turns (matching the brutal length of Run 4). Player correctly targeted Mystic but Headbutt (9 damage) was insufficient against Mystic's ~15 block.
- **Headbutt does 9 damage, not 11**: The summary noted the player assumed Headbutt dealt 11. It deals 9. This miscalculation left Mystic at 1 HP instead of killing it, allowing Mystic to heal back. This extended the fight by 2+ turns.
- **Why this matters**: Each extra turn vs Centurion+Mystic costs ~12-18 HP from Centurion's attacks. Two extra turns = 24-36 HP lost, which was the difference between entering the Gremlin Leader at 35+ HP vs 11 HP.
- Lesson: (1) Check exact card damage values before committing to a kill sequence. (2) Against Mystic, use high-burst cards (Carnage+, Searing Blow) to break through block in one hit. Headbutt + follow-up is risky when Mystic gains 15 block per turn. (3) Leaving an enemy at 1 HP is the worst possible outcome — all the resources spent dealing 40+ damage were wasted because the last 1 HP healed back.
- Confidence: MEDIUM (Run 5 — Headbutt 9 damage confirmed from card entry, Mystic surviving at 1 HP reported in summary)

## Run 5: Correct play — applied lessons from Runs 1-4 successfully

- NOTE: Not a mistake. Documenting what went RIGHT for reference.
- **Gremlin Nob**: Zero Skills, 4-turn clean kill (applying Runs 2/3/4 lesson). Bash+ turn 1 on free turn, Headbutt for 13 Vuln damage + deck manipulation.
- **Guardian boss**: Beat The Guardian for the second time. Carnage+ + Headbutt loop for consistent 28-42 damage. Skill Potion -> Impervious for the 32-damage turn. Fairy as safety net. 12-turn fight.
- **Upgrade discipline**: 3 upgrades by Act 2 (Bash+, Shrug It Off+, Carnage+) — massive improvement over Run 4's 1 upgrade in 28 floors.
- **Card evaluation**: Took Reaper from Neow (applying Run 2 lesson of not skipping strong unknown cards). Took Carnage correctly evaluating Ethereal tradeoff. Took Dropkick for Vulnerable synergy.
- **Byrd fight**: 7 turns (vs 12 in Run 3). Carnage+ killed first Byrd turn 1, Thunderclap for AOE Flight stripping. Dramatically better than Run 3.
- **Target priority**: Correctly focused Mystic in Centurion+Mystic (applying Run 4 lesson).
- **The run failed from HP management** (entering Gremlin Leader at 11 HP) and the shop bug (157g lost), not from tactical errors.
- Confidence: HIGH (Run 5 — player demonstrably applied lessons from Runs 1-4, improvements are measurable)

## Run 6: Entered Book of Stabbing elite at 6 HP — 4th death from low HP entry

- Floor 24 (Act 2): Player entered Book of Stabbing elite at 6 HP (7% of 86 max). The fight was unwinnable from the start — despite dealing 140 damage in 5 turns (Book went 161->21), the player couldn't survive the scaling multi-hit attacks with Wound-clogged draws at 6 HP.
- **HP trace**: Entered Act 2 at 80/80 (full HP for first time!). Byrd fight drained to ~19 HP. Burning Blood +6 = 25 HP. Centurion+Mystic fight: Fairy consumed reviving at ~24 HP. Exit fight at ~5 HP. Burning Blood +6 = ~11 HP. Dropkick+ taken. Pleading Vagrant event (85g for relic). Ancient Writing (mass upgrades). Rest site: rested to ~6 HP? Book of Stabbing elite: died at 6 HP.
- **Why only 6 HP at rest site**: The Centurion+Mystic fight consumed the Fairy in a Bottle and left the player at ~5 HP. Burning Blood healed to ~11 HP. The rest site healed some but the player was still critically low.
- **Root cause**: The Byrd -> Centurion+Mystic -> Elite path is a death cascade. Each long fight drains 25-50 HP, Burning Blood cannot compensate (+6/fight), and there aren't enough healing opportunities between fights. The Fairy being consumed in Centurion+Mystic removed the safety net.
- **This is the 4th death from low HP entry** (Runs 3, 4, 5, 6). The pattern is unambiguous. The player must start making different pathing decisions to avoid this cascade.
- Lesson: (1) After ANY fight that drops you below 30% HP, the next room MUST be a rest site, shop, or event — not another monster/elite. (2) If the path forces elite after a brutal fight with no healing, skip the elite entirely (backtrack to a different path if possible). (3) Fairy in a Bottle should be saved for elites/bosses — using it in a hallway fight means no safety net later. (4) Consider: is the elite reward worth the risk of death? At 6 HP, no reward is worth the risk.
- Confidence: HIGH (Run 6 — 4th consecutive Act 2 death from low HP entry)

## Run 6: Fairy consumed during Centurion+Mystic — no safety net for elite

- Floor 21: Player deliberately took 24 damage (8x3 from Centurion) with only 6 Metallicize block, knowing Fairy in a Bottle would revive at ~24 HP. The Fairy was consumed here instead of being available for the Book of Stabbing elite 3 floors later.
- **Was this wrong?** The player had no choice — at 9 HP with 24 incoming damage, death was unavoidable. But the path leading to this point (Byrd fight draining to 25 HP, then Centurion+Mystic) is what caused the Fairy consumption.
- **Pattern**: In Run 5, Fairy was consumed in Centurion+Mystic fight (floor 22), then died to Gremlin Leader (floor 25). In Run 6, same pattern — Fairy consumed in Centurion+Mystic, then died to Book of Stabbing. Centurion+Mystic is consistently the fight that burns through Fairy.
- Lesson: (1) Centurion+Mystic is a Fairy-consuming fight. If you enter below 50% HP, expect to lose the Fairy. (2) Plan paths so that Fairy is available for elites, not consumed in hallway fights. (3) If Fairy is your only safety net, do not fight Centurion+Mystic at low HP — find an alternative path.
- Confidence: HIGH (Run 5 and 6 — same pattern in consecutive runs)

## Run 6: Correct play — significant improvements from Runs 1-5

- NOTE: Not a mistake. Documenting what went RIGHT for reference.
- **Entered Act 2 at full HP (80/80)**: First time ever. Previous best was Run 5 at 69/80. This was a major milestone — the Act 1 HP management was excellent.
- **Centurion+Mystic lesson applied**: Correctly killed Mystic first in the Centurion+Mystic fight (applying Run 4 lesson). Fight was still long but played correctly.
- **Feed card usage**: Brilliant use of Feed to kill Byrd (+3 Max HP) and Centurion (+3 Max HP) for +6 total Max HP. Used Headbutt+ to place Feed on top of draw pile for guaranteed kill shots. This is the kind of creative play that wins runs.
- **Ancient Writing event**: Chose [Simplicity] to upgrade all Strikes and Defends — approximately +8 upgrades. This massively improved deck quality. Strike+ (9 damage) and Defend+ (8 block) are significantly better than base versions.
- **Dropkick+ synergy**: Recognized and exploited the Vulnerable synergy — Dropkick+ was effectively free (1E cost, 1E refund, draw 1) against Vulnerable targets. Against Book of Stabbing, Dropkick+ dealt 36 total damage for 0 net energy.
- **Double Metallicize**: Setup 6 block/turn passive in both Guardian and Centurion+Mystic fights. This is a strong defensive foundation.
- **Upgrade discipline**: 4+ upgrades before Act 2 (Bash+, Pommel Strike+, Headbutt+, Thunderclap+), plus Ancient Writing for mass upgrades. Best upgrade record across all runs.
- **Guardian victory**: Third Guardian victory across all runs. Clean fight using Snecko Oil clutch turn + double Metallicize + Letter Opener passive damage.
- **The run failed from HP management** (6 HP into Book of Stabbing elite), not from card play or tactical errors. The player's tactical execution was the best yet.
- Confidence: HIGH (Run 6 — measurable improvements in upgrade discipline, HP management into Act 2, card synergy exploitation, and creative Feed usage)

## Run 7: No Weak source for Hexaghost — REGRESSION after 3 boss victories

- Floor 16, died to Hexaghost (Ironclad, A0) with boss at 61/250 HP remaining.
- **This is a regression**: Runs 4, 5, and 6 all beat their Act 1 boss. Run 7 died. The player had been improving steadily — this death breaks the winning streak.
- **Root cause #1 — No Weak for Inferno**: The deck had NO way to apply Weak (no Shockwave, no Clothesline, no Intimidate, no Weak Potion). Hexaghost's 7x6=42 Inferno attack hit at full power. Without Weak (reduces to 28), this multi-hit attack is near-impossible to survive.
- **Root cause #2 — Brutality in a long fight**: Brutality (0E Power, draw +1 card/turn, lose 1 HP/turn) was played early. In a 9-turn fight, this cost 9 HP minimum. Combined with Burns (2-4 HP/turn from unplayable status cards), the player lost 20-30 HP from self-inflicted damage alone.
- **Root cause #3 — Scrap Ooze event wasted 25 HP**: Player repeatedly reached inside Scrap Ooze (3 HP per attempt) and found no relic. Total HP lost: ~25. This left the player entering the boss at ~50/80 HP instead of ~75/80.
- **Root cause #4 — No Metallicize**: No passive block for the long fight. Run 3's Metallicize provided 39 free block over 13 turns. Run 7 had nothing.
- **Why this is a regression**: The player KNEW Hexaghost needs Weak (Run 3 Hexaghost Strategy section documents this clearly). But the card picks during Act 1 did not prioritize finding a Weak source. The deck focused on damage (Twin Strike, Pommel Strike+, Thunderclap) without solving the defensive problem.
- **Lesson**: (1) When Hexaghost is the boss, acquiring a Weak source is the #1 priority from floors 1-15. Take Clothesline, Shockwave, or Intimidate over almost anything else. Buy a Weak Potion at the shop if available. (2) Do NOT play Brutality against bosses with Burns or other end-of-turn damage sources. (3) Scrap Ooze at low HP is a trap — if you've lost 9+ HP (3 attempts) with no relic, stop and leave. (4) Verify the Hexaghost Checklist (Weak source + HP 70%+ + Passive block) before floor 16. If missing requirements, adjust card picks.
- Confidence: HIGH (Run 7 — clear regression, all 4 root causes identified, directly contradicts lessons from Run 3 that were already documented)

## Run 7: Brutality against Hexaghost — self-damage spiral

- Brutality (Power, 0E, draw 1 extra card/turn, lose 1 HP/turn) was played in the Hexaghost fight.
- Over 9 turns: 9 HP lost to Brutality. But more importantly, the extra draw didn't help enough — drawing 6 cards/turn instead of 5 doesn't matter when the deck lacks the answers (no Weak, no Metallicize). The extra card drawn was usually a Strike or Defend, not a game-changing answer.
- Combined with Burns dealing 2-4 HP/turn from turn 3 onward, the total self-inflicted damage was 20-30 HP over the fight. That's 40-60% of the player's starting HP wasted on self-damage.
- **RULE**: NEVER play Brutality against: (1) Hexaghost (Burns compound with self-damage), (2) Any fight expected to last 7+ turns, (3) When entering at less than 70% HP. Brutality is only safe in short fights (3-5 turns) or when Reaper/Feed can offset the HP drain.
- Confidence: HIGH (Run 7 — 9 HP from Brutality + 15-20 HP from Burns = 24-29 HP from self-damage in one fight. This alone would have kept the player alive long enough to potentially win.)

## Run 7: Scrap Ooze at low HP — lost 25 HP for nothing

- The Scrap Ooze event costs 3 HP per attempt with a 25% chance of finding a relic per attempt. The player attempted ~8 times (25 HP total) and found nothing.
- Expected HP cost for one relic: 12 HP (4 attempts on average). Getting unlucky with 8 attempts (25 HP) is within normal variance — but at ~75 HP going into the boss, spending 25 HP on a gamble is too risky.
- **Stopping rule**: At Scrap Ooze, set a maximum HP you're willing to spend BEFORE starting. If HP is above 80%, spend up to 12 HP (4 attempts). If HP is 60-80%, spend at most 6 HP (2 attempts). If HP is below 60%, LEAVE IMMEDIATELY.
- Run 3 got Lantern from Scrap Ooze on the first try (3 HP cost). Run 7 got nothing after 25 HP. The variance makes this event a gamble — only take it when you can afford to lose.
- Confidence: MEDIUM (Runs 3 and 7 — one success in 1 try, one failure in 8 tries. Event is high variance.)

## Run 8: Shockwave+ delayed to turn 4 against 3 Cultists — critical timing error

- Floor 20, died to 3 Cultists (Act 2 hallway fight) at 37/95 HP.
- **The critical mistake**: Shockwave+ was available in hand on turn 2 but was NOT played. Instead, Reaper was played on turn 2 for healing. Shockwave+ was finally played on turn 4.
- **By turn 4**, each Cultist had +9 Strength (3 Ritual/turn * 3 turns). Attacks were 15+ damage each. The Weak from Shockwave+ reduced turn 4 attacks from 15 to ~11 each — but turns 2 and 3 dealt full damage (27 + 36 = 63 total unmitigated damage from the 3 Cultists).
- **If Shockwave+ was played turn 2**: Turns 2-6 would all have Weak applied (-25% damage). Turn 2 goes from 27 to ~20. Turn 3 from 36 to ~27. That's ~16 HP saved on those two turns alone, plus Vulnerable on all enemies means faster kills = fewer total turns of damage.
- **Why the player chose Reaper instead**: Reaper heals based on damage dealt. On turn 2, the healing from Reaper was maybe 5-8 HP. But Shockwave+ would have PREVENTED 16+ HP of damage over turns 2-3. Prevention > healing.
- **General lesson**: In scaling fights (Cultists, Gremlin Leader), damage prevention cards (Shockwave+ Weak) ALWAYS take priority over healing cards (Reaper). The damage you prevent by applying Weak early far exceeds the healing from one Reaper use. Play Shockwave+ on the first attack turn, not later.
- Confidence: HIGH (Run 8 — turn 4 Shockwave+ vs turn 2 Shockwave+ is a 16+ HP difference. Timing is everything in scaling fights.)

## Run 8: Entered 3 Cultists at 37/95 HP with 0 potions

- Floor 20: Player entered the 3 Cultists fight at 37/95 HP (39%) with zero potions available. This is the 5th death from entering a fight at dangerously low HP.
- **HP pattern continues**: Runs 3 (28 HP), 4 (42 HP), 5 (11 HP), 6 (6 HP), and now 8 (37 HP) — every Act 2 death is preceded by entering a fight below 50% HP.
- **Zero potions**: With no potions to supplement healing or provide emergency block, the player had no safety net. A single Block Potion or Weak Potion on turn 2 could have extended survival.
- **Lesson**: The 50% HP minimum rule for Act 2 fights is now confirmed across 5 deaths. If HP is below 50% in Act 2, take alternative paths (events, rest sites, shops). If forced into combat, use ALL available potions aggressively on turn 1-2.
- Confidence: HIGH (Run 8 — 5th death from low HP entry, pattern is undeniable)

## Run 8: Shop bug — THIRD occurrence, workaround NOT followed

- Floor 11 (Act 1): Player entered shop. Called `state` (partial workaround), saw empty shop, then sent `proceed` to exit.
- The player did NOT try `choose 0`, `choose 1`, `choose purge`, or other probe commands. The workaround from Runs 4 and 5 was only partially followed.
- **This is the 3rd time in 8 runs (37.5%)** that the shop bug has cost the player. The workaround was documented after Run 4 and reinforced after Run 5, but is STILL not being fully executed.
- **The player must probe the shop with `choose` commands EVERY TIME the shop appears empty.** Calling `state` alone is not sufficient. The bug may be in the display layer while items are still selectable.
- Confidence: HIGH (3 occurrences across Runs 4, 5, 8 — workaround partially attempted but not fully executed)

## Run 8: Correct play — significant strengths despite death

- NOTE: Not a mistake. Documenting what went RIGHT for reference.
- **Feed mastery**: Feed accumulated +12-18 Max HP across multiple combats (Fat Gremlin, Slaver, Spike Slime during boss, Cultist). Starting from 80 Max HP, reached 95-98 Max HP. This is the best Feed usage across all runs.
- **Slime Boss victory**: Second successful Slime Boss kill. Used Shockwave+ for mass debuff, Feed for kill+Max HP during split phase. Clean boss execution.
- **Seeing Red+ utility**: Used 0E gain-2E card to enable multi-card burst turns. Excellent energy efficiency.
- **Reaper for sustain**: Used Reaper effectively in multiple fights for healing (though timing vs Shockwave+ was wrong in the death fight).
- **The run failed from** (1) Shockwave+ timing in the Cultists fight, (2) low HP entry into that fight, and (3) zero potions. The boss phase was played well — the Act 2 hallway fight was the problem.
- Confidence: HIGH (Run 8 — Feed usage and Slime Boss victory show significant improvement, death was from specific timing error + HP management)
