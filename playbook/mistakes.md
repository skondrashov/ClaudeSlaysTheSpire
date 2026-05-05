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
