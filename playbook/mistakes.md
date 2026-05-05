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
