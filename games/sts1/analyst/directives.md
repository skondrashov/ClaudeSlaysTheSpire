# Exploration Directives

Written by Curate agent. Updated after the run 236-240 audit consolidation (seventh curation cycle). Run-222-era directives retired below.

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

**Census update (runs 236-240):** total feeds 10 → 4 → 14 → 7. The manual habit CAN take — run 239 recalled 10 hallway pages including a pre-routing recall, and its fights ran closest to book cost of any run in the series — but it does not stick (240 regressed to targeted-only). Two cautions now on record: (a) the first A9 WIN (run 237) read LESS than the 1-HP loss before it — the deck, not the habit, was the difference; do not let the victory teach "reading is optional." (b) Delivery is necessary but compliance binds at the death fight: run 239 died contradicting a page it had LOADED (chosen.md kill order). Persistent blind spots: boss-relic screens (run 236's costliest miss was the unread Ectoplasm/Black Star choice), final-boss entry (237's Awakened One, unread), Book of Stabbing (4 audited runs bare), own-deck card pages (one crack of daylight: run 240 recalled cards/Corruption at run start, directive-driven). The delivery mechanism remains the maintainer's call.

## Directive 11: Corruption-without-FNP — seed replay

**Status:** Open — ONE REPLICATION AUTHORIZED, then close regardless (run 240 attempted, audited: analyst/audits/run_240.md). Seed `3405875975300375922` (A9 Ironclad).

**Run 240 outcome:** Died floor 25 (Centurion+Mystic) from 47/80 — **predominantly interface races** (an eaten turn + a wrong-card resolution during relay lag; the race is since fixed at source), not the thesis. Route/pick controls held node-for-node both acts (comparison-integrity grade B). **Sub-question (a) ANSWERED: CONFIRMED, scoped to ~4-7 turn fights** — verified ledgers: Nob T1 4E of Skills free; Spheric Guardian 8 Skills at 0E (~9E saved) with Barricade banking the surplus; **Sentinel under Corruption is strictly energy-positive (0E play → block + 2E refund, mechanically clean)**; exhaust never bound before fight end. Counter-finding: Frail taxed ~30% of all engine block, and on the one matched Act 2 fight (solo Spheric F18) the engine paid 42 HP where the baseline's attack line paid 16 — net-positive energy per turn does NOT mean fight-level superiority in block-vs-block attrition. FNP never appeared on this seed (both shops verified). **Sub-question (b) — Snake Plant F31 with the engine — STILL UNCOLLECTED.**

**Replication (one only, conditions):** (1) identical draft/route — the run-240 controls carry over; (2) Spheric F18: the engine measurement is already collected — play it attack-led/cheaper to preserve HP (the run-240 death chain started with the 42-HP overpay there); (3) enter Book of Stabbing ≥ ~30 HP or bail pre-commitment, so **Smoke Bomb survives to Centurion+Mystic** (it saved the baseline there); (4) C+M: Mystic-first per the page, and apply the heal-arming rule — Mystic heals (priority, repeatable, +16 all enemies) once ANY enemy is missing 16+ HP, so burst Mystic past the kill inside one arm-window or hold damage entirely; (5) the prize is floor 31: survive to Snake Plant and price the Frail turn vs the baseline's death there. If the rerun dies pre-F25 for non-interface reasons, close with run 240's findings as final.

**Success criteria (unchanged):** Reach the Act 2 boss. Secondary: survive floor 31's Snake Plant with a priced Frail turn.

## Directive 12: Barricade/Body Slam — seed replay

**Status:** CLOSED — run 239 (audited: analyst/audits/run_239.md). **Primary criterion CONFIRMED-WITH-CAVEATS; archetype generality NEEDS-REPLICATION.** (Run 238 on this directive was a junk false-start — seed-format bug, fixed post-run.)

**Outcome:** Floor 22 PASSED (Snake Plant dead in 6 turns, low-water 32/80, vs the baseline's death there); Act 2 boss NOT reached (died floor 24, Cultist+Chosen — an allocation/potion execution error, not an engine failure, though Hex's tax on the engine's Skill-heavy setup is a real recorded weakness). Offer-stream question answered emphatically: Body Slam offered 5x, Barricade twice (F10 elite reward + Act 1 boss reward). This is the project's **first level-4 (controlled-comparison) evidence**: on this seed at A9, the engine beat the Strength+exhaust line in attrition fights (Lagavulin 25 vs 39 gross, Hexaghost 10 turns pre-Inferno vs 13, Shelled Parasite, the F22 pass) and LOST the races/mirrors (Nob +13 worse, Spheric +10 worse). Caveats: baseline F22 death had an execution-error component; favorable Snecko Confusion rolls (F22 conclusion robust to them); F12 ?-event diverged between runs; the own-Weak checklist post-dates the baseline. Curate: word the archetypes.md update per audit §3 — claim scoped to attrition fights on offer-supported seeds, A9 viability past early Act 2 still level 2.

**Replication:** spun out as Directive 14 (different-seed, opportunistic) — a same-seed rerun adds no rungs.

## Directive 13: Mummified Hand power-density build-around

**Status:** Open (opportunistic — no dedicated runs; activate whenever Mummified Hand is acquired).

**Hypothesis:** Mummified Hand (a random card costs 0 after each Power play) scales multiplicatively with Power count. A Power-dense Ironclad deck of cheap Powers (Inflame, Feel No Pain, Metallicize, Evolve) might sustain 5+ plays per turn. Prior observations: 2-4 free plays/turn in a 5-Power Ironclad deck and a 3-Power Silent deck; a recent A9 run's margin note proposes the build-around explicitly.

**Test:** When holding Mummified Hand, weight Powers up in drafting and tally free plays per turn per fight in thinks.

**Success criteria:** Evidence it sustains ≥2 free plays/turn across a run's fights → promote a build-around note to mummified-hand.md; otherwise record the ceiling.

## Directive 14: Barricade/Body Slam — different-seed replication

**Status:** Open (opportunistic — no dedicated runs; activate in any A9 run where Barricade + a Body Slam are offered by early Act 2).

**Hypothesis (the level-5 rung):** the attrition-fight advantage Directive 12 demonstrated on one seed generalizes across seeds. The archetypes.md entry is currently fenced to "offer-supported seeds, unproven past early Act 2" — this directive tests both fences.

**When activated, bias for:** (1) **Entrench** — the engine's missing piece; without it the wall peaked ~39/turn while hard scalers demand 60+ (observation filed: the wall is linear without Entrench and hard scalers outpace it); (2) **reaching the Act 2 boss** — the unmet secondary; Bronze Automaton's Stasis stealing Barricade (a Power, likely the deck's rarest card) is the untested catastrophic risk; (3) a Cultist+Chosen / Hex plan decided BEFORE T1 — commit one target per chosen.md's branch, potions converted early; (4) potion conversion discipline generally.

**Success criteria:** Reach the Act 2 boss with the engine online on a fresh seed. Record per-fight costs by fight type (attrition vs race vs mirror) so the fight-type-dependence claim can be tested, not just the engine's viability.

---

## Retired / Completed (archive)

- **Directive 1 (Corruption+FNP without Strength) and Directive 2 (Corruption+FNP vs Spheric Guardian data):** Run-222-era, never attempted as written; the meta moved to A9 and the question is superseded by the seed-specific Directive 11 and the "under investigation" markers in drafting.md. Retired.
- **Directive 3 (Watcher archetype), 4 (Watcher execution), 5 (Guardian for Watcher), 6 (Watcher first win):** Complete. Outcome: stance dance engine viable but knowledge surface too large; Watcher paused at 0/14 in favor of Ironclad. Findings live in the Watcher-specific heuristics and the-guardian.md.
- **Directive 7 (Ironclad win streak):** Complete — win on run 219 (A5, Corruption+FNP+Brimstone).
- **Directive 8 (Watcher Slime Boss data):** Retired as dormant — Watcher play is paused; the observations live in slime-boss.md's Watcher section. Re-open if Watcher resumes.
- **Directive 9 (Ironclad A5 consolidation):** Overtaken by events — play moved to A9 after the run 227 A5 win. The A9 campaign's findings are consolidated in the run 227-233 audits. Retired.
