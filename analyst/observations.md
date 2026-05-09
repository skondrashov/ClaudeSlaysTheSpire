# Observations

Items pending confirmation or further investigation. Promote to playbook when confident.

## Promoted (archived — already in playbook)

Preserved Insect, Upgrade death spiral (3x confirmed), Slime Boss split threshold, Disarm vs Slime Boss split, Corruption + Dead Branch synergy, Corruption setup cost trap, Mugger enemy, Looter + Mugger pairing, Dead Branch relic, Wing Boots relic, Pantograph 25 HP correction, The Champ boss + Execute mechanic, Dark Shackles card, Maw Bank relic, Spheric Guardian block growth rate, Spot Weakness+ upgrade, Rage+ per-turn expiration, Blood for Blood cost reduction, Barricade (player card), Fiend Fire in Cultist+Chosen multi-fights, Heavy Blade damage formula, Blessing of the Forge, Spheric Guardian Frail application, Eternal Feather relic, Oddly Smooth Stone relic, Masked Bandits event, Gremlin Leader Rally +3 Str ALL (3x confirmed), Uppercut+ upgrade (2 Weak + 2 Vuln confirmed), Spheric Guardian 4th death + Demon Form insufficient, Uppercut+ Artifact stripping vs SG confirmed, Spheric Guardian first survival (Corruption + FNP engine), Feed+ multi-kill Max HP gain (+22 from Slime Boss), Bloodletting card, Battle Trance sequencing warning, Fairy in a Bottle elite consumption timing, Intimidate upgrade (2 Weak), Gremlin Leader turn economy + Rally scaling math, Brimstone relic, Sword Boomerang card, Snake Plant 9x3 damage correction, Brimstone + Demon Form combo (+4 Str/turn), Calipers relic, Impervious+ upgrade (40 block), Spheric Guardian second survival (Immolate+Impervious++Calipers+Spot Weakness), Weak multiplier direction error (systematic, 3+ runs), Liquid Memories exhaust/discard confusion, Block-first at critical HP rule, Fire Breathing+ exhaust synergy blindness (Immolate Burns), Bronze Automaton Stasis targeting (Powers/Skills), Bronze Automaton Hyper Beam scaling (38-51), Brimstone + Book of Stabbing anti-synergy (2 deaths), 3 Cultists 60% threshold (6 deaths), Corruption vs Guardian trap (Hard Rule #9), Hexaghost Turn 2 blocking mandatory, SIO+ upgraded value (11 not 8), Strength/Rampage reset between combats, Confusion + X-cost cards interaction.

## Unconfirmed

- Boss relic collection automation issue: In Run 71 and Run 77, a `proceed` command after Act 1 boss auto-collected the chest without showing boss relic selection options. Confirmed recurring (2 occurrences). CommunicationMod or automation bug. STILL UNRESOLVED. Needs infrastructure investigation.
- Healing card RNG denial streak: 7 of last 9 runs with no Reaper/Feed offered. Backup healing plan insufficient. Not addressable through playbook changes -- this is variance. Player should take Feed even in late Act 1 (floor 12+) and buy Blood/Regen Potions at every shop when no healing card exists.
- Hexaghost multi-hit attack variants: Turn 2 appears to be 5x6=30 (not Inferno). Later turns have 4x6=24 variant. Need more data points with exact hit counts.
- Burns+ timing: Burns+ (4 damage each) appear from later ATTACK_DEBUFF turns. Exact transition turn unknown.
- Horn Cleat: Observed 14 block on turn 2. Fixed or scaling?
- Gremlin Horn: Works on ALL enemy deaths including minions?
- Whetstone: Can upgrade already-upgraded cards?
- Collector total HP: 279 or 282? Conflicting observations.
- Knowing Skull HP cost: Flat or increasing per interaction?
- Corruption + Second Wind: Does Second Wind exhaust itself under Corruption?
- Feel No Pain + Frail: Is FNP block reduced by Frail?
- Frail + Rage block: Is Rage block reduced by Frail?
- Kunai + Whirlwind: Does each hit count as a separate attack for Kunai?
- Book of Stabbing per-hit damage: 6 or 7 per hit? Need confirmation.
- Donu and Deca: Not yet encountered.

## Prediction Errors (non-fatal, monitoring)

**Recurring arithmetic error patterns (ALL promoted to COMBAT ARITHMETIC CHECKLIST in strategy.md):**
- Weak direction confusion: applied 0.75 to own damage when enemies Weakened (Runs 63, 124)
- Upgraded value misuse: SIO+ as 8 instead of 11 (Run 125), Armaments+ block forgotten (Run 126)
- Flame Barrier+ block/counter confusion: used counter value (6) as block value (16) (Run 125)
- Strength carryover between combats: calculated damage with Str from previous fight (Run 127)
- Rampage counter carryover: self-corrected mid-reasoning (Run 125). Monitor.
- Hexaghost HP tracking drift: lost count of boss HP mid-fight (Run 129). Monitor.

**Strategic errors (promoted to relevant playbook files):**
- Fire Breathing+ exhaust synergy blindness: PROMOTED to fire-breathing.md
- Block-first at critical HP: PROMOTED to strategy.md, slavers.md
- Demon Form + Stasis vulnerability: Demon Form stolen by Stasis in Run 125, never replayed. Inflame (1E, immediate, cannot be stolen after play) is better against Bronze Automaton. Documented in bronze-automaton.md.
- Red Mask strips 1 Artifact at combat start. Documented in bronze-automaton.md and red-mask.md.
- Headbutt grid interaction: UI misplay in Run 78. Not recurred. Low priority.

## Recurring Patterns (all addressed by Hard Rules, monitoring only)

Hard Rules 1-9 all have zero violations since implementation. No new Hard Rule needed at this time. The recurring patterns that are NOT addressed by Hard Rules:
- **Arithmetic errors in combat** -- NOT a Hard Rule issue. Six different errors in runs 124-129. Now addressed by COMBAT ARITHMETIC CHECKLIST in strategy.md.
- **Boss relic collection skipped** (Run 71, Run 77): Automation bug. STILL UNRESOLVED. Needs infrastructure investigation.

## Open Questions

- Face Trader event options and outcomes
- Transmogrifier: does it keep the same rarity?
- Ancient Writing: what does the Insight option offer?
- The Joust: 70% win chance for Murderer accurate?
- Offering self-damage at sub-30% HP: 6 HP cost was exactly lethal margin in Run 128. Monitor whether Offering at critical HP causes deaths.
- Dual RNG denial: Run 128 had both healing AND Strength scaling denied across 24 floors despite Prayer Wheel. Two criteria denied simultaneously makes runs near-unwinnable. No fix possible -- pure variance.
