# Node Choice

Consider, choosing the next map node:

- The remaining ledger: current HP minus what each forced fight between here and the next recovery will cost THIS deck — derived from its damage clock against your kill speed, not recalled — with margin for the largest single spike — [[layer:heuristics, hp-management]].
- What each candidate yields against what it costs: an elite's relic compounds for the rest of the run; a rest buys back about one fight's worth of HP; an unknown room in Act 2 prices as a full hallway fight — [[layer:heuristics, map]].
- The lock-ins: a node's children, and their children — a cheap node that forces an elite at low HP two floors later is the expensive one. Trace forward before committing. A forced Monster room is NOT a safe default: price its worst-case enemy too, not just the elite you routed around.
- **[[acts/Act 3]] Monster-pool kill-threats** (price these at the fork before committing a forced Monster child, the same way you price a forced elite):
  - **[[enemies/Transient]]** — a block-CHECK survival fight: attacks 40/50/60/70/80 over 5 turns at A2+, then fades. The turn-5 80 exceeds most reachable block ceilings; a block-light / attack-heavy hand cannot cover it. Price your turn-5 block BEFORE routing in. (Attack it — [[buffs/Shifting]] means damage you deal reduces incoming; do not pure-block.)
  - **[[enemies/The Maw]]** — 300 HP, opens Roar (3 Weak + 3 Frail), then Slam 25 / Nom Nom (ramping multi-hit) / Drool (+3 Str each). A slow deck eats escalating hits under Frail; a real kill threat if you can't burst it down.
  - **[[enemies/Reptomancer]]** — summons Daggers (up to 4), Big Bite 30 / Snake Strike 13x2+Weak; without AOE the dagger swarm out-damages a slow clear.
- Recovery distance from each candidate: how many forced fights to the next rest, shop, or healing, and whether a bad draw along the way is covered.
- Whether the act plan still holds: re-route only when a fight cost well over what you priced it at and the remaining ledger no longer clears — [[layer:heuristics, map]].
- How close the boss is: in the last floors the priority inverts — rest, shop, and known rooms over fights, no HP-for-reward trades — [[layer:heuristics, map]].
