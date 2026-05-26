# Agents

Actors that read from and write to the knowledge system. An agent is given a goal, reads relevant knowledge, performs actions in the domain, and writes back what it learned.

## Properties

Every agent:
- **Has a goal** — one of the goal files, which defines what to read, do, and output
- **Reads from all three layers** — ontology for facts, heuristics for strategy, goals for operating mode
- **Writes to specific layers** — different agents have different write permissions
- **Operates one action at a time** — no autonomous loops, no background automation

## Agent Roles

A Praxis system defines domain-specific agent roles. These typically include:

- **Performer** — acts in the domain (plays the game, solves the puzzle, writes the code). Reads knowledge, follows heuristics, records observations.
- **Analyst** — reviews the performer's work for correctness. Checks execution against knowledge. Flags errors but doesn't rewrite strategy.
- **Curator** — evaluates the knowledge system itself. Checks for overfitting, coverage gaps, contradictions, quality. Writes exploration directives.
- **Explorer** — tests hypotheses from the curator or the performer's observations. Willing to try non-standard approaches to generate evidence.

Not all systems need all roles. A minimal Praxis setup is just Performer + Curator.

## Agent Cycling

Agents cycle to prevent the system from converging on local optima:
- Only performing → overfits to current strategy
- Only curating without exploring → replaces one bias with another
- Only exploring without curating → no direction for experiments
- Only analyzing without curating → flags errors that never get addressed

The cycle pattern and cadence are domain-specific, defined in the domain's goal files.
