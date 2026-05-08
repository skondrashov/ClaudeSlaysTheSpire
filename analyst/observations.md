# Observations

Items pending confirmation or further investigation. Promote to playbook when confident.

## Promoted from Run 70

- Preserved Insect relic: PROMOTED TO PLAYBOOK. Documented in relics/preserved-insect.md. Enemies in Elite fights start with 25% less HP.
- Upgrade death spiral third data point: PROMOTED TO PLAYBOOK. Run 70 confirmed the pattern for the third time. Updated strategy.md.
- Slime Boss split threshold management: PROMOTED TO PLAYBOOK. Updated bosses/slime-boss.md with damage threshold management guidance.
- Disarm vs Slime Boss split: PROMOTED TO PLAYBOOK. Strength reduction does not transfer to split slimes. Documented in cards/disarm.md.

## Promoted from Run 73

- Corruption + Dead Branch synergy: PROMOTED TO PLAYBOOK. Documented in cards/corruption.md and relics/dead-branch.md.
- Corruption setup cost trap: PROMOTED TO PLAYBOOK. 3E unupgraded leaves zero block on setup turn. Documented in cards/corruption.md.
- Mugger enemy: PROMOTED TO PLAYBOOK. Documented in enemies/mugger.md.
- Looter + Mugger pairing: PROMOTED TO PLAYBOOK. Multi-enemy Act 2 fight with 20+ combined damage/turn. Documented in enemies/looter.md.
- Dead Branch relic: PROMOTED TO PLAYBOOK. Documented in relics/dead-branch.md.
- Wing Boots relic: PROMOTED TO PLAYBOOK. Documented in relics/wing-boots.md.

## Promoted from Run 71

- Pantograph heals 25 HP, not full HP: PROMOTED TO PLAYBOOK. Previous entry incorrectly stated "Heal to FULL HP." Corrected in relics/pantograph.md. Earlier runs where Pantograph appeared to fully heal were likely cases where the HP deficit was small enough that 25 HP brought the player near max.
- The Champ boss: PROMOTED TO PLAYBOOK. New entry created at bosses/the-champ.md. Execute mechanic documented: at ~50% HP, cleanses all debuffs, gains +8 Str and Metallicize 5.
- Dark Shackles card: PROMOTED TO PLAYBOOK. New entry created at cards/dark-shackles.md. 0E Skill, temporary Strength reduction, Exhaust.

## Unconfirmed

- Boss relic collection automation issue: In Run 71, a `proceed` command after Act 1 boss auto-collected the chest without showing boss relic selection options. This potentially cost a run-defining boss relic. May be a CommunicationMod or automation issue. Needs investigation -- is the boss relic choice screen being skipped, or is it presenting and auto-selecting?
- The Champ Execute exact HP threshold: Believed to be ~50% HP. Exact percentage or HP amount unconfirmed. Need more encounters to pin down the exact trigger.
- The Champ Execute Metallicize value: Observed as Metallicize 5. Need second data point to confirm this is consistent.
- The Champ Execute Strength gain: Observed as +8 Strength. Need second data point to confirm consistency.
- The Champ total HP: Not precisely recorded. Need exact HP from a future encounter.
- Dark Shackles exact Strength reduction amount: Reduces enemy Strength for 1 turn. Exact reduction amount not confirmed -- believed to match a fixed value or scale. Need precise observation.
- Golden Idol effect: Believed to increase gold earned by 25%. Taken but effect never directly measured.
- Odd Mushroom relic effect: Acquired in Run 4. Possibly +1 Dex or modifies Vulnerable. Never confirmed.
- Maw Bank relic effect: PROMOTED TO PLAYBOOK. Confirmed: 12 gold per non-shop floor, disabled when spending gold at shop.


- Flight damage halving rounding: Believed to be floor(damage/2). Not precisely confirmed.
- Council of Ghosts Apparition power: Prevents ALL damage for 1 turn each, Ethereal. Never used -- refused at 79 Max HP. Value vs cost (-40 Max HP) untested.
- Torii damage threshold: Triggers at 5 or less unblocked damage, reducing to 1. Confirmed against Burns. Does it work on all damage sources or only attacks?
- Molten Egg: Does it upgrade Attack cards from potions (Attack Potion, Skill Potion generating Attacks)?
- Lizard Tail heal amount: Believed to heal to 50% Max HP. Observed once. Needs second data point.
- Enchiridion Power pool: Confirmed to generate Brutality (Ironclad Power). Can it generate non-class Powers? Needs cross-class data point.
- Dream Catcher card pool: Same as normal rewards or different/restricted?
- Corruption + Second Wind interaction: Does Second Wind exhaust itself under Corruption? Needs confirmation.
- Blessing of the Forge: PROMOTED TO PLAYBOOK. Confirmed: upgrades a card in the deck. Can be used at rest sites for an extra upgrade alongside Smith. Used twice in a single run (once at rest site, once before boss).
- Vampires Max HP loss exact formula: Observed 80->56 (-24, 30% loss). Is it always 30% or a fixed amount? Needs second data point.
- Bite upgrade: Does Bite have an upgraded version? If so, what are the improved stats?
- Gremlin Leader summoning pattern: Does Leader re-summon immediately when gremlins die, or on specific turns? Rally confirmed to give +3 Str to ALL enemies. Re-summoning trigger still unconfirmed.
- Horn Cleat block amount: Observed 14 block on turn 2. Is this always 14 or does it scale?
- Slaver's Collar source: How is this relic obtained? Boss reward, shop, or event?
- Block values sometimes higher than expected: Player noted block values exceeding card text. Possible relic interaction (Horn Cleat turn 2?) or Dexterity source not accounted for.
- Wheel of Change full outcome table: Observed "Lose 8 HP" and "Heal to full health" as outcomes. Other possible outcomes unknown -- could include gold, card rewards, curses, relics. Need more data points to build a complete decision framework.
- Gremlin Horn exact trigger timing: Observed +1E and draw 1 on enemy death. Does it trigger on ALL enemy deaths including minion summons dying? Does it work with Torch Head deaths in Collector fight?
- Whetstone upgrade targeting: Described as "2 random Attack cards." Are Strikes included in the pool? Can it upgrade already-upgraded cards (no effect)?
- Heavy Blade exact damage formula: Confirmed 14 + Str*3 (unupgraded). At Str 1: 14+3=17. At Str 3: 14+9=23. Upgraded formula confirmed as 14 + Str*5 (used with Demon Form+ in Run 71 as core scaling engine against The Champ). PROMOTED TO PLAYBOOK: documented in cards/heavy-blade.md.

- Transient exact damage pattern: Turn 1 attack ~22, Turn 2 attack ~38 (with Str accumulation). Exact per-turn Strength gain unknown. Need more data points. Disarm (-2 Str) + Disarm+ (-3 Str) + Shockwave+ (Weak 3) reduced Turn 2 from ~38 to ~26 but still lethal at 15 HP.
- Writhing Mass exact HP: Observed ~160 HP. Exact amount not confirmed.
- Writhing Mass Malleable block scaling: Gains block per hit. Exact formula unknown. Single large hits (Hemokinesis, Immolate) are better than multi-hit. Need to confirm if Malleable resets each turn or accumulates.
- Darklings Life Link exact mechanic: Observed that dead Darklings revive at half HP. Does this happen immediately or at end of turn? Must all 3 die in the same turn, or within the same turn cycle?
- Spikers Thorns scaling: Observed Thorns 3 and Thorns 7 on different Spikers. Do Spikers start with different Thorns values or gain Thorns over time?
- Donu and Deca: Not yet encountered. Boss identified from Act 3 plan screen. Need first encounter data.
- Collector total HP: Player noted 282 HP on entry. Previous entry says 279. Need to confirm exact HP.
- Hard Rules compliance: Zero failures in Runs 63, 64, and 65. Three consecutive runs with zero compliance failures. Hard Rule 4 actively shaped gameplay in Run 65 (prevented True Grit unupgraded play). Rules are working as intended.
- Chosen 28-damage attack: Observed at 7x2 base with +3 Str accumulated and Vulnerable on player. Exact calculation: (7+3)*2 = 20, with Vulnerable: floor(20*1.5) = 30? Or 7x2=14 base, +Str scaling. Needs precise formula verification -- the 28 damage figure may include Vulnerable or may be a higher base attack pattern.
- Fiend Fire in Cultist+Chosen multi-fights: PROMOTED TO PLAYBOOK. Using Fiend Fire to kill Cultist exhausts defensive cards needed for Chosen. Confirmed death in Run 64 (14 HP, 13 block vs 28 incoming). Documented in cards/fiend-fire.md and enemies/chosen.md.
- Hard Rule 4 strategic tradeoff: Rule correctly prevented True Grit (unupgraded, random exhaust) from being played. However, in the Book of Stabbing fight, True Grit would have been the only Wound exhaust tool available. The rule prevents misplays but also removes options in fights where even random exhaust is better than Wound clog. The rule is still correct -- random exhaust of key cards is historically deadlier than Wound clog -- but this tradeoff is worth monitoring.
- Knowing Skull HP cost scaling: Observed 12 HP loss from a single interaction. Exact scaling formula unknown -- does it cost a flat amount per ask, or does the cost increase per subsequent ask? Need more data points.

- Spheric Guardian block growth rate: PROMOTED TO PLAYBOOK. Confirmed across 3 encounters: starts at 40 block, grows to 65+ by turn 4. Block gain is 15-20 per defend turn. Alternates ATTACK_DEFEND and DEFEND patterns. Documented in enemies/spheric-guardian.md.
- Spot Weakness+ upgrade confirmed: PROMOTED TO PLAYBOOK. +4 Str (up from +3) when enemy intends to attack. Observed twice in Hexaghost fight for total +8 Str. Documented in cards/spot-weakness.md.
- Dark Embrace + Second Wind interaction: Second Wind exhausts all non-Attacks, Dark Embrace draws 1 per exhaust. This combo works as expected but is dangerous -- it can draw into more Skills which are NOT exhausted (already resolved). The draw happens after all exhausts.
- Match and Keep card pool: Observed Bash and Perfected Strike as matchable cards. Are the cards drawn from a fixed pool, from the player's class, or random? Need more data.
- Rage+ duration: PROMOTED TO PLAYBOOK. Confirmed: Rage+ block-per-attack effect expires at end of the turn it is played. Despite being classified as a Power card, the effect is per-turn only. Player must replay Rage each turn to benefit. Documented in cards/rage.md.
- Lee's Waffle: Relic purchased from shop for 157g. Heals to full HP when resting at rest sites. Observed healing 31->87 HP at one rest site. Need to confirm if it also provides other benefits or if it is purely a rest-healing upgrade.
- Blood for Blood cost reduction: PROMOTED TO PLAYBOOK. Confirmed: cost reduces by 1 per instance of HP loss, not per point of HP lost. Reached 0E in Guardian fight, 3 Cultists fight, and Shelled Parasite fight. Brutality counts as a damage instance for cost reduction.
- Barricade (player card): PROMOTED TO PLAYBOOK. Documented at cards/barricade.md. 3E Power, block persists. Taken but never played in one run due to 3E cost consuming entire turn with no free turns available.

- Mugger exact HP and damage values: Estimated ~48-52 HP, ~10-12 damage per attack. Exact values need confirmation from a future encounter where we survive long enough to observe multiple turns.
- Mugger gold theft amount: Assumed similar to Looter (15 gold/turn). Exact amount unconfirmed.
- Corruption + Dead Branch random card quality: The engine generates random cards. Are the random cards drawn from the player's class pool, all cards, or a specific subset? Need observation from a fight where the engine actually activates.
- Corruption + Second Wind interaction: Does Second Wind exhaust itself under Corruption? Still unconfirmed (previously noted, still untested).
- Corruption upgrade availability: Was Corruption offered at rest sites or shops before the fatal fight? If so, was the upgrade skipped? Need to verify whether the player had an opportunity to upgrade Corruption to 2E and missed it.

## Prediction Errors (non-fatal, for monitoring)

- Weak multiplier applied incorrectly: Player calculated Strike+ damage as floor((9+9)*0.75) = 13 against Acid Slime (L), but Acid Slime does not apply Weak to the player. Correct damage should have been 18 (no multiplier reduction). The fight was won regardless, but this shows confusion about when the 0.75 Weak damage reduction applies. Weak reduces the PLAYER'S Attack damage when the player is Weakened, or reduces ENEMY Attack damage when the enemy is Weakened. If neither is Weakened, no 0.75 multiplier applies.
- Spheric Guardian incoming damage miscalculation: Player wrote "10 incoming" in turn 6 reasoning when Spheric Guardian does 10x2=20 on attack turns. In context, the Spheric Guardian was actually on a defend turn (player took 0 damage), so the "10 incoming" may have been from a Sentry or the player may have been confused about the attack pattern. Non-fatal but worth monitoring for future Spheric Guardian encounters.
- Rage+ misunderstood as permanent: Player played Rage+ on Turn 1 of Spheric Guardian fight and assumed it would provide 5 block per attack for the entire combat. On Turn 5, player explicitly planned around Rage block (wrote "Rage(5 from Strike) + Rage(5 from Iron Wave)"), but the block never appeared because Rage had expired on Turn 1. This directly caused the death -- 6 block vs 10 incoming at 1 HP. FATAL prediction error. CORRECTED in playbook: Rage+ expires at end of turn, documented in cards/rage.md.
- True Grit+ exhausting Spot Weakness: Player exhausted Spot Weakness on Turn 1 of Spheric Guardian fight, reasoning "cant trigger this turn, deck thinning is valuable." This removed the only Strength scaling option for the entire fight. In hindsight, Spot Weakness's permanent +3 Str was critical for breaking through Barricade block. Strategic error -- exhaust Strikes and Defends before situational but powerful cards.

- Pantograph full heal assumption: FATAL prediction error. Playbook stated Pantograph "heals to FULL HP." Player entered The Champ at 49/87 HP expecting to heal to 87/87. Pantograph healed only 25 HP (to 74/87). The 13 HP shortfall (87-74=13) combined with The Champ's post-Execute damage caused death at 7 HP. If the player had known the actual heal amount, they could have prioritized healing before the boss or adjusted strategy. CORRECTED in playbook: relics/pantograph.md now states 25 HP. Previous "full heal" observations from Runs 63 were likely small deficits where 25 HP happened to bring HP near max (e.g., entering at 55/80 = 25 deficit = healed to 80).

- Corruption played into multi-enemy fight without block: FATAL prediction error. Player played Corruption (3E) on turn 1 against Looter + Mugger, leaving zero energy for Defend. Combined enemy damage was 20+ unblocked. The player likely assumed the Corruption + Dead Branch engine would generate enough value to compensate, but the engine requires at least one full turn of Skill plays to start generating cards. The setup turn is a pure tempo loss. This is the same category of error as playing Barricade (3E) into active enemies -- expensive Powers must wait for free turns or require energy surplus. ADDRESSED in playbook: corruption.md updated with SETUP COST TRAP section.

- Feel No Pain block and Frail interaction: Does Frail reduce FNP's 3 block per exhaust? FNP is a Power effect, not a card play. Frail says "block gained from cards is reduced by 25%." If FNP block is classified as "from a Power trigger" rather than "from a card," it would be unaffected by Frail. This matters in Slime Boss fights where Spike Slime L applies Frail. Needs in-game testing.
- Disarm Strength reduction vs Slime Boss split: Confirmed that pre-split Disarm does NOT carry to split slimes. The split creates new enemy instances with base stats. Play Disarm post-split, not pre-split.
- Slimed card generation timing vs split mechanics: Do Slimed cards get added to the deck during the split turn itself, or only on subsequent enemy attack turns? If Slimed is added during the split transition, the hand clog starts immediately. Needs precise observation.
- Frail interaction with Rage block: Does Frail reduce block gained from Rage (a Power triggering on Attack plays)? Frail says "Block gained from cards is reduced by 25%." Rage block is gained from a Power effect, not directly from a card play. This distinction may mean Rage block is NOT reduced by Frail. Needs confirmation -- the question was raised but never tested because Rage expired before the Frail turns.
- Spheric Guardian Frail application: PROMOTED TO PLAYBOOK. Applies Frail 5 at start of fight. Confirmed in all 3 encounters. Documented in enemies/spheric-guardian.md.

## Open Questions

- Shop bug root cause: Recurring in ~37% of runs. CommunicationMod, state_formatter, or cmd.py issue?
- Face Trader event: What are the actual options and outcomes?
- Transmogrifier transform rules: Does it keep the same rarity?
- Ancient Writing second option (Insight): What does it offer?
- The Joust odds: 70% win chance for Murderer accurate?
- Confusion interaction with X-cost cards: Unconfirmed.
- Frail block calculation under player reasoning: Player wrote "2x Defend (10 block w/ Frail)" but Frail should reduce 5 to 3. Possible miscalculation.
- Healing card availability: PARTIALLY ANSWERED. Run 53 confirms Reaper/Feed can be denied by RNG entirely. Runs 51, 57 took Reaper when offered. Run 59 took Feed. The priority rule IS working when cards appear. The gap is now addressed with a backup healing plan in strategy.md.
- Bronze Automaton Stasis targeting: Does Stasis preferentially steal Powers/Skills, or is it random? Observed stealing Double Tap+ (Skill) and Inflame (Power). Need more data points.
- Bronze Automaton Hyper Beam exact damage: Not precisely measured. Believed to be very high single-hit. Need exact number.
- Kunai trigger counting: Does Whirlwind count as 1 Attack or X Attacks for Kunai's 3-Attack threshold? Believed to count as 1 play regardless of hits. Needs confirmation.

## Recurring Patterns (for strategist review)

- Index shifting: ADDRESSED in Strategist Review 2 — moved to player.md Hard Rule #2. Four confirmed deaths (Runs 3, 21, 22, 57). Monitor future runs for compliance.
- Potion hoarding partially fixed: Run 20 used potions aggressively. But Run 50 had Blessing of the Forge unused at death. Hard Rule #5 now addresses this.
- Unknown rooms as combat: Runs 20 and 44 hit dangerous fights from Unknown rooms. Unknown rooms are NOT safe at low HP. Documented in strategy.md.
- **Runic Dome compliance failure:** ADDRESSED in Strategist Review 2 — moved to player.md Hard Rule #1. Two deaths from taking it. Run 63: NO FAILURE (boss relic swap gave Sozu, not Runic Dome -- player correctly refused to take Runic Dome in prior runs). Monitor continues.
- **Zero-upgrade compliance failure:** ADDRESSED in Strategist Review 2 — moved to player.md Hard Rule #3. Run 63: Bash+ upgraded Floor 3, Armaments+ upgraded Floor 12, multiple cards upgraded via Armaments+ mid-combat, Immolate+ and Thunderclap+ at rest sites. COMPLIANT.
- **Random exhaust compliance failure:** ADDRESSED in Strategist Review 2 — moved to player.md Hard Rule #4. Run 63: Player correctly refused Havoc and unupgraded True Grit from card rewards. COMPLIANT.
- **Brutality in long fights:** ADDRESSED in Strategist Review 3 — moved to player.md Hard Rule #6. Confirmed death at full HP (Run 72) from Brutality self-damage over 6 turns. Also played vs Book of Stabbing in Run 65 (generated by Enchiridion). Monitor future runs for compliance.
- **Exhausting key cards (Spot Weakness, Shockwave+):** ADDRESSED in Strategist Review 3 — moved to player.md Hard Rule #7. Run 72: Spot Weakness exhausted via True Grit+ on turn 1 of Spheric Guardian fight. Run 69: Second Wind exhausted Shockwave+, True Grit+, and Defend+. Both directly caused deaths. Monitor future runs.
- **Spheric Guardian as top killer (3 deaths):** ADDRESSED in Strategist Review 3 — strategy.md updated with Strength scaling requirement. Spheric Guardian now tied with 3 Cultists for most lethal encounter. Unknown rooms in Act 2 are the primary spawn source (all 3 deaths from Unknown rooms). Monitor future encounters.
- **Boss relic collection skipped (Run 71):** A `proceed` command after the Act 1 boss auto-collected the chest without presenting boss relic selection. This may be a CommunicationMod or command-handling issue. If the player is not offered a boss relic choice, every run after Act 1 misses a critical power spike. Needs investigation and possible fix in the automation layer.
- **3E Power setup deaths (Corruption, Barricade):** Run 73: Corruption (3E) played turn 1 into Looter + Mugger, zero block, died to 20+ unblocked. Run 72: Barricade (3E) taken but never played due to no free turns. Pattern: 3E Powers that provide no immediate block or damage are unplayable into active enemies without energy surplus. The player must either upgrade them to reduce cost, wait for a free turn, or have 4+ energy. This is now a recurring pattern across multiple cards. Consider adding a Hard Rule: "Never play a 3E Power on turn 1 unless the enemy intent is non-damaging."
