# Entry Quality

What makes an entry useful vs. noise.

## Ontology Quality

A good ontology entry is:
- **Complete enough to reason from.** An agent reading just this entry should have every fact needed to reason about this entity. If they'd need to check the game to verify a number, the entry is incomplete.
- **Minimal.** No sentence that doesn't state a fact. No narrative, no history, no commentary.
- **Linked.** References to other entities use `[[category/Name]]` so agents can follow them.
- **Ascension-aware.** Where values change by ascension level, include the variants that matter (A0 for baseline, higher for current play level).

A bad ontology entry:
- States facts AND gives advice in the same file
- Is missing key mechanics (an enemy entry without the attack pattern algorithm)
- Includes hedging language ("Vulnerable probably increases damage by 50%") — ontology entries are facts, not guesses

The ideal ontology entry is boring. It reads like a wiki data page.

## Heuristic Quality

A good heuristic entry is:
- **Actionable.** The reader can make a concrete decision after reading it. "Be careful" is not actionable. "Block for full incoming damage on Turn 2, then burst damage on Turn 3 during Bellow" is.
- **Conditional.** States when the advice applies AND when it doesn't. "ALWAYS rest below 40% HP" is less useful than "ALWAYS rest below 40% HP... UNLESS the upgrade is Bash+ and boss is 3+ floors away."
- **Evidence-grounded.** Cites run numbers or specific outcomes. "Confirmed fatal in Run 217" is grounded. "This is usually bad" is not.
- **Specific.** Names cards, enemies, numbers, thresholds. "Use potions before rest sites" is vague. "Use potions on the elite before a rest site if it saves you the rest, freeing the site for an upgrade" is specific.
- **Honest about uncertainty.** Uses "I think" when evidence is thin. Marks unvalidated claims as provisional.

A bad heuristic entry:
- Is so general it could apply to anything ("play cards that are good")
- Gives advice without explaining why (agents need the reasoning to know when to deviate)
- Makes absolute claims from single runs
- Is a wall of text with no structure (bold headers, bullet points, sections)

## The Stub Question

Is a 3-line entry worth having?

For **ontology**: yes. Even a minimal card entry (cost, type, effect) is useful as an input for composition (the composed result itself is a heuristic, not an ontology entry). An agent encountering the card can look it up and get the facts. Better than nothing.

For **heuristics**: usually no. A 1-sentence heuristic ("This is good") adds no value over what the agent would conclude from the ontology facts alone. Either write a useful heuristic (when to play, synergies, warnings) or don't write one at all.

Exception: warnings. "NEVER play Fiend Fire against Thorns enemies" is 1 sentence and high value because the failure mode is non-obvious and fatal.

## Topic Files vs. Per-Entity Files

Topic files (combat.md, drafting.md, archetypes.md) are the most valuable entries in the system. They contain cross-cutting decision algorithms that no individual entity entry can capture.

**Write a topic file when:** The same reasoning pattern applies across many entities. "How to decide what to block" doesn't belong on any one enemy's entry — it belongs in combat.md.

**Write a per-entity file when:** The advice is specific to that entity and wouldn't generalize. "Gremlin Nob: play zero Skills" is Nob-specific.

**The most common quality mistake** is putting topic-level insights on per-entity entries. If you notice you're writing the same advice on multiple enemy heuristics, it belongs in a topic file instead.
