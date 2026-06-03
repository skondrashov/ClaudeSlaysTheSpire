# Retrieval — survey & recall

How a playing agent gets knowledge out of the web. Generic Praxis mechanism;
domains plug in. Replaces force-feeding (a script composing the prompt from
on-screen state) with **agent-driven retrieval**: tool calls report *options*, the
agent composes its own context.

## The two verbs

- **`survey(state)`** — returns a *menu of handles*: paths to documents the agent
  *might* want, given the live state. No content. The agent reads the menu against
  its own reasoning and decides what's worth pulling.
- **`recall(handles)`** — returns the full text of exactly the named documents.
  **Does not follow links.** Links inside returned text are just more menu items;
  to navigate them the agent calls `recall()` again. (Auto-following would
  re-introduce force-feeding through the back door.)

Both are generic verbs and live in the Praxis layer. A domain supplies only *data*
(its index) and *its state* — there is no domain-specific procedure. The agent sees
one interface (the game tools); `survey`/`recall` there are thin pass-throughs to
the Praxis verbs.

## What survey returns, and how

`survey` is **one model call**. You cannot know whether a contextual interaction
applies without asking, so there is no cheaper deterministic pre-pass that saves a
call — the reranker returns everything relevant in one shot: ontology, heuristics,
and phenomena handles for the situation.

It works by handing the live state plus an **index** to a small/fast model (e.g.
Haiku), which returns the handles whose entries might apply. The model holds the
index; the state is the query. The model is instructed to **return paths only**.

## The index: `{blurb, target}`

One uniform shape per entry:

- **blurb** — an applicability descriptor ("surface me when …"), written *for the
  reranker*.
- **target** — what to recall: usually a path, sometimes a *pattern*.

Two kinds of entry populate it:

1. **Resolvable phenomena** (generated upgrade forms, `phenomena/sts1/cards/`):
   collapse to **one rule entry** — *"for any `+` card in state, include its
   resolved form."* The target is a pattern, not a path. No per-card entries; the
   mapping is mechanical and the reranker just applies the rule.
2. **Contextual phenomena** (`phenomena/sts1/interactions/`): one entry each, the
   blurb **extracted** (mechanically) from the file's authored `Applies when:`
   field. Ontology/heuristic availability for on-screen entities rides along the
   same call.

## Authored vs programmatic — the hard line

The split that matters: **blurbs are authored, extraction is programmatic.** A
contextual interaction can take any shape (a two-card combo, or a whole board-state
pattern), so *nothing* about when it applies is derivable from structure — not even
"both participants present" is a reliable trigger. The semantic content is
human/agent-authored end to end; code only lifts the already-written blurb into a
searchable index.

Likewise **materialization** — deciding a recurring derivation is *worth caching as
a phenomenon* — is an agent judgment, vague on purpose. Recognizing "this is worth
keeping" is the same unscripted recognition as relevance itself, on the write side.
There is no frequency threshold; an LLM (the codify/analyst loop) makes the call.
This is why phenomena are authored, not generated: the entire point of an LLM is to
do the part that can't be scripted.

## Two readers per phenomenon

Authoring a contextual phenomenon means writing for two audiences in one file: the
**blurb** is retrieval bait for the reranker, the **body** is knowledge for the
playing agent. Different register, same file. See `phenomena/sts1/interactions/`.

## Where the pieces live

- **Praxis (generic):** the `survey`/`recall` verbs, the index format, the rerank
  call, the upgrade rule.
- **Domain (data + thin glue):** the index contents (its phenomena), and handing
  the reranker the domain's live state. For sts1 that state already arrives from
  CommunicationMod; if raw state is reranker-legible (expected), the sts1 `survey`
  is a one-liner and carries no procedure — the domain-specificity is the index.
- **Agent:** sees only the game tools. Calls `survey()` when it wants a menu;
  `recall()` to pull. Cadence is the agent's choice, not a fixed schedule.

## Status

Built, not yet validated against a live run. Implementation:
- `tools/retrieval/build_index.py` — extracts `Applies when:` blurbs into the
  `{blurb, target}` index (+ the upgrade rule entry); writes `awareness/<domain>/survey-index.json`.
- `awareness/sts1/survey-index.json` — the committed built index.
- `tools/retrieval/survey.py` — `survey()` (one cached reranker call, returns paths
  only), `recall()` (fetch, no link-following), `load_index()`.
- `games/sts1/cmd.py` — agent-facing `survey()`/`recall()` (thin wrappers; guarded import).

Open: needs `ANTHROPIC_API_KEY` at runtime; reranker prompt + model
(`claude-haiku-4-5`) to be tuned against real surveys; cadence is the agent's call.
