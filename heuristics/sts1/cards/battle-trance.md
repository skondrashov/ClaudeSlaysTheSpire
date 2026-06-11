# Battle Trance

Free card draw. Finds key cards faster.

**When to play:** Always. Play at start of turn before making other decisions, since the drawn cards may change the optimal plan. The only exception is if you already have a perfect hand.

**Critical sequencing:** Do NOT batch `end` in the same turn() call as Battle Trance. The drawn cards need to be evaluated and played before ending the turn. Play Battle Trance first, read the new game state, THEN plan the rest of the turn.

**Decision points:** Against [[enemies/Gremlin Nob]], Battle Trance is a Skill and triggers [[buffs/Enrage]] -- still worth playing on free turns but avoid during attack turns.

**Downside:** You cannot draw additional cards the turn you play Battle Trance — No Draw kills EVERY later draw effect this turn: [[cards/Pommel Strike]] digs find nothing, [[cards/Shrug It Off]]'s draw is gone, and a [[potions/Snecko Oil]] drunk after it is wasted whole. Sequence any draw effect you intend to use BEFORE Battle Trance, or drop it from the turn — never play a card this turn whose value is the draw.

**Upgrade priority:** Moderate. Draw 4 instead of 3.

**Synergies:** [[cards/Demon Form]] (finding it turns 1-2 instead of turn 5 is game-changing), any combo deck (more draw = more likely to find combo pieces).
