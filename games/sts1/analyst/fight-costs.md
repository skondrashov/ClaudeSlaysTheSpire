# Fight Costs — paid-HP data, keyed to the deck that paid it

The statistical home for what fights actually cost. Heuristic pages do NOT carry prices (a stored "expected cost" anchors the player toward paying it and stops the cheaper-line search — see hp-management.md); they carry the fight's damage clock and reduction levers. The numbers live here, as data: one line per priced fight, with the deck shape that produced the number, so patterns are minable ("attrition decks pay 2-3x vs Spheric-likes") without ever compressing back into a scalar budget.

Format: `enemy | paid | ascension | character | deck shape (the relevant interaction) | run/audit ref`

Audits append a line for each fight whose cost was notable (unusually cheap, unusually dear, or structurally interesting). Curate prunes only for redundancy, never for age — old points are still data.

## Seed data (migrated from the retired heuristic-page cost rows and recent audits)

- Gremlin Nob | 11 | A9 | Silent | zero-skills race + Weak coverage | run 243
- Gremlin Nob | 43 | A9 | Silent | skill-led, no race line | run 241
- Gremlin Nob | 18 | A9 | Ironclad | T1 potion-Corruption free-skill turn | run 240
- The Guardian | 17 | A9 | Silent | poison ticks cancelling Mode Shift x3 | run 243
- The Guardian | 22 | A9 | Silent | shiv burst, mode-shift cancels | run 241
- Spheric Guardian | 21 | A9 | Silent | Artifact strip (CE/Neutralize) then poison through Barricade | run 243
- Spheric Guardian | 28 | A9 | Ironclad | attack-led per amendment, no engine | run 242
- Spheric Guardian | 42 | A9 | Ironclad | Corruption block engine (attrition mirror) | run 240
- Spheric Guardian | 16 | A9 | Ironclad | attack line, baseline | run 234
- Centurion + Mystic | 24 | A9 | Silent | Mystic burst inside one heal window (Flex Potion) | run 243
- Centurion + Mystic | ~25-61 historical band | A2-A9 | mixed | legacy book row, decks unrecorded | pre-243 pages
- The Collector | 4 | A9 | Ironclad | Barricade bank on free Spawn turn, exact-lethal Torch Head clears | run 242
- Snake Plant | 0 | A9 | Silent | Piercing Wail on the multi-hit + poison | run 243
- Snake Plant | ~15-42 historical band | mixed | mixed | legacy book row, decks unrecorded | pre-243 pages
- Gremlin Leader | death from 40/70 | A9 | Silent | 8-turn engine vs 5-6-turn clock, forced entry | run 243
- Byrd flock | ~36-73 historical band | mixed | mixed | legacy book row, decks unrecorded | legacy
- Chosen | ~30-40 historical band | mixed | mixed | legacy book row, decks unrecorded | legacy
- Donu & Deca | death at 21-24 block ceiling vs 44 ramped beams | A9 | Silent | shiv burst, one Footwork | run 241
- Slavers | ~20-40 historical band | mixed | mixed | legacy book row, decks unrecorded | pre-243 pages
- Shelled Parasite | ~40-50 historical band | mixed | mixed | legacy book row: decks without a large-hit engine | pre-243 pages
- Writhing Mass | ~25-40 historical band | mixed | mixed | legacy book row, decks unrecorded | pre-243 pages
- Snecko | ~25-40 historical band | high ascension | mixed | legacy book row, decks unrecorded | pre-243 pages
- Book of Stabbing | ~25-45 historical band | mixed | mixed | legacy book row: exhaust tools + front-loaded burst | pre-243 pages
- Gremlin Leader | ~25-45 historical band | mixed | mixed | legacy book row: decks killing by turn 5-6 | pre-243 pages
- Byrd flock | ~20 | mixed | mixed | legacy book row: Thunderclap AOE + burst, ~7-turn kill (the 36-73 band above is the no-AOE row) | pre-243 pages
- Slime Boss / Bronze Automaton / Time Eater | ~30-50 historical band each | mixed | mixed | identical generic row on the legacy boss pages, decks unrecorded — likely a template budget, low confidence (same row on Guardian/Collector pages contradicted by run data above and dropped) | pre-243 pages
- 3 Sentries | 6 | A9 | Silent | NF+ poison race, artifact stripped by cheap debuffs first, outer-then-middle kill order | run 244
- Gremlin Nob | 14 | A9 | Silent | zero-skills race, Duplication Potion 6-shiv T1, NF+ played as Power exception | run 244
- Hexaghost | 33 | A9 | Silent | NF+ clock + Terror 99-vuln T2, killed T8 before second Inferno; Divider eaten at 29 | run 244
- Gremlin Leader | 3 | A9 | Silent | kill-speed pricing vindicated: T1 Sneaky kill + T2 Wizard kill, Terror+Bane burst, NF+/Envenom ~30/turn, 146 HP down T6 | run 244
- Book of Stabbing | 6 | A9 | Silent | shiv race + per-hit-denial blocking (24-32 ceilings), Speed Potion on worst multi-stab turn | run 244
- The Collector | 56 (29 of it a self-inflicted double-end skipped turn + the Fairy; ~27 organic) | A9 | Silent | poison clock kill T11; crisis turn spent on revive-surviving permanents | run 244
- Nemesis | 45 | A9 | Silent | structurally dear for shiv/poison decks: Intangible halves the clock (poison ticks 1), Scythe 45 vs ~30 block ceiling; page-compliant execution, priced off realized elite averages at routing — the mispricing, not the play | run 244
- Transient | death from 6/70 (T1-4 taken at ZERO, T5 80 > 62 max mitigation) | A9 | Silent | strip line played to ceiling; A2+ ladder is 40-80, not the page's 30-70 | run 244
- Transient | ~24 net (70 post-Offering -> 39, SURVIVED) | A9 | Ironclad | attacked every turn to trigger Shifting (Immolate+/Heavy Blade+/Cleave dropping each turn's hit), T5 Str -90 via Spot Weakness+Heavy Blade+Immolate reduced the 80 to ~0; Block Potion T4, Impervious held — the correct line, contrast run 245's pure-block inversion | run 246
- Giant Head (burning elite) | ~20 net (65 -> 45, ~12-turn marathon) | A9 | Ironclad | Slow exploited via multi-card burst turns (Double Tap+Immolate+/Heavy Blade+), Essence-of-Steel+Regen (Sacred-Bark doubled) sustaining the long race vs Metallicize 8 + Regen 7; won but expensive | run 246
- Reptomancer | 43 (71 -> 28) | A9 | Ironclad | Shockwave+/Cleave/Immolate+ AOE held the dagger swarm and Double Tap+Immolate+ chunked the body, but NO potions left (spent on Giant Head one floor prior via the forced treasure->elite funnel) — the cost is downstream of the routing commit, not the play | run 246
- Nemesis | death from 28/87 (Scythe 45 -> Defend to 6, then T3 Impervious mis-spent on the 21 Attack, T4 Weak'd-33 Scythe unblockable) | A9 | Ironclad | back-to-back forced elite with no rest (entered at 32% off Reptomancer); Impervious-allocation misplay is execution, the 28-HP entry is routing | run 246
