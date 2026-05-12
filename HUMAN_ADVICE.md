# Human Advice Log

Historical record of knowledge explicitly injected into the system by a human player. This file is NOT read by the pipeline — it exists purely for provenance tracking. Everything here has been incorporated into the player system through player.md and strategy.md.

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

## 2026-05-12 — Session 3: Hard Rules Abolished

**Context:** The player had accumulated 9 "Hard Rules" — NEVER-do prohibitions added after specific deaths. The human identified this as a fundamentally wrong approach for games.

**Human's key insight:** "Hard rules in general just aren't how games work. If the player doesn't understand how to use something it's something they need to explore, not just write a rule about with like one or two runs of data."

### Feedback on each hard rule:

**1. "NEVER TAKE RUNIC DOME"**
- "It's not like runic dome is something the developers put in to trick the player."
- "Realistically, what it means is we can't use runic dome until we've memorized all of the attack patterns in the game."
- Human says this guidance belongs under the Runic Dome playbook entry, not as a blanket prohibition.

**2. "ALWAYS USE CARD NAMES"**
- "It's not a gameplay rule, it's how to interact with the game, and ideally the player doesn't have to worry about it because the system makes it easy."
- Infrastructure issue, not gameplay. The system (cmd.py) already handles name→index resolution transparently.

**3. "UPGRADE AT EVERY REST SITE where HP is above threshold"**
- "Why is that a rule? Obviously you upgrade at a rest site if you don't need to rest. There's no 'HP threshold', everything is situational in games."

**4. "NEVER PLAY unupgraded True Grit with key cards"**
- "Kind of true but... never? Everything is situational."

**5. "USE ALL POTIONS below 40% HP"**
- "The only rule I kinda like, though again optimal potion use is much more complicated than that, and 40% is an arbitrary threshold."

**6. "NEVER PLAY BRUTALITY in long fights"**
- "Useless, how do you know if the fight is long?"

**7. "NEVER EXHAUST Spot Weakness/Reaper"**
- "Doesn't make sense on a lot of levels."

**8. "NEVER PLAY 3-cost Power turn 1 when attacked"**
- "Kind of reasonable but it belongs to the specific powers in question, and also again 'never' is stupid."

**9. "NEVER PLAY Corruption vs Guardian without Dead Branch/FNP"**
- "Specific to the point of being useless even aside from saying 'never'. Obviously you sometimes want to play corruption and sometimes you don't, and what does the guardian have to do with anything?"

### Resolution:
Hard Rules section removed from player.md entirely. Relevant guidance distributed as soft context to individual card/relic playbook entries (runic-dome.md, corruption.md, true-grit.md, brutality.md, etc.). Card name usage retained in the "Card Names and Enemy Targeting" section as infrastructure guidance, not a gameplay rule.
