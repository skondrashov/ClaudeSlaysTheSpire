# Human Advice Log

Historical record of knowledge explicitly injected into the system by a human player. This file is NOT read by the pipeline — it exists purely for provenance tracking. Everything here has been incorporated into the player system through heuristics.md and subsequent strategist reworks.

---

## 2026-05-09 — Session 1: The Reasoning Rework

**Context:** 130+ runs, 0 wins, floor average regressing from 25-26 to 23.1. The self-learning loop (analyst/strategist) had stalled. The strategist identified arithmetic errors as the bottleneck, but the human identified a deeper issue: the player's fundamental reasoning model was wrong.

**Human's key insight:** "One of the most consistent mistakes is thinking of fights with low health as different from fights with high health. It doesn't actually make any sense to take more or less damage in either scenario — health is a resource that carries through the whole act."

### Heuristics provided:

**1. HP is an act-level resource (not per-fight)**
- "The only time you can spend it shamelessly is if you're in a boss fight"
- "You can also afford to take 6 damage if you're at full health because of burning blood"
- "Or 25 damage before a boss cause of pantograph if you have it"

**2. Full block is the default combat algorithm**
- "The basic combat strategy is really as simple as 'full block if you can' a lot of the time"
- "There's some exceptions like cultists because they scale so aggressively"
- "You eventually have to make tradeoffs and let 1 or 2 hp through, but not in A0"

**3. Full act pathing before the first fight**
- "You're supposed to know how many elites, shops, and campfires you're hitting before you select the first fight in every act. We've simply never done that"

**4. Act 1 card evaluation is a tier list**
- "You nearly always have the same deck when you start a run, so a memorized tier list is just really good in the first act"
- "That tier list generally looks like 'take attacks so you don't die to gremlin nob'"
- "They're not always identical because of neow but yes" (re: starting deck)

**5. Draft for known encounters**
- "You can beat the slime boss for free if you just take any cards that say 'when you draw a status card' on them"
- "Knowing what fights are guaranteed to happen and picking cards and relics accordingly"
- "It's a very deep set of rules and you don't need any of them in a0 but it's important to understand that category of heuristic"

## 2026-05-12 — Session 2: Full Block Refinement

**Human's addition to full block:**
- "Killing something that's attacking is always something you look into. So there's alternatives."
- "In general the pipeline is not good at considering alternatives"
- "It's basically a template you would fill out to determine the paths toward full block, and you'd obviously prefer to kill something and then full block if you can"

**Human's decision to prioritize stream quality:**
- "I kind of want to start using these heuristics so that the stream looks more impressive"
- "Initially it's more important to have a bot that plays well to impress people rather than a bot that slowly learns"
- "If anything we'll scale back later and see if we can't deduce the heuristics from first principles in a later run"
