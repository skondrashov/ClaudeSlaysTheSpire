# Strategy

High-level strategic principles for Ironclad runs.

**CURRENT BOTTLENECK (118-run milestone):** TWO distinct failure modes remain. (1) Entering the Act 2 boss at sufficient HP -- THREE consecutive Act 2 boss reaches (Runs 105, 110, 114, all Floor 33) confirm the 4-criteria readiness system WORKS when all 4 criteria are met. (2) Criteria RNG denial -- both healing and block scaling can be denied by card-offer RNG. Run 116 died F21 with no healing card offered across 21 floors. Run 118 died F21 with no block scaling card offered -- had Reaper, Demon Form, Spot Weakness, Whirlwind, Thunderclap, Shockwave (strong offense+healing) but zero Shrug It Off/Impervious/Flame Barrier/Metallicize. Feel No Pain was counted as "partial" block scaling but produced only 3-6 block per fight, grossly insufficient vs Snake Plant 7x3=21. **Feel No Pain does NOT fulfill the block scaling criterion.** When a criterion cannot be filled, the backup plan (conservative pathing, rest-heavy routing) must activate IMMEDIATELY.

**SCORECARD (runs 101-118):**
- Act 1 boss wins: ~80% -- Run 103 died to Guardian F16 (Pandora's Box removed all Defends), Run 107 died to Guardian F16 (Corruption+ exhausted block Skills -- now Hard Rule #9)
- Act 2 boss reaches: 3 (Runs 105, 110, 114, all Floor 33) -- STRONG TREND
- Act 2 hallway deaths: Run 116 died F21 (healing never offered). Run 118 died F21 (block scaling never offered; Feel No Pain insufficient).
- Bronze Automaton: 2 deaths (Run 105 -- block scaling gap; Run 114 -- 45% HP entry despite having all tools including Dark Shackles)
- The Collector: 1 death (Run 110 -- 57% HP entry, missing Impervious and Shockwave+)
- Hard Rule violations: 0
- Best floor: 39 (Run 63) -- unchanged but system is reliably reaching F33
- **70% HP threshold violated: 3/3 boss fights (100%).** Run 105: N/A (Pantograph). Run 110: 57%. Run 114: 45%. This is the #1 problem to solve.
- **Criteria RNG denial: Run 116 (healing denied, 21 floors). Run 118 (block scaling denied, 21 floors).** The 4-criteria system has a structural weakness: any single criterion denied by card-offer RNG creates an unrecoverable spiral.
- MILESTONE: Three consecutive Act 2 boss reaches confirm the 4-criteria readiness system works when all 4 criteria are met. Runs 116+118 show ANY criterion can be RNG-denied.

**IMMEDIATE PRIORITIES (in order):**
1. **Preserve HP in the last 5 floors before the Act 2 boss.** The 70% entry threshold has been violated in 3/3 boss fights (100% failure rate). This is now the #1 cause of death. New rules: no HP-for-reward trades, skip elites in the last 3 floors, rest over upgrade at every rest site if below 70%, prioritize paths with rest sites over combat/elite paths. See "Pre-boss HP preservation" section for full rules.
2. **Trace full paths before every map choice.** Before choosing any path, trace EVERY option forward to the next rest/shop. Count forced combats. Choose fewer combats. Say the count aloud: "Path A: 3 combats to rest. Path B: 1 combat to rest." This is especially critical in the last 5 floors -- count total combats remaining before the boss on each path.
3. **Build Act 2-ready decks by Floor 15.** The deck needs ALL FOUR: (a) front-loaded Strength (Inflame or Spot Weakness, NOT Demon Form alone), (b) AOE (Thunderclap, Cleave, Immolate, Whirlwind), (c) healing beyond Burning Blood, (d) block scaling beyond basic Defends (Shrug It Off, Flame Barrier, Metallicize, Ghostly Armor, Impervious, or True Grit+). Run 114 proved this system works -- the deck met all 4 criteria and had the tools to beat the boss. The failure was HP, not deck quality.
4. **Do NOT buy Brimstone if Book of Stabbing is a possible Act 2 elite.** Brimstone + Book of Stabbing has killed the player twice. The anti-synergy makes Book of Stabbing damage grow quadratically (more hits * more damage per hit). If already holding Brimstone, AVOID Book of Stabbing entirely.
5. **3 Cultists threshold is 60%, not 50%.** Six deaths at 5-53% HP confirm that even strong block tools cannot survive Ritual scaling. Kill speed (AOE burst to remove one Cultist fast) matters more than defensive tools.
6. **Have Strength scaling by Floor 15** (Inflame > Spot Weakness > Limit Break). Spheric Guardian and other high-block enemies are mathematically unwinnable without it.

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
3. **Snake Plant in Unknown rooms**: 21 HP/turn with Frail debuff. Drains 15-42 HP depending on Strength scaling. Run 112: 42 HP drained with zero Strength scaling. Run 116: 15 HP drained with Inflame (+4 Str), Bash+, Thorns, and correct play -- but entered at 22 HP (27%) and survived at 1 HP, making the next combat lethal. Unknown rooms can become Snake Plant fights -- they are NOT safe at low HP.
3b. **Spheric Guardian (solo or with Sentry)**: 30-38 HP drain even with correct play and Strength scaling. Run 116: Spheric Guardian solo drained 38 HP over 14 turns (60->22 HP) despite Inflame, Thunderclap x3 for Artifact stripping, Bash+ for Vulnerable, and Offering for draw. Barricade block makes Reaper useless and chip damage futile. Four deaths confirmed from this encounter (at 26%, 43%, 47%, and 100% HP entry). Unknown rooms are the most dangerous room type in Act 2 at any HP level when this fight spawns.
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

**This is non-negotiable.** A deck with Reaper + adequate damage will reach Act 3. A deck with perfect damage/block but no healing will die in Act 2 floors 20-30. Run 116 confirmed: deck had 3 of 4 criteria (Inflame, Thunderclap, Shrug It Off + Flame Barrier+) but neither Reaper nor Feed was ever offered across 21 floors. The healing gap was the sole cause of the HP death spiral.

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
- HP entry at 70%+ or Pantograph -- 300 HP boss with +3 Str/cycle scaling. Run 105 entered at 92/92 (Pantograph) and still died -- HP alone is insufficient without block scaling. Run 114 entered at 39/85 (45%) with excellent block scaling and still died -- block alone is insufficient without HP.
- **Block scaling (MANDATORY)** -- Hyper Beam deals 38-45+ damage (scales with Str). Basic Defends (4x5=20 block) are NOT enough. Need Shrug It Off, Flame Barrier, Metallicize, Impervious, or Ghostly Armor. Run 105 died specifically because the deck had zero block scaling cards. Run 114 had Metallicize + Ghostly Armor + Shrug It Off + Dark Shackles but still died because HP was too low to absorb residual damage.
- Artifact strippers -- Thunderclap+, Bash+, Shockwave+. Automaton starts with Artifact 3. Run 105 stripped all 3 Artifacts by turn 3 using Thunderclap+ (x2) + Bash+. Shockwave+ then applied Weak 3 + Vuln 3 successfully on turn 4.
- Burst damage -- Fiend Fire+, Rampage, Bludgeon. The fight is a DPS race against Strength scaling. Kill before turn 10 if possible.
- Weak source -- Shockwave+ reduces Hyper Beam by 25% (38->28). Critical for survival. Must land AFTER Artifact is stripped.
- **Kill Stasis Orbs early** -- Orb minions steal cards via Stasis. Run 114: Metallicize was stolen, removing 3 block/turn permanently. Prioritize killing any Orb that steals a block scaling or Weak source card. If Metallicize, Impervious, or Shockwave is stolen, that Orb becomes kill priority #1.
- Intent visibility -- Runic Dome removes the ability to predict Hyper Beam. Avoid taking Runic Dome if Bronze Automaton is a possible Act 2 boss.
- **Odd Mushroom anti-synergy** -- Odd Mushroom reduces Vulnerable from 1.5x to 1.25x, cutting burst by ~17%. In a DPS race against 300 HP + Strength scaling, this extends the fight by 1-2 turns, potentially forcing survival through an extra Hyper Beam cycle.
- **Dark Shackles**: Excellent but not sufficient alone. Reduces Hyper Beam by ~9 damage (from ~51 to ~42 with 6 Str). Still need 30+ block on top of the reduction.

**Donu and Deca needs (NOT YET ENCOUNTERED):**
- AOE damage (Immolate+, Thunderclap+) -- two 250 HP enemies
- Disarm -- reduce Donu's Strength before killing it
- Shockwave+ -- mass Weak+Vulnerable on both
- Block density for 10+ turn fight
- Kill Donu first (prevents Strength scaling for both)

### Act 2 Boss Survival (THE CORE BOTTLENECK)

The system now reliably reaches Act 2 bosses (3 in a row). The challenge is arriving with enough HP. Three deaths (Runs 105, 110, 114) reveal:

**Key cards for Act 2 boss survival (prioritize in Act 2 card rewards and shops):**
1. **Impervious** -- The single most impactful defensive card for Act 2 bosses. 30 block (40 upgraded) absorbs Hyper Beam (38 dmg), Collector post-debuff turns (37+ dmg), and Champ Execute burst. Both Act 2 boss deaths (Runs 105, 110) would have been different with Impervious in the deck. If offered in Act 2, TAKE IT over almost any other card.
2. **Shockwave+** -- Mass Weak 3 + Vuln 3 to ALL enemies. Reduces combined incoming from multi-enemy bosses (Collector + Torch Heads, Automaton + Orbs) by 25% for 3 turns while boosting all damage by 50%. The highest-value single play in Act 2 boss fights.
3. **Disarm** -- Permanent Strength reduction. Play Turn 1 against Collector or Champ for maximum cumulative value.

**Pre-boss HP preservation (last 5 floors before Act 2 boss) -- THE #1 UNSOLVED PROBLEM:**

The 70% HP threshold has been violated in ALL THREE Act 2 boss fights (Runs 105, 110, 114). This is not variance -- it is a systematic failure. Root cause analysis across all three runs:

**WHY the threshold keeps being violated:**
1. **HP drain accumulates over floors 26-32, not just the last 2.** Run 114 traced: F26 Cultist+Chosen (58->52 HP), F27 Knowing Skull (-12 HP, 52->40), F28 Shelled Parasite+Fungi Beast (-6 HP, 44->38), F29 Centurion+Mystic (-16 HP, 38->23, rest to 48), F30 Byrd+Chosen (50->44), F31 3 Cultists (50->42, then took True Grit+), F31 Slavers elite (36->14, rest to 39). Six consecutive combats with only 1 rest site = impossible to maintain 70%.
2. **Events drain HP when they should preserve it.** Run 114: Knowing Skull cost 12 HP for 90g (useless). Run 110: Colosseum forced combat. Events in the last 5 floors are HP traps.
3. **Elites in the last 3 floors are too costly.** Run 114: Slavers at F31 drained 22 HP with only 1 rest site remaining. No recovery possible.
4. **The player takes gold/reward trades when HP preservation should be the ONLY priority.** Run 114: Knowing Skull gold trade at 58% HP. Also the Golden Idol trade on F13 lost 11 HP. These small drains compound.

**NEW RULES for last 5 floors before Act 2 boss (Floors ~28-33):**
- **HARD RULE: No HP-for-reward trades.** Do not spend HP at Knowing Skull, Golden Idol, or any event that costs HP. Zero exceptions in the last 5 floors.
- **HARD RULE: Skip elites in the last 3 floors.** The relic is not worth the HP drain. If the only path contains an elite, accept the suboptimal path. A relic at 14 HP is worth less than entering the boss at 70%.
- **HARD RULE: Rest over upgrade at EVERY rest site in the last 5 floors if below 70% HP.** Run 114 correctly rested instead of upgrading Shockwave, but the single rest site was insufficient to compensate for 6 consecutive combats.
- **Path selection priority in last 5 floors: Rest > Shop > Event > Monster > Elite.** Invert the normal priority. The goal is HP, not cards/relics/gold.
- Treat Unknown rooms in the last 5 floors as Monster rooms (potential Snake Plant, Spheric Guardian, or Chosen+Byrd). If an alternative path with a rest site exists, take it.
- Count total forced combats on each path from current floor to boss. If ALL paths force 4+ combats before the boss, the run may already be in danger -- use all potions aggressively in each fight to minimize HP loss.

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
- **Unknown rooms are NOT safe in Act 2.** They can resolve as any hallway fight, including Byrds, Snake Plant, and Spheric Guardian + Sentry. THREE deaths confirmed from Spheric Guardian spawning from Unknown rooms (at 26%, 43%, and 100% HP). The third death occurred at FULL HP -- even 87/87 was not enough. Run 116: Unknown room at F20 spawned Snake Plant at 22 HP (27% of max) -- survived at 1 HP but was doomed for the next mandatory combat. Treat Unknown rooms as Monster rooms when routing in Act 2. Only take Unknown rooms in Act 2 if the deck has Strength scaling and the alternative path is worse. **At below 30% HP, Unknown rooms are lethal -- the player chose Unknown at 22 HP hoping for a non-combat outcome and got Snake Plant instead.**

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

Reaper and Feed are uncommon cards -- they may not appear in card rewards at all (confirmed: Run 53 had neither offered across 33 floors; Run 116 had neither offered across 21 floors, directly causing death at F21). The healing priority rule works when cards are offered, but RNG can deny them entirely. **Activate this backup plan by Floor 17 if no healing card has been acquired** -- do not wait until HP is critical. When this happens, the player must actively pursue alternative healing:

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

Across all Act 1 boss victories (10 total, including 1 Act 2 boss victory) and 3 Act 2 boss deaths (Runs 105, 110, 114), the differentiators are:
1. **Boss-specific answer cards**: Every victory had at least one card for the boss's main threat. Every death lacked this. Hexaghost victories used Disarm, Rampage+, Reaper, or Shockwave from potions. Collector victory used Immolate+ (AOE for Torch Heads), Shockwave+ (mass debuff), and Impervious (post-debuff survival).
2. **Passive block/sustain**: Metallicize, Plated Armor, Pantograph, or Torii appeared in most victories. None of the Act 1 boss deaths had passive block. Pantograph was the key enabler for the Collector victory (entered at 57% HP, healed 25 HP to near-full).
3. **Entry HP**: Victories entered at 50-80 HP (or had Pantograph). Deaths entered at 16-50 HP.
4. **Self-damage avoidance**: No boss victory used Berserk or Brutality. Brutality is confirmed as a death cause in long fights even at full HP entry -- the 1 HP/turn drain is lethal in fights lasting 8+ turns. Only play Brutality in fights expected to end within 4-5 turns.
5. **Upgrade discipline**: Victories had 1-4 key upgrades. Zero-upgrade runs are unwinnable (3x confirmed).
6. **Damage scaling for long fights**: Hexaghost victories had damage scaling (Inflame, Rampage+, Disarm). Collector victory relied on Immolate+ AOE. Two Hexaghost deaths had Weak but no damage scaling.
7. **Extra energy**: The Collector victory had 4 energy (Sozu). Extra energy enables offense + defense simultaneously.

### Cross-Run Death Pattern (Act 2) -- Updated at 116 runs

Across 30+ Act 2 deaths, the pattern has SHIFTED decisively. Deck building is solved (4-criteria readiness works). Two remaining killers: (A) **HP management in the last 5 floors before the boss** and (B) **healing card RNG denial** creating unrecoverable HP spirals even from full HP entry:
1. **HP attrition from consecutive combats (primary cause)**: The player enters Act 2 at healthy HP, loses 30-50 HP in one fight (Byrds, Snake Plant, Centurion+Mystic, Spheric Guardian), then enters the NEXT fight at critical HP and dies. This is a MAP PATHING failure. The fix is mandatory path tracing before every map choice. Run 116: entered Act 2 at 80/80 HP but Spheric Guardian drained 38 HP (to 22), then Unknown room spawned Snake Plant (to 1 HP), then forced combat killed the run. Without healing cards, even 100% HP entry provides only ~3 fight buffer before death.
1b. **HP threshold violation at Act 2 boss (3/3 boss fights, 100% failure rate)**: Run 105 had Pantograph (special case). Run 110 entered at 57%. Run 114 entered at 45%. ALL THREE RUNS had decks ready to win -- the boss killed them because they arrived too damaged. Run 114 is the clearest example: all 4 readiness criteria met, Dark Shackles for Hyper Beam, Shockwave for mass debuff, Bottled Inflame for guaranteed Strength -- and still died because 6 consecutive combats + 1 event HP drain in the last 7 floors left only 39/85 HP. The fix is aggressive HP preservation pathing in the last 5 floors (new rules added to Pre-boss HP preservation section).
2. **Block scaling gap at Act 2 boss (Run 105)**: Fixed by adding block scaling as 4th readiness criterion. Run 114 confirmed: Metallicize + Ghostly Armor + Shrug It Off provided adequate block scaling. This is no longer the bottleneck.
2b. **Elite timing near boss (Run 114, NEW)**: Taking Slavers at Floor 31 (2 floors from boss) drained HP from 36 to 14. Only 1 rest site remained, healing to 39/85 (45%). New rule: skip elites in the last 3 floors before the boss.
3. **Brimstone anti-synergy (2 deaths)**: Brimstone purchased at shop without evaluating Act 2 elite pool. Book of Stabbing with Brimstone deals quadratically scaling damage. Both deaths occurred with strong Str decks that would have survived without Brimstone's enemy buff.
4. **3 Cultists + scaling hallway fights**: 6 deaths to 3 Cultists at 5-53% HP. This is a HALLWAY fight, not an elite. It cannot be avoided via pathing (it spawns on Monster nodes). The only defense is entering every Act 2 combat at 60%+ HP -- which requires better pathing between combats. Run 112 entered at 5% HP after Snake Plant drained 42 HP on the prior floor -- the death cascade was Snake Plant (no Strength scaling, 7-turn fight) into 3 Cultists at lethal HP.
5. **Book of Stabbing is the #1 elite killer**: 3 deaths. Wound clog + escalating multi-hit. Decks without exhaust tools cannot win. Decks with Brimstone cannot win.
6. **Odd Mushroom anti-synergy (contributing factor, Run 105)**: Odd Mushroom reduces Vulnerable from 1.5x to 1.25x, cutting burst output by ~17%. In DPS-race fights (Bronze Automaton, Book of Stabbing), this extends fights by 1-2 turns, forcing survival through additional damage cycles. Consider refusing Odd Mushroom when the deck is Vulnerable-dependent.
7. **The deck building window is Floor 6-15**: After Floor 15, there are too few card rewards and shops left to fill gaps. If the deck is missing Str scaling, AOE, or block scaling by Floor 12, the player must prioritize these over all other card choices.
