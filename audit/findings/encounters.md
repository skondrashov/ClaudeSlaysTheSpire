# Audit: ontology/sts1/encounters/

COVERAGE: read 42 ontology files.
2-louse, 3-louse, 3-byrds, 2-thieves, chosen-cultist, 2-orb-walkers, 3-shapes, 2-fungi-beasts, 3-sentries, 3-cultists, gremlin-leader, giant-head, centurion-mystic, darklings, jaw-worm-horde, gremlin-gang, chosen-solo, blue-slaver, gremlin-nob, exordium-wildlife, book-of-stabbing, exordium-thugs, lagavulin, jaw-worm-solo, looter, large-slime, lots-of-slimes, maw, nemesis, orb-walker, red-slaver, reptomancer, shelled-parasite-fungi-beast, shelled-parasite-solo, slavers, small-slimes, snake-plant, sphere-2-shapes, spire-growth, writhing-mass, snecko, transient.

Also cross-referenced ~40 ontology/sts1/enemies/ files + site/build.py wiki-link resolver.

## Link resolver behavior (site/build.py:20-29)
`[[enemies/Name]]` -> slug = Name.lower(), spaces->`-`, strip apostrophes/periods -> `ontology-sts1-enemies-<slug>.html`. A link resolves IFF a file `enemies/<slug>.md` exists. Display name is Title Case in source but file is kebab-case; resolver lowercases, so Title-Case links are fine as long as the kebab file exists.

## Defects

[HIGH] ontology/sts1/encounters/2-louse.md — BROKEN-LINK: `2x [[enemies/Louse]] (each randomly [[enemies/Red Louse]] or [[enemies/Green Louse]])`. `[[enemies/Louse]]` resolves to `enemies/louse.md`, which does NOT exist (only red-louse.md / green-louse.md). Dead link. FIX: drop the generic `[[enemies/Louse]]` link (keep plain text "Louse") or rephrase as "2x Louse, each randomly [[enemies/Red Louse]] or [[enemies/Green Louse]]" with the parenthetical links carrying the resolution.

[HIGH] ontology/sts1/encounters/3-louse.md — BROKEN-LINK: same dead `[[enemies/Louse]]` link (no louse.md). FIX: same as 2-louse.

[HIGH] ontology/sts1/encounters/exordium-wildlife.md — BROKEN-LINK: `e.g. [[enemies/Jaw Worm]] + [[enemies/Louse]], [[enemies/Fungi Beast]] + [[enemies/Louse]]`. Both `[[enemies/Louse]]` instances are dead (no louse.md). FIX: replace `[[enemies/Louse]]` with plain "Louse" or with red/green louse links.

[HIGH][VERIFY] ontology/sts1/encounters/3-shapes.md — FACT-ERROR / CONTRADICTION: declares `**Act:** 3` for `3x random from Exploder, Repulsor, Spiker`. sphere-2-shapes.md uses the SAME Shape enemies but declares `**Act:** 2`. Internally contradictory. Real StS: Shapes (Exploder/Repulsor/Spiker) and Spheric Guardian are Act 2 (The City) enemies, so Act 3 here is almost certainly wrong. (Note: the Exploder/Repulsor/Spiker enemy files also say Act 3 — out of scope but corroborates a systemic Act-2-vs-3 error for Shapes.) FIX: change 3-shapes.md to Act 2 to match sphere-2-shapes.md and StS; verify Shapes pool act.

[MED][VERIFY] ontology/sts1/encounters/exordium-thugs.md — FACT-ERROR: example combo `[[enemies/Looter]] + [[enemies/Mugger]]` in an Act 1 ("Exordium") encounter. Mugger is an Act 2 enemy (enemies/mugger.md says Act 2; Looter is its Act 1 counterpart). A Looter+Mugger pairing cannot occur in Act 1. The other example (Blue Slaver + Red Slaver) is valid. FIX: replace the Mugger example with an Act-1 enemy (e.g. Looter + Red/Blue Slaver), or drop it.

[MED][VERIFY] ontology/sts1/encounters/reptomancer.md — FACT-ERROR?: composition `1x Reptomancer, 2x [[enemies/Dagger]]` implies 2 Daggers present at combat start. In real StS the Reptomancer fight starts with the Reptomancer alone and it summons 2 Daggers on turn 1 (its opener is always Summon Dagger). enemies/reptomancer.md is itself contradictory ("Fight starts with Reptomancer + 2 Daggers" vs "Always opens with Summon Dagger"). FIX: verify; if daggers are summoned turn 1, list composition as "1x Reptomancer (summons 2 Daggers turn 1)" rather than starting with 2 Daggers.

[MED][VERIFY] ontology/sts1/encounters/lots-of-slimes.md — REDUNDANT / HEDGE-CONTRADICTION: facts read `3-5 small slimes, mix of Spike Slime S and Acid Slime S`, identical to small-slimes.md (`3-5 slimes total, mix of Spike Slime S and Acid Slime S`). The Notes section asserts "Distinct from 'Small Slimes' encounter in possible slime count distribution" but the stated 3-5 ranges are identical, so the file does not actually encode the claimed distinction (and the real-StS distinction between these two Act-1 small-slime encounters is unverified here). FIX: either give the two encounters distinct, sourced counts, or merge them; remove the unsupported "distinct distribution" note.

[LOW] ontology/sts1/encounters/lots-of-slimes.md — CONTAMINATION (minor): the "## Notes" prose comparing this encounter to another ("Distinct from ... encounter") is meta/derived commentary rather than an atomic fact. FIX: move comparison out of the atomic-fact ontology file (or delete once counts are corrected).

[LOW] ontology/sts1/encounters/ (systemic) — FACT-INCOMPLETE: no encounter file states **combined HP**, although the ontology layer rule lists combined HP as an allowed atomic fact. Per-enemy HP lives in enemies/ files, so this is recoverable, but the encounter files give act+type+roster only. FIX (optional): add a "Combined HP" line per encounter, or accept as deliberate (HP delegated to enemy files).

[LOW] ontology/sts1/encounters/ (systemic) — FACT-INCOMPLETE: no Ascension notes. Several encounters change with Ascension in StS (e.g. higher-Ascension hallway fights can add enemies / use buffed "horde" HP). None recorded at encounter level. FIX (optional): note A-level roster/count changes where they exist (e.g. jaw-worm-horde HP, sentry/elite scaling).

[LOW][VERIFY] ontology/sts1/encounters/jaw-worm-horde.md — FACT-INCOMPLETE: `3x [[enemies/Jaw Worm]]`, Act 3. enemies/jaw-worm.md lists Jaw Worm as Act 1 only with HP 40-44; the Act 3 Horde variant uses higher HP and starts buffed (Bellow precast) in StS. Encounter doesn't note the Act-3 stat/behavior difference. FIX: note that horde Jaw Worms are the Act-3 variant (buffed HP / pre-applied Strength) or ensure the enemy file covers the Act-3 variant.

## CLEAN
3-byrds, 2-thieves, chosen-cultist, 2-orb-walkers, 2-fungi-beasts, 3-sentries, 3-cultists, gremlin-leader, giant-head, centurion-mystic, darklings, gremlin-gang, chosen-solo, blue-slaver, gremlin-nob, book-of-stabbing, lagavulin, jaw-worm-solo, looter, large-slime, maw, nemesis, orb-walker, red-slaver, shelled-parasite-fungi-beast, shelled-parasite-solo, slavers, small-slimes, snake-plant, sphere-2-shapes, spire-growth, writhing-mass, snecko, transient.

(All CLEAN files: act+type+roster verified consistent with their linked enemy ontology files; all wiki-links resolve to existing kebab-case enemy files.)

## PATTERNS

RECURRING (already-known systemic, new instances):
- Category/target-mismatch broken links: `[[enemies/Louse]]` used in 3 encounter files (2-louse, 3-louse, exordium-wildlife) with no `enemies/louse.md` target. A "Louse" is only ever Red or Green; there is no generic Louse ontology node, so every generic-Louse link is dead. This is the dominant defect in this folder.

- Act-pool errors for The City enemies: Shapes pool is split across Act 2 (sphere-2-shapes) and Act 3 (3-shapes); the underlying Exploder/Repulsor/Spiker enemy files also carry Act 3. Suggests a systemic Act-2-vs-Act-3 misfiling for City "shape" enemies that spans both encounter and enemy layers.

NEW systemic patterns:
- Encounters omit the "combined HP" atomic fact uniformly (all 42). If the schema intends combined HP at the encounter level, it is 100% missing; if HP is intentionally delegated to enemy files, the layer rule's mention of combined HP is misleading.
- Encounters omit Ascension notes uniformly (all 42), even where the roster/stats demonstrably change (jaw-worm-horde, elite scaling).
- POSITIVE / no-defect note: the usual "strategy/derivation living in ontology" contamination pattern is essentially ABSENT in the encounter folder — files are clean roster+act+type with no "focus X first" / "dangerous because" framing. The one exception is the lots-of-slimes Notes line (a meta-comparison, not strategy). So encounters are the cleanest-of-layer for contamination but the worst for broken Louse links.
