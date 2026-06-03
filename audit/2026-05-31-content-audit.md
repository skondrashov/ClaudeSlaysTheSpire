# Praxis Book — Content Audit (2026-05-31)

**Status:** COMPLETE. Exhaustive on buffs, debuffs, enemies, bosses, events, potions, encounters, heuristic topic files, and the entire `praxis`/`book-sts1`/`goals` meta layer. **Cards and relics were sampled (~45% / ~44%)** with a structural recommendation in lieu of exhaustive cataloguing (maintainer decision — the entries should be regenerated from canonical data, so per-file fixes would be thrown away).

**Method:** read-only deep read of each entry against its companion. No web — factual suspects flagged `[VERIFY]` for a later wiki/data pass. Rubric: **ontology = atomic facts only**; composed/derived consequences belong in **heuristics** (no new category or term); heuristic value judged by content, not length.

**Output policy:** this audit FLAGS and recommends; it makes **no edits** to knowledge entries.

**Raw per-chunk findings:** `audit/findings/*.md` (cards-sample-dl, cards-sample-mz, relics-sample, enemies-nz-bosses, events, potions, encounters, misc). Wave-1 detail is inline below.

---

## TL;DR

~200 defects were found, but they trace to a **handful of root causes**. Fixing those structurally is far higher-leverage than correcting entries one by one:

1. **Paraphrase drift** in game-object ontology (cards / relics / potions / events) — the book re-words canonical game text and drifts. ~97% of these entries are *pure paraphrase* → **regenerate from game data** and the whole error class disappears.
2. **`buffs/` is populated by effect, not by actual powers** — it has spurious entries (e.g. `pen-nib`, a relic) and is missing real powers (the Watcher stances; six enemy powers), so references dangle.
3. **The repo restructure** left stale paths/counts everywhere and an **unvalidated wiki-link resolver** in `build.py`, so broken links 404 silently.
4. **A framework-doc gap:** "ontology = atomic only; derived consequences are heuristics" is never stated — and is actively contradicted where composition is discussed.

The ontology/heuristics **split discipline itself is healthy** — strategy is almost always correctly confined to heuristics companions. The problems are fidelity, category hygiene, and restructure fallout, not contamination.

---

## Root-Cause & Structural Recommendations (do these first)

### R1 — Generate game-object ontology (cards/relics/potions/events) from canonical data
**Evidence:** across ~157 sampled cards: effect drift ~9–13%, **97% pure paraphrase**, only 1 entry carried an atomic fact not printed on the card. Across ~77 sampled relics: effect drift ~8%, **rarity wrong ~18%**, 3 phantom relics, ~95% pure paraphrase. Confirmed drift examples: crush-joints (Weak→Vulnerable), compile-driver (per-orb vs per-type), predator (20→22), wallop (12→13), rip-and-tear (fabricated ×2), parasite, necronomicurse, the-nest, augmenter/J.A.X., blessing-of-the-forge, distilled-chaos.
**Recommendation:** a game-object ontology entry should be **{structured metadata: cost, rarity, type, character/color, target} + {verbatim effect text, base + upgraded} + {`[[links]]` to referenced mechanics}** — never a reworded behavior description. Source these from the StS card/relic/potion/event data (mod export or community dataset) rather than hand-writing. This auto-fixes the ~1-in-10 effect errors and ~1-in-5 relic-rarity errors, surfaces phantom entries (no source row), and stops recurrence. Derived consequences / synergies / strategy stay in the heuristics companions (already the case).
**Caveat:** preserve the <5% of entries flagged `HAS-EXTRA-FACTS` (e.g. genetic-algorithm's "Block is permanent"); diff before overwriting.

### R2 — Rebuild `buffs/` around actual in-game powers
**Rule:** a buff/debuff entry exists **iff** it is a real applied in-game power/status — not for every effect a relic or card produces.
- **Delete/merge spurious:** `buffs/pen-nib.md` duplicates the `relics/pen-nib.md` effect (and carries the "persists across combats" error). `[VERIFY]` whether a real "Pen Nib" power exists; if not, delete and fold into the relic. Audit the rest of `buffs/` for the same pattern.
- **Create missing (all currently dangling references):** Watcher stances **Wrath / Calm / Divinity** (core mechanic, no entry at all — linked from `energy.md`, `watcher.md`), and enemy powers **Fading, Shifting, Reactive, Invincible, Curiosity, Beat of Death**.

### R3 — Add wiki-link validation to `site/build.py`
`resolve_wiki_link` builds the URL straight from the `category/Name` text and never checks the target exists, so every miscategorized or typo'd link 404s with no build error. **Make the build warn (or fail) on unresolved links.** This single change would have caught the entire broken-link class below: `[[buffs/Slow]]`/`[[buffs/Painful Stabs]]` (files under `debuffs/`), `[[enemies/Louse]]` (no generic node), the 10-link acts/ cluster, the six missing buffs, `[[topic-files]]`, `[[goals]]`, `[[interface]]`.

### R4 — Sweep restructure staleness
Knowledge layers were hoisted to repo root but runtime artifacts stayed under `games/sts1/`. Fix root-relative paths (`analyst/`, `data/`, scripts) in `goals/sts1/*` (6 files), `ontology/book-sts1/{evidence,pipeline,site}.md`, and `ontology/sts1/analysis/index.md` — either prefix `games/sts1/` or declare cwd. Correct heuristics counts ("349" → **343**, 8 categories not 9; phantom `goals` category, missing `development`). Fix `last_goal`→`last_agent` in pipeline.md.

### R5 — State the ontology=atomic rule in the framework docs
Currently silent-to-contradictory. Priority insert in **`heuristics/praxis/splits.md`** ("Derived Consequences Are Heuristics"); reconcile `ontology/praxis/layers.md:10-11`, `ontology/praxis/index.md:9`, `ontology/book-sts1/index.md:29`, `ontology/book-sts1/ontology.md:49` (the "Bash → 1.5× without a separate entry" example reads as ontology — reword so the derivation is a *heuristic* composing two ontology facts).

### R6 — Relocate derived `Interactions:` lines to heuristics
Mostly in buffs/debuffs (and `relics/fossilized-helix.md`): worked examples and "since X is a Y…" deductions sitting in ontology. Move to heuristics companions (create them where absent — buffs/debuffs have none). Keep only the atomic fact in ontology.

### R7 — Topic-file & heuristic hygiene
- Reconcile the **boss-rest HP threshold**: `rest-sites.md` says 60%, `hp-management.md`/`map.md`/`drafting.md` say 70%. Pick one; reference a single threshold table.
- De-duplicate cross-file guidance (potion-timing, "two healing sources by A2F5", "post-brutal-fight → non-combat").
- **Move agent-harness advice out of game heuristics** into `development/interface/sts1.md`: "don't batch `end` in the same turn()" (battle-trance, bloodletting), turn()-index warnings (watcher, several enemies), index-shifting notes. This is API/tool advice, not StS strategy.

---

## Drift Quantification (sample)

| Category | Sampled | Effect drift | Metadata drift | Pure-paraphrase | Phantom |
|----------|---------|-------------|----------------|-----------------|---------|
| Cards a–c (exhaustive) | 84 | ~6 (~7%) | Character missing ×2+ | — | 0 |
| Cards d–l | 35 | 3 (~9%) | 1 | 34/35 | 0 |
| Cards m–z | 38 | 5 (~13%) | 0 | 38/38 | 0 (1 existence?) |
| Relics a–c (exhaustive) | 37 | ~2 | — | high | 2 (brass-ring, cables) |
| Relics d–z | 40 | 2 (~5%) | **7 rarity (~18%)** | 38/40 | 1 (strike-dummy) |

**Takeaway:** ~9% card effect drift, ~18% relic rarity drift, ≥3 phantom relics — and ~97% of all entries are regenerable verbatim. R1 is well-justified.

---

## Findings by Area

### Framework / meta (exhaustive)
- DESIGN gap → R5. Staleness (counts, paths) → R4. Broken meta links: `heuristics/book-sts1/index.md:8` `[[topic-files]]`; `ontology/book-sts1/index.md:11,14` `[[goals]]`/`[[interface]]`; `goals/book-sts1/{extend,curate}.md` point at `heuristics/book-sts1/{entry-quality,splits,overfitting,attribution}.md` (live in `praxis/`).
- `[MED]` `goals/sts1/*` use `[[goals/next]]` (should be `[[next]]`) + dead `[[exploration/]]`/`[[audit/]]`/`[[curation/]]`; goals-layer link convention is undefined in `linking.md`.
- `[MED]` "four phases required" (pipeline.md, agents.md) drops the 5th goal (Develop). `[LOW]` evidence ladder triplicated.

### Cards (sampled) — see R1; raw: cards-sample-dl/mz.md, wave-1 a–c inline
- `[HIGH]` crush-joints (Weak not Vulnerable; upgrade drops condition), predator (20→22), wallop (12→13), grand-finale (Character Colorless not Silent).
- `[HIGH/MED][VERIFY]` berserk, choke+, coolheaded+, compile-driver, rip-and-tear, parasite, necronomicurse, darkness, dark-shackles, loop, rampage, pain. (`sands-of-time` existence `[VERIFY]`.)
- `[MED]` missing `Character` on colorless/event cards (apparition, beta). Cost double-encoding + inconsistent "Upgraded:" convention — symptoms of hand-authoring, resolved by R1.
- `[MED]` agent-harness advice in `heuristics/cards/{battle-trance,bloodletting}.md`, meta-commentary in `barrage.md` → R7.

### Relics (sampled) — see R1; raw: relics-sample.md, wave-1 a–c inline
- `[HIGH][VERIFY]` phantoms: brass-ring (≈Vajra), cables (≈Emotion Chip), strike-dummy (≈Wrist Blade).
- `[HIGH][VERIFY]` paper-crane (40%/Wrath-form + phantom Watcher tag → generic "Weakened enemies deal 25% less"), `heuristics/relics/bloody-idol.md` (invents 40–60 gold).
- `[MED][VERIFY]` rarity wrong: golden-idol, tungsten-rod, war-paint, red-mask, the-specimen, tingsha, tough-bandages. Effect: cauldron (random not choose), blue-candle (HP loss not damage), strange-spoon.
- `[LOW]` fossilized-helix Interactions → R6; coffee-dripper wording; anchor heuristic math.

### Buffs & Debuffs (exhaustive) — raw inline (wave-1)
- `[HIGH]` split (overkill + Poison inheritance contradict enemy files), pen-nib (→R2), confused (X-cost cards cost 0 is wrong).
- `[MED]` hex Interactions narrows non-Attack (drops Status/Curse) + smuggles strategy; sharp-hide A19 `[VERIFY]`; weak modifiable `[VERIFY]`.
- `[MED/LOW]` MOVE-TO-HEURISTICS (→R6): intangible, mantra, mode-shift, life-link, buffer, flight, storm, the-bomb, omega, burst, painful-stabs, time-warp. Redundant Interactions restating Effect: enrage, entangled, hex, pen-nib. foresight missing Watcher tag.

### Enemies & Bosses (exhaustive) — raw: enemies-nz-bosses.md + wave-1 a–m inline
- `[HIGH]` broken links (→R3): corrupt-heart `[[buffs/Painful Stabs]]`/`[[buffs/Beat of Death]]`/`[[buffs/Invincible]]`, awakened-one `[[buffs/Regenerate]]`(→Regeneration)/`[[buffs/Curiosity]]`, transient `[[buffs/Fading]]`+`[[buffs/Shifting]]`, writhing-mass `[[buffs/Reactive]]`, exploder `[[buffs/Explosive]]`, book-of-stabbing/giant-head category-mismatch.
- `[HIGH][VERIFY]` corrupt-heart Invincible 200/300 inverted; Blood Shots 2×15 hits/damage swapped (→2×12).
- `[HIGH]` `heuristics/enemies/centurion-mystic.md` internal 8×3 vs 6×3.
- `[MED]` missing ascension scaling (cultist, chosen, darkling, sharp-hide); looter/mugger duplication; darkling/darklings stem mismatch. Boss companion gap (no heuristic for corrupt-heart, spire-shield, spire-spear).

### Events (exhaustive) — raw: events.md
- `[HIGH]` the-nest ("Heal 10"→Lose 6), augmenter J.A.X. (wrong effect), forgotten-altar (omits Bloody Idol, %MaxHP), bonfire-spirits (missing rarity reward table). All `[VERIFY]`.
- `[MED]` pattern: **escalating mechanics flattened to constants** (scrap-ooze, knowing-skull, cursed-tome, wheel-of-change); reward-omitted/cost-only; values hard-coded for ~80-HP Ironclad instead of %MaxHP. → R1 (regenerate from data).

### Potions (exhaustive) — raw: potions.md
- `[HIGH][VERIFY]` blessing-of-the-forge (deck/random/permanent → all cards in **hand**, rest of **combat**; error mirrored in heuristic), distilled-chaos (1 card → top **3**, Sacred Bark 6).
- `[MED]` **none of 26 potions record Sacred Bark doubling** (atomic fact) → R1; flex-potion potency `[VERIFY]`. Generic "unused potion = failure" maxim duplicated across entries → R7.

### Encounters (exhaustive) — raw: encounters.md
- `[HIGH]` dead `[[enemies/Louse]]` links (2-louse, 3-louse, exordium-wildlife) — no generic Louse node. `[HIGH][VERIFY]` 3-shapes Act 3 vs Act 2 (the City) — misfiled in both encounter + enemy layers.
- `[MED][VERIFY]` exordium-thugs (Mugger is Act 2, can't be in Act 1), reptomancer (daggers summoned T1, not present at start). All 42 omit combined HP (may be intentional).

### Heuristic topic files (exhaustive) — raw inline (wave-1)
- `[HIGH]` rest-sites boss threshold 60% vs 70% elsewhere (→R7); drafting "Burning Blood 6% max HP" → flat 6.
- `[MED]` combat "No exceptions" overfitting; Wraith Form rule unsourced/Silent-in-Ironclad-file; curse-removal cost escalation; archetypes "All Wins Share" platitudes; Reaper unconditional.
- `[LOW]` combat.md/drafting.md bloat (>150 lines, split candidates); cross-file redundancy (→R7). CLEAN: exhaust.md.

---

## Systemic Patterns
1. **Paraphrase drift** (cards/relics/potions/events) — the dominant fact-error engine → R1.
2. **Category-mismatch / missing-target broken links**, unvalidated by build → R3.
3. **`buffs/` populated by effect not by power** (spurious + missing) → R2.
4. **Restructure staleness** (paths, counts, field names) → R4.
5. **Errors mirrored across ontology↔heuristic companions** (berserk, coolheaded, blessing-of-the-forge) — fix in pairs (R1 handles the ontology side).
6. **Agent-harness advice leaking into game heuristics** → R7.
7. **Missing ascension variants** — recurring incompleteness in enemies/buffs.
8. **Derived `Interactions:` lines in ontology** → R6.

---

## Coverage Log
| Chunk | Mode | Source |
|-------|------|--------|
| buffs (37), debuffs (18) | exhaustive | wave-1 |
| enemies a–m (26+19) | exhaustive | wave-1 |
| enemies n–z + bosses (35+27) | exhaustive | findings/enemies-nz-bosses.md |
| events (33+33) | exhaustive | findings/events.md |
| potions (26+26) | exhaustive | findings/potions.md |
| encounters (42) | exhaustive | findings/encounters.md |
| topic files (7) | exhaustive | wave-1 |
| misc ontology + heuristics/characters,development (24+6) | exhaustive | findings/misc.md |
| praxis/book-sts1/goals meta (31) | exhaustive | wave-1 |
| cards a–c (84+36) | exhaustive | wave-1 |
| cards d–l, m–z (73 sampled) | **sampled** | findings/cards-sample-*.md |
| relics a–c (37+21) | exhaustive | pilot |
| relics d–z (40 sampled) | **sampled** | findings/relics-sample.md |

---

## Working Pile — live status

- **R3 — wiki-link validation in `build.py`** — ✅ DONE. 77 broken occurrences / 44 unique targets inventoried; `--strict` available for CI.
- **R4 — strip brittle counts + fix genuinely-stale facts** (book-sts1 docs) — ✅ DONE. Most "stale paths" were false alarms (correct relative to `games/sts1/` cwd); fixed `last_agent`, build data path, phantom `goals` category.
- **R5 — state "ontology = atomic; derived → heuristics"** in framework docs — ✅ DONE (`splits.md` + layers/index/ontology/entry-quality).
- **R1 — regenerate card/relic/potion/event ontology from canonical sources** — 🔄 IN PROGRESS.
  - `tools/regen/compare_cards.py`: game wording (local jar localization) vs our card effects, no web. 24 keyword mismatches after noise reduction; **Crush Joints (Weak vs Vulnerable) confirmed against canonical game text**.
  - TODO: extend compare to relics/potions/events; add a community dataset for numbers/cost/rarity (localization lacks them); build the generator; show sample.
  - Finding: power-granting cards use a non-canonical "Apply N <Power> to self" phrasing vs the game's inline effect — decision needed (keep composable style vs inline canonical text).
- **R2 — rebuild `buffs/` around real powers** — ⏳ PENDING. Delete spurious (e.g. `pen-nib`); create missing (Wrath/Calm/Divinity stances; Fading/Shifting/Reactive/Invincible/Curiosity/Beat of Death; Vigor; After Image).
- **R6 — relocate derived `Interactions:` lines to heuristics** — ⏳ PENDING.
- **R7 — topic-file hygiene** (boss-rest threshold, de-dup cross-file advice, move agent-harness advice out of game heuristics) — ⏳ PENDING.
- **R8 — NEW: ontology `modes/` category** — ⏳ PENDING. Group the game's gameplay modes (combat, shop, map, event, rest, reward) as one category: move top-level `combat.md` → `modes/combat.md`, fold the 1-entry `shop` category in, add the missing mode entries (map/event/rest/reward mechanics). UI modes (main menu, settings) aren't play-relevant — out of scope unless completeness is wanted. Ripple: file moves + wiki-link updates (R3 validation will catch misses) + page-name change.
- **Flagged (your call):** duplicate CI workflows (`deploy.yml` + `deploy-site.yml`) race on the `pages` concurrency group — delete one.
- **Optional (declined):** make `build.py` write-in-place instead of `rmtree`-ing `site/out` — left as-is; clobber is simplest for handling deletions.
