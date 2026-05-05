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

## Open Questions

- Shop bug root cause: Recurring in 3/8 runs (37.5%). Is this a CommunicationMod issue, a state_formatter issue, or a cmd.py issue? The `choose` probe workaround has not been fully tested.
- Cursed Tome event: Encountered in Run 4, player left immediately. What does it actually offer?
- Face Trader event: Encountered in Run 3, player left at low HP. What are the actual options and outcomes?
- Transmogrifier transform rules: Does it keep the same rarity? Run 4 transformed Strike into Headbutt (both Common). Need more data.
- Ancient Writing second option: Player chose Simplicity (upgrade all Strikes/Defends). The other option ([Insight]) was not explored. What does it offer?
- The Joust odds: Listed as 70% win chance for Murderer. Is this accurate? Run 5 appeared to lose. Expected value calculation needs verification.
