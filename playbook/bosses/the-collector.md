# The Collector (Act 2, HP: 282)

PATTERN:
- **Turn 1**: Spawns 2 Torch Head minions (30-40 HP each, attack for 7 damage each).
- **Turn 2-3**: Attacks for ~15-20 damage while Torch Heads also attack.
- **Turn 4**: Uses STRONG_DEBUFF -- applies Vulnerable 3, Frail 3, and Weakened 3 simultaneously. No damage on this turn.
- **Turn 5+**: Attacks while player is fully debuffed. Combined damage from Collector + 2 Torch Heads is 40-50+ raw, amplified by Vulnerable on player. Frail cuts block cards by 25%. Weakened cuts player's attack damage by 25%.
- **Minion respawn**: The Collector can resummon Torch Heads if they die. Killing Torch Heads is not a permanent solution.

KEY MECHANICS:
- **STRONG_DEBUFF (Turn 4)**: The most dangerous mechanic. Applies ALL THREE debuffs at once -- Vulnerable 3 (take 50% more damage), Frail 3 (block cards give 25% less), Weakened 3 (deal 25% less damage). This single turn makes the following 3 turns nearly unwinnable at low HP. Must have sufficient HP buffer to survive post-debuff turns.
- **Torch Heads**: Each deals 7 damage per turn. Combined with the Collector's own attacks, total incoming damage is 25-35+ per turn normally, and 40-50+ when Vulnerable is on the player.
- **HP check boss**: Unlike The Guardian (long fight, sustained block needed) or Hexaghost (specific counter cards needed), the Collector is primarily an HP check. Entering at low HP means the STRONG_DEBUFF turn creates unwinnable math.

PREPARATION CHECKLIST:
1. **Enter at 70%+ HP or have Pantograph** -- the STRONG_DEBUFF on Turn 4 creates a 3-turn window where incoming damage spikes by 50% and block is reduced by 25%. Pantograph heals 25 HP at boss start, which helps but does NOT bypass the threshold if you enter more than 25 HP below max. Without Pantograph, low HP entry is fatal.
2. **AOE damage (HIGHEST PRIORITY)** -- Immolate+ is the MVP. Hits Collector + both Torch Heads simultaneously. With Vulnerable: 42 damage to Collector per cast. Thunderclap+ applies Vulnerable to all 3 targets. AOE is MORE important than single-target burst because Torch Heads respawn.
3. **Mass debuff** -- Shockwave+ (Weak 3 + Vuln 3 to ALL enemies) is the second-highest-value card. Reduces combined incoming from 3 enemies by 25% for 3 turns while boosting all damage by 50%.
4. **Impervious** -- 30 block absorbs an entire post-debuff turn. The single best defensive card for this fight.
5. **Block density** -- After STRONG_DEBUFF, Frail reduces all block by 25%. Need multiple block sources to survive 40-50+ incoming. Armaments+ upgrading Defends mid-combat helps.
6. **Disarm** -- Permanently reduces Collector Strength. Play on Turn 1 for maximum cumulative value across 10 turns.
7. **Potions** -- Use aggressively if available. Gambler's Brew is excellent for finding block cards on critical turns.

STRATEGY:
- **Turn 1 (spawn turn)**: Collector spawns 2 Torch Heads. Use this turn for AOE setup: Thunderclap+ applies Vulnerable to all 3 enemies. Disarm on Collector reduces Strength. Front-load damage while Mutagenic Strength (if available) is active.
- **Turns 2-3**: Deal maximum damage to the Collector while blocking Torch Head attacks. Bash+ refreshes Vulnerable. Shockwave+ applies Weak to ALL enemies, reducing combined incoming by 25% for 3 turns -- this is the highest-value play in the fight.
- **Turn 4 (STRONG_DEBUFF)**: This turn deals no direct damage. Use it to play burst damage (Immolate+ with Vulnerable = 42+ damage to Collector + kills/damages Torch Heads) or setup. Treat it like a free turn for offense.
- **Turns 5-7 (post-debuff crisis)**: Block is reduced by Frail, damage is reduced by Weak, and you take 50% more from Vulnerable. This is the survival gauntlet. Impervious (30 block) is the best single card for surviving this window.
- **Turns 8-10 (cleanup)**: If the Collector is still alive, re-apply Vulnerable and use AOE (Immolate+) to clear re-summoned Torch Heads while chipping at Collector HP. Headbutt can put Immolate+ on top of draw pile for guaranteed AOE on the killing turn.

CONFIRMED WINNING APPROACH:
- Deck: Bash+, Immolate+, Thunderclap+, Shockwave+, Impervious, Disarm, Clothesline, Hemokinesis, Headbutt, Armaments+, Rage, Pommel Strike, Shrug It Off, 2x Defend, 2x Strike.
- Turn 1: Thunderclap+ (AOE Vuln) + Disarm (Collector -2 Str) + Hemokinesis + Strike for ~50 damage.
- Turn 3: Rage + Immolate+ (42 vuln damage to Collector, kills/damages Torch Heads) + Impervious (30 block). This turn is the pivot -- massive AOE damage while absorbing all incoming.
- Turn 4: Shockwave+ (Weak+Vuln all 3 enemies for 3 turns). Reduces post-debuff crisis damage significantly.
- Turns 5-7: Immolate+ again to clear re-summoned Torch Heads. Headbutt to guarantee draw order.
- Fight lasted 10 turns. Entered at full HP (Pantograph). Exited at 14/80 HP -- the fight IS an HP drain even when won.

RUN 110 DEATH CASE STUDY (DEFEAT, Floor 33):
- Entered at 49/86 (57%) -- below the 70% threshold. The Colosseum event on the previous floor forced an unexpected Slaver fight that drained HP. No upgrades in Act 2 (rested at both rest sites due to low HP entering them).
- Deck was strong offensively: Fire Breathing+/Evolve engine, Whirlwind+ (AOE), Flame Barrier+, Metallicize, Inflame, Spot Weakness, Bash+, Feed, Offering. Had Bronze Scales (Thorns 3) and Red Skull (+3 Str <50%).
- Turn 1 (spawn): Pommel Strike + Bash+ on Collector (Vulnerable applied). Solid start.
- Turn 2: Offering (-6 HP to 43) for setup. Metallicize, Shrug It Off, Defend+, 2x Strike+ on Collector. Took 13 damage (43->30).
- Turn 3: Flame Barrier+ + Defend+. Took 5 (30->25). Counter + Thorns dealt 27 passive damage.
- Turn 4 (STRONG_DEBUFF): Pommel Strike + Iron Wave on Collector. No damage incoming (free turn).
- Turn 5 (crisis): Used ALL 3 potions (Fire Potion on Torch Head, Dexterity +2, Speed +5). Killed one Torch Head with Strike+. 2x Defend+ with +7 Dex + Frail = 11 each = 25 total block vs 37 incoming. Took 12 (25->13 HP).
- Turn 6: Flame Barrier+ + Inflame. 16 block vs 37+ incoming. Knew death was likely.
- Turn 7: Shrug It Off + Feed (killed Torch Head 2) + Defend+. 17 block vs 37 incoming = take 20. Dead at 13 HP.
- **ROOT CAUSE**: 57% HP entry. The math was unwinnable after Turn 4 debuff at only 25 HP. Even with correct potion usage and strong AOE/counter damage, 25 HP cannot survive 3 turns of 37+ incoming with Frail-reduced block.
- **MISSING CARDS**: Impervious (30 block absorbs an entire crisis turn), Shockwave+ (mass Weak reduces 37 incoming to ~28 for 3 turns). Either card likely saves this run.
- **LESSON**: The 70% HP entry threshold is validated. At 57%, the Collector's Turn 4 triple debuff creates mathematically unwinnable turns even with optimal play. Also: Colosseum event must be factored into pre-boss HP planning.

WHAT NOT TO DO:
- Enter below 70% HP without Pantograph. Run 110 entered at 57% and died despite strong deck and optimal play. The STRONG_DEBUFF on Turn 4 creates incoming damage spikes that require 30-40+ HP buffer to survive. The 70% threshold is non-negotiable.
- Ignore Torch Heads entirely. Their combined 14 damage/turn adds up. AOE that hits all three targets is far more efficient than single-target.
- Save potions for "later." The post-debuff turns (5-7) are the crisis -- potions should be used to survive this window. Run 110 correctly used all 3 potions on Turn 5 but still died due to insufficient HP.
- Play Shockwave+ on Turn 1 before Torch Heads spawn. Wait until Turn 2+ when all enemies are present.
- Rely on single-target damage only. Immolate+ is the MVP of this fight -- AOE that damages all 3 targets simultaneously is critical for managing Torch Head respawns.
- Enter Unknown rooms before the boss without accounting for Colosseum event (forces combat, drains HP). Juzu Bracelet does NOT prevent Colosseum -- it is an event, not a monster room. Run 110: Unknown room 2 floors before boss was Colosseum, forcing a Slaver fight that drained HP from 65% to 57%. This directly caused the boss death. In the last 2-3 floors before the Act 2 boss, treat Unknown rooms as potential HP drains and prefer known-safe paths.
- Enter without Impervious or Shockwave+. Both Act 2 boss deaths (Runs 105, 110) were missing Impervious. The Collector's post-debuff turns deal 37-50+ damage -- 30 block from Impervious absorbs an entire crisis turn. Shockwave+ reduces 37 incoming to ~28 for 3 turns. These cards are disproportionately important for this fight.
