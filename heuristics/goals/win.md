# Goal: Win

Play Slay the Spire. Win by defeating the Act 3 boss. Make one decision at a time. Every action requires explicit reasoning.

## Knowledge Entry Points

Read these at the start of the session:

**Ontology:**
- `ontology/sts1/game.md` — Game domain: cards, enemies, bosses, relics, events, rules, interface

**Heuristics:**
- `heuristics/combat.md` — Combat execution, the full block algorithm
- `heuristics/drafting.md` — Card evaluation, deck building
- `heuristics/map.md` — Map routing, elite targeting
- `heuristics/archetypes.md` — Proven winning deck formulas (read at run start — do NOT force a single archetype)
- Per-entity heuristics discovered during play via `heuristics/<category>/<name>.md`

## Setup

```python
import sys
sys.path.insert(0, r"C:\Users\tkond\projects\autoplay\games\sts1")
from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, think, deck, start
```

Call `state()` to see the game. See `ontology/sts1/interface/tools.md` for the full tool reference.

Post reasoning to the stream overlay with `think()` so viewers can follow your decisions.

## How to Play

Use the current best knowledge. Read heuristic files for enemies, cards, bosses as you encounter them. Follow the guidance unless the current situation clearly warrants deviation — and if you deviate, say why.

**Do NOT force a single archetype.** The game offers cards and relics — your job is to recognize which archetype the game is pushing you toward and build into it. Strength scaling, exhaust engines, Barricade+Body Slam, Corruption+FNP, defensive attrition — all are viable. Evaluate what you're offered, not what you wish you were offered.

## Margin Notes

Roughly half the time, you'll notice something interesting during play — a card combo that could be powerful, a relic interaction worth testing, an archetype you're not pursuing but can see the outline of. When this happens, drop a margin note in your `think()` output:

```
MARGIN NOTE: [what you noticed, why it's interesting, what you'd want to test]
```

Do NOT divert your gameplay to explore it. Play to win. The note is for the Explore agent to pick up later.

Examples:
- "MARGIN NOTE: Runic Pyramid + Well-Laid Plans showed up together. The hand retention could enable massive burst turns — worth testing as a build-around."
- "MARGIN NOTE: I have Corruption but no FNP. Still won this fight easily because Corruption alone removed 6E of Skill costs. Corruption without FNP might be underrated — worth exploring."
- "MARGIN NOTE: Snecko Eye + expensive cards (Bludgeon, Immolate) seems incredibly strong. 25% chance of 0-cost Bludgeon is 32 free damage. Snecko Eye drafting heuristic should weight expensive cards higher."
- "MARGIN NOTE: This seed offered Corruption F3, FNP F7, Dead Branch F12 but I went Strength. Explore should replay this seed building exhaust — it looked like the game was pushing that archetype hard."

Margin notes can suggest **seed replays** — when you can see the game was offering an archetype you didn't pursue, note the seed for the Explore agent to replay with a different strategy. Seeds are recorded automatically in the run log.

## Run End

When the run ends (GAME_OVER screen), proceed through it and STOP. Report:
- Victory or defeat, floor reached, HP at death/victory
- What went well, what went wrong
- Knowledge gaps encountered
- Any margin notes from the run (collected)
