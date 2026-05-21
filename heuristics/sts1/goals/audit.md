# Goal: Audit a Run

Review a completed run log and evaluate the quality of each decision. You are checking EXECUTION, not STRATEGY — did the player do the right thing given what they knew and what was on screen? Don't second-guess the strategic framework. Flag errors for the Curator to address at the playbook level.

## Knowledge Entry Points

Read these at the start of the session:

**Ontology:**
- `ontology/sts1/game.md` — Game domain (you need to understand what cards/enemies/relics do to evaluate decisions)
- `ontology/sts1/analysis/index.md` — Analysis methodology: prediction errors, attribution, observation lifecycle

**Heuristics:**
- [[audit/]] — How to evaluate decisions, common error patterns, what "correct" looks like (read what exists)
- Game heuristics ([[cards/]], [[enemies/]], etc.) as reference standard — read per-entity files to check whether the player followed guidance

## Input

Run log at `analyst/runs/run_NNN.json` — read it first. Contains every decision (command + reasoning) and the resulting game state after each action.

## What to Check

### Combat Decisions
For each fight, evaluate:
1. **Arithmetic.** Did the player calculate damage and block correctly? Common errors: forgetting Vulnerable (+50%), miscounting multi-hit, wrong Strength multiplier on Heavy Blade, not accounting for enemy block.
2. **Intent reading.** Did the player check enemy intents and plan accordingly? Missed an attacker intent = took avoidable damage.
3. **Card order.** Did draw cards come last in the sequence? Did the player play cards in an order that makes sense (buffs before attacks, block cards on defense turns)?
4. **Heuristic compliance.** Read the relevant heuristic files for each card played and enemy fought. Did the player follow the guidance? If they deviated, was it justified by the specific situation?
5. **Potion timing.** Were potions used when they mattered, or hoarded until death? Were potions used wastefully on easy fights?
6. **Lethal awareness.** On turns where the player was at risk of dying, did they recognize it and play accordingly?

### Non-Combat Decisions
1. **Card rewards.** Did the player look up card heuristics before choosing? Did the choice make sense for the deck's archetype and current needs?
2. **Map pathing.** Did the player plan a full act route? Did they follow it? Were deviations justified?
3. **Shop purchases.** Did the player prioritize correctly (card removal, key relics, key cards)?
4. **Rest sites.** Upgrade vs rest — was the choice correct given HP and upcoming threats?
5. **Events.** Did the player look up the event? Did they choose the best option?

### What You're NOT Doing
- You are NOT evaluating whether the playbook's strategy is correct. If the heuristic says "prioritize Strength" and the player followed it but died anyway, that's a Curate problem, not an Audit problem.
- You are NOT rewriting heuristics. Flag issues; don't fix them.
- You are NOT making code changes.

## Output

For each fight and each major non-combat decision, write a brief assessment:

```
FLOOR [N] — [fight/event/shop/rest]
ASSESSMENT: [correct / error / debatable]
DETAIL: [what happened, what should have happened if error]
```

At the end, summarize:
- **Error count:** N arithmetic errors, N intent-reading errors, N heuristic violations, N potion mistakes
- **Patterns:** Recurring error types across the run
- **Flags for Curator:** Issues that suggest the playbook needs updating (not the player's execution)

Write output to `analyst/audits/run_NNN.md`.

**Next goal recommendation** — read [[goals/next]] and recommend which goal the next agent should pursue (Win, Explore, Audit, or Curate) and why. Include this at the end of your audit report.
