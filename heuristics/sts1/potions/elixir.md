# Elixir

Use when hand is clogged with status cards (Burns, Wounds, [[cards/Slimed]], [[cards/Dazed]]). Mass-exhaust garbage cards to improve future draws. Also useful for controlled deck thinning mid-combat (exhaust extra Strikes/Defends that are diluting key card draws).

## Multi-Select Index Shifting (CRITICAL)

Elixir opens a HAND_SELECT screen where you choose cards one at a time. **After each card is selected, it is removed from the displayed hand and all indices shift down.** You must re-read the hand state after each selection.

**Example error that gets you killed:** Hand was [Carnage, Wound, Wound, Wound, Defend, Shockwave]. Player intended to exhaust 3 Wounds. After selecting indices 1 and 2 (two Wounds), the hand became [Carnage, Wound, Defend, Shockwave]. The player selected index 3 expecting the third Wound, but index 3 was now [[cards/Shockwave]]. Shockwave was exhausted, removing the only [[debuffs/Weak]] source, and the player died to unmitigated damage.

**Rule:** During multi-select, ALWAYS re-read the hand after each selection. Never assume indices from the original hand still apply. Select by reading the current hand, not by counting from the original.
