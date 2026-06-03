# Explore

Play Slay the Spire to TEST SOMETHING SPECIFIC. You are not trying to maximize win probability — you are trying to generate evidence about a hypothesis. Wins are a bonus, not the objective.

## Knowledge Entry Points

Read these at the start of the session:

**Ontology:**
- `ontology/sts1/game.md` — Game domain: cards, enemies, bosses, relics, events, rules

**Interface:**
- `interface/sts1/tools.md` — Setup, commands, how to interact with the game

**Heuristics:**
- [[layer:heuristics, explore]] — Experiment design, hypothesis evaluation, confounder tracking (read what exists)
- [[archetypes]] — Known archetypes (your experiments often test beyond these)
- Game heuristics ([[combat]], per-entity files) as baseline — you need to play competently even while experimenting

## What You're Testing

Your session context includes one or more hypotheses to test. These come from:
- **Win margin notes** — things noticed during play but not pursued
- **Curate directives** — strategic experiments flagged during curation
- **Specific archetype tests** — "play 3 runs building around X"

Read the hypothesis carefully. Understand what evidence would confirm or refute it.

## Method

How to play the experiment (bias toward the hypothesis without throwing the game, win% labeling, tracking results), seed replay, and confounder tracking are in [[layer:heuristics, explore]]. Read it before starting.


## Run End

When the run ends (GAME_OVER screen), proceed through it and STOP. Report:
- Victory or defeat, floor reached
- **Experiment summary:** What was tested, what evidence was generated, verdict (confirmed / refuted / needs more data)
- Confounders that limit the conclusion
- Suggested follow-up experiments
- **Next goal recommendation** — read [[layer:goals, next]] and recommend which goal to pursue next (Win, Explore, Audit, or Curate) and why
