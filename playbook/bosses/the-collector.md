# The Collector (Act 2, HP: 282)

HP: 282 at A0, 300 at A9.

PATTERN:
- **Turn 1**: Always Spawn -- summons 2 Torch Head minions (HP: 38-40, attack for 7 damage each).
- **Turn 2-3**: Fireball (18 damage) or Buff (all enemies gain 3 Str, Collector gains 15 Block).
- **Turn 4**: Always Mega Debuff -- applies 3 Weak + 3 Vulnerable + 3 Frail simultaneously. No damage.
- **Turn 5+**: With 0-1 minions: Spawn 25% / Fireball 45% / Buff 30%. With 2 minions: Fireball 70% / Buff 30%. Cannot use Buff 2x in a row. Cannot use Fireball 3x in a row.
- **Torch Heads**: 38-40 HP. Tackle for 7 damage every turn. Minion tag.
- **Minion respawn**: The Collector can resummon Torch Heads if they die. Max 2 active at a time.

KEY MECHANICS:
- **STRONG_DEBUFF (Turn 4)**: The most dangerous mechanic. Applies ALL THREE debuffs at once -- Vulnerable 3 (take 50% more damage), Frail 3 (block cards give 25% less), Weakened 3 (deal 25% less damage). This single turn makes the following 3 turns nearly unwinnable at low HP. Must have sufficient HP buffer to survive post-debuff turns.
- **DEFEND_BUFF Strength scaling**: Each time the Collector uses Buff (DEFEND_BUFF), ALL enemies gain +3 Str and the Collector gains 15 Block. The Collector starts at Str 3. Over a long fight with 4+ DEFEND_BUFF uses, Str escalates to 9-14+. By Turn 15-19, Fireball hits for 30+ instead of 18. Combined with Torch Heads that also gain +3 Str per buff, total incoming per attack turn can exceed 50-60 in extended fights. This makes long fights exponentially more dangerous -- the Collector is not just an HP check but a DPS race.
- **Torch Heads**: Each deals 7 damage per turn (base). Combined with the Collector's own attacks, total incoming damage is 25-35+ per turn normally, and 40-50+ when Vulnerable is on the player. Torch Heads also gain +3 Str from each DEFEND_BUFF, so late-fight Torch Heads hit for 13-16+ each.
- **HP check boss AND DPS race**: The Collector punishes both low HP entry (STRONG_DEBUFF creates unwinnable math at low HP) and slow kill speed (DEFEND_BUFF Str scaling makes late-fight attacks devastating). Entering at low HP means the STRONG_DEBUFF turn creates unwinnable math. Extending the fight means DEFEND_BUFF Str scaling compounds to lethal levels.

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

SILENT-SPECIFIC STRATEGY:
- **Play defensive powers (After Image, Footwork+) IMMEDIATELY -- do not wait.** These powers must be active before Turn 4's triple debuff. After Image provides 1 block per card played (crucial when Frail reduces all other block). Footwork+ provides Dex that partially offsets Frail. If these powers sit in discard unplayed when the debuff lands, the post-debuff turns become unsurvivable.
- **Poison (Noxious Fumes+) is the primary win condition for Silent.** Noxious Fumes+ applies 3 poison/turn to ALL enemies (Collector + both Torch Heads). Poison ignores block, bypasses Frail/Weak debuffs on the player, and scales passively. Set it up Turn 1 above all else. Poison is especially important because it is the only damage source unaffected by the Weakened debuff from Turn 4.
- **Piercing Wail+ is the Silent's Shockwave equivalent.** Reduces ALL enemy Str by 8 for 1 turn. Against Collector + 2 Torch Heads, this can reduce combined incoming by 20+ damage. Use it on high-damage turns (post-debuff or when multiple enemies attack).
- **Prioritize killing Torch Heads with Shivs.** After Image + Shivs (0E each) generates block while dealing damage to Torch Heads. Each Shiv played = 1 free block + 4 damage. Two Shivs from Cloak and Dagger+ = 8 damage + 2 free block on top of C&D+'s base block.
- **Wraith Form timing is critical.** Do NOT play Wraith Form early in this fight. The Collector fight lasts 15-20 turns due to DEFEND_BUFF turns and Torch Head respawns extending the fight. Playing Wraith Form on Turn 2 means Dex is -17 or worse by Turn 19, making all Skill-based block 0. After Image (~7-8 block/turn) cannot survive 50-60 incoming from Str-scaled attacks. Hold Wraith Form until the Collector is below 50 HP or the fight will end within 5-6 turns. See wraith-form.md for detailed timing rules.
- **The Collector's DEFEND_BUFF Str scaling punishes slow kills.** Each DEFEND_BUFF gives all enemies +3 Str. In a 19-turn fight with 4+ DEFEND_BUFF uses, the Collector's Fireball scales from 18 to 30+ and Torch Heads hit for 13-16 each instead of 7. Poison scaling (Noxious Fumes+) is the answer -- it kills passively without extending the fight.

WHAT NOT TO DO:
- Enter below 70% HP without Pantograph. The STRONG_DEBUFF on Turn 4 creates incoming damage spikes that require 30-40+ HP buffer to survive. The 70% threshold is non-negotiable.
- Ignore Torch Heads entirely. Their combined 14 damage/turn adds up. AOE that hits all three targets is far more efficient than single-target.
- Save potions for "later." The post-debuff turns (5-7) are the crisis -- potions should be used to survive this window. Run 110 correctly used all 3 potions on Turn 5 but still died due to insufficient HP.
- Play Shockwave+ on Turn 1 before Torch Heads spawn. Wait until Turn 2+ when all enemies are present.
- Rely on single-target damage only. Immolate+ is the MVP of this fight -- AOE that damages all 3 targets simultaneously is critical for managing Torch Head respawns.
- Enter Unknown rooms before the boss without accounting for Colosseum event (forces combat, drains HP). Juzu Bracelet does NOT prevent Colosseum -- it is an event, not a monster room. Run 110: Unknown room 2 floors before boss was Colosseum, forcing a Slaver fight that drained HP from 65% to 57%. This directly caused the boss death. In the last 2-3 floors before the Act 2 boss, treat Unknown rooms as potential HP drains and prefer known-safe paths.
- Enter without Impervious or Shockwave+. Both Act 2 boss deaths (Runs 105, 110) were missing Impervious. The Collector's post-debuff turns deal 37-50+ damage -- 30 block from Impervious absorbs an entire crisis turn. Shockwave+ reduces 37 incoming to ~28 for 3 turns. These cards are disproportionately important for this fight.
