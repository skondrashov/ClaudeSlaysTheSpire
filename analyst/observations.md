# Observations

Items pending confirmation or further investigation. Promote to playbook when confident.

## Promoted (archived — already in playbook)

Preserved Insect, Upgrade death spiral (3x confirmed), Slime Boss split threshold, Disarm vs Slime Boss split, Corruption + Dead Branch synergy, Corruption setup cost trap, Mugger enemy, Looter + Mugger pairing, Dead Branch relic, Wing Boots relic, Pantograph 25 HP correction, The Champ boss + Execute mechanic, Dark Shackles card, Maw Bank relic, Spheric Guardian block growth rate, Spot Weakness+ upgrade, Rage+ per-turn expiration, Blood for Blood cost reduction, Barricade (player card), Fiend Fire in Cultist+Chosen multi-fights, Heavy Blade damage formula, Blessing of the Forge, Spheric Guardian Frail application, Eternal Feather relic, Oddly Smooth Stone relic, Masked Bandits event, Gremlin Leader Rally +3 Str ALL (3x confirmed), Uppercut+ upgrade (2 Weak + 2 Vuln confirmed), Spheric Guardian 4th death + Demon Form insufficient, Uppercut+ Artifact stripping vs SG confirmed, Spheric Guardian first survival (Corruption + FNP engine), Feed+ multi-kill Max HP gain (+22 from Slime Boss), Bloodletting card, Battle Trance sequencing warning, Fairy in a Bottle elite consumption timing, Intimidate upgrade (2 Weak), Gremlin Leader turn economy + Rally scaling math, Brimstone relic, Sword Boomerang card, Snake Plant 9x3 damage correction, Brimstone + Demon Form combo (+4 Str/turn), Calipers relic, Impervious+ upgrade (40 block), Spheric Guardian second survival (Immolate+Impervious++Calipers+Spot Weakness), Weak multiplier direction error (systematic, 3+ runs), Liquid Memories exhaust/discard confusion, Block-first at critical HP rule, Fire Breathing+ exhaust synergy blindness (Immolate Burns), Bronze Automaton Stasis targeting (Powers/Skills), Bronze Automaton Hyper Beam scaling (38-51), Brimstone + Book of Stabbing anti-synergy (2 deaths), 3 Cultists 60% threshold (6 deaths), Corruption vs Guardian trap (in corruption.md), Hexaghost Turn 2 blocking mandatory, SIO+ upgraded value (11 not 8), Strength/Rampage reset between combats, Confusion + X-cost cards interaction, Byrd fight 73 HP drain worst case (promoted to byrd.md), Evolve vs Slime Boss confirmed excellent (promoted to evolve.md and slime-boss.md), Spot Weakness +3/+4 value confusion (promoted to strategy.md arithmetic checklist), Act 2 first-floor safety valve routing (promoted to strategy.md and byrd.md), Mushrooms Eat Parasite curse correction (promoted to mushrooms.md), Fungi Beast +3 Str buff scaling (promoted to fungi-beast.md), Sentries 20-turn no-AOE benchmark (promoted to sentry.md), Neow's Lament elite readiness trap (promoted to neow-s-lament.md), Sentries elite readiness gate (promoted to strategy.md elite risk assessment), Hyper Beam #2 at 57 damage (promoted to bronze-automaton.md), Hyper Beam fires twice in long fights (promoted to bronze-automaton.md and enemies/bronze-automaton.md), Clothesline non-exhausting Weak for Automaton (promoted to clothesline.md), Mark of Pain + Evolve+ synergy (promoted to evolve.md and mark-of-pain.md), Mark of Pain relic (new entry created), Self-Forming Clay relic (new entry created), Bronze Automaton Impervious+ draw RNG (promoted to impervious.md and bronze-automaton.md).

## Unconfirmed

- **Boss relic collection SKIPPED (3 occurrences: Run 71, Run 77, Run 142) -- but NOT in Runs 143-148.** Six consecutive clean runs including both VICTORIES. Bug resolved. Removing from active monitoring.
- **Treasure chest relic SKIPPED (1 occurrence: Run 142 Floor 9) -- but NOT in Runs 143-148.** Six consecutive clean runs. Bug resolved.
- Fungi Beast HP range: Playbook had ~19 HP. Run 141 showed one at 24 HP, other possibly 22 HP. Need more data to confirm Act 1 paired Fungi Beast HP range (22-28 suspected). May vary by ascension or Act.
- Sentry Metallicize value: Confirmed 4 block/turn (from effective damage calculations in Run 141). Already in updated sentry.md, but only 1 observation. Monitor for consistency.
- Headbutt selection UI confusion: Player attempted to select 2 cards for Headbutt (which only selects 1). Not a bug -- player misunderstood the interface. The `choose 0` then `choose 1` on lines 124-125 suggests the first `choose` completed the Headbutt selection, and the second was interpreted as a different action. Monitor for recurrence.
- Ceramic Fish relic: Gives 9 gold per card added. Observed twice. Need to confirm value.
- Centurion 10x3 multi-hit attack: Run 142 death caused by 30 damage from 10x3 attack. Previously documented only as 12-18 single hits. Playbook updated. Need more data on attack pattern rotation (when does 10x3 appear vs 12 single hit?).
- Sundial relic: Every 3 shuffles, gain 2 energy. Confirmed from Run 142: 5E on Turn 4 of 3 Cultists fight (3 base + 2 bonus). Playbook entry created. Monitor for consistency.
- Healing card RNG denial streak BROKEN: Feed obtained from Guardian boss card reward in Run 145. Streak was 10 of 12 runs with no healing card. Feed+ gave +3 max HP on Orb Walker kill (77 max HP total). Promoted note: Feed from boss card rewards is a reliable source since boss rewards always include a rare card option.
- Mark of Pain + Evolve+ synergy confirmed: Promoted to evolve.md and mark-of-pain.md. Strong engine (4E + 2 draws per Wound = 5-7 cards/turn). One observation. Monitor for consistency across multiple runs.
- Mark of Pain Wound dilution: Wounds added to draw pile by attacks reduce probability of drawing specific cards on critical turns. In Run 143, 2x Impervious+ in a 15-card deck (plus accumulating Wounds) meant neither was drawn on either Hyper Beam turn. The card advantage from Evolve+ may not compensate for the draw dilution when specific cards are needed. Need more data.
- Bronze Automaton Strength can reach +12 by turn 12. Hyper Beam #2 at 57 damage (45 base + 12 Str). Previous maximum was 51 (turn 6). Promoted to bronze-automaton.md.
- Bronze Automaton fires TWO Hyper Beams in long fights (turn ~6 and ~12). Confirmed. Must plan block for both. Promoted to bronze-automaton.md and enemies/bronze-automaton.md.
- Clothesline as non-exhausting Weak source for Automaton: confirmed useful on both Hyper Beam turns. Promoted to clothesline.md.
- Hexaghost multi-hit attack variants: Conflicting Turn 2 data. Previous observation: 5x6=30. Run 144 observed 4x6=24 on Turn 2. The difference (24 vs 30) is significant for block planning. Playbook currently says "~5x6=30." Need more data to determine if Turn 2 is always 4x6 or variable.
- Burns+ timing: Burns+ (4 damage each) appear from later ATTACK_DEBUFF turns. Exact transition turn unknown.
- Horn Cleat: Observed 14 block on turn 2. Fixed or scaling?
- Gremlin Horn: Works on ALL enemy deaths including minions?
- Whetstone: Can upgrade already-upgraded cards?
- Collector total HP: CONFIRMED 282 (from Run 145 Rampage+ opening hit at 282 HP). Updated the-collector.md.
- Knowing Skull HP cost: Flat or increasing per interaction?
- Corruption + Second Wind: Does Second Wind exhaust itself under Corruption?
- Feel No Pain + Frail: Is FNP block reduced by Frail?
- Frail + Rage block: Is Rage block reduced by Frail?
- Kunai + Whirlwind: Does each hit count as a separate attack for Kunai?
- Book of Stabbing per-hit damage: 6 or 7 per hit? Need confirmation.
- Donu and Deca: PROMOTED. Defeated in both Run 147 and Run 148 (back-to-back victories). Full boss entry in donu-and-deca.md. 250 HP each, Artifact 1 each. Kill Donu first. Snecko Eye + Immolate+ + Limit Break confirmed across both wins.
- Mummified Hand + Power-heavy decks: Observed generating 2-4 free plays per turn in a 5-Power deck (Barricade+, 2x Metallicize, Inflame+, Evolve+). The relic's value scales multiplicatively with Power count. One observation -- monitor for consistency.
- Bird-Faced Urn relic: Heals 2 HP per Power played. Obtained from Sentries elite. Playbook entry created. Only 1 observation -- monitor for exact trigger conditions (does it work with Powers played from potions? from Distilled Chaos?).
- Sentries Plated Armor interaction: Essence of Steel (4 Plated Armor) reduced damage per Sentry attack turn by 4. Over 14 turns, this is ~28-56 block total. But Plated Armor decays by 1 when hit (confirmed -- player's notes show Plated dropping from 4 to 3 to 2 across hits). Need more data on exact decay mechanic.
- Gremlin Nob displayed intent includes player Vulnerable: Player noted T4 "9 base * 1.5 Vuln on me = 13" but displayed intent already showed 13 (or higher). The run summary confirms "displayed enemy intent already includes player Vulnerable in the damage number." If true, the player should use the displayed number directly, not recalculate Vulnerable on top. Need more observations to confirm consistently.
- The Maw HP: Observed at approximately 300 HP (player noted 272 after 28 damage Turn 1, starting at ~300). Need exact confirmation.
- The Maw pattern: STRONG_DEBUFF Turn 1, then alternating BUFF/ATTACK with escalating damage (5/16/33/56). Only 1 observation. Monitor for consistency.
- Orb Walker HP: Observed at 93. Only 1 observation.
- Orb Walker Str scaling: +3 Str per turn observed. Only 1 observation.
- Exploder + Spiker fight composition: Exploders (~30 HP each) deal AoE on death, Spiker has Thorns 3. Only 1 observation.
- Ectoplasm + Maw Bank anti-synergy: Maw Bank gives 12g/floor but Ectoplasm blocks all gold gain. Maw Bank became completely useless. Both are relics that cannot be discarded.
- Card index shifting bug (Maw fight): Impervious was played instead of Headbutt due to card index shifting after Bash was played. Player noted "Impervious was accidentally played due to card index shift." This is the 5th+ documented index shifting incident. Infrastructure issue, not strategy.
- Barricade+ (2E) from Frozen Egg auto-upgrade: Barricade was obtained as a boss card reward and auto-upgraded to Barricade+ (2E instead of 3E) by Frozen Egg. This 1E saving is critical -- at 5E base, Barricade+ costs 2E leaving 3E for block, vs Barricade at 3E leaving only 2E.
- Ancient Writing event (Simplicity option): Upgrades ALL Strikes and Defends in the deck. Massive value (9 free upgrades in Run 145). Previously an open question about what options it offers. The "Simplicity" option is confirmed to mass-upgrade Strikes and Defends.
- Byrd Flight regain timing: Player observed "Byrds regained Flight to 3" on buff turns. Byrd.md documents "Byrds regain Flight 3 on buff turns." But how does Flight interact with Vulnerable/Weak duration? Does Vulnerable applied by TC+ last the stated number of turns, or does Flight regain reset interaction? Need more observations to confirm Vuln wears off as documented.
- Byrd combined Str growth: All 3 Byrds gained +1 Str on buff turns. By Turn 4-5, individual Byrds had Str 1-2. Combined with Flight 3 regaining on buff turns, this means late-fight all-attack turns can deal 38+ damage. 5 rounds of buffs observed across 8-turn fight.
- Incense Burner counter persistence: Counter increments across combats. Promoted to incense-burner.md. Need to confirm: does the counter increment on turns where you have Intangible, or does it reset? Monitor.
- Cultist Potion Ritual value: Confirmed +1 Str/turn. Promoted to cultist-potion.md. Need more data: is the Ritual value always 1, or can it be higher?
- Full heal between acts: DOUBLE CONFIRMED. HP restored to max between Act 1 and Act 2 (Run 140: 3->74, Run 145: ~15->74/74 after Guardian). Also confirmed between Act 2 and Act 3 (Run 145: 5->77/77 after Collector + Burning Blood). This means entering the boss at low HP is acceptable if you can survive the fight -- the next act starts at full HP regardless.
- Shop buy confusion: Recurring shop translation mismatches. Run 142: intended Evolve, translated "Buy Bandage Up." Run 143: intended Evolve (76g), translated "Buy Finesse" (line 37); intended card removal (100g), translated "Buy Cleave" (line 342). In all cases the correct card/action was obtained (deck contained Evolve, card was removed). The `translated` field appears to display incorrect card names but the actual purchase executes correctly. This is a display/logging issue, not a gameplay bug. Low priority.

## Prediction Errors (non-fatal, monitoring)

**Recurring arithmetic error patterns (ALL promoted to COMBAT ARITHMETIC CHECKLIST in strategy.md):**
- Weak direction confusion: applied 0.75 to own damage when enemies Weakened (Runs 63, 124)
- Upgraded value misuse: SIO+ as 8 instead of 11 (Run 125), Armaments+ block forgotten (Run 126)
- Flame Barrier+ block/counter confusion: used counter value (6) as block value (16) (Run 125)
- Strength carryover between combats: calculated damage with Str from previous fight (Run 127)
- Rampage counter carryover: self-corrected mid-reasoning (Run 125). Monitor.
- Hexaghost HP tracking drift: lost count of boss HP mid-fight (Run 129). Monitor.
- Spot Weakness upgraded value confusion: described SW as "+4 Str" during Byrd fight Turn 1 planning but card was unupgraded (+3 Str). Game state showed correct Str of 3. PROMOTED to strategy.md arithmetic checklist. Monitor for recurrence.
- **FATAL: Basic comparison error "13 > 20" (Run 144).** PROMOTED to strategy.md checklist item #4. Player wrote "Iron Wave deals 5+8=13 damage > 20 HP" -- basic numeric comparison failure. The command was already submitted with `end` chained on the same line, so the error could not be corrected. New rule: never chain `end` with attacks on kill turns.

**Strategic errors (promoted to relevant playbook files):**
- Fire Breathing+ exhaust synergy blindness: PROMOTED to fire-breathing.md
- Block-first at critical HP: PROMOTED to strategy.md, slavers.md
- Demon Form + Stasis vulnerability: Demon Form stolen by Stasis in Run 125, never replayed. Inflame (1E, immediate, cannot be stolen after play) is better against Bronze Automaton. Documented in bronze-automaton.md.
- Red Mask strips 1 Artifact at combat start. Documented in bronze-automaton.md and red-mask.md.
- Headbutt grid interaction: UI misplay in Run 78. Not recurred. Low priority.

## Recurring Patterns

Hard Rules retired (Session 2026-05-12). Guidance distributed to individual card/relic playbook entries where it's contextually relevant. Remaining recurring patterns:
- **Arithmetic errors in combat** — Seven different errors in runs 124-144. Runs 140-143 showed significant improvement with Full Block Algorithm enforcing explicit math. But Run 144 introduced a new fatal error type: basic comparison failure ("13 > 20") on a kill turn with `end` chained in the same command. Checklist item #4 added to address this.
- **Boss relic collection skipped** (Run 71, Run 77, Run 142): Automation bug. 3 confirmed occurrences. Did NOT occur in Runs 143-148 (six consecutive clean runs including both VICTORIES). Bug resolved. Removing from active monitoring.
- **Act 2 first-fight death spiral** — Byrd/SG fights as first Act 2 room drain 30-73 HP. If map forces consecutive Monster rooms with no recovery, the run dies regardless of skill. Route planning must prioritize early non-combat rooms.
- **Elite readiness = deck quality, not just HP** — Run 141 entered Sentries at 95% HP but with a starter-quality deck (Strikes/Defends/Bash/Headbutt/SIO). The fight took 20 turns and drained 56 HP. Elite decision should evaluate DECK vs MATCHUP, not just HP. Neow's Lament exacerbates this by creating full HP with an undeveloped deck. Documented in sentry.md, neow-s-lament.md, strategy.md.
- **Playbook accuracy gaps** — Mushrooms Eat option was documented as "Heal 22 HP" but actually heals 21 HP + Parasite curse. Fungi Beast buff turns were documented as "free damage windows" but are actually +3 Str per buff (scaling to 12-15 damage by Turn 5-6). These errors directly contributed to a death. Other playbook entries may have similar omissions from early runs when observation was less rigorous.

- Snecko Eye + high-cost deck: SECOND OBSERVATION (2 consecutive wins with Snecko Eye). Both victories used Snecko Eye as Act 2 boss relic. The consistency of 2 wins confirms Snecko Eye is the strongest Act 2 boss relic for high-cost Ironclad decks. Not just lucky RNG -- the relic fundamentally enables the winning formula. FULLY PROMOTED to snecko-eye.md. No longer needs monitoring.
- Dual Wield+ on Immolate+: FIRST OBSERVATION. Created 2 copies of Immolate+ in hand (3 total). Under Snecko Eye, each copy got a new cost roll. All three were playable in one turn for 102 AOE. Promoted to dual-wield.md. Only 1 observation -- monitor for consistency.
- Donu and Deca Artifact count: CONFIRMED Artifact 1 each across 2 victories. Consistent with both encounters. Promoting as confirmed -- each boss blocks exactly 1 debuff before becoming fully vulnerable.
- Donu and Deca block patterns: Both bosses had intermittent block (8-16 observed). The block pattern is not well understood. Donu had 16 block when killed by Heavy Blade. Deca had block on some turns. Need more observations.
- Donu Strength buff amount: Donu buffs Strength for both enemies. The exact amount per buff turn was not precisely tracked. Incoming damage grew from 20 Turn 1 to 32 Turn 5. Need more data on the exact Str gain per Donu buff.
- Blessing of the Forge + Snecko Eye: Upgraded all 7 drawn cards for one combat. Heavy Blade became Heavy Blade+ (5x Str multiplier instead of 3x). Critical for the Automaton kill. One observation -- need to confirm the interaction is consistent.
- Regal Pillow rest healing: Confirmed +15 HP per rest (24 base + 15 = 39 total). Enabled full HP recovery before Donu and Deca (53 + 39 = 92, capped at 80/80). Promoted to regal-pillow.md. One observation.
- Nunchaku counter persistence: Counter appears to persist across combats. In the victory run, Nunchaku triggered multiple times per boss fight. Need to confirm the counter does not reset between fights.
- Champion Belt Vulnerable -> Weak: Confirmed applying 1 Weak whenever Vulnerable is applied. Promoted to champion-belt.md. Only 1 observation.
- Bag of Marbles Turn 1 Vulnerable: Confirmed applying 1 Vulnerable to ALL enemies at combat start. With Paper Phrog = 1.75x damage on Turn 1 attacks for free. Promoted to bag-of-marbles.md. One observation.
- Sling of Courage +2 Str at boss/elite start: Confirmed. Promoted to sling-of-courage.md. One observation.
- Omamori curse negation: Used twice in the victory run. (1) Scrap Ooze event at F7 -- Omamori negated the curse from reaching inside, getting a free relic (Omamori itself). Wait -- Omamori was obtained FROM Scrap Ooze? Need to verify. (2) Coffin event at F31 -- Omamori negated Curse from opening coffin, getting Paper Phrog for free. (3) Big Fish Eat event at F14 -- Omamori negated Parasite curse, getting 20 HP heal for free. Omamori is S-tier when events with curse downsides are encountered.
- Maw Bank gold accumulation: 12g per floor. Accumulated substantial gold for Act 2 shop purchases (Toy Ornithopter 155g, Sling of Courage 153g, card removal 100g, Flame Barrier 69g, Blessing of the Forge 52g, Essence of Steel 74g). Already documented. Confirmed strong value in runs with shops.

- Flex+ into Limit Break+ combo: PROMOTED. Flex+ gives 4 temporary Str, Limit Break+ doubles total Str to make it effectively permanent. Net gain after end-of-turn Str loss is significant (e.g., 1 base + 4 Flex = 5, doubled to 10, lose 4 = 6 permanent). Key contributor to second victory. Promoted to flex.md and limit-break.md.
- Bronze Scales relic: 3 Thorns damage per Attack received. Delivered killing blow on Deca at 4 HP in the second victory. Promoted to bronze-scales.md (new entry).
- Gambling Chip + Snecko Eye synergy: PROMOTED. Mulligan at combat start lets you discard cards with bad Snecko cost rolls and draw replacements with new rolls. Dramatically improves Turn 1 consistency. Present in second victory. Promoted to gambling-chip.md and snecko-eye.md.
- Snecko Oil + Snecko Eye: PROMOTED. With Confusion already active, Snecko Oil's cost randomization is redundant but the draw 5 is pure upside. Expands hand to ~10 cards Turn 1 of boss fights. Used in second victory. Promoted to snecko-oil.md and snecko-eye.md.
- Duplication Potion on 0-cost Immolate+: PROMOTED. 60 AOE for 0E. Best observed Duplication Potion play. Promoted to duplication-potion.md.
- Darklings simultaneous AOE kill: CONFIRMED. All 3 Darklings killed in same turn bypasses Life Link. Promoted to darklings.md (new entry).
- Fairy in a Bottle saved the run vs Spikers/Guardians in Act 3. Confirms Fairy is critical safety net for Act 3 fights with Thorns mechanics. Promoted to fairy-in-a-bottle.md.
- **TWO winning formulas confirmed across 3 victories**: PROMOTED. (A) Snecko Eye + Immolate+ + Limit Break (Runs 147-148, vs Donu and Deca). (B) Barricade + Corruption + FNP + Entrench + Body Slam (Run 150, vs Time Eater). Both share Immolate+ as primary AOE. Both require zero UI misplays. Promoted to strategy.md as THE WINNING FORMULAS. New playbook entries created: body-slam.md, entrench.md, apotheosis.md, time-eater.md, cursed-key.md, ornamental-fan.md.
- **The Champ Act 2 boss**: Defeated in Run 148 at 11 HP. 9-turn fight, Duplication Potion on Immolate+ (0-cost from Snecko Eye) delivered the killing blow. Immolate+ was the MVP again. The Champ had no playbook entry update needed -- existing entry is sufficient.
- **Slaver's Collar relic**: +1 energy at elite/boss starts. Combined with Busted Crown (+1E), gave 5E in hallway fights and 6E in boss fights. The energy advantage from double boss-relic energy was significant. Two energy boss relics stacking is a powerful combination. Only 1 observation.

- **Barricade + Corruption + FNP + Entrench + Body Slam engine**: PROMOTED to strategy.md, barricade.md, corruption.md, feel-no-pain.md, second-wind.md. New entries: body-slam.md, entrench.md, apotheosis.md, time-eater.md. Fully confirmed victory engine.
- **Fusion Hammer as Neow swap**: Viable when Apotheosis or Blessing of the Forge compensate for lost upgrades. Promoted to fusion-hammer.md. Run 150 won all 3 bosses without a single rest-site upgrade.
- **Apotheosis + Fusion Hammer synergy**: PROMOTED to fusion-hammer.md and apotheosis.md (new entry). The sole upgrade path when Fusion Hammer prevents smithing. Under Corruption, costs 0E and exhausts (free mass upgrade + FNP trigger).
- **Second Wind+ exhaust of Normality curse**: PROMOTED to second-wind.md. Under Corruption, SW+ exhausts Normality permanently from the deck during combat. High-priority play.
- **Body Slam+ as primary damage source**: PROMOTED to body-slam.md (new entry). 0E, damage = current block. With 100-200 block from Barricade engine, deals 100-200 damage per play. The highest damage-per-energy card in the game when paired with Barricade.
- Time Eater 12-card mechanic: Confirmed every 12 cards played triggers Time Warp (heal 32, +2 Str, end turn). Promoted to time-eater.md (new entry). Need more observations on exact mechanics (does the counter persist across turns or reset?).
- Time Eater HP: Observed at 480. Only 1 observation. Monitor.
- Writhing Mass HP: Previously listed as ~160. Run 150 fight lasted long but HP not precisely tracked. Monitor.
- Writhing Mass Reactive mechanic: Confirmed changes intent based on card type played. Spot Weakness should be played BEFORE attacks to check intent while it's still Attack-type. Only 1 detailed observation.
- White Beast Statue potion guarantee: Confirmed 100% potion drop after every combat. Combined with no Burning Blood (Fusion Hammer swap), potions were the primary sustain source. Excellent relic when Burning Blood is unavailable.
- Blood Vial relic: Heals 2 HP at combat start. Minor passive healing. One observation. Confirmed value from Run 150.
- Empty Cage boss relic: Remove 2 cards. Excellent deck thinning. Used to remove 2 Strikes after Act 2 boss. One observation.
- Toxic Egg + Molten Egg + Frozen Egg: All three Eggs obtained in one run (Frozen from event, Molten from chest, Toxic from Giant Head elite). With all three, every new card auto-upgrades. Extremely powerful but rare to have all three.
- The Boot relic: Attacks deal minimum 5 damage. Good vs Intangible enemies (Nemesis). One observation.
- Ornamental Fan: +4 block per 3 attacks. PROMOTED to ornamental-fan.md (new entry). Minor value in Corruption engine decks. One observation.
- Normality curse from Cursed Key: The most dangerous curse in the game for Corruption engine decks. Limits plays to 3/turn, crippling skill exhaust chains. Prioritize removal at shop (100-125g). PROMOTED to cursed-key.md (new entry).
- Sensory Stone event "Recall" option: Grants 1 free Colorless card pick. Apotheosis was available as one of the options. Need more data on what Colorless cards can appear.

## Open Questions

- Face Trader event options and outcomes
- Transmogrifier: does it keep the same rarity?
- Ancient Writing: "Simplicity" option upgrades ALL Strikes and Defends (confirmed Run 145, 9 free upgrades). "Insight" option still unknown.
- The Joust: 70% win chance for Murderer accurate?
- Offering self-damage at sub-30% HP: 6 HP cost was exactly lethal margin in Run 128. Monitor whether Offering at critical HP causes deaths.
- Dual RNG denial: Run 128 had both healing AND Strength scaling denied across 24 floors despite Prayer Wheel. Two criteria denied simultaneously makes runs near-unwinnable. No fix possible -- pure variance.
