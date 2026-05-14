# Slime Boss (Act 1, HP: 140)

HP: 140 at A0, 150 at A9.

PATTERN: Fixed repeating cycle: Goop Spray -> Preparing -> Slam. Splits at 50% HP or below.

DAMAGE:
- Goop Spray: 0 damage, adds 3 Slimed cards to discard pile (5 at A19)
- Preparing: 0 damage (does nothing)
- Slam: 35 damage (38 at A4)
- Split: At 50% HP (70 HP at A0), disappears and spawns 1 Acid Slime (L) + 1 Spike Slime (L), each with the boss's current HP

Pre-split: Alternates between debuff turns (Goop Spray + Preparing = safe to go all-in) and Slam (35 damage). Debuff turns are safe windows for damage.
Split: At 50% HP (70 HP remaining), splits into Spike Slime (L) + Acid Slime (L). Each split slime has HP equal to the boss's remaining HP at split. **Excess damage past 70 HP is wasted AND makes the fight harder** -- if the boss goes from 87 to 63, both slimes spawn with 63 HP each instead of 70 HP.
- Post-split: Two enemies each with significant HP and damage. Spike Slime (L) attacks for ~16 and applies Frail. Acid Slime (L) attacks for ~11-12 and applies Weak. Combined 25-36 damage per turn. Both add Slimed cards to deck.

KEY MECHANICS:
- **Split transition**: Going from 1 enemy to 2 with combined 25-36 damage/turn is the hardest moment.
- **Slimed cards**: Cost 1E to exhaust, do nothing. Clog hand badly (3 of 5 cards being Slimed observed).
- **Dual debuffs**: Frail (block reduced 25%) + Weak (damage reduced 25%) simultaneously is devastating.
- **Large slimes split on death**: Both Spike Slime (L) and Acid Slime (L) split into 2 medium slimes when killed. Spike Slime (L) splits into 2x Spike Slime (M). Acid Slime (L) splits into 2x Acid Slime (M). This means killing one large slime creates a 3-enemy situation (1 large + 2 mediums), which can be worse than the 2-enemy state.

PREPARATION CHECKLIST:
1. AOE for the split (Thunderclap, Whirlwind, Cleave) -- MANDATORY. Without AOE, you must single-target each of 4+ enemies after both large slimes split. Confirmed death in Run 70: no AOE was ever offered, and single-target damage could not keep up with Slimed card generation from multiple enemies.
2. Burst single-target to kill one slime fast (Fiend Fire, Carnage+)
3. Exhaust tools for Slimed cards (Fiend Fire turns Slimed into 7 damage each, True Grit+, Burning Pact, Feel No Pain converts exhaust into 3 block each). Without exhaust tools, Slimed cards clog the hand (3 of 5 cards being Slimed observed), leaving only 2 playable cards per turn.
3b. Feed+ for massive Max HP gain. Slime Boss split creates multiple kill-eligible enemies (large slimes, medium slimes). Feed+ on each kill = +4 Max HP per kill. Confirmed: +22 Max HP from a single Slime Boss fight with Feed+, reaching 98 Max HP from 80 base. This is the best Feed fight in Act 1.
4. Enough block/HP to survive 2-3 turns of 25-36 combined damage
5. At least 1 upgrade before the fight. Zero upgrades makes the fight dramatically harder -- unupgraded Bash provides only 2 turns of Vulnerable instead of 3, and all damage/block cards are weaker.

CONFIRMED WINNING COMBINATION: Evolve + Thunderclap+ + Spot Weakness + Shuriken. Evolve neutralizes Slimed clog. Thunderclap+ applies AOE Vulnerable on split slimes. Spot Weakness + Shuriken provide Strength scaling that compounds across multi-enemy phase. With 6+ Str, Strikes deal 12-18 each (with Vuln), enabling fast kills even at low HP. Survived split phase at 3 HP through precise kill sequencing: killed Large Spike Slime, killed split Acid Medium, finished last enemy with exact lethal.

STRATEGY:
- **Pre-split**: Use debuff turns (free turns) to deal damage. Apply Vulnerable with Bash+. Don't worry about killing fast -- prepare for the split. **Manage damage near the 70 HP threshold**: on the turn the boss will cross 70 HP, calculate exact damage to avoid massive overkill. Spending energy on block instead of excess damage past the threshold is often correct.
- **SPLITTING A SLIME THAT IS ABOUT TO ATTACK IS YOUR BLOCK.** When a large or medium slime is about to deal damage and is close to its split threshold, prioritize damage to split it over blocking the incoming hit. Splitting the slime removes it from the board and replaces it with smaller slimes that act on future turns -- the incoming attack is completely prevented. Example: a Spike Slime (M) about to deal 16 damage has 8 HP remaining. Playing Dagger Throw (9 dmg) + Sneaky Strike (12 dmg) kills it, preventing 16 damage entirely. Spending 2E on block instead only mitigates 14 of the 16. Offensive plays that remove a threat are strictly better than defensive plays that partially absorb it.
- **At split**: Use Thunderclap for mass Vulnerable on both slimes. AOE with Whirlwind or Cleave.
- **Post-split**: SPREAD DAMAGE to both large slimes before killing either one. Killing one creates a 3-enemy situation (2 mediums + 1 large). Ideally, reduce both to low HP, then kill them in quick succession to minimize turns spent fighting 3+ enemies. If forced to kill one first, kill the one you can follow up on immediately -- do NOT leave a full-HP large slime alive while dealing with mediums.
- **Slimed management**: Exhaust Slimed cards as priority. Each one exhausted is one fewer dead draw for the rest of combat. Fiend Fire is ideal -- converts Slimed cards to 7 damage each. Feel No Pain turns each Slimed exhaust into 3 block, making the tempo cost much more bearable.

WHAT NOT TO DO:
- Enter without AOE. Single-target damage cannot handle the split. If no AOE was offered in card rewards, consider the run compromised against Slime Boss -- path aggressively through shops and events to find Thunderclap or Cleave before Floor 16.
- Enter with 0 upgrades. The upgrade death spiral (low HP forces resting at every rest site, which means no upgrades, which means fights are harder, which means more HP loss) was confirmed fatal in Run 70. Both rest sites were spent healing because HP was critically low from fights with unupgraded cards.
- Enter below 60% HP. 50/85 HP (58%) entry contributed to death in Run 70.
- Ignore Slimed cards. They accumulate and destroy hand quality.
- Play Berserk. Self-Vulnerable against 2 enemies doing 25-36 combined is suicidal.
- Focus all damage on one large slime while ignoring the other. Killing Acid Slime (L) at 63 HP while Spike Slime (L) sits untouched at 63 HP creates a 3-enemy nightmare (Spike Slime L + 2x Acid Slime M dealing 33+ combined damage). Spread damage to both large slimes before killing either.
- Use Hemokinesis at low HP during split phase. The 2 HP self-damage compounds with split damage.

---
