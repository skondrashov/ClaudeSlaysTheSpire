# Session Notes — 2026-05-21

## Pipeline State

**Last committed run:** 190 (Watcher, F16, Guardian)
**Git:** main branch, all pushed. Clean working tree except ORCHESTRATION.md edit (not yet committed).

## What Got Done This Session

1. **Run 189** — committed & pushed (Watcher Explore, F20, Blasphemy self-kill)
2. **Run 190** — played by agent, committed & pushed (Watcher Explore, F16, card-index shift caused Wrath entry vs Guardian)
3. **Directive 3 COMPLETE** — 3/3 Watcher Explore runs done. 0 wins, best F20. Stance dance shows promise but all deaths were execution errors.
4. **First Audit ever** — Run 190 audited. Key finding: `turn()` card-index shifting is a systemic execution risk. Written to `analyst/audits/run_190.md`.
5. **Curate session** — Synthesized Directive 3 results:
   - Directive 3 marked COMPLETE in `analyst/directives.md`
   - **Directive 4** created: 3 Watcher Win runs with execution cleanup rules (card names in turn(), no Blasphemy without confirmed arithmetic)
   - **Directive 5** created: Guardian matchup data collection for Watcher
   - Combat heuristic rule 6 added: USE CARD NAMES IN turn() BATCHES
   - Guardian boss heuristic: added Watcher matchup section
   - Watcher character heuristic: added Execution Risks + Current Status sections
   - Archetypes: added Watcher stance dance as unproven-but-promising
6. **play.py expanded** — Agent added CLI wrappers for play, end, choose, proceed, skip, think, deck, potion_use, potion_discard

## What To Do Next

**Goal:** Win (Watcher) — Directive 4, run 1 of 3.

Steps:
1. Kill any stale processes: `.\scripts\kill.ps1`
2. Launch game: `.\scripts\launch.ps1` (waits for relay on :19284)
3. Clear player lock: `rm -f data/player.lock`
4. Commit the ORCHESTRATION.md edit (adds launch script docs)
5. Spawn Watcher Win agent per Directive 4

**Session token:** `8f81114d-3d60-4d45-9661-5487631f0705`

**Key context for the Win agent:**
- Use card NAMES in turn() batches, never indices (combat rule 6)
- Never play Blasphemy without confirmed kill arithmetic via think()
- Post fight strategy via think() before every elite/boss
- Stance dance engine: Calm→Wrath cycling, Eruption+ is #1 upgrade
- At least 2 Wrath exit sources needed for boss fights
- Watcher heuristic has Execution Risks section — read it

## Directives Status

| # | Topic | Status | Notes |
|---|-------|--------|-------|
| 1 | Corruption+FNP without Strength | Open | 0/3 runs, not started |
| 2 | Corruption+FNP vs Spheric Guardian | Open | Data collection during Dir 1 |
| 3 | Watcher Archetype Development | **COMPLETE** | 0/3 wins, execution errors |
| 4 | Watcher Execution Cleanup | Open | 0/3 Win runs |
| 5 | Guardian Matchup for Watcher | Open | Data collection during Dir 4 |

## Important Scripts

- `scripts/launch.ps1` — Launches game via ModTheSpire, auto-clicks Play, waits for relay
- `scripts/kill.ps1` — Kills game, relay, and stragglers
- `scripts/configure-commmod.ps1` — Sets CommunicationMod config
- `scripts/install-commmod.ps1` — Installs CommunicationMod

## Relay Architecture Note

CommunicationMod launches relay.py as a child process. relay.py bridges stdin/stdout to TCP on port 19284. If relay.py dies, CommunicationMod does NOT restart it — the game must be fully restarted. Do NOT try to start relay.py manually — it needs CommunicationMod's stdin/stdout pipe.

## Watcher Stats

- 0 wins in 8 runs (128-132, 188-190)
- Best floor: 33 (run 131)
- Stance dance is the only engine tested
- Engine works mechanically — recent deaths were all execution errors
