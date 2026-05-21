# Exploration Directives

Written by Curate agent. Updated after Run 193 (third curation cycle, Directive 4 synthesis).

## Directive 1: Corruption+FNP Without Strength Sources

**Status:** Open (no Explore runs attempted yet)

**Hypothesis:** The exhaust/block engine (Corruption + Feel No Pain + Body Slam) can win independently of Strength scaling. Run 187 won with Corruption+FNP as the primary engine (Spot Weakness and Red Skull were supplementary), but we have never tested a run where the player explicitly avoids Strength sources to validate the engine in isolation.

**Test:** Play 3 runs building around Corruption+FNP. If Inflame, Spot Weakness, or Demon Form are offered alongside FNP or Corruption, take the engine piece (FNP/Corruption) instead. Take Strength sources ONLY if no engine piece is available. Goal: determine whether Body Slam + block scaling alone can defeat Act 3 bosses without any Strength.

**Success criteria:** At least 1 win or 2 runs reaching Act 3 boss. If all 3 die in Act 2, the engine may genuinely need supplementary Strength for hallway fights.

**Why this matters:** The playbook was overfitted on Strength as the sole damage scaling path. If this test succeeds, it validates the rebalanced drafting heuristics. If it fails, we need to document specifically WHERE the engine breaks down (hallway fights? bosses? Spheric Guardian?) and add conditional guidance.

## Directive 2: Corruption+FNP vs Spheric Guardian Data Collection

**Status:** Open (no data collected yet)

**Hypothesis:** Corruption+FNP can reliably beat Spheric Guardian without Strength. One observation exists (from observations.md: "Corruption + FNP successfully defeated Spheric Guardian with only 12 HP lost"). Need more data points.

**Test:** When playing Corruption+FNP runs from Directive 1, deliberately record the Spheric Guardian fight outcome if encountered: turns taken, HP lost, block generated, Body Slam damage dealt. This is a data collection directive, not a separate run.

**Why this matters:** The old "Strength Scaling Is Mandatory" section used Spheric Guardian as its primary justification. If the exhaust engine reliably beats SG, the argument for Strength-only is definitively refuted.

## Directive 3: Watcher Archetype Development

**Status:** COMPLETE (Runs 188, 189, 190). 0 wins, best Floor 20. See assessment below.

**Results:** Stance dance was the engine tested in all 3 runs. The engine assembled in 2 of 3 runs (189, 190) but both deaths were execution errors, not archetype failures:
- Run 188 (F12): Died to Lagavulin. Engine still assembling -- insufficient DPS for elite. Inconclusive.
- Run 189 (F20): Died to Blasphemy self-kill. Engine was online (Eruption+, Rushdown, Simmering Fury+, Deva Form+, Flurry of Blows+). Misplay.
- Run 190 (F16): Died to Guardian. Card-index shifting in batched turn() command caused accidental Wrath entry. Misplay.

**Assessment:** The stance dance engine is mechanically sound. When it assembled (runs 189, 190), the player's strategic plan was correct in both cases -- deaths were caused by execution failures (Blasphemy timing, turn() index shifting), not by the archetype being too weak. However, 0 wins in 8 total Watcher runs (best F33) means we lack proof the engine can actually close out a run. The data is muddied by execution errors. More runs are needed, but with the execution problems fixed first.

## Directive 4: Watcher Execution Cleanup Runs

**Status:** COMPLETE (Runs 191, 192, 193). 0 wins, best Floor 33. See assessment below.

**Results:** Execution was clean across all 3 runs — zero index-shift errors, zero Blasphemy self-kills. The execution rules worked. Deaths were all strategic/knowledge gaps:
- Run 191 (F24): Chosen+Byrd hallway. Hex debuff collapsed Skill-heavy engine (Dazed flooding). Knowledge gap: Watcher Hex counter-strategy.
- Run 192 (F25): Slavers elite at 40% HP. Sozu+Philosopher's Stone = no potions + harder fights. HP attrition from Snake Plant (Malleable punishes multi-hit). Knowledge gap: relic risk assessment, HP management.
- Run 193 (F33): Bronze Automaton at 36/300 HP. Kill was in hand (Smite + Strike = 36 damage in Wrath = exact lethal). Player miscalculated Tantrum+ damage as 12 (undoubled) instead of 24 (doubled in Wrath), thought they were 12 short, used Distilled Chaos "for insurance." Distilled Chaos randomly played Meditate+ (ends turn, 0 block) against 102 Hyper Beam. Dead. Knowledge gap: Wrath damage arithmetic, Distilled Chaos risk, potion ordering.

**Assessment:** Execution is solved. The execution rules from Directive 4 work — card names in turn() batches, Blasphemy arithmetic checks, fight strategy planning. The problem has shifted from "execution errors kill the player" to "knowledge gaps kill the player." The Watcher needs better matchup-specific heuristics (Hex, boss fight arithmetic, potion risk assessment). Run 193 was one correct arithmetic check away from winning. The stance dance engine is viable; the knowledge framework around it was insufficient. All 5 heuristic gaps flagged in the Run 193 audit have now been addressed in the playbook.

## Directive 5: Guardian Matchup for Watcher

**Status:** COMPLETE (data collected from Runs 190, 191, 193). Guardian matchup section added to the-guardian.md.

**Results:** Run 193 faced Guardian as Act 1 boss and won cleanly (12/72 HP remaining). The deck had 3 Wrath exit sources (Vigilance+, Empty Body, Meditate) and the fight lasted 10 turns. Run 190 died to Guardian with only 1 Wrath exit (Vigilance) — Tranquility had been exhausted. Run 191 beat Guardian (different boss RNG, not applicable).

**Assessment:** The Guardian Watcher matchup section has been written in the-guardian.md. Key finding: minimum 2 Wrath exit sources in deck. Run 193's clean Guardian win with 3 exits validates the threshold. The existing Guardian Watcher section (added after Run 190) already covers the critical points. No further data collection needed.

## Directive 6: Watcher First Win

**Status:** Open

**Hypothesis:** The Watcher stance dance engine can win now that execution is clean (Directive 4) and knowledge gaps have been addressed (Distilled Chaos warning, Wrath arithmetic rules, Hex counter-strategy, Bronze Automaton Watcher section, potion ordering rules). Run 193 was one arithmetic check away from an Act 2 boss kill. The playbook updates from this curation cycle should close the remaining gaps.

**Test:** Play 3 Watcher Win runs with the updated heuristics. Specific rules carry forward from Directive 4:
1. Card NAMES in turn() batches (never indices).
2. Blasphemy requires confirmed kill arithmetic via think().
3. Fight strategy via think() before every elite and boss.
4. NEW: NEVER use Distilled Chaos. Skip or ignore it.
5. NEW: On kill turns, play deterministic damage cards FIRST. Verify kill math BEFORE using any random effect.
6. NEW: In Wrath, double ALL damage numbers in kill math. Post the doubled calculation explicitly via think().

**Success criteria:** At least 1 win. If all 3 die, assess whether deaths are (a) new knowledge gaps (document them), (b) bad RNG (variance), or (c) archetype limitation (consider switching focus).

**Why this matters:** 11 Watcher runs, 0 wins. But the trajectory is positive: F12 -> F20 -> F16 -> F24 -> F25 -> F33. Execution is clean. Run 193 nearly won. The heuristic updates from this curation session address every flagged gap. If the Watcher cannot win in the next 3 runs with clean execution AND correct knowledge, we should shift focus back to Ironclad or Silent for efficient win production while continuing occasional Watcher runs for learning.
