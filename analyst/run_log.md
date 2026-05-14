# Run Log

## Runs 0-45 Summary (archived)

37 runs total. 7 Act 1 boss victories (Guardian x4, Slime Boss x2, Hexaghost x3). Key lessons absorbed into playbook:
- True Grit unupgraded is run-ending (Runs 2, 32, 44)
- Index shifting kills (Runs 3, 21, 22, 57) — 4 confirmed deaths
- Low HP entry is the #1 cause of death (19 of 22 documented deaths)
- Hexaghost needs Weak + damage scaling (not just Weak)
- AOE mandatory for Slime Boss split; both large slimes split on death
- Exhaust-heavy decks collapse in long fights (Guardian)
- Act 2 HP drain from Byrds/Centurion+Mystic triggers death spirals
- 3 Cultists is the most lethal hallway fight (3 deaths at 30-39% HP entry)
- Random exhaust (Havoc, unupgraded True Grit) destroyed critical cards in 3 runs
- Demon Form + Limit Break scaling is too slow for emergency fights at low HP
- Fiend Fire + Unceasing Top is the strongest combo observed
- Unknown rooms are NOT safe at low HP (Snake Plant appearances)
- Burning Blood alone cannot sustain Act 2 (confirmed across 10+ runs)

## Runs 48-78 Summary (archived)

31 runs. Key lessons absorbed into playbook:
- Slavers elite: 3 enemies, 27+ combined damage/turn (Run 50, death F23)
- Vampires event -30% Max HP is crippling (Run 51, death F24)
- Bronze Automaton: Stasis steals cards, Runic Dome hides Hyper Beam (Run 52, death F33)
- First Collector encounter: STRONG_DEBUFF Turn 4 triple debuff (Run 48, death F33)
- Best floor 39 (Run 63) -- Transient death in Act 3 after beating Guardian + Collector via Pantograph
- Spheric Guardian 3 deaths (Runs 69, 72, 75) -- Barricade + Frail combo requires front-loaded Strength
- Two Spheric Guardian survivals confirmed: Corruption+FNP engine, Immolate+Impervious++Calipers
- Hard Rules introduced at Run 60, zero violations since
- Corruption setup trap (3E turn 1 = death, Run 73)
- Gremlin Leader Rally +3 Str ALL confirmed across 3 runs
- Brimstone anti-synergy with Book of Stabbing (2 deaths Runs 91, 100)
- 3 Cultists threshold revised from 50% to 60% (5 deaths confirmed)
- Shop indexing bug fixed (CommunicationMod purge offset)


## Runs 81-100 Summary (archived)

10 logged deaths. Average death floor: 26.2. All deaths in Act 2. Key lessons absorbed into playbook:
- Brimstone + Book of Stabbing anti-synergy caused 2 deaths (Runs 91, 100) -- quadratic damage growth
- 3 Cultists threshold revised to 60% (5th death at 52% HP, Run 96)
- Shop indexing bug fixed (CommunicationMod purge offset)
- Boss relic collection bug unresolved (2 occurrences, Runs 71, 77)
- Floor average plateaued at 25-26 for 40+ runs at the 100-run milestone

## Runs 101-110 Summary (BREAKTHROUGH -- Act 2 boss reached twice)

4 logged deaths. Average death floor: ~24.5. TWO Act 2 boss reaches (F33). Guardian regression: 2 deaths.
- Run 103 (F16): Guardian death. Pandora's Box from Neow removed all Defends. Deck had only Iron Wave (5 block) and Flame Barrier (12 block). Maximum block ~12 vs 32-damage attack. RNG-driven unwinnable deck.
- Run 105 (F33): MILESTONE -- Bronze Automaton (Act 2 boss). Deck met 3/4 readiness criteria (AOE via Thunderclap+, Str via Spot Weakness, Healing via Feed+). Block scaling gap: only basic Defends (4x5=20 max) vs Hyper Beam (38 damage). Artifact stripping executed correctly (Thunderclap+ x2 + Bash+). Died turn 8 at 7 HP unable to block 24 incoming. Block scaling added as 4th mandatory readiness criterion.
- Run 107 (F16): Guardian death. Corruption+ played turn 9. All Skills exhausted by turn 14. Guardian at 10/240 HP but zero block cards remaining. Now Hard Rule #9 (no Corruption vs Guardian without Dead Branch/FNP).
- Run 110 (F33): MILESTONE -- The Collector (Act 2 boss). Deck met ALL 4 readiness criteria. Strong deck: Whirlwind+ (AOE), Spot Weakness+Inflame (Str), Feed (Healing), Shrug It Off+Flame Barrier++Metallicize (Block). HP entry was 57% (49/86) instead of required 70%. Colosseum event forced combat before boss. Missing Impervious and Shockwave+ meant post-debuff crisis unwinnable at 25 HP. 70% threshold validated.

KEY FINDINGS AT 110 RUNS:
1. F25-26 plateau BROKEN. Two consecutive Act 2 boss reaches.
2. 4-criteria readiness checklist is WORKING -- decks arrive at boss well-prepared.
3. New bottleneck: surviving Act 2 boss fights (block scaling + HP entry threshold).
4. Impervious and Shockwave+ identified as disproportionately important for Act 2 boss survival.
5. Hard Rule #9 added: no Corruption vs Guardian without Dead Branch/FNP.
6. Guardian "solved" status has two known exceptions: Pandora's Box and Corruption without exhaust payoffs.

## Runs 111-123 (GAP -- not analyzed)

Runs 111-123 were not individually analyzed. Known death floors from run_stats: Run 112 (F25), Run 114 (F33), Run 116 (F21), Run 118 (F21), Run 121 (F16), Run 123 (F16). Some findings from these runs were already incorporated into playbook updates (strategy.md scorecard, Spheric Guardian third survival, 3 Cultists threshold, etc.) based on partial analysis during those runs.

## Run 124 — Ironclad A0, Death Floor 23

DECK: Whirlwind, Inflame+, Bash+, Impervious, Barricade, Shockwave, Rampage, Thunderclap, Shrug It Off x3, Intimidate, Demon Form, Strike+ x2, Defend x2
RELICS: Burning Blood, Gambling Chip, others
CAUSE OF DEATH: Gremlin Leader elite at Floor 23. Entered at 42/80 HP (52%), below 60% threshold. Rally scaled to +12 Str (4 Rallies). By Turn 9, incoming was 68/turn (Leader 18x3 + gremlins 14) vs 10 HP with 13 block.
KEY MOMENTS: (1) Barricade+Impervious combo dominated Guardian fight -- 30 permanent block wall led to clean boss kill. (2) Spheric Guardian survived with Barricade+Impervious+Regen Potion but drained 32 HP (80->48). (3) Impervious wasted on Turn 1 of Gremlin Leader for 30 block against 22 incoming, zero damage dealt. (4) Systematic Weak multiplier misapplication -- player applied 0.75 to own damage when enemies were Weakened (not player), underestimating own damage output throughout Act 2.
LESSONS: (1) Impervious Turn 1 against Gremlin Leader is wrong -- use for Turn 4-5 when Rally damage peaks. (2) Weak direction confusion is a recurring mechanics error that needs correction. (3) Third consecutive run with no Reaper/Feed offered -- backup healing plan exists but wasn't enough. (4) Barricade+Impervious is a confirmed strong combo for Guardian.

## Run 125 — Ironclad A0, Death Floor 33

DECK: Immolate, Reaper, Demon Form, Flame Barrier+, Inflame, Bash+, Battle Trance, Rampage, Shrug It Off+, Intimidate, Thunderclap, Headbutt, Panacea, 2 Strikes, 4 Defends
RELICS: Burning Blood, Lantern, Preserved Insect, Red Mask, Liquid Memories (potion)
CAUSE OF DEATH: Bronze Automaton Hyper Beam on Turn 6. 51 damage vs 27 block at 24 HP = exactly 24 unblocked = exactly lethal (0 HP).
KEY MOMENTS: (1) CLOSEST to beating an Act 2 boss -- died by exactly 1 HP. Met 70% HP threshold for the first time (60/80 = 75%). All 4 readiness criteria met. (2) Intimidate exhausted on Turn 1 for Artifact stripping instead of saved for Hyper Beam. Weak would have reduced 51 to 38, surviving at 13 HP. (3) Liquid Memories used to recover Intimidate from exhaust -- but Liquid Memories retrieves from DISCARD, not EXHAUST. Mechanics misunderstanding. (4) Stasis stole Demon Form + Flame Barrier+, both recovered by killing Orbs but Demon Form was never played. (5) Reaper confirmed critical for Act 2 -- healed 16->30 HP in 3 Cultists fight via AOE. (6) SIO+ block miscalculated as 8 instead of 11 on Hyper Beam turn.
LESSONS: (1) Save exhausting Weak sources (Intimidate, Shockwave) for Hyper Beam, use Bash+/Thunderclap for Artifact stripping. (2) Liquid Memories cannot recover exhausted cards. (3) Hyper Beam can reach 51 damage (higher than prior 38-45 range). (4) Always use upgraded values in calculations after upgrading.

## Run 126 — Ironclad A0, Defeat Floor 21
DECK: Reaper, Carnage+, Demon Form, Dropkick, Ghostly Armor, Headbutt, Armaments+, Shrug It Off+, Bash+, starters + Pain curse
RELICS: Burning Blood, Toy Ornithopter, (chest relic)
CAUSE OF DEATH: Shelled Parasite + Fungi Beast at 7 HP with no potions. Unwinnable at that HP.
KEY MOMENTS: Beat Guardian using Mode Shift cancellation (cancelled both 32-hit and 5x4=20). Beat Spheric Guardian with Demon Form scaling (41 HP drain). Chosen fight drained 32 HP (39->7), setting up lethal next fight.
LESSONS: (1) Demon Form as sole Str source leaves Reaper healing too slow -- need front-loaded Str (Inflame/Spot Weakness) to make Reaper effective. (2) Armaments+ block value (5 block) was forgotten in survival calculations -- documented prominently. (3) Missing AOE for entire run (criterion 2 unmet). (4) Chosen is a reliable death spiral trigger in Act 2 (30-40 HP drain even with good cards).

## Run 127 — Ironclad A0, Defeat Floor 23
DECK: Inflame+, Whirlwind+, Flame Barrier+, Shockwave, Offering, Bash+, Thunderclap, Intimidate, Pommel Strike, Headbutt, Shrug It Off, 4 Strikes, 4 Defends
RELICS: Burning Blood, Preserved Insect, Regal Pillow, others
CAUSE OF DEATH: Slavers elite at Floor 23, entered at 19/80 HP (23%) with zero potions. Three enemies dealt lethal damage Turn 1 despite mass Weak+Vuln from Shockwave.
KEY MOMENTS: (1) Strong Act 1 -- beat Slime Boss cleanly with Whirlwind+ AOE, met 3/4 readiness criteria (Str, AOE, block scaling). (2) Snecko fight at F22 drained HP to 19 via Confusion + Vulnerable combo; smart Duplication Potion play on 0-cost Strike under Confusion saved the fight. (3) Forced elite at F23 with no potions and 23% HP. Turn 1 played Shockwave (2E) + Pommel Strike (1E) for damage instead of Shockwave + Defend for 5 block. Died to combined Weakened damage. (4) No healing card (Reaper/Feed) offered entire run -- 5th run in 7 with healing RNG denial.
LESSONS: (1) Block-first at critical HP -- Defend over damage when sub-30% HP. (2) Healing RNG denial is the most persistent failure pattern. (3) Confusion + Duplication Potion synergy confirmed (target 0-cost cards). (4) Slavers HP data: ~36 HP per Slaver (with Preserved Insect -25%, base ~48).

## Run 128 — Ironclad A0, Defeat Floor 24
DECK: Evolve, Fire Breathing+, True Grit+, Feel No Pain, Flame Barrier, Immolate+, Disarm, Shockwave+, Uppercut+, Armaments, Anger, Thunderclap, Offering, Shrug It Off, 3 Strikes, 3 Defends
RELICS: Burning Blood, Pen Nib, Prayer Wheel, others
CAUSE OF DEATH: Shelled Parasite + Fungi Beast at Floor 24. Entered at 37/80 (46%) with zero potions. Drew no block cards on final turn (5 attacks + Evolve), took 16 unblocked damage at 14 HP.
KEY MOMENTS: (1) Evolve + Fire Breathing+ engine beat Hexaghost cleanly (36/80 HP remaining). Confirmed second clean victory with this engine. (2) Exhausted Fire Breathing+ via True Grit+ against Shelled Parasite+Fungi Beast, reasoning "no major status generation" -- but Immolate Burns would have triggered 10 free damage each, shortening the fight. Critical synergy awareness error. (3) Three consecutive monster rooms (F20-22) drained HP: Shelled Parasite (-41), Centurion+Mystic (-16 after Blood Potion), Snecko (-33). Act 2 death spiral from consecutive combat. (4) Pen Nib doubled Immolate for 42 AOE in key fights (Centurion+Mystic, Spike Slime split). (5) No Strength scaling entire run despite Prayer Wheel giving double card rewards.
LESSONS: (1) Do not exhaust Fire Breathing+ when Immolate is in the deck -- Burns trigger 10 free damage bypassing Plated Armor. (2) Shelled Parasite + Fungi Beast now at 3 deaths -- Plated Armor fights without Str scaling are a death trap. (3) Healing RNG denial continues: 6th run in 8 with no Reaper/Feed offered. (4) Gambler's Brew saved the Snecko fight by rerolling a lethal Confusion hand.

## Run 129 — Ironclad A0, Defeat Floor 16
DECK: 3 Strike, 4 Defend, Bash+, Inflame+, Headbutt, Twin Strike, Spot Weakness, Ghostly Armor, Shrug It Off, Intimidate, Flame Barrier
RELICS: Burning Blood, Darkstone Periapt, (chest relic)
CAUSE OF DEATH: Hexaghost Burns accumulation. By Turn 12, 5+ Burns/Burns+ in deck dealing 4 damage each at end of turn. Burns ate block, leaving nothing for Hexaghost attacks. Hexaghost at ~43/250 HP (17% remaining) when killed.
KEY MOMENTS: (1) Neow removed 2 Strikes for thin 8-card deck. Strong Str scaling: Inflame+ (+3) + Spot Weakness (+3) = up to +9 Str. (2) Turn 2 critical error: spent all 3E on Inflame+ + Spot Weakness + Ghostly Armor (10 block vs ~30 multi-hit incoming = 20 unblocked damage, 55->35 HP). The 20 HP lost here was the margin that made Burns lethal by Turn 12. (3) No AOE -- 5 small slimes fight drained 15 HP unnecessarily. (4) No healing beyond Burning Blood. (5) Intimidate forced on Turn 11 at 7 HP for survival instead of saved for Inferno. (6) Flame Barrier played Turn 12, too late to save.
LESSONS: (1) Hexaghost Turn 2 blocking is mandatory -- even with strong Str scaling, 20 unblocked damage on Turn 2 makes Burns lethal later. Budget at least 1E for block on Turn 2. (2) Burns+ (upgraded Burns) deal 4 damage each, not 2 -- significantly worse than regular Burns. (3) This is the 4th Hexaghost death despite extensive playbook guidance -- Turn 2 setup greed is a new specific failure mode not previously documented. (4) Deck had strong damage scaling but missing AOE and healing criteria.

## Run 140 — Ironclad A0, Defeat Floor 19 (FIRST RUN WITH NEW HEURISTICS)
DECK: Strike+, Strike x2, Defend x3, Defend+, Bash+, Spot Weakness, Thunderclap+, Ghostly Armor, Evolve, Sword Boomerang
RELICS: Burning Blood, Shuriken, Golden Idol, Potion Belt
CAUSE OF DEATH: Looter + Mugger at F19. Entered at 7/74 HP with 0 potions and only 1 Defend in opening hand vs 20 incoming. No survival path existed.
KEY MOMENTS: (1) Strong Act 1 -- Slime Boss killed at 3 HP using Spot Weakness + Limit Break Str engine. Evolve neutralized Slimed clog. Clean execution of split phase kill sequencing. (2) Entered Act 2 at 74/74 HP (full heal between acts). First fight was 3 Byrds. Turn 2: all 3 Byrds attacked for 38 combined damage with only 1 Defend in hand. Fight took 8 turns, drained 73 HP (74 to 1). Worst Byrd fight documented. (3) Map forced Monster room at F19 with no non-combat alternative. 7 HP (1 + 6 Burning Blood) vs 20 incoming = dead.
LESSONS: (1) Byrd fight HP drain range is 20-73, not 20-58. Worst case all-attack turns are unblockable with bad hand draws. (2) Act 2 routes MUST include non-combat room in first 2-3 floors as safety valve. All entry points were Monster rooms -- no escape. (3) New heuristics (Full Block, Full Act Pathing, Tier List) were applied correctly throughout. Death was caused by encounter RNG + map structure, not heuristic failure. (4) Minor prediction error: Spot Weakness described as +4 Str but card was unupgraded (+3). (5) No healing card offered (8th of last 10 runs).

## Run 141 — Ironclad A0, Defeat Floor 8
DECK: Strike x4, Defend x4, Bash, Headbutt, Shrug It Off, Thunderclap + Parasite curse
RELICS: Burning Blood, Neow's Lament, Ceramic Fish
CAUSE OF DEATH: 2x Fungi Beast at F7 (Unknown room). Entered at 41/85 HP (48%) with Parasite curse clogging draws. Fungi Beast Str scaling reached 12 and 15 damage by Turn 6. Combined 27 incoming vs 18 max block = lethal at 9 HP.
KEY MOMENTS: (1) Neow's Lament gave 3 free fights but only Headbutt + SIO added to deck -- near-starter deck entered Sentries elite at F5. (2) Sentries fight took 20 turns (estimated 7-8), drained 56 HP (76->20). No AOE, Strikes dealing only 2 effective damage per hit through Metallicize 4. (3) Mushrooms event eaten for 21 HP heal at 20 HP -- playbook omitted that Eat gives Parasite curse. Curse clogged draws in subsequent Fungi fight. (4) Unknown at F7 resolved as combat at 48% HP. Fungi Beast Str scaling undocumented in playbook -- buff turns give +3 Str each, making late-fight damage 12-15 per Fungi instead of the documented ~9.
LESSONS: (1) Sentries without AOE/damage scaling is a 20-turn, 56-HP-drain fight -- elite readiness is about DECK, not just HP. (2) Mushrooms Eat option gives Parasite curse (playbook corrected). (3) Fungi Beast buff is +3 Str per buff turn, not a passive -- damage escalates to 12-15 by Turn 5-6 (playbook corrected). (4) Neow's Lament creates a false elite-readiness signal: full HP after 3 free fights but starter-quality deck. (5) No command/sequence bugs found -- reported issues were player confusion with Headbutt selection interface.

## Run 142 — Ironclad A0, Defeat Floor 24
DECK: Bash+, Iron Wave+, Thunderclap+, Inflame, Flame Barrier, Feed, Headbutt, Second Wind, Intimidate, Strike x3, Defend x3
RELICS: Burning Blood, Neow's Lament, Sundial, Juzu Bracelet, Ceramic Fish (boss relic SKIPPED, Act 1 chest relic SKIPPED)
CAUSE OF DEATH: Centurion + Mystic at F24. Centurion's 10x3 = 30 multi-hit attack at 3 HP. No block cards or potions remaining after Mystic kill phase.
KEY MOMENTS: (1) Clean Slime Boss kill at 46/80 HP. Thunderclap+ was mandatory AOE for split. Feed obtained from boss card reward. (2) **BOSS RELIC SKIPPED** -- two `proceed` commands bypassed BOSS_REWARD screen. 3rd confirmed occurrence (Runs 71, 77, 142). (3) **ACT 1 CHEST SKIPPED** -- `proceed` on Floor 9 Treasure room bypassed chest. No relic collected. (4) Feed killed 3 enemies for +9 Max HP (80->89). Feed+Headbutt combo used correctly. (5) Juzu Bracelet bought at shop (147g) gave safe Act 2 Unknown rooms. (6) Blood Potion used on 3 Cultists fight (F20), not available for Centurion+Mystic. Duplication Potion + Liquid Memories both used on Mystic kill, leaving zero potions for Centurion solo phase. (7) Centurion 10x3 = 30 multi-hit not previously documented in playbook. Entered fight at 61/86, drained to 0 over 4 turns.
LESSONS: (1) Centurion has a 10x3 = 30 multi-hit attack (playbook corrected from 12-18 single hit). (2) Boss relic skip bug is now confirmed 3x -- MUST be fixed at infrastructure level. (3) Treasure chest skip is a new related bug. (4) Potion allocation across two-phase fights matters -- do not spend everything on phase 1 (Mystic) when phase 2 (Centurion solo) still has lethal attacks. (5) Deck lacked block scaling (no Shrug It Off, Impervious) -- only Flame Barrier and Iron Wave+ for block beyond Defends. Against 30 incoming, max block from hand was ~17 (Flame Barrier 12 + Defend 5), insufficient.

## Run 143 — Ironclad A0, Defeat Floor 33
DECK: Bash+, 2x Impervious+, Inflame+, Evolve+, Cleave, Clothesline, Shrug It Off, Pommel Strike, Headbutt, Strike+ x2, Defend x3, Intimidate
RELICS: Burning Blood, Golden Idol, Self-Forming Clay, Whetstone, Horn Cleat, Mark of Pain, Toy Ornithopter, Strawberry
CAUSE OF DEATH: Bronze Automaton at 7/300 HP. Hyper Beam #2 dealt 57 damage (45 base + 12 Str) with only 13 block and 54 HP. Both Impervious+ exhausted on earlier turns. Could not output enough damage to kill in 13 turns.
KEY MOMENTS: (1) CLOSEST Act 2 boss kill -- Automaton at 7 HP when player died. (2) No UI misplays: boss relic (Mark of Pain) collected, both treasure chests opened, all shops browsed, all events evaluated. First clean run since UI bugs identified. (3) Distilled Chaos potion randomly played Impervious+ from draw pile on Hyper Beam #1 for 40 block -- saved that turn via RNG. Without this potion, Hyper Beam #1 would have been lethal. (4) Both Impervious+ used on Snake Plant hallway fight (zero damage taken), then restored after combat. Both upgraded at rest sites before boss. But neither drawn on either Hyper Beam turn in boss fight -- draw RNG failure in a Wound-diluted deck. (5) Mark of Pain + Evolve+ engine worked excellently: 4E + 2 draws per Wound = 5-7 cards per turn. (6) Duplicator event duplicated Impervious (2 copies, both upgraded to Impervious+). (7) Excellent hallway fight execution: zero damage vs Snake Plant (6 turns), 1 damage vs Jaw Worm, minimal damage vs all others.
LESSONS: (1) Hyper Beam #2 can reach 57 damage (Str scales to 12 by turn 12). Previous max was 51. Updated bronze-automaton.md. (2) Inflame+ alone (+3 Str) is marginal sustained damage against 300 HP -- need a second Str source or burst damage to kill before Hyper Beam #2. (3) Mark of Pain + Evolve+ is a confirmed powerful engine but Wounds dilute the deck, reducing probability of drawing specific cards (Impervious+) on critical turns. (4) Clothesline is the best Weak source for Automaton because it does not exhaust -- can apply Weak on both Hyper Beam turns. (5) Distilled Chaos is an excellent emergency tool -- can randomly play Impervious+ from draw pile when not in hand.

## Run 144 — Ironclad A0, Defeat Floor 16
DECK: Strike x2, Defend x4, Bash+, Sword Boomerang, Headbutt, Rampage, Evolve, Iron Wave
RELICS: Burning Blood, Incense Burner, Potion Belt
CAUSE OF DEATH: Hexaghost at 7/250 HP. ARITHMETIC ERROR: played Iron Wave (13 damage) against 20 HP Hexaghost with Headbutt (17 damage) in hand and 2E remaining. Wrote "13 > 20" in reasoning. Ended turn in same command line as attack.
KEY MOMENTS: (1) CRITICAL ARITHMETIC ERROR cost the run. Iron Wave + Headbutt = 30 > 20 HP, easy kill. Player committed `play Iron Wave 0; end` before finishing the kill calculation. (2) Cultist Potion + Rampage scaling was devastating: Rampage dealt 45 damage on 3rd play with +6 Str and Vuln. Hexaghost went from 250 to 20 HP in 8 turns. (3) Evolve handled Burns perfectly, no hand clog despite no Fire Breathing. (4) Incense Burner Intangible triggered twice, enabling all-offense turns. (5) Sentry fight cost 51 HP (73->22) with no AOE, 12 turns. (6) Deck thinned to 12 cards (3 Strikes removed via 2 events + 1 shop). (7) No Weak source found all run. (8) No UI misplays -- second consecutive clean run.
LESSONS: (1) NEVER include `end` in the same command as an attack on potential kill turns. Play attack, verify kill, then end separately. New checklist item #4 added. (2) Cultist Potion + Rampage is a confirmed powerful boss-killing engine. (3) Incense Burner is excellent vs Hexaghost (2 Intangible turns in 12-turn fight). (4) Entering boss at 47% HP (below 70% threshold) was survivable thanks to Cultist Potion scaling and Incense Burner, but left zero margin for error.

## Run 146 — Ironclad A0, Defeat Floor 12
DECK: Strike x3, Defend x4, Bash+, Shockwave, Shrug It Off, Limit Break (dead — no Str source)
RELICS: Burning Blood, Golden Idol, Bird-Faced Urn, Incense Burner
CAUSE OF DEATH: Gremlin Nob (elite F11). Entered at 43/80 (53%) with 7 Skills vs 4 Attacks. Forced to play Skills for survival on T5 (+4 Str to Nob). Died T7-T8 at 0 HP.
KEY MOMENTS: (1) Sentries at F6 drained 52 HP (60->8) with near-starter deck — only 2 monster rooms before elite. (2) Golden Idol Smash cost 20 HP before Sentries (80->60), compounding crisis. (3) Limit Break from Neow was dead weight (0 Str entire run). (4) Clean execution otherwise: zero hallway damage in Cultist and Slime fights, correct Bash+ upgrade, good Strike removal.
LESSONS: (1) Do not path into elites with only 0-2 monster rooms beforehand — not enough fights to build a deck. (2) Golden Idol Smash before an elite is reckless — 20 HP loss reduces elite survivability. (3) Limit Break as Neow rare is dead without a Str source. (4) Deck Attack/Skill ratio matters for Nob — 7 Skills vs 4 Attacks makes most hands unplayable.

## Run 147 — Ironclad A0, VICTORY Floor 51 (FIRST WIN EVER)

DECK: 22 cards — Bash+, Immolate+, Heavy Blade (upgraded to + via Blessing of the Forge in Automaton fight), Impervious x2, Spot Weakness+, Limit Break, Dual Wield+, Evolve, Rampage, Headbutt+, Anger+, Cleave, Flame Barrier, Metallicize, Shrug It Off, Strike x2, Defend x3
RELICS: Burning Blood, Omamori, Anchor, Dream Catcher, Busted Crown (Act 1 boss), Maw Bank, Toy Ornithopter, Nunchaku, Paper Phrog, Champion Belt, Sling of Courage, Snecko Eye (Act 2 boss), Regal Pillow, Whetstone, Bag of Marbles, Maw Bank
VICTORY: Donu and Deca (Act 3 Boss), Floor 51, Score 652, Final HP 31/80
KEY MOMENTS: (1) Neow's Lament gave 3 free fights -- built deck safely. Living Wall upgraded Bash at F3 for free. Immolate from F11 card reward was the run-defining pickup. (2) Lagavulin elite defeated in 5 turns taking only 16 damage -- Spot Weakness+ + Headbutt recycling Bash+ for Vuln. (3) Slime Boss defeated cleanly -- Immolate+ and Evolve handled the split phase. Took Impervious from boss card reward + Busted Crown (4E) as boss relic. (4) Book of Stabbing elite (Act 2) defeated at 57% HP using Immolate+ burst. Headbutt top-decked Immolate+ for 48 Vuln damage Turn 4. Took Limit Break from Dream Catcher + Maw Bank. (5) Bronze Automaton defeated at 80/80 HP. Essence of Steel + Blessing of the Forge potions. Str scaled to 16 via Spot Weakness+ x2 + Limit Break. Heavy Blade+ dealt 94 damage in a single play. Took Snecko Eye as Act 2 boss relic -- the single most impactful decision in the run. (6) Donu and Deca defeated in 6 turns. Immolate+ at 0E from Snecko on Turn 1. Dual Wield+ copied Immolate+ twice for TRIPLE 34 AOE (102 damage) on Turn 4. Limit Break doubled Str 6 to 12. Heavy Blade 50-damage finisher on Deca. 3 potion uses healed 15 HP via Toy Ornithopter during the boss fight.
LESSONS: (1) Snecko Eye + high-cost Str-scaling deck = the winning formula. Draw 7 cards with 0-cost rolls on Immolate+ and Heavy Blade is game-breaking. (2) Toy Ornithopter patched the healing gap when Reaper/Feed never appeared -- 3 potion uses = 15 HP in the final boss fight. (3) Dual Wield+ on Immolate+ is the strongest offensive combo observed (102 AOE in one turn). (4) Full HP entry at every boss (Slime Boss 80/80, Automaton 80/80, Donu+Deca 80/80) was enabled by Regal Pillow (+15 rest healing) and smart pathing. (5) Zero UI misplays -- fifth consecutive clean run. Both boss relics collected, all chests opened, shops browsed.

## Run 148 — Ironclad A0, VICTORY Floor 51 (SECOND WIN -- BACK TO BACK)

DECK: 17 cards — including Immolate+, Limit Break+ (upgraded F40), Flex+, Heavy Blade, and others
RELICS: 9 relics including Snecko Eye (Act 2 boss), Gambling Chip, Bronze Scales
VICTORY: Donu and Deca (Act 3 Boss), Floor 51, Score 703, Final HP 4/85
KEY MOMENTS: (1) Snecko Eye again as Act 2 boss relic -- 2nd consecutive win with it. (2) Limit Break+ upgrade at F40 campfire was the most impactful decision -- enabled infinite Str doubling. (3) Flex+ into Limit Break+ gave 10 Str on Turn 4 of boss fight. (4) Duplication Potion on 0-cost Immolate+ dealt 60 AOE Turn 3. (5) Snecko Oil Turn 1 expanded hand to 10 cards. (6) Bronze Scales killed Deca at 4 HP from its own attacks. (7) Fairy in a Bottle saved the run vs Spikers/Guardians. (8) Darklings killed with simultaneous AOE. (9) Gambling Chip improved Turn 1 hands by mulliganing expensive Snecko Eye draws.
LESSONS: (1) Snecko Eye + Immolate+ + Limit Break is the confirmed winning formula (2 consecutive wins). (2) Limit Break+ upgrade is the #1 campfire priority approaching Act 3 boss. (3) Flex+ has real value with Limit Break+ (temporary Str gets doubled into permanent). (4) Gambling Chip + Snecko Eye is a powerful consistency combo. (5) Bronze Scales can deliver killing blows at very low HP. (6) Zero UI misplays -- sixth consecutive clean run.

## Run 150 — Ironclad A0, VICTORY Floor 51 (THIRD WIN -- Barricade Engine)

DECK: 24 cards — Bash, Immolate (upgraded via Blessing of the Forge), Iron Wave, Carnage+, Offering, Feed, Barricade, Corruption, Feel No Pain, Metallicize, Evolve, Disarm, Spot Weakness, Shrug It Off, Second Wind+, Entrench+, 2x Impervious, Body Slam+, Apotheosis, 3 Defend, 1 Strike
RELICS: Fusion Hammer (Neow swap), White Beast Statue, Anchor, Blood Vial, Preserved Insect, Ornamental Fan, Cursed Key (Act 1 boss), Empty Cage (Act 2 boss), Frozen Egg, Molten Egg, Toxic Egg, The Boot
VICTORY: Time Eater (Act 3 Boss), Floor 51, Final HP 26/87
KEY MOMENTS: (1) Neow swapped Burning Blood for Fusion Hammer. Blessing of the Forge x2 upgraded key cards early. (2) Immolate on F3. Barricade+Corruption+FNP engine assembled by F21. (3) Apotheosis from Sensory Stone event solved upgrade problem. (4) Body Slam+ from Nemesis elite completed the damage loop. (5) Time Eater defeated via Entrench+ doubling block to 138, Body Slam+ for 146 damage.
LESSONS: (1) Barricade+Corruption+FNP+Entrench+Body Slam is a second winning formula. (2) Fusion Hammer as Neow swap viable with Apotheosis. (3) Three wins in four runs confirms A0 competence.

## Run 145 — Ironclad A0, Defeat Floor 44 (NEW BEST FLOOR -- FIRST ACT 3!)
DECK: 23 cards — Bash+, Impervious, Wild Strike+, Whirlwind+, Immolate+, Armaments+, Inflame+, Rampage+, Feed+, Barricade+, Evolve+, 2x Metallicize(3+4), Bloodletting+, Headbutt, 3x Strike+, 3x Defend+
RELICS: Burning Blood, Golden Idol, Ancient Tea Set, Mummified Hand, Sundial, Ectoplasm, Frozen Egg, Pantograph, Maw Bank, Omamori, Ceramic Fish, Gremlin Horn, Fusion Hammer
CAUSE OF DEATH: The Transient (Floor 44, Act 3). Impervious played Turn 1 against 30 damage (wasted). Turn 2: all attacks drawn, 0 block, took 40 unblocked (77->37). Turn 3: 50 incoming, 11 block max, died by 2 HP.
KEY MOMENTS: (1) FIRST run to beat BOTH Act 1 and Act 2 bosses. Guardian killed cleanly via Mode Shift cancellation (both 32-damage attacks cancelled). Collector killed at 5/282 HP with Rampage+ scaling. (2) Barricade+ (from Frozen Egg auto-upgrade) + 2x Metallicize (7 block/turn stacking) dominated Act 3 hallways. The Maw (300 HP) defeated at 0 damage taken. (3) Mummified Hand enabled 2-4 free plays per turn with 5 Powers in deck. (4) Feed gave +3 max HP on Orb Walker kill (77 max HP). (5) Ancient Writing event upgraded ALL Strikes and Defends (9 free upgrades). (6) Card index shifting bug caused Impervious to be accidentally played in Maw fight. (7) Third consecutive clean run -- no UI misplays.
LESSONS: (1) Impervious against Transient must be saved for Turn 3+ (50-70 damage). Turn 1 (30 damage) is handleable by Defend+ and block cards. (2) Barricade + 2x Metallicize is the strongest sustained defense engine observed -- makes Act 3 hallway fights trivial. (3) Mummified Hand is S-tier in Power-heavy decks (4-5 Powers). (4) Collector HP confirmed at 282. (5) Full HP heal confirmed between Act 2 and Act 3.

## Run 152 — The Silent A0, Defeat Floor 33
DECK: 19 cards — Noxious Fumes+, Footwork+, After Image, Phantasmal Killer+, Piercing Wail+, Flechettes+, Sneaky Strike, Dagger Throw+, Backflip+, Cloak and Dagger+, Acrobatics+, Concentrate+, All-Out Attack+, Neutralize (Innate), Survivor, 4x Defend + Necronomicurse
RELICS: Pocketwatch, Ring of the Snake, Kunai, Necronomicon, Ceramic Fish, Bloody Idol, Nunchaku, Bottled Flame, Matryoshka, Whetstone
CAUSE OF DEATH: The Collector, Floor 33. Failed to play After Image and Footwork+ in early turns -- both were in discard unplayed when Turn 4 triple debuff landed. Without defensive powers active, post-debuff incoming of 60-90 effective damage was unsurvivable at 20 HP.
KEY MOMENTS: (1) Poison-through-block strategy crushed Spheric Guardian (89 block irrelevant). (2) Pocketwatch discipline excellent -- consistently played 3 or fewer cards to trigger +3 draw. (3) Refused Sssserpent gold despite shop nearby (net 100g missed). (4) Slavers elite took 35 HP despite strong deck. (5) Collector Turn 4 Vuln+Frail+Weak at 20 HP was lethal.
LESSONS: (1) Defensive powers (After Image, Footwork+) must be played in first 2 turns of Collector fight -- they are the Silent's answer to post-debuff crisis. (2) Curse-giving events should be evaluated against nearby shops for net-profit removal. (3) Split timing on slimes is a defensive tool -- splitting a slime about to attack prevents the incoming damage entirely.

## Run 151 — The Silent A0, Death Floor 50 (FIRST SILENT RUN)
DECK: 31 cards — Neutralize+, Survivor, 4x Strike, 5x Defend (1 upgraded), After Image+, Blade Dance, Quick Slash, Flying Knee, Infinite Blades, Flash of Steel, Finisher, Well-Laid Plans, Tools of the Trade, Accuracy, Sneaky Strike, Corpse Explosion, Footwork, Noxious Fumes, Blur, Adrenaline, Reflex, Backflip+, Deflect+, Catalyst+, Parasite (curse)
RELICS: Ring of the Snake, Bird-Faced Urn, Wing Boots, Regal Pillow, Fusion Hammer, Enchiridion, Letter Opener, Sozu, War Paint
CAUSE OF DEATH: Awakened One Phase 2, Turn 14. 6 HP vs 16x3 = 48 multi-attack with 28 block. AO at 188/300 HP with Regenerate 10.
KEY MOMENTS: (1) First Silent run reached Act 3 boss. Poison + shiv archetype. (2) Played 6 Power cards into Awakened One (After Image+, Footwork, Infinite Blades, Noxious Fumes, Accuracy, Tools of Trade), giving AO +6 Str minimum across phases. Player declared powers "essential" and ignored Curiosity mechanic. (3) The +6 Str turned a survivable 10x3 = 30 multi-attack into lethal 16x3 = 48. With 28 block and 6 HP, the extra Str from Powers was the exact margin of death. (4) Catalyst+ was exhausted (poison tripling is one-shot), AO down to 188/300 but Regenerate 10 healing each turn. (5) Sozu blocked all potion use. (6) Void status drained energy.
LESSONS: (1) Awakened One Curiosity mechanic is the CENTRAL consideration of the fight, not a footnote. Playing Powers freely into it is a fundamental misunderstanding of the boss. Created awakened-one.md. (2) Power-heavy Silent decks (7 Powers in deck) are specifically bad against Awakened One. Deck building for Act 3 should factor in the visible boss. (3) Sozu is dangerous for boss fights that need emergency potion use. (4) Phase 2 strips all buffs -- Powers played in Phase 1 provide zero carry-over value, only the Str given to the boss mattered.

## Run 153 — The Silent A0, Defeat Floor 45
DECK: 21 cards (all upgraded) — Noxious Fumes+, Deadly Poison+ (innate), Catalyst+, Well-Laid Plans+, Tools of the Trade+, Tactician+, Wraith Form+, After Image+, Footwork+, Malaise+, 2x Piercing Wail+, Neutralize+, Survivor+, Backflip+, Deflect+, 2x Defend+, 2x Strike+
RELICS: Ring of the Snake, Hovering Kite, Plated Armor 4 (Thread and Needle), Pocketwatch, Mark of the Bloom, Girya, Blue Candle, others
CAUSE OF DEATH: Transient at Floor 45. Fading 1 (last turn), Transient dealt 48 damage (after PW+ and Malaise debuffs) vs 41 block (38 played + 3 Plated Armor) at 3 HP. Died 7 damage short. Transient would have faded at end of its turn.
KEY MOMENTS: (1) Mind Bloom "I am Awake" upgraded all cards but gave Mark of the Bloom (cannot heal). At 69/70 HP, player reasoned "healing is irrelevant" -- but fights remained before the boss. (2) Mysterious Sphere fight (2 Orb Walkers with +3 Str/turn each + Burns) drained 66 HP (69 to 3). Mark of the Bloom made this permanent. (3) Catalyst+ spent on Orb Walkers to kill one fast, exhausting it before Awakened One boss. (4) Wraith Form+ gave 3 Intangible (turns 1-3 safe) but -1 Dex/turn left Dex at -2 by turn 5, reducing block output. (5) Poison engine dominated Act 3 hallways -- near-zero damage in Spiker+Repulsor, Darklings. Card retention engine (WLP+ + TotT+ + Tactician+ + Hovering Kite) was excellent.
LESSONS: (1) Mind Bloom "I am Awake" is a trap when fights remain before the boss. Mark of the Bloom prevents ALL healing. Updated mind-bloom.md. (2) Do not fight Mysterious Sphere when Mark of the Bloom is active. Created mysterious-sphere.md. (3) Catalyst+ is irreplaceable for Awakened One -- do not spend on hallway fights. (4) Wraith Form+ Dex penalty makes Transient turns 4-5 extremely tight. Updated transient.md with Silent-specific strategy. (5) Best Silent floor yet (45 vs 50 and 33).

## Run 154 — The Silent A0, Defeat Floor 16
DECK: 16 cards — 2x Footwork+, Dash+, Masterful Stab, Deflect, Backflip, Quick Slash, Neutralize+, Crippling Cloud, Setup+, Survivor, 2x Defend, Strike
RELICS: Astrolabe, Art of War, Molten Egg
CAUSE OF DEATH: Hexaghost at 24/250 HP. 23-turn fight. Second Inferno (8x6=48) hit with hand of all Burns. Zero playable cards on final turn. Burns+ (12+ per turn) had accumulated to unsurvivable levels.
KEY MOMENTS: (1) Astrolabe from Neow transformed 3 Strikes into 2x Footwork+ and Setup+ -- incredible defensive core but zero damage scaling. (2) Zero damage taken in 5/6 pre-boss hallway fights. Masterful Stab at 0E confirmed excellent in short fights. (3) Hexaghost fight: blocking was trivial (Dex 6 = Defend 11, Deflect 10, Dash+ 19, Survivor 14) but damage output was only ~10/turn average. (4) Masterful Stab cost escalated from 0E to 4-7E by Turn 12 due to Burns chip damage, becoming unplayable. Setup+ was used twice to reset its cost. (5) Crippling Cloud saved for first Inferno (Turn 16, reduced to 6x6=36). Neutralize+ used for ongoing Weak. (6) No poison scaling in deck -- Catalyst+, Deadly Poison, and Noxious Fumes were never offered or taken during Act 1 card rewards.
LESSONS: (1) Block without damage loses to Hexaghost -- 5th death confirms this pattern. Dex 6 blocks everything except Burns, which are unblockable end-of-turn damage. (2) Masterful Stab is a trap against Hexaghost -- Burns chip damage makes it unplayable by mid-fight. Created masterful-stab.md. (3) Silent has NO native Burns management (no Evolve, Fire Breathing, True Grit). Kill speed through poison scaling is the only answer. (4) Art of War encourages all-block turns but the fight demands mixed offense+defense -- anti-synergy with Hexaghost where damage output matters most.

## Run 155 — The Silent A0, Defeat Floor 23
DECK: 19 cards — 2x Footwork+, Accuracy, Blade Dance, Cloak and Dagger, Tools of the Trade, Piercing Wail, Quick Slash, Dagger Throw, Sneaky Strike, Neutralize+, Survivor, 3x Defend, 2x Strike, Backflip
RELICS: Ring of the Snake, Pocketwatch, Sacred Bark, Juzu Bracelet, Mercury Hourglass, Cursed Key, Golden Idol
CAUSE OF DEATH: Book of Stabbing elite at Floor 23. Entered at 33/70 HP (47%) with zero potions. Book's double scaling (+1 hit/turn AND +3 Str/turn) overwhelmed Dex 6 block by Turn 6. Dealt 137 of 161 HP but could not survive the 30 incoming on final turn (11 block vs 30 = 19 unblocked at 13 HP).
KEY MOMENTS: (1) Act 1 clean -- Slime Boss near-zero damage with Cultist Potion (Sacred Bark doubled to Ritual 2) + Shiv burst. (2) Sentry + Spheric Guardian fight (Act 2 F22) drained 26 HP (59->33) -- Turn 3 drew zero block cards against 10x2, taking 20 unblocked. (3) Forced into Book of Stabbing at 47% HP with no alternative route. (4) Piercing Wail used Turn 2 defensively (Str -6 made that turn zero damage), unavailable for later turns when damage peaked. (5) All 4 Powers (Accuracy, 2x Footwork+, TotT) set up by Turn 3 but each cost 1E of damage tempo.
LESSONS: (1) Book of Stabbing has +3 Str/turn -- not just +1 hit/turn. Double scaling makes damage grow quadratically. Updated book-of-stabbing.md. (2) Silent Dex stacking cannot keep pace with Book's Str scaling. Need poison, Malaise, or exhaust tools. (3) 47% HP into a forced elite is a death sentence. (4) Sacred Bark doubling potions is extremely strong (Cultist Potion -> Ritual 2, Essence of Steel -> 8 Plated Armor). (5) Spending 3 turns setting up Powers against Book trades early-fight damage tempo for late-fight defense -- but the fight does not last long enough for the defense to matter.

## Run 156 — The Silent A0, Defeat Floor 33
DECK: ~20 cards — Noxious Fumes+, Wraith Form, After Image, Footwork+, Blur, Phantasmal Killer+, Piercing Wail+ (exhaust), Flechettes+, Sneaky Strike, Dagger Throw+, Backflip+, Cloak and Dagger+, Acrobatics+, Concentrate+, All-Out Attack+, Neutralize (Innate via Bottled Flame), Survivor, 4x Defend, Necronomicurse
RELICS: Pocketwatch, Astrolabe (boss relic replacing Ring of the Snake), Kunai, Nunchaku, Bottled Flame, Matryoshka, Whetstone, Bloody Idol, Ceramic Fish, Necronomicon
CAUSE OF DEATH: The Collector, Floor 33. 19-turn fight. Wraith Form played too early, causing permanent cumulative -1 Dex/turn. By Turn 19, Dex was -17 or worse. All Skill-based block (Defend, Survivor, Backflip+) produced 0 block. After Image provided ~7-8 block/turn (only remaining block source) but insufficient against Collector's Str-scaled attacks. Collector at 5/282 HP when player died -- 5 HP short of winning.
KEY MOMENTS: (1) Beat Slime Boss Act 1 cleanly. Astrolabe transformed 3 Strikes into useful cards. (2) Act 2 progression was solid -- beat Chosen, Byrds, Snecko, Snake Plant, Slavers, Centurion+Mystic, Sentry+Spheric Guardian. Took Necronomicon from Cursed Tome event. (3) Poison-through-block strategy effective against Spheric Guardian (Noxious Fumes+ ignores Barricade). (4) Collector fight lasted 19 turns due to DEFEND_BUFF turns and Torch Head respawns. Each DEFEND_BUFF gave all enemies +3 Str, scaling Collector from Str 3 to Str 14+. (5) Wraith Form played early for Intangible safety, but -1 Dex/turn accumulated to -17 by Turn 19, destroying all Skill block. (6) After Image was the ONLY functional block source at high negative Dex (~7-8 block/turn from card plays). (7) Blur carried block from Intangible turns to post-Intangible turns, partially bridging the gap. (8) Collector died 5 HP after the player -- if 5 more block existed on any single turn, the fight was won.
LESSONS: (1) Wraith Form must be delayed until the final 5-6 turns in boss fights expected to last 15+ turns. Playing early in a long fight creates an unrecoverable Dex deficit. Created wraith-form.md with detailed timing rules. (2) After Image is the Silent's only block source immune to Dex drain and Frail -- it gives flat 1 block per card played regardless of debuffs. It must be active before the Collector's Turn 4 triple debuff. Created after-image.md. (3) Blur is the critical companion card to Wraith Form -- carries block from Intangible turns (when damage is irrelevant) to post-Intangible turns (when Dex penalty makes new block impossible). Created blur.md. (4) The Collector's DEFEND_BUFF gives +3 Str to ALL enemies per use. In a 19-turn fight, this scaled the Collector from Str 3 to Str 14+. Updated the-collector.md with Str scaling documentation. (5) The fight was lost by 5 HP -- being 5 HP short suggests the strategy was close to viable but Wraith Form timing was the critical error.
