# Layers

The layers of the Praxis knowledge tree. Each layer is a top-level directory; within it, every domain that uses the layer has its own subtree (`<layer>/<domain>/…`). Most domains carry ontology, heuristics, and goals; phenomena appears only where a domain has stable derived constructs. Volume differs by layer and domain.

## Knowledge vs operational

The layers divide two ways. By what they are *about*:
- **Knowledge layers** — ontology, phenomena, heuristics — describe the *domain*: what is true, what it resolves to, what to do about it.
- **Operational layers** — goals, and awareness — govern how the *agent* runs: which mode it is in, and what to pull into context. They are not claims about the domain.

And by *form*:
- **Link-addressable** markdown — ontology, phenomena, heuristics, goals — entries reachable by `[[category/id]]` links (the site build's `LINK_LAYERS`).
- **Substrate** — awareness (JSON memory) and the body (`tools/`, `interface/` code) — served by tooling, not read or linked as prose.

Awareness sits at both intersections — operational *and* substrate — which is why it is documented under Memory in the Praxis index rather than given a markdown layer section here. Goals are operational but still link-addressable prose; the three knowledge layers are both knowledge and link-addressable.

## Ontology

**What things are.**

- Atomic facts, mechanics, definitions, numbers, behavioral patterns
- Composable — two facts can be combined to derive a third; that derivation, when materialized, is a *phenomenon* (below), not stored in ontology
- Atomic only — no derived/composed consequences (worked examples, resolved values, interaction results); those are materialized as phenomena
- Closure-checked — a correct entry never needs revision, only extension
- No strategic language: no "should," "always," "never," "prioritize"

An ontology entry is either correct or incomplete. It can be extended (new ascension data, additional mechanics) but its existing content doesn't become wrong.

## Phenomena

**Derived facts, materialized.**

- Materialized derivations from ontology, of two species (see [[retrieval]]):
  **resolutions** — deterministic compositions (a resolved upgraded card, an
  encounter roster) — are *generated* by tooling and regenerated rather than
  edited; **recognitions** — a configuration of things that should bring a
  particular thought process to mind (a card combo, a dangerous board state) —
  are *authored*, because neither when they apply nor whether they're worth
  keeping is derivable from structure.
- Each carries links back to the noumena it derives from.
- Materialized only when the derivation is *stable, reused, and error-prone to recompute under time pressure* — the justification heuristics get, applied to facts. The long tail of possible derivations is computed on demand at runtime (working memory), never stored.
- A phenomenon names what a situation *resolves to*; a recognition's body points at the situation-tailored heuristics it should call to mind, rather than restating strategy itself.

Ontology is the generative truth (the noumenon); a phenomenon is its resolved, practical form. The game itself runs this split — a card's class defines base values plus an upgrade transform; the live instance holds the resolved values.

## Heuristics

**What to do about things.**

- Strategy, decisions, priorities, warnings, algorithms
- Provisional — every heuristic is a current best guess that may be updated
- Evidence-grounded — claims cite observed outcomes
- Conditional — good heuristics specify when they apply AND when they don't
- Actionable — every sentence should help make a specific decision

A heuristic entry IS expected to change. It represents the system's current understanding, which improves as more evidence accumulates.

### Two types of heuristic entries:
- **Per-entity** — specific guidance for one entity (a card, an enemy, a knowledge category). Lives in a category subdirectory.
- **Topic** — cross-cutting guidance that applies across many entities (combat execution, drafting strategy). Lives as a top-level file in the heuristics domain.

Topic files are typically the most valuable entries in a heuristic set because they capture patterns no individual entity entry can.

## Goals

**What to do right now.**

- Operating mode definitions — what to read, what to do, what to output
- Define the agent's purpose for a session
- Include decision logic for when to switch modes
- Separate from heuristics because they're about agent behavior, not domain strategy

Goals are the most stable layer. They change when the pipeline structure changes, not when domain knowledge improves.
