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

## SILENT POISON APPROACH

Poison bypasses Metallicize 8 entirely -- it ticks at end of enemy turn, ignoring block. This makes poison the primary damage source for the Silent against Giant Head.

**Strategy:** Apply poison early (Deadly Poison+, Crippling Cloud, Noxious Fumes), then triple with Catalyst+ for a lethal poison total. The key math: if Giant Head has 375 HP (with Preserved Insect -25%), tripling 16+ poison with Catalyst+ produces 48+ poison, which deals 48+47+46+...=1176 total damage over time -- far more than needed. The fight becomes a race to triple poison before It Is Time escalates past your block capacity.

**Slow mechanic helps the Silent.** Each card played makes Giant Head take 10% more damage. The Silent's high card-count turns (5-8 cards with draw engines and Shivs) mean Giant Head takes 50-80% more damage from Attacks. Pair Shiv generation with targeted attacks for maximum Slow bonus. Poison damage is NOT affected by Slow (it's not Attack damage), so Slow primarily amplifies direct Attacks.

**Metallicize 8 interaction:** Direct attacks (Strikes, Bane+, Dash) must overcome 8 Metallicize block before dealing HP damage. Bane+ (20 damage on poisoned) breaks through. Single Strikes (6 damage) bounce off entirely unless block was already stripped by a prior attack that turn.

**Critical timing window:** After Catalyst+ triples poison (e.g., to 48+), the fight is mathematically won but the player must survive 2-3 more turns for poison to finish the kill. These survival turns often coincide with It Is Time reaching 40-50+ damage. Block aggressively on these turns. Use Neutralize+ (Weak), Malaise, Piercing Wail to reduce incoming. **Use ALL available potions on survival turns.** A Strength Potion adding +2 to Strikes, or an Explosive Potion dealing 10 direct damage, can be the difference between the enemy dying from poison this turn versus surviving at 1 HP.

**DEATH PATTERN (Silent, Floor 40):** Giant Head survived at 1 HP after poison tick (52 HP - 51 poison = 1 HP). Player had Strength Potion and Explosive Potion unused at death. Either potion would have dealt the 1 extra damage needed for poison to finish the kill. The player used Malaise defensively on Turn 8 instead of using potions offensively on Turn 7. Potions are zero-cost -- no energy, no card play. ALWAYS use offensive potions against Giant Head before the kill window closes.
