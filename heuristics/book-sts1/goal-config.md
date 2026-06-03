# Goal Configuration — STS1

How the Praxis goals are instantiated for Slay the Spire.

## Goals

| Goal | Goal file | Purpose |
|------|-----------|---------|
| Win | `goals/sts1/win.md` | Play to win |
| Explore | `goals/sts1/explore.md` | Test hypotheses |
| Audit | `goals/sts1/audit.md` | Review execution quality |
| Curate | `goals/sts1/curate.md` | Evaluate strategic health |
| Develop | `goals/sts1/develop.md` | Improve interface layer |

Develop is STS1-specific — it handles the interface layer (CommunicationMod relay, stream overlay, cmd.py). This goal exists because STS1 has a custom technical interface that needs ongoing maintenance.

## Cycling Cadence

- **Win** runs by default
- **Audit** every ~3 runs (checks execution quality)
- **Curate** every ~10 runs (checks strategic health)
- **Explore** when Curate writes directives (tests hypotheses)
- **Develop** on demand (when interface issues are flagged)

Decision logic in `goals/sts1/next.md`.

## What Each Goal Loads

All goals read `ontology/sts1/game.md` as the domain entry point. Then:

- **Win** loads game heuristics (combat, drafting, map, archetypes, per-entity)
- **Explore** loads exploration heuristics + game heuristics as baseline
- **Audit** loads audit heuristics + game heuristics as reference standard
- **Curate** loads the full heuristic tree (it's evaluating all of it)
- **Develop** loads interface docs + development heuristics

## What Each Goal Writes

- **Win** → run logs, margin notes (observations for Explore)
- **Explore** → run logs, experiment results
- **Audit** → audit reports, curation flags
- **Curate** → exploration directives, playbook edits (conservative)
- **Develop** → code changes, interface docs

## Margin Notes

Win's mechanism for communicating interesting observations to a future Explore session without diverting gameplay. Formatted as `MARGIN NOTE: [observation]` in think() output. Not every run produces margin notes — roughly half the time something interesting surfaces.

## Seed Replay

Explore's most powerful tool. Replaying a Win session's seed with a different strategy eliminates card/enemy variance as a confounder. If Win died on seed X building Strength and Explore wins on seed X building Exhaust, that's strong evidence the game was offering Exhaust.
