# Exploration Directives

Written by Curate agent. Updated after Run 190 (second audit cycle, Runs 1-190).

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

**Status:** Open

**Hypothesis:** The Watcher stance dance engine can win if execution errors (turn() index shifting, Blasphemy timing) are eliminated. Runs 189 and 190 both had working engines killed by misplays, not by the archetype being too weak.

**Test:** Play 3 Watcher Win runs (not Explore -- the goal is winning, not hypothesis testing). Specific execution rules:
1. NEVER use index-based card references in turn() batches. Use card NAMES in all turn() actions (e.g., `turn(["play Eruption 0", "play Strike 0", "end"])` not `turn(["play 1 0", "play 3 0", "end"])`).
2. NEVER play Blasphemy unless the kill is confirmed with exact arithmetic posted via think() first.
3. Post a fight strategy via think() before every elite and boss fight.

**Success criteria:** At least 1 win, or 2 runs reaching Act 2 boss. If all 3 die in Act 1 with correct execution, the engine has a fundamental problem.

**Why this matters:** We cannot distinguish "Watcher is weak" from "Watcher execution is error-prone" until the execution errors are eliminated. 2 of 3 Directive 3 deaths were execution failures. Fixing those is prerequisite to evaluating the archetype.

## Directive 5: Guardian Matchup for Watcher

**Status:** Open

**Hypothesis:** The Watcher needs specific Guardian preparation beyond generic stance dance guidance. Run 190 had a working engine but died to Guardian partly due to lacking a Wrath exit on a critical turn (Tranquility exhausted, only 1 Vigilance in the whole deck).

**Test:** Data collection, not a separate run. During Directive 4 runs, when Guardian is the Act 1 boss, record:
1. Number of Wrath exit sources in deck at boss time (Vigilance, Inner Peace, Empty Body, Fear No Evil, Tranquility).
2. Whether a turn occurred where Wrath exit was unavailable.
3. Sharp Hide damage taken per Mode Shift cycle.

**Why this matters:** The Guardian heuristic file has Ironclad, Silent, and Defect matchup sections but no Watcher section. The stance dance engine's reliance on Wrath exits makes Guardian uniquely dangerous -- Sharp Hide punishes attacks, and lacking an exit in Wrath doubles incoming damage. We need to document the minimum Wrath-exit density for the Guardian fight.
