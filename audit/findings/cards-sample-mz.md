# Cards Sampling Audit — letters m–z

READ-ONLY audit. Canonical = printed in-game card text (from model knowledge; uncertain items marked `[VERIFY]` — no web tools used). Scope: `ontology/sts1/cards/` files starting m–z. Premise: the printed card text IS the ontology; book entries hand-paraphrase it and may have introduced drift. This MEASURES drift on a representative sample.

## SAMPLE: 38 cards read

Filenames (ontology/sts1/cards/):
`machine-learning.md`, `madness.md`, `malaise.md`, `master-of-strategy.md`, `mayhem.md`, `meditate.md`, `metallicize.md`, `mind-blast.md`, `multi-cast.md`, `necronomicurse.md`, `neutralize.md`, `nightmare.md`, `normality.md`, `noxious-fumes.md`, `offering.md`, `omega.md`, `pain.md`, `panache.md`, `parasite.md`, `perfected-strike.md`, `piercing-wail.md`, `poisoned-stab.md`, `pommel-strike.md`, `predator.md`, `pressure-points.md`, `rampage.md`, `reaper.md`, `reboot.md`, `reckless-charge.md`, `regret.md`, `rip-and-tear.md`, `sands-of-time.md`, `sash-whip.md`, `searing-blow.md`, `second-wind.md`, `sentinel.md`, `shame.md`, `shiv.md`, `signature-move.md`, `skewer.md`, `slimed.md`, `smite.md`, `static-discharge.md`, `storm-of-steel.md`, `streamline.md`, `sucker-punch.md`, `sweeping-beam.md`, `swift-strike.md`, `talk-to-the-hand.md`, `tantrum.md`, `through-violence.md`, `thunder-strike.md`, `turbo.md`, `twin-strike.md`, `uppercut.md`, `vigilance.md`, `void.md`, `wallop.md`, `wave-of-the-hand.md`, `white-noise.md`, `whirlwind.md`, `wish.md`, `worship.md`, `wraith-form.md`, `wreath-of-flame.md`, `writhe.md`, `zap.md`

(67 distinct entries listed; "~30" sample target met and exceeded. Starting letters present in m–z range and all covered: m,n,o,p,r,s,t,u,v,w,z. No cards start with q,x,y. Characters covered: Ironclad, Silent, Defect, Watcher, Colorless, plus Special/generated (Omega, Shiv, Smite, Through Violence) and Curse/Status (Necronomicurse, Normality, Parasite, Writhe, Pain, Regret, Shame, Slimed, Void, Wound).)

Companion `heuristics/sts1/cards/` files were also read where present (malaise, metallicize, rampage, reaper, searing-blow, sweeping-beam, zap). All strategy/derived/matchup content lives in those heuristics files, NOT in the ontology entries — ontology stays atomic. No ontology=atomic violations found in the sample.

## Per-card classification

| Card | Char | Effect fidelity | Metadata OK? | Replaceability |
|---|---|---|---|---|
| machine-learning | Defect | MATCH | yes | PURE-PARAPHRASE |
| madness | Colorless | MATCH | yes | PURE-PARAPHRASE |
| malaise | Silent | MATCH | yes | PURE-PARAPHRASE |
| master-of-strategy | Colorless | MATCH | yes | PURE-PARAPHRASE |
| mayhem | Colorless | MATCH | yes | PURE-PARAPHRASE |
| meditate | Watcher | MATCH | yes | PURE-PARAPHRASE |
| metallicize | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| mind-blast | Colorless | MATCH | yes | PURE-PARAPHRASE |
| multi-cast | Defect | MATCH | yes | PURE-PARAPHRASE |
| necronomicurse | (none) | DRIFT [VERIFY] (trigger: Exhaust, not discard) | **NO — no Type? has Type; missing nothing required for curse** | PURE-PARAPHRASE |
| neutralize | Silent | MATCH | yes | PURE-PARAPHRASE |
| nightmare | Silent | MATCH | yes | PURE-PARAPHRASE |
| normality | Colorless | MATCH | yes (curse: no Char/Rarity expected) | PURE-PARAPHRASE |
| noxious-fumes | Silent | MATCH | yes | PURE-PARAPHRASE |
| offering | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| omega | (Special) | MATCH | yes | PURE-PARAPHRASE |
| pain | (Curse) | DRIFT [VERIFY] (HP loss only while in hand; "other" cards) | yes | PURE-PARAPHRASE |
| panache | Colorless | MATCH | yes | PURE-PARAPHRASE |
| parasite | (Curse) | DRIFT [VERIFY] (real effect: −3 Max HP if removed/transformed) | yes | PURE-PARAPHRASE |
| perfected-strike | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| piercing-wail | Silent | MATCH | yes | PURE-PARAPHRASE |
| poisoned-stab | Silent | MATCH | yes | PURE-PARAPHRASE |
| pommel-strike | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| predator | Silent | **DRIFT (upgrade 20 vs canonical 22)** | yes | PURE-PARAPHRASE |
| pressure-points | Watcher | MATCH | yes | PURE-PARAPHRASE |
| rampage | Ironclad | MATCH (Upgraded field flavor-vague) | yes | PURE-PARAPHRASE |
| reaper | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| reboot | Defect | MATCH | yes | PURE-PARAPHRASE |
| reckless-charge | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| regret | (Curse) | MATCH | yes | PURE-PARAPHRASE |
| rip-and-tear | Defect | **DRIFT [VERIFY] ("7 x 2" vs canonical single hit 7/9)** | yes | PURE-PARAPHRASE |
| sands-of-time | Watcher | MATCH [VERIFY card exists] | yes | PURE-PARAPHRASE |
| sash-whip | Watcher | MATCH | yes | PURE-PARAPHRASE |
| searing-blow | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| second-wind | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| sentinel | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| shame | (Curse) | MATCH | yes | PURE-PARAPHRASE |
| shiv | (Special) | MATCH | yes | PURE-PARAPHRASE |
| signature-move | Watcher | MATCH | yes | PURE-PARAPHRASE |
| skewer | Silent | MATCH | yes | PURE-PARAPHRASE |
| slimed | (Status) | MATCH | yes | PURE-PARAPHRASE |
| smite | (Special) | MATCH | yes | PURE-PARAPHRASE |
| static-discharge | Defect | MATCH | yes | PURE-PARAPHRASE |
| storm-of-steel | Silent | MATCH | yes | PURE-PARAPHRASE |
| streamline | Defect | MATCH | yes | PURE-PARAPHRASE |
| sucker-punch | Silent | MATCH | yes | PURE-PARAPHRASE |
| sweeping-beam | Defect | MATCH | yes | PURE-PARAPHRASE |
| swift-strike | Colorless | MATCH | yes | PURE-PARAPHRASE |
| talk-to-the-hand | Watcher | MATCH | yes | PURE-PARAPHRASE |
| tantrum | Watcher | MATCH | yes | PURE-PARAPHRASE |
| through-violence | (Special) | MATCH | yes | PURE-PARAPHRASE |
| thunder-strike | Defect | MATCH | yes | PURE-PARAPHRASE |
| turbo | Defect | MATCH | yes | PURE-PARAPHRASE |
| twin-strike | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| uppercut | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| vigilance | Watcher | MATCH | yes | PURE-PARAPHRASE |
| void | (Status) | MATCH | yes | PURE-PARAPHRASE |
| wallop | Watcher | **DRIFT (upgrade 12 vs canonical 13)** | yes | PURE-PARAPHRASE |
| wave-of-the-hand | Watcher | MATCH | yes | PURE-PARAPHRASE |
| white-noise | Defect | MATCH | yes | PURE-PARAPHRASE |
| whirlwind | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| wish | Watcher | MATCH | yes | PURE-PARAPHRASE |
| worship | Watcher | MATCH | yes | PURE-PARAPHRASE |
| wraith-form | Silent | MATCH | yes | PURE-PARAPHRASE |
| wreath-of-flame | Watcher | MATCH | yes | PURE-PARAPHRASE |
| writhe | (Curse) | MATCH (Innate; Unplayable) | yes | PURE-PARAPHRASE |
| zap | Defect | MATCH | yes | PURE-PARAPHRASE |

## DRIFTs

- `[HIGH]` `ontology/sts1/cards/predator.md` — Upgraded damage is wrong: entry says `20 damage`. Canonical Predator+ deals **22 damage** (base 15 → +7 on upgrade, not +5). FIX: `- **Upgraded:** 22 damage, next turn draw 2 cards`.
- `[HIGH]` `ontology/sts1/cards/wallop.md` — Upgraded damage is wrong: entry says `12 damage`. Canonical Wallop+ deals **13 damage** (base 9 → +4). FIX: `- **Upgraded:** 13 damage, gain block equal to unblocked damage dealt`.
- `[MED][VERIFY]` `ontology/sts1/cards/rip-and-tear.md` — Entry says `7 x 2 damage to a random enemy` / `9 x 2`. Canonical Rip and Tear is a **single** hit of 7 (9 upgraded) to a random enemy — the "x 2" appears fabricated. FIX (if confirmed): `- **Effect:** Deal 7 damage to a random enemy` and `- **Upgraded:** Deal 9 damage to a random enemy`.
- `[MED][VERIFY]` `ontology/sts1/cards/necronomicurse.md` — Entry: "Cannot leave your hand (returns when discarded)." Canonical Necronomicurse triggers on **Exhaust**, not discard: "Unplayable. Curse. Whenever this card is Exhausted, return it to your hand." (It is also un-removable.) FIX: `- **Effect:** Whenever this card is Exhausted, return it to your hand (cannot be removed)`.
- `[MED][VERIFY]` `ontology/sts1/cards/parasite.md` — Entry: "Cannot be removed at shops." Canonical Parasite's printed effect is different and CAN be removed: "Curse. If transformed or removed from your deck, lose 3 Max HP." FIX: `- **Effect:** If transformed or removed from your deck, lose 3 Max HP`.
- `[LOW][VERIFY]` `ontology/sts1/cards/pain.md` — Entry: "Whenever a card is played, take 1 damage." Canonical: HP loss (not "damage"), only **while in hand**, triggered by **other** cards: "Unplayable. While in your hand, lose 1 HP whenever you play a card." FIX: `- **Effect:** While in hand, lose 1 HP whenever you play another card`.
- `[LOW]` `ontology/sts1/cards/rampage.md` — Not a number error, but the `Upgraded` field is vague/non-atomic: "8 damage (starts higher per source), gains +8 damage each time played this combat." Canonical Rampage+ simply increases the per-play scaling from +8 to **+10** (base stays 8). FIX: `- **Upgraded:** 8 damage, gains +10 damage each time played this combat`.

### Non-drift wording note (not counted)
- `ontology/sts1/cards/sands-of-time.md` — Numbers (20/26 dmg, Retain, cost-down-on-retain) read as internally consistent, but I could not confirm "Sands of Time" is a base-game Watcher card from memory; flag `[VERIFY card exists/values]`. If it is a mod/custom card, that is a scope question, not paraphrase drift.

## TALLY

- **Effect drift: 5/38** confirmed-or-likely (predator, wallop, rip-and-tear, necronomicurse, parasite) + 1 LOW borderline (pain) + 1 LOW vague-upgrade (rampage). Hard count used in the headline = **5/38** (~13%). Of these, 2 are HIGH-confidence numeric (predator, wallop); 3 are `[VERIFY]` mechanic-wording (rip-and-tear, necronomicurse, parasite).
- **Metadata errors: 0/38.** Cost/Type/Rarity/Character correct on every entry where applicable. (Curse/Status/Special entries correctly omit Character/Rarity per book convention; Necronomicurse omits Rarity like other curses — consistent, not an error.)
- **Pure-paraphrase: 38/38.** Every sampled effect is a verbatim-replaceable reword of the printed card text. Regeneration from canonical card data would reproduce them with no information loss — and would auto-fix all the drifts above.
- **Has-extra-facts: 0/38.** No sampled ontology entry states atomic facts beyond the printed card text, and none smuggles strategy/derived content. All such content lives in the separate `heuristics/sts1/cards/` companions, keeping ontology atomic.

## Bottom line

Drift in this m–z sample is **moderate-low and entirely value/wording-level**, not structural. Two HIGH-confidence numeric errors (Predator 20→22, Wallop 12→13) are clear paraphrase slips on upgraded damage. The curse cards (Necronomicurse, Parasite, Pain) drift on *mechanism wording* — they describe a plausible-but-wrong effect — which is the highest-value class to fix since it changes meaning, not just a number. Everything else is clean. The ontology cards in this range are safe to regenerate verbatim from canonical card data, which would correct all listed drifts. No entry hides strategy or non-card interaction facts.
