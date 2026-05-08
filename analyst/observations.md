# Observations

Items pending confirmation or further investigation. Promote to playbook when confident.

## Promoted (archived — already in playbook)

Preserved Insect, Upgrade death spiral (3x confirmed), Slime Boss split threshold, Disarm vs Slime Boss split, Corruption + Dead Branch synergy, Corruption setup cost trap, Mugger enemy, Looter + Mugger pairing, Dead Branch relic, Wing Boots relic, Pantograph 25 HP correction, The Champ boss + Execute mechanic, Dark Shackles card, Maw Bank relic, Spheric Guardian block growth rate, Spot Weakness+ upgrade, Rage+ per-turn expiration, Blood for Blood cost reduction, Barricade (player card), Fiend Fire in Cultist+Chosen multi-fights, Heavy Blade damage formula, Blessing of the Forge, Spheric Guardian Frail application.

## Unconfirmed

- Boss relic collection automation issue: In Run 71, a `proceed` command after Act 1 boss auto-collected the chest without showing boss relic selection options. May be a CommunicationMod or automation issue. Needs investigation.
- The Champ Execute exact HP threshold: Believed to be ~50% HP. Exact percentage unconfirmed.
- The Champ Execute Metallicize value: Observed as Metallicize 5. Need second data point.
- The Champ Execute Strength gain: Observed as +8 Strength. Need second data point.
- The Champ total HP: Not precisely recorded.
- Dark Shackles exact Strength reduction amount: Exact value unconfirmed.
- Golden Idol effect: Believed to increase gold earned by 25%. Never directly measured.
- Odd Mushroom relic effect: Acquired in Run 4. Possibly +1 Dex or modifies Vulnerable. Never confirmed.
- Flight damage halving rounding: Believed to be floor(damage/2). Not confirmed.
- Council of Ghosts Apparition power: Prevents ALL damage for 1 turn each, Ethereal. Value vs cost (-40 Max HP) untested.
- Torii damage threshold: Triggers at 5 or less unblocked damage, reducing to 1. Does it work on all damage sources?
- Molten Egg: Does it upgrade Attack cards from potions?
- Lizard Tail heal amount: Believed to heal to 50% Max HP. Needs second data point.
- Enchiridion Power pool: Confirmed Brutality (Ironclad Power). Can it generate non-class Powers?
- Dream Catcher card pool: Same as normal rewards or different/restricted?
- Corruption + Second Wind interaction: Does Second Wind exhaust itself under Corruption?
- Vampires Max HP loss exact formula: Observed 80->56 (-24, 30% loss). Fixed amount or percentage?
- Bite upgrade: Does Bite have an upgraded version?
- Gremlin Leader summoning pattern: Re-summoning trigger unconfirmed.
- Horn Cleat block amount: Observed 14 block on turn 2. Always 14 or scaling?
- Slaver's Collar source: How is this relic obtained?
- Wheel of Change full outcome table: Observed "Lose 8 HP" and "Heal to full." Other outcomes unknown.
- Gremlin Horn exact trigger timing: Works on ALL enemy deaths including minions?
- Whetstone upgrade targeting: Are Strikes included? Can it upgrade already-upgraded cards?
- Transient exact damage/Strength pattern: Turn 1 ~22, Turn 2 ~38. Exact per-turn Str gain unknown.
- Writhing Mass exact HP: Observed ~160 HP. Exact amount unconfirmed.
- Writhing Mass Malleable block scaling: Per hit. Exact formula unknown. Resets each turn or accumulates?
- Darklings Life Link exact mechanic: Revive at half HP. Immediately or end of turn?
- Spikers Thorns scaling: Do Spikers start with different Thorns values or gain over time?
- Donu and Deca: Not yet encountered. Need first encounter data.
- Collector total HP: 279 or 282? Conflicting observations.
- Chosen 28-damage calculation: Needs exact formula verification.
- Knowing Skull HP cost scaling: Flat or increasing per interaction?
- Mugger exact HP/damage values: Estimated ~48-52 HP, ~10-12 damage. Needs confirmation.
- Mugger gold theft amount: Assumed similar to Looter (15 gold/turn). Unconfirmed.
- Corruption + Dead Branch random card pool: Class-specific, all cards, or subset?
- Lee's Waffle full effect: Heals to full HP when resting. Other benefits?
- Dark Embrace + Second Wind interaction: Draw happens after all exhausts resolve.
- Match and Keep card pool: Class-specific or random?
- Feel No Pain block and Frail interaction: Is FNP block reduced by Frail?
- Frail interaction with Rage block: Is Rage block reduced by Frail?
- Bronze Automaton Stasis targeting: Random or preferential?
- Bronze Automaton Hyper Beam exact damage: Very high single-hit. Need exact number.
- Kunai trigger counting: Does Whirlwind count as 1 or X attacks for Kunai?

## Prediction Errors (non-fatal, for monitoring)

- Weak multiplier applied incorrectly (Run 63): Player confused about when 0.75 multiplier applies.
- Spheric Guardian incoming damage miscalculation: Confused attack pattern timing.
- True Grit+ exhausting Spot Weakness: Strategic error -- exhaust low-value cards first.

## Recurring Patterns (for strategist review)

- Index shifting: ADDRESSED (Hard Rule #2). Monitor.
- Potion hoarding: PARTIALLY ADDRESSED (Hard Rule #5). Monitor.
- Unknown rooms as combat: Documented in strategy.md. Monitor.
- Runic Dome: ADDRESSED (Hard Rule #1). Zero failures since Run 63. Monitor.
- Zero-upgrade: ADDRESSED (Hard Rule #3). Monitor.
- Random exhaust: ADDRESSED (Hard Rule #4). Monitor.
- Brutality in long fights: ADDRESSED (Hard Rule #6). Monitor.
- Exhausting key cards: ADDRESSED (Hard Rule #7). Monitor.
- 3E Power setup deaths: ADDRESSED (Hard Rule #8). Two deaths (Run 72 Barricade unplayable, Run 73 Corruption fatal). Monitor.
- Boss relic collection skipped (Run 71): Possible automation bug. Needs investigation.

## Open Questions

- Shop bug root cause: Recurring in ~37% of runs. CommunicationMod, state_formatter, or cmd.py issue?
- Face Trader event: What are the actual options and outcomes?
- Transmogrifier transform rules: Does it keep the same rarity?
- Ancient Writing second option (Insight): What does it offer?
- The Joust odds: 70% win chance for Murderer accurate?
- Confusion interaction with X-cost cards: Unconfirmed.
