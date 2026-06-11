# Win

Play Slay the Spire. Win by defeating the Act 3 boss. Make one decision at a time. Every action requires explicit reasoning.

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

Post reasoning to the stream overlay with `think()` so viewers can follow your decisions.

## How to Play

Use the current best knowledge. Read heuristic files for enemies, cards, bosses as you encounter them. Follow the guidance unless the current situation clearly warrants deviation — and if you deviate, say why.

**This is the casual Win goal — play to win, but with room to learn.** You are not racing, so spend some of your budget on the learning artifact: label a win% as you go — forward, blind to how the run ends — at least at every meaningful decision, ideally at every state.

```
WIN%: [estimate] ([+/-] from last)
WHY: [what moved it]
```

That live trail is what lets an Audit measure calibration — where your in-the-moment beliefs were wrong — not just regret. When you instead want a no-overhead, all-tokens-on-the-game attempt (a clean benchmark of best play), use [[layer:goals, tournament]], which drops the labeling entirely.

**Anchor the label, don't inherit it.** Derive the baseline from the situation — this ascension level, this character's actual record at it — not from an optimistic constant carried over from easier runs. And re-derive the number at act entries and boss entries (HP minus the booked costs of every forced fight to the next recovery; kill-turns × expected incoming for a boss) instead of carrying the previous label forward. A label that does not move when its inputs moved is not an estimate — it is the previous label.

**Do NOT force a single archetype.** The game offers cards and relics — your job is to recognize which archetype the game is pushing you toward and build into it. Strength scaling, exhaust engines, Barricade+Body Slam, Corruption+FNP, defensive attrition — all are viable. Evaluate what you're offered, not what you wish you were offered.

## Margin Notes

Roughly half the time, you'll notice something interesting during play — a card combo that could be powerful, a relic interaction worth testing, an archetype you're not pursuing but can see the outline of. When this happens, drop a margin note in your `think()` output:

```
MARGIN NOTE: [what you noticed, why it's interesting, what you'd want to test]
```

Do NOT divert your gameplay to explore it. Play to win. The note is for a future Explore session to pick up.

Examples:
- "MARGIN NOTE: Runic Pyramid + Well-Laid Plans showed up together. The hand retention could enable massive burst turns — worth testing as a build-around."
- "MARGIN NOTE: I have Corruption but no FNP. Still won this fight easily because Corruption alone removed 6E of Skill costs. Corruption without FNP might be underrated — worth exploring."
- "MARGIN NOTE: Snecko Eye + expensive cards (Bludgeon, Immolate) seems incredibly strong. 25% chance of 0-cost Bludgeon is 32 free damage. Snecko Eye drafting heuristic should weight expensive cards higher."
- "MARGIN NOTE: This seed offered Corruption F3, FNP F7, Dead Branch F12 but I went Strength. An Explore session should replay this seed building exhaust — it looked like the game was pushing that archetype hard."

Margin notes can suggest **seed replays** — when you can see the game was offering an archetype you didn't pursue, note the seed for an Explore session to replay with a different strategy. Seeds are recorded automatically in the run log.

## Run End

When the run ends (GAME_OVER screen), proceed through it and STOP. Report:
- Victory or defeat, floor reached, HP at death/victory
- What went well, what went wrong
- Knowledge gaps encountered
- Any margin notes from the run (collected)
- **Next goal recommendation** — read [[layer:goals, next]] and recommend which goal to pursue next (Win, Explore, Audit, or Curate) and why
