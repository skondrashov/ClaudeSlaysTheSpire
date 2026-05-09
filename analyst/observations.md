# Observations

Items pending confirmation or further investigation. Promote to playbook when confident.

## Promoted (archived — already in playbook)

Preserved Insect, Upgrade death spiral (3x confirmed), Slime Boss split threshold, Disarm vs Slime Boss split, Corruption + Dead Branch synergy, Corruption setup cost trap, Mugger enemy, Looter + Mugger pairing, Dead Branch relic, Wing Boots relic, Pantograph 25 HP correction, The Champ boss + Execute mechanic, Dark Shackles card, Maw Bank relic, Spheric Guardian block growth rate, Spot Weakness+ upgrade, Rage+ per-turn expiration, Blood for Blood cost reduction, Barricade (player card), Fiend Fire in Cultist+Chosen multi-fights, Heavy Blade damage formula, Blessing of the Forge, Spheric Guardian Frail application, Eternal Feather relic, Oddly Smooth Stone relic, Masked Bandits event, Gremlin Leader Rally +3 Str ALL (3x confirmed), Uppercut+ upgrade (2 Weak + 2 Vuln confirmed), Spheric Guardian 4th death + Demon Form insufficient, Uppercut+ Artifact stripping vs SG confirmed, Spheric Guardian first survival (Corruption + FNP engine), Feed+ multi-kill Max HP gain (+22 from Slime Boss), Bloodletting card, Battle Trance sequencing warning, Fairy in a Bottle elite consumption timing, Intimidate upgrade (2 Weak), Gremlin Leader turn economy + Rally scaling math, Brimstone relic, Sword Boomerang card, Snake Plant 9x3 damage correction, Brimstone + Demon Form combo (+4 Str/turn), Calipers relic, Impervious+ upgrade (40 block), Spheric Guardian second survival (Immolate+Impervious++Calipers+Spot Weakness).

## Unconfirmed

- Boss relic collection automation issue: In Run 71 and Run 77, a `proceed` command after Act 1 boss auto-collected the chest without showing boss relic selection options. Confirmed recurring (2 occurrences). CommunicationMod or automation bug. HIGH PRIORITY -- missing boss relic is a significant power loss each time. STILL UNRESOLVED AS OF RUN 100. Needs infrastructure investigation.
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
- Gremlin Leader summoning pattern: Re-summoning trigger unconfirmed. Rally +3 Str to ALL confirmed across four runs. Fourth data point: at 52% HP entry with Inflame+ and 3 potions, Impervious+Inflame on Turn 1 (zero damage) allowed 4 Rallies (+12 Str total) by turn 5. Leader attack became 18x3=54, gremlins added 14 = 68 total incoming by turn 9. Turn economy confirmed as the decisive factor -- setup turns that deal zero damage extend the fight into unwinnable Rally territory.
- Healing card RNG denial streak: Now 7 of last 9 runs (Runs 121-124, 127, 128, 129) with no Reaper or Feed offered. Run 125 acquired Reaper (breaking the streak temporarily), Run 126 had Reaper, but Run 127 and 128 had no healing card offered across 23 and 24 floors respectively. Run 128 had Prayer Wheel (double card rewards from combat) and STILL no healing card appeared -- even doubling the card reward rate did not break the denial streak. The backup healing plan (potions, events, conservative pathing) continues to produce insufficient healing to offset 30+ HP drain fights. Potion-based healing (Regen Potion, Blood Potion) remains the most reliable backup but is consumed mid-Act 2 leaving nothing for elites. This is now the single most persistent RNG-driven failure pattern. Consider: should the player take Feed even in late Act 1 (floor 12+) when it was previously considered less urgent? Should shop healing purchases (Blood Potion, Regen Potion) be mandatory at EVERY shop when no healing card exists?
- Hexaghost Turn 2 multi-hit damage: Observed ~30 damage (player calculated "30 incoming" and lost 20 HP after 10 block). The playbook documents Inferno as 7x6=42, but Turn 2 appears to be a separate multi-hit attack at 5x6=30. Later in the same fight (Turn 10), player observed "4x6=24" as a different multi-hit. Are there multiple distinct multi-hit attacks, or does Inferno vary in hit count? Need additional data points with exact hit counts to clarify.
- Burns+ (upgraded Burns) damage: Run 129 player's Turn 12 reasoning mentions Burns dealing more than 2 damage each ("Praying Burns only deal 2-4 total, not 8"). Later Burns in the Hexaghost fight appear to be Burns+ dealing 4 damage each instead of 2. This is consistent with Hexaghost's later ATTACK_DEBUFF turns adding Burns+ instead of regular Burns. Already promoted to hexaghost.md as a note, but exact turn at which Burns+ start appearing needs verification.
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
- Bronze Automaton Stasis targeting: PROMOTED. Confirmed preferential -- targets Power and Skill cards. Observed stolen: Demon Form (Power), Flame Barrier+ (Skill), Metallicize (Power) across multiple runs. Documented in bronze-automaton.md.
- Bronze Automaton Hyper Beam exact damage: PROMOTED. Observed 38 (Run 105), 51 (Run 125 at turn 6 with accumulated Str). Base is 45, scales with Automaton's Strength gains (+3 per cycle). Updated in bronze-automaton.md and enemies/bronze-automaton.md.
- Kunai trigger counting: Does Whirlwind count as 1 or X attacks for Kunai?
- Snake Plant Malleable stacking behavior: Does Malleable block reset each turn or accumulate across turns? Observed increasing block per hit within a turn, but cross-turn behavior unconfirmed.
- Treasure chest display bug: Treasure chests gave no visible rewards in Run 77. Possible display/automation issue or chests may only contain gold (which is auto-collected without explicit display).
- Brimstone enemy Strength interaction with Weak: Does Weak reduce the effective damage of enemy attacks AFTER Brimstone Strength is applied? Assumed yes (standard Weak formula) but not directly measured.
- Book of Stabbing per-hit damage: Previously documented as ~6 per hit, Run 77 observed 7 per hit. Need more data points to confirm exact base damage.

## Prediction Errors (non-fatal, for monitoring)

- Weak multiplier direction error (SYSTEMATIC, PROMOTED): Player systematically applied 0.75 Weak multiplier to own attacks when ENEMIES were Weakened (from Shockwave/Intimidate). Observed in Gremlin Leader fight (4+ calculations affected): Rampage calculated as "(8+3)*0.75=8" instead of correct 11, Strike+ calculated as "(9+3)*0.75*1.5=13" instead of correct 16. Player underestimated own damage by 25-35% in critical turns. This caused the player to choose defensive plays when aggressive plays would have been sufficient. Correction added to mechanics.md Weak section with explicit warning. DIFFERENT from Run 63 error below -- Run 63 was about timing, this is about direction (who is Weakened).
- Weak multiplier applied incorrectly (Run 63): Player confused about when 0.75 multiplier applies.
- Spheric Guardian incoming damage miscalculation: Confused attack pattern timing.
- True Grit+ exhausting Spot Weakness: Strategic error -- exhaust low-value cards first.
- Demon Form too slow vs Spheric Guardian: Demon Form reached 13 Str by turn 9 but Barricade block was already 65+. Front-loaded Strength is required for this fight.
- Zero potion runs in Act 2: Run 75 had zero potions for entire Act 2. No drops, no purchases. Contributes directly to Spheric Guardian death -- a single Strength or Fire potion may have changed the outcome.
- Battle Trance + `end` batching error: Turn 3 of Gremlin Leader fight, Battle Trance + Bloodletting + `end` were batched together. Drew cards and generated energy, then immediately ended turn. The drawn cards and energy were completely wasted. This cost an entire turn against a Rally-scaling enemy, contributing directly to death. This is a command/automation sequencing issue.
- Snake Plant damage was documented as 7x3 but observed as 9x3 in Run 77. Playbook corrected. Previous HP drain estimates were understated.
- Brimstone + Book of Stabbing anti-synergy: PROMOTED. Confirmed across 2 deaths (Runs 091, 100). 
- 3 Cultists threshold revision: PROMOTED. Five deaths confirmed. Threshold revised to 60%.
- Calipers + Impervious+ combo: PROMOTED. Confirmed strong in Spheric Guardian fight. Documented in impervious.md.
- Corruption vs Guardian trap: PROMOTED. Run 107 death confirmed. Now Hard Rule #9.
- Impervious timing discipline (Guardian): PROMOTED. Run 107 wasted Impervious on 16-damage turn. Documented in impervious.md and guardian.md.
- Headbutt grid interaction: Headbutt's discard-pile selection UI caused misplays in Run 78. Unknown mechanism -- possibly related to grid/list index confusion similar to shop bug. Needs investigation if it recurs.
- Liquid Memories exhaust/discard confusion (PROMOTED): Run 125 player attempted to recover Intimidate from exhaust pile using Liquid Memories, which only retrieves from the discard pile. Retrieved Shrug It Off+ from discard instead. Correction added to liquid-memories.md. This is a mechanics misunderstanding, not a strategic error.
- Hexaghost HP tracking drift: Run 129 Turn 4, player says "Strike (18 w/ Vuln+Str)" and "Hexaghost 218->200" -- but 218-18=200, which is correct. However, earlier on Turn 3: player says "Headbutt (22 w/ Vuln+Str) + Strike (18) = 40 dmg. Hexaghost 240->200." 240-40=200, correct. But Turn 4 starts with "Hexaghost 218" -- somewhere between Turn 3 and Turn 4, Hexaghost went from 200 to 218, which makes no sense unless the Hexaghost healed or the player's tracking was wrong. More likely the player simply lost track. On Turn 5 the player says "Hexaghost 200->184" -- reverting to the Turn 3 end value. This HP drift may indicate the player was confused about Hexaghost's HP in the middle of the fight. Non-fatal but worth monitoring.
- Flame Barrier+ block miscalculation under Frail: Run 125 vs Spheric Guardian, player calculated Flame Barrier+ as "4 block (6 reduced by Frail 25%)". Flame Barrier+ provides 16 block base, not 6. With Frail: floor(16*0.75) = 12 block, not 4. The player appears to have confused the counter damage value (6) with the block value (16). Non-fatal error (survived the fight) but indicates confusion between Flame Barrier+'s two separate effects (block and counter). Monitor for recurrence.
- SIO+ upgraded value miscalculation: Run 125 player calculated SIO+ block as 8 (base) instead of 11 (upgraded) on the Hyper Beam turn. This 3-block error was exactly the survival margin. Correction note added to shrug-it-off.md. This is a recurring pattern: the player sometimes uses unupgraded values in calculations after upgrading a card. Monitor for recurrence.
- Red Mask + Artifact interaction: Red Mask applies 1 Weak at combat start, which strips 1 Artifact charge from enemies with Artifact (Bronze Automaton 3->2, Spheric Guardian 3->2). This reduces the number of debuff applications needed for Artifact stripping. Confirmed in Run 125 vs Bronze Automaton. Already implicit in game mechanics (Artifact negates any debuff application) but worth noting as a tactical interaction for Artifact-heavy enemies.
- Block-first at critical HP (PROMOTED): Run 127 Slavers elite at 19 HP. Player played Shockwave (2E) + Pommel Strike (1E) for 13 damage with zero block. Died Turn 1 to combined Weakened damage from 3 enemies. Playing Shockwave + Defend (5 block) would have reduced incoming by 5, potentially surviving at 2-4 HP. At sub-30% HP against multi-enemy attacks, block MUST take priority over damage. Promoted to strategy.md, slavers.md, and shockwave.md.
- Rampage resets between combats: Run 125 player noted "4th play, resets between combats - actually 1st this combat = 8 base" when playing Rampage in a new fight. Rampage's scaling counter resets to 0 at the start of each new combat. The player corrected themselves mid-reasoning. Monitor whether this causes errors.
- Strength carryover miscalculation (cross-combat): Run 127 Centurion+Mystic fight: player calculated Bash+ as 13 damage (implying +3 Str from Inflame+) on Turn 1, but Inflame+ had not been played in that combat -- it was played in a PREVIOUS combat. Correct damage was 10 (Bash+ base with 0 Str). 3-damage miscalculation, non-fatal but part of a pattern: the player sometimes carries Strength values from one combat into the next, forgetting that Inflame+ is a per-combat Power. Related to Rampage reset issue above -- both are "combat state resets between fights" errors. Monitor for recurrence.
- Fire Breathing+ exhaust synergy blindness (PROMOTED): Run 128 Shelled Parasite + Fungi Beast fight: player exhausted Fire Breathing+ via True Grit+, reasoning "no major status generation in this fight." But Immolate was in the deck and would be played multiple times -- each Immolate adds a Burn to discard, and each Burn drawn triggers Fire Breathing+ for 10 free damage bypassing Plated Armor. With Evolve also active, Burns draw replacement cards AND deal damage. Over the remaining 5+ turns, this would have been 30-50+ free damage, potentially shortening the fight by 2-3 turns and avoiding the lethal final turn with no block cards. The player correctly identified Evolve+Fire Breathing+ as an engine for Hexaghost but failed to recognize the same engine applies to ANY fight where Immolate is played. Correction added to fire-breathing.md and strategy.md Never Exhaust list.
- Demon Form + Stasis vulnerability: Demon Form is a 3E Power that needs to be played early for maximum value. Stasis preferentially steals Powers. If Demon Form is stolen by Stasis Turn 1-2, the player loses their primary scaling card for several turns while killing the Orb. In Run 125, Demon Form was stolen by Stasis and was NEVER PLAYED the entire fight despite being recovered by killing the Orb. The card ended up in the discard pile and was never drawn again before death on Turn 6. Consider: is Demon Form too slow AND too vulnerable to Stasis for the Bronze Automaton fight? Inflame (1E, immediate, cannot be stolen after play) may be strictly better here.

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
- Corruption vs Guardian: ADDRESSED (Hard Rule #9). One death (Run 107). Monitor.
- Boss relic collection skipped (Run 71, Run 77): Confirmed recurring automation bug (2 occurrences). STILL UNRESOLVED as of Run 100. HIGH PRIORITY infrastructure investigation needed.

## Open Questions

- Shop bug root cause: RESOLVED. CommunicationMod purge offset was identified and fixed. No longer affecting runs 99+. Monitor for recurrence.
- Face Trader event: What are the actual options and outcomes?
- Transmogrifier transform rules: Does it keep the same rarity?
- Ancient Writing second option (Insight): What does it offer?
- The Joust odds: 70% win chance for Murderer accurate?
- Confusion interaction with X-cost cards: CONFIRMED in Run 127. Whirlwind+ under Confusion used all remaining energy (2E = 2 hits). X-cost cards are reliable under Confusion because they bypass the randomized cost mechanic and consume whatever energy remains. Duplication Potion + 0-cost card under Confusion also confirmed as strong synergy. Consider promoting to snecko.md (already added).
- Louse Curl Up block residual calculation: Player computed "Strike 2 deals 4" against remaining Curl Up block, suggesting 6-7+6=4 through. Actual math with Curl Up 7: first Strike 6 vs 7 block = 0 through (1 block remaining), second Strike 6 vs 1 block = 5 through. The 4 vs 5 discrepancy is 1 HP -- needs verification of whether Curl Up block values vary (3-7 range observed).
- HP tracking drift across multi-turn fights: In Run 126 Shelled Parasite + Fungi Beast fight, HP values drifted by 2-3 HP from expected calculations. Pain curse (1 HP per draw when drawn) may account for this. Needs explicit tracking.
- Was AOE offered in Run 126 or RNG-denied the entire run? If AOE was offered and skipped, that is a decision error. If never offered across 21 floors, that is RNG denial.
- Strength scaling RNG denial in Run 128: No Inflame, Spot Weakness, Demon Form, or any Strength source was offered across 24 floors despite Prayer Wheel doubling card rewards. The deck's damage against Plated Armor enemies was critically low (Strikes dealing 0 through 14 armor, Immolate dealing only 7 actual). Combined with healing RNG denial (6 of last 8 runs), two separate criteria can be RNG-denied simultaneously, making runs nearly unwinnable regardless of decision quality. Consider: should the Strength scaling criterion be elevated to #1 priority when Shelled Parasite is a known Act 2 encounter?
- Offering self-damage at low HP: Run 128 F24 Shelled Parasite fight -- player used Offering at 26 HP, losing 6 HP to 20 HP. This was followed by taking more damage and eventually dying at 14 HP. The 6 HP from Offering was exactly the margin that could have kept the player alive one more turn. At sub-30% HP, Offering's 6 HP cost should be weighed against the risk of dropping into lethal range. Not clearly wrong in this case (the +2E and draw 5 generated significant value) but worth monitoring.
