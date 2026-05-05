# Events

Events encountered across all runs, organized by act.

---

## Act 1 Events

### The Cleric (Act 1)
OPTIONS:
- [Heal] Heal HP.
- [Purify] 50 Gold: Remove a card from your deck.

DECISION FRAMEWORK: At high HP, Purify is better (permanent deck improvement). At low HP, Heal. Removing a Strike improves draw quality for the rest of the run.
PRIORITY: Purify (high HP) > Heal (low HP).

### Big Fish (Act 1)
OPTIONS:
- [Banana] Heal to full HP.
- [Donut] +5 Max HP.
- [Box] Obtain a relic + gain Regret curse.

DECISION FRAMEWORK: Low HP -> Banana. Near full HP -> Donut (+5 Max HP is permanent). Box is risky -- Regret curse permanently pollutes the deck.
PRIORITY: Banana (low HP) > Donut (high HP) > Box (rarely worth the curse).

### Living Wall (Act 1)
OPTIONS:
- [Forget] Remove a card.
- [Grow] Upgrade a card.
- [Change] Transform a card.

DECISION FRAMEWORK: If a game-defining upgrade exists (True Grit -> True Grit+, Shockwave -> Shockwave+), ALWAYS choose Grow. Otherwise, Forget (Remove) is the default -- deck thinning is permanent value. Change (Transform) is high variance.
PRIORITY: Grow (if critical upgrade target exists) > Forget (default) > Change (gambling).

### Shining Light (Act 1)
OPTIONS:
- [Enter] Take 17 damage, upgrade 2 random cards.
- [Leave] Nothing.

DECISION FRAMEWORK: Only enter at high HP (60%+). Two random upgrades are valuable but 17 damage before a boss could be fatal.
PRIORITY: Enter (high HP, no boss imminent) > Leave (low HP or boss coming).

### Golden Idol (Act 1)
OPTIONS:
- [Take] Obtain Golden Idol, trigger trap. Then choose:
  - [Outrun] Lose 6 Max HP.
  - [Smash] Take 20 damage.
  - [Hide] Gain a curse.

DECISION FRAMEWORK: Golden Idol increases gold earned by ~25% (not fully confirmed). The trap costs are ranked: Smash (20 HP, recoverable at rest sites) > Outrun (6 Max HP, permanent loss) > Hide (curse, permanent deck pollution). At full HP, Smash is affordable. Below 50% HP, skip entirely.
PRIORITY: Smash (high HP) > Outrun (if 6 Max HP is affordable) > Leave (low HP). Never choose Hide.

### Scrap Ooze (Act 1)
OPTIONS:
- [Reach Inside] Lose 3 HP. 25% chance: Find a Relic. Repeatable.

DECISION FRAMEWORK: High variance. Set a maximum HP budget BEFORE starting:
- Above 80% HP: spend up to 12 HP (4 attempts).
- At 60-80% HP: spend at most 6 HP (2 attempts).
- Below 60% HP: LEAVE IMMEDIATELY.
Expected cost for one relic: 12 HP (4 attempts average). Getting unlucky with 8+ attempts costs 25+ HP for nothing.
PRIORITY: Attempt with budget (high HP) > Leave immediately (moderate/low HP).

### Transmogrifier (Act 1)
OPTIONS:
- [Pray] Transform a card.
- [Leave] Nothing.

DECISION FRAMEWORK: Transforming a Strike is almost always positive -- nearly any card is better. Risk of getting something worse exists but the floor is very low.
PRIORITY: Transform a Strike > Leave.

### Mushrooms (Act 1)
OPTIONS:
- [Stomp] Fight Fungi Beasts. Rewards include a relic.
- [Leave / Curse option]

DECISION FRAMEWORK: Fighting is usually better than a permanent curse. Fungi Beasts are manageable if you can handle Spore Cloud Vulnerable.
PRIORITY: Stomp (if HP allows) > Leave/Curse.

---

## Act 2 Events

### Council of Ghosts (Act 2)
OPTIONS:
- [Accept] Lose 40 Max HP, gain 5 Apparition cards (prevent ALL damage for 1 turn each, Ethereal).
- [Refuse] Leave.

DECISION FRAMEWORK: 5 turns of invincibility is powerful, but -40 Max HP is devastating. At 100+ Max HP with a strong deck that ends fights quickly, Accept can work (Apparitions buy 5 free turns). At low Max HP (<80), Refuse -- being at 39 Max HP means one bad fight ends the run.
PRIORITY: Accept (100+ Max HP, strong deck) > Refuse (default, especially <80 Max HP).

### Forgotten Altar (Act 2)
OPTIONS:
- [Sacrifice] Lose 20 HP, gain +5 Max HP.
- [Desecrate] Gain Decay curse.
- [Leave]

DECISION FRAMEWORK: If near a rest site, Sacrifice is almost always correct. 20 HP is recoverable; Decay curse permanently ruins draws; +5 Max HP is permanent value.
PRIORITY: Sacrifice (can recover HP) > Leave > Desecrate (never worth the curse).

### Old Beggar (Act 2)
OPTIONS:
- [Offer Gold] 75 Gold: Remove a card from your deck.
- [Leave]

DECISION FRAMEWORK: 75g for card removal is slightly expensive but always valuable. Remove Strikes before Defends (Strikes become worse as better attacks are added; Defend's 5 block stays relevant).
PRIORITY: Offer Gold (if you can afford it and won't need gold for shop) > Leave.

### Ominous Forge (Act 2)
OPTIONS:
- [Forge] Upgrade a card in your deck.
- [Leave]

DECISION FRAMEWORK: ALWAYS choose Forge. Free upgrades are the best events in the game. No HP cost, no gold cost. Follow standard upgrade priority: Bash > key attack/skill cards > Thunderclap > Defend.
PRIORITY: Forge (always).

### Ancient Writing (Act 2)
OPTIONS:
- [Simplicity] Upgrade all Strikes and Defends.
- [Insight] Second option uncertain (possibly gain a card or relic).

DECISION FRAMEWORK: Simplicity is approximately +7-8 upgrades in one event when you have many basic cards remaining. Strike+ (9 damage, 13 Vuln) is 50% more than Strike (6, 9 Vuln). Defend+ (8 block) is 60% more than Defend (5). Choose Simplicity when 3+ Strikes and Defends remain unupgraded. The alternative may be better for decks with few basic cards.
PRIORITY: Simplicity (many basic cards remaining) > Insight (few basic cards).

### Pleading Vagrant (Act 2)
OPTIONS:
- [Offer Gold] 85 Gold: Obtain a Relic.
- [Rob] Obtain a Relic + gain a Curse.
- [Leave]

DECISION FRAMEWORK: If you can afford 85g and don't need it for shops, paying for a relic is positive (relics are permanent value). Robbing adds a curse that permanently pollutes the deck. Leave if gold is critical for upcoming shop purchases.
PRIORITY: Offer Gold (can afford) > Leave > Rob (curse cost too high).

### Face Trader (Act 2)
OPTIONS: Unknown exactly. Involves HP cost for uncertain reward.

DECISION FRAMEWORK: Don't engage at low HP. The reward is uncertain and the HP cost is real.
PRIORITY: Leave (low HP) > Engage (high HP, feeling adventurous).

### Cursed Tome (Act 2)
OPTIONS: Unknown. Name suggests interaction with Curses.

DECISION FRAMEWORK: Avoid unless more information is available. Curses permanently pollute the deck.
PRIORITY: Leave (default).

### The Joust (Act 2)
OPTIONS:
- [Murderer] Bet 50 Gold -- 70% chance to win 100 Gold.
- Other options unknown.

DECISION FRAMEWORK: Expected value: 0.7*100 - 0.3*50 = +55g. Mathematically positive but high variance. Take if gold isn't critical for imminent shop purchases.
PRIORITY: Bet (gold surplus) > Leave (need gold for shop soon).
