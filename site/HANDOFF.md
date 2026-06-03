# Session Handoff — Site / Linking System

> **Ownership (2026-06-01):** this site/linking work is now owned by the
> awareness/regen agent — there is no longer a separate website session (and if one
> runs, it's UI-only). That agent maintains **both** this handoff and the root
> `HANDOFF.md`. See the "Note from the site/linking agent" at the end of root
> `HANDOFF.md` for the transfer summary and the one open item (linking-docs reconcile).


> **UPDATE (timer run, ~05:10 EST):** Reviewed the structure as the other agent left it
> and fixed the rebuild. The other agent added a new **`phenomena`** layer (derived
> facts — resolved upgraded cards like `a-thousand-cuts-plus`, generated from ontology
> by `tools/regen`; `phenomena/sts1/cards`, 333 entries) and had wired it into the build
> *logic* (LINK_LAYERS, section loop, SECTION_META, cards special-case) but **not the
> presentation**. Fixed: added `--phenomena` color (cyan), `.category-card`/`.node-row`/
> `.section-badge` phenomena CSS, the **Phenomena nav entry**, and a Phenomena card on the
> landing Knowledge grid. Build now exits 0, **1527 pages**, all key pages 200, broken
> links **64** (content gaps only). Also note: `awareness/` (memory JSON) and `tools/`
> (regen + awareness tooling, Python) are correctly ignored by the build.
>
> **Both pending items are now CLOSED:** (1) chose **ontology-canonical** — a bare
> cross-ref defaults to the ontology fact page. (2) Switched link qualifiers to
> spelled-out lowercase **`layer:` / `domain:` / `category:`** (no abbreviations) and ran
> the semantics-preserving codemod: 10 `[[goals/*]]` links → explicit `[[layer:goals, …]]`
> across 6 goal files (same targets, just explicit). `[[category/id]]` links were already
> canonical under ontology-default and left untouched. Build 1527 pages, broken
> links **47** (content gaps only — missing buff/enemy/relic ontology entries +
> encounter-name mismatches; see `site/out/broken-links.txt`). Also fixed two
> presentation bugs this run: `inline()` now protects backtick code spans so
> doc examples like `` `[[category/Name]]` `` stop rendering as broken links, and
> de-linked a substrate ref (`[[development/interface/sts1]]` → `interface/sts1/`). The resolver keeps a tolerant leading-keyword fallback,
> so old-style links still resolve even though content no longer uses them.

---


**Written:** 2026-06-01 ~02:06 EST. **Resume target:** ~05:06 EST (3h out), once the
other agent (working on the `awareness` memory model) is "for sure done."

This is a restart-proof record. If the session restarted, read this top-to-bottom;
it's everything a fresh context needs.

---

## TASK TO DO AT ~05:06 EST

Review the repo structure **as the other agent has left it**, then run and/or edit
`site/build.py` until the website builds clean and renders correctly for all the new
stuff. Specifically:

1. `python site/build.py` — must exit 0. Note the broken-wiki-link count it prints
   (baseline before this session's work was ~83; we got it to **66**, all genuine
   content gaps, not resolver bugs).
2. Check whether the other agent's changes broke the build or the link system:
   - `awareness/` is a NEW top-level dir holding **JSON** (`awareness/sts1/win.json`),
     a memory substrate — NOT link-addressable md. The build's `discover_nodes` only
     reads `goals`/`ontology`/`heuristics`, so awareness *should* be ignored, but
     confirm it doesn't trip anything and decide if awareness needs any site presence.
   - `tools/` is a NEW top-level dir (the "interface" body splitting out). Confirm the
     build ignores it cleanly.
   - The other agent has been editing `ontology/`, `heuristics/`, `goals/` content +
     the wiki-link validator. Re-run and reconcile.
3. Serve and eyeball: `python -m http.server 8000 --directory site/out` then check
   `ontology.html`, `goals.html`, `goals-sts1-tournament.html`,
   `ontology-sts1-cards.html`, and a few entry pages with `[[links]]`.
4. Fix `build.py` as needed so everything renders correctly.

**Serving note (important):** never start `http.server` with its cwd *inside*
`site/out` — the build does `shutil.rmtree(site/out)`, and on Windows a process whose
cwd is in that dir locks it, so the rebuild deletes the files but can't recreate the
folder → every page 404s. Always serve with `--directory` from elsewhere.

---

## LINKING SYSTEM — DESIGN (final) + STATE

### The design we converged on
- **Address model:** the **id** is the address. Qualifiers `L:` (layer) and `D:`
  (domain) are OPTIONAL and default to the current page's layer/domain. **Category
  stays explicit/visible** (as the `category/id` slash) because it tells a reading
  agent the target's *type* without a lookup. Flat layers (goals) have no category.
- **Why labeled L:/D::** order-free, so the arbitrary "layer vs domain" ordering is a
  non-question; the link never encodes it.
- **Layers** are two species: **knowledge layers** = link-addressable md
  (`ontology`, `heuristics`, `goals`) vs **substrate layers** = not linked
  (`awareness` = memory/JSON, `tools`/`interface` = body/code). `LINK_LAYERS` in
  build.py = `{ontology, heuristics, goals}`.
- **Domains:** `sts1`, `praxis`, `book-sts1`.
- **Bigger vision (NOT built):** a resolver *tool* + an `id → location` index, so the
  agent resolves links via the same tool call it already makes to *read* the target
  (zero marginal cost), and storage can be reorganized freely. Bare `[[id]]` would
  resolve via the index with collision-validation forcing a qualifier only on real
  ambiguity. The static-site build and the agent's resolver tool would share one
  index as the single source of truth.

### What's IMPLEMENTED in `site/build.py` (this session, additive, zero-regression)
- Rewrote `resolve_wiki_link` to support: optional `L:`/`D:` qualifiers; leading
  layer-keyword routing (`[[goals/next]]` → goals layer); `category/id` slash;
  `[[category/]]` → category index page; `[[…|Display]]` alias.
- Legacy `[[cards/Strike]]` unchanged (still defaults layer=ontology, domain=current).
- Bare unqualified `[[word]]` still renders as inline code (safe until the index lands).
- `_valid_pages` widened to include node-index and category-index pages.
- Fixed an apostrophe bug: `inline()` HTML-escapes before resolution, so `'` arrived as
  `&#x27;` and corrupted slugs (`Nilry's Codex` → `nilryx27s`). Now `html.unescape`d
  at the top of `resolve_wiki_link`.
- `LINK_LAYERS` and `_slugify()` helpers added.

### What's PENDING / OPEN
1. **BLOCKING DECISION (ask the user):** should a bare cross-reference default to the
   **current layer** (companion behavior: a `[[cards/X]]` on a heuristics page →
   heuristics entry) or stay **ontology-canonical** (a card mention always means the
   fact page)? Right now it's ontology-canonical (unchanged). This decision gates the
   content migration because flipping it silently retargets every existing
   heuristics→ontology reference.
2. **Content migration codemod (NOT run):** expand existing short links to the new
   minimal form across `ontology/ heuristics/ goals/`. Do it *semantics-preserving* —
   make the implicit explicit with `L:` where a target's layer ≠ the page's layer —
   and run as one verified pass. Touches the other agent's content, so coordinate.
3. **Remaining 66 broken links are content gaps**, not resolver bugs: missing entries
   (`enemies/louse`, several `buffs/*` like `fading`/`wrath`/`calm`/`vigor`), a
   malformed `[[development/interface/sts1]]` in `goals/sts1/develop.md`, and a couple
   literal `[[<category>/<name>]]` doc placeholders in tournament.md/win.md/praxis docs.
   These are the other agent's territory.
4. **Strict mode:** build supports `STS_STRICT_LINKS=1` (env var) to fail on broken
   links — added by the other agent. Don't turn it on globally until the gaps close.

---

## OTHER WORK DONE THIS SESSION (for context)

- **Site visuals:**
  - Section pages (`ontology.html`/`heuristics.html`/`goals.html`) now render the three
    domains as full-width **rows** ordered Slay the Spire → Book → Praxis, each with a
    tagline + a per-cell description (the 9 `(layer × domain)` blurbs). See
    `NODE_ORDER`, `NODE_TAGLINES`, `NODE_SECTION_BLURB` and `.node-row` CSS.
  - **Faceted cards page** (`ontology-sts1-cards.html`): interactive group-by
    (Character/Type/Rarity/Cost) + sort-by, collapsible groups, parsed live from each
    card's `- **Field:**` list. Cost rendering: clean costs as-is, upgrade costs as
    `1E (0E)+` (green parenthetical), conditional costs as base + `*` (e.g. `3E*`),
    no-base conditionals as `*`. See `render_faceted_cards`, `_parse_cost`,
    `parse_entry_fields`, `.card-tile`/`.facet-*` CSS.
- **Goals (knowledge content) — win% reasoning:** added a per-state **win%** model.
  - `goals/sts1/audit.md`: new primary lens — label win% at EVERY state (forward,
    outcome-blinded), `regret = win%(best available) − win%(chosen)` to strip variance,
    calibration = live-vs-retrospective gap. Output leads with steepest-regret +
    calibration gaps.
  - `goals/sts1/explore.md`: label win% at every state live.
  - `goals/sts1/win.md`: marked **casual** Win — labels win% as an affordable learning
    artifact.
  - `goals/sts1/tournament.md`: NEW goal — "sweaty" Win, every token on winning, NO
    win% labeling (it's a learning cost you can't afford at max effort).
  - `goals/sts1/next.md`: registers Tournament; notes which goals carry live labels
    (Casual Win + Explore) vs retrospective-only (Tournament).

## Repo facts worth knowing
- Working dir: `C:\Users\tkond\projects\praxis` (Windows, Python 3.14, git-bash + pwsh).
- Build output: `site/out/` (rebuilt from scratch each run; CNAME = claudeslaysthespire.org).
- A local web server may be running in the background on :8000.
- Tooling has been flaky this session: the Bash tool's cwd breaks after `rmtree site/out`
  (use absolute paths / PowerShell); some tool output gets truncated — verify via
  re-reads, don't trust a single garbled read.
