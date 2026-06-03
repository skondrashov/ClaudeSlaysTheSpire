# Audit: enemies n–z + all bosses

COVERAGE: read 35 ontology + 27 heuristic files.

Ontology enemies (n–z, 23): nemesis, orb-walker, pointy, red-louse, red-slaver, repulsor, reptomancer, sentry, shelled-parasite, shield-gremlin, snake-plant, sneaky-gremlin, snecko, spheric-guardian, spike-slime-l, spike-slime-m, spike-slime-s, spiker, spire-growth, taskmaster, the-maw, transient, writhing-mass.
Ontology bosses (12): spire-shield, spire-spear, corrupt-heart, the-champ, the-collector, the-guardian, hexaghost, bronze-automaton, slime-boss, donu-and-deca, time-eater, awakened-one.
Heuristic enemies (n–z + grouped, 18): nemesis, orb-walker, red-slaver, reptomancer, repulsor, sentry, shelled-parasite, snake-plant, snecko, spheric-guardian, spike-slime-l, spike-slime-m, spiker, the-maw, transient, writhing-mass, slavers, small-slimes.
Heuristic bosses (9): donu-and-deca, hexaghost, the-collector, time-eater, the-champ, awakened-one, the-guardian, bronze-automaton, slime-boss.
(Companion gaps: heuristics have no nemesis/pointy/red-louse/sneaky-gremlin/shield-gremlin/spike-slime-s/spire-growth/taskmaster exact-stem for some ont, and ont has no corrupt-heart/spire-shield/spire-spear heuristic — see PATTERNS.)

## Defects

### Broken links
- [HIGH] ontology/sts1/bosses/corrupt-heart.md — BROKEN-LINK: `[[buffs/Painful Stabs]]` (line 18), file is `debuffs/painful-stabs.md`. CONFIRMED (known issue). FIX: `[[debuffs/Painful Stabs]]`.
- [HIGH] ontology/sts1/bosses/corrupt-heart.md — BROKEN-LINK: `[[buffs/Beat of Death]]` (lines 18, 22) — no `beat-of-death.md` exists in buffs/ or debuffs/. FIX: create `ontology/sts1/buffs/beat-of-death.md` (out of scope here) or point at existing target.
- [HIGH] ontology/sts1/bosses/corrupt-heart.md — BROKEN-LINK: `[[buffs/Invincible]]` (line 23) — no `invincible.md` exists. FIX: create buffs/invincible.md.
- [HIGH] ontology/sts1/bosses/awakened-one.md — BROKEN-LINK: `[[buffs/Regenerate]]` (line 33) — file is `buffs/regeneration.md` titled "Regeneration"; `regen-potion.md` correctly uses `[[buffs/Regeneration]]`. FIX: `[[buffs/Regeneration]]` (or rename mechanic to Regeneration).
- [HIGH] ontology/sts1/bosses/awakened-one.md — BROKEN-LINK: `[[buffs/Curiosity]]` (lines 29, 31) — no `curiosity.md` exists. FIX: create buffs/curiosity.md.
- [HIGH] ontology/sts1/enemies/transient.md — BROKEN-LINK: `[[buffs/Fading]]` (lines 6, 21 x2) and `[[buffs/Shifting]]` (line 23) — neither file exists. FIX: create buffs/fading.md + buffs/shifting.md.
- [HIGH] ontology/sts1/enemies/writhing-mass.md — BROKEN-LINK: `[[buffs/Reactive]]` (line 25) — no `reactive.md` exists. (`Malleable` resolves fine.) FIX: create buffs/reactive.md.
- [MED] heuristics/sts1/enemies/transient.md — BROKEN-LINK: `[[buffs/Fading]]`/`[[buffs/Shifting]]` (line 3) mirror the ont missing-target; also `[[encounters/Transient]]` (line 29) — wrong category, the file is `enemies/transient.md`. FIX: fix Fading/Shifting once targets exist; change `[[encounters/Transient]]`→`[[enemies/Transient]]`.

### Ontology — factual / completeness
- [HIGH][VERIFY?] ontology/sts1/bosses/corrupt-heart.md — FACT-ERROR: "`[[buffs/Invincible]] 200 (300 at A0)`" is internally contradictory (A0 IS the base) and inverted. Real: Invincible = 300 at A0, 200 at A19+ (lower cap on higher asc). FIX: "Has Invincible 300 (200 at A19)."
- [HIGH][VERIFY?] ontology/sts1/bosses/corrupt-heart.md — FACT-ERROR: Blood Shots `2x15 (A0)` has hits/damage swapped — real is 12 hits × 2 dmg at A0 (15×2 at A4/higher). FIX: "Blood Shots | 2x12 = 24 (2x15 = 30 at A4) | Multi-hit". [VERIFY] exact asc breakpoint.
- [MED] ontology/sts1/bosses/corrupt-heart.md — FACT-INCOMPLETE: "Echo 40" lacks ascension scaling ([VERIFY] Echo is 40→45/45→? at higher asc) and no A-variant noted for Debilitate stacks. Also Blood Shots row shows only "(A0)" with no higher value. FIX: add asc variants.
- [MED] ontology/sts1/bosses/the-collector.md — MOVE-TO-HEURISTICS: Pattern/Attacks embed "(attack for 7 damage each)" Torch Head behavior inline twice + Mechanics block repeats it — Torch Head is a separate summoned entity; atomic facts OK but the triple repetition of "38-40 HP, 7 dmg" is REDUNDANT. FIX: state Torch Head stats once (own subsection).
- [MED] ontology/sts1/enemies/the-maw.md — FACT-INCOMPLETE/HEDGE: "Nom Nom | 5xN (N increases -- roughly current turn / 2 rounded up)" hedges the algorithm ("roughly"). Real: Nom Nom hit count scales deterministically. FIX: state exact formula or flag [VERIFY]; remove "roughly".
- [MED] ontology/sts1/enemies/the-maw.md — FACT-INCOMPLETE: Turn-2+ pattern omits which move opens Turn 2 (Drool is the implicit first post-Roar move but the "After Drool…" cycle never states the entry point). FIX: state "Turn 2: Drool" explicitly.
- [LOW] ontology/sts1/enemies/spheric-guardian.md — FORMAT: Block/Barricade/Activate use bare "Block" not `[[rules/Block]]` (inconsistent with bronze-automaton.md which links it). Also Activate=25 vs base 40 Block + Barricade interplay not cross-referenced. FIX: link rules/Block; minor.
- [LOW] ontology/sts1/enemies/spheric-guardian.md (spheric) — FACT-INCOMPLETE: no Ascension variants given at all (HP fixed 20 is correct; but Slam/Frail values have no A-line). Likely correct as-is for this enemy. FIX: confirm no A-variant exists, else add.
- [LOW] ontology/sts1/enemies/transient.md — FACT-INCOMPLETE: damage table stops at Turn 5 but Fading 5 means it acts on turns 1–5 then fades — OK; however "attacks BEFORE fading" + Shifting belong together; Shifting's effect (damage-reduces-incoming) is only in the heuristic, not ont. FIX: add atomic Shifting line to ont (or rely on buffs/shifting.md once created).
- [LOW] ontology/sts1/enemies/snecko.md — FACT-INCOMPLETE: Tail Whip "(+ 2 Weak at A17)" — [VERIFY] Snecko's A17 Tail Whip adds Weak; plausible but confirm threshold.
- [LOW] ontology/sts1/enemies/red-slaver.md — FACT-INCOMPLETE: no HP ascension line (46-50 fixed is correct), and Entangle has no asc note — fine; Scrape Vuln "2 at A17" present. CLEAN-ish.
- [LOW] ontology/sts1/enemies/spiker.md — FACT-INCOMPLETE: "Cannot use Spike after it has been used 6 times" — [VERIFY] cap is 6 (Spike has a usage limit); Thorns start 3 OK.
- [LOW] ontology/sts1/enemies/reptomancer.md — FACT-INCOMPLETE: Dagger HP "20-25 each" consistent with dagger.md; but Reptomancer HP "180-190" has no A-line ([VERIFY] elite HP unchanged by asc — true for most A0/A7 elites get +? ). FIX: confirm.
- [LOW] ontology/sts1/bosses/donu-and-deca.md — FACT-INCOMPLETE: no Ascension HP/damage variants (Beam 10x2, Str 3) — [VERIFY] A19 raises Str gain or Beam? Likely fixed. FIX: confirm.
- [LOW] ontology/sts1/bosses/spire-shield.md / spire-spear.md — FACT-INCOMPLETE: HP ranges given but zero ascension variants and pattern described loosely ("Can also use Smash"/"Can also Skewer") without the trigger condition or %s — drifts from atomic algorithm. FIX: specify when Smash/Skewer fire (these are Act 4 act-pressure escalation moves).
- [LOW] ontology/sts1/bosses/the-guardian.md — FACT-INCOMPLETE: Mode Shift "Threshold 30 (first cycle), 40, 50, +10 each" — correct; but Whirlwind shown 5x4=20 with no asc; Fierce Bash 32 no asc (Guardian damage is fixed across asc — OK). Acceptable.
- [LOW] ontology/sts1/bosses/awakened-one.md — REDUNDANT: Phase-2 buff/persistence prose (lines 31, 33) duplicates the same After Image/Inflame/Footwork persistence list that lives in the heuristic; the ont prose ("Phase 1 Power plays are doubly valuable") edges toward derived consequence. FIX: keep atomic (Rebirth removes Power cards, stat buffs persist, Curiosity/Str reset); drop value judgment.

### Heuristics — content
- [MED] heuristics/sts1/enemies/transient.md — DUPLICATES-ONTOLOGY borderline + the Fading/Shifting explanation is genuinely a derivation (actionable) so NOT vacuous; but it restates the 30/40/50/60/70 table verbatim from ont. Keep (adds "attack-first" sequencing). No fix.
- [MED] heuristics/sts1/enemies/small-slimes.md — STUB-VACUOUS risk: "Trivial encounter… very low HP and damage" adds little beyond ont, BUT "Kill the Acid Slime first to avoid Weak stacking" is a real actionable order. Borderline-acceptable. No fix.
- [MED] heuristics/sts1/enemies/spike-slime-m.md — STUB-VACUOUS borderline: "Mostly uses Lick (70%)… blocking needs moderate" restates ont 70% + Frail; the "kill in 3-4 turns" benchmark is the only added value. Thin but acceptable.
- [MED] heuristics/sts1/bosses/bronze-automaton.md — TOPIC-MISPLACED/agent-harness leak: "do NOT batch… use card names, not indices (see combat.md rule 6/8)" and "Distilled Chaos randomly playing Meditate+" reference the agent harness/automation, not StS strategy. NEW instance of agent-harness-advice-in-heuristics. FIX: move harness mechanics to combat.md.
- [MED] heuristics/sts1/bosses/the-guardian.md — agent-harness leak: "do NOT batch the whole sequence in turn() — use card names, not indices (see combat.md rule 6)" (line 41). FIX: relocate.
- [MED] heuristics/sts1/bosses/time-eater.md — agent-harness leak: "State count before and after each play" framing + Fiend Fire note is fine, but "Lose track of the 12-card count" as a death cause is harness-operator advice. Minor. FIX: trim.
- [LOW] heuristics/sts1/enemies/repulsor.md — CONTRADICTION (cross-entry ordering): "Kill after Exploders but before Spikers" presumes a specific grouped encounter; spiker.md heuristic says "kill Spiker first to stop Thorns." These can both be right in different encounters but read as conflicting kill-order absolutes. FIX: scope each to its encounter.
- [LOW] heuristics/sts1/enemies/sentry.md — UNCONDITIONAL: "The AOE benchmark is the only acceptable outcome." Absolute; evidence is one 20-turn run. Reasonable but strong. Keep with caveat.
- [LOW] heuristics/sts1/enemies/snecko.md — NOT-ACTIONABLE edge: "With good RNG… better; with bad RNG… wasted" is descriptive; rest (Powers/Metallicize/Duplication) is actionable. OK.
- [LOW] heuristics/sts1/enemies/spike-slime-l.md — DUPLICATES-ONTOLOGY: split/AOE advice fine; thin but actionable. OK.
- [LOW] heuristics/sts1/bosses/awakened-one.md — NO-EVIDENCE edge: "Duplication + HB+ = 312 one-shot" cites Run 184 (good); the "(14 + 18*5)*1.5 = 156" math is a derivation (correct: 104*1.5=156). Fine — keep.
- [LOW] heuristics/sts1/enemies/reptomancer.md — DUPLICATES-ONTOLOGY: "Each Dagger that explodes deals 25 damage" restates dagger.md atomic fact, but frames kill-timing (actionable). OK.

## CLEAN
ontology: pointy, red-louse, sneaky-gremlin, shield-gremlin, spike-slime-s, spire-growth, taskmaster, orb-walker, repulsor, sentry, shelled-parasite, snake-plant, spike-slime-l, spike-slime-m, nemesis, the-champ, the-collector(minus redundancy), hexaghost, bronze-automaton, slime-boss, time-eater.
heuristics: red-slaver, reptomancer, repulsor, sentry, shelled-parasite, snake-plant, snecko, spheric-guardian, the-maw, writhing-mass, spiker, slavers, nemesis, orb-walker, donu-and-deca, hexaghost, the-collector, the-champ, slime-boss.

## PATTERNS
- RECURRING (known) — category-mismatch / missing-target broken links: corrupt-heart (`buffs/Painful Stabs`, `buffs/Beat of Death`, `buffs/Invincible`), awakened-one (`buffs/Regenerate`→regeneration, `buffs/Curiosity`), transient (`buffs/Fading`,`buffs/Shifting`; heuristic `encounters/Transient`), writhing-mass (`buffs/Reactive`). build.py builds URLs from `category/Name` text and never validates → silent 404 (documented in audit/2026-05-31-content-audit.md). The novel sub-pattern: an entire family of enemy/boss SPECIAL buffs (Fading, Shifting, Reactive, Invincible, Curiosity, Beat of Death) has NO ontology file at all — these are referenced only from the enemy/boss files that need them.
- RECURRING (known) — agent-harness advice leaking into heuristics: NEW instances in bosses/bronze-automaton.md, bosses/the-guardian.md, bosses/time-eater.md ("use card names not indices / turn() batching / Distilled Chaos auto-play / track the count"). These describe the automation harness, not StS.
- RECURRING (known) — grouped-encounter heuristics breaking exact-stem companions: slavers.md (covers red/blue-slaver+taskmaster), small-slimes.md, plus no exact-stem heuristic for several n–z ont enemies (pointy, red-louse, sneaky-gremlin, shield-gremlin, spike-slime-s, spire-growth, taskmaster); conversely no ont→heuristic pair for corrupt-heart/spire-shield/spire-spear (bosses have 12 ont but 9 heur).
- RECURRING (known) — missing ascension variants in ontology: spire-shield, spire-spear, donu-and-deca, reptomancer (Reptomancer HP), corrupt-heart (Echo/Blood Shots higher-asc), several enemies lack A-lines where StS has them. Flagged [VERIFY] individually.
- NEW SYSTEMIC — errors-mirrored-in-ontology+heuristic for corrupt-heart: the Blood Shots `2x15` and Invincible inversion live only in ont (no heuristic companion exists), so the mirror is absent here; but the missing-buff-file family is mirrored (transient ont + transient heuristic both dead-link Fading/Shifting).
- NEW SYSTEMIC — cross-entry kill-order contradiction: repulsor.md ("before Spikers") vs spiker.md ("kill Spiker first") give conflicting unconditional orderings because neither scopes to its actual encounter.
</content>
</invoke>
