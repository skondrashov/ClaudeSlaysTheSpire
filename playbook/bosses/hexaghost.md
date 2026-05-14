# Hexaghost (Act 1, HP: 250)

PATTERN:
- **Turn 1**: Does NOT attack. Intent UNKNOWN. Free setup turn.
- **Turn 2**: Multi-hit attack, ~5x6=30 damage. This is the FIRST big attack. Must have block on this turn -- spending all energy on setup with zero block is a common fatal mistake (see "Turn 2 blocking" below).
- **Inferno**: 7x6 = 42 damage (multi-hit). Weak reduces each hit: floor(6*0.75)=4 per hit = 28 total. This is the most dangerous attack. Occurs later in the fight, not Turn 2.
- **ATTACK_DEBUFF**: Moderate damage + adds Burn status cards to deck.
- **DEFEND_BUFF**: Gains block and +Strength. No attack. Free turn for damage and Vulnerable refresh.
- **Medium attacks**: 4-8 and 14-24 damage on non-Inferno attack turns.
- **Block**: Can gain 12+ block.
- **Fight length**: ~13 turns with adequate damage. Can extend to 23+ turns without damage scaling. Long fight.

KEY MECHANICS:
- **Inferno (42 damage)**: Multi-hit means each hit is checked against block individually. Without Weak, this is near-impossible to survive. With Weak: 28 total, which is survivable.
- **Burn cards**: Unplayable status cards. Deal 2 damage per Burn in hand at end of turn AND clog hand (fewer real cards). Burns accumulate over the fight and create a death spiral.
- **Strength scaling**: Hexaghost gains Strength on DEFEND_BUFF turns, making subsequent attacks stronger. Long fight = more Strength = more dangerous.
- **Turn 1 free**: Use this for setup: Thunderclap (Vulnerable ALL), Metallicize, Powers.

PREPARATION CHECKLIST (must have at least 3 of 4):
1. Weak source (Shockwave, Clothesline, Intimidate, Uppercut, Weak Potion) -- reduces Inferno from 42 to 28. MANDATORY.
2. HP above 70% OR Pantograph relic (heals 25 HP at boss start -- NOT full HP). Multiple deaths at 35-50% HP entry confirm that even good decks cannot absorb Burns + Inferno at low HP. One death at 76% HP entry also occurred when Turn 2 blocking was insufficient (20 HP lost immediately), effectively reducing the HP advantage.
3. Passive block (Metallicize, Flame Barrier+) OR Impervious for the Inferno turn.
4. Burns management OR damage scaling to end the fight before Burns overwhelm. See "Burns management" section below.

If you have 0-2 of these, Hexaghost will likely kill you. Weak + passive block (or passive Dex) is NOT enough without damage scaling or Burns management -- the fight drags to 13+ turns (23 turns in worst case) and Burns attrition becomes unsurvivable. However, strong scaling (Cultist Potion Ritual + Rampage) combined with Incense Burner Intangible can compensate for missing Weak -- one fight reached Hexaghost 20/250 HP (92% damage dealt) in 8 turns with zero Weak sources. The fight was lost to an arithmetic error, not the missing Weak. Scaling that kills in 8-9 turns reduces Burns accumulation enough to survive without Weak.

DAMAGE OUTPUT MATTERS -- THE #1 CAUSE OF HEXAGHOST DEATH: Five deaths confirm the pattern. Weak and block keep you alive temporarily, but insufficient damage is the actual killer. In 13+ turn fights, Burns accumulate to 3-5 cards dealing 6-10 HP/turn in self-damage alone PLUS clogging your hand so you draw fewer real cards. The death spiral is: more turns -> more Burns -> less hand quality -> less damage -> even more turns -> even more Burns. Four deaths occurred with Weak sources but no way to handle Burns or end the fight quickly. One death had Hexaghost at 59/250 HP (24% remaining) when 4 Burns in hand dealt 8 damage at end of turn. Another death had Hexaghost at ~43/250 HP (17% remaining) with 5+ Burns dealing 4 damage each (Burns+) -- the deck had strong Str scaling (Inflame+ + Spot Weakness = 9 Str) but Turn 2 HP loss (20 damage from insufficient blocking) left no margin for the Burns attrition that accumulated over 12 turns. A fifth death (Silent) had Hexaghost at 24/250 HP (10% remaining) after 23 turns -- the deck had Dex 6 from 2x Footwork+ making blocking trivial but only ~10 damage/turn average. The fight lasted so long that 12+ Burns/Burns+ accumulated, dealing 12+ damage/turn from Burns alone, and the second Inferno (8x6=48) hit with a hand of ALL Burns. Damage scaling cards (Rampage, Inflame, Spot Weakness, Demon Form, Reaper) shorten the fight and reduce total Burns damage. Without at least one of these, the fight is near-unwinnable even with perfect Weak timing and Metallicize.

WHAT WORKS:
- **Evolve + Fire Breathing** -- the best anti-Burns engine. Evolve draws a replacement card when a Burn is drawn, neutralizing hand clog. Fire Breathing deals 6 (10 upgraded) damage to Hexaghost each time a Burn is drawn. Together, Burns become free damage with no downside. Confirmed across two clean Hexaghost victories (44/80 and 36/80 HP remaining after the fight). Set up both Powers on Turn 1 (free turn). This combo alone can handle Burns entirely -- no other Burns management needed. Even without Strength scaling, the engine shortens the fight significantly via passive damage.
- **Cultist Potion + Rampage** -- devastating scaling engine. Cultist Potion grants Ritual (+1 Str/turn permanent). Combined with Rampage's per-play scaling, damage grows multiplicatively. Confirmed: Rampage 3rd play with +6 Str and Vulnerable dealt 45 damage. By Turn 7 the fight was nearly won (Hexaghost at 20/250 HP). This combination can kill Hexaghost in 9 turns even without a Weak source. If Cultist Potion is available, use it Turn 1 (free turn) for maximum scaling.
- Demon Form (+2 Str/turn) -- the best scaling card for Hexaghost. By turn 5, every attack gains +8-10 damage. Combined with Anger (0E) and Shuriken (+1 Str per 3 attacks), the fight can be won in 7 turns instead of 13. Shorter fight = fewer Burns = less attrition.
- Disarm (-2 Str permanently) -- reduces all Hexaghost attacks including each Inferno hit. Very effective.
- Spot Weakness+ -- +4 Str on each Attack intent turn. Hexaghost's attack turns are frequent enough to trigger this reliably. In a 12-turn fight, two applications give +8 Str permanently. Combined with Vajra (+1 Str), this reached 9 Str for 22+ damage per Strike against Vulnerable Hexaghost. Strong alternative to Demon Form for Strength scaling.
- Rampage+ -- scales over the long fight to 40-60+ damage per play. One of the best Hexaghost-killing cards.
- Evolve (standalone) -- draws a replacement card whenever a Burn is drawn. Neutralizes Burns hand-clogging completely. Play on Turn 1 (free turn) alongside other Powers.
- Flame Barrier+ -- 16 block + 42 counter damage (7 Inferno hits x 6 each). Single best defensive card for Inferno turns. Upgrade priority if facing Hexaghost.
- Torii relic -- reduces each 2-damage Burn to 1 damage (halves Burns attrition). Does not save the fight alone but significantly extends survivability.
- Incense Burner -- Intangible every 6 turns. In a 12-turn fight, triggers twice. Intangible on an Inferno turn reduces 42 damage to 1. Even without a Weak source, Incense Burner can substitute for one by negating the most dangerous attacks entirely. Combined with Rampage scaling, enables all-offense turns on Intangible without needing block.

BURNS MANAGEMENT (CRITICAL -- four deaths from Burns accumulation):

Burns deal 2 damage per Burn in hand at end of turn AND reduce hand quality by replacing real cards. By turn 8-10, a typical hand contains 3-4 Burns and only 1-2 real cards. The fight becomes unwinnable not because of Hexaghost's attacks but because the deck can no longer generate meaningful damage or block. Burns+ (upgraded Burns from later ATTACK_DEBUFF turns) deal 4 damage each instead of 2 -- they are significantly more dangerous than regular Burns.

**Burns damage is DOUBLE-LETHAL**: Burns eat block at end of turn (reducing your block to zero or near-zero), AND THEN the next Hexaghost attack hits you with no block remaining. A player at 25 HP with 10 block and 4 Burns in hand will lose 8 HP from Burns (leaving 2 block), then take a 24-damage attack minus 2 block = 22 HP lost. The effective incoming is Burns + attack combined, not either one alone. Plan block for the SUM of Burns + next attack.

**Burns management tools (priority order):**
1. **Evolve + Fire Breathing** -- the best anti-Burns engine (see "WHAT WORKS"). Burns become free damage with no downside.
2. **Evolve (standalone)** -- neutralizes hand clog. Burns still deal end-of-turn damage, but you draw real cards to replace them.
3. **True Grit+** -- exhaust Burns for 9 block. Removes Burns permanently from the deck. Each exhausted Burn is -2 HP/turn and +1 real card per draw cycle.
4. **Fire Breathing (standalone)** -- each Burn drawn deals 6-10 damage to Hexaghost. Does not stop hand clog, but turns Burns into a damage source.
5. **Second Wind** -- exhaust all non-Attack cards in hand including Burns, gaining block for each. Mass Burns removal in one play.
6. **Damage scaling** (Inflame, Spot Weakness, Demon Form, Rampage) -- not Burns management per se, but shortens the fight from 13 turns to 8-9, reducing total Burns accumulated from 4-5 to 2-3.

**If the deck has NO Burns management AND NO damage scaling by Floor 15, the Hexaghost fight is near-unwinnable.** Metallicize + Weak + basic damage cannot outrace Burns accumulation in a 13-turn fight. Even WITH damage scaling (Inflame+ + Spot Weakness = +9 Str), the fight can still be lost if HP is wasted on Turn 2 from insufficient blocking -- the damage scaling shortens the fight from 13 to 12 turns, but Burns+ (4 damage each) in the final turns are still lethal at low HP. Actively seek Evolve, Fire Breathing, True Grit+, or Inflame/Spot Weakness before the boss. **The Silent has NO native Burns management tools** (no Evolve, Fire Breathing, True Grit, Second Wind). The Silent's only solution is kill speed: poison scaling (Deadly Poison + Catalyst+, Noxious Fumes) or high attack density to end the fight before Burns accumulate.

STRATEGY:
- **Turn 1 (free)**: Set up. Demon Form (3E) is the ideal turn 1 play -- the entire fight is won by scaling. If Demon Form is not available, play Thunderclap for mass Vulnerable + Metallicize + Evolve. Play Powers before anything else on this free turn.
- **Turn 2 (MUST BLOCK)**: Turn 2 is a ~30 damage multi-hit. Spending all 3E on setup (Powers, Spot Weakness) with zero or minimal block is a fatal mistake. Every HP lost on Turn 2 compounds with Burns damage later. Budget at LEAST 1E for block on Turn 2. If choosing between playing a second setup card and playing a block card, play the block card. One death confirmed from spending 3E on Inflame+ + Spot Weakness + Ghostly Armor (10 block vs 30 incoming = 20 unblocked) -- the 20 HP lost here was the exact margin that made Burns lethal by Turn 12.
- **Save Weak for Inferno**: Apply Shockwave/Clothesline/Intimidate on the first Inferno turn to reduce 42 to ~28.
- **Play Metallicize early**: 3 block/turn over 13 turns = 39 free block. Set up as soon as possible.
- **Reapply Vulnerable with Bash+**: Use DEFEND_BUFF (free) turns to refresh Vulnerable without spending block resources.
- **Burns management**: Exhaust Burns with True Grit+ if available. Play Evolve on Turn 1 to neutralize hand clog. Burns deal cumulative damage -- 3 Burns = 6 damage/turn + 3 fewer real cards.
- **Kill speed matters**: Shorter fight = fewer Burns accumulated = less attrition damage. Inflame (+2 Str) on turn 1 shortens the fight by 2-3 turns. This is not optional -- without damage scaling, Burns WILL overwhelm even a well-blocked deck.

SILENT-SPECIFIC STRATEGY (confirmed in one defeat):

The Silent's primary challenge against Hexaghost is damage output, not defense. Footwork+ stacking (Dex 6) makes blocking trivial -- zero damage taken in hallway fights and most boss turns. But without poison scaling, Noxious Fumes, or burst attacks, the fight drags 20+ turns. Burns accumulate faster than the Silent can kill.

**The Silent kill condition for Hexaghost requires one of:**
1. **Poison scaling**: Deadly Poison + Catalyst+ (triple poison for massive guaranteed damage). This can kill Hexaghost in ~10 turns from poison alone, avoiding the Burns death spiral.
2. **Noxious Fumes**: Passive 2 poison/turn to all enemies. Over 13 turns = 182 guaranteed damage. Combined with other poison sources, shortens the fight enough.
3. **Burst attack density**: Dash+, Predator, Backstab, Blade Dance provide immediate damage. The Silent's base attacks (Strikes) are weaker than Ironclad's -- need multiple upgraded attack cards to kill in reasonable time.

**Without at least one strong damage source, the Silent cannot kill Hexaghost before Burns overwhelm.** A deck with 2x Footwork+ (Dex 6), Dash+, Quick Slash, one Strike, and Masterful Stab reached Hexaghost 24/250 HP in 23 turns but died to the second Inferno (8x6=48) with a hand of all Burns. The defensive core was excellent (zero damage taken in 5/6 pre-boss fights), but damage output was ~10/turn average, far too slow.

**Masterful Stab is a trap against Hexaghost.** Its cost increases by 1E for each HP lost in combat. Even chip damage from Burns (2-4 HP/turn) raises the cost from 0E to 4-7E within 10 turns, making it unplayable. By Turn 15, the player was using Setup+ to reset Masterful Stab to 0E, wasting a play. In short fights where zero damage is taken, Masterful Stab is excellent (free 12 damage). In the Hexaghost fight where Burns deal unavoidable chip damage, it becomes dead weight.

**Burns+ (upgraded Burns from ATTACK_DEBUFF turns) deal 4 damage each at end of turn.** By Turn 12, a hand of 3 Burn+ cards deals 12 unblockable damage per turn, eating through block and draining HP even when Hexaghost attacks are fully blocked. Silent has no native Burns management (no Evolve, Fire Breathing, True Grit). The only solution is kill speed.

**Crippling Cloud** is a good Silent Weak source for Hexaghost (2 Weak + 4 Poison for 2E, exhausts). Combined with Neutralize+ (2 Weak), the Silent has exactly 2 Weak applications -- enough for 2 separate Inferno turns. **Save Crippling Cloud for an Inferno turn, NOT for poison damage on a non-attack turn.** Confirmed error: player used Crippling Cloud on a DEFEND_BUFF turn (Turn 13) for 4 poison, wasting the 2 Weak. The first Inferno came on Turn 16 without Weak, dealing full 6x6=36 damage instead of 6x4=24. The 12 extra damage (36 vs 24) was a significant portion of the player's remaining HP. The poison from Crippling Cloud (10 total damage over 4 turns) was far less valuable than the 12 damage prevented by Weak on Inferno.

**Art of War relic** has anti-synergy with the Silent's damage needs here. Gaining +1E on turns with no attacks encourages all-block turns, but the fight demands mixed offense+defense turns. Playing zero attacks for the Art of War bonus extends the fight by several turns.

WHAT NOT TO DO:
- **End turn before verifying the kill.** When Hexaghost is near death, calculate total damage from ALL playable cards before ending turn. A confirmed death occurred at Hexaghost 7/250 HP remaining because the player played Iron Wave (13 damage) against 20 HP and ended turn, despite having Headbutt (17 damage) in hand with 2E remaining. Combined damage (30) would have killed. The error was writing "13 > 20" in reasoning -- a basic arithmetic mistake. On kill turns, play attacks one at a time and verify the kill before ending.
- Spend all energy on setup Turn 2 with minimal block. Turn 2 is a ~30 damage multi-hit. Even 5 more block (one Defend) reduces damage from 20 to 15, which can be the difference between surviving Burns in the final turns and dying. Setup is important, but not at the cost of 20+ unblocked damage.
- Fight without a Weak source. Inferno at full power (42) is near-unsurvivable.
- Fight without Burns management OR damage scaling. Five deaths had Weak + passive block but no way to handle Burns or end the fight quickly. Metallicize alone cannot save you from 4 Burns dealing 8+ damage/turn. Footwork+ Dex scaling alone cannot save you either -- Dex 6 blocks every attack perfectly but zero Burns management + low damage output = 23-turn fight where Burns overwhelm.
- Play Brutality. Burns + Brutality self-damage = 3-5 HP/turn death spiral.
- Play Berserk. Self-Vulnerable + Inferno = death.
- Enter below 70% HP without Pantograph. Pantograph only heals 25 HP, not full -- plan accordingly. The 250 HP + Inferno + Burns demands a large HP buffer. At the pre-boss rest site, REST if below 70% HP -- do not upgrade. An upgrade is worthless if you die on the boss.
- Waste Shockwave on a non-Inferno turn. Same applies to Crippling Cloud (Silent): do not use on a DEFEND_BUFF turn for poison when the Weak is needed for Inferno.
- Take Odd Mushroom from the Mushrooms event when Hexaghost is the Act 1 boss. Odd Mushroom reduces Vulnerable from 1.5x to 1.25x, cutting all Vulnerable-amplified damage by ~17%. In a fight where kill speed determines whether Burns overwhelm you, 17% less damage extends the fight by 1-2 turns and adds 1-2 more Burns to the deck. Confirmed as a contributing factor in a death where Hexaghost reached 24% HP remaining but Burns attrition finished the run.
