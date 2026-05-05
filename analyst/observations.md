# Observations

Items pending confirmation or further investigation. Promote to reference/ when confident.

## Unconfirmed

- Speed Potion exact Dexterity amount: Observed +5 Dexterity in one use (Run 1 vs Slime Boss, Defend went from 5 to 10 block). Needs second observation to confirm.
- Dazed mechanic details: Believed to be Unplayable + Ethereal (auto-exhausts at end of turn if in hand). Observed in Chosen and Sentry fights but exact interaction needs confirmation.
- Hex duration/stacking: Hex debuff from Chosen triggers on each Skill played (adds Dazed to draw pile). Duration and whether it stacks with multiple applications unclear.
- Golden Idol effect: Believed to increase gold earned by 25%. Taken in Runs 1 and 3 but effect never directly observed in gameplay.
- Odd Mushroom relic effect: Acquired in Run 4. Player guessed "+1 Dex or modifies Vulnerable." Never directly confirmed.
- Anchor relic effect: Inferred as "gain 10 block at start of each combat" from Run 5 combat patterns. Not directly confirmed.
- Happy Flower relic: Believed to grant 1 energy every 3 turns. Acquired in Run 8, effect inferred from standard game knowledge.
- Toy Ornithopter relic: Believed to heal 5 HP whenever a potion is used. Acquired in Run 8, effect inferred from standard game knowledge.
- Liquid Bronze relic: Believed to deal 3 thorns damage when hit by attacks. Acquired in Run 7. Multi-hit thorns interaction (e.g., 7x Inferno = 21 thorns) assumed but not precisely confirmed.
- Maw Bank relic: Acquired in Run 6 for 85 gold. Effect unknown, likely gold-related.
- Blood Vial/Blood Potion formula: Observed 16 HP heal on 83 max HP in Run 6. Inferred floor(maxHP * 0.2). Needs second data point.
- Mode Shift initial value: Run 2 observed starting at 27 (not 10 as previously thought). Later cycle values (40, 50) need reconfirmation.
- Flight damage halving rounding: Believed to be floor(damage/2) but exact rounding not confirmed. Math example from Run 3 showed Pommel Strike (9 damage) dealing ~4-5 vs Flight 3 Byrd.
- Council of Ghosts Apparition power: Apparitions prevent ALL damage for 1 turn each, Ethereal. Never actually used — refused in Run 4 at 79 Max HP. Value vs cost (-40 Max HP) untested.
- Torii damage threshold: Believed to trigger at 5 or less unblocked damage, reducing to 1. Confirmed against Burns (2->1) in Runs 11 and 12. Does it work on all sources or only attacks? Hexaghost Inferno individual hits at 6 damage each may be above the threshold.
- Molten Egg upgrade scope: Confirmed to auto-upgrade Attack cards obtained after acquiring it. Does it also upgrade Attack cards from potions (Attack Potion, Skill Potion generating Attacks)? Needs confirmation.
- Lizard Tail heal amount: Believed to heal to 50% Max HP. Observed once in Run 13. Needs second observation to confirm exact percentage.
- Enchiridion Power pool: What Powers can Enchiridion generate? Observed Corruption in Run 13. Can it generate any Power in the game, or only class-specific Powers?
- Dream Catcher card pool: Does Dream Catcher at rest sites offer the same card pool as normal rewards? Or is it a different/restricted pool?

- Potion use discipline failure pattern: Across deaths at low HP, potions are frequently unused. The strategy.md guidance says "use ALL potions aggressively" but the player still hoards them. Is the issue that the guidance isn't specific enough about WHEN the threshold triggers? Hypothesis: the player needs a hard rule like "below 35% HP = use every potion on turn 1, no exceptions" rather than the softer "use aggressively."
- Power Through deck-building trap: When taken without exhaust tools, creates a negative feedback loop in long fights. Wounds reduce block density, which increases damage taken, which makes the fight longer, which means more Wound cycling. Need to confirm whether this is unique to Power Through or applies to any status-generating card (Wild Strike Wounds, Reckless Charge Dazed).
- Looter+Mugger fight HP cost: This fight drained from some higher HP to 18/72. What is the typical HP cost of Looter+Mugger? If consistently 20-30+ HP, it should be documented as a "drain fight" alongside Byrds and Centurion+Mystic.

## Open Questions

- Shop bug root cause: Recurring in 3/8 runs (37.5%). Is this a CommunicationMod issue, a state_formatter issue, or a cmd.py issue? The `choose` probe workaround has not been fully tested.
- Face Trader event: Encountered in Run 3, player left at low HP. What are the actual options and outcomes?
- Transmogrifier transform rules: Does it keep the same rarity? Run 4 transformed Strike into Headbutt (both Common). Need more data.
- Ancient Writing second option: Player chose Simplicity (upgrade all Strikes/Defends). The other option ([Insight]) was not explored. What does it offer?
- The Joust odds: Listed as 70% win chance for Murderer. Is this accurate? Run 5 appeared to lose. Expected value calculation needs verification.
- Rampage+ starting damage: Observed scaling 12->20->28->36->48->60 in Run 13. Does Rampage+ start at 12 damage (vs 8 base)? Or does it start at 8 and scale +8? The sequence 12, 20, 28... fits +8 increments starting at 12. Need confirmation of base Rampage starting damage.
- Shelled Parasite mechanics: CONFIRMED. HP 68-71, Plated Armor 14, attacks for 13+ damage. Promoted to playbook/enemies/shelled-parasite.md with full details.
- Snecko confusion mechanic: Snecko applies cost confusion (randomizes card costs 0-3). Exact duration, whether it stacks, and interaction with X-cost cards need confirmation.
- Corruption interaction with Second Wind: Does Second Wind exhaust itself after use (since it's a Skill under Corruption)? If so, it becomes a one-time mass exhaust for block. Need confirmation.
- Brutality HP threshold for multiple copies: Run 13 died playing 2 copies at 10 HP. What's the safe HP threshold for playing 2 Brutalities? Hypothesis: 40+ HP for 2 copies in a fight expected to last 5+ turns.
