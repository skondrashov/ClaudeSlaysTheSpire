# Audit a Run

Review a completed run log and evaluate the quality of each decision. You are checking EXECUTION, not STRATEGY — did the player do the right thing given what they knew and what was on screen? Don't second-guess the strategic framework. Flag errors for a Curate session to address at the playbook level.

## Knowledge Entry Points

Read these at the start of the session:

**Ontology:**
- `ontology/sts1/game.md` — Game domain (you need to understand what cards/enemies/relics do to evaluate decisions)

**Heuristics:**
- [[layer:heuristics, audit]] — How to evaluate decisions, common error patterns, what "correct" looks like (read what exists)
- Game heuristics ([[cards/]], [[enemies/]], etc.) as reference standard — read per-entity files to check whether the player followed guidance

## Input

Run log at `analyst/runs/run_NNN.json` — read it first. Contains every decision (command + reasoning) and the resulting game state after each action.

## Method

Evaluate the EXECUTION quality of every decision — the win%/regret/calibration lens, the combat and non-combat checklists, and the knowledge-gap vs retrieval-miss diagnosis are in [[layer:heuristics, audit]]. Read it before starting.


## Output

For each fight and each major non-combat decision, write a brief assessment:

```
FLOOR [N] — [fight/event/shop/rest]
WIN%: [forward estimate]   REGRET: [win% lost vs best available, or ~0]
ASSESSMENT: [correct / error / debatable]
DETAIL: [what happened, what should have happened if error]
```

At the end, summarize:
- **Steepest regret:** the 1–3 decisions that cost the most win probability — the better line, and where they sit in the run (NOT necessarily the death fight)
- **Calibration gaps** (if the run has live labels): where the player's live win% diverged most from your honest forward estimate → Curator flags
- **Error count:** N arithmetic errors, N intent-reading errors, N heuristic violations, N potion mistakes
- **Patterns:** Recurring error types across the run
- **Flags for Curator:** Issues that suggest the playbook needs updating (not the player's execution). Tag each as a **knowledge gap** (the fact was missing — write it) or a **retrieval miss** (the fact existed but wasn't loaded — fix the awareness manifest, `awareness/sts1/`)

Write output to `analyst/audits/run_NNN.md`.

**Next goal recommendation** — read [[layer:goals, next]] and recommend which goal to pursue next (Win, Explore, Audit, or Curate) and why. Include this at the end of your audit report.
