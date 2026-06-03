# Interaction Phenomena

Contextual phenomena: card/relic/enemy **interactions and combos** whose relevance
is situational and cannot be enumerated from a single on-screen entity. The other
phenomena category (`phenomena/sts1/cards/`) is *resolvable* — generated upgrade
forms, derivable by rule. These are the opposite: **agent-authored**, arbitrary in
shape, and surfaced by relevance judgment, not by a lookup.

## File format

Every entry has two designated parts, written for two different readers:

- **`- **Applies when:**`** — the *applicability blurb*. Retrieval bait, written
  for the survey selector (a small model): "surface me when …". This is the field
  the index extractor pulls. It is **authored**, never generated — an interaction
  can take any shape, so nothing about when-it-applies is programmatically derivable.
- **body** — the knowledge itself, written for the playing agent. The `recall()`
  target. Links in the body are an inline menu the agent may recall next; they are
  not auto-followed.

## How they're used

`survey()` hands live state + the interaction index (blurbs only) to the selector,
which returns the handles of interactions that might apply. The agent then
`recall()`s the ones it wants. See [[domain:praxis, retrieval]] for the full model.

## How they're created

An analyst/codify agent writes these from observed runs (and known theory). Deciding
that a recurring interaction is *worth materializing* is an unscripted judgment — the
same vague recognition problem as relevance, on the write side. That is why an LLM
authors them.
