# Observations

Items pending confirmation or further investigation. Promote to playbook when confident.

## Unconfirmed

- Golden Idol effect: Believed to increase gold earned by 25%. Taken but effect never directly measured.
- Odd Mushroom relic effect: Acquired in Run 4. Possibly +1 Dex or modifies Vulnerable. Never confirmed.
- Maw Bank relic effect: Acquired in Run 6. Likely gold-related. Never confirmed.
- Blood Vial/Blood Potion formula: Observed 16 HP heal on 83 max HP. Inferred floor(maxHP * 0.2). Needs second data point.
- Mode Shift initial value: Run 2 observed starting at 27 (not 10). Later cycle values (40, 50) need reconfirmation.
- Flight damage halving rounding: Believed to be floor(damage/2). Not precisely confirmed.
- Council of Ghosts Apparition power: Prevents ALL damage for 1 turn each, Ethereal. Never used -- refused at 79 Max HP. Value vs cost (-40 Max HP) untested.
- Torii damage threshold: Triggers at 5 or less unblocked damage, reducing to 1. Confirmed against Burns. Does it work on all damage sources or only attacks?
- Molten Egg: Does it upgrade Attack cards from potions (Attack Potion, Skill Potion generating Attacks)?
- Lizard Tail heal amount: Believed to heal to 50% Max HP. Observed once. Needs second data point.
- Enchiridion Power pool: Can it generate any Power, or only class-specific?
- Dream Catcher card pool: Same as normal rewards or different/restricted?
- Corruption + Second Wind interaction: Does Second Wind exhaust itself under Corruption? Needs confirmation.
- Blessing of the Forge exact mechanic: Random card in deck vs random card in hand? Never used.
- Vampires Max HP loss exact formula: Observed 80->56 (-24, 30% loss). Is it always 30% or a fixed amount? Needs second data point.
- Bite upgrade: Does Bite have an upgraded version? If so, what are the improved stats?
- Gremlin Leader summoning pattern: Does Leader re-summon immediately when gremlins die, or on specific turns? Need to observe the exact trigger.
- Horn Cleat block amount: Observed 14 block on turn 2. Is this always 14 or does it scale?
- Slaver's Collar source: How is this relic obtained? Boss reward, shop, or event?
- Block values sometimes higher than expected: Player noted block values exceeding card text. Possible relic interaction (Horn Cleat turn 2?) or Dexterity source not accounted for.

## Open Questions

- Shop bug root cause: Recurring in ~37% of runs. CommunicationMod, state_formatter, or cmd.py issue?
- Face Trader event: What are the actual options and outcomes?
- Transmogrifier transform rules: Does it keep the same rarity?
- Ancient Writing second option (Insight): What does it offer?
- The Joust odds: 70% win chance for Murderer accurate?
- Confusion interaction with X-cost cards: Unconfirmed.
- Frail block calculation under player reasoning: Player wrote "2x Defend (10 block w/ Frail)" but Frail should reduce 5 to 3. Possible miscalculation.
- Is the player not being OFFERED healing cards, or skipping them? Critical question for the healing sustain gap.

## Recurring Patterns (for strategist review)

- Index shifting: Despite documentation, player used numeric indices in Runs 21 and 22 against 3 Cultists. Both resulted in fatal misplays. The fix may need to be in the system prompt, not the playbook.
- Potion hoarding partially fixed: Run 20 used potions aggressively. But Run 50 had Blessing of the Forge unused at death.
- Unknown rooms as combat: Runs 20 and 44 hit dangerous fights from Unknown rooms. Unknown rooms are NOT safe at low HP.
