# Strategy

High-level strategic principles for Ironclad runs.

**CURRENT BOTTLENECK (130-run milestone):** The system has TWO distinct failure layers. **Layer 1: Mechanics execution errors** -- the player keeps misapplying basic game mechanics despite documented corrections. Weak direction confusion (Run 124), SIO+ block miscalculation (Run 125), Flame Barrier+ block vs counter confusion (Run 125), Armaments+ block value forgotten (Run 126), Strength carryover between combats (Run 127), Hexaghost Turn 2 multi-hit undocumented until after death (Run 129). Six different mechanics errors in six consecutive runs. The playbook documents the correct values, but the player does not reliably consult or apply them during combat. **Layer 2: HP attrition without healing** -- healing card RNG denial (7 of last 9 runs with no Reaper/Feed offered) forces reliance on potions and rest sites, which cannot offset 30-50 HP Act 2 fights. The backup healing plan is documented but produces death spirals anyway.

**THE REAL PROBLEM:** Layer 1 is more addressable than Layer 2. Every mechanics error costs 3-20 HP. Across a run, 3-5 such errors compound to 15-60 lost HP -- equivalent to an entire fight's worth of damage. Fixing execution would effectively add one free fight's worth of HP to every run, partially compensating for healing denial. The player needs a combat arithmetic checklist, not more strategic documentation.

**SCORECARD (runs 101-137):**
- Act 1 boss wins: ~75% -- Guardian regression (4 deaths in 36 runs). Hexaghost regression (Run 129 F16, Run 137 F16).
- Act 2 boss reaches: 4 (Runs 105, 110, 114, 125). No new Act 2 boss reach since Run 125.
- Act 2 hallway/elite deaths (Runs 124-137): F23 Gremlin Leader, F21 Shelled Parasite, F23 Slavers, F24 Shelled Parasite, F16 Hexaghost, F23, F21, F23, F24, F16.
- Best floor: 39 (Run 63) -- unchanged for 70+ runs.
- Hard Rule violations: 0.
- **Floor average (last 20 tracked runs): 23.1.** Down from 25-26 plateau at Run 100. This is REGRESSION, not progress.
- **Mechanics errors: 6 distinct errors in runs 124-129.** Weak direction, SIO+ value, Flame Barrier+ block vs counter, Armaments+ value, Str carryover, Hexaghost Turn 2 damage. Each error cost 3-20 HP. Combined, these errors account for more HP loss than any single strategic gap.
- **Healing RNG denial: 7 of last 9 runs.** Backup plan insufficient. However, this is NOT addressable -- RNG denial cannot be fixed. Focus on what CAN be fixed: mechanics execution.
- **Hexaghost regression: 2 deaths at F16 in last 16 runs** despite extensive playbook. The playbook is not being applied.

**IMMEDIATE PRIORITIES (in order):**
1. **STOP MAKING ARITHMETIC ERRORS.** This is the #1 addressable cause of death. Before EVERY damage/block calculation in combat, verify: (a) Is Weak on ME or on the ENEMY? Weak on enemy = their attacks weaker, MY attacks normal. (b) Am I using UPGRADED card values? Check the + suffix. SIO+ = 11, not 8. Flame Barrier+ = 16 block + 6 counter (two separate numbers). (c) Does Strength carry over from last combat? NO. Inflame, Spot Weakness, Demon Form all reset. Only relic Str (Vajra) persists. See the COMBAT ARITHMETIC CHECKLIST below.
2. **Build Act 2-ready decks by Floor 15.** ALL FOUR criteria: (a) front-loaded Strength (Inflame or Spot Weakness, NOT Demon Form alone), (b) AOE, (c) healing beyond Burning Blood, (d) block scaling beyond basic Defends.
3. **Trace full paths before every map choice.** Count forced combats to the next rest/shop on each path. Choose fewer combats. In the last 5 floors before the Act 2 boss, path selection priority: Rest > Shop > Event > Monster > Elite.
4. **Block before setup on attack turns.** Budget at least 1E for block when enemies attack. Hexaghost Turn 2 (30 multi-hit), Slavers Turn 1 (27+ combined), any multi-enemy fight. Setup greed (spending all 3E on Powers/Strength) has killed directly in Runs 127 and 129.
5. **Brimstone + Book of Stabbing = death.** Do NOT buy Brimstone if Book of Stabbing is possible. Two deaths confirmed.
6. **3 Cultists threshold is 60%.** Six deaths at 5-53% HP confirm.

---

## COMBAT ARITHMETIC CHECKLIST (read every fight)

Before calculating damage or block, answer these THREE questions:

**1. WHO has Weak?** 
- Weak on ENEMY (from Bash, Shockwave, Intimidate, Thunderclap) = THEIR attacks deal 25% less. YOUR damage is UNAFFECTED.
- Weak on YOU (from enemy debuffs) = YOUR attacks deal 25% less.
- NEVER apply 0.75 to your own damage when enemies are Weakened. This error has occurred in 3+ runs.

**2. Am I using UPGRADED values?**
- Check the + suffix on every card before calculating. Common errors:
  - SIO+ = 11 block (not 8)
  - Flame Barrier+ = 16 block AND 6 counter damage (two separate effects, do not confuse them)
  - Armaments+ = 5 block (not 0, it still blocks) AND upgrades ALL cards in hand
  - Bash+ = 10 damage, 3 Vulnerable (not 2)
  - Intimidate+ = 2 Weak (not 1)

**3. Does my Strength reset?**
- Inflame, Spot Weakness, Demon Form: Strength is PER-COMBAT. Resets to 0 each new fight.
- Vajra relic: permanent, persists across combats.
- Strength Potion: temporary within one combat only.
- Rampage counter: also resets each combat.
- NEVER carry Strength values from the previous fight into calculations.

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
- **BLOCK-FIRST RULE at sub-30% HP:** When HP is below 30%, every energy point not spent on block must be justified. If you have 1E remaining and the choice is between a damage card and Defend, play Defend. Surviving to Turn 2 enables everything; dying on Turn 1 with 13 extra damage dealt is meaningless. Mass Weak (Shockwave) reduces incoming by 25% but does NOT replace block -- even Weakened multi-enemy damage can be lethal at critical HP.

### The Act 2 Death Spiral Is Predictable

The pattern across 10 low-HP deaths: the player enters Act 2 at reasonable HP, loses 30-50 HP in one brutal fight (Byrds, Centurion+Mystic, Chosen solo, Cultist+Chosen, Looter+Mugger), then enters the NEXT fight at critical HP and dies. The mistake is not the first fight -- it's taking a second combat room immediately after. After ANY fight that leaves you below 30% HP, the next room MUST be non-combat. If the map doesn't offer this, the run was lost at map selection, not at the fight.

Even "hallway" fights in Act 2 can be run-ending: 3 Cultists has killed the player three times at 30-39% HP entry. These are not elites -- they appear on normal Monster nodes. The only defense is entering with sufficient HP or having a path that avoids consecutive combat rooms.

**Act 2 decision point:** After each fight, if HP is below 35%, evaluate the ENTIRE remaining path. If it contains 2+ consecutive combat rooms before a rest site, consider abandoning elites and taking the safest available path even if it means missing rewards.

### What Causes the HP Drain

1. **Byrd fights**: 36-58 HP lost per fight. Flight makes fights 8-12 turns. The primary Act 2 HP drain. Without Thunderclap (mass Flight stripping + Vulnerable), expect the upper end. Thunderclap is the single most important card for Act 2 Byrd survival.
2. **Centurion+Mystic**: 25-42 HP lost per fight. Mystic's healing extends the fight. Often consumes Fairy in a Bottle.
3. **Chosen (solo or paired)**: 30-40 HP drained even with strong decks. Hex punishes Skills (Dazed clog), Vulnerable on player amplifies incoming damage to 20+/turn, and +3 Str scaling makes the fight progressively more dangerous. A confirmed death spiral trigger: 39 HP entry with Carnage+, Bash+, Headbutt, Dropkick, Demon Form resulted in exiting at 7 HP (32 HP drain over 7 turns). The next fight was unwinnable at 7 HP.
4. **Snake Plant in Unknown rooms**: 21 HP/turn with Frail debuff. Drains 15-42 HP depending on Strength scaling. Run 112: 42 HP drained with zero Strength scaling. Run 116: 15 HP drained with Inflame (+4 Str), Bash+, Thorns, and correct play -- but entered at 22 HP (27%) and survived at 1 HP, making the next combat lethal. Unknown rooms can become Snake Plant fights -- they are NOT safe at low HP.
5. **Spheric Guardian (solo or with Sentry)**: 30-41 HP drain even with correct play and Strength scaling. Barricade block makes Reaper useless and chip damage futile. Four deaths confirmed from this encounter (at 26%, 43%, 47%, and 100% HP entry). One survival with Demon Form + Carnage+ still cost 41 HP (80->39). Unknown rooms are the most dangerous room type in Act 2 at any HP level when this fight spawns.
6. **No healing between fights**: Burning Blood (+6) cannot compensate for 30-50 HP fights.
7. **Fairy consumed in wrong fight**: In multiple runs, Fairy was consumed in Centurion+Mystic, leaving no safety net for elites. Save Fairy for elites/bosses when possible.
8. **Decay curse compound damage**: Each Decay in hand deals 2 unblockable damage per turn. With 2 Decays, that is 4 HP/turn lost regardless of block. Over a 5-turn fight, that is 20 free HP lost. Prioritize curse removal at shops or via exhaust (Fiend Fire).
9. **Vampires event Max HP loss**: Accepting the Vampires event removes ~30% of Max HP (observed: 80->56). At 56 Max HP, every HP threshold in the table above shifts drastically -- 60% for elites becomes 34 HP, which is nearly impossible to maintain through Act 2. The 5 Bite cards provide 2 HP healing per play but cannot compensate for the reduced HP ceiling against burst damage. Refuse this event unless desperate for healing with no alternatives.

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

1. **Front-loaded Strength**: Inflame, Spot Weakness, or Corruption+FNP engine. NOT Demon Form alone (too slow for hallway fights -- confirmed in 2 SG deaths and 1 Act 2 hallway death at F21). Demon Form fills the boss scaling role but does NOT satisfy this criterion. If Demon Form is the only Str source, treat this criterion as UNMET and continue prioritizing Inflame or Spot Weakness. Without front-loaded Str, Reaper healing is also ineffective (Reaper needs Str on the turn it's played, not 3 turns later). If no front-loaded Strength source exists by Floor 12, take the next one offered over any other card.
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
- Damage scaling (Rampage, Inflame, Spot Weakness) -- kill before Burns overwhelm (insufficient damage killed 2 runs despite having Weak). Even with strong Str scaling (Inflame+ + Spot Weakness = +9 Str), Turn 2 HP loss from insufficient blocking can make Burns lethal by Turn 12.
- Passive block (Metallicize) for the 13-turn fight
- Turn 1 setup (Thunderclap for Vulnerable)
- Turn 2 block discipline -- Turn 2 is a ~30 damage multi-hit. Budget at least 1E for block.
- No self-damage cards (Brutality, Berserk)

**The Collector needs:**
- HP entry at 70%+ or Pantograph -- STRONG_DEBUFF on Turn 4 applies Vulnerable 3, Frail 3, Weakened 3 simultaneously. Pantograph heals 25 HP at boss start, which helps but does NOT bypass the threshold if you enter more than 25 HP below max.
- AOE damage (HIGHEST PRIORITY) -- Immolate+ is the single best card. Hits Collector + both Torch Heads. With Vulnerable: 42 damage to Collector per cast. Torch Heads respawn, so AOE is more valuable than single-target.
- Mass debuff -- Shockwave+ (Weak 3 + Vuln 3 to ALL enemies) reduces combined incoming by 25% while boosting all damage by 50%. Second-highest priority.
- Impervious -- 30 block absorbs post-debuff turns. Critical defensive card.
- Disarm -- permanent Str reduction compounds over the 10-turn fight. Play Turn 1.
- Block density for post-debuff turns -- Frail reduces block by 25%, need multiple sources

**Bronze Automaton needs:**
- HP entry at 70%+ or Pantograph -- 300 HP boss with +3 Str/cycle scaling. HP alone is insufficient without block scaling. Block alone is insufficient without HP. Both are required.
- **Block scaling (MANDATORY)** -- Hyper Beam deals 38-51 damage (scales with Str; observed 51 at turn 6). Basic Defends (4x5=20 block) are NOT enough. Need Shrug It Off, Flame Barrier, Metallicize, Impervious, or Ghostly Armor. Even SIO+ + Defend (27 block) is not enough to survive Hyper Beam 51 without Weak.
- **Weak source saved for Hyper Beam (MANDATORY)** -- Weak reduces Hyper Beam by 25% (51->38). This reduction is often the survival margin. **Do NOT exhaust Weak sources (Intimidate, Shockwave) for Artifact stripping.** Use Bash+ and Thunderclap for Artifact stripping instead. Save Intimidate/Shockwave for after Artifact is gone, ideally for the Hyper Beam turn. Red Mask strips 1 Artifact automatically at combat start.
- Artifact strippers -- Thunderclap, Bash+. Use NON-EXHAUSTING debuffs for this. Automaton starts with Artifact 3. Red Mask strips 1 (to 2). Bash+ strips 1 (to 1). Thunderclap strips 1 (to 0). Then save Intimidate/Shockwave for Hyper Beam.
- Burst damage -- Fiend Fire+, Rampage, Bludgeon. The fight is a DPS race against Strength scaling. Kill before turn 10 if possible.
- **Kill Stasis Orbs early** -- Orb minions steal cards via Stasis. Stasis targets Power and Skill cards preferentially. Demon Form and Flame Barrier+ are high-value steal targets. Prioritize killing any Orb that steals a block scaling or Weak source card. If Metallicize, Impervious, or Shockwave is stolen, that Orb becomes kill priority #1.
- Intent visibility -- Runic Dome removes the ability to predict Hyper Beam. Avoid taking Runic Dome if Bronze Automaton is a possible Act 2 boss.
- **Odd Mushroom anti-synergy** -- Odd Mushroom reduces Vulnerable from 1.5x to 1.25x, cutting burst by ~17%. In a DPS race against 300 HP + Strength scaling, this extends the fight by 1-2 turns, potentially forcing survival through an extra Hyper Beam cycle.
- **Dark Shackles**: Excellent but not sufficient alone. Reduces Hyper Beam by ~9 damage (from ~51 to ~42 with 6 Str). Still need 30+ block on top of the reduction.

**Donu and Deca needs (NOT YET ENCOUNTERED):**
- AOE damage (Immolate+, Thunderclap+) -- two 250 HP enemies
- Disarm -- reduce Donu's Strength before killing it
- Shockwave+ -- mass Weak+Vulnerable on both
- Block density for 10+ turn fight
- Kill Donu first (prevents Strength scaling for both)

### Act 2 Boss Survival

**Top 3 cards for Act 2 boss fights** (take over almost anything if offered in Act 2):
1. **Impervious** -- 30/40 block handles the biggest hit from any Act 2 boss.
2. **Shockwave+** -- mass Weak 3 + Vuln 3 to ALL enemies for 3 turns.
3. **Disarm** -- permanent Str reduction, play Turn 1.

See individual boss files (bronze-automaton.md, the-collector.md, the-champ.md) for boss-specific strategies.

**Pre-boss HP preservation (last 5 floors before Act 2 boss):**
- **No HP-for-reward trades.** No Knowing Skull, Golden Idol, or HP-cost events. Zero exceptions.
- **Skip elites in the last 3 floors.** Relic value < boss HP threshold.
- **Rest over upgrade at every rest site if below 70% HP.**
- **Path priority: Rest > Shop > Event > Monster > Elite.** Invert normal priority.
- **Treat Unknown rooms as Monster rooms.** Potential Snake Plant, Spheric Guardian.
- Count forced combats on each path to the boss. If ALL paths force 4+ combats, use potions aggressively in each fight.

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
- Synergy engines: Fire Breathing+ when Immolate is in the deck (Burns from Immolate trigger 10 free damage per draw, bypassing Plated Armor)

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
- **Gremlin Leader** (3 deaths): Rally gives +3 Str to ALL enemies per cast. By turn 5, all enemies have +6 Str. Fight is unwinnable after turn 7. NEED: AOE for gremlins, Shockwave for mass debuff, 60%+ HP entry. Do NOT waste turns (Battle Trance + end = death). Do NOT play Impervious Turn 1 -- use it Turn 4-5 when Rally-scaled damage peaks. Confirmed: Inflame+ + Impervious Turn 1 (zero damage) at 42 HP led to 9-turn fight and death.
- **Slavers** (2 deaths): 3 enemies, 27+ combined damage from Turn 1 (no free setup turn). NEED: AOE, mass debuff, block density, 60%+ HP. At sub-25% HP, even mass Weak (Shockwave) cannot save you -- block is mandatory Turn 1. Confirmed: Shockwave + damage (zero block) at 19 HP = Turn 1 death.

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

### What Wins and What Kills (Summary)

**Every boss victory** had: (1) a card that addressed the boss's main threat, (2) passive block/sustain, (3) entry HP above 50% or Pantograph, (4) at least 1 key upgrade, (5) no self-damage cards (Brutality/Berserk). **Every boss death** was missing at least one of these.

**Act 2 death causes (ranked by frequency, 35+ deaths):**
1. **HP attrition from consecutive combats** -- the player enters Act 2 healthy, one drain fight (30-50 HP), next room is combat at critical HP, death. This is a pathing failure. Solved by mandatory path tracing.
2. **3 Cultists at low HP** -- 6 deaths at 5-53% HP entry. Hallway fight, not avoidable. Only defense: enter every Act 2 combat at 60%+ HP.
3. **Book of Stabbing** -- 3 deaths. #1 elite killer. Needs exhaust tools. Brimstone makes it unwinnable.
4. **Mechanics execution errors** -- arithmetic mistakes that waste 3-20 HP per error, compounding into lethal HP deficits. See COMBAT ARITHMETIC CHECKLIST above.
5. **Healing RNG denial** -- 7 of last 9 runs with no Reaper/Feed offered. Not addressable. Backup plan (potions, rest sites, conservative pathing) is documented but insufficient alone.
6. **Brimstone anti-synergy** -- 2 deaths from Brimstone + Book of Stabbing.
7. **Deck building window closes at Floor 15** -- missing criteria after F15 cannot be filled. Prioritize gaps over "good" cards.
