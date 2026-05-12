# Observations

Items pending confirmation or further investigation. Promote to playbook when confident.

## Promoted (archived — already in playbook)

Preserved Insect, Upgrade death spiral (3x confirmed), Slime Boss split threshold, Disarm vs Slime Boss split, Corruption + Dead Branch synergy, Corruption setup cost trap, Mugger enemy, Looter + Mugger pairing, Dead Branch relic, Wing Boots relic, Pantograph 25 HP correction, The Champ boss + Execute mechanic, Dark Shackles card, Maw Bank relic, Spheric Guardian block growth rate, Spot Weakness+ upgrade, Rage+ per-turn expiration, Blood for Blood cost reduction, Barricade (player card), Fiend Fire in Cultist+Chosen multi-fights, Heavy Blade damage formula, Blessing of the Forge, Spheric Guardian Frail application, Eternal Feather relic, Oddly Smooth Stone relic, Masked Bandits event, Gremlin Leader Rally +3 Str ALL (3x confirmed), Uppercut+ upgrade (2 Weak + 2 Vuln confirmed), Spheric Guardian 4th death + Demon Form insufficient, Uppercut+ Artifact stripping vs SG confirmed, Spheric Guardian first survival (Corruption + FNP engine), Feed+ multi-kill Max HP gain (+22 from Slime Boss), Bloodletting card, Battle Trance sequencing warning, Fairy in a Bottle elite consumption timing, Intimidate upgrade (2 Weak), Gremlin Leader turn economy + Rally scaling math, Brimstone relic, Sword Boomerang card, Snake Plant 9x3 damage correction, Brimstone + Demon Form combo (+4 Str/turn), Calipers relic, Impervious+ upgrade (40 block), Spheric Guardian second survival (Immolate+Impervious++Calipers+Spot Weakness), Weak multiplier direction error (systematic, 3+ runs), Liquid Memories exhaust/discard confusion, Block-first at critical HP rule, Fire Breathing+ exhaust synergy blindness (Immolate Burns), Bronze Automaton Stasis targeting (Powers/Skills), Bronze Automaton Hyper Beam scaling (38-51), Brimstone + Book of Stabbing anti-synergy (2 deaths), 3 Cultists 60% threshold (6 deaths), Corruption vs Guardian trap (in corruption.md), Hexaghost Turn 2 blocking mandatory, SIO+ upgraded value (11 not 8), Strength/Rampage reset between combats, Confusion + X-cost cards interaction, Byrd fight 73 HP drain worst case (promoted to byrd.md), Evolve vs Slime Boss confirmed excellent (promoted to evolve.md and slime-boss.md), Spot Weakness +3/+4 value confusion (promoted to strategy.md arithmetic checklist), Act 2 first-floor safety valve routing (promoted to strategy.md and byrd.md), Mushrooms Eat Parasite curse correction (promoted to mushrooms.md), Fungi Beast +3 Str buff scaling (promoted to fungi-beast.md), Sentries 20-turn no-AOE benchmark (promoted to sentry.md), Neow's Lament elite readiness trap (promoted to neow-s-lament.md), Sentries elite readiness gate (promoted to strategy.md elite risk assessment).

## Unconfirmed

- Boss relic collection automation issue: In Run 71 and Run 77, a `proceed` command after Act 1 boss auto-collected the chest without showing boss relic selection options. Confirmed recurring (2 occurrences). CommunicationMod or automation bug. STILL UNRESOLVED. Needs infrastructure investigation.
- Fungi Beast HP range: Playbook had ~19 HP. Run 141 showed one at 24 HP, other possibly 22 HP. Need more data to confirm Act 1 paired Fungi Beast HP range (22-28 suspected). May vary by ascension or Act.
- Sentry Metallicize value: Confirmed 4 block/turn (from effective damage calculations in Run 141). Already in updated sentry.md, but only 1 observation. Monitor for consistency.
- Headbutt selection UI confusion: Player attempted to select 2 cards for Headbutt (which only selects 1). Not a bug -- player misunderstood the interface. The `choose 0` then `choose 1` on lines 124-125 suggests the first `choose` completed the Headbutt selection, and the second was interpreted as a different action. Monitor for recurrence.
- Ceramic Fish relic: Gives 9 gold per card added. Observed once. Need to confirm value.
- Healing card RNG denial streak: 8 of last 10 runs with no Reaper/Feed offered. Backup healing plan insufficient. Not addressable through playbook changes -- this is variance. Player should take Feed even in late Act 1 (floor 12+) and buy Blood/Regen Potions at every shop when no healing card exists.
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
- Byrd Flight regain timing: Player observed "Byrds regained Flight to 3" on buff turns. Byrd.md documents "Byrds regain Flight 3 on buff turns." But how does Flight interact with Vulnerable/Weak duration? Does Vulnerable applied by TC+ last the stated number of turns, or does Flight regain reset interaction? Need more observations to confirm Vuln wears off as documented.
- Byrd combined Str growth: All 3 Byrds gained +1 Str on buff turns. By Turn 4-5, individual Byrds had Str 1-2. Combined with Flight 3 regaining on buff turns, this means late-fight all-attack turns can deal 38+ damage. 5 rounds of buffs observed across 8-turn fight.
- Full heal between acts: Confirmed HP is restored to max between Act 1 and Act 2. Player went from 3 HP (post-Slime Boss + Burning Blood = 9) to 74/74 at Act 2 start.
- Shop buy confusion: Player intended to buy Evolve (73g) but translated command showed "Buy Bandage Up." The deck at boss fight included Evolve, so either the translation was wrong or the purchase worked despite display. Monitor for shop index misalignment.

## Prediction Errors (non-fatal, monitoring)

**Recurring arithmetic error patterns (ALL promoted to COMBAT ARITHMETIC CHECKLIST in strategy.md):**
- Weak direction confusion: applied 0.75 to own damage when enemies Weakened (Runs 63, 124)
- Upgraded value misuse: SIO+ as 8 instead of 11 (Run 125), Armaments+ block forgotten (Run 126)
- Flame Barrier+ block/counter confusion: used counter value (6) as block value (16) (Run 125)
- Strength carryover between combats: calculated damage with Str from previous fight (Run 127)
- Rampage counter carryover: self-corrected mid-reasoning (Run 125). Monitor.
- Hexaghost HP tracking drift: lost count of boss HP mid-fight (Run 129). Monitor.
- Spot Weakness upgraded value confusion: described SW as "+4 Str" during Byrd fight Turn 1 planning but card was unupgraded (+3 Str). Game state showed correct Str of 3. PROMOTED to strategy.md arithmetic checklist. Monitor for recurrence.

**Strategic errors (promoted to relevant playbook files):**
- Fire Breathing+ exhaust synergy blindness: PROMOTED to fire-breathing.md
- Block-first at critical HP: PROMOTED to strategy.md, slavers.md
- Demon Form + Stasis vulnerability: Demon Form stolen by Stasis in Run 125, never replayed. Inflame (1E, immediate, cannot be stolen after play) is better against Bronze Automaton. Documented in bronze-automaton.md.
- Red Mask strips 1 Artifact at combat start. Documented in bronze-automaton.md and red-mask.md.
- Headbutt grid interaction: UI misplay in Run 78. Not recurred. Low priority.

## Recurring Patterns

Hard Rules retired (Session 2026-05-12). Guidance distributed to individual card/relic playbook entries where it's contextually relevant. Remaining recurring patterns:
- **Arithmetic errors in combat** — Six different errors in runs 124-129. Now addressed by COMBAT ARITHMETIC CHECKLIST in strategy.md. Runs 140-141 showed significant improvement. Full Block Algorithm is enforcing explicit math.
- **Boss relic collection skipped** (Run 71, Run 77): Automation bug. STILL UNRESOLVED. Needs infrastructure investigation.
- **Act 2 first-fight death spiral** — Byrd/SG fights as first Act 2 room drain 30-73 HP. If map forces consecutive Monster rooms with no recovery, the run dies regardless of skill. Route planning must prioritize early non-combat rooms.
- **Elite readiness = deck quality, not just HP** — Run 141 entered Sentries at 95% HP but with a starter-quality deck (Strikes/Defends/Bash/Headbutt/SIO). The fight took 20 turns and drained 56 HP. Elite decision should evaluate DECK vs MATCHUP, not just HP. Neow's Lament exacerbates this by creating full HP with an undeveloped deck. Documented in sentry.md, neow-s-lament.md, strategy.md.
- **Playbook accuracy gaps** — Mushrooms Eat option was documented as "Heal 22 HP" but actually heals 21 HP + Parasite curse. Fungi Beast buff turns were documented as "free damage windows" but are actually +3 Str per buff (scaling to 12-15 damage by Turn 5-6). These errors directly contributed to a death. Other playbook entries may have similar omissions from early runs when observation was less rigorous.

## Open Questions

- Face Trader event options and outcomes
- Transmogrifier: does it keep the same rarity?
- Ancient Writing: what does the Insight option offer?
- The Joust: 70% win chance for Murderer accurate?
- Offering self-damage at sub-30% HP: 6 HP cost was exactly lethal margin in Run 128. Monitor whether Offering at critical HP causes deaths.
- Dual RNG denial: Run 128 had both healing AND Strength scaling denied across 24 floors despite Prayer Wheel. Two criteria denied simultaneously makes runs near-unwinnable. No fix possible -- pure variance.
