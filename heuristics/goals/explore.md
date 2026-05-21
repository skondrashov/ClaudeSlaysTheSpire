# Goal: Explore

Play Slay the Spire to TEST SOMETHING SPECIFIC. You are not trying to maximize win probability — you are trying to generate evidence about a hypothesis. Wins are a bonus, not the objective.

## Knowledge Entry Points

Read these at the start of the session:

**Ontology:**
- `ontology/sts1/game.md` — Game domain: cards, enemies, bosses, relics, events, rules, interface

**Heuristics:**
- `heuristics/exploration/` — Experiment design, hypothesis evaluation, confounder tracking (read what exists)
- `heuristics/archetypes.md` — Known archetypes (your experiments often test beyond these)
- Game heuristics (`heuristics/combat.md`, per-entity files) as baseline — you need to play competently even while experimenting

## Setup

```python
import sys
sys.path.insert(0, r"C:\Users\tkond\projects\autoplay\games\sts1")
from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, think, deck, start
```

Call `state()` to see the game. See `ontology/sts1/interface/tools.md` for the full tool reference.

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

## Seed Replay

The most powerful tool for controlled experiments. Pass a seed to `start()` to replay the exact same run — same card offerings, same enemies, same map, same relics:

```python
start("IRONCLAD", 0, seed="ABC123")
```

Seeds are recorded in every run log (`analyst/runs/run_NNN.json`, field `seed`). When the session context says "replay Run 185's seed with a different strategy," look up the seed and use it.

**Why this matters:** In a normal run, you can't tell if a strategy failed because it's bad or because the card offerings were bad. Seed replay eliminates that confounder. If Win died on seed X building Strength and you win on seed X building Corruption, that's strong evidence the game was offering Corruption, not Strength — and the Win agent's framework missed it.

**When to replay vs fresh run:**
- **Replay** when testing "could this specific run have gone differently with a different strategy?"
- **Fresh run** when testing "is archetype X generally viable?" (you want natural variance)

## Confounders

Roguelike variance is high. A single run doesn't prove anything. Note confounders honestly:
- "This run offered Corruption on Floor 2 — unusually early. The archetype might not come together this smoothly normally."
- "No Strength sources appeared despite 8 card rewards. This isn't a fair test of the non-Str archetype — it's a test of what happens when nothing works."
- Seed replays eliminate card/enemy variance but not decision variance — you still might play the alternative strategy suboptimally because you're less practiced with it.

## Run End

When the run ends (GAME_OVER screen), proceed through it and STOP. Report:
- Victory or defeat, floor reached
- **Experiment summary:** What was tested, what evidence was generated, verdict (confirmed / refuted / needs more data)
- Confounders that limit the conclusion
- Suggested follow-up experiments
- **Next goal recommendation** — read `heuristics/goals/next.md` and recommend which goal the next agent should pursue (Win, Explore, Audit, or Curate) and why
