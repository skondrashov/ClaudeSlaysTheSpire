# Slay the Spire Book

A structured knowledge system for playing Slay the Spire, built and maintained by Claude agents across 223+ runs.

## Components

The book has three layers, each stored as a directory tree of markdown files:

- **[[ontology]]** — Facts about the game. Cards, enemies, bosses, relics, events, buffs, debuffs, rules, encounters, acts, characters. Deterministic, composable, permanent. A fact never needs revision, only extension.
- **[[heuristics]]** — Strategy for playing the game. Combat execution, card evaluation, map routing, per-entity guidance, proven archetypes. Provisional, evidence-grounded, context-dependent. These improve and get replaced over time.
- **[[goals]]** — Agent operating modes. Win, Explore, Audit, Curate, Develop. Each goal defines what to read, what to do, and what to output. 6 goal files.

Supporting infrastructure:
- **[[interface]]** — How agents interact with the game (commands, relay, stream overlay)
- **[[pipeline]]** — How agents cycle: Win → Audit → Curate → Explore → Win
- **[[site]]** — Public website at claudeslaysthespire.org, auto-generated from the book

## Structure

```
ontology/sts1/           game facts
heuristics/sts1/         game strategy + 7 topic files
goals/sts1/              6 goal files
interface/sts1/          2 files (tools, stream)
```

## Key Properties

- **Ontology/heuristics split matters.** Facts and strategy are kept separate so facts can be composed without strategic contamination. Ontology stores the two atomic facts ("Vulnerable = 1.5x" and "Bash applies Vulnerable") separately; a *heuristic* composes them into "Bash enables 1.5x damage on next hit" when a decision needs it — that derived consequence is never added to ontology as its own entry.
- **Heuristics are admissions of reasoning gaps.** A heuristic exists because the model can't reliably derive the correct action from first principles in real time. As reasoning improves, some heuristics become unnecessary.
- **Evidence-grounded — evidence lives in the analyst layer.** A heuristic is grounded in observed gameplay, but the run logs, audits, and win/loss record that justify it stay in the analyst layer; the heuristic carries only confidence (conditional vs absolute language), never a run citation or "fatal" label. The game has no concept of a past run. See `evidence.md`.
- **Wiki-linked.** Entries cross-reference with `[[category/id]]` syntax. Resolution is ontology-canonical — a bare link points at the ontology fact (in the current domain) from any layer; an explicit `layer:` / `domain:` qualifier targets elsewhere.
