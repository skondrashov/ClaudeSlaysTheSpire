# Misc Audit — sts1 rules/types/characters/acts/shop + top-level + analysis + char/dev heuristics

COVERAGE: read 24 ontology + 6 heuristic files.

Ontology:
- top-level: game, combat
- rules/: block, buffs-and-debuffs, card-draw, damage, energy, retain
- types/: attack, skill, power, status, curse
- characters/: defect, ironclad, silent, watcher
- acts/: act-1, act-2, act-3
- shop/: shop
- analysis/ (methodology): index, attribution, prediction-errors, heuristic-updates, ontology-corrections, observations, strategic-patterns

Heuristics:
- characters/: defect, ironclad, silent, watcher
- combat (read for cross-reference; topic-level, not primary scope)
- development/interface/: sts1

Link-resolution note: site/build.py `resolve_wiki_link` slugifies the display name (`lower`, spaces→`-`, strip `'`/`.`) and ALWAYS emits `ontology-sts1-<category>-<slug>.html`. It never targets the heuristics layer and does not validate existence. "BROKEN-LINK" below = the slugified target ontology page does not exist (verified against site/out/ and ontology/sts1/<cat>/). No-category links like `[[combat]]`/`[[drafting]]` render as inert `<code>`, not links. `analysis/*` intra-links DO resolve (pages exist in site/out/).

## Defects — ONTOLOGY (facts)

[HIGH] ontology/sts1/characters/watcher.md — BROKEN-LINK + FACT-INCOMPLETE: `[[buffs/Wrath]]`, `[[buffs/Calm]]`, `[[buffs/Divinity]]` (and No Stance) — no `ontology/sts1/buffs/{wrath,calm,divinity}.md` exists. The four stances are the Watcher's core unique mechanic and have NO ontology entries anywhere; the stance table here is the only definition. FIX: create `buffs/wrath.md`, `buffs/calm.md`, `buffs/divinity.md` (or a `rules/stances.md`) and point the links there; same targets are also linked from rules/energy.md.

[HIGH] ontology/sts1/acts/act-1.md — BROKEN-LINK: `[[encounters/Jaw Worm]]`→`jaw-worm` (file is `jaw-worm-solo`), `[[encounters/Cultist]]`→`cultist` (lives in `enemies/cultist`, not encounters). Both target pages absent. FIX: relink to `[[encounters/Jaw Worm Solo]]` and the correct single-enemy encounter page (or `[[enemies/Cultist]]`).

[HIGH] ontology/sts1/acts/act-2.md — BROKEN-LINK (5): `[[encounters/Chosen]]`→`chosen` (file `chosen-solo`); `[[encounters/Chosen and Cultist]]`→`chosen-and-cultist` (file `chosen-cultist`); `[[encounters/Centurion and Mystic]]`→`centurion-and-mystic` (file `centurion-mystic`); `[[encounters/Spheric Guardian]]`→`spheric-guardian` (only `enemies/spheric-guardian`, no encounter page); `[[encounters/Shelled Parasite]]`→`shelled-parasite` (files `shelled-parasite-solo`/`-fungi-beast`). All target pages absent. FIX: relink to actual encounter slugs / disambiguate the multi-variant encounters.

[HIGH] ontology/sts1/acts/act-3.md — BROKEN-LINK (3): `[[encounters/Double Orb Walkers]]`→`orb-walkers` (files `orb-walker`/`2-orb-walkers`); `[[encounters/Spiker and Exploder]]`→`spiker-and-exploder` (no encounter page; only `enemies/spiker`,`enemies/exploder`); `[[encounters/The Maw]]`→`the-maw` (file `maw`). All target pages absent. FIX: relink to actual encounter slugs (e.g. `[[encounters/2 Orb Walkers]]`, `[[encounters/Maw]]`); create/point the Spiker+Exploder encounter.

[MED] ontology/sts1/types/curse.md — CONTRADICTION (vs shop.md): "Removable at shops for 75 gold (except Parasite)" asserts a flat cost; shop.md correctly states removal is 75 then +25 per use (shared escalating counter). FIX: change to "Removable at shops (cost escalates; see [[shop/Shop]])" and drop the fixed "75 gold".

[MED][VERIFY] ontology/sts1/rules/buffs-and-debuffs.md — FACT-ERROR?: "Most debuffs have stacks that decrement at the start of the affected entity's turn." For Weak/Vulnerable/Frail the duration ticks down at the END of the afflicted entity's turn, not the start (Poison ticks at start, after dealing its damage). Stating "start" for "most" is likely wrong. FIX: verify engine timing; if confirmed, "duration debuffs (Weak/Vulnerable/Frail) decrement at the END of the afflicted entity's turn."

[MED] ontology/sts1/combat.md — BROKEN-LINK + HEDGE: "See [[rules/exhaust]] if it exists." — `rules/exhaust.md` does not exist; the link is dead and the "if it exists" hedge is self-admitted uncertainty in an atomic-fact layer. Exhaust is otherwise only defined inline here. FIX: create `rules/exhaust.md` and link it, or remove the link and the hedge.

[MED] ontology/sts1/combat.md — MOVE-TO-HEURISTICS: "Intent damage numbers are FINAL — use them directly for block calculations. Do not re-apply modifiers." (also duplicated in rules/damage.md). The imperative "use them directly … Do not re-apply" is player instruction, not an atomic fact. The fact is "intent numbers already include all modifiers." FIX: keep the factual half; move the do/don't instruction to heuristics/combat.md (where the block algorithm already lives).

[MED] ontology/sts1/combat.md — REDUNDANT/MOVE-TO-HEURISTICS: "## Strength" section (sources of per-combat vs persistent Strength, enemy Strength) restates types/attack + rules/damage and lists card sources that belong in card entries; "Strength resets between combats" framing is strategy already stated in heuristics/characters. FIX: trim to a pointer to a buffs/strength entry; drop the curated source lists from the combat fact file.

[LOW] ontology/sts1/combat.md — CONTAMINATION: Fossilized Helix/Buffer multi-hit interaction ("block is depleted by hit 1 … then subsequent hits land with no block") is a derived/composed consequence, not an atomic fact. Borderline; acceptable as a stated interaction but leans into heuristics. FIX: consider moving the worked multi-hit consequence to a heuristic; keep "block is consumed before the prevention check" as the fact.

[LOW] ontology/sts1/game.md — FORMAT: `[[combat]]` and (via heuristics list) bare topic names render as inert `<code>`, not links, because the resolver requires a category. Also the "buffs/Strength", "debuffs/Vulnerable" links in the bullet list resolve fine (those dirs exist). FIX: write `[[combat]]` with no expectation of a link, or add a category, for the topic cross-refs.

[LOW] ontology/sts1/rules/energy.md — REDUNDANT: the "## Stances ([[characters/Watcher]])" mini-section (Calm exit +2E, Divinity entry +3E) duplicates the stance table in characters/watcher.md and depends on the missing buffs/Calm,Divinity entries (same broken links as HIGH above). FIX: keep one canonical stance definition; reference it.

[LOW] ontology/sts1/shop/shop.md — FACT-INCOMPLETE: "### Cards (5 offered) … 1 Colorless card" — does not note that a shop card may appear on-sale (one random card 50% off), which the same file mentions one line later ("Cards on sale: 50% off") without saying it is shop-wide one-slot. Minor wording. FIX: clarify exactly one shop card is discounted.

## Defects — ANALYSIS (methodology: coherence/links/staleness)

[HIGH] ontology/sts1/analysis/index.md — STALENESS: paths `analyst/runs/run_NNN.json`, `ontology/`, `heuristics/`, `analyst/observations.md` are all repo-root-relative, but after the restructure the runtime tree lives at `games/sts1/` (verified: `games/sts1/analyst/runs/run_001.json`, `games/sts1/analyst/observations.md` exist; no root-level `analyst/`). "Read the run JSON first." points at a nonexistent root path. FIX: prefix runtime paths with `games/sts1/` (knowledge paths `ontology/`,`heuristics/` are repo-root and OK).

[MED] ontology/sts1/analysis/observations.md — STALENESS: "Working notes live in `analyst/observations.md`." — actual file is `games/sts1/analyst/observations.md`. FIX: correct the path.

[LOW] ontology/sts1/analysis/heuristic-updates.md — STALENESS (minor): describes writing to `heuristics/` (correct, repo-root) but the doc's sibling index.md mis-states the run-input path; ensure consistency once index.md is fixed. No change needed here beyond cross-check.

[LOW] ontology/sts1/analysis/ontology-corrections.md — FORMAT (false-positive guard): the literal `[[category/Name]]` placeholder renders as a dead `ontology-sts1-category-name.html` link. It is illustrative, not a real link. FIX (optional): wrap in backticks/code so it is not slugified into a broken anchor.

## Defects — HEURISTICS

[HIGH] heuristics/sts1/characters/watcher.md — TOPIC-MISPLACED (harness/interface advice in a strategy file): "## Execution Risks" item 1 "Accidental Wrath entry via turn() index shifting. Batched turn() commands with index-based card references … Always use card names in turn() batches (see combat.md rule 6)." This is agent-harness API guidance (turn()/send()/index semantics), not StS strategy; it duplicates heuristics/combat.md rule 6 and belongs in development/interface/sts1.md. FIX: move the turn()-batching rule to the interface doc; keep the StS-level point ("don't enter Wrath without a confirmed exit"). Same pattern: item 2 "Blasphemy self-kill … confirmed with exact arithmetic" and item 4 reference the harness math workflow.

[MED] heuristics/sts1/characters/watcher.md — DUPLICATES (cross-file): "## Wrath Damage Arithmetic" (double every hit; Tantrum+ 10→20; Run 193) and "## NEVER Use Distilled Chaos as Watcher" (Run 193 Meditate+ fatal) restate heuristics/combat.md rules 7 & 9 nearly verbatim. Acceptable as character emphasis but the Run-193 worked example is triplicated (here, combat.md §7, combat.md §9). FIX: keep the Watcher-specific stance framing; reference combat.md for the generic arithmetic/Distilled-Chaos rules instead of re-deriving.

[MED] heuristics/sts1/characters/watcher.md — STUB-VACUOUS pointer: "See 'HP Management' below for relic interactions and boss math." and "See Slime Boss matchup notes." / "See 'HP Management' below" — fine internally, but "## HP Sensitivity" and "## HP Management" both open with the identical sentence "The Watcher is more HP-sensitive than other characters because Wrath doubles incoming damage." (verbatim duplication within one file). FIX: merge the two HP sections; state the premise once.

[LOW] heuristics/sts1/characters/ironclad.md — NO-EVIDENCE/HEDGE (acknowledged): "6 wins across 130 runs … (all also had Str sources -- the engine's independence is under investigation)" and "Whether the engine can function independently without Strength is under investigation." This is honest uncertainty, but per heuristic-updates.md rule 2 ("No confidence tags … uncertain goes in observations") the under-investigation caveat should live in analyst/observations, not the heuristic. FIX: move the "independence under investigation" note to games/sts1/analyst/observations.md; keep the actionable engine descriptions.

[LOW] heuristics/sts1/characters/ironclad.md — STALENESS (run-count drift, cross-file): "6 wins across 130 runs … Ascension 5" vs watcher.md "0 wins in 14 runs (128-132, 188-196)". Run-number ranges are baked into prose (rule 1 of heuristic-updates.md says "No run numbers. State conclusions, not history."). Several character files violate the no-run-numbers rule. FIX: strip explicit run IDs from heuristics; keep them in analyst logs.

[LOW] heuristics/sts1/characters/silent.md / defect.md — DUPLICATES-ONTOLOGY (mild): silent.md "[[cards/Neutralize]] is free [[debuffs/Weak]]. 0E Attack" and defect.md Frost-orb block numbers restate ontology stat lines, but each adds a "therefore play it / therefore replaces Defend" judgment, so they stay actionable. No fix required; noted for the cross-cutting pattern.

[LOW] heuristics/sts1/development/interface/sts1.md — STUB-VACUOUS sections: "## Known Issues — (None documented yet …)" and "## State Representation Decisions — (Document decisions … here)" are empty placeholders. Meanwhile real interface issues (turn() index shifting, double-end bug) are documented in heuristics/combat.md and interface/sts1/tools.md instead of here. FIX: migrate the harness/execution rules currently scattered in combat.md and the watcher heuristic into these empty sections (this is the correct home for them).

## CLEAN

ontology/sts1/characters/{ironclad,silent,defect}.md (facts); ontology/sts1/types/{attack,skill,power,status}.md; ontology/sts1/rules/{block,card-draw,damage,retain}.md; ontology/sts1/analysis/{attribution,prediction-errors,strategic-patterns}.md; heuristics/sts1/characters/{ironclad,silent,defect}.md (links all resolve; content actionable).

## PATTERNS

- **NEW — acts/ encounter links are systematically broken by display-name vs filename slug drift.** 10 `[[encounters/<Display Name>]]` links across act-1/2/3 slugify to pages that don't exist because the real files use suffixed/abbreviated stems (`*-solo`, `*-horde`, `centurion-mystic`, `orb-walker`, `maw`) or live in `enemies/` (Cultist, Spheric Guardian, Spiker, Exploder). This is the largest single broken-link cluster found and is mechanical/repeatable — likely an automated relink fixes all 10.
- **NEW — Watcher stances have no ontology entry at all.** `Wrath/Calm/Divinity` are referenced as `[[buffs/...]]` from rules/energy.md and characters/watcher.md but no file backs them; the only definition is an inline table. Both a broken-link and a genuine FACT-INCOMPLETE gap for a core mechanic.
- Known pattern (restructure staleness): analysis/index.md + observations.md hardcode root-relative `analyst/…` paths; runtime now lives under `games/sts1/`. interface/sts1/tools.md (out of scope) additionally hardcodes an even older `C:\…\autoplay\games\sts1` path — flag for the interface owner.
- Known pattern (agent-harness advice in heuristics): watcher.md "Execution Risks" + the whole of heuristics/combat.md (rules 5/6/7) encode `turn()/send()/play N` harness mechanics as if they were game strategy. The intended home — development/interface/sts1.md — sits empty. Migration target identified.
- Known pattern (derivation/instruction in ontology): combat.md carries "use intent numbers directly / do not re-apply", a Strength source roster, and the Helix/Buffer multi-hit walkthrough — composed consequences and player instructions rather than atomic facts.
- Known pattern (no-run-numbers rule violated in heuristics): per analysis/heuristic-updates.md rule 1, but ironclad.md and watcher.md embed explicit run IDs and win/loss tallies in prose.
- Resolver caveat (not a per-file defect): `resolve_wiki_link` only ever links to the ontology layer and never validates targets, so heuristic→heuristic intent silently links to ontology pages, and any typo'd category/name renders a dead anchor with no build error.
