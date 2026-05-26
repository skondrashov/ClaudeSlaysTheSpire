# Layers

The three knowledge layers in Praxis. Every node has entries in all three layers, though the volume differs.

## Ontology

**What things are.**

- Facts, mechanics, definitions, numbers, behavioral patterns
- Deterministic and composable — two facts can be combined to derive a third
- Closure-checked — a correct entry never needs revision, only extension
- No strategic language: no "should," "always," "never," "prioritize"

An ontology entry is either correct or incomplete. It can be extended (new ascension data, additional mechanics) but its existing content doesn't become wrong.

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
- **Topic** — cross-cutting guidance that applies across many entities (combat execution, drafting strategy). Lives as a top-level file in the heuristics node.

Topic files are typically the most valuable entries in a heuristic set because they capture patterns no individual entity entry can.

## Goals

**What to do right now.**

- Operating mode definitions — what to read, what to do, what to output
- Define the agent's purpose for a session
- Include decision logic for when to switch modes
- Separate from heuristics because they're about agent behavior, not domain strategy

Goals are the most stable layer. They change when the pipeline structure changes, not when domain knowledge improves.
