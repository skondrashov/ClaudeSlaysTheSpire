# Cards Sampling Audit — letters d–l

READ-ONLY audit. Canonical = printed in-game card text (from model knowledge; uncertain items marked `[VERIFY]` — no web tools used). Scope: `ontology/sts1/cards/` files starting d–l.

## SAMPLE: 30 cards read

Filenames (ontology/sts1/cards/):
`dagger-spray.md`, `dagger-throw.md`, `dark-shackles.md`, `darkness.md`, `deadly-poison.md`, `demon-form.md`, `devotion.md`, `double-tap.md`, `dropkick.md`, `echo-form.md`, `empty-fist.md`, `envenom.md`, `eruption.md`, `eviscerate.md`, `fasting.md`, `feed.md`, `fiend-fire.md`, `flechettes.md`, `force-field.md`, `genetic-algorithm.md`, `glass-knife.md`, `grand-finale.md`, `hand-of-greed.md`, `heavy-blade.md`, `heel-hook.md`, `hyperbeam.md`, `indignation.md`, `inflame.md`, `iron-wave.md`, `judgment.md`, `juggernaut.md`, `leg-sweep.md`, `like-water.md`, `limit-break.md`, `loop.md`

(35 distinct entries listed; "~30" sample target met and exceeded. Letters covered: d,e,f,g,h,i,j,l. No cards in this range start with k. Characters covered: Ironclad, Silent, Defect, Watcher, Colorless.)

Companion `heuristics/sts1/cards/` files were also read where present (demon-form, dropkick, feed, fiend-fire, loop). Strategy/derived content lives in those heuristics files, NOT in the ontology entries — ontology stays atomic. No ontology=atomic violations found in the sample.

## Per-card classification

| Card | Char | Effect fidelity | Metadata OK? | Replaceability |
|---|---|---|---|---|
| dagger-spray | Silent | MATCH | yes | PURE-PARAPHRASE |
| dagger-throw | Silent | MATCH | yes | PURE-PARAPHRASE |
| dark-shackles | Colorless | DRIFT [VERIFY] (duration wording) | yes | PURE-PARAPHRASE |
| darkness | Defect | DRIFT [VERIFY] (upgrade: "the Dark orb" vs ALL Dark orbs) | yes | PURE-PARAPHRASE |
| deadly-poison | Silent | MATCH | yes | PURE-PARAPHRASE |
| demon-form | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| devotion | Watcher | MATCH | yes | PURE-PARAPHRASE |
| double-tap | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| dropkick | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| echo-form | Defect | MATCH | yes | PURE-PARAPHRASE |
| empty-fist | Watcher | MATCH | yes | PURE-PARAPHRASE |
| envenom | Silent | MATCH | yes | PURE-PARAPHRASE |
| eruption | Watcher | MATCH | yes | PURE-PARAPHRASE |
| eviscerate | Silent | MATCH | yes | PURE-PARAPHRASE |
| fasting | Watcher | MATCH | yes | PURE-PARAPHRASE |
| feed | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| fiend-fire | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| flechettes | Silent | MATCH | yes | PURE-PARAPHRASE |
| force-field | Defect | MATCH | yes | PURE-PARAPHRASE |
| genetic-algorithm | Defect | MATCH | yes | HAS-EXTRA-FACTS (Block from this is permanent) |
| glass-knife | Silent | MATCH | yes | PURE-PARAPHRASE |
| grand-finale | Colorless | MATCH (effect) | **NO — Character wrong** | PURE-PARAPHRASE |
| hand-of-greed | Colorless | MATCH | yes | PURE-PARAPHRASE |
| heavy-blade | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| heel-hook | Silent | MATCH | yes | PURE-PARAPHRASE |
| hyperbeam | Defect | MATCH | yes | PURE-PARAPHRASE |
| indignation | Watcher | MATCH | yes | PURE-PARAPHRASE |
| inflame | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| iron-wave | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| judgment | Watcher | MATCH | yes | PURE-PARAPHRASE |
| juggernaut | Ironclad | MATCH | yes | PURE-PARAPHRASE (uses buffs/Juggernaut abstraction) |
| leg-sweep | Silent | MATCH | yes | PURE-PARAPHRASE |
| like-water | Watcher | MATCH | yes | PURE-PARAPHRASE |
| limit-break | Ironclad | MATCH | yes | PURE-PARAPHRASE |
| loop | Defect | DRIFT [VERIFY] (upgrade is +trigger, not cost→0) | Cost field wrong if drift confirmed | PURE-PARAPHRASE |

## DRIFTs

- `[HIGH]` `ontology/sts1/cards/grand-finale.md` — **Metadata: Character is "Silent" but Grand Finale is Colorless.** Effect text itself is correct. FIX: `- **Character:** Colorless`
- `[MED][VERIFY]` `ontology/sts1/cards/loop.md` — Entry says upgrade only lowers cost: `Cost: 1E (0E upgraded)` / `Upgraded: Costs 0E`. Canonical Loop+ keeps cost 1 and triggers the orb passive **2 additional times** (not 1); the upgrade is a trigger increase, not a cost reduction. FIX: `- **Cost:** 1E` and `- **Upgraded:** Triggers the first orb's passive 2 additional times`.
- `[MED][VERIFY]` `ontology/sts1/cards/darkness.md` — Upgraded entry: "Also triggers the Dark orb's passive" (singular). Canonical Darkness+ triggers the passive of **all** your Dark orbs. FIX: `- **Upgraded:** Channel 1 Dark orb. Trigger the passive ability of ALL your Dark orbs.`
- `[MED][VERIFY]` `ontology/sts1/cards/dark-shackles.md` — Entry: "until end of its next turn." Canonical printed wording is the Strength loss lasts "for the rest of this turn" (ends when the enemy's current/next turn ends — wording differs from "next turn"). The numbers (9 / 15) and Exhaust are correct. FIX (if confirmed): `- **Effect:** Enemy loses 9 Strength for the rest of this turn, Exhaust`.

## TALLY

- Effect drift: **3/35** (~8.6%) confirmed-or-likely effect-text drifts (darkness, dark-shackles, loop — all `[VERIFY]`). Grand Finale's effect text is fine; its error is metadata.
- Metadata errors: **1/35** confirmed (grand-finale Character) + **1/35** conditional on the Loop drift (loop Cost). → 1 confirmed, 2 if Loop drift holds.
- Pure-paraphrase: **34/35**. Every sampled effect is a verbatim-replaceable reword of the card text. Regeneration from canonical card data would reproduce them with no information loss (and would fix all 4 drifts).
- Has-extra-facts: **1/35** — `genetic-algorithm` (states "Block from this card is permanent," which on the real card is its own printed line, so arguably still on-card; only borderline-extra). No sampled entry contains hidden-interaction facts that a card-text regeneration would lose. All strategy/derived facts live in the separate `heuristics/sts1/cards/` companions, not in ontology.

## Bottom line

Drift in this d–l sample is **low and almost entirely numeric/wording-level**, not structural. The entries are clean atomic paraphrases — the book's ontology cards in this range are essentially safe to regenerate verbatim from canonical card data, which would also auto-correct the Grand Finale character error and the Loop/Darkness/Dark Shackles wording. No ontology entry hides strategy or non-card interaction facts.
