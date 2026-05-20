# Goal: Review System Health

Step back and evaluate whether the knowledge system is working. Run every ~10 runs. Are we getting better? Is the knowledge serving the player? Is the architecture helping?

## Inputs

- `analyst/observations.md` — uncertain items
- `heuristics/` — all strategic guidance
- `ontology/` — all game facts
- `data/run_stats.json` — win/death/floor stats
- `analyst/runs/` — full event logs

## Questions

### 1. Are we improving?

Last 10 runs: floor reached, cause of death, deck quality.
- Trending up? Plateauing? Regressing?
- Dying to new things (exploring) or same things (not learning)?
- If plateauing: what's the bottleneck?

### 2. Is the knowledge serving the player?

- **Dead weight**: Entries the player never loads?
- **Missing coverage**: Decisions the player keeps getting wrong without heuristic guidance?
- **Signal-to-noise**: Are entries concise and actionable, or bloated?
- **Ontology quality**: Are entries formally closed? Links correct? Facts accurate?
- **Heuristic quality**: Are conclusions grounded in evidence? Contradictions between entries?

### 3. Are there patterns the analyst is missing?

- Same cause of death recurring → needs stronger heuristic
- Observations that keep reappearing → probably confirmed, promote them
- Contradictory analyst notes → one is wrong, determine which

### 4. Cleanup

- Dedup entries that say the same thing in different places
- Trim bloat from heuristic files
- Ensure ontology entries are formally closed (no strategic advice leaking in)
- Promote confirmed observations to heuristics
- Fix contradictions
- Archive stale data

## Output

1. Brief assessment (10-15 lines): what's working, what's not, what you changed
2. Heuristic edits — structural changes, rewrites, consolidations
3. Strategy.md updates if high-level principles need revision
4. Cleanup — dedup, trim, promote observations

## Principles

- **Be willing to delete.** Smaller and accurate beats comprehensive and noisy.
- **Name the bottleneck.** Every plateau has a reason. Not "play better" but "we keep entering [[acts/Act 2]] without scaling because card reward evaluation doesn't weight it."
- **Measure progress.** Concrete numbers, not vibes.
