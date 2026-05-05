# Game Mechanics

Mechanics documented from actual runs. Focus on things we got wrong or needed to learn.

## Status Cards

### Slimed
- Cost: 1 energy
- Effect: Exhaust (that's it — it does nothing except waste energy and a card slot)
- Source: Slime enemies add these to your deck
- Impact: Devastating to hand quality. In a 5-card hand, each Slimed card is -20% of your resources. We saw hands with 3 Slimed cards in Run 1, leaving only 2 playable cards.
- Playing Slimed is usually correct even if you have nothing else to do with the energy, because it exhausts the card permanently. Leaving it means it recycles into your deck.
- Confidence: HIGH (observed extensively in Run 1)

## Debuffs

### Frail
- Effect: Block gained from cards is reduced by 25%
- Duration: N turns, decrements at start of your turn
- Math: Defend 5 → 3 block (observed). Shrug It Off 8 → 6 block (observed).
- This is rounding: floor(5 * 0.75) = 3, floor(8 * 0.75) = 6
- Confidence: HIGH (observed in Run 1, math verified)

### Vulnerable
- Effect: Take 50% more damage from attacks
- Duration: N turns
- Berserk card applies this TO YOURSELF — extremely dangerous. 2 turns of Vulnerable in a multi-enemy fight can be fatal.
- Confidence: MEDIUM (observed in Run 1 — Berserk applied Vulnerable to self)

## Energy

- Base energy: 3 per turn (Ironclad, no relics modifying it)
- Energy resets each turn — unspent energy is wasted
- Confidence: HIGH (standard mechanic)

## Card Draw

- Standard draw: 5 cards per turn
- Cards that draw (like Shrug It Off) add to your hand mid-turn
- When planning a turn with draw cards, you can't predict the full turn — play the draw card first, then reassess
- Confidence: HIGH (standard mechanic)

## Damage Calculation

- Base formula: floor((card_base_damage + strength) * multipliers)
- Vulnerable multiplier: 1.5x (on target)
- Weak multiplier: 0.75x (on attacker)
- These stack multiplicatively
- **Order of operations (confirmed Run 3)**: Add Strength to base damage FIRST, then apply multipliers. floor((base + Str) * Weak * Vuln). Rounding: floor() is applied AFTER all multipliers.
- **Example with Strength + Weak (Run 3 confirmation)**: Strike (6 base) + 2 Strength + Weakened: floor((6+2) * 0.75) = floor(6.0) = 6 damage. Player calculated this correctly in Run 3 Chosen fight and the observed damage matched (2 Strikes dealt 12 damage total, Chosen went from 18 to 6 HP).
- **Example with Strength + Vulnerable**: Strike (6 base) + 2 Strength, target Vulnerable: floor((6+2) * 1.5) = floor(12) = 12 damage.
- **Example with Weak + Vulnerable stacking**: Strike (6 base), Weakened attacker, Vulnerable target: floor(6 * 0.75 * 1.5) = floor(6.75) = 6 damage.
- Confidence: HIGH (Run 3 confirmed Strength + Weak formula with exact damage match)

## Exhaust

- Exhausted cards are removed from the deck for the rest of combat
- They go to the exhaust pile, not the discard pile
- Some cards exhaust after use (like Slimed, Shockwave). Others don't (like Bash, Strike).
- Exhaust is permanent for the combat — the card will not be drawn again
- True Grit+ can exhaust a card from your hand as an additional effect (observed in Run 0)
- Confidence: HIGH (standard mechanic, confirmed across Run 0 and Run 1)

## Ethereal

- Ethereal cards are automatically exhausted at end of turn if they are still in your hand (not played)
- This means you MUST play them or lose them permanently
- Always play Ethereal cards if they're in hand, even if you don't need the effect — permanent loss is worse than wasted block/damage
- Observed: Ghostly Armor in Run 1 — player correctly identified "must play or lose it"
- Confidence: MEDIUM (observed in Run 1, standard mechanic)

## Potions

### Fruit Juice
- Effect: Gain +5 Max HP (permanent)
- Best used at the start of a long fight (like a boss) for maximum value — the extra HP is available immediately
- Observed: Run 1, used at start of Slime Boss fight
- Confidence: MEDIUM (used once in Run 1)

### Speed Potion
- Effect: Gain Dexterity (adds block to all block-gaining cards for the rest of combat)
- Observed: Run 1, used against Slime Boss. Player used it to boost block against 35 incoming damage. Defend went from 5 to 10 block (5 Dexterity).
- Confidence: LOW (used once, exact Dexterity amount needs confirmation — may be +5)

## Relics

### Golden Idol
- Source: Golden Idol event (Act 1). Choose to take the idol, then choose a cost (lose 21 HP, lose 6 max HP, or gain a curse).
- Effect: Unknown. The player took 21 HP damage to acquire it (Run 1, floor 4) but we never observed what it does.
- Confidence: LOW (acquired in Run 1, effect not observed)

### Burning Blood
- Ironclad starter relic.
- Effect: Heal 6 HP at the end of every combat.
- WRONG previous confidence: Was LOW, now upgraded. Confirmed in Run 2: player explicitly referenced "Burning Blood heals to X" multiple times with consistent +6 HP math (e.g., floor 3: "71 HP stays. Burning Blood heals to 77" = +6).
- Confidence: HIGH (confirmed across Run 2, exact heal amount = 6)

## Curl Up (Enemy Passive)

- Some enemies (Louses) have a passive shield that triggers when they are first hit
- Gives the enemy block (5-7 observed in Run 1)
- The first attack that hits them is partially or fully absorbed by this block
- Strategy: Hit them with a small attack first to trigger the block, then follow up with big attacks
- Or: Apply Vulnerable first with Bash to get value over more turns, accepting the first attack is partially absorbed
- Confidence: MEDIUM (observed in multiple Louse fights in Run 1)

## Mode Shift (Guardian Mechanic)

- The Guardian has a Mode Shift counter in Attack Mode
- When you deal enough damage to reduce it to 0, the Guardian switches to Defensive Mode (Sharp Hide)
- The counter resets and increases each cycle: observed starting at 27 in Run 2 (player noted Mode Shift 27->21 after 6 damage on turn 1). Previous entry said "10 -> 40 -> 50" — the initial value of 10 appears WRONG; 27 was observed. Later cycle values need reconfirmation.
- In Defensive Mode, Sharp Hide 3 = 3 damage to player per Attack card played
- After some turns in Defensive Mode, switches back to Attack Mode
- Mode Shift tracks total HP damage dealt, not damage to block
- Confidence: MEDIUM (observed across Run 2 Guardian fight, 14 turns of data)

## Sharp Hide (Guardian Defensive Mode)

- When the Guardian is in Defensive Mode, it has Sharp Hide N (N=3 observed)
- Every time the player plays an Attack card, Sharp Hide deals N damage to the player
- This damage is applied to block first (if player has block), then HP
- Strategy: In Sharp Hide mode, either (1) play Defend/block cards BEFORE attacks to absorb the retaliation, or (2) only play Skills for pure block
- At low HP without block, playing ANY Attack is suicide (3 damage per Attack at 2 HP = death)
- Confidence: MEDIUM (observed in Run 2, confirmed damage-to-block interaction)

## Relics

### Charon's Ashes
- Effect: Whenever a card is exhausted, deal 3 damage to ALL enemies
- Synergy: With True Grit (exhaust per turn) and Dark Embrace (draw on exhaust), creates an exhaust engine that deals damage and cycles cards
- In Run 2, Charon's Ashes dealt 3 damage many times during the Guardian fight. Over 14 turns, contributed ~30+ total damage
- Danger: Encourages over-exhausting, which can thin the deck dangerously
- Confidence: MEDIUM (used extensively in Run 2)

### Ancient Tea Set
- Effect: Gain 2 energy on turn 1 if the previous room was a Rest site
- This means turn 1 has 5 energy total (3 base + 2 from Ancient Tea Set)
- Extremely valuable for boss fights immediately after a rest site — the extra 2 energy on turn 1 can set up powers or deal massive opening damage
- Run 2: Used to play Power Potion (Metallicize, 0E) + Dark Embrace (2E) + True Grit (1E) + Strike (1E) on Guardian turn 1. Note: player had 5E but only spent 4E — 1E was wasted. Could have played an additional Defend for 5 more block.
- **Path implication**: Always rest (not smith) at the rest site before a boss when you have Ancient Tea Set, unless you're at high HP. The 2E bonus is worth more than most upgrades.
- Confidence: MEDIUM (confirmed in Run 2, wasted energy noted)

### Burning Blood
- Ironclad starter relic
- Effect: Heal 6 HP at the end of every combat
- Confirmed: 6 HP heal observed in Run 2 after multiple combats
- Confidence: HIGH (confirmed in Run 2)

## Powers

### Dark Embrace
- Type: Power (permanent for rest of combat)
- Effect: Whenever a card is exhausted, draw 1 card
- Synergy: With exhaust cards (True Grit), makes exhausting free in terms of hand size — you always replace the exhausted card
- Combined with Charon's Ashes: every exhaust = draw 1 card + 3 AOE damage. This is a powerful engine.
- Danger: Encourages exhausting more cards, which can thin deck below survival threshold
- Confidence: MEDIUM (confirmed in Run 2)

### Metallicize
- Type: Power (permanent for rest of combat)
- Effect: Gain N block at the end of each turn (before enemy attacks are resolved)
- Run 2: Metallicize 3 (from Power Potion) provided 3 free block every turn for 14 turns = 42 total block
- This is the block equivalent of Strength for attacks — passive scaling that rewards long fights
- Confidence: MEDIUM (confirmed in Run 2)

## Strength (Player Debuff)

- Lagavulin and other enemies can reduce player Strength permanently during combat
- Each -1 Strength reduces ALL attack card damage by 1: Strike 6->5->4, Pommel Strike 9->8->7, Iron Wave 5->4->3
- With Vulnerable on target, reduced damage still gets multiplied: floor((6-1)*1.5) = floor(7.5) = 7 for Strike at -1 Str
- Run 2 Lagavulin fight: Player's Strikes went from 6 to 5 to (probably) 4 damage over the fight as debuffs stacked
- IMPORTANT: Recalculate all damage values after Strength changes. Plans made with base values will overestimate output.
- Confidence: MEDIUM (observed in Run 2 Lagavulin fight, damage values matched debuffed Strength)

## Snecko Oil Potion

- Effect: Draw 5 cards, randomize the cost of all cards in hand (0-3 energy each)
- Run 2: Used TWICE against Gremlin Nob (had 2 copies). First use (turn 3): got 0-cost Defend and 0-cost Pommel Strike — enabled 19 block + 17 damage that would have been impossible normally. Second use (turn 4): got low enough costs to deal 31+ damage for the kill.
- Very high variance — can give you an incredible turn or an unplayable hand
- Best used as a desperation move when the standard hand can't win
- Note: Randomizes the cost of ALL cards in hand after drawing, including previously held cards
- Confidence: MEDIUM (used twice in Run 2, both times in desperation, both times succeeded)

## Power Potion

- Effect: Choose from 3 random Power cards and add one to your hand. It costs 0 energy this turn.
- Run 2: Used on Guardian turn 1. Options included Metallicize and Berserk. Player correctly chose Metallicize (lesson from Run 1: Berserk self-Vulnerable is deadly). Metallicize 3 provided 42 total block over 14 turns for free.
- Best use: Turn 1 of a boss fight, especially on a free (non-attack) turn. Powers are permanent, so early setup = maximum value.
- The 0-cost aspect means it doesn't compete with your normal hand for energy.
- Confidence: MEDIUM (used once in Run 2, confirmed: choose 1 of 3 Powers, free to play)

## Fairy in a Bottle Potion

- Effect: When HP reaches 0, automatically revive with ~30% Max HP
- Run 2: Triggered on floor 11 (Red Slaver fight). Player deliberately took lethal at 7/85 HP, Fairy revived at 25 HP (25/85 = ~29%). Player used this strategically — went all-in on damage knowing the Fairy would save them.
- Acts as a second life — critical safety net for boss fights or desperate situations
- Triggers automatically, no need to use it manually
- CORRECTION: Previous entry said "used before Guardian fight (consumed or discarded?)" — actually triggered during floor 11 Slaver fight, consumed there. Player did NOT have it for the Guardian fight.
- Confidence: MEDIUM (triggered once in Run 2, revive amount ~30% max HP confirmed)

## Status Cards (Run 3 additions)

### Burn
- Cost: Unplayable (cannot be played from hand)
- Effect: At end of turn, if Burn is in your hand, take 2 damage. The Burn stays in your hand and cycles back to your draw pile.
- Source: Hexaghost boss adds Burns to your deck on ATTACK_DEBUFF turns.
- Impact: Double punishment — (1) takes a card slot in your hand, reducing effective hand size, AND (2) deals 2 damage per Burn per turn. Multiple Burns compound: 3 Burns = 6 damage per turn + 3 fewer playable cards.
- Cannot be played or exhausted normally. Cards that exhaust from hand (True Grit+) can remove them.
- Confidence: MEDIUM (observed in Run 3 Hexaghost fight, damage and unplayable status confirmed)

### Dazed
- Cost: Unplayable
- Effect: Ethereal. Cannot be played. If in hand at end of turn, exhausts (Ethereal).
- Source: Chosen enemy adds Dazed when you play Skill cards (via Hex debuff).
- Impact: Clogs your hand for 1 turn, then exhausts itself. Less permanent than Burns or Slimed, but the constant influx from Hex (every Skill played = 1 Dazed added) can overwhelm draws quickly.
- Confidence: LOW (observed in Run 3 Chosen fight, exact mechanics inferred — Ethereal + Unplayable needs confirmation)

## Flight (Enemy Mechanic)

- **Effect**: While an enemy has Flight N (N > 0), all damage dealt to that enemy is halved (likely floor(damage/2)). Each time the enemy is hit by an attack, Flight decrements by 1.
- **Stripping Flight**: Each individual hit reduces Flight by 1. Multi-hit attacks (Whirlwind) and AOE (Thunderclap) each count as separate hits. Thunderclap hitting 3 Byrds reduces each Byrd's Flight by 1.
- **Flight reset**: After Flight reaches 0, the enemy takes full damage. However, Byrds can regain Flight on buff turns ("take flight" action), resetting the counter.
- **Strategy**: (1) Use cheap multi-hit or AOE attacks to strip Flight first. (2) Save big single-hit attacks (Bash+, Pommel Strike) for after Flight is at 0. (3) Focus fire one enemy to strip its Flight and kill it before it can reset.
- **Math example (Run 3)**: Pommel Strike (9 damage) vs Flight 3 Byrd: deals ~4-5 damage and reduces Flight to 2. Strike (6 damage) vs same Byrd: deals ~3 damage and reduces Flight to 1. Next hit: Flight 0, full damage goes through.
- Confidence: MEDIUM (observed in Run 3 Byrd fight, damage halving confirmed, exact rounding uncertain)

## Hex (Enemy Debuff)

- **Effect**: When you play a Skill card, a Dazed status card is added to your draw pile.
- **Source**: Applied by the Chosen enemy (Act 2).
- **Impact**: Punishes defensive play. Every Defend, Shrug It Off, True Grit, Shockwave, etc. adds a dead card. This creates a vicious cycle — you need block to survive, but blocking clogs your deck with Dazed cards, which means fewer block cards drawn next turn.
- **Counter-strategy**: Minimize Skill usage. Rely on Attack cards that provide block (Iron Wave), Powers that provide passive block (Metallicize), or just kill the enemy fast with pure Attacks.
- Confidence: LOW (observed in Run 3 Chosen fight, exact trigger confirmed — needs more data on duration/stacking)

## Relics (Run 3 additions)

### Pantograph
- Source: Gremlin Nob elite reward (Run 3).
- Effect: Heal to full HP at the start of boss fights.
- Run 3: Player entered Hexaghost boss at 56/80 HP. HP was 80/80 at start of turn 2 (and potions were used for Regen, so the 80 HP is from Pantograph, not Regen). Confirmed: Pantograph restores ALL HP, not a partial heal.
- Evaluation: Extremely powerful relic. Removes the need to conserve HP before the boss — you can take risky elite fights, spend HP at events, and still enter the boss at full. Changes the rest-site calculus: always Smith before boss when you have Pantograph.
- Confidence: HIGH (Run 3, heal to full confirmed — entered at 56, started boss at 80)

### Lantern
- Source: Scrap Ooze event (Run 3, floor 9). Cost 3 HP.
- Effect: Gain 1 energy on turn 1 of each combat (4 energy turn 1 instead of 3).
- Run 3: Player noted "gives +1 energy on turn 1 of each combat." Turn 1 of Hexaghost boss, the player played 4 cards costing 1E each (Thunderclap + Pommel Strike + Strike + Defend), suggesting 4 energy available. This is consistent with 3 base + 1 Lantern = 4 energy.
- Evaluation: Solid relic. Extra energy on turn 1 allows stronger openers — play a setup Power AND still have energy for damage/block. Weaker than Ancient Tea Set (which gives +2 energy but only after rest sites).
- Confidence: MEDIUM (Run 3, +1 energy turn 1 inferred from play patterns, not explicitly confirmed by game text)

### Neow's Lament
- Source: Neow's blessing (Run 3 opening choice).
- Effect: Enemies in your next 3 combats have 1 HP. Gives 3 completely free fights with full card/gold/potion rewards.
- Run 3: All 3 fights were instant kills. Floor 1 (Acid Slime M + Spike Slime S), Floor 3 (Jaw Worm), Floor 4 (2 Louses). One Strike each was sufficient to kill. Player got Pommel Strike, Iron Wave, and a Flex Potion as rewards from these free fights.
- Evaluation: One of the best Neow offerings. 3 free fights = 3 card rewards + 3 gold drops + potential potions + zero HP lost. Equivalent to ~50 gold and 3 card choices with no risk.
- Confidence: HIGH (Run 3, all 3 combats confirmed enemies at 1 HP)

### Golden Idol
- Source: Golden Idol event (Act 1). Costs: 20 HP damage, 6 max HP, or a curse card.
- Effect: Increases gold earned by 25% (unconfirmed from our runs — effect not directly observed).
- Run 3: Player took the idol again (chose 20 HP damage at 80 HP -> 60 HP). Player was still unable to observe what Golden Idol does during gameplay. The 25% gold increase is from common game knowledge but not confirmed from our data.
- Confidence: LOW (taken in Runs 1 and 3, effect never directly observed in gameplay)

## Events (Act 1)

### The Cleric
- Options: [Heal] Heal HP, [Purify] 50 Gold: Remove a card from your deck
- Run 2: Player chose Purify, removed a Strike for 50g. Deck went from 11 to 10 cards. Good choice when HP is near-full.
- Confidence: MEDIUM (1 encounter in Run 2)

### Big Fish
- Options: [Banana] Heal to full HP, [Donut] +5 Max HP, [Box] Obtain a relic + gain Regret curse
- Run 2: Player chose Donut (+5 Max HP, 80->85). Correct when near full HP. Banana is correct when HP is low. Box is risky — Regret curse clogs the deck.
- Confidence: MEDIUM (1 encounter in Run 2)

### Living Wall
- Options: [Forget] Remove a card, [Grow] Upgrade a card, [Change] Transform a card
- Run 2: Player chose Remove (removed a Strike) despite initially wanting Upgrade. This was a critical mistake — upgrading True Grit to True Grit+ would have changed the outcome of the entire run.
- Run 3: Player chose Forget (Remove), removed a Strike. Correct decision here — no critical upgrade targets (Bash already upgraded, no True Grit in deck). Deck went from 13 to 12 cards.
- Decision framework: If you have a card where the upgrade is game-defining (True Grit, Shockwave, etc.), ALWAYS choose Upgrade over Remove at this event. Otherwise, Remove is the default best choice.
- Confidence: MEDIUM (2 encounters across Runs 2 and 3, option names confirmed as [Forget]/[Grow]/[Change])

### Shining Light
- Options: [Enter] Take 17 damage, upgrade 2 random cards, [Leave] Nothing
- Run 2: Player left — correct decision at 21 HP (17 damage would leave 4 HP before the boss). Would be strong at high HP.
- Confidence: LOW (1 encounter in Run 2, did not enter)

### Golden Idol
- Options: [Take] Obtain Golden Idol, trigger a trap. Then: [Outrun] Lose 6 Max HP, [Smash] Take 20 damage, [Hide] Gain a curse (Injury?)
- Run 3: Player chose Take, then Smash (20 HP damage, 80->60 HP). At full HP with Neow's Lament active, the 20 HP cost was affordable. Correct evaluation: 20 damage is recoverable, -6 Max HP is permanent, curse is a permanent deck clog.
- Confidence: MEDIUM (2 encounters across Runs 1 and 3, trap options confirmed)

### Scrap Ooze
- Options: [Reach Inside] Lose 3 HP. 25%: Find a Relic. Repeatable.
- Run 3: Player reached inside once at 63 HP, lost 3 HP, and found a Relic (Lantern) on the first try. Lucky outcome — expected HP cost is 12 HP (4 tries at 3 HP each on average).
- Confidence: LOW (1 encounter in Run 3, got lucky on first try)

### Face Trader (Act 2)
- Options: Unknown exact options. Player saw [Continue] then a choice to trade (lose 8 HP?) or [Leave].
- Run 3: Player left at 28 HP — couldn't afford the HP cost for an unknown gamble. Correct decision at low HP.
- Confidence: LOW (1 encounter in Run 3, chose not to engage)

## Events (Act 2)

No events fully documented yet. Face Trader observed but not engaged.

## Potions (Run 3 additions)

### Flex Potion
- Effect: Gain +2 Strength for this turn only (Strength is removed at end of turn).
- Run 3: Used against Gremlin Nob on turn 2. Bash+ with +2 Str dealt 12 damage (10 base + 2 Str). The temporary Strength was well-timed for a burst turn.
- Best use: On a turn where you play multiple Attack cards (each one benefits from +2 damage). On a turn with Bash+ or Pommel Strike to maximize the value.
- Confidence: MEDIUM (used once in Run 3, +2 Str for 1 turn confirmed)

### Regen Potion
- Effect: Gain Regeneration. Heals HP each turn for several turns (amount decreases by 1 each turn — starts at 5, then 4, 3, 2, 1 = 15 total HP, unconfirmed exact numbers).
- Run 3: Used at start of Hexaghost fight turn 2. Player referenced "5 Regen" then "4 Regen" then "3 Regen" in subsequent turns, confirming the decrementing mechanic. Total healing over 5 turns was approximately 15 HP.
- Best use: Start of a long fight (boss) for maximum total healing. The earlier you use it, the more turns of healing you get.
- Confidence: MEDIUM (used once in Run 3, decrementing heal confirmed from player references)

### Skill Potion
- Effect: Choose 1 of 3 random Skill cards and add it to your hand. It costs 0 energy this turn.
- Run 3: Used twice during Hexaghost fight. First use: chose Shockwave (Weak + Vulnerable to all enemies, Exhaust). Second use: chose Ghostly Armor (10 block, Ethereal). Both were critical — Shockwave reduced Hexaghost's Inferno from 42 to ~28, Ghostly Armor provided 10 free block on a key turn.
- Best use: During boss fights when you need a specific answer (mass debuff, big block, etc.). The 0-cost means it's essentially free value.
- Confidence: MEDIUM (used twice in Run 3, choose-1-of-3 + free confirmed)
