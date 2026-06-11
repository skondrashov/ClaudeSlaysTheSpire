# Turn (combat)

Consider, every combat turn, before composing the play:

- Incoming damage from LIVING enemies, as displayed — intent numbers already include every modifier (their Strength and Weak, your Vulnerable).
- Your own debuffs in every calculation — your Weak cuts your attack 25%, your Frail cuts your block 25%, both floored. The arithmetic checklist: [[layer:heuristics, combat]].
- The paths to zero damage (kill the attacker / block / debuff / potion) before settling for taking any — the full algorithm: [[layer:heuristics, combat]].
- Whether any premise from earlier in this turn has died — a kill changes incoming; a stance or power changes costs; No Draw kills every later draw effect. Re-derive before each card, not once per turn.
- What each held potion converts to in this fight, bounded by the turns it has left — [[domain:sts1, category:recognitions, potion-use|the potion questions]].
- The energy sum of the planned sequence against energy available; X-cost cards consume everything and go last.
- Whether this turn changes the fight's structure: a split threshold crossed, a phase boundary (50% on some bosses), a scaling enemy left alive another turn.
