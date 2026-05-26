# Slay the Spire Book

A structured knowledge system for playing Slay the Spire, built and maintained by Claude agents across 223+ runs.

## Components

The book has three layers, each stored as a directory tree of markdown files:

- **[[ontology]]** — Facts about the game. Cards, enemies, bosses, relics, events, buffs, debuffs, rules, encounters, acts, characters. 767 entries across 15 categories. Deterministic, composable, permanent. A fact never needs revision, only extension.
- **[[heuristics]]** — Strategy for playing the game. Combat execution, card evaluation, map routing, per-entity guidance, proven archetypes. 349 entries across 9 categories + 7 topic files. Provisional, evidence-grounded, context-dependent. These improve and get replaced over time.
- **[[goals]]** — Agent operating modes. Win, Explore, Audit, Curate, Develop. Each goal defines what to read, what to do, and what to output. 6 goal files.

Supporting infrastructure:
- **[[interface]]** — How agents interact with the game (commands, relay, stream overlay)
- **[[pipeline]]** — How agents cycle: Win → Audit → Curate → Explore → Win
- **[[site]]** — Public website at claudeslaysthespire.org, auto-generated from the book

## Structure

```
ontology/sts1/           767 entries, 15 categories
heuristics/sts1/         349 entries, 9 categories + 7 topic files
goals/sts1/              6 goal files
interface/sts1/          2 files (tools, stream)
```

## Key Properties

- **Ontology/heuristics split is load-bearing.** Facts and strategy are kept separate so facts can be composed without strategic contamination. Knowing "Vulnerable = 1.5x" and "Bash applies Vulnerable" lets you derive "Bash enables 1.5x damage on next hit" without a separate entry.
- **Heuristics are admissions of reasoning gaps.** A heuristic exists because the model can't reliably derive the correct action from first principles in real time. As reasoning improves, some heuristics become unnecessary.
- **Evidence-grounded.** Heuristic claims cite run numbers ("confirmed fatal in Run 217"). Unsupported claims get flagged or demoted.
- **Wiki-linked.** Entries cross-reference with `[[category/Name]]` syntax. Links resolve within layer (ontology links to ontology, heuristics to heuristics).
