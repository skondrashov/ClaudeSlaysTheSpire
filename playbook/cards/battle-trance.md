# Battle Trance (0E, Skill, draw 3 cards | +: draw 4 cards)
Free card draw. Finds key cards faster.

WHEN IT'S GOOD: Always. 0-cost draw is the best possible form of card advantage. Finding Demon Form, Flame Barrier+, or Bash+ one turn earlier can be the difference between winning and losing. Play at start of turn before making other decisions, since the drawn cards may change the optimal plan.

DECISION POINTS: Play first every turn it's drawn. The only exception is if you already have a perfect hand and drawing would add nothing (rare). Against Gremlin Nob, Battle Trance is a Skill and triggers Enrage (+2 Str to Nob) -- still worth playing on free turns but avoid during attack turns.

CRITICAL SEQUENCING: Battle Trance draws cards into your hand. Do NOT batch `end` (end turn) in the same turn() call as Battle Trance. The drawn cards need to be evaluated and played before ending the turn. Play Battle Trance first, read the new game state to see what was drawn, THEN plan the rest of the turn. A wasted turn from ending before playing drawn cards is lethal in scaling fights like Gremlin Leader (where each lost turn is +3 Str to all enemies). Similarly, do not batch Battle Trance with Bloodletting or other energy-generating cards and then `end` -- the generated energy and drawn cards are useless if the turn ends before they can be spent.

DOWNSIDE: You cannot draw additional cards the turn you play Battle Trance (locks out further draw effects like Pommel Strike draw, Shrug It Off draw). This matters in draw-heavy decks but is rarely relevant in most builds.

UPGRADE: Draw 4 instead of 3. Moderate priority -- extra card draw is always valuable but other upgrades may have more impact.

SYNERGIES:
- **Demon Form**: Finding Demon Form in the first 2 turns instead of turn 5 is game-changing. Battle Trance digs through the deck faster.
- **Any combo deck**: More draw = more likely to find combo pieces (Rage + Anger, Corruption + Feel No Pain, etc).

MATCHUPS: Universally useful. Particularly valuable in boss fights where setup timing matters.
