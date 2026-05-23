# Session Notes — 2026-05-23

## Pipeline State

**Check `data/pipeline_state.json` — that's the source of truth.**

Current state: Run 215 was the first Watcher win. Multiple Win agents have run since the last Audit (run 190). The pipeline is overdue for an Audit and a Curate.

## What To Do Next

Read `data/pipeline_state.json`. Follow the `next_recommended` field. Don't default to Win.

## Important Scripts

- `scripts/launch.ps1` — Launches game via ModTheSpire, auto-clicks Play, waits for relay
- `scripts/kill.ps1` — Kills game, relay, and stragglers

## Watcher Stats

- 1 win in ~33 runs (runs 128-132, 188-215)
- First win: Run 215 (Snecko Eye + Necronomicon + Deva Form)
- Best floor: 51 (run 215, victory)
