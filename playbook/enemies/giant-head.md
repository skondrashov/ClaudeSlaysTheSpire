# Giant Head (Elite, Act 3)

HP: 625. Single target. Very long fight.

KEY MECHANIC: **Slow** -- each card played in a turn increases a counter. Attack damage is reduced based on how many cards you've played that turn. This punishes wide turns with many card plays. Play fewer, bigger cards.

ATTACK PATTERN: Giant Head starts with low attacks (~13) but escalates by +5 every attack turn. By turn 8-10, attacks reach 50-60+, making the fight a DPS race.

DEBUFF TURN: Giant Head alternates attacks with a debuff turn (applies Weak, possibly status cards). This is a free damage turn with no incoming attack.

STRATEGY:
- **Demon Form is critical.** Must be played Turn 1-2. At 625 HP, you need exponential Strength scaling to kill Giant Head before its attacks become unsurvivable. Delaying Demon Form by even 2-3 turns can be fatal.
- **Minimize card plays per turn** due to Slow. Play 1-2 big attacks rather than 3-4 small ones.
- **Immolate+ with high Strength** is the best damage card -- single play, massive damage.
- **Entrench+ is essential** for surviving high-damage turns. Double your block to keep pace with escalating attacks.
- **Impervious** gives 30 block but exhausts. Save for the turn attacks spike past your normal block capacity.
- **Reaper is critical** for sustain in this long fight. Without healing, you bleed out over 10+ turns.

HP THRESHOLD: Enter this fight above 60% HP. The fight lasts 10+ turns with increasing damage. Even with good block, expect to take chip damage from turns where attacks exceed your block capacity.

DEATH PATTERN (Run 149): Entered at 53/80 (66%). Accidentally exhausted Reaper+ Turn 1 due to index shifting. Demon Form delayed to Turn 4. By Turn 10, Giant Head was dealing 55+ damage/turn but had only lost ~250 of 625 HP. Fairy in a Bottle triggered Turn 10 (revive to 24 HP). Died Turn 11 to 60 damage with only 27 block. Lost the DPS race because Reaper and Demon Form were both unavailable early.

LESSON: **Never use turn() sequences with cards that shift indices.** Play one card at a time with state() checks between plays. A single index-shift error can exhaust a critical card and lose the fight.

BARRICADE ENGINE APPROACH (CONFIRMED WIN): The Barricade + Corruption + FNP + Entrench + Body Slam engine can defeat Giant Head without Demon Form or Strength scaling. Body Slam+ with 66-83 accumulated block deals massive single-card damage (bypasses Slow penalty since it is one card play). Apotheosis on the setup turn upgrades all cards. Entrench+ doubles block from 63 to 126, then Body Slam+ delivers the killing blow. With Preserved Insect reducing HP by 25%, the effective HP is ~469. The engine completed the kill in 8 turns with zero HP lost after the block wall was established. The key advantage: Body Slam+ is a SINGLE card play per turn, so Slow penalty is minimal.

NOTE: Demon Form is NOT required to kill Giant Head. Either Demon Form (Strength scaling) or Barricade + Body Slam (block scaling) works. The fight is unwinnable only when NEITHER scaling engine is available.
