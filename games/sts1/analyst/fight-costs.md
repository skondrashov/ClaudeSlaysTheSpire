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
