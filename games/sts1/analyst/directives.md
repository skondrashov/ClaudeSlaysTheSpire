# Exploration Directives

Written by Curate agent. Updated after the run 245 audit (tenth curation cycle — D16 widened from "price the forced elite" to "price EVERY forced child whose worst case exceeds current HP," incl. forced Monster rooms; structural fix landed in node-choice.md). Prior: runs 243-244 audits (ninth cycle — D16 added on commit-node blindness; D15 progress note). Run-222-era directives retired below.

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

**Census update (runs 236-242):** total feeds 10 → 4 → 14 → 7 → 3 → 10. The manual habit CAN take — run 239 recalled 10 hallway pages including a pre-routing recall, and its fights ran closest to book cost of any run in the series — but it does not stick (240 regressed to targeted-only; 241 regressed to bosses-only and paid at the one place a loaded page was contradicted). Two cautions now on record: (a) the first A9 WIN (run 237) read LESS than the 1-HP loss before it — the deck, not the habit, was the difference; do not let the victory teach "reading is optional." (b) Delivery is necessary but compliance binds at the death fight: runs 239 AND 241 both died deviating from a kill-order page they had LOADED (chosen.md; donu-and-deca.md). Persistent blind spots: boss-relic screens, final-boss entry (237's Awakened One; 242 never identified its Act 3 boss before dying 2.5 floors out), Writhing Mass (FIVE audited runs bare), own-deck card pages. **Strongest evidence yet that the fix must be tool-level (run 242):** all 10 of its feeds landed inside its directive's scope and 0/8 fights after the directive's criteria were met — including the fatal Transient, whose page names the exact losing shape played at T1. The manual habit held exactly as long as a directive enforced it, failing on a floor boundary INSIDE a single run. The post-success-discipline rule is now written into the Explore goal/heuristics; the delivery mechanism remains the maintainer's call.

## Directive 11: Corruption-without-FNP — seed replay

**Status:** CLOSED — CONFIRMED, scoped (run 242, audited: analyst/audits/run_242.md §3/§11; the authorized replication is spent). Final standing of "can Corruption-without-FNP work on Ironclad at A9": **YES at same-seed controlled-comparison level.** The engine with Barricade as accumulator cleared Act 1, Act 2, the Act 2 boss (Collector, net -4 vs expected 30-50), and the baseline's death fight (F31 Snake Plant, +11 net). Frail tax measured twice (~30%, runs 240/242) and answered by VOLUME — free-Skill block survives the tax that kills capped-block decks. Exhaust scope-edge observed directly: in a ~20-card deck the Skill pool empties ~3 engine turns in (max block 12 by T4 of uptime) — the 4-7-turn scoping is confirmed from the inside. Mirror-fight caveat triple-confirmed: Spheric-likes cost the Skill-heavy deck more even attack-led (-28 vs -16). NOT licensed: cross-seed generality (Directive 14's lane); raw "engine better than attack line" (the third arm carried curated rules + seed foreknowledge the baseline lacked — matched fights only). The closure package is worded into corruption.md, archetypes.md, spheric-guardian.md, snake-plant.md, sentinel.md, centurion-mystic.md (heal-arming rule: third datum, first prospective validation — followed as written, zero heals fired). Run 242's death (F48 Transient, 15 floors past the directive's scope) was a retrieval miss, not an engine failure — see D10's census update.

**History:** three arms on seed `3405875975300375922` (A9 Ironclad) — run 234 (attack baseline, died F31), run 240 (engine, died F25, interface-confounded; sub-question (a) confirmed scoped to ~4-7 turn fights, Sentinel strictly energy-positive), run 242 (replication: both criteria met — Act 2 boss reached and beaten, F31 Snake Plant survived with the Frail turn priced at 31%).

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

## Directive 15: Silent A9 — block scaling past Shiv saturation

**Status:** Open (opportunistic — activate on the next Silent run at A9, Win or Explore; no dedicated runs required).

**Hypothesis:** Deep Silent A9 runs fail on BLOCK scaling, not damage. The Shiv engine saturates at ~2x Accuracy (Shivs one-shot hallway enemies); past that point additional engine depth (3rd/4th Accuracy, more Blade Dances) is worth ~0, while the Act 3 boss check is block-per-turn against an escalating clock (Donu's +3 Str/cycle grew the beam requirement +6/cycle while the deepest Silent run's block ceiling stayed flat ~21-24). The deck named its own block gap for two acts and kept buying engine. Evidence: one run (the deepest Silent A9 on record, died at the Act 3 boss exactly on this gap) — needs prospective confirmation before any tier-list change.

**When activated:** (1) once Shivs one-shot hallway enemies, spend every discretionary slot (card rewards, shop slots, upgrades) on defensive scaling — Footwork + upgrades, After Image, second Footwork, repeatable Weak (Leg Sweep) — and tally the picks vs engine-depth alternatives in thinks; (2) target a block ceiling ≥ 30/turn before the Act 3 boss; record the realized max-block-per-turn at each boss; (3) if the Act 3 boss is Donu & Deca, follow the page's Donu-first order as written and record the Square-of-Protection/Dazed tax — the counterfactual datum the page's no-AOE section needs.

**Success criteria:** A Silent A9 run entering the Act 3 boss with a 30+ block ceiling. Confirm or refute: does the defensive-scaling disposition close the gap the saturated-engine disposition left open? If confirmed across 2 runs, promote the saturation rule in accuracy.md/silent.md from disposition note to drafting rule.

**Progress (runs 243-244):** Drafting discipline held both runs (Footwork+/Deflect+/Dex relics, every discretionary slot defensive). Run 244 REACHED saturation for the first time (Wrist Blade, Act 3 entry) with a realized block ceiling of 32 (Book T5) — but neither run reached the Act 3 boss, so the directive's actual hypothesis is still untested. Both failure modes so far were kill-speed floors on Act 2/3 elites and routing, NOT the block ceiling — note this when the directive is next touched; the block-ceiling hypothesis may be downstream of a more pressing routing/kill-speed problem.

## Directive 16: Commit-node blindness — price EVERY forced child, not just the forced elite

**Status:** Open (opportunistic — activate every Win/Explore run; it's a map-discipline drill, no dedicated runs). **WIDENED after the run 245 audit.**

**The pattern (runs 243 + 244, then 245):** the run's largest avoidable regret was the same shape three times — a node committed past a funnel whose forced child killed the run at capped/low HP. Run 243: rest→Gremlin Leader (rest-capped 40/70). Run 244: treasure→Nemesis, lesson recited verbatim at run start with the escape named in the player's OWN act plan, then deferred one floor at the click. **Recitation did not produce application.** Run 245 is the diagnostic case: the D16 check FIRED and CHANGED the route at the fatal fork (F13→F14, i2039) — the player enumerated children, saw the Unknown branch funneled into a forced ELITE at 37 HP, and consciously routed AROUND it into a Monster room. But the Monster room rolled the Transient (a block-check survival fight), which at 37 HP with a block-light hand was DEADLIER than the elite avoided. **The check fired, priced the named threat (the elite), and committed a fatal route anyway — because the habit's content was "avoid the forced elite," not "price every forced child."** This is a funnel-commit regret DESPITE the check firing.

**Verdict:** run 245 does NOT satisfy the old success criterion (two consecutive runs with no funnel-commit regret). It carries a funnel-commit regret via an un-priced MONSTER child. This is evidence promoting D10 shape 3 (node-choice tool/manifest surfacing) from problem-statement toward a maintainer task: the habit fired and enumerated correctly and still committed, because the priced threat was the elite, not the monster pool's worst case. The structural fix landed this cycle — the Act 3 Monster-pool kill-threats (Transient / Maw / Reptomancer) are now in `awareness/sts1/boundaries/node-choice.md` so the forced-monster worst case is in context at the fork.

**Hypothesis (widened):** pricing EVERY forced child whose worst case exceeds current HP — forced elite AND forced monster room — at ROUTING time is what prevents the funnel commit, IF the check fires AND its content covers the monster pool. The competing hypothesis (audit's preferred, now stronger): habit-level rules don't bind here and only the tool/manifest-level surfacing at the node-choice boundary will — i.e. this is D10 shape 3, third corpse.

**When activated:** (1) at EVERY map-choice node, before clicking, enumerate the children of each candidate node one floor down; **price every forced child whose worst case exceeds current HP — not just forced elites but forced MONSTER rooms** (Act 3 monster rooms include the Transient block-check, the Maw, and Reptomancer; a forced monster room can be deadlier than the elite you routed around). Treat the worst-case forced enemy as already-chosen and price it NOW by your turns-to-kill against THAT enemy's clock (Act 2/3 elites and Act 3 survival fights are kill-speed / block-check checks — Intangible/HP-scaler/block-check enemies invalidate any realized-average transfer); (2) when your plan names an escape branch, make the call at the fork where the branch exists, never one node later; (3) re-derive WIN% at every elite entry, every block-check fight entry, and after any >15-HP fight, citing the re-derived inputs (not a re-affirmed prior total). Log each map-choice with the children check shown — AND the worst-case forced-monster price, not only the elite — so the audit can measure whether the widened check fired.

**Success criteria:** Two consecutive audited runs with NO funnel-commit regret flagged of EITHER kind (forced elite or forced monster), the check having fired and priced the worst-case forced child at the fork. If a funnel still gets committed despite the widened check being in the habit, that is the evidence that promotes D10 shape 3 from problem-statement to a maintainer tool/manifest task.

---

## Retired / Completed (archive)

- **Directive 1 (Corruption+FNP without Strength) and Directive 2 (Corruption+FNP vs Spheric Guardian data):** Run-222-era, never attempted as written; the meta moved to A9 and the question is superseded by the seed-specific Directive 11 and the "under investigation" markers in drafting.md. Retired.
- **Directive 3 (Watcher archetype), 4 (Watcher execution), 5 (Guardian for Watcher), 6 (Watcher first win):** Complete. Outcome: stance dance engine viable but knowledge surface too large; Watcher paused at 0/14 in favor of Ironclad. Findings live in the Watcher-specific heuristics and the-guardian.md.
- **Directive 7 (Ironclad win streak):** Complete — win on run 219 (A5, Corruption+FNP+Brimstone).
- **Directive 8 (Watcher Slime Boss data):** Retired as dormant — Watcher play is paused; the observations live in slime-boss.md's Watcher section. Re-open if Watcher resumes.
- **Directive 9 (Ironclad A5 consolidation):** Overtaken by events — play moved to A9 after the run 227 A5 win. The A9 campaign's findings are consolidated in the run 227-233 audits. Retired.
