# Exploration Directives

Written by Curate agent. Updated after Run 222 (fifth curation cycle, 7 audit flags addressed).

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

**Status:** COMPLETE (Runs 194, 195, 196). 0 wins in 3 runs. Failed. See assessment below.

**Results:** Execution was clean. All 3 heuristic rules (no Distilled Chaos, deterministic cards first, doubled Wrath math) were followed. Deaths were all new knowledge gaps or HP attrition:
- Run 194 (F16): Slime Boss. Slimed cards flooded the small deck, clogging draws. The Watcher lacks exhaust tools (no True Grit, no Fiend Fire equivalent) to manage Slimed. Knowledge gap: Watcher Slime Boss matchup.
- Run 195 (F45): Nemesis. Flurry of Blows damage miscalculation + Burns from Runic Pyramid clogged hand. Best Watcher floor ever (F45 = deep Act 3). Knowledge gap: Burns/Runic Pyramid hand-clog interaction, Nemesis intangible phase timing.
- Run 196 (F39): Spire Growth. Entered at 9 HP after Orb Walker drained HP (ended in Wrath with no exit + Burns). Constricted 10 + attack = 26/turn, max block 12. Unsurvivable. Root cause: HP attrition through Act 3 with no healing sources.

**Assessment:** The directive explicitly stated: "If all 3 die, assess whether deaths are (a) new knowledge gaps, (b) bad RNG, or (c) archetype limitation." Answer: primarily (a) new knowledge gaps, with (c) emerging as a secondary factor. Each death revealed a genuinely new gap (Slime Boss matchup, Burns/Runic Pyramid interaction, HP attrition without healing). But the pattern of "each run reveals yet another gap" after 14 total runs suggests the Watcher's knowledge surface is much larger than other characters. The Ironclad won on run 102 (after ~100 runs of learning). The Silent won on run 112 (after ~7 runs). The Defect won on run 126 (after ~2 runs). The Watcher at 14 runs has 0 wins and is still discovering fundamental matchup gaps.

The structural issue is now clear: **the Watcher has no built-in healing** (Ironclad has Burning Blood), **no built-in scaling defense** (Silent has poison for passive damage, Defect has passive orbs), and **Wrath doubles incoming damage**, creating a uniquely punishing feedback loop where any knowledge gap or suboptimal turn costs 2x the HP. This makes the Watcher strictly harder to pilot, requiring a larger knowledge base to survive the same encounters.

**Decision: Pause Watcher. Switch to Ironclad for efficient win production.** The Watcher knowledge base should be preserved and expanded incrementally. When we return to Watcher, we will have a stronger general knowledge base (boss matchups, encounter strategies) that transfers. But continuing to pour runs into a 0/14 character when Ironclad has proven it can win (5/122, and the recent win rate since run 184 is much higher) is not optimal resource allocation.

## Directive 7: Ironclad Win Streak

**Status:** COMPLETE (Run 219 = victory, satisfying success criteria)

**Hypothesis:** The Ironclad has 5 wins and two proven archetypes (Snecko+Str, Corruption+FNP+Barricade) plus a third (pure Str burst). The playbook is mature. Returning to Ironclad should produce wins more efficiently than continuing to debug the Watcher. Additionally, Ironclad wins generate transferable knowledge (boss behavior, encounter patterns, map pathing) that will benefit all characters including Watcher.

**Runs 216-222 results (7 runs):** 1 win (Run 219), 6 deaths. Death causes:
- Run 216 (F14): Double-end command bug (interface issue).
- Run 217 (F33): Sozu without healing card (strategic error, now in playbook).
- Run 218 (F22): Thunderclap/Vulnerable confusion (arithmetic error, now in checklist #8).
- Run 219 (F51): **VICTORY.** Corruption+FNP engine + Brimstone Str scaling. First Ironclad A5 win.
- Run 220 (F6): Routing into elite without rest site coverage at 12 HP.
- Run 221 (F50): Void status card drained 1E on lethal turn. Died by 1 HP to Awakened One. Flawless execution, RNG death.
- Run 222 (F10): Back-to-back elites with no rest between. No damage scaling vs Lagavulin.

**Assessment:** Success criteria met (1 win in Runs 219-222). The playbook corrections from audit 216-218 prevented recurrence of those failure modes. Run 219 demonstrated mastery of the Corruption+FNP engine. Post-win deaths (220-222) revealed two new systemic issues (route safety, damage scaling check) now addressed in the playbook. Run 221 was an RNG loss with flawless execution.

## Directive 8: Watcher Slime Boss Matchup (Data Collection)

**Status:** Open (passive -- collect data opportunistically, do not force Watcher runs)

**Hypothesis:** The Watcher needs AOE for Slime Boss split phase, but the Watcher's AOE options are limited (Conclude+, Wheel Kick, Windmill Strike for single-target). The stance dance engine is single-target focused. Slimed card flooding is uniquely punishing for the Watcher because the deck relies on drawing specific stance-change cards in the right order.

**Observation from Run 194:** Small deck + Slimed flooding = engine collapse. The Watcher has no exhaust tools for junk cards (unlike Ironclad's True Grit/Fiend Fire or Silent's Calculated Gamble).

**When Watcher runs resume:** If Slime Boss is the Act 1 boss, document: (a) deck size at time of fight, (b) AOE cards available, (c) Slimed management strategy, (d) outcome. Possible mitigations to test: larger deck size to dilute Slimed, Conclude+ as AOE finisher, Empty Mind to cycle past junk cards.

**This directive does not require dedicated runs.** It is a data collection note for when Watcher play eventually resumes.

## Directive 9: Ironclad A5 Consolidation

**Status:** Open

**Hypothesis:** The playbook has been significantly updated after Runs 216-222. Three systemic issues are now addressed: (1) route safety before elites, (2) damage scaling check before elites, (3) Normality + Corruption+FNP interaction. The Ironclad win rate at A5 should improve with these corrections. Runs 220-222 deaths had correctable root causes. Run 221 was RNG (flawless execution, died by 1 HP to Void).

**Test:** Play 3 Ironclad A5 runs with the updated playbook. Key behavioral changes to validate:
1. **Route safety rule:** Never commit to an elite without rest site coverage within 2 floors, or HP above 70%.
2. **Damage scaling before elites:** Verify at least one scaling source exists before routing through Act 1 elites.
3. **Normality management:** If Cursed Key is taken with Corruption engine, exhaust Normality immediately when drawn.
4. **Void awareness:** After Sludge adds Void, plan for potential 1E loss on critical turns.
5. All other existing heuristics (healing priority, potion timing, debuff verification, fight strategy planning).

**Success criteria:** At least 1 win in 3 runs. If 2+ wins, consider advancing to A6. If 0 wins, audit for new failure modes.

**Why stay at A5 (not advance to A6):** Only 1 win at A5 so far. The playbook needs validation that the post-Run-222 corrections work. Advancing before confirming the fixes risks compounding new ascension mechanics with unresolved routing/scaling issues.
