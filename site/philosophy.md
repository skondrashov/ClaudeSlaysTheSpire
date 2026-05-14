# Philosophy

## How Humans Actually Learn

The default assumption in AI game-playing is self-play: let the model play thousands of games, learn from wins and losses, converge on good strategy. Self-play works, and this project uses it — but it's not the only way humans learn, and it's not even the primary way.

When a human picks up Slay the Spire for the first time, they don't play 10,000 runs in silence. They read a guide. They watch a streamer. They ask a friend "what does this relic do?" They get stomped by a boss, look up the mechanic, and come back with a plan. They develop *intuitions* from a handful of experiences, not *statistics* from a mountain of data.

Self-play produces competence through volume. Human learning produces competence through *understanding* — and understanding transfers. A human who deeply learns one deckbuilder will be decent at a second one on day one. A self-play agent trained on one game knows nothing about the next.

This project is an attempt to isolate the strategies humans use to learn, implement them for LLMs alongside self-play, and see if the resulting knowledge transfers. We've identified several learning strategies that self-play alone doesn't naturally replicate:

- **Guided instruction.** Humans read guides, watch tutorials, and absorb distilled wisdom from experts. This project uses human coaching — explicit advice about mechanics, priorities, and common mistakes — alongside self-play.
- **Structured review.** After a loss, humans don't just "try again." They analyze *what specifically went wrong*, update their mental model, and change their approach. Our analyst agent does exactly this: reads the run log, identifies mistakes, and updates the playbook with corrections.
- **Conceptual frameworks.** Humans build abstract models — "this is a scaling fight," "I need to kill the high-damage enemy first," "this boss punishes X so avoid X." These frameworks transfer across encounters. Our playbook entries include decision prompts and strategic frameworks, not just raw data.
- **Deliberate practice.** Humans focus on weaknesses. They don't just play — they practice specific skills. A human who keeps dying to Act 2 elites will specifically study those fights.
- **Social learning.** Humans learn from each other — from streams, forums, tier lists, and discussion. The human coaching component of this project simulates this channel.

## The Playbook as Transferable Knowledge

The playbook isn't just a strategy guide for Slay the Spire. It's an experiment in knowledge representation. Each entry contains:

- **Mechanics** — what something does (objective facts)
- **Strategy** — how to use it well (learned wisdom)
- **Decision prompts** — questions to ask yourself when encountering this thing

The hypothesis is that this format — mechanics + strategy + decision prompts — is a transferable structure. A Balatro playbook could use the same format. An entirely different domain could use the same format. The *content* changes, but the *structure of how you organize and retrieve knowledge* stays the same.

## The Grand Experiment

The first phase of this project is to push through Slay the Spire using every learning strategy available: guides, coaching, structured analysis, deliberate practice. Build up a comprehensive playbook. Win at high ascension levels.

The second phase is the interesting one: take the *learning strategies* we've refined — not the Slay the Spire knowledge, but the meta-strategies for how an LLM acquires and applies game knowledge — and apply them to a new game with a blank playbook. Balatro is the obvious candidate (another card roguelike), but the real question is whether the strategies extend further.

Can the same analyst/player/strategist loop that learns Slay the Spire also learn a fundamentally different kind of game? Can the playbook format that works for card evaluations also work for, say, puzzle-solving heuristics? These are open questions, and this project exists to answer them.

## Related Projects

We're not the only ones exploring this space. Several projects tackle LLM game-playing with a focus on learning and knowledge accumulation:

- **Gemini Plays Pokemon** (Google DeepMind, 2025) — Gemini 2.5 Pro plays Pokemon Red with specialized sub-agents and an XML map model. Their most interesting finding: *larger context windows actually degraded performance*. With 100k+ tokens of history, the model repeated past actions instead of synthesizing new plans. Context control design mattered more than raw model capability. Walkthrough knowledge from training data was a double-edged sword — it helped with strategy but caused version confusion (Fire Red items vs. original Blue). Completed a fully autonomous run in ~406 hours.

- **Claude Plays Pokemon** (Anthropic, 2025) — Claude plays Pokemon Red with a self-managed persistent knowledge base the model can add to, edit, and reference across thousands of actions. The prompt explicitly tells Claude to trust only screenshots and its own knowledge base, not training data. This is the closest analog to our playbook system — the model curates what it remembers. Became a valuable internal eval at Anthropic because unlike MMLU-style benchmarks, it tests long-horizon reasoning, adaptation, and information accumulation. Performance leaped between model versions — 3.0 Sonnet couldn't leave the first room; 3.7 Sonnet beat three gym leaders.

- **Voyager** (NVIDIA / MineDojo, 2023) — An LLM agent for Minecraft that builds an ever-growing skill library of executable code. Skills compound across sessions — true lifelong learning. The skill library is the clearest example of persistent, accumulating knowledge that's reusable and transferable. Their three components (automatic curriculum, skill library, iterative self-verification) map surprisingly well onto our player/analyst/strategist loop.

- **ExpeL** (UC Berkeley, 2023) — Contrasts successful and failed trajectories, extracts "rules of thumb," and stores them as reusable heuristics. This is the closest to human-style post-game reflection — distilling experience into transferable strategic principles. Very similar in spirit to our analyst agent's post-run reviews.

- **LPLH — Learning to Play Like Humans** (ACL 2025) — Explicitly models how human players learn interactive fiction, drawing on cognitive science principles: structured map building, action learning, and feedback-driven experience analysis. The name says it all — they're asking the same question we are.

The common thread: LLMs benefit enormously from structured, persistent knowledge that accumulates over time. Pure in-context reasoning hits a ceiling. The interesting question — the one all these projects are circling — is *how* to structure that knowledge so it transfers across games, across domains, and across model versions.

## What We Want to Learn

By the end of this project, we want to answer:

1. **Which human learning strategies are most effective for LLMs?** Is coaching more valuable than self-play? How much does structured review matter compared to raw experience?
2. **What knowledge representation transfers across domains?** Does the playbook format work for any game, or is it specific to card games?
3. **Can meta-learning strategies be distilled and reused?** If we figure out the right analyst/player/strategist loop for one game, does the same loop work for a second game with zero game-specific tuning?

These aren't rhetorical questions. We're running the experiments to find out.
