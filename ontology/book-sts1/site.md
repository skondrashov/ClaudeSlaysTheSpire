# Website

Public site at claudeslaysthespire.org. Auto-generated from the book's markdown files.

## Build

`site/build.py` — Zero-dependency Python static site generator. Reads from `ontology/`, `heuristics/`, `goals/`, and `games/sts1/data/run_stats.json`. Outputs to `site/out/`.

Resolves wiki-links to HTML links. Generates category index pages, individual entry pages, and a changelog from git history.

## Deploy

GitHub Actions workflow triggers on push to `main` when `ontology/`, `heuristics/`, `goals/`, `site/`, `agents/`, or `games/sts1/data/run_stats.json` change. Builds with Python 3.12, deploys to GitHub Pages.

## Pages

- **Home** — Twitch embed, live stats (runs, wins, entry counts), character journey, knowledge overview
- **Ontology** — Browsable index of all factual entries
- **Heuristics** — Browsable index of all strategic entries
- **Knowledge System** — How the system works (from `site/knowledge-system.md`)
- **Philosophy** — Project philosophy (from `site/philosophy.md`)
- **Changelog** — Git-based changelog with diffs for commits touching ontology/heuristics/agents

## Stats

Live counts (pages, runs, wins, entry totals) are computed by the build and shown on the site's Home page — not tracked here, to avoid drift.
