# Exploration Directives

Written by Curate agent after first audit of the knowledge system (Runs 1-187).

## Directive 1: Corruption+FNP Without Strength Sources

**Hypothesis:** The exhaust/block engine (Corruption + Feel No Pain + Body Slam) can win independently of Strength scaling. Run 187 won with Corruption+FNP as the primary engine (Spot Weakness and Red Skull were supplementary), but we have never tested a run where the player explicitly avoids Strength sources to validate the engine in isolation.

**Test:** Play 3 runs building around Corruption+FNP. If Inflame, Spot Weakness, or Demon Form are offered alongside FNP or Corruption, take the engine piece (FNP/Corruption) instead. Take Strength sources ONLY if no engine piece is available. Goal: determine whether Body Slam + block scaling alone can defeat Act 3 bosses without any Strength.

**Success criteria:** At least 1 win or 2 runs reaching Act 3 boss. If all 3 die in Act 2, the engine may genuinely need supplementary Strength for hallway fights.

**Why this matters:** The playbook was overfitted on Strength as the sole damage scaling path. If this test succeeds, it validates the rebalanced drafting heuristics. If it fails, we need to document specifically WHERE the engine breaks down (hallway fights? bosses? Spheric Guardian?) and add conditional guidance.

## Directive 2: Corruption+FNP vs Spheric Guardian Data Collection

**Hypothesis:** Corruption+FNP can reliably beat Spheric Guardian without Strength. One observation exists (from observations.md: "Corruption + FNP successfully defeated Spheric Guardian with only 12 HP lost"). Need more data points.

**Test:** When playing Corruption+FNP runs from Directive 1, deliberately record the Spheric Guardian fight outcome if encountered: turns taken, HP lost, block generated, Body Slam damage dealt. This is a data collection directive, not a separate run.

**Why this matters:** The old "Strength Scaling Is Mandatory" section used Spheric Guardian as its primary justification. If the exhaust engine reliably beats SG, the argument for Strength-only is definitively refuted.

## Directive 3: Watcher Archetype Development

**Status:** 0 wins in 5 runs (best: Floor 33). The Watcher has no documented winning archetype in archetypes.md. This is the biggest character coverage gap.

**Test:** Play 3 Watcher runs. Focus on identifying which engine works: Stance dancing (Wrath/Calm cycling), Mantra scaling, or Pressure Points. Document what kills the run and what feels close to working.

**Why this matters:** With 5 runs and zero wins, we need data before we can write meaningful Watcher heuristics. The current `heuristics/characters/watcher.md` likely has minimal guidance.
