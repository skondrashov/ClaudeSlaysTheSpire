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
