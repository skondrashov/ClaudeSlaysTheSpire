# Strategy

High-level strategic principles for Ironclad runs.

**CURRENT BOTTLENECK (110-run milestone):** Surviving Act 2 boss fights. The F25-26 plateau is BROKEN -- two consecutive Act 2 boss reaches (Runs 105 and 110, both Floor 33). The 4-criteria readiness checklist is working: decks are arriving at the boss well-prepared. The failures are now boss-specific: Run 105 died to Bronze Automaton (block scaling gap -- only basic Defends vs 38-damage Hyper Beam). Run 110 died to The Collector (57% HP entry vs required 70% -- Colosseum event drained HP before boss). Two key cards are disproportionately important for Act 2 boss survival: Impervious (absorbs the biggest hit of any boss fight) and Shockwave+ (mass debuff reduces combined incoming from multi-enemy bosses by 25%).

**SCORECARD (runs 101-110):**
- Act 1 boss wins: ~80% -- Run 103 died to Guardian F16 (Pandora's Box removed all Defends), Run 107 died to Guardian F16 (Corruption+ exhausted block Skills -- now Hard Rule #9)
- Act 2 boss reaches: 2 (Runs 105 and 110, both Floor 33) -- BREAKTHROUGH
- Act 2 hallway deaths: reduced from prior batches
- Bronze Automaton: 1 death (Run 105 -- block scaling gap, only basic Defends)
- The Collector: 1 death (Run 110 -- 57% HP entry, missing Impervious and Shockwave+)
- Hard Rule violations: 0
- Best floor: 39 (Run 63) -- unchanged but system is now reliably reaching F33
- Shop indexing bug: FIXED. Boss relic skip bug: UNRESOLVED (2 occurrences, not seen in 101-110)
- MILESTONE: Two consecutive Act 2 boss reaches confirm the 4-criteria readiness system works. Bottleneck has shifted from Act 2 hallways to Act 2 boss fights.

**IMMEDIATE PRIORITIES (in order):**
1. **Trace full paths before every map choice.** Before choosing any path, trace EVERY option forward to the next rest/shop. Count forced combats. Choose fewer combats. This is the #1 structural fix -- the majority of deaths result from entering fights at sub-threshold HP because the path forced consecutive combats. Say the count aloud: "Path A: 3 combats to rest. Path B: 1 combat to rest."
2. **Do NOT buy Brimstone if Book of Stabbing is a possible Act 2 elite.** Brimstone + Book of Stabbing has killed the player twice. The anti-synergy makes Book of Stabbing damage grow quadratically (more hits * more damage per hit). If already holding Brimstone, AVOID Book of Stabbing entirely.
3. **Build Act 2-ready decks by Floor 15.** The deck needs ALL FOUR: (a) front-loaded Strength (Inflame or Spot Weakness, NOT Demon Form alone), (b) AOE (Thunderclap, Cleave, Immolate, Whirlwind), (c) healing beyond Burning Blood, (d) block scaling beyond basic Defends (Shrug It Off, Flame Barrier, Metallicize, Ghostly Armor, Impervious, or True Grit+). Run 105 proved that (a)+(b)+(c) alone is insufficient -- Hyper Beam (38+ damage) is unsurvivable with only basic Defends (4x5=20 block). If missing any by Floor 12, actively seek it in remaining card rewards, shops, and events.
4. **3 Cultists threshold is 60%, not 50%.** Five deaths at 30-53% HP confirm that even strong block tools cannot survive Ritual scaling. Kill speed (AOE burst to remove one Cultist fast) matters more than defensive tools.
5. **Have Strength scaling by Floor 15** (Inflame > Spot Weakness > Limit Break). Spheric Guardian and other high-block enemies are mathematically unwinnable without it.

---

## HP Management: The #1 Cause of Death

24+ of 30+ documented deaths resulted from entering a fight below safe HP thresholds or making a fatal tempo error (playing a 3E Power with no block). The pattern is always the same: a drain fight takes 30-50 HP, the next room is combat, and the player dies. Or: the player spends all energy on a Power and takes full unblocked damage.

### HP Thresholds for Act 2

| Fight Type | Minimum HP | Notes |
|---|---|---|
| Hallway (easy) | 25% | Byrds/Chosen can still drain 40-60 HP |
| Hallway (hard) | 60% | 3 Cultists (6 deaths, even 53% was insufficient), Centurion+Mystic, Snake Plant |
| Elite | 60% | Gremlin Leader, Book of Stabbing, Slavers |
| Boss | 70% or Pantograph | Act 2 boss has massive damage |

**CRITICAL: 3 Cultists is the most lethal hallway fight in the game (6 deaths confirmed at 5%, 30%, 37%, 39%, 52%, 53% HP entry).** Triple independent +3 Str/turn = +9 combined Str/turn. Even decks with Impervious+, Calipers, Immolate, Shockwave+ failed at 53% HP because Ritual scaling outpaces all defensive tools -- kill speed (AOE burst to eliminate one Cultist fast) matters more than block density. The 60% threshold for this encounter is NON-NEGOTIABLE. Run 112's death at 5% HP was caused by Snake Plant draining 42 HP on the prior floor -- the fight was lost at map pathing, not in combat.

### What to Do at Low HP

- Below the threshold for the next fight? Take a DIFFERENT PATH. Event rooms, rest sites, shops -- anything but combat.
- If forced into a fight below threshold, use ALL potions aggressively on turn 1. Don't save them for "later" -- there may not be a later. This includes Strength Potions: +2 damage per attack over a 5-turn fight is 10-20 extra damage, which is 2-4 fewer turns of incoming damage. An unused potion on a death screen is a strategic failure.
- If there's a rest site before an elite, REST (don't upgrade). HP > upgrades when below threshold.
- After any fight that drops you below 30% HP, the next room MUST be a rest site, shop, or event -- not combat.

### The Act 2 Death Spiral Is Predictable

The pattern across 10 low-HP deaths: the player enters Act 2 at reasonable HP, loses 30-50 HP in one brutal fight (Byrds, Centurion+Mystic, Cultist+Chosen, Looter+Mugger), then enters the NEXT fight at critical HP and dies. The mistake is not the first fight -- it's taking a second combat room immediately after. After ANY fight that leaves you below 30% HP, the next room MUST be non-combat. If the map doesn't offer this, the run was lost at map selection, not at the fight.

Even "hallway" fights in Act 2 can be run-ending: 3 Cultists has killed the player three times at 30-39% HP entry. These are not elites -- they appear on normal Monster nodes. The only defense is entering with sufficient HP or having a path that avoids consecutive combat rooms.

**Act 2 decision point:** After each fight, if HP is below 35%, evaluate the ENTIRE remaining path. If it contains 2+ consecutive combat rooms before a rest site, consider abandoning elites and taking the safest available path even if it means missing rewards.

### What Causes the HP Drain

1. **Byrd fights**: 36-58 HP lost per fight. Flight makes fights 8-12 turns. The primary Act 2 HP drain. Without Thunderclap (mass Flight stripping + Vulnerable), expect the upper end. Thunderclap is the single most important card for Act 2 Byrd survival.
2. **Centurion+Mystic**: 25-42 HP lost per fight. Mystic's healing extends the fight. Often consumes Fairy in a Bottle.
3. **Snake Plant in Unknown rooms**: 21 HP/turn with Frail debuff. Drains 20-42 HP depending on Strength scaling (Run 112: 42 HP drained with zero Strength scaling despite correct play -- single large hits, Bash+ Vulnerable). Without Strength scaling, the fight extends to 7 turns and Weak+Malleable reduce each hit to 3-6 effective damage. Unknown rooms can become Snake Plant fights -- they are NOT safe at low HP.
3b. **Spheric Guardian + Sentry from Unknown rooms**: 29 combined damage/turn with Frail 5 reducing block. Spheric Guardian's Barricade block makes Reaper useless and chip damage futile. Three deaths confirmed from this encounter (at 26%, 43%, and 100% HP entry). The third death occurred at FULL HP -- even 87/87 was insufficient because Brutality self-damage and Rage+ expiring at end of turn left no survival path after 6 turns. Unknown rooms are the most dangerous room type in Act 2 at any HP level when this fight spawns.
4. **No healing between fights**: Burning Blood (+6) cannot compensate for 30-50 HP fights.
5. **Fairy consumed in wrong fight**: In multiple runs, Fairy was consumed in Centurion+Mystic, leaving no safety net for elites. Save Fairy for elites/bosses when possible.
6. **Decay curse compound damage**: Each Decay in hand deals 2 unblockable damage per turn. With 2 Decays, that is 4 HP/turn lost regardless of block. Over a 5-turn fight, that is 20 free HP lost. Prioritize curse removal at shops or via exhaust (Fiend Fire).
7. **Vampires event Max HP loss**: Accepting the Vampires event removes ~30% of Max HP (observed: 80->56). At 56 Max HP, every HP threshold in the table above shifts drastically -- 60% for elites becomes 34 HP, which is nearly impossible to maintain through Act 2. The 5 Bite cards provide 2 HP healing per play but cannot compensate for the reduced HP ceiling against burst damage. Refuse this event unless desperate for healing with no alternatives.

---

## Rest Site Decisions

### Upgrade vs Rest Framework

**Upgrade** when:
- HP is above 50% in Act 2 (above 35% in Act 1)
- A critical upgrade target exists (Bash, True Grit, Limit Break, key attack card)
- Earlier is better: one upgrade on floor 8 benefits 20+ fights

**Rest** when:
- HP is below 50% in Act 2 (below 35% in Act 1)
- Next room is a known elite or boss AND you are below 60% HP
- The path ahead contains 2+ combat rooms before the next rest site AND you are below 50%

### The Upgrade Death Spiral

Zero upgrades in an entire run is a death sentence. Even one missed upgrade makes fights harder, which drains more HP, which forces more resting, which means more missed upgrades. This has now been observed three times: once with only 1 upgrade across 28 floors, once with literally ZERO upgrades across 23 floors, and once in Run 70 where ZERO upgrades occurred until Floor 15 (both rest sites consumed by healing due to critically low HP from fights with unupgraded cards). All three runs died with decks that had adequate card quality but no upgraded cards to back it up.

**The spiral is self-reinforcing:** unupgraded cards mean fights take longer and deal more damage, which forces resting instead of upgrading, which keeps cards unupgraded. In Run 70, the deck had good cards (Dropkick, Clothesline, Feel No Pain, Disarm, Burning Pact, Ghostly Armor) but zero upgrades made every fight drain more HP than necessary, creating the exact spiral described here.

**MANDATORY RULE: Upgrade at EVERY rest site where HP is above the rest threshold (35% Act 1, 50% Act 2).** If no upgrade has been performed by Floor 10, something is seriously wrong -- the player is either resting unnecessarily or skipping rest sites. Bash should be upgraded by Floor 8 at the latest. If FORCED to rest at the first rest site due to low HP, the deck is already in danger -- path to the next rest site urgently and upgrade there no matter what.

### Upgrade Priority

1. Bash (3 Vulnerable vs 2 is massive)
2. Corruption (3E -> 2E is life-or-death -- one confirmed kill from unupgraded Corruption setup)
3. True Grit (CHOSEN exhaust vs RANDOM is game-deciding)
4. Armaments (upgrade 1 card -> upgrade ALL cards in hand -- transformative)
5. Carnage (28 vs 20 damage)
6. Iron Wave (7/7 vs 5/5)
7. Pommel Strike (10 damage + draw 2 vs 9 + draw 1)
8. Thunderclap (7 vs 4 AOE)
9. Shrug It Off (11 vs 8 block)
10. Headbutt (12 vs 9 damage)
11. Defend (8 vs 5 block -- low individual priority but Ancient Writing mass upgrade is excellent)

**Context-dependent overrides:** If Corruption is your engine piece, upgrade it above Bash. If you already have Bash+, move to the next unupgraded priority. The list is a default -- always upgrade the card that will save the most HP in the next 5 fights.

---

## Deck Building Philosophy

### Healing Card Priority (THE CRITICAL GAP)

The single biggest strategic failure across 50 runs: entering Act 2 without a healing card. Burning Blood (+6/fight) heals 6% of max HP per fight. Act 2 fights drain 25-50 HP (30-60% of max). The math does not work.

**Card reward priority when offered a healing card:**
- Reaper: TAKE IT. Even over good damage/block cards. It is the best card in the game for Ironclad.
- Feed: TAKE IT in the first half of Act 1. +3-4 Max HP per kill compounds over 15+ fights. Less urgent in late Act 1.
- If neither is offered by Floor 12, actively seek healing potions (Blood Potion, Regen Potion) and healing relics (Toy Ornithopter, Meal Ticket, Bloody Idol) at shops.

**This is non-negotiable.** A deck with Reaper + adequate damage will reach Act 3. A deck with perfect damage/block but no healing will die in Act 2 floors 20-30.

### Act 2 Readiness Checklist (verify before Floor 17)

By the time the Act 1 boss is dead, the deck needs ALL FOUR of these or it will die in Act 2:

1. **Front-loaded Strength**: Inflame, Spot Weakness, or Corruption+FNP engine. NOT Demon Form alone (too slow for hallway fights -- confirmed in 2 SG deaths). If no Strength source exists by Floor 12, take the next one offered over any other card.
2. **AOE damage**: Thunderclap, Cleave, Immolate, or Whirlwind. Required for Gremlin Leader (gremlins re-summon, AOE clears them efficiently), Slime Boss split, and 3 Cultists. Two Gremlin Leader deaths had zero AOE.
3. **Healing beyond Burning Blood**: Reaper, Feed, or multiple healing potions/relics. Burning Blood (+6/fight) cannot offset 30-50 HP Act 2 fights.
4. **Block scaling beyond basic Defends**: Shrug It Off, Flame Barrier, Metallicize, Ghostly Armor, Impervious, or True Grit+. Basic Defends provide only 5 block each (20 block from a full hand of 4). Act 2 boss Hyper Beam deals 38-45 damage -- unsurvivable with basic Defends alone. Even Act 2 hallway fights (Book of Stabbing turn 5: 6x6=36) outscale basic Defends. Run 105 had criteria 1-3 fully met but died to Hyper Beam because the deck's only block was 4 basic Defends. **Impervious is the highest-priority block scaling card** -- 30 block (40 upgraded) handles the biggest hit from ANY Act 2 boss. If Impervious is offered, take it.

If missing 2+ of these entering Act 2, the run is in serious danger. Shift to conservative pathing (avoid elites, path through shops and rest sites, skip unknown rooms).

### Take Cards That Solve Problems

A card's value depends on what your deck needs RIGHT NOW.

Before taking a card, ask:
- Do I have a healing card? (If no, this is the #1 gap to fill)
- Do I have Strength scaling? (If no, this is the #2 gap to fill -- see below)
- Do I have AOE? (If no, this is the #3 gap -- Gremlin Leader and 3 Cultists will kill you)
- Do I have block scaling beyond basic Defends? (If no, this is the #4 gap -- Hyper Beam and late Book of Stabbing will kill you. Shrug It Off, Flame Barrier, Metallicize, Ghostly Armor, Impervious, True Grit+)
- What fights am I struggling with?
- Will this card dilute my draws (bigger deck = less likely to draw key cards)?

A mediocre card that fills a gap is better than a strong card that duplicates what you already have.

### Strength Scaling Is Mandatory for Act 2

Spheric Guardian (the single most dangerous Act 2 hallway fight, 3 deaths confirmed) has Barricade -- its block never expires and grows 15-20 per defend cycle. At 0-1 Strength, Strikes deal 6-7 damage per play against 15-20 block gained per cycle. The fight is mathematically unwinnable without Strength scaling.

**By Floor 15, the deck MUST have at least one Strength source:**
- Inflame (+2 Str permanent, 1E) -- best standalone option
- Spot Weakness (+3/+4 Str when enemy attacks, 1E) -- excellent but conditional
- Demon Form (+2 Str/turn, 3E) -- too slow for hallway fights but works for bosses
- Limit Break (doubles current Str) -- requires a Str source to double
- Vajra relic (+1 Str) -- passive, always on
- Strength Potion (+2 Str) -- temporary but bridges the gap

**Card reward priority when the deck has NO Strength scaling:**
Inflame > Spot Weakness > Limit Break (if other Str source exists) > any other card.

This is nearly as important as healing. A deck with block + healing but no Strength scaling will die to Spheric Guardian's Barricade every time.

### Deck Thinning

Remove Strikes at shops and events. A 10-12 card deck draws key cards much more reliably than a 15+ card deck. Remove Strikes before Defends (Strikes get outclassed faster; Defend's 5 block stays relevant).

### Multi-Purpose Cards Win

The winning formula across all victories: cards that do two things. Block+draw (Shrug It Off), damage+draw (Pommel Strike), damage+block (Iron Wave), damage+heal (Reaper), damage+deck manipulation (Headbutt). Single-purpose cards (Strike, Defend) are the weakest cards in the deck.

### Slow Scaling Engines Are a Deck Weakness

Demon Form (+2 Str/turn) and Limit Break (double Strength) are powerful scaling cards in long fights -- but they require 2-3 free setup turns before providing meaningful value. Against fast-scaling enemies at low HP (3 Cultists, multi-enemy fights), this setup time does not exist. The player is dead before the engine comes online.

**Pattern:** A deck built around Demon Form + Limit Break can beat bosses comfortably but die to hallway fights when entered at low HP. The fix is NOT to avoid these cards -- it is to recognize that they solve long fights (bosses) but do NOT solve emergency situations. The deck still needs immediate burst (Fiend Fire, Rampage, Immolate) and block density for fights where you cannot afford 2 turns of setup.

**Rule:** If your primary damage scaling is Demon Form or Limit Break, you MUST have an alternative fast-burst plan for emergencies. Do not enter fights below 50% HP relying solely on a slow engine.

### 3-Cost Power Setup Trap

Corruption (3E), Barricade (3E), and Demon Form (3E) are all powerful cards that consume ALL energy on a 3-energy turn. Playing them on turn 1 against attacking enemies leaves zero energy for block. Two deaths and one near-miss confirm this pattern:
- Run 73: Corruption (3E) into Looter + Mugger. Zero block. 20+ unblocked damage. Dead.
- Run 72: Barricade (3E) was never played because no turn was safe enough to spend all energy.

**When to play 3E Powers:**
- Enemy is buffing/defending (free turn with no incoming damage)
- You have 4+ energy (from relics like Lantern, Sozu, or cards like Offering)
- You have enough HP to absorb the full unblocked hit AND still survive subsequent turns
- You upgraded the Power to 2E (Corruption+ is 2E, leaving 1E for Defend)

**When NOT to play 3E Powers:**
- Turn 1 against multi-enemy fights (combined damage 15-25+)
- Any turn where blocking is survival-critical
- When you cannot afford to take a full unblocked hit

This is now Hard Rule #8.

### Unknown Card Evaluation

- **Skip** unknown cards with self-damage, self-debuff, or suspicious keywords ("lose," "take damage," "Vulnerable to self," curses).
- **Take** unknown cards that seem purely beneficial (damage + heal, damage + draw, block + effect). The upside outweighs the risk.
- **Especially take** unknown cards that fill a known gap in your deck.

---

## Boss Preparation

### Pre-Boss Checklist (Verify by Floor 12-15)

Before the Act 1 boss, verify ALL THREE:
1. A card that addresses the specific boss threat
2. A sustain/passive defense source (Metallicize, Plated Armor, Pantograph, or high HP)
3. Enough HP (60%+ without Pantograph)

If you have 0-1 of these, the boss will likely kill you. Adjust card picks in remaining floors.

### Boss-Specific Requirements

**Slime Boss needs:**
- AOE for the split (Thunderclap, Whirlwind, Cleave) -- MANDATORY. If no AOE has been offered by Floor 12, actively seek it at shops or events. Without AOE, the Slime Boss fight is near-unwinnable because post-split enemies generate Slimed cards faster than single-target damage can clear them.
- Burst single-target to kill one slime fast (Fiend Fire)
- Exhaust for Slimed cards (Burning Pact, Feel No Pain, True Grit+)
- Manage pre-split damage: aim to trigger the split as close to 70 HP as possible. Excess damage past the threshold is wasted.

**The Guardian needs:**
- 32+ block capability in one turn (Impervious, double Metallicize + Weak)
- Burst damage for Mode Shift (Bludgeon at 32-48, Carnage+ at 28-42)
- Enough cards to last 12+ turns (do NOT over-exhaust)
- **Avoid exhaustion-heavy strategies.** Fiend Fire + Dark Embrace creates a thin deck by mid-fight. Block density on 32-damage turns (turns 8-12) drops below survivable thresholds when the deck thins to 8-10 cards. Use Fiend Fire on free turns or for burst, never as the primary deck engine.
- **Do NOT play Corruption/Corruption+ without Dead Branch or Feel No Pain.** Run 107: Corruption+ played turn 9, all Skills exhausted by turn 14, died at Guardian 10/240 HP with zero block cards remaining. Corruption is a trap in 14-turn fights -- the energy savings do not compensate for losing all block in the second half. This is now the SECOND Guardian death from block-density collapse (Run 103: Pandora's Box, Run 107: Corruption+).

**Hexaghost needs:**
- Weak source (Shockwave, Clothesline, Intimidate, Weak Potion) -- MANDATORY
- Damage scaling (Rampage, Inflame) -- kill before Burns overwhelm (insufficient damage killed 2 runs despite having Weak)
- Passive block (Metallicize) for the 13-turn fight
- Turn 1 setup (Thunderclap for Vulnerable)
- No self-damage cards (Brutality, Berserk)

**The Collector needs:**
- HP entry at 70%+ or Pantograph -- STRONG_DEBUFF on Turn 4 applies Vulnerable 3, Frail 3, Weakened 3 simultaneously. Pantograph heals 25 HP at boss start, which helps but does NOT bypass the threshold if you enter more than 25 HP below max.
- AOE damage (HIGHEST PRIORITY) -- Immolate+ is the single best card. Hits Collector + both Torch Heads. With Vulnerable: 42 damage to Collector per cast. Torch Heads respawn, so AOE is more valuable than single-target.
- Mass debuff -- Shockwave+ (Weak 3 + Vuln 3 to ALL enemies) reduces combined incoming by 25% while boosting all damage by 50%. Second-highest priority.
- Impervious -- 30 block absorbs post-debuff turns. Critical defensive card.
- Disarm -- permanent Str reduction compounds over the 10-turn fight. Play Turn 1.
- Block density for post-debuff turns -- Frail reduces block by 25%, need multiple sources

**Bronze Automaton needs:**
- HP entry at 70%+ or Pantograph -- 300 HP boss with +3 Str/cycle scaling. Run 105 entered at 92/92 (Pantograph) and still died -- HP alone is insufficient without block scaling.
- **Block scaling (MANDATORY)** -- Hyper Beam deals 38-45 damage. Basic Defends (4x5=20 block) are NOT enough. Need Shrug It Off, Flame Barrier, Metallicize, Impervious, or Ghostly Armor. Run 105 died specifically because the deck had zero block scaling cards. This is the #1 requirement.
- Artifact strippers -- Thunderclap+, Bash+, Shockwave+. Automaton starts with Artifact 3. Run 105 stripped all 3 Artifacts by turn 3 using Thunderclap+ (x2) + Bash+. Shockwave+ then applied Weak 3 + Vuln 3 successfully on turn 4.
- Burst damage -- Fiend Fire+, Rampage, Bludgeon. The fight is a DPS race against Strength scaling. Kill before turn 10 if possible.
- Weak source -- Shockwave+ reduces Hyper Beam by 25% (38->28). Critical for survival. Must land AFTER Artifact is stripped.
- Redundant key cards -- Orb minions steal cards via Stasis. Do not rely on a single copy of any critical card (Fiend Fire, Shockwave+).
- Intent visibility -- Runic Dome removes the ability to predict Hyper Beam. Avoid taking Runic Dome if Bronze Automaton is a possible Act 2 boss.
- **Odd Mushroom anti-synergy** -- Odd Mushroom reduces Vulnerable from 1.5x to 1.25x, cutting burst by ~17%. In a DPS race against 300 HP + Strength scaling, this extends the fight by 1-2 turns, potentially forcing survival through an extra Hyper Beam cycle.

**Donu and Deca needs (NOT YET ENCOUNTERED):**
- AOE damage (Immolate+, Thunderclap+) -- two 250 HP enemies
- Disarm -- reduce Donu's Strength before killing it
- Shockwave+ -- mass Weak+Vulnerable on both
- Block density for 10+ turn fight
- Kill Donu first (prevents Strength scaling for both)

### Act 2 Boss Survival (THE NEW BOTTLENECK)

The system now reliably reaches Act 2 bosses. The challenge is surviving them. Two deaths (Runs 105 and 110) reveal the requirements:

**Key cards for Act 2 boss survival (prioritize in Act 2 card rewards and shops):**
1. **Impervious** -- The single most impactful defensive card for Act 2 bosses. 30 block (40 upgraded) absorbs Hyper Beam (38 dmg), Collector post-debuff turns (37+ dmg), and Champ Execute burst. Both Act 2 boss deaths (Runs 105, 110) would have been different with Impervious in the deck. If offered in Act 2, TAKE IT over almost any other card.
2. **Shockwave+** -- Mass Weak 3 + Vuln 3 to ALL enemies. Reduces combined incoming from multi-enemy bosses (Collector + Torch Heads, Automaton + Orbs) by 25% for 3 turns while boosting all damage by 50%. The highest-value single play in Act 2 boss fights.
3. **Disarm** -- Permanent Strength reduction. Play Turn 1 against Collector or Champ for maximum cumulative value.

**Pre-boss HP preservation (last 2-3 floors before Act 2 boss):**
- The 70% HP threshold for Act 2 bosses is NON-NEGOTIABLE. Run 110 died because Colosseum event drained HP to 57% before the boss.
- Treat Unknown rooms in the last 2-3 floors before the boss as potential HP drains (Colosseum forces combat, Juzu Bracelet does NOT prevent it).
- Rest over upgrade if below 70% HP at the pre-boss rest site. The upgrade is worthless if you die to the boss.
- Skip card rewards and event risks in the last 2-3 floors. HP preservation is the only priority.

### Save One-Use Cards for Bosses

Exhaust cards like Shockwave+ are single-use per combat. Don't waste them on hallway fights unless the fight is genuinely dangerous. The boss is almost always the hardest fight.

### Use Potions at Boss Start

Stat-boost potions (Strength, Speed, Essence of Steel) provide maximum value when used turn 1 of a boss fight. Powers from Power Potion are permanent for the combat. Don't hoard potions -- use them.

---

## Shockwave+ Timing Rule

**Play Shockwave+ on the FIRST ATTACK TURN of multi-enemy fights.**

- Turn 1 is NOT always right: if all enemies are buffing (Cultists turn 1), Weak is wasted.
- Turn 2 is usually correct: attacks start here for most multi-enemy fights.
- NEVER save for turn 4+: enemies have already accumulated Strength by then. Early Weak saves more HP than late Weak.

Priority on first attack turn: Shockwave+ (mass Weak+Vuln) > Reaper (healing) > single-target damage. Preventing damage with Weak > healing damage already taken.

---

## Exhaust Strategy

### The Power and the Limit

Exhaust synergy (Dark Embrace draw + Charon's Ashes 3 AOE) is a strong engine. But there's a critical breakpoint: once the deck is too thin, you can't survive big attacks.

### Before Exhausting, Ask:

1. Can my remaining deck survive the enemy's biggest attack? Calculate max block from remaining block cards.
2. Is the card truly expendable? Strikes and Defends early -- yes. Core damage/block cards -- never.
3. Am I in the first half of the fight (thin = good) or second half (thin = fatal)?

### Random Exhaust Is Run-Ending

Unupgraded True Grit and Havoc both cause RANDOM exhaust -- you cannot control which card is lost. In a deck with even one irreplaceable card (Rampage+, Fiend Fire+, Feed+, Bash+), random exhaust is a coin flip that can destroy the run. Havoc exhausted Rampage+ in one fight; unupgraded True Grit exhausted Fiend Fire+ in another -- both in the same run, directly causing death.

**Rule: Never play Havoc or unupgraded True Grit when the deck contains cards you cannot afford to lose.** If you must take True Grit, upgrade it IMMEDIATELY. If you cannot upgrade it, do not play it. Havoc should not be taken in any deck with irreplaceable scaling cards.

### Safe Exhaust Targets
- Strikes (once better attacks exist)
- Extra Defends
- Status cards (Slimed, Wound, Burn, Dazed)

### Never Exhaust
- Last copy of your best damage card
- Last copy of a high-block card
- Core combo pieces (Bash+ when Vulnerable matters)

### The Long Fight Problem

Exhaust cards front-load power into the first 5 turns. After that, the deck plays like a basic starter deck. Against scaling enemies (Gremlin Leader rallies, Cultist Ritual), the first 5 turns aren't enough, and the remaining deck can't handle scaled enemies. If 30%+ of the deck exhausts/is Ethereal, the fight MUST be won in 5-6 turns.

### Fiend Fire + Unceasing Top Engine

Exception to the long fight problem: Fiend Fire + Unceasing Top creates a sustained draw engine. After Fiend Fire exhausts hand, Top draws a card. Play it, hand empties, draw again. This cycles through the draw pile in one mega-turn. With energy from Bloodletting/Offering, this can deal 50-100+ damage in a single turn while generating block from Rage. This is currently the strongest combo observed for Ironclad.

---

## Map Pathing

### Core Principles

- **MANDATORY PATH TRACE: Before choosing ANY path, trace EVERY available option forward to the next rest site or shop.** Count the number of forced combat rooms on each path. Choose the path with the fewest forced combats between here and the next healing opportunity. This single practice prevents the majority of death-spiral entries. Do NOT just look at the next room -- trace the FULL path.
- **Look 2-3 floors ahead, not just the next room.** At EVERY map node, trace paths forward. If a path leads to 2+ consecutive combat rooms with no rest/shop/event between them, that path is dangerous at any HP below 70%. Three deaths (Runs 20, 21, 22) were caused by map topology forcing combat after a drain fight.
- Prefer routes with a rest site in the last 1-2 floors before the boss.
- After a brutal fight (Byrds, Centurion+Mystic), next room MUST be healing, not another combat.
- If the path forces an elite at low HP, skip it entirely -- take any alternative path.
- **Unknown rooms are NOT safe in Act 2.** They can resolve as any hallway fight, including Byrds, Snake Plant, and Spheric Guardian + Sentry. THREE deaths confirmed from Spheric Guardian spawning from Unknown rooms (at 26%, 43%, and 100% HP). The third death occurred at FULL HP -- even 87/87 was not enough. Treat Unknown rooms as Monster rooms when routing in Act 2. Only take Unknown rooms in Act 2 if the deck has Strength scaling and the alternative path is worse.

### Elite Risk Assessment

Before fighting an elite, check:
1. **HP threshold**: Below 30 HP for Act 1 elites is dangerous. Below 60% for Act 2 elites is dangerous.
2. **Deck vs elite matchup**: Gremlin Nob punishes Skill-heavy decks. Lagavulin punishes slow decks. Sentries need AOE.
3. **Potions available**: Potions compensate for bad matchups.
4. **Path alternatives**: If a safer path exists with similar value, take it.

**Act 2 Elite Threat Ranking:**
- **Book of Stabbing** (3 deaths, now #1 killer): Escalating multi-hit (+1 per turn). Wounds clog draw pile. NEED: exhaust for Wounds, fast kill, 60%+ HP. Do NOT play Brutality. **CRITICAL: If you have Brimstone, DO NOT FIGHT Book of Stabbing. Brimstone gives it +2 Str/turn on top of +1 hit/turn -- damage grows quadratically. Two deaths confirmed from this anti-synergy (Runs 091, 100). Even at 75% HP with strong Str scaling, the fight is unwinnable by turn 5.**
- **Gremlin Leader** (2 deaths in 5 runs): Rally gives +3 Str to ALL enemies per cast. By turn 5, all enemies have +6 Str. Fight is unwinnable after turn 7. NEED: AOE for gremlins, Shockwave for mass debuff, 60%+ HP entry. Do NOT waste turns (Battle Trance + end = death).
- **Slavers**: 3 enemies, 27+ combined damage. NEED: AOE, mass debuff, 60%+ HP.

### Brimstone Elite Avoidance

If Brimstone is equipped, the Act 2 elite pool becomes asymmetrically dangerous:
- **Book of Stabbing: HARD AVOID.** Brimstone + multi-hit + hit-count escalation = quadratic damage growth. Two deaths confirmed. No amount of player Strength compensates.
- **Snake Plant: CAUTION.** Brimstone adds +2/turn to each of its 3 hits. 9x3 becomes 11x3 by turn 2. Combined with Frail, expect 40-60 HP drain.
- **Gremlin Leader: MODERATE RISK.** Brimstone adds +2 to every gremlin. With Rally +3, combined scaling is +5 Str/turn to all enemies.

When holding Brimstone, avoid elite paths entirely if HP is below 70%. The enemy Strength scaling makes every elite fight significantly harder.

### Fairy Management

Fairy in a Bottle is often consumed in Centurion+Mystic fights. If Fairy is your only death insurance, avoid fights that might trigger it before the elite/boss. Plan paths so Fairy is available for the most dangerous fight.

---

## Act 2 Preparation

Act 2 enemies hit significantly harder than Act 1.

### Enter Act 2 at Full HP

Pantograph heals 25 HP at boss start (NOT full HP). Act 2 hallway fights drain 30-60 HP. Enter with maximum possible HP. If you enter the boss 40 HP below max, Pantograph only recovers 25 of that deficit.

### Upgrades Matter More

Unupgraded cards are much weaker against Act 2 enemies. Prioritize upgrading at rest sites over resting when HP is above 50%. The upgrade death spiral (no upgrades -> harder fights -> more HP loss -> forced resting -> no upgrades) must be avoided.

### Healing Sustain Is Critical

Burning Blood (+6/fight) cannot compensate for 30-50 HP fights. Reaper and Feed are the only reliable in-combat healing. Feed provides permanent Max HP scaling (12-18+ Max HP over a full run). Take healing cards early for maximum value.

**Reaper alone is NOT sufficient healing sustain.** Reaper exhausts after a single use per fight. In consecutive combat rooms (common in Act 2), Reaper heals once per fight but cannot offset sustained drain across multiple fights. A deck with Reaper as its only healing source lost 20 HP in Centurion+Mystic (29 to 9), recovered only 6 via Burning Blood, then died two floors later with no way to heal back. Multiple healing sources are required for Act 2 survival.

**Healing source priority for Act 2 survival:**
1. Reaper (heals for damage dealt to ALL enemies -- scales with Strength and Vulnerable)
2. Feed (permanent +3-4 Max HP per kill, compounds over the run)
3. Blood Potion / Regen Potion (one-time emergency heal)
4. Toy Ornithopter relic (+5 HP per potion used)
5. Bite cards (2 HP per play -- sustained but small; comes at devastating Max HP cost from Vampires event)
6. Rest sites (but spending rest on healing means no upgrades)

**Minimum healing requirement:** At least TWO sources from the list above (not counting rest sites) by Act 2 Floor 5. A single Reaper or single Feed is not enough given that Act 2 hallway fights drain 25-50 HP each and often come in consecutive pairs.

If by Floor 20 your only healing is Burning Blood, the run is in danger. Actively prioritize healing card picks in Act 1 when offered.

### Backup Healing Plan (when Reaper/Feed are NOT offered)

Reaper and Feed are uncommon cards -- they may not appear in card rewards at all (confirmed: Run 53 had neither offered across 33 floors). The healing priority rule works when cards are offered, but RNG can deny them entirely. When this happens, the player must actively pursue alternative healing:

1. **Shop healing**: Buy Blood Potion or Regen Potion at every shop if no healing card exists. Buy Toy Ornithopter or Meal Ticket if offered.
2. **Event healing**: The Cleric heals. Big Fish offers healing. Woman in Blue sells potions. Prioritize these events.
3. **Map pathing for rest sites**: Without healing cards, rest sites become the primary healing source. Path through MORE rest sites, accept fewer upgrades. This is a degraded strategy but better than dying.
4. **Potion management**: Treat Blood Potions and Regen Potions as precious resources. Do not use them in trivial fights.
5. **Conservative play**: Without healing, EVERY point of HP matters more. Take safer paths, skip elites after Floor 15, avoid Unknown rooms below 50% HP.

The absence of healing cards does NOT mean the run is lost. It means the player must shift from "aggressive with healing to recover" to "conservative to avoid damage in the first place."

---

## Act 3 Preparation

Act 3 enemies hit harder than Act 2 and have unique mechanics that punish specific strategies.

### Enter Act 3 at Full HP

Pantograph heals 25 HP at the Act 2 boss start (NOT full HP). The Collector fight itself drains 50-65 HP. Entering Act 3 at 14-20 HP (as observed) is extremely dangerous. The first hallway fight in Act 3 can drain 25-40 HP (Writhing Mass, Darklings). If possible, path through a rest site or event between the boss and Act 3.

### Act 3 HP Thresholds

| Fight Type | Minimum HP | Notes |
|---|---|---|
| Hallway (easy) | 40% | Spikers, Repulsors -- manageable but Thorns punish attacks |
| Hallway (hard) | 60% | Writhing Mass (25-40 HP drain), Darklings (Life Link extends fight) |
| The Transient | 50% | Pure survival check -- 5 turns of escalating damage, do not attack |
| Elite | 70% | Act 3 elites are extremely dangerous at low HP |
| Boss | 70% or Pantograph | Donu and Deca, Awakened One, or Time Eater |

### Act 3 Key Enemies

- **Writhing Mass**: Malleable gains block per hit. Use single large hits, NOT multi-hit (Whirlwind, Pummel). Expect 25-40 HP drain. Long fight (6-8 turns).
- **The Transient**: 999 HP, Fading 5. Survive 5 turns. Do NOT attack (Shifting gives it block). Disarm and Weak are essential. Enter at 50%+ HP.
- **Darklings**: Life Link -- must kill all 3 in the same turn or they revive at half HP. AOE (Immolate+) is critical. Save AOE for the kill turn.
- **Spikers**: Thorns damage per Attack played. Block before attacking. Use fewer, larger attacks.

### What the Deck Needs for Act 3

1. **Block density**: Impervious, Shrug It Off, Defend+. Act 3 fights are longer and hit harder.
2. **AOE**: Immolate+ is the single best card. Darklings require simultaneous kills; Writhing Mass + allies require spread damage.
3. **Disarm/Weak sources**: Transient and scaling enemies require Strength reduction and Weak application.
4. **Healing cards**: Even more critical than Act 2. Writhing Mass drains 25-40 HP per fight. Without Reaper or Feed, consecutive fights will end the run.
5. **Deck thinning**: A lean deck (18-22 cards) draws key cards more reliably in long fights.

---

### Cross-Run Victory Pattern

Across all Act 1 boss victories (10 total, including 1 Act 2 boss victory) and 2 Act 2 boss deaths (Runs 105, 110), the differentiators are:
1. **Boss-specific answer cards**: Every victory had at least one card for the boss's main threat. Every death lacked this. Hexaghost victories used Disarm, Rampage+, Reaper, or Shockwave from potions. Collector victory used Immolate+ (AOE for Torch Heads), Shockwave+ (mass debuff), and Impervious (post-debuff survival).
2. **Passive block/sustain**: Metallicize, Plated Armor, Pantograph, or Torii appeared in most victories. None of the Act 1 boss deaths had passive block. Pantograph was the key enabler for the Collector victory (entered at 57% HP, healed 25 HP to near-full).
3. **Entry HP**: Victories entered at 50-80 HP (or had Pantograph). Deaths entered at 16-50 HP.
4. **Self-damage avoidance**: No boss victory used Berserk or Brutality. Brutality is confirmed as a death cause in long fights even at full HP entry -- the 1 HP/turn drain is lethal in fights lasting 8+ turns. Only play Brutality in fights expected to end within 4-5 turns.
5. **Upgrade discipline**: Victories had 1-4 key upgrades. Zero-upgrade runs are unwinnable (3x confirmed).
6. **Damage scaling for long fights**: Hexaghost victories had damage scaling (Inflame, Rampage+, Disarm). Collector victory relied on Immolate+ AOE. Two Hexaghost deaths had Weak but no damage scaling.
7. **Extra energy**: The Collector victory had 4 energy (Sozu). Extra energy enables offense + defense simultaneously.

### Cross-Run Death Pattern (Act 2) -- Updated at 110 runs

Across 30+ Act 2 deaths, the pattern has SHIFTED from "missing critical tools" to "HP attrition from pathing" -- but Runs 105 and 110 reveal boss-specific failure modes:
1. **HP attrition from consecutive combats (primary cause)**: The player enters Act 2 at healthy HP, loses 30-50 HP in one fight (Byrds, Snake Plant, Centurion+Mystic), then enters the NEXT fight at critical HP and dies. The mistake is not the first fight -- it is taking a second combat room immediately after. This is a MAP PATHING failure, not a deck building failure. The fix is mandatory path tracing before every map choice.
2. **Block scaling gap at Act 2 boss (Run 105)**: Run 105 met all three original Act 2 readiness criteria (Thunderclap+ for AOE, Spot Weakness for Strength, Feed+ for healing) and reached the Act 2 boss for the first time. Died to Bronze Automaton Hyper Beam (38 damage) because the deck had only 4 basic Defends (5 block each = 20 max). Block scaling is now the 4th mandatory readiness criterion. Cards like Shrug It Off, Flame Barrier, Metallicize, or Impervious would have saved this run.
2b. **HP entry threshold at Act 2 boss (Run 110)**: Run 110 had excellent deck quality (all 4 readiness criteria met: Whirlwind+ AOE, Spot Weakness+Inflame Str, Feed healing, Shrug It Off+Flame Barrier++Metallicize block). Died to The Collector at Floor 33 because HP entry was 57% (49/86) instead of the required 70%. The Colosseum event on the prior floor forced an unexpected combat that drained HP. Missing Impervious and Shockwave+ meant the post-debuff crisis was unsurvivable at 25 HP. Two consecutive boss reaches (Runs 105, 110) confirm the deck building is working -- the bottleneck is now boss-specific preparation (block scaling, HP management, key defensive cards like Impervious/Shockwave+).
3. **Brimstone anti-synergy (2 deaths)**: Brimstone purchased at shop without evaluating Act 2 elite pool. Book of Stabbing with Brimstone deals quadratically scaling damage. Both deaths occurred with strong Str decks that would have survived without Brimstone's enemy buff.
4. **3 Cultists + scaling hallway fights**: 6 deaths to 3 Cultists at 5-53% HP. This is a HALLWAY fight, not an elite. It cannot be avoided via pathing (it spawns on Monster nodes). The only defense is entering every Act 2 combat at 60%+ HP -- which requires better pathing between combats. Run 112 entered at 5% HP after Snake Plant drained 42 HP on the prior floor -- the death cascade was Snake Plant (no Strength scaling, 7-turn fight) into 3 Cultists at lethal HP.
5. **Book of Stabbing is the #1 elite killer**: 3 deaths. Wound clog + escalating multi-hit. Decks without exhaust tools cannot win. Decks with Brimstone cannot win.
6. **Odd Mushroom anti-synergy (contributing factor, Run 105)**: Odd Mushroom reduces Vulnerable from 1.5x to 1.25x, cutting burst output by ~17%. In DPS-race fights (Bronze Automaton, Book of Stabbing), this extends fights by 1-2 turns, forcing survival through additional damage cycles. Consider refusing Odd Mushroom when the deck is Vulnerable-dependent.
7. **The deck building window is Floor 6-15**: After Floor 15, there are too few card rewards and shops left to fill gaps. If the deck is missing Str scaling, AOE, or block scaling by Floor 12, the player must prioritize these over all other card choices.
