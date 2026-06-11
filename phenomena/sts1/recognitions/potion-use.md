# Potion Use (in combat)

Applies when: in combat holding any potion, and at least one of — incoming damage exceeds what the hand can block; a kill may be in reach this turn or next; the fight is an elite or boss; the belt is full.

The questions this situation asks, and what feeds them:

- **How many turns does this fight have left?** A potion's value is bounded by the fight it's drunk in. Estimate turns-to-kill and turns-to-survive first; every conversion below is multiplied by that number.
- **What does each held potion convert to here?** A damage potion is damage toward removing an attacker (which is also damage prevention); a block potion is this turn's spike, covered; a Strength or draw potion is its effect times the remaining turns. Run the arithmetic per potion against this fight — see each potion's own entry.
- **What does holding cost?** Potions expire worthless at the run's end, and a full belt forfeits the next reward — a potion drunk at full slots costs nothing. Holding is justified by a named fight within the next 1-2 floors, not by "later." The full economics: Potion Economy in [[layer:heuristics, combat]].
- **Is this one of the situations where drinking is reliably right?** An enemy that scales each turn ([[buffs/Ritual]], Rally) makes early kills worth more than the potion's face value; a hit the hand cannot block converts a block potion one-for-one into HP, the resource that does not come back ([[layer:heuristics, hp-management]]).
- **Does the potion's timing interact with this turn's plan?** Random-outcome potions come after deterministic plays; draw potions are dead under No Draw; a targeted potion's target may already be dying to the cards in hand.
