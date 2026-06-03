# Tournament Win

Play Slay the Spire to win, all out — the "sweaty" mode. Same objective as [[layer:goals, win]] (defeat the Act 3 boss), same strategy, same knowledge. The difference is where your budget goes: **every token serves the decision in front of you.** No win% labeling, no margin-note detours, no experiments — instrumentation competes with play, and here play wins. Use this for a clean benchmark of best effort, or when a win simply matters most.

## Knowledge Entry Points

Read these at the start of the session:

**Ontology:**
- `ontology/sts1/game.md` — Game domain: cards, enemies, bosses, relics, events, rules

**Interface:**
- `interface/sts1/tools.md` — Setup, commands, how to interact with the game
- `interface/sts1/stream.md` — Streaming overlay, viewer communication

**Heuristics:**
- [[combat]] — Combat execution, the full block algorithm
- [[drafting]] — Card evaluation, deck building
- [[map]] — Map routing, elite targeting
- [[archetypes]] — Proven winning deck formulas (read at run start — do NOT force a single archetype)
- Per-entity heuristics discovered during play via `[[<category>/<name>]]`

## All Budget on the Game

In [[layer:goals, win]] you spend some slack on learning artifacts — a live win% trail, margin notes — because casual play has room for it. Tournament does not. Whatever compute you would spend estimating win% or noting tangents, spend it instead on the move: deeper arithmetic, fuller intent reads, longer lookahead, stricter potion and map accounting.

- **Do not label win%.** It is a learning cost, and you are not here to learn — you are here to win. An Audit can reconstruct the win% trajectory retrospectively from the run log if it wants one.
- **Skip margin notes** unless one is genuinely free — do not divert attention to articulate a tangent.
- **Reason only toward the decision.** Every `think()` should be about winning the current state, not about what the run teaches.

## How to Play

Same strategy as [[layer:goals, win]]: use the current best knowledge, read per-entity heuristics as you encounter them, deviate only with stated reasons, and **do not force a single archetype** — build into what the game offers. Tournament effort means more care per decision, not a different plan.

## Run End

When the run ends (GAME_OVER screen), proceed through it and STOP. Report:
- Victory or defeat, floor reached, HP at death/victory
- What went well, what went wrong; knowledge gaps encountered
- No live win% self-report — leave win%/regret analysis to a retrospective Audit
- **Next goal recommendation** — read [[layer:goals, next]] and recommend which goal to pursue next (Win, Tournament, Explore, Audit, or Curate) and why
