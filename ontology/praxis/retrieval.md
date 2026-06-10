# Retrieval — survey & recall

How a playing agent gets knowledge out of the web. Generic Praxis mechanism;
domains plug in. Replaces force-feeding (a script composing the prompt from
on-screen state) with **agent-driven retrieval**: tool calls report *options*, the
agent composes its own context.

## The two verbs

- **`survey(state)`** — returns a *menu of handles*: addresses of entries the agent
  *might* want, given the live state. No content. The agent reads the menu against
  its own reasoning and decides what's worth pulling.
- **`recall(handles)`** — returns the full text of exactly the named entries.
  **Does not follow links.** Links inside returned text are just more menu items;
  to navigate them the agent calls `recall()` again. (Auto-following would
  re-introduce force-feeding through the back door.)

Cadence is the agent's choice, not a fixed schedule — survey at meaningful decision
points, recall whatever the menu (or the agent's own reasoning) makes relevant.

## What survey returns, and how

`survey` is **one model call**. You cannot know whether a contextual phenomenon
applies without judgment, so there is no cheaper deterministic pre-pass that saves
a call — the selector returns everything relevant in one shot: the on-board
entities (with their heuristic handles), upgraded cards, and any phenomenon whose
conditions match the state.

It works by handing the live state plus the domain's **map** to a small/fast model
(e.g. Haiku), which returns the applicable handles. The model holds the map; the
state is the query. The model is instructed to **return handles only** — never
content, never composed prose.

## The map

The index is not a list of every entity (that would be hundreds of lines restating
the directory tree). It is a **condensed map**: how to address anything, plus the
exceptions.

1. A **slug rule** that resolves the vast majority of names by convention.
2. The **category search order** for bare names. A name that exists in several
   categories returns every match.
3. The **upgrade rule** — `<name>+` addresses the resolved upgraded card.
4. An **alias table** — only the names that don't slug to their file, plus any
   phenomenon recognition lines (`<applies-when>: <path>`).

Recall honors the same map: names resolve by slug, then by alias, in any layer.

## Two species of phenomena

A phenomenon is a materialized derivation, and the two ways one comes to exist are
different in kind:

- **Resolutions** — deterministic compositions of ontology: an upgraded card
  (base ⊕ delta), an encounter roster. **Generated** by tooling from the noumena
  and regenerated rather than edited; each links back to what it derives from.
- **Recognitions** — a particular configuration of things that should bring a
  particular thought process to mind: a card combo, a dangerous board state, a
  situation with its own tailored guidance. **Authored**, because nothing about
  when the configuration applies — or whether it is worth keeping at all — is
  derivable from structure. Recognizing "this is a thing you see" is the same
  unscripted judgment as relevance itself, on the write side; the codify loop
  makes the call, with no frequency threshold.

An authored phenomenon is written for two readers in one file: its
**applies-when** is retrieval bait for the selector (it becomes the phenomenon's
line in the map), its **body** is what the recognition resolves to — linking the
situation-tailored heuristics it should bring to mind. Different register, same
file. Recognitions are how the awareness layer gets filled out: each one teaches
the selector a situation worth surfacing before the agent thinks to ask.

## Where the pieces live

- **Praxis (generic):** the `survey`/`recall` verbs, the map format, the selector
  call.
- **Domain (data + thin glue):** the map contents, the live state handed to the
  selector, and the name-resolution conventions (slug, categories, aliases) its
  entries follow.
- **Agent:** sees only the game tools. Calls `survey()` when it wants a menu;
  `recall()` to pull.

## Status

Validated against live runs. Implementation:

- `tools/retrieval/build_index.py` — builds the condensed map (slug rule, category
  order, upgrade rule, auto-detected aliases); writes
  `awareness/<domain>/survey-index.md`.
- `awareness/sts1/survey-index.md` — the committed map.
- `tools/retrieval/survey.py` — the selector call (one `claude -p` invocation,
  subscription auth, small/fast model; returns handles only) and `load_index()`.
- `games/sts1/cmd.py` — agent-facing `survey()`/`recall()`; recall implements the
  map's name resolution (slug, category search, aliases, layers).

Open: selector latency (~10–50s per call via CLI cold start) is acceptable but
unloved; recall's name resolution should eventually hoist into the generic layer
so a new domain gets it for free; no authored recognitions exist yet — the first
one is the real test of the applies-when path through the selector.
