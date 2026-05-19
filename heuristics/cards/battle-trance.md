# Battle Trance

Free card draw. Finds key cards faster.

**When to play:** Always. Play at start of turn before making other decisions, since the drawn cards may change the optimal plan. The only exception is if you already have a perfect hand.

**Critical sequencing:** Do NOT batch `end` in the same turn() call as Battle Trance. The drawn cards need to be evaluated and played before ending the turn. Play Battle Trance first, read the new game state, THEN plan the rest of the turn.

**Decision points:** Against Gremlin Nob, Battle Trance is a Skill and triggers Enrage -- still worth playing on free turns but avoid during attack turns.

**Downside:** You cannot draw additional cards the turn you play Battle Trance (locks out further draw effects like Pommel Strike draw, Shrug It Off draw).

**Upgrade priority:** Moderate. Draw 4 instead of 3.

**Synergies:** Demon Form (finding it turns 1-2 instead of turn 5 is game-changing), any combo deck (more draw = more likely to find combo pieces).
