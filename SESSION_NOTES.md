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

## Tomorrow — Fixes & Reorg

User plans to reorganize the pipeline. Run 224 is abandoned — start fresh.

### Bugs to fix
- **IB-008: Double-end command** — cmd.py should reject duplicate `end` in same turn. Add `_turn_ended` flag. (Run 216 death)
- **IB-009: Duplicate run logging** — cmd.py's GAME_OVER handler may fire twice. Add guard to `_log_run()`. (Runs 216/217 identical)

### Agent behavior issues
- **HP management drift** — Agents say "I can afford damage at 80 HP" despite combat.md explicitly forbidding this. The heuristic exists but agents don't internalize it. Options: make it more prominent in combat.md preamble, add to agent prompt template, or have agent re-read hp-management.md before fights.
- **Prompt template** — Win agent prompt is getting long with accumulated critical rules. Consider extracting to a file that gets composed into the prompt automatically.

### Pipeline improvements
- Agent sometimes plays 2 runs in one session (fixed by adding "play only ONE run" to prompt, but fragile)
- Auditors cite wrong "runs since last curate" count — they don't know about recent curations. Consider giving them pipeline_state.json.

## Important Scripts

- `scripts/launch.ps1` — Launches game via ModTheSpire, auto-clicks Play, waits for relay
- `scripts/kill.ps1` — Kills game, relay, and stragglers
