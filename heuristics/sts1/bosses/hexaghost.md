# Hexaghost

**Core rule:** Damage output is the #1 priority. [[debuffs/Weak]] and block keep you alive temporarily, but insufficient damage is the actual killer. In 13+ turn fights, Burns accumulate and create a death spiral.

## Preparation Checklist (must have at least 3 of 4)

1. **Weak source** ([[cards/Shockwave]], [[cards/Clothesline]], [[cards/Intimidate]], [[potions/Weak Potion]]) -- reduces all damage by 25%. Inferno scales with accumulated [[buffs/Strength]] from [[cards/Inflame]] turns (first Inferno: 24 at A0, 30 at A4; second Inferno: 36 at A0, 42 at A4). Without Weak, this damage must be blocked outright. Highest-value survival prep — but Weak keeps you alive without winning the fight; kill speed can substitute (see What Works).
2. **HP for an expected 30-50 HP fight** (run the ledger before the final rest site decision) OR [[relics/Pantograph]] relic
3. **Passive block** ([[cards/Metallicize]], [[cards/Flame Barrier]]) OR [[cards/Impervious]] for the Inferno turn
4. **Burns management** OR damage scaling to end the fight before Burns overwhelm

## Burns Management (CRITICAL)

**Block absorbs Burn damage.** Burns resolve at end of turn while your block is still active, so every point of leftover block eats Burn damage one-for-one. Block math for this fight is therefore (incoming attack + 2 per Burn in hand, 4 per Burn+) — over-block by the Burn total instead of treating it as unavoidable chip.

Priority order:
1. [[cards/Evolve]] + [[cards/Fire Breathing]] (the best anti-Burns engine -- Burns become free damage with no downside)
2. Evolve standalone (neutralizes hand clog)
3. [[cards/True Grit]] (exhaust Burns for 9 block)
4. Fire Breathing standalone (Burns drawn deal 6-10 damage to Hexaghost)
5. [[cards/Second Wind]] (mass Burns removal)
6. Damage scaling (Inflame, [[cards/Spot Weakness]], [[cards/Demon Form]], [[cards/Rampage]]) -- shortens fight from 13 to 8-9 turns

**[[cards/Dark Embrace]] is NOT Burns management.** It draws a card when you exhaust a Burn, but Burns replenish every Sear turn. Once the deck has 3+ Burns, exhausting one with True Grit+ draws another Burn from the saturated draw pile. The "engine" becomes a wash. Dark Embrace is strong with finite status cards (Wounds, [[cards/Dazed]]) but counterproductive against Hexaghost's continuously replenishing Burns.

## Strategy

- **Turn 1 (free):** Setup. Demon Form is ideal. Otherwise: [[cards/Thunderclap]] + Metallicize + Evolve.
- **Turn 2 (MUST BLOCK):** Divider = (floor(HP/12)+1) x 6 multi-hit. At 80 HP = 42, at 67 HP = 36, at 50 HP = 30. Budget at LEAST 1E for block. Do not spend all 3E on setup. Use [[cards/Headbutt]] on Turn 1 to place Impervious on top of draw pile if Impervious is in the discard.
- **Save Weak for Inferno:** Apply Shockwave/Clothesline on the first Inferno turn.
- **Kill speed matters:** Shorter fight = fewer Burns = less attrition.

## What Works

- Evolve + Fire Breathing engine (the cleanest answer to Burns)
- [[potions/Cultist Potion]] + Rampage (devastating scaling, can kill in 9 turns without Weak)
- Demon Form (+2 Str/turn, best scaling card for Hexaghost)
- Spot Weakness+ (+4 Str on attack turns)
- Flame Barrier+ (16 block + counter damage from Inferno's 6 hits = 36 counter at Flame Barrier+ value of 6/hit)
- [[relics/Incense Burner]] ([[buffs/Intangible]] on Inferno turn negates it entirely)

## What NOT to Do

- Fight without Burns management OR damage scaling (Weak alone keeps you alive but does not win the fight — Burns accumulate until the death spiral)
- Play [[cards/Brutality]] (Burns + Brutality self-damage = death spiral)
- Play [[cards/Berserk]] (self-[[debuffs/Vulnerable]] + Inferno = death)
- Waste Shockwave on a non-Inferno turn
- Take [[relics/Odd Mushroom]] when Hexaghost is boss (17% less Vuln damage extends fight)
- Buy Dark Embrace to handle Burns (draws more Burns from the saturated deck -- see Burns Management above)

## Character Matchups

**[[characters/Silent]]:** No native Burns management. Only solution is kill speed: poison scaling ([[cards/Deadly Poison]] + [[cards/Catalyst]], [[cards/Noxious Fumes]]) or [[cards/Shiv]] burst with amplifiers ([[cards/Accuracy]], [[cards/Terror]]). Save [[cards/Piercing Wail]] for Inferno (do NOT spend on [[enemies/Gremlin Nob]]). Save [[cards/Crippling Cloud]] for Inferno turn (Weak is worth more than 4 poison). [[cards/Masterful Stab]] is a trap (cost increases with Burns chip damage).

**[[characters/Watcher]]:** Enter Wrath ONLY on free/debuff turns (Inflame intent). Do NOT enter Wrath on Turn 2 (Divider would be doubled = instant death). [[cards/Wave of the Hand]] for Weak on Inferno. Kill speed target: 9-11 turns via Wrath burst. [[cards/Judgment]] finishes at 30-40 HP remaining.
