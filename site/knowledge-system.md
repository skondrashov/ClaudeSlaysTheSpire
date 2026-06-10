# The Knowledge System

Most AI game-playing projects train on thousands of games. This one is trying something different: build a structured knowledge base that an AI agent reads, reasons over, and writes back to — the way a human would use notes, guides, and post-game analysis.

The knowledge lives in layers: **ontology** (facts about the game), **phenomena** (derived facts, generated from the ontology), **heuristics** (strategy for navigating it), and **goals** (the agent's operating modes). The two that carry most of the weight are ontology and heuristics. The agent is ephemeral — it spawns, plays, and disappears. The knowledge web is what persists and accumulates.

---

## Ontology and Heuristics

### Ontology — what the world is

Facts about the game. What exists, how it behaves, how things relate to each other. Deterministic, composable, permanent.

- "Vulnerable causes the target to take 1.5x damage from attacks."
- "The draw pile reshuffles from the discard pile when empty."
- "Gremlin Nob gains 2 Strength whenever the player plays a Skill card."

A correct ontological entry never needs revision — only extension. The aspiration is completeness: know everything about how the game works. Over a thousand entries and counting.

### Heuristics — how to navigate it

Cached reasoning. Pre-baked conclusions for situations the agent can't reliably think through from first principles in real time.

- "Don't play Skills against Gremlin Nob."
- "Kill scaling enemies before they scale."
- "Take Offering in Act 1 — the HP cost is worth the card draw."

A heuristic is an admission: the reasoning engine isn't good enough to derive this on its own every time, so here's a shortcut. Heuristics are useful, but they're provisional. As the model gets smarter, heuristics that were necessary become unnecessary and fall away.

A perfectly intelligent agent with complete ontology needs zero heuristics — it derives optimal play from first principles. Heuristics exist in the gap between what you know and what you can figure out from what you know.

### Why the split matters

Ontology composes. Knowing that Vulnerable means 1.5x damage AND that Bash applies Vulnerable lets you derive that Bash effectively deals 1.5x damage on the next hit. You don't need a separate entry for that interaction — it falls out of the facts.

Heuristics don't compose the same way. "Kill scaling enemies fast" and "prioritize blocking in Act 2" might contradict each other in a specific situation. Resolving the contradiction requires reasoning, not lookup.

Keeping them separate means the agent always knows whether it's reading a ground truth or someone's opinion. Ground truths are safe to build on. Opinions need to be evaluated.

---

## How It Works

### The linked graph

Every entry cross-references related concepts with explicit links. A card entry links to the effects it applies. An enemy entry links to the buffs it gains. An encounter entry links to the enemies that compose it.

These links serve double duty: they help readers navigate related concepts, and they give the agent a way to request related knowledge in batches. "Give me the enemy I'm fighting and everything it links to" pulls in the attack patterns, the relevant buffs and debuffs, and the mechanical interactions — all in one query.

### The agent loop

```
Agent spawns with a goal ("win this run")
    ↓
Queries the knowledge web for relevant context
    ↓
Takes one action, with explicit reasoning
    ↓
Observes the result
    ↓
Notices gaps — things it needed but didn't know
    ↓
Records gaps for later investigation
    ↓
Session ends → progress + a queue of things to learn
    ↓
Next session's goal may be: fill those gaps
```

The agent isn't playing blind, and it isn't running on pure instinct. It's reading its own accumulated knowledge before every decision — and after every session, that knowledge gets a little better.

### What's browsable here

**Ontology** — the complete factual database of the game. Every card, enemy, relic, potion, event, boss, buff, debuff, encounter, and game rule. Browse it like a wiki.

**Heuristics** — strategic guidance organized in parallel. How to fight each enemy, when to play each card, which relics to prioritize. Accumulated from gameplay and analysis. These are the opinions — they might be wrong, and they'll improve over time.

---

## The Ceiling

Decision quality is bounded by two things:

1. **Ontological completeness.** If you don't know how something works, you can't reason about it. This is fillable — observe more, test more, record more.

2. **Reasoning capacity.** Given complete ontology, can the agent derive the right action? This is the hard limit. A heuristic exists precisely when the answer is "not reliably." Better models raise this ceiling.

The system tries to be honest about which ceiling it's hitting. "I lost because I didn't know Flight halves damage" is a knowledge gap — fixable. "I lost because I couldn't figure out the optimal turn sequence even though I knew all the mechanics" is a reasoning gap — fixable only by being smarter, or by caching the conclusion as a heuristic for next time.
