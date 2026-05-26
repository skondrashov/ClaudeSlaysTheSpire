# Website

Public site at claudeslaysthespire.org. Auto-generated from the book's markdown files.

## Build

`site/build.py` — Zero-dependency Python static site generator. Reads from `ontology/sts1/`, `heuristics/sts1/`, and `data/run_stats.json`. Outputs to `site/out/`.

Resolves wiki-links to HTML links. Generates category index pages, individual entry pages, and a changelog from git history.

## Deploy

GitHub Actions workflow triggers on push to `main` when `ontology/`, `heuristics/`, `site/`, `agents/`, or `data/run_stats.json` change. Builds with Python 3.12, deploys to GitHub Pages.

## Pages

- **Home** — Twitch embed, live stats (runs, wins, entry counts), character journey, knowledge overview
- **Ontology** — Browsable index of all factual entries
- **Heuristics** — Browsable index of all strategic entries
- **Knowledge System** — How the system works (from `site/knowledge-system.md`)
- **Philosophy** — Project philosophy (from `site/philosophy.md`)
- **Changelog** — Git-based changelog with diffs for commits touching ontology/heuristics/agents

## Stats (as of run 223)

- 1,145 generated pages
- 223 runs, 10 wins
- 767 ontology entries, 349 heuristics entries
