# Node Choice

Consider, choosing the next map node:

- The remaining ledger: current HP minus the expected costs of every forced fight between here and the next recovery, with margin for the largest single spike — [[layer:heuristics, hp-management]].
- What each candidate yields against what it costs: an elite's relic compounds for the rest of the run; a rest buys back about one fight's expected cost; an unknown room in Act 2 prices as a full hallway fight — [[layer:heuristics, map]].
- The lock-ins: a node's children, and their children — a cheap node that forces an elite at low HP two floors later is the expensive one. Trace forward before committing.
- Recovery distance from each candidate: how many forced fights to the next rest, shop, or healing, and whether a bad draw along the way is covered.
- Whether the act plan still holds: re-route only when a fight cost well over its expected price and the remaining ledger no longer clears — [[layer:heuristics, map]].
- How close the boss is: in the last floors the priority inverts — rest, shop, and known rooms over fights, no HP-for-reward trades — [[layer:heuristics, map]].
