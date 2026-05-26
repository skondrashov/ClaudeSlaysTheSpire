# Praxis

A framework for building domain knowledge through structured practice. Theory-informed action: you do something, reflect on what happened, codify what you learned, and use the codified knowledge to act better next time.

## Structure

Praxis organizes knowledge into three layers stored as directory trees of markdown files:

- **Ontology** — What things ARE. Facts, mechanics, definitions, behavioral descriptions. Deterministic and composable. A correct fact never needs revision, only extension.
- **Heuristics** — What to DO about things. Strategy, decisions, warnings, algorithms. Provisional and evidence-grounded. These improve over time as understanding deepens.
- **Goals** — Operating modes. What to read, what to do, what to output, and when to switch modes. Define the agent's purpose for a given session.

Each layer has the same directory structure: a top-level directory containing **nodes**, where each node is a domain or body of knowledge.

## Nodes

A node is a self-contained knowledge domain within a layer. Current nodes:

| Node | What it covers |
|------|---------------|
| `praxis` | The framework itself (this) |
| `sts1` | Slay the Spire — facts, strategy, and goals for playing the game |
| `book-sts1` | The Slay the Spire Book — facts, strategy, and goals for maintaining the STS1 knowledge system |

Each node appears in all three layers:
```
ontology/praxis/     ontology/sts1/     ontology/book-sts1/
heuristics/praxis/   heuristics/sts1/   heuristics/book-sts1/
goals/praxis/        goals/sts1/        goals/book-sts1/
```

## Key Properties

- **Ontology/heuristics split is load-bearing.** Facts and strategy are kept separate so facts compose without strategic contamination and strategy can evolve without destabilizing facts.
- **Heuristics are admissions of reasoning gaps.** A heuristic exists because the correct action can't be reliably derived from first principles in real time. As reasoning improves, some heuristics become unnecessary.
- **Evidence-grounded.** Heuristic claims are grounded in observed outcomes, not theory alone.
- **Self-referential.** Praxis is itself described in Praxis (this node). The ontology of Praxis describes what it is; the heuristics of Praxis describe how to use it well.

## Books

A **book** is a Praxis-built knowledge system for a specific domain. The book node (e.g., `book-sts1`) describes the book's structure, coverage, and health. The domain node (e.g., `sts1`) contains the actual domain knowledge.

A book is the product. Praxis is the process.
