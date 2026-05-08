# Observations

Items pending confirmation or further investigation. Promote to playbook when confident.

## Promoted (archived — already in playbook)

Preserved Insect, Upgrade death spiral (3x confirmed), Slime Boss split threshold, Disarm vs Slime Boss split, Corruption + Dead Branch synergy, Corruption setup cost trap, Mugger enemy, Looter + Mugger pairing, Dead Branch relic, Wing Boots relic, Pantograph 25 HP correction, The Champ boss + Execute mechanic, Dark Shackles card, Maw Bank relic, Spheric Guardian block growth rate, Spot Weakness+ upgrade, Rage+ per-turn expiration, Blood for Blood cost reduction, Barricade (player card), Fiend Fire in Cultist+Chosen multi-fights, Heavy Blade damage formula, Blessing of the Forge, Spheric Guardian Frail application, Eternal Feather relic, Oddly Smooth Stone relic, Masked Bandits event, Gremlin Leader Rally +3 Str ALL (3x confirmed), Uppercut+ upgrade (2 Weak + 2 Vuln confirmed), Spheric Guardian 4th death + Demon Form insufficient, Uppercut+ Artifact stripping vs SG confirmed, Spheric Guardian first survival (Corruption + FNP engine), Feed+ multi-kill Max HP gain (+22 from Slime Boss), Bloodletting card, Battle Trance sequencing warning, Fairy in a Bottle elite consumption timing, Intimidate upgrade (2 Weak), Gremlin Leader turn economy + Rally scaling math, Brimstone relic, Sword Boomerang card, Snake Plant 9x3 damage correction, Brimstone + Demon Form combo (+4 Str/turn), Calipers relic, Impervious+ upgrade (40 block), Spheric Guardian second survival (Immolate+Impervious++Calipers+Spot Weakness).

## Unconfirmed

- Boss relic collection automation issue: In Run 71 and Run 77, a `proceed` command after Act 1 boss auto-collected the chest without showing boss relic selection options. Confirmed recurring (2 occurrences). CommunicationMod or automation bug. HIGH PRIORITY -- missing boss relic is a significant power loss each time.
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
- Gremlin Leader summoning pattern: Re-summoning trigger unconfirmed. Rally +3 Str to ALL confirmed across three runs. Third data point: at 56% HP entry, wasted turn 3 (Battle Trance sequencing error) allowed Rally to stack to +9 Str by turn 7-8, producing 44+ damage/turn.
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
- Spheric Guardian survivals (2 confirmed): (1) Corruption + FNP + burst damage won with 12 HP lost. (2) Immolate + Impervious+ + Calipers + Spot Weakness won with 20 HP lost. Common thread: front-loaded damage that breaks Barricade before it stacks past 60. Promoted to playbook.
- Feed+ Max HP gain from Slime Boss: +22 Max HP confirmed (80->98). How many individual kills produced this? Slime Boss split yields up to 7 kill-eligible enemies (boss pre-split doesn't count since it splits, so: 2 large slimes + 4 medium slimes = 6 kills max at +4 each = +24). The +22 suggests 5-6 kills with Feed+.
- Battle Trance + turn() sequencing: Batching draw effects with `end` wastes drawn cards. This is an automation/command issue, not a card evaluation issue. Applies to all draw effects (Pommel Strike draw, Shrug It Off draw) but most critical with Battle Trance (3-4 cards drawn = 3-4 cards wasted).
- Frail interaction with Rage block: Is Rage block reduced by Frail?
- Bronze Automaton Stasis targeting: Random or preferential?
- Bronze Automaton Hyper Beam exact damage: Very high single-hit. Need exact number.
- Kunai trigger counting: Does Whirlwind count as 1 or X attacks for Kunai?
- Snake Plant Malleable stacking behavior: Does Malleable block reset each turn or accumulate across turns? Observed increasing block per hit within a turn, but cross-turn behavior unconfirmed.
- Treasure chest display bug: Treasure chests gave no visible rewards in Run 77. Possible display/automation issue or chests may only contain gold (which is auto-collected without explicit display).
- Brimstone enemy Strength interaction with Weak: Does Weak reduce the effective damage of enemy attacks AFTER Brimstone Strength is applied? Assumed yes (standard Weak formula) but not directly measured.
- Book of Stabbing per-hit damage: Previously documented as ~6 per hit, Run 77 observed 7 per hit. Need more data points to confirm exact base damage.

## Prediction Errors (non-fatal, for monitoring)

- Weak multiplier applied incorrectly (Run 63): Player confused about when 0.75 multiplier applies.
- Spheric Guardian incoming damage miscalculation: Confused attack pattern timing.
- True Grit+ exhausting Spot Weakness: Strategic error -- exhaust low-value cards first.
- Demon Form too slow vs Spheric Guardian: Demon Form reached 13 Str by turn 9 but Barricade block was already 65+. Front-loaded Strength is required for this fight.
- Zero potion runs in Act 2: Run 75 had zero potions for entire Act 2. No drops, no purchases. Contributes directly to Spheric Guardian death -- a single Strength or Fire potion may have changed the outcome.
- Battle Trance + `end` batching error: Turn 3 of Gremlin Leader fight, Battle Trance + Bloodletting + `end` were batched together. Drew cards and generated energy, then immediately ended turn. The drawn cards and energy were completely wasted. This cost an entire turn against a Rally-scaling enemy, contributing directly to death. This is a command/automation sequencing issue.
- Snake Plant damage was documented as 7x3 but observed as 9x3 in Run 77. Playbook corrected. Previous HP drain estimates were understated.
- Brimstone + Book of Stabbing anti-synergy: Brimstone gave Book of Stabbing +2 Str/turn, amplifying every escalating hit. With Brimstone equipped, Book of Stabbing's per-hit damage grows by +2 each turn in addition to the +1 hit/turn escalation. Double-scaling makes the fight significantly more dangerous.
- Headbutt grid interaction: Headbutt's discard-pile selection UI caused misplays in Run 78. Unknown mechanism -- possibly related to grid/list index confusion similar to shop bug. Needs investigation if it recurs.
- Calipers + Impervious+ combo: Impervious+ (40 block) retains 25 block next turn with Calipers. Confirmed strong in Spheric Guardian fight (absorbed 10x2 attack turns with carried-over block). Single data point -- monitor for additional confirmation.
- 3 Cultists at 53% HP: Death despite Impervious+, Calipers, Immolate. Entry was 45 HP. Fourth data point for this fight (deaths at 30%, 37%, 39%, 53%). The 50% threshold may need revision upward -- even 53% was insufficient with strong tools but no kill speed. Kill speed (AOE burst to eliminate one Cultist fast) may matter more than defensive tools.

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
- Boss relic collection skipped (Run 71, Run 77): Confirmed recurring automation bug (2 occurrences). HIGH PRIORITY investigation needed.

## Open Questions

- Shop bug root cause: Recurring in ~40% of runs. CommunicationMod, state_formatter, or cmd.py issue? Latest instance: Run 75 accidental purchases of Sever Soul and Clash wasted gold and diluted deck quality. Previous: Run 74 bought 2 Havocs instead of intended Inflame due to shop index mismatch. This bug continues to produce tangible run damage -- wasted gold, dead cards, deck bloat.
- Face Trader event: What are the actual options and outcomes?
- Transmogrifier transform rules: Does it keep the same rarity?
- Ancient Writing second option (Insight): What does it offer?
- The Joust odds: 70% win chance for Murderer accurate?
- Confusion interaction with X-cost cards: Unconfirmed.
