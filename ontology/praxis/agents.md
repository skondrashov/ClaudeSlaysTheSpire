# Agent

The single actor that reads from and writes to the knowledge system. There is one agent. It is given a goal, reads the knowledge relevant to that goal, performs actions in the domain, and writes back what it learned.

## Properties

The agent:
- **Has a current goal** — one of the goal files, which defines what to read, what to do, and what to output
- **Reads from all three layers** — ontology for facts, heuristics for strategy, goals for operating mode
- **Writes to specific layers** — different goals have different write targets
- **Operates one action at a time** — no autonomous loops, no background automation

## Goals, Not Roles

A goal is not an identity. The agent doesn't become a different entity when it switches from playing to auditing — it changes what it's optimizing for, which changes which heuristics are relevant. The goal file specifies:
- What knowledge to load
- What behavior is expected
- What output to produce
- What goal to recommend next

## Goal Cycling

Goals cycle to prevent the system from converging on local optima:
- Only playing → overfits to current strategy
- Only curating without exploring → replaces one bias with another
- Only exploring without curating → no direction for experiments
- Only auditing without curating → flags errors that never get addressed

The cycle pattern and cadence are domain-specific, defined in the domain's goal files.
