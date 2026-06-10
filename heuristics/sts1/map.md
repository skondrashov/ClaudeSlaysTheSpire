# Map Routing

## Relic Economy: Why Elites Matter

Relics are the primary driver of run strength. Every winning formula was built on specific relics ([[relics/Snecko Eye]], [[relics/Dead Branch]], [[relics/Mummified Hand]], [[relics/Bottled Lightning]], [[cards/After Image]] via [[relics/Bottled Tornado]]). Elites are the primary source of relics — each elite drops a relic guaranteed. Skipping elites means fewer relics means weaker runs.

**Elite targets per act:**
- **[[acts/Act 1]]: Fight 2 elites.** The Act 1 elite pool ([[enemies/Gremlin Nob]], [[enemies/Lagavulin]], Sentries) is the easiest in the game. Two elite relics + boss relic = 3 relics by [[acts/Act 2]]. If the map offers a 2-elite path with rest site coverage, take it. Only settle for 1 elite if the map forces bad rest site spacing or the deck is still starter-quality at Floor 5.
- **Act 2: Fight 1-2 elites.** Act 2 elites are dangerous but the relic rewards are stronger (rare pool). If HP is above 60% and the deck has its scaling engine online, path through at least 1 elite. Skip only when the deck cannot handle the matchup (e.g., [[relics/Brimstone]] vs [[enemies/Book of Stabbing]]).
- **[[acts/Act 3]]: Fight 0-1 elites.** Act 3 elites ([[enemies/Giant Head]], [[enemies/Reptomancer]], [[enemies/Nemesis]]) are extremely dangerous. Only take an elite if the path naturally includes one and the deck is strong. Don't go out of the way for Act 3 elites.

**When comparing routes, elites are a POSITIVE, not just a risk.** A route with 1 elite + 1 rest site is often better than a route with 0 elites + 2 rest sites, because the relic from the elite compounds for the rest of the run while the extra rest only heals one fight's worth of damage.

## Full Act Pathing

**At the START of each act, read the ENTIRE map.** Count elites, shops, campfires, and unknowns on every viable route. Choose a full route before floor 1. This replaces room-by-room pathing.

**Priority order: safety gate first, then default-aggressive.** Check the Elite Route Safety Rule and HP thresholds first — routes that fail the gate are off the table. Among routes that pass, default to the most elite-heavy one. These two doctrines are sequential, not in tension.

- **Default to the elite-heavy route.** Only downgrade to the safe route when HP or deck quality can't handle the elite pool.
- **Re-route only when forced.** Follow your act plan. Only deviate if HP drops below safe thresholds.
- **At each floor, verify the planned route is still viable.** Count remaining forced combats to the next rest site. If the path forces 2+ combats and HP is below 50%, re-route.
- Prefer routes with a rest site in the last 1-2 floors before the boss.
- After a brutal fight (Byrds, [[enemies/Centurion]]+[[enemies/Mystic]]), next room MUST be healing, not another combat.
- If the path forces an elite at low HP, skip it entirely — take any alternative path.

## Act 2 Route Selection

- **Act 2 route must include a non-combat room in the first 2-3 floors.** The first Act 2 hallway fight can be 3 Byrds (50-73 HP drain), [[enemies/Spheric Guardian]] (30-41 HP drain), or other high-damage encounters. If the first 2-3 floors are all Monster rooms with no rest/shop/event escape valve, a single brutal fight leaves no recovery option. Prefer routes where a rest site, shop, or event appears by floor 2-3.
- **Evaluate rest site density across the entire path.** Count forced combats between rest sites on each viable path. A route of M-R-E-M-M-?-E forces 6 fights with only 1 rest site. Prefer paths where rest sites break up combat sequences (e.g., M-M-R-M-R-E gives recovery opportunities). At reduced Max HP (post-Apparitions, post-Vampires), rest site density is even more critical.
- **Unknown rooms are NOT safe in Act 2.** They resolve as any hallway fight ~50% of the time, including Byrds, [[enemies/Snake Plant]], and Spheric Guardian. Treat Unknown rooms as Monster rooms when routing in Act 2. **At below 30% HP, Unknown rooms are lethal.**

## Elite Route Safety Rule

**Never route through an elite unless at least one rest site is reachable within 2 floors after the elite, OR HP is above 70% and no second elite follows before a rest.**

Routing into elites without rest site coverage is a common cause of death:
- A Monster path that locks into a following Elite floor with no rest option leaves no way to recover HP before the fight.
- Back-to-back elites with no rest between (e.g. Gremlin Nob costing ~26 HP, then Lagavulin) compound HP loss past survivable levels.

Before committing to an elite path, trace the route forward: count forced combats between the elite and the next rest site. If the path forces 2+ combats after the elite with no rest, take the safer route unless HP is above 70%.

## Elite Risk Assessment

Before fighting an elite, check:
1. **HP threshold**: Below 30 HP for Act 1 elites is dangerous. Below 60% for Act 2 elites.
2. **Deck vs elite matchup**: Gremlin Nob punishes Skill-heavy decks. Lagavulin punishes slow decks. Sentries need AOE or damage scaling. Count your Attack/Skill ratio before committing to an elite path. **Minimum 3 monster rooms before first elite** — 0-2 fights are not enough to build a deck that can handle any Act 1 elite.
3. **Damage scaling check**: Before routing through Act 1 elites, verify the deck has at least one damage scaling source ([[cards/Inflame]], [[cards/Spot Weakness]], [[cards/Carnage]], or a strong Uncommon attack). Without scaling, high-HP elites ([[enemies/Lagavulin]] 110 HP, Sentries 40+42+42) are DPS races that base-damage decks cannot win. Entering Lagavulin with no Str source means you cannot deal enough damage before its Siphon Soul debuffs compound, and the fight is unwinnable.
4. **Potions available**: Potions compensate for bad matchups.
5. **Path alternatives**: Only prefer a safer path if the elite risk is unmanageable. Don't default to "safer path exists, take it."

**Act 2 Elite Threat Ranking (most to least dangerous):**
- **Book of Stabbing**: Double scaling — +1 hit/turn AND +3 Str/turn. Wounds clog draw pile. NEED: exhaust for Wounds, fast kill, 60%+ HP. **If you have Brimstone, DO NOT FIGHT. Brimstone + Book of Stabbing = unsurvivable.**
- **[[enemies/Gremlin Leader]]**: Rally gives +3 Str to ALL enemies per cast. Must win by turn 5-6 or Rally scaling overwhelms you (see [[layer:heuristics, enemies/Gremlin Leader]]). NEED: AOE for gremlins, [[cards/Shockwave]] for mass debuff, 60%+ HP.
- **Slavers**: 3 enemies, 27+ combined damage from Turn 1. NEED: AOE, mass debuff, block density, 50%+ HP (see [[layer:heuristics, enemies/Slavers]]).

## Brimstone Elite Avoidance

If Brimstone is equipped, the Act 2 elite pool becomes asymmetrically dangerous:
- **Book of Stabbing: HARD AVOID.** Brimstone + multi-hit + hit-count escalation = quadratic damage growth.
- **Snake Plant: CAUTION.** Brimstone adds +2/turn to each of its 3 hits.
- **Gremlin Leader: MODERATE RISK.** Brimstone adds +2 to every gremlin. With Rally +3, combined scaling is +5 Str/turn to all enemies.

When holding Brimstone, avoid elite paths entirely if HP is below 70%.

## Pre-Boss Routing (last 5 floors)

- **No HP-for-reward trades.** No [[events/Knowing Skull]], [[relics/Golden Idol]], or HP-cost events.
- **Skip elites in the last 3 floors.** Relic value < boss HP threshold. High-drain elites (Slavers especially — 20-40+ HP) within 2 floors of the boss almost guarantee a sub-threshold boss entry; see [[layer:heuristics, enemies/Slavers]].
- **Rest over upgrade at every rest site if below 70% HP.**
- **Path priority: Rest > Shop > Event > Monster > Elite.** Invert normal priority.
- **Unknown rooms before the boss carry [[events/Colosseum]] risk** (forced combat, 15-25 HP drain — even with [[relics/Juzu Bracelet]]). Prefer known rooms in the last 2 floors.
- Count forced combats on each path to the boss. Potion use is aggressive by default (see Potion Economy in [[layer:heuristics, combat]]); a path forcing many combats is a reason to drink even sooner, not a special trigger.

## Fairy Management

[[potions/Fairy in a Bottle]] is often consumed in Centurion+Mystic fights. If Fairy is your only death insurance, plan paths so Fairy is available for the most dangerous fight (elite or boss).

## Mark of the Bloom = No Optional Combat

If [[relics/Mark of the Bloom]] is active, every point of damage is permanent. Under this condition:
- Do NOT fight [[events/Mysterious Sphere]], Unknown rooms, or elites unless forced.
- Take only shops, rest sites (upgrades only), events with known non-combat outcomes.
