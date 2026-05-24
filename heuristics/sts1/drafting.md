# Drafting & Deck Building

Card evaluation and deck construction heuristics for [[characters/Ironclad]]. Every card pick should solve a problem, not add raw power.

---

## Healing Card Priority (THE CRITICAL GAP)

The single biggest strategic failure across 50 runs: entering [[acts/Act 2]] without a healing card. [[relics/Burning Blood]] (+6/fight) heals 6% of max HP per fight. Act 2 fights drain 25-50 HP. The math does not work.

**Card reward priority when offered a healing card:**
- **[[cards/Reaper]]: TAKE IT.** Even over good damage/block cards. Best card in the game for Ironclad.
- **Feed: TAKE IT** in early [[acts/Act 1]]. +3-4 Max HP per kill compounds over 15+ fights.
- If neither offered by Floor 12, seek healing potions ([[potions/Blood Potion]], [[potions/Regen Potion]]) and healing relics ([[relics/Toy Ornithopter]], [[relics/Meal Ticket]], [[relics/Bloody Idol]]) at shops.

**This is non-negotiable.** A deck with Reaper + adequate damage will reach [[acts/Act 3]]. A deck with perfect damage/block but no healing will die in Act 2 floors 20-30.

**Reaper alone is NOT sufficient.** Reaper exhausts after a single use per fight. In consecutive combat rooms (common in Act 2), Reaper heals once per fight but cannot offset sustained drain across multiple fights. Multiple healing sources are required. **Minimum TWO healing sources by Act 2 Floor 5.**

**Sozu boss relic risk:** [[relics/Sozu]] (+1E, no potions) permanently eliminates potions as a healing source. Do NOT take Sozu unless the deck already has a healing card (Reaper, Feed) or a healing relic (Toy Ornithopter, Meal Ticket). Burning Blood alone cannot compensate for Act 2 HP drain without potion supplementation. **Confirmed fatal in Run 217:** took Sozu with no healing card, forced 5 rests in Act 2, entered boss at 51% HP (threshold 70%), died.

---

## Act 2 Readiness Checklist

Verify by Floor 15. ALL FOUR criteria or die in Act 2:

1. **Damage scaling** -- the deck needs SOME way to outpace enemy block and HP growth. Two valid paths:
   - **Strength path:** [[cards/Inflame]], [[cards/Spot Weakness]] (front-loaded). NOT [[cards/Demon Form]] alone (too slow for hallway fights, confirmed in 2+ deaths). Demon Form fills the boss scaling role but does NOT satisfy this criterion. Without front-loaded Str, Reaper healing is also ineffective (Reaper needs Str on the turn it is played, not 3 turns later).
   - **Exhaust/Block path (under investigation):** [[cards/Corruption]] + [[cards/Feel No Pain]] (+ [[cards/Body Slam]] for damage conversion). This engine may generate block and damage without Strength — Run 187 won with it as the primary engine (with supplementary Str from Spot Weakness + Red Skull). Whether it works WITHOUT any Str sources is being tested (see exploration directives).
2. **AOE damage** -- [[cards/Thunderclap]], [[cards/Cleave]], [[cards/Immolate]], [[cards/Whirlwind]]. Required for [[enemies/Gremlin Leader]] (gremlins re-summon), 3 Cultists (hard-scaler, kill speed matters), [[bosses/Slime Boss]] split.
3. **Healing beyond Burning Blood** -- Reaper, Feed, potions/relics. Burning Blood (+6/fight) cannot offset 30-50 HP Act 2 fights.
4. **Block scaling beyond basic Defends** -- [[cards/Shrug It Off]], [[cards/Flame Barrier]], [[cards/Metallicize]], [[cards/Impervious]], or [[cards/Corruption]] + [[cards/Feel No Pain]] (FNP generates block on every exhaust). Basic Defends provide only 20 block from a full hand of 4. Act 2 boss Hyper Beam deals 45-57 damage. Even late Act 2 hallway fights ([[enemies/Book of Stabbing]] turn 5: 6x6=36) outscale basic Defends.

**If missing 2+ entering Act 2, shift to conservative pathing** -- avoid elites, path through shops and rest sites, skip unknown rooms.

---

## Ironclad Act 1 Tier List

The starting deck is nearly identical every run. Use a tier list, not first-principles reasoning.

**MUST-TAKE** (take over almost anything):
- Reaper (healing -- most important card for Ironclad)
- Feed (permanent Max HP scaling, take early for max value)
- Inflame (immediate +2 Str, satisfies front-loaded Str requirement)
- Immolate (massive AOE + single target, solves multiple problems)
- Impervious (30 block in one card, solves every block problem)
- Shrug It Off (block + draw, best defensive common)
- [[cards/Pommel Strike]] (damage + draw, best offensive common)

**HIGH PRIORITY** (take to fill gaps):
- Spot Weakness (+3/+4 Str when enemy attacks -- most enemies attack)
- Thunderclap (AOE + [[debuffs/Vulnerable]], critical for Byrds in Act 2)
- [[cards/Headbutt]] (damage + deck manipulation)
- [[cards/Carnage]] (high damage Ethereal attack -- great for Nob-safe damage)
- [[cards/Iron Wave]] (damage + block in one card)
- [[cards/Clothesline]] (damage + [[debuffs/Weak]])
- [[cards/Shockwave]] (mass Weak + Vulnerable, exhausts -- incredible vs multi-enemy)
- Flame Barrier (block + counter damage, excellent in multi-hit fights)

**SITUATIONAL** (take only if it fills a specific gap):
- [[cards/Evolve]] (MUST-TAKE if Slime Boss is the Act 1 boss -- trivializes [[cards/Slimed]] cards)
- [[cards/Fire Breathing]] (MUST-TAKE if Slime Boss AND you have Evolve)
- [[cards/Uppercut]] (Weak + Vulnerable in one card, but 2E is expensive)
- [[cards/Perfected Strike]] (only if 3+ Strike cards remain in deck)
- [[cards/Anger]] (free attack, good for Nob, but adds copies to discard)
- [[cards/Rampage]] (scaling damage, needs multiple plays to ramp)
- [[cards/True Grit]] (ONLY if you can upgrade it soon -- unupgraded random exhaust is dangerous)
- [[cards/Sentinel]] (block + energy on exhaust)
- [[cards/Feel No Pain]] (3 block per exhaust. Enables Corruption engine; also good standalone with True Grit, Fiend Fire, or any exhaust source. Under investigation as a high-priority pick — see exploration directives.)

**SKIP** (do not take in Act 1 unless noted):
- Demon Form (too slow for hallway fights, does not satisfy front-loaded damage scaling)
- [[cards/Limit Break]] (needs a Str source first)
- [[cards/Barricade]] (3E, too slow, no immediate value -- but take from boss card rewards if building block engine)
- [[cards/Corruption]] (3E, dangerous without [[cards/Feel No Pain]]. Under investigation: may be worth taking if FNP is already in deck, but needs more data — see exploration directives.)
- [[cards/Brutality]] (self-damage in long fights)
- [[cards/Berserk]] (self-Vulnerable is extremely dangerous)

**Boss-specific overrides (APPLY BEFORE tier list):**
- Slime Boss visible: Evolve and Fire Breathing become MUST-TAKES
- [[bosses/Hexaghost]] visible: Weak sources (Shockwave, Clothesline, [[cards/Intimidate]]) become MUST-TAKES. A Weak source outranks ANY generic tier list pick -- take Clothesline over Pommel Strike, take Intimidate over Iron Wave, etc. Without Weak, Hexaghost's Inferno and Tackles deal full damage for 16+ turns. No amount of block cards compensates.
- [[bosses/The Guardian]] visible: Burst damage for [[buffs/Mode Shift]] (Carnage, [[cards/Bludgeon]])

**Elite-specific overrides:**
- [[enemies/Gremlin Nob]]: Take attacks, not skills. Nob gains +2 Str per Skill you play.
- Slavers in Act 2: AOE and mass debuff are critical for 3-enemy fight.
- Book of Stabbing in Act 2: Exhaust tools for Wound removal.

---

## Draft for Known Encounters

You see the boss from Floor 1. You know which elites exist in each act. Evaluate cards against fights you are GUARANTEED to face, not generically.

The boss is visible on the map from the start. Every card pick, relic choice, and deck-building decision should account for that specific boss matchup. A card that is mediocre in isolation but strong against your boss is worth more than a generically powerful card that does not address the boss threat.

After Act 1, shift from the tier list to gap-filling based on the Act 2 Readiness Checklist.

---

## Take Cards That Solve Problems

A card's value depends on what the deck needs RIGHT NOW and what fights are coming next.

Before taking a card, ask:
1. Do I have a healing card? (If no, #1 gap)
2. Do I have a damage scaling path? (If no, #2 gap -- Str sources are proven; Corruption+FNP is a promising alternative under investigation)
3. Do I have AOE? (If no, #3 gap -- Gremlin Leader and 3 Cultists will kill you)
4. Do I have block scaling beyond basic Defends? (If no, #4 gap -- Hyper Beam will kill you. Note: Corruption+FNP also fills this gap.)
5. Does this card help against my boss?

A mediocre card that fills a gap is better than a strong card that duplicates what you already have.

---

## Damage Scaling Is Mandatory

[[enemies/Spheric Guardian]] has Barricade -- its block never expires and grows 15-20 per defend cycle. At 0-1 Strength with no scaling engine, Strikes deal 6-7 damage per play against 15-20 block gained per cycle. The fight is unwinnable without some form of damage scaling.

**By Floor 15, the deck MUST have a scaling path.** Either:

**Path A -- Strength scaling:**
1. Inflame (+2 Str permanent, 1E) -- best standalone option
2. Spot Weakness (+3/+4 Str when enemy attacks, 1E) -- excellent but conditional
3. [[relics/Brimstone]] relic (+2 Str/turn to you AND enemies) -- run-defining when acquired early (see brimstone.md). Pairs exceptionally well with Reaper.
4. Limit Break (doubles current Str) -- only if another Str source exists to double
5. Demon Form (+2 Str/turn, 3E) -- too slow for hallway fights but works for bosses
6. [[relics/Vajra]] relic (+1 Str) -- passive, always on

**Path B -- Exhaust/Block engine (under investigation):**
1. [[cards/Corruption]] + [[cards/Feel No Pain]] -- core combo. FNP generates block on each exhausted Skill; Corruption makes all Skills free but one-use. Together they produce massive block per turn. Add [[cards/Body Slam]] to convert block to damage.
2. [[cards/Barricade]] -- block persists, so the engine snowballs. Not required early but completes the engine.
3. [[cards/Entrench]] -- doubles accumulated block. With Barricade, this is exponential growth.

These paths are not mutually exclusive. Run 187 won with Corruption+FNP primary and Spot Weakness secondary. Run 104 won with the full Barricade+Corruption+FNP+Body Slam engine. Both winning runs ALSO had Strength sources. Whether the exhaust/block engine can win purely on its own (without any Str) is being tested — see exploration directives. What IS clear: a deck cannot survive without SOME scaling path.

**Card reward priority when the deck has NO scaling path:**
Inflame > Spot Weakness > Corruption (if FNP available or likely) > Feel No Pain (if Corruption available or likely) > Limit Break (with Str source) > anything.

---

## Curse Management

Curses are removable at shops for 75g (except Parasite, which cannot be removed).

**When an event offers gold + a curse, check the map:**
- **Shop within 2-3 floors:** Take the gold + curse, remove at shop. Net profit after 75g removal. [[events/Sssserpent]] (175g + Doubt curse) nets 100g profit.
- **No shop before boss/elite:** Refuse. A curse stuck in the deck for 5+ floors degrades draw quality and costs HP in hard fights.
- **Parasite: Never take.** Cannot be removed at shops. No exceptions unless [[relics/Omamori]] will negate it.

Evaluate the map context, not just the curse itself.

---

## Deck Thinning

Remove Strikes at shops and events. A 10-12 card deck draws key cards much more reliably than a 15+ card deck.

Remove Strikes before Defends. Strikes get outclassed faster by better attacks; Defend's 5 block stays relevant longer.

---

## Multi-Purpose Cards Win

The winning formula across all victories: cards that do two things.

- Block + draw: Shrug It Off
- Damage + draw: Pommel Strike
- Damage + block: Iron Wave
- Damage + heal: Reaper
- Damage + deck manipulation: Headbutt

Single-purpose cards (Strike, Defend) are the weakest cards in the deck. When choosing between a single-purpose card and a dual-purpose card of similar power level, always take the dual-purpose card.

---

## 3-Cost Power Setup Trap

[[cards/Corruption]] (3E), Barricade (3E), Demon Form (3E) consume ALL energy on a 3-energy turn. Playing them on Turn 1 against attacking enemies leaves zero energy for block. Two deaths confirmed from this pattern.

**Only play 3E Powers when:**
- Enemy is buffing/defending (free turn with no incoming damage)
- You have 4+ energy (from [[relics/Lantern]], [[relics/Sozu]], [[cards/Offering]], etc.), leaving energy for block
- You upgraded the Power to 2E (Corruption+ is 2E, leaving 1E for Defend)
- It is a boss fight where spending HP for setup speed is acceptable

**Do NOT play 3E Powers when:**
- Any turn with incoming damage in a hallway fight
- Turn 1 against multi-enemy fights (combined damage 15-25+)
- The Full Block Flowchart shows no path to zero damage after spending 3E

---

## Slow Scaling Engines

Demon Form (+2 Str/turn) and Limit Break (double Strength) are powerful in long fights but require 2-3 setup turns before providing meaningful value. They solve bosses but NOT hallway fights.

Against fast-scaling enemies at low HP (3 Cultists, multi-enemy fights), setup time does not exist. The player is dead before the engine comes online.

**Rule:** If primary scaling is Demon Form or Limit Break, MUST have an alternative fast-burst plan for hallway fights. Slow engines are for bosses. Hallway fights need cards that contribute to Full Block paths on the turn they are drawn.

---

## Backup Healing Plan

Activate by Floor 17 if no healing card has been acquired. Do not wait until HP is critical.

1. **Shop healing:** Buy Blood Potion or Regen Potion at every shop. Buy Toy Ornithopter or Meal Ticket if offered.
2. **Event healing:** [[events/The Cleric]] heals. [[events/Big Fish]] offers healing. [[events/Woman in Blue]] sells potions. Prioritize these events.
3. **Path through more rest sites:** Without healing cards, rest sites become the primary healing source. Accept fewer upgrades. Degraded strategy but better than dying.
4. **Potion management:** Treat Blood Potions and Regen Potions as precious resources. Do not use them in trivial fights.
5. **Conservative pathing:** Take safer paths, skip elites after Floor 15, avoid Unknown rooms below 50% HP.

The absence of healing cards does NOT mean the run is lost. It means Full Block discipline becomes even more critical and map pathing must be more conservative.
