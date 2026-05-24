# Session Notes — 2026-05-23

## Pipeline State

**Check `data/pipeline_state.json` — that's the source of truth.**

Current: Ironclad A5, Run 223 complete. Run 224 was abandoned mid-fight (killed by orchestrator). Next agent: Win.

## Session Results (2026-05-23)

8 runs (216-223), 2 audits, 2 curations, 1 victory.

| Run | Floor | Outcome | Notes |
|-----|-------|---------|-------|
| 216 | F14 | Sentries | Double-end bug |
| 217 | F33 | The Collector | Sozu + no healing |
| 218 | F22 | Centurion | Thunderclap/Vulnerable confusion |
| **219** | **F51** | **WIN** | Corruption+FNP+Reaper, beat Awakened One |
| 220 | F6 | Early death | |
| 221 | F50 | Awakened One | Died by 1 HP (Void drained 1E) |
| 222 | F10 | Lagavulin | Back-to-back elites, no rest |
| 223 | F21 | Spheric Guardian | HP spiral Act 2 |

## Key Playbook Changes This Session

- Thunderclap Vulnerable vs Weak fix in combat.md
- Potion timing trigger rule in combat.md
- Sozu risk assessment in drafting.md
- Elite Route Safety Rule in map.md
- New heuristics: Void, Brimstone, Transient
- Directive 7 closed, Directive 9 (A5 Consolidation) opened
- Overlay fix: character stats show correct ascension for wins

## Tomorrow

User plans to reorganize the pipeline. Run 224 is abandoned — start fresh.

## Important Scripts

- `scripts/launch.ps1` — Launches game via ModTheSpire, auto-clicks Play, waits for relay
- `scripts/kill.ps1` — Kills game, relay, and stragglers
