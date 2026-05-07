# Observations

Items pending confirmation or further investigation. Promote to playbook when confident.

## Unconfirmed

- Golden Idol effect: Believed to increase gold earned by 25%. Taken but effect never directly measured.
- Odd Mushroom relic effect: Acquired in Run 4. Possibly +1 Dex or modifies Vulnerable. Never confirmed.
- Maw Bank relic effect: Acquired in Run 6. Likely gold-related. Never confirmed.


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
- Gremlin Leader summoning pattern: Does Leader re-summon immediately when gremlins die, or on specific turns? Rally confirmed to give +3 Str to ALL enemies. Re-summoning trigger still unconfirmed.
- Horn Cleat block amount: Observed 14 block on turn 2. Is this always 14 or does it scale?
- Slaver's Collar source: How is this relic obtained? Boss reward, shop, or event?
- Block values sometimes higher than expected: Player noted block values exceeding card text. Possible relic interaction (Horn Cleat turn 2?) or Dexterity source not accounted for.
- Wheel of Change full outcome table: Only observed "Lose 8 HP" as an outcome. Other possible outcomes unknown -- could include gold, card rewards, curses, healing, relics. Need more data points to build a complete decision framework.
- Gremlin Horn exact trigger timing: Observed +1E and draw 1 on enemy death. Does it trigger on ALL enemy deaths including minion summons dying? Does it work with Torch Head deaths in Collector fight?
- Whetstone upgrade targeting: Described as "2 random Attack cards." Are Strikes included in the pool? Can it upgrade already-upgraded cards (no effect)?
- Heavy Blade exact damage formula: Confirmed 14 + Str*3 (unupgraded). At Str 1: 14+3=17. At Str 3: 14+9=23. Upgraded formula believed to be 14 + Str*5 but not yet observed in upgraded form.

## Prediction Errors (non-fatal, for monitoring)

- Weak multiplier applied incorrectly: Player calculated Strike+ damage as floor((9+9)*0.75) = 13 against Acid Slime (L), but Acid Slime does not apply Weak to the player. Correct damage should have been 18 (no multiplier reduction). The fight was won regardless, but this shows confusion about when the 0.75 Weak damage reduction applies. Weak reduces the PLAYER'S Attack damage when the player is Weakened, or reduces ENEMY Attack damage when the enemy is Weakened. If neither is Weakened, no 0.75 multiplier applies.

## Open Questions

- Shop bug root cause: Recurring in ~37% of runs. CommunicationMod, state_formatter, or cmd.py issue?
- Face Trader event: What are the actual options and outcomes?
- Transmogrifier transform rules: Does it keep the same rarity?
- Ancient Writing second option (Insight): What does it offer?
- The Joust odds: 70% win chance for Murderer accurate?
- Confusion interaction with X-cost cards: Unconfirmed.
- Frail block calculation under player reasoning: Player wrote "2x Defend (10 block w/ Frail)" but Frail should reduce 5 to 3. Possible miscalculation.
- Is the player not being OFFERED healing cards, or skipping them? Critical question for the healing sustain gap. Run 52 confirms at least one case where Reaper and Feed were never offered across the entire run. The healing priority rule is working (player would take them if offered) but card pool RNG can deny healing cards entirely.
- Bronze Automaton Stasis targeting: Does Stasis preferentially steal Powers/Skills, or is it random? Observed stealing Double Tap+ (Skill) and Inflame (Power). Need more data points.
- Bronze Automaton Hyper Beam exact damage: Not precisely measured. Believed to be very high single-hit. Need exact number.
- Kunai trigger counting: Does Whirlwind count as 1 Attack or X Attacks for Kunai's 3-Attack threshold? Believed to count as 1 play regardless of hits. Needs confirmation.

## Recurring Patterns (for strategist review)

- Index shifting: Despite documentation, player continues to use numeric indices. Four confirmed deaths (Runs 3, 21, 22, 57) directly caused by index shifting. Run 57 also had shop index confusion (bought Sever Soul instead of Flame Barrier). The playbook fix is clearly insufficient -- the player reads the rule but does not follow it. This is a SYSTEM-LEVEL problem that likely needs to be addressed in the player agent's system prompt or hard-coded into the command interface, not just documented in the playbook.
- Potion hoarding partially fixed: Run 20 used potions aggressively. But Run 50 had Blessing of the Forge unused at death.
- Unknown rooms as combat: Runs 20 and 44 hit dangerous fights from Unknown rooms. Unknown rooms are NOT safe at low HP.
- **Runic Dome compliance failure (CRITICAL):** Player has now taken Runic Dome TWICE despite explicit playbook guidance saying "refuse it" / "skip Runic Dome." This is not a knowledge gap -- the playbook clearly states the downside. The player reads the guidance but does not follow it. Playbook language has been escalated to absolute prohibition ("DO NOT TAKE. ALWAYS REFUSE."). If this continues, it is a system-level compliance problem identical to the index shifting pattern.
- **Zero-upgrade compliance failure:** Player completed an entire 23-floor run without a single upgrade. Strategy says upgrade at rest sites above 35% (Act 1) / 40% (Act 2). Either the player never visited rest sites, or visited them and chose to rest when HP was above threshold. This needs investigation in the event log. Language in strategy.md has been strengthened with a mandatory rule.
