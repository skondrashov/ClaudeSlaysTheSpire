# Agent Configuration — STS1

How the four Praxis agent roles are instantiated for Slay the Spire.

## Role Mapping

| Praxis role | STS1 agent | Goal file |
|-------------|-----------|-----------|
| Performer | Win | `goals/sts1/win.md` |
| Explorer | Explore | `goals/sts1/explore.md` |
| Analyst | Audit | `goals/sts1/audit.md` |
| Curator | Curate | `goals/sts1/curate.md` |
| (additional) | Develop | `goals/sts1/develop.md` |

Develop is STS1-specific — it handles the interface layer (CommunicationMod relay, stream overlay, cmd.py). This role exists because STS1 has a custom technical interface that needs ongoing maintenance.

## Cycling Cadence

- **Win** runs by default
- **Audit** every ~3 runs (checks execution quality)
- **Curate** every ~10 runs (checks strategic health)
- **Explore** when Curate writes directives (tests hypotheses)
- **Develop** on demand (when agents flag interface issues)

Decision logic in `goals/sts1/next.md`.

## What Each Agent Reads

All agents read `ontology/sts1/game.md` as the domain entry point. Then:

- **Win** reads game heuristics (combat, drafting, map, archetypes, per-entity)
- **Explore** reads exploration heuristics + game heuristics as baseline
- **Audit** reads audit heuristics + game heuristics as reference standard
- **Curate** reads the full heuristic tree (it's evaluating all of it)
- **Develop** reads interface docs + development heuristics

## What Each Agent Writes

- **Win** → run logs, margin notes (observations for Explore)
- **Explore** → run logs, experiment results
- **Audit** → audit reports, curator flags
- **Curate** → exploration directives, playbook edits (conservative)
- **Develop** → code changes, interface docs

## Margin Notes

Win agent's mechanism for communicating interesting observations to Explore without diverting gameplay. Formatted as `MARGIN NOTE: [observation]` in think() output. Not every run produces margin notes — roughly half the time something interesting surfaces.

## Seed Replay

Explore agent's most powerful tool. Replaying a Win agent's seed with a different strategy eliminates card/enemy variance as a confounder. If Win died on seed X building Strength and Explore wins on seed X building Exhaust, that's strong evidence the game was offering Exhaust.
