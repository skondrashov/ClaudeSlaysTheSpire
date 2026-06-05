# Explore — Heuristics

How to run a controlled experiment while playing. The method behind the [[layer:goals, explore]] goal.

## How to Play

**Bias toward the experiment.** When card rewards, shop purchases, relic choices, or pathing decisions come up, lean toward options that serve the hypothesis — even if the "safe" or "known-good" choice is different. The whole point is to explore the road less traveled.

**But don't throw the game.** Exploration doesn't mean ignoring lethal damage or refusing to block. Play competently within the experiment's constraints. A run that dies on Floor 6 because you refused to take block cards generates no useful data about the hypothesis.

**Label a win% at EVERY state.** At every decision point — each combat turn, card reward, path choice, shop, rest, event — post an honest estimate of the run's win probability, judged FORWARD: only what is knowable right now, with no idea how the run ends.

```
WIN%: [estimate] ([+/-] from last)
WHY: [what moved it]
```

Label every state, but spend your thinking budget unevenly — a snap number on a trivial turn, real deliberation at the swingy ones. At pivotal states, also estimate the win% of the best ALTERNATIVE action you are passing up; the gap between what you did and that best option is the regret an audit will hunt for. The complete win% trajectory — not just the big moments — is what lets an audit locate where a run was actually lost.

Exploration deliberately PAYS win% for information, and labeling makes the price explicit: a drop you chose into is regret you accepted for evidence; a drop that surprises you later is a hole in your own model. Note which is which.

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

Seeds are recorded in every run log (`analyst/runs/run_NNN.json`, field `seed`). When the session context says "replay run N's seed with a different strategy," look up the seed and use it.

**Why this matters:** In a normal run, you can't tell if a strategy failed because it's bad or because the card offerings were bad. Seed replay eliminates that confounder. If a Win session died on seed X building Strength and you win on seed X building Corruption, that's strong evidence the game was offering Corruption, not Strength — and the Win strategy missed it.

**When to replay vs fresh run:**
- **Replay** when testing "could this specific run have gone differently with a different strategy?"
- **Fresh run** when testing "is archetype X generally viable?" (you want natural variance)

## Confounders

Roguelike variance is high. A single run doesn't prove anything. Note confounders honestly:
- "This run offered Corruption on Floor 2 — unusually early. The archetype might not come together this smoothly normally."
- "No Strength sources appeared despite 8 card rewards. This isn't a fair test of the non-Str archetype — it's a test of what happens when nothing works."
- Seed replays eliminate card/enemy variance but not decision variance — you still might play the alternative strategy suboptimally because you're less practiced with it.
