# Session Handoff — Awareness · Phenomena · Card Regeneration

**Written:** 2026-06-01 (updated through the design session). Restart-proof record of the
memory/awareness build. **I now own both this handoff and `site/HANDOFF.md`** — the whole
site/linking system transferred to me (the other agent finished; see its note below).
Nothing is committed — all changes are in the working tree for review before commit.

---

## Vocabulary (settled this session)

The knowledge tree is a grid of **domain × layer**.

- **Domain** (was "node") — what knowledge is *about*: `sts1` (an environment), `praxis`
  (the framework), `book-sts1` (the book's self-knowledge). Renamed node→domain across
  `ontology/praxis/*.md` and the awareness tool's `domain=` parameter.
- **Layer** — the *kind* of content. Two orthogonal splits (see `ontology/praxis/layers.md`):
  - *knowledge* (ontology, phenomena, heuristics) vs *operational* (goals, awareness)
  - *link-addressable md* (ontology, phenomena, heuristics, goals) vs *substrate*
    (awareness = JSON, `tools/`/`interface/` = code). Build's `LINK_LAYERS` enforces this.

## The three new pieces

### 1. Phenomena — a new top-level layer (`phenomena/sts1/cards/`)
Derived, materialized facts. A noumenon (ontology) holds **base + an upgrade delta**;
the phenomenon is the **resolved** upgraded card. Generated, marked DO-NOT-EDIT, each
falling back to its noumenon via a `[[cards/<slug>|Name]]` link.
- `ontology/sts1/cards/bash.md`: `Effect: Deal 8 damage. Apply 2 Vulnerable.` + `Upgrade: +2 damage, +1 Vulnerable`
- `phenomena/sts1/cards/bash-plus.md`: `# Bash+` … `Effect: Deal 10 damage. Apply 3 Vulnerable.`
- 333 phenomena files generated. Fixes the old bug where `Grand Finale+` implied it was
  playable with a non-empty draw pile (the delta system never restates resolved numbers).

### 2. Awareness — the relevance index + loader (`awareness/sts1/`, `tools/awareness/`)
"What to pull into context before you've seen it," learned not computed.
- **Data:** `awareness/<domain>/<goal>.json` manifests (machine twin of a goal's
  "Knowledge Entry Points"). Today: `awareness/sts1/win.json`, goal tier only.
- **Tool:** `tools/awareness/` — generic loader whose ONLY state is a session dedup cache
  (`games/sts1/data/awareness_cache.json`). `load()` (bulk preload), `load_one()` (single
  entity), `load_goal()`, `reset()`. Both reads dedup against one cache.
- **CLI:** `python -m tools.awareness --goal win --json` (loads 7 refs + ~125 links;
  re-run in same session → all dedup'd). `--reset` to invalidate (new run / compaction).
- **Memory loop:** a session only READS (LOAD/RETRIEVE). Writing back (CODIFY) is a
  *separate* analyst job — see `ontology/praxis/index.md` Memory section.

### 3. Generator — base+delta noumena + phenomena (`tools/regen/`)
- `generate.py` — `render()` (noumenon), `render_phenomenon()` (resolved). Delta comes from
  the dataset's **structured fields** (never `upgrade.description`, junk for ~2 cards), with
  `WORDED_DELTAS` for text-change upgrades, `DESC_OVERRIDE` for cards whose dataset
  description dropped the `[W]` energy glyph (Deva Form/Fasting/Follow-Up — restored from
  the game jar), and `energy()` to render `[R][R]` → `2 Energy`.
- `stage_cards.py` — stages to `staging/` (gitignored) + `staging-report.md`. Compares
  effect *meaning* (number-sets, energy-normalized, card-self-name dropped, plural-tolerant)
  so the report shows genuine diffs, not phrasing.
- `apply_cards.py` — **the only writer.** `--apply` / `--only` / `--force`; dry-run default.
  Preserves provenance (Strike/Defend `Character: All`; Apparition/Bite rarity) and a
  data-loss guard skips entries carrying hand-written prose. **Already applied** this session.

## What was applied (review before commit)
- 354 noumena rewritten + 11 new cards (`ontology/sts1/cards/` now 361 files), 333 phenomena.
- **61 metadata fact-fixes** from canonical data — full list in the `apply_cards.py` dry-run
  output: ~40 cost-encoding cleanups, 12 rarity fixes, Zap 0→1, Barrage/Talk-to-the-Hand 2→1,
  X-cost formats, Sadistic Nature Silent→Colorless. **Spot-check the 12 rarity changes** —
  they trust the dataset over the (known-erroneous) hand-authored entries.
- Several effect fixes where the current entry was wrong: Coolheaded draw 3→2, Follow-Up
  ("costs 0" → "gain 1 Energy"), Shockwave 2→3 Weak/Vuln, Deva Form loses Ethereal.
- `site/build.py`: phenomena added to `LINK_LAYERS`, `SECTION_META`, the section list,
  `git_changelog` pathspec, and the faceted card view. Build green (now 47 broken / 1527
  pages after the other agent's linking migration; all broken links are content gaps).
- `games/sts1/cmd.py` (live bot): the **dead-path bug is fixed** (ONTOLOGY_DIR/HEURISTICS_DIR
  pointed at non-existent `games/sts1/{ontology,heuristics}`; now the praxis root tree).
  `_load_phenomenon` added — `+` names serve the resolved phenomenon. Awareness cache resets
  at run end (guarded import; the bot never crashes if the tool tree is absent).

## Open items / not done
- **cmd.py `reason()`/`plan()` are superseded by the design direction below** — move to
  `survey` + `recall` (agent-driven selective pull), not the current force-feed or full
  tool-delegation. They work today (the dead-path bug is fixed; they use the corrected direct
  loaders), which is fine until survey/recall is built.
- **Linking docs: RESOLVED.** The other agent locked **ontology-canonical** + spelled-out
  `layer:`/`domain:`/`category:` qualifiers; I reconciled the three prose docs
  (`ontology/praxis/entries.md`, `ontology/book-sts1/{index,linking}.md`) to match. I now own
  the whole site/linking system (build, resolver, broken-link health).
- **Deferred (plan):** the situation/entity awareness tiers — but see the design direction:
  the situation tier turns out to be the *neural retriever*, not a static manifest. Automatic
  compaction hook still deferred. (`.phenomena-card` CSS is **done**.)
- **Verify commands:** `python -m tools.awareness --goal win --json` · `python tools/regen/apply_cards.py`
  (dry-run) · `python C:\…\site\build.py` (47 broken / 1527 pages; run by absolute path — both
  shells drift cwd into `ontology/sts1/cards`).

## Design direction — agent-driven retrieval (discussed this session, NOT built)

A long conversation reframed how the playing agent should get knowledge. The static files
(ontology = parametric rules, phenomena = cached common compositions) are a **corpus**; the
live memory operations *over* it are partly neural. Conclusions, in dependency order:

**Replace `reason()`/`plan()` force-feeding with `survey` + `recall`.** Today `plan()` dumps the
full ontology+heuristic bundle for every on-screen entity — retrieval *policy* baked into the
body. Invert it so the agent owns policy:
- **`survey`** — maps live state to a *zero-depth availability index*: for each on-screen entity,
  which layers have an entry (ontology / phenomenon / heuristic). No content, not even one-liners
  — purely "what's recallable." Game-specific glue in cmd.py over the generic loader.
- **`recall(handles)`** — fetches exactly the named entries, full text, and **does NOT follow
  links** (links in returned text are an inline menu; the agent recalls again to navigate). Built
  on `load(payload)` with `resolve_links: false`. The agent picks layer + depth + entities.
- Loop: survey → agent reads the menu against its reasoning → recall the few it needs → decide.
  `reason()` survives as a one-off recall.

**State carries the entities + live cost, never card damage.** `format_state` already gives the
hand, the piles (grouped summaries), relics, potions, intents (`move_adjusted_damage` resolved),
and each card's *live* cost (combat-active cost mods reflected — caveat: this-turn `cost_for_turn`
reductions may not show; `is_playable` corroborates). It carries **no** per-card damage/block. So
survey's job is the *knowledge the state omits* (what a card DOES), not re-dumping state.

**Phenomena identity = an index, not name-matching.** "Is Bash+ a phenomenon?" shouldn't be
inferred from the `-plus` filename. Split it: (1) the *domain adapter* resolves a live instance →
entity ids (upgrades≥1 → the upgraded id; a Slay-the-Spire rule, in cmd.py); (2) a *generator-built
index* (`id → {layers/locations}`, plus interaction→participants) records what was actually
generated. survey resolves, then looks up — no filename sniffing. Same `id → location` index the
link resolver wants (one index, two consumers). Generalizes past `+` (encounters; Searing Blow's
unbounded upgrades).

**Relevance retrieval is fundamentally neural.** A phenomenon's *relevance* is contextual ("only on
Act 2," "when Corruption costs 4") and unenumerable — you cannot extend survey per-combo. Two-stage:
cheap **deterministic candidate generation** (on-screen entities + their linked/participant
phenomena, deliberately over-including) → **neural rerank** (a small/Haiku model holding the
*candidate index*, queried by live state, returns relevant ids) → recall. The deterministic
survey/index is stage-1 candidate-gen, NOT the retriever. *This is what awareness IS* — the answer
to "what do you feed the retriever," which is why the deferred situation tier was hard (it's the
corpus-assembly problem) and has to be a model. Asymmetry with *materialization* (the write side):
it also needs a net (recognizing "this combination again" is the same vagueness), but its input is
just a *sequence of runs* + a targeted dedup check — it never needs the corpus fed to it. Retrieval
is the hard one precisely because feeding it the corpus is unsolved.

**Working memory for per-instance state.** Class (ontology/phenomena) ≠ instance (a specific card
with mutable state). Cards that carry changing values — Rampage (+dmg/play), Glass Knife (−dmg/use),
Genetic Algorithm (+block), Searing Blow (unbounded) — have current values the state does NOT
surface. The instance layer:
- Keyed by card **uuid** (CommunicationMod gives each card a uuid distinct from its type id —
  **verify this**; the layer rests on it). Solves "two Rampage+'s, off-by-one or synced" trivially.
- Working memory = a uuid-keyed ledger that **folds observed play events through the ontology's
  parametric rules** (Rampage's "+5/play" is the transition fn). The entry *is* the live instance.
- Lookup cascade: **uuid → working memory → phenomenon → ontology**, first hit wins; most cards stop
  at the phenomenon (no instance state).
- **Requires the ontology to carry executable/parametric rules**, not just base+delta — a real
  completeness requirement (base+delta materializes the common +1; unbounded/odd cases force the rule).
- Opposite difficulty from relevance: instance lookup is an *exact key* into a *small* store (easy
  retrieval, hard *maintenance* of the fold); relevance is keyless over a large corpus (reverse).

**Where the new maintenance lives.** survey code, awareness manifests, and the "materialize this
recurring derivation" judgment are all *maintained operational bridges* from situation→knowledge,
kept in sync with the KB between runs, evidence-driven, via codify — a "maintain the bridge" family
next to `goals/book-sts1/awareness.md`. New *instance* of a known phenomenon kind = automatic
(generator+index); new *kind* = the judgment + teaching survey's resolver, same owner. The
retrieval-miss audit loop is the reactive safety net if the bridge drifts.

## Pointers
- Plan: `C:\Users\tkond\.claude\plans\okay-let-s-build-the-fuzzy-whale.md`
- Canonical concept docs: `ontology/praxis/{index,layers,entries}.md`
- The other agent's site/linking handoff: `site/HANDOFF.md`

---

## Note from the site/linking agent — 2026-06-01 (ownership handoff)

Leaving this from the site/linking session. **Going forward you own BOTH handoffs** —
this one and `site/HANDOFF.md`. The user does not plan to run a separate website
session; if they do, it'll be strictly UI-only. So the site build (`site/build.py`),
the wiki-link resolver, broken-link health, and the whole linking system are now yours
to maintain alongside the awareness/regen work.

**State of the site/linking work (all in working tree, uncommitted):**
- Linking decision locked: **ontology-canonical** — a bare `[[category/id]]` resolves to
  the ontology page regardless of the page's layer; explicit `layer:` / `domain:` /
  `category:` (spelled out, lowercase, no abbreviations) override. Resolver + migration
  done; the 10 `[[goals/*]]` links were converted to `[[layer:goals, …]]`.
- `inline()` now protects backtick code spans, so doc examples like `` `[[category/Name]]` ``
  render literally instead of resolving to broken links.
- Phenomena fully presented: nav entry, `--phenomena` color, `.category-card` /
  `.node-row` / `.section-badge` CSS, landing-grid card. Your deferred `.phenomena-card`
  cosmetic item is **done**.
- Build green: 1527 pages. Broken links **47**, all genuine ontology content gaps
  (missing buff/enemy/relic entries + `[[encounters/X]]` names that actually live under
  `enemies/`); full list in `site/out/broken-links.txt`. **None are resolver bugs.**
- Full detail in `site/HANDOFF.md`.

**The one open site concern — needs your hand:**
The linking **docs still describe the OLD resolution model** and now contradict the
shipped resolver. They say links resolve "within the same layer" (current-layer / option B),
but we shipped **ontology-canonical** (option A). Update these to ontology-canonical + the
`layer:`/`domain:`/`category:` grammar:
- `ontology/praxis/entries.md` — "links resolve within the same layer and domain"
- `ontology/book-sts1/index.md` — "ontology links to ontology, heuristics to heuristics"
- `ontology/book-sts1/linking.md` — the "within layer" framing

I left these for you on purpose: they're your conceptual prose (praxis/book voice), and you
already flagged the reconciliation in this handoff (the "other agent owns links" item). With
the decision now made, it's just the edit.

**→ DONE (this session):** all three linking docs reconciled to ontology-canonical + the
spelled-out `layer:`/`domain:`/`category:` grammar (examples backtick-protected so they render
literally). Rebuild still 47 broken / 1527 pages — no resolver regressions.
