# Giant Head (Elite, Act 3, HP: 500)

Single target. Very long fight.

POWER: **Slow** -- whenever you play a card, the Giant Head receives 10% more damage from Attacks this turn. This actually REWARDS playing many cards per turn -- more plays = more damage dealt to it.

PATTERN: For the first 4 turns, uses Count (13 damage) or Glare (1 Weak) with 50/50 chance (cannot repeat either 3x in a row). After 4 turns, exclusively uses "It Is Time" for the rest of combat.

DAMAGE:
- Count: 13 damage
- Glare: 0 damage, applies 1 Weak
- It Is Time: 30 damage base, increases by 5 per use (30 -> 35 -> 40 -> 45 -> 50 -> 55 -> 60 max)

KEY MECHANIC: It Is Time escalates by +5 per use. After 4 turns of Count/Glare, every subsequent turn deals 30+ and growing. The fight is a DPS race -- kill before It Is Time reaches 50+.

STRATEGY:
- **Demon Form is critical.** Must be played Turn 1-2. At 500 HP, you need exponential Strength scaling to kill Giant Head before its attacks become unsurvivable. Delaying Demon Form by even 2-3 turns can be fatal.
- **Slow HELPS you** -- each card played makes Giant Head take 10% more damage from attacks this turn. Play many cards per turn to maximize damage. Shivs and multi-card turns are rewarded.
- **Immolate+ with high Strength** is the best damage card -- single play, massive damage.
- **Entrench+ is essential** for surviving high-damage turns. Double your block to keep pace with escalating attacks.
- **Impervious** gives 30 block but exhausts. Save for the turn attacks spike past your normal block capacity.
- **Reaper is critical** for sustain in this long fight. Without healing, you bleed out over 10+ turns.

HP THRESHOLD: Enter this fight above 60% HP. The fight lasts 10+ turns with increasing damage. Even with good block, expect to take chip damage from turns where attacks exceed your block capacity.

DEATH PATTERN (Run 149): Entered at 53/80 (66%). Accidentally exhausted Reaper+ Turn 1 due to index shifting. Demon Form delayed to Turn 4. By Turn 10, Giant Head was dealing 55+ damage/turn but had only lost ~250 of 500 HP. Fairy in a Bottle triggered Turn 10 (revive to 24 HP). Died Turn 11 to 60 damage with only 27 block. Lost the DPS race because Reaper and Demon Form were both unavailable early.

LESSON: **Never use turn() sequences with cards that shift indices.** Play one card at a time with state() checks between plays. A single index-shift error can exhaust a critical card and lose the fight.

BARRICADE ENGINE APPROACH (CONFIRMED WIN): The Barricade + Corruption + FNP + Entrench + Body Slam engine can defeat Giant Head without Demon Form or Strength scaling. Body Slam+ with 66-83 accumulated block deals massive single-card damage (bypasses Slow penalty since it is one card play). Apotheosis on the setup turn upgrades all cards. Entrench+ doubles block from 63 to 126, then Body Slam+ delivers the killing blow. With Preserved Insect reducing HP by 25%, the effective HP is ~375. The engine completed the kill in 8 turns with zero HP lost after the block wall was established. The key advantage: Body Slam+ is a SINGLE card play per turn, so Slow penalty is minimal.

NOTE: Demon Form is NOT required to kill Giant Head. Either Demon Form (Strength scaling) or Barricade + Body Slam (block scaling) works. The fight is unwinnable only when NEITHER scaling engine is available.
