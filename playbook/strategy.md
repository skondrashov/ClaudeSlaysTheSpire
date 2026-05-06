# Strategy

High-level strategic principles for Ironclad runs.

---

## HP Management: The #1 Cause of Death

Entering fights at critically low HP is the single most common cause of death across all runs. Thirteen of sixteen deaths resulted from entering a fight below 50% HP or with fatal self-damage mechanics active.

| Run | Entry HP | % of Max | Fight | Result |
|---|---|---|---|---|
| 3 | 28 | 35% | Chosen | Died (Chosen at 6 HP) |
| 4 | 42 | 50% | Centurion+Mystic | Died (at 1 HP) |
| 5 | 11 | 13% | Gremlin Leader | Died (unwinnable) |
| 6 | 6 | 7% | Book of Stabbing | Died (dealt 140 dmg, Book at 21 HP) |
| 8 | 37 | 39% | 3 Cultists | Died (Shockwave+ timing + low HP) |
| 10 | low | <50% | Slime Boss | Died (Hemokinesis self-damage post-split) |
| 11 | 18 | ~22% | Chosen+Byrd | Died (HP drained through Act 2) |
| 13 | 10 | ~12% | Fungi Beast+Shelled Parasite | Died (2x Brutality self-damage at 10 HP) |
| 19 | 18 | 25% | Shelled Parasite+Fungi Beast | Died (no block cards, Offering -6 HP left at 6) |
| 20 | 15 | 19% | Cultist+Chosen | Died (7x2 Vuln=20 vs 13 block, HP at 3) |
| 21 | 35 | 39% | 3 Cultists | Died (index shift error + scaling overwhelmed block) |
| 22 | 28 | 30% | 3 Cultists | Died (Demon Form+Limit Break too slow, scaling overwhelmed) |
| 23 | 7 | 9% | Cultist+Chosen | Died (Hex+Vuln, 20 dmg vs max 8 block at 7 HP) |

### HP Thresholds for Act 2

| Fight Type | Minimum HP | Notes |
|---|---|---|
| Hallway (easy) | 25% | Byrds/Chosen can still drain 40-60 HP |
| Hallway (hard) | 50% | 3 Cultists, Centurion+Mystic, Snake Plant |
| Elite | 60% | Gremlin Leader, Book of Stabbing |
| Boss | 70% or Pantograph | Act 2 boss has massive damage |

**CRITICAL: 3 Cultists is the single most lethal encounter in the game -- responsible for three deaths (the most of any fight).** Triple independent +3 Str/turn = +9 combined Str/turn. Deaths occurred at 30%, 37%, and 39% HP entry. Even a deck with Shockwave+, Metallicize, Inflame, Fiend Fire, and Rampage failed at 30% HP because slow scaling engines cannot kill fast enough to survive the combined damage. The 50% threshold for hard hallway fights is NON-NEGOTIABLE for this encounter.

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

1. **Byrd fights**: 36-58 HP lost per fight. Flight makes fights 10-12 turns. The primary Act 2 HP drain.
2. **Centurion+Mystic**: 25-42 HP lost per fight. Mystic's healing extends the fight. Often consumes Fairy in a Bottle.
3. **Snake Plant in Unknown rooms**: 21 HP/turn with Frail debuff. Even with burst damage, drains 20-30 HP. Unknown rooms can become Snake Plant fights -- they are NOT safe at low HP.
4. **No healing between fights**: Burning Blood (+6) cannot compensate for 30-50 HP fights.
5. **Fairy consumed in wrong fight**: In multiple runs, Fairy was consumed in Centurion+Mystic, leaving no safety net for elites. Save Fairy for elites/bosses when possible.
6. **Decay curse compound damage**: Each Decay in hand deals 2 unblockable damage per turn. With 2 Decays, that is 4 HP/turn lost regardless of block. Over a 5-turn fight, that is 20 free HP lost. Prioritize curse removal at shops or via exhaust (Fiend Fire).

---

## Rest Site Decisions

### Upgrade vs Rest Framework

**Upgrade** when:
- HP is above 45%
- Next room is unknown or normal monsters
- A critical upgrade target exists (Bash, True Grit, key attack card)
- Earlier is better: one upgrade on floor 8 benefits 20+ fights

**Rest** when:
- HP is below 35%
- Next room is a known elite or boss
- At 35-45%, consider the specific next room -- elite/boss = rest, unknown = upgrade

### The Upgrade Death Spiral

Only upgrading once in 28 floors was the worst strategic error observed. Each missed upgrade makes fights harder, which drains more HP, which forces more resting, which means more missed upgrades. Break the cycle: upgrade at the FIRST rest site unless HP is critically low.

### Upgrade Priority

1. Bash (3 Vulnerable vs 2 is massive)
2. True Grit (CHOSEN exhaust vs RANDOM is game-deciding)
3. Armaments (upgrade 1 card -> upgrade ALL cards in hand -- transformative)
4. Carnage (28 vs 20 damage)
5. Iron Wave (7/7 vs 5/5)
6. Pommel Strike (10 damage + draw 2 vs 9 + draw 1)
7. Thunderclap (7 vs 4 AOE)
8. Shrug It Off (11 vs 8 block)
9. Headbutt (12 vs 9 damage)
10. Defend (8 vs 5 block -- low individual priority but Ancient Writing mass upgrade is excellent)

---

## Deck Building Philosophy

### Take Cards That Solve Problems

A card's value depends on what your deck needs RIGHT NOW.

Before taking a card, ask:
- What fights am I struggling with?
- Do I have enough damage? Enough block? AOE?
- Will this card dilute my draws (bigger deck = less likely to draw key cards)?

A mediocre card that fills a gap is better than a strong card that duplicates what you already have.

### Deck Thinning

Remove Strikes at shops and events. A 10-12 card deck draws key cards much more reliably than a 15+ card deck. Remove Strikes before Defends (Strikes get outclassed faster; Defend's 5 block stays relevant).

### Multi-Purpose Cards Win

The winning formula across all victories: cards that do two things. Block+draw (Shrug It Off), damage+draw (Pommel Strike), damage+block (Iron Wave), damage+heal (Reaper), damage+deck manipulation (Headbutt). Single-purpose cards (Strike, Defend) are the weakest cards in the deck.

### Slow Scaling Engines Are a Deck Weakness

Demon Form (+2 Str/turn) and Limit Break (double Strength) are powerful scaling cards in long fights -- but they require 2-3 free setup turns before providing meaningful value. Against fast-scaling enemies at low HP (3 Cultists, multi-enemy fights), this setup time does not exist. The player is dead before the engine comes online.

**Pattern:** A deck built around Demon Form + Limit Break can beat bosses comfortably but die to hallway fights when entered at low HP. The fix is NOT to avoid these cards -- it is to recognize that they solve long fights (bosses) but do NOT solve emergency situations. The deck still needs immediate burst (Fiend Fire, Rampage, Immolate) and block density for fights where you cannot afford 2 turns of setup.

**Rule:** If your primary damage scaling is Demon Form or Limit Break, you MUST have an alternative fast-burst plan for emergencies. Do not enter fights below 50% HP relying solely on a slow engine.

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
- AOE for the split (Thunderclap, Whirlwind) -- MANDATORY
- Burst single-target to kill one slime fast (Fiend Fire)
- Exhaust for Slimed cards

**The Guardian needs:**
- 32+ block capability in one turn (Impervious, double Metallicize + Weak)
- Burst damage for Mode Shift (Carnage+)
- Enough cards to last 12+ turns (do NOT over-exhaust)
- **Avoid exhaustion-heavy strategies.** Fiend Fire + Dark Embrace creates a thin deck by mid-fight. Block density on 32-damage turns (turns 8-12) drops below survivable thresholds when the deck thins to 8-10 cards. Use Fiend Fire on free turns or for burst, never as the primary deck engine.

**Hexaghost needs:**
- Weak source (Shockwave, Clothesline, Intimidate, Weak Potion) -- MANDATORY
- Damage scaling (Rampage, Inflame) -- kill before Burns overwhelm (insufficient damage killed 2 runs despite having Weak)
- Passive block (Metallicize) for the 13-turn fight
- Turn 1 setup (Thunderclap for Vulnerable)
- No self-damage cards (Brutality, Berserk)

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

- Prefer routes with a rest site in the last 1-2 floors before the boss.
- Don't take unnecessary damage from events when HP is limited.
- After a brutal fight (Byrds, Centurion+Mystic), next room MUST be healing, not another combat.
- If the path forces an elite at low HP, skip it entirely -- take any alternative path.

### Elite Risk Assessment

Before fighting an elite, check:
1. **HP threshold**: Below 30 HP for Act 1 elites is dangerous. Below 60% for Act 2 elites is dangerous.
2. **Deck vs elite matchup**: Gremlin Nob punishes Skill-heavy decks. Lagavulin punishes slow decks. Sentries need AOE.
3. **Potions available**: Potions compensate for bad matchups.
4. **Path alternatives**: If a safer path exists with similar value, take it.

### Fairy Management

Fairy in a Bottle is often consumed in Centurion+Mystic fights. If Fairy is your only death insurance, avoid fights that might trigger it before the elite/boss. Plan paths so Fairy is available for the most dangerous fight.

---

## Act 2 Preparation

Act 2 enemies hit significantly harder than Act 1.

### Enter Act 2 at Full HP

Pantograph heals to full before the boss, but Act 2 hallway fights drain 30-60 HP. Enter with maximum possible HP.

### Upgrades Matter More

Unupgraded cards are much weaker against Act 2 enemies. Prioritize upgrading at rest sites over resting when HP is above 45%. The upgrade death spiral (no upgrades -> harder fights -> more HP loss -> forced resting -> no upgrades) must be avoided.

### Healing Sustain Is Critical

Burning Blood (+6/fight) cannot compensate for 30-50 HP fights. Reaper and Feed are the only reliable in-combat healing. Feed provides permanent Max HP scaling (12-18+ Max HP over a full run). Take healing cards early for maximum value.

**Reaper alone is NOT sufficient healing sustain.** Reaper exhausts after a single use per fight. In consecutive combat rooms (common in Act 2), Reaper heals once per fight but cannot offset sustained drain across multiple fights. A deck with Reaper as its only healing source lost 20 HP in Centurion+Mystic (29 to 9), recovered only 6 via Burning Blood, then died two floors later with no way to heal back. Multiple healing sources are required for Act 2 survival.

**Healing source priority for Act 2 survival:**
1. Reaper (heals for damage dealt to ALL enemies -- scales with Strength and Vulnerable)
2. Feed (permanent +3-4 Max HP per kill, compounds over the run)
3. Blood Potion / Regen Potion (one-time emergency heal)
4. Toy Ornithopter relic (+5 HP per potion used)
5. Rest sites (but spending rest on healing means no upgrades)

**Minimum healing requirement:** At least TWO sources from the list above (not counting rest sites) by Act 2 Floor 5. A single Reaper or single Feed is not enough given that Act 2 hallway fights drain 25-50 HP each and often come in consecutive pairs.

If by Floor 20 your only healing is Burning Blood, the run is in danger. Actively prioritize healing card picks in Act 1 when offered.

### Cross-Run Victory Pattern

Across all boss victories (7 total), the differentiators are:
1. **Boss-specific answer cards**: Every victory had at least one card for the boss's main threat. Every death lacked this. Hexaghost victories used Disarm, Rampage+, Reaper, or Shockwave from potions.
2. **Passive block/sustain**: Metallicize, Plated Armor, Pantograph, or Torii appeared in most victories. None of the Act 1 boss deaths had passive block.
3. **Entry HP**: Victories entered at 50-80 HP (or had Pantograph). Deaths entered at 16-50 HP.
4. **Self-damage avoidance**: No boss victory used Berserk or Brutality. Brutality+Rupture is a valid Act 2 scaling engine but must not be active during boss fights with status damage.
5. **Upgrade discipline**: Victories had 1-4 key upgrades. One victory had 0 upgrades but compensated with rare cards.
6. **Damage scaling for long fights**: Hexaghost victories had damage scaling (Inflame, Rampage+, Disarm) to shorten the fight. Two deaths had Weak sources but insufficient damage -- the fight lasted too long and Burns attrition killed them.
