# resources/sts1 — authoritative game data

Reference data extracted **directly from the Slay the Spire game jar** —
`SlayTheSpire/desktop-1.0.jar` — not the wiki or memory. This is the
source-of-truth that ontology entries (cards, enemies, encounters, buffs)
should be verified against. It is *resources* (raw decoded data), not
ontology/heuristics.

## Contents

- `localization/*.json` — verbatim copies of the game's English localization
  (`localization/eng/` inside the jar): `powers.json` (buff/power text),
  `stances.json` (Wrath/Calm/Divinity), `monsters.json`, `cards.json`,
  `relics.json`, `potions.json`, `keywords.json`. These give canonical
  **wording/mechanics** but NOT numeric values (HP/damage live in compiled code).
- `localization/encounter-display-names.json` — the player-facing encounter
  names (jar `ui.json` → `RunHistoryMonsterNames`).
- `monsterhelper-getencounter.txt` — lossless decode of
  `MonsterHelper.getEncounter()` bytecode: each encounter's **internal key** and
  the monster classes it constructs (its roster). The authoritative encounter
  compositions. Encounters whose monsters are built by helpers/loops (Slimes,
  Gremlin Gang, Louse, Shapes) show empty/partial bodies — see the ontology
  encounter files for their resolved rosters.
- `encounter-name-map.json` — internal `getEncounter` key → player-facing display
  name, for the 18 encounters where they differ (e.g. `"2 Thieves"` →
  `"City Muggers"`, `"Chosen and Byrds"` → `"Chosen Flock"`). The ontology
  encounter files use the **display** names.

## Regenerating

The jar lives at `C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\desktop-1.0.jar`.
Localization is plain JSON inside the jar (read with any zip tool). Encounter
compositions require decoding `MonsterHelper.class` bytecode (no `javap` in the
bundled JRE) — the extraction script used this session is the reference method.

## Provenance notes

- Two canonical name systems exist: the internal `getEncounter` keys (e.g.
  `"Gremlin Gang"`, `"3 Cultists"`) and the display names (`"Gang of Gremlins"`,
  `"Triple Cultists"`). The community wiki generally uses the internal keys.
- Numeric values (enemy HP, attack damage, buff magnitudes) are NOT in this data;
  they live in compiled monster classes and still require the wiki or a
  community dataset.
