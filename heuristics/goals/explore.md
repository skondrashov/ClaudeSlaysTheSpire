# Goal: Explore

Play Slay the Spire to TEST SOMETHING SPECIFIC. You are not trying to maximize win probability — you are trying to generate evidence about a hypothesis. Wins are a bonus, not the objective.

Start from `ontology/index.md` to understand the game.

## Setup

```python
import sys
sys.path.insert(0, r"C:\Users\tkond\projects\autoplay\games\sts1")
from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, think, deck, start
```

Call `state()` to see the game. See `ontology/interface/tools.md` for the full tool reference.

## What You're Testing

Your session context includes one or more hypotheses to test. These come from:
- **Win agent margin notes** — things the win player noticed but didn't pursue
- **Curate directives** — strategic experiments the Curator wants data on
- **Specific archetype tests** — "play 3 runs building around X"

Read the hypothesis carefully. Understand what evidence would confirm or refute it.

## How to Play

**Bias toward the experiment.** When card rewards, shop purchases, relic choices, or pathing decisions come up, lean toward options that serve the hypothesis — even if the "safe" or "known-good" choice is different. The whole point is to explore the road less traveled.

**But don't throw the game.** Exploration doesn't mean ignoring lethal damage or refusing to block. Play competently within the experiment's constraints. A run that dies on Floor 6 because you refused to take block cards generates no useful data about the hypothesis.

**Track results explicitly.** At key moments, post experiment-relevant observations with `think()`:

```
EXPERIMENT: [hypothesis label]
OBSERVATION: [what happened, what it tells us]
EVIDENCE: [confirms / refutes / inconclusive] because [reasoning]
```

## Confounders

Roguelike variance is high. A single run doesn't prove anything. Note confounders honestly:
- "This run offered Corruption on Floor 2 — unusually early. The archetype might not come together this smoothly normally."
- "No Strength sources appeared despite 8 card rewards. This isn't a fair test of the non-Str archetype — it's a test of what happens when nothing works."

## Run End

When the run ends (GAME_OVER screen), proceed through it and STOP. Report:
- Victory or defeat, floor reached
- **Experiment summary:** What was tested, what evidence was generated, verdict (confirmed / refuted / needs more data)
- Confounders that limit the conclusion
- Suggested follow-up experiments
