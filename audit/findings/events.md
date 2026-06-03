# Audit: Events (ontology/sts1/events + heuristics/sts1/events)

COVERAGE: read 33 ontology + 33 heuristic files.
Ontology files: living-wall, scrap-ooze, transmogrifier, old-beggar, pleading-vagrant, the-joust, woman-in-blue, world-of-goop, the-library, shining-light, masked-bandits, big-fish, knowing-skull, mysterious-sphere, forgotten-altar, cursed-tome, mushrooms, colosseum, sssserpent, mind-bloom, the-cleric, ancient-writing, face-trader, the-nest, vampires, wheel-of-change, match-and-keep, bonfire-spirits, purifier, ominous-forge, golden-idol, council-of-ghosts, augmenter.
Heuristic files: same 33 stems (1:1 with ontology; verified via glob — no missing companion, no cross-pair broken links).

## DEFECTS

[HIGH] C:\Users\tkond\projects\praxis\ontology\sts1\events\the-nest.md — FACT-ERROR / CONTRADICTION: "Stay: Heal 10 HP, obtain Ritual Dagger card". In real StS "Stay" (let the cultist stab you / "Take the dagger") you LOSE 6 HP and gain Ritual Dagger — it is HP loss, not a 10 HP heal. The companion heuristic repeatedly assumes the correct value ("6 HP can be lethal", "absorb the 6 HP loss", "The 6 HP loss cannot be recovered"), so ontology contradicts its own heuristic. FIX: change to "Stay: Lose 6 HP, obtain [[cards/Ritual Dagger]]".

[HIGH][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\augmenter.md — FACT-ERROR: J.A.X. described as "0 cost, Exhaust: Deal 2 damage for each card in your hand." Real J.A.X. is "Lose 3 HP. Gain 2 Strength" (upgraded: Gain 3 Strength), 0-cost Colorless. The stated effect appears fabricated/confused with another card. Error is mirrored into the heuristic ("J.A.X. deals 2 damage × hand size... 10-14 damage for 0E", Snecko/Runic-Pyramid synergy) — both layers wrong. FIX: correct the J.A.X. effect in ontology to "Lose 3 HP, gain 2 Strength" and rewrite the heuristic's J.A.X. paragraph (it is now strength-scaling, not hand-size damage).

[HIGH][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\forgotten-altar.md — FACT-ERROR / FACT-INCOMPLETE: "Sacrifice: Lose 20 HP, gain 5 Max HP" and "Desecrate: Gain Decay curse" omit the relic reward. Real Forgotten Altar grants the **Bloody Idol** relic on the Sacrifice path (and the event also has a Golden-Idol-present "Offer" variant); Sacrifice cost is a % of Max HP, not a flat 20, and there is no "+5 Max HP". The "+5 Max HP" looks conflated with a different event. FIX: verify against StS wiki and restate options (Sacrifice → lose Max-HP%, gain Bloody Idol; Desecrate → gain Decay; add Golden-Idol "Offer" variant if present). Heuristic's "+5 Max Hp is permanent value" also depends on this.

[HIGH][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\bonfire-spirits.md — FACT-INCOMPLETE: presented as plain "Offer: Remove a card from your deck." Real Bonfire Spirits burns ONE chosen card and grants a reward keyed to that card's RARITY (Basic/Curse → no/negative reward; Common/Uncommon → heal; Rare → full heal + Spirit Poop relic), then ends. The reward mechanic and rarity scaling are entirely missing, and the heuristic's "Remove Strikes first" is the wrong frame (you burn high-rarity for the best reward). FIX: restate option to include the rarity-based reward table.

[MED] C:\Users\tkond\projects\praxis\heuristics\sts1\events\ancient-writing.md — CONTRADICTION / BROKEN option name: body discusses "Elegance" but the Priority line reads "Simplicity ... > **Insight** (few basic cards)". Ontology options are Simplicity / Elegance — "Insight" is not an option of this event. FIX: replace "Insight" with "Elegance".

[MED][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\face-trader.md — FACT-ERROR: "receive a random relic and lose a random relic". Real Face Trader "Touch" loses HP (a % of Max HP) and grants a relic (the Cultist Mask / a random relic); it does NOT remove one of your relics. FIX: drop "lose a random relic"; specify HP cost as Max-HP%.

[MED][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\golden-idol.md — FACT-ERROR: trap penalties given as flat numbers "Outrun: Lose 6 Max HP" and "Smash: Take 20 damage". Real StS uses percentages (Outrun ≈ lose 8% Max HP; Smash ≈ take 25% current HP as damage; Hide → gain Injury curse). FIX: restate as percentages and name the curse (Injury).

[MED][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\wheel-of-change.md — FACT-INCOMPLETE: outcomes listed as "gain Gold, lose HP, heal to full, gain a Curse, or gain a card" (5, vague). Real Wheel has 6 equal segments including a **relic** and a **card-removal/Purge** outcome; "heal to full" is actually heal a set amount, and the damage segment is a fixed value. FIX: enumerate all 6 segments with their amounts; the heuristic's "-8 HP" / "full heal" framing depends on this.

[MED][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\scrap-ooze.md — FACT-ERROR (mechanic): "Lose 3 HP. 25% chance to find a Relic. Repeatable..." Real Scrap Ooze cost ESCALATES each Reach Inside (3, then 4, 5...) and the success chance INCREASES per attempt (~25% then +10%/attempt). Flat "3 HP / 25% each" is wrong on both axes. FIX: state escalating HP cost and rising success probability. (Heuristic's "Expected cost 12 HP / 4 attempts" derivation is built on the wrong flat model.)

[MED][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\knowing-skull.md — FACT-INCOMPLETE: asks listed only as "Lose HP (escalating cost per ask)" with no reward magnitudes; "Leave: Costs 6 HP". Real Knowing Skull gives specific rewards (e.g., gold ask ≈ 90 gold, potion ask, card-reward ask) at escalating HP costs, and the leave cost equals the running HP counter (not a fixed 6 once you've engaged). FIX: add reward amounts and clarify leave-cost mechanic.

[MED][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\mushrooms.md — FACT-ERROR: "Eat: Heal 21 HP". Real StS heals a percentage of Max HP (~25%), not a flat 21. FIX: state as "Heal 25% Max HP" (verify exact %). (Stomp / 3 Fungi Beasts / Odd Mushroom is correct.)

[MED][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\cursed-tome.md — FACT-ERROR/INCOMPLETE: stage damage "1/2/3, final Lose 10 HP". Real Cursed Tome deals escalating damage across the pages (commonly cited as 1, 2, 3 on early pages then a larger final hit ≈ 10–15) — verify the exact final value and whether per-stage values match. FIX: confirm numbers vs wiki.

[MED][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\world-of-goop.md — FACT-INCOMPLETE: "Leave: Nothing happens." In real World of Goop, leaving still has you LOSE some gold dropped in the goop (the "Leave" path is not strictly neutral). FIX: verify and, if so, note the gold loss on Leave.

[MED][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\pleading-vagrant.md — FACT-ERROR(cost): "Offer Gold: Pay 85 Gold". Verify the gold cost (Pleading Vagrant cost is commonly 85 but confirm it is not act-scaled). FIX: confirm 85.

[MED][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\the-cleric.md — FACT(cost/amount): Heal "Pay 35 Gold, heal HP" (real = heal 25% Max HP — amount omitted); Purify "Pay 50 Gold". Verify Purify cost (50 vs 75) and add the 25% heal magnitude. FIX: add heal amount; confirm Purify price.

[LOW][VERIFY] C:\Users\tkond\projects\praxis\ontology\sts1\events\vampires.md — FACT-INCOMPLETE: "Lose approximately 30% of Max HP" omits the **Blood Vial** interaction (if you hold Blood Vial, it is consumed and the option text/penalty changes). FIX: note Blood Vial variant.

[LOW] C:\Users\tkond\projects\praxis\ontology\sts1\events\augmenter.md — FORMAT: uses "Act 2 event." + "## Options" + numbered list, diverging from the uniform "- **Act:** / - **Options:**" bulleted format used by the other 32 ontology files. FIX: normalize to standard template.

[LOW] C:\Users\tkond\projects\praxis\heuristics\sts1\events\match-and-keep.md — NO-EVIDENCE/anecdote leak: "(observed: [[cards/Bash]] and [[cards/Perfected Strike]] added to a deck that did not want them)" reads as a run-log artifact rather than a general heuristic. FIX: generalize ("can force unwanted Basic/Strike-tier cards") or drop the parenthetical.

[LOW] C:\Users\tkond\projects\praxis\heuristics\sts1\events\the-library.md — HEDGE/OVERCLAIM: "the best opportunity to find Reaper, Feed..." and "probability of at least one healing card... much higher" assert a probability without a number and slightly overstate (the 20-card pool is character/rarity-weighted, not uniform). FIX: soften or quantify; keep as heuristic.

[LOW] C:\Users\tkond\projects\praxis\heuristics\sts1\events\scrap-ooze.md — NOT-ACTIONABLE-RISK: HP-budget table is built on the incorrect flat 25%/3-HP model (see ontology finding); recommendations (e.g. "spend up to 12 HP = 4 attempts") will misprice once the ontology is corrected to escalating cost/odds. FIX: recompute after ontology fix.

## CLEAN
ontology: living-wall, transmogrifier, old-beggar, the-joust, woman-in-blue, the-library, shining-light, masked-bandits, big-fish, mysterious-sphere, colosseum, sssserpent, mind-bloom, ominous-forge, council-of-ghosts, match-and-keep, purifier.
heuristics: living-wall, scrap-ooze (logic ok modulo ontology error), transmogrifier, old-beggar, pleading-vagrant, the-joust, woman-in-blue, world-of-goop, shining-light, masked-bandits, big-fish, knowing-skull, mysterious-sphere, forgotten-altar, cursed-tome, mushrooms, colosseum, sssserpent, mind-bloom, the-cleric, face-trader, the-nest, vampires, wheel-of-change, bonfire-spirits, purifier, ominous-forge, golden-idol, council-of-ghosts, augmenter.

## PATTERNS
- RECURRING (known): "fixed numbers where real StS uses percentages" — the dominant systemic error here: the-nest (6 HP heal sign error), mushrooms (21 HP), golden-idol (6 Max HP / 20 dmg), forgotten-altar (20 HP / +5), face-trader, the-cleric, council-of-ghosts/vampires (already correctly hedged "~%"). Many heal/damage values are hard-coded for an ~80-HP Ironclad rather than expressed as Max-HP%.
- RECURRING (known): errors mirrored across both layers — augmenter (J.A.X.) and forgotten-altar propagate the same wrong fact into ontology AND heuristic.
- RECURRING (known): broken cross-category wikilinks — [[cards/J.A.X.]] and [[cards/Ritual Dagger]] have no ontology page (glob: no file). Systemic, outside events scope but flagged.
- NEW SYSTEMIC PATTERN: "escalating-mechanic flattened to a constant" — events whose cost/odds change per interaction are written as single fixed values: scrap-ooze (escalating HP + rising odds → flat 3 HP/25%), knowing-skull (escalating ask cost + reward amounts omitted), cursed-tome (per-page escalation unverified), wheel-of-change (6 weighted segments collapsed to a 5-item "either/or"). Downstream heuristics then compute EV/budgets on the wrong model (scrap-ooze "12 HP" budget, joust-style EV reasoning).
- NEW SYSTEMIC PATTERN: "reward omitted, only cost stated" — bonfire-spirits (rarity reward table missing), knowing-skull (ask rewards missing), world-of-goop (Leave gold-loss missing). Ontology captures the price but not what you get, leaving the heuristic to assert value with no atomic basis.
- FORMAT drift: augmenter alone breaks the shared ontology template.
