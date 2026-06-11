# Exploration Directives

Written by Curate agent. Updated after the run 227-233 audit consolidation (sixth curation cycle). Run-222-era directives retired below.

## Directive 10: Knowledge delivery to hallway fights and own-deck locks

**Status:** Open — PROBLEM STATEMENT ONLY. The delivery mechanism is a harness design decision **reserved for the maintainer; do NOT implement any auto-injection from an Explore or Curate session.**

**The problem (five consecutive audited runs, 229-233):** knowledge delivery reaches bosses (3/3 recalled with plans by run 233) and some elites, but hallway enemies at ~0/20 per run, and own-deck card pages never — the recall path only ever fires on enemies. It has been run-deciding three times:
- Run 229: Writhing Mass entered with both its pages on file, unloaded (~25-40 cost row, move table, re-roll rule).
- Run 232: centurion-mystic.md's 25-61 cost row and "put the full range on the ledger before routing in" instruction — written for exactly the routing decision that lost the run — unloaded at both the routing node and the fight.
- Run 233: battle-trance.md names verbatim the No-Draw interaction that killed the deepest A9 run (three in-fight violations); no delivery path covers a card in the player's own deck.
Codified hallway facts also get re-derived or misapplied repeatedly (thievery-through-block: four consecutive runs). The measured value of a loaded page is large (run 233: Champ with recall+plan ≈ net 0 HP vs Book of Stabbing bare ≈ -41).

**Candidate shapes (for the maintainer to choose among; audits 230-233 consistently show tool-level fixes stick where habit-level ones don't — choose-N and batch-energy families died only when the tool enforced them):**
1. Combat-start injection: at fight start the harness knows the enemy names; inject each present entity's heuristic core rule + expected-cost line (budget-capped, first encounter per run).
2. Extend injection to own-deck interaction locks: pages for deck cards with global locks (Battle Trance/No Draw, Velvet Choker, Normality, Dead Branch) at fight start.
3. Routing-time surfacing: act-level hallway cost tables in the win awareness manifest, so expected-cost rows are in context at MAP nodes, not just fights.
4. Habit backstop in the win goal: "before T1 of any fight not yet recalled this run, recall every named enemy" — cheap, but the evidence says insufficient alone.

**Until decided, Explore/Win runs should drill the manual habit (shape 4) and each audit should re-run the recall census** (boss/elite/hallway/event/card coverage) so the fix's effect is measurable when it lands.

## Directive 11: Corruption-without-FNP — seed replay

**Status:** Open. Seed `3405875975300375922` (A9 Ironclad).

**Context:** A run on this seed picked up a free Corruption at the burning Gremlin Nob (Power Potion on the free turn), explicitly tagged it "engine seed — need FNP," never completed the package, and died on floor 31 (Snake Plant) with strong Act 1 momentum wasted. A standing margin note also suggests Corruption alone (zeroing Skill costs) may be underrated even without FNP.

**Test:** Replay the seed. Priorities: complete the exhaust package (Feel No Pain, exhaust tools; Dead Branch if offered) around Corruption, and weight block density per the updated drafting checklist. Record: (a) whether Corruption-without-FNP turns were net positive before the package completes (energy saved vs cards lost to exhaust), (b) the Snake Plant fight cost with the engine vs without.

**Success criteria:** Reach the Act 2 boss. Secondary: survive floor 31's Snake Plant with a priced Frail turn.

## Directive 12: Barricade/Body Slam — seed replay

**Status:** Open. Seed `5894277716703663016` (A9 Ironclad).

**Context:** Flagged by the maintainer for a Barricade/Body Slam build-around attempt. The previous run on this seed went a Strength+exhaust line and died on floor 22 (Snake Plant, own-Weak omitted from kill math — that checklist item is now codified).

**Test:** Replay the seed building toward the Barricade + Body Slam block engine (Barricade, Body Slam, Entrench, block density; Corruption/FNP welcome but not the focus). The archetype has one win on record (Time Eater) but no A9 evidence.

**Success criteria:** Pass floor 22; reach the Act 2 boss. Record whether the offer stream actually supports the engine (card rewards are not logged, so note offers manually in thinks).

## Directive 13: Mummified Hand power-density build-around

**Status:** Open (opportunistic — no dedicated runs; activate whenever Mummified Hand is acquired).

**Hypothesis:** Mummified Hand (a random card costs 0 after each Power play) scales multiplicatively with Power count. A Power-dense Ironclad deck of cheap Powers (Inflame, Feel No Pain, Metallicize, Evolve) might sustain 5+ plays per turn. Prior observations: 2-4 free plays/turn in a 5-Power Ironclad deck and a 3-Power Silent deck; a recent A9 run's margin note proposes the build-around explicitly.

**Test:** When holding Mummified Hand, weight Powers up in drafting and tally free plays per turn per fight in thinks.

**Success criteria:** Evidence it sustains ≥2 free plays/turn across a run's fights → promote a build-around note to mummified-hand.md; otherwise record the ceiling.

---

## Retired / Completed (archive)

- **Directive 1 (Corruption+FNP without Strength) and Directive 2 (Corruption+FNP vs Spheric Guardian data):** Run-222-era, never attempted as written; the meta moved to A9 and the question is superseded by the seed-specific Directive 11 and the "under investigation" markers in drafting.md. Retired.
- **Directive 3 (Watcher archetype), 4 (Watcher execution), 5 (Guardian for Watcher), 6 (Watcher first win):** Complete. Outcome: stance dance engine viable but knowledge surface too large; Watcher paused at 0/14 in favor of Ironclad. Findings live in the Watcher-specific heuristics and the-guardian.md.
- **Directive 7 (Ironclad win streak):** Complete — win on run 219 (A5, Corruption+FNP+Brimstone).
- **Directive 8 (Watcher Slime Boss data):** Retired as dormant — Watcher play is paused; the observations live in slime-boss.md's Watcher section. Re-open if Watcher resumes.
- **Directive 9 (Ironclad A5 consolidation):** Overtaken by events — play moved to A9 after the run 227 A5 win. The A9 campaign's findings are consolidated in the run 227-233 audits. Retired.
