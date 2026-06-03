# Potions Audit — ontology/sts1/potions + heuristics/sts1/potions

COVERAGE: read 26 ontology + 26 heuristic files.
Ontology: attack-potion, blessing-of-the-forge, blood-potion, cultist-potion, distilled-chaos, duplication-potion, elixir, energy-potion, entropic-brew, essence-of-steel, explosive-potion, fairy-in-a-bottle, fear-potion, fire-potion, flex-potion, fruit-juice, gamblers-brew, liquid-memories, power-potion, regen-potion, skill-potion, smoke-bomb, snecko-oil, speed-potion, strength-potion, weak-potion.
Heuristics: same 26 stems.

Wikilink targets ALL verified to exist under ontology/sts1/ (cards/, buffs/, debuffs/, types/, relics/, enemies/, bosses/, encounters/, acts/). No broken links found. Note: wiki resolver (site/build.py resolve_wiki_link) always points to the ontology layer and does NOT validate existence, so "broken" = referenced ontology file missing; none are.

## Defects

[HIGH][VERIFY] ontology/sts1/potions/blessing-of-the-forge.md — FACT-ERROR: "Effect: Upgrade a random unupgraded card in your deck. Can be used outside of combat." Real StS Blessing of the Forge upgrades ALL cards currently in your HAND for the rest of the COMBAT only (not random, not deck-wide, not permanent, cannot be used out of combat). Wrong on every axis. FIX: "Upgrade all cards in your hand for the rest of combat." Remove "outside of combat".
[HIGH][VERIFY] heuristics/sts1/potions/blessing-of-the-forge.md — CONTRADICTION/NO-EVIDENCE (mirrors ontology error): "Use before a fight, not during... At rest sites, using this potion gives a free upgrade without spending the rest site action -- use it in addition to the normal Smith action for two upgrades." This is false if the potion is combat-only hand-upgrade; the entire rest-site "free permanent upgrade" framing is wrong. FIX: rewrite once ontology effect corrected — use it in a combat where many hand cards are unupgraded; it does NOT grant permanent/rest-site upgrades.
[HIGH][VERIFY] ontology/sts1/potions/distilled-chaos.md — FACT-ERROR: "Play the top card of your draw pile for free" (singular). Real StS plays the top 3 cards of the draw pile (Sacred Bark: 6). FIX: "Play the top 3 cards of your draw pile (Sacred Bark: 6)."
[MED][VERIFY] heuristics/sts1/potions/distilled-chaos.md — mirrors the singular-card error: "The free play is incredible value", "The card played is random (top of draw pile)". Reasoning treats it as ONE card, understating value and mis-describing mechanic. FIX: update to 3 cards played top-down; randomness = you can't choose which 3 / their order.

[MED] heuristics/sts1/potions/elixir.md — TOPIC-MISPLACED (harness/interface advice): entire "## Multi-Select Index Shifting (CRITICAL)" section about HAND_SELECT screen, index shifting, re-reading hand state is interface-harness guidance, not StS strategy. Belongs in heuristics/sts1/development/interface/sts1.md (which currently has no HAND_SELECT coverage). FIX: move the index-shifting block to the interface doc; keep only "exhaust status/garbage cards, thin deck mid-combat" here.
[MED] ontology/sts1/potions/fairy-in-a-bottle.md — FACT-INCOMPLETE/HEDGE: "heal to approximately 30% Max HP" — it is exactly 30% (Sacred Bark: 60%). Drop "approximately"; add Sacred Bark value. FIX: "heal to 30% Max HP (Sacred Bark: 60%)."
[MED] heuristics/sts1/potions/strength-potion.md — TOPIC-MISPLACED + UNCONDITIONAL: "In any fight approaching lethal, use ALL offensive potions before the window closes" and "An unused Strength Potion on a death screen means 10-20 damage was left on the table" — generic lethal-turn/potion-dumping advice belongs in combat.md / hp-management.md, not this card. FIX: move generic lethal-turn rule to combat.md; keep Strength-specific Turn-1-scaling + Giant Head Metallicize-8 breakpoint here.
[MED] heuristics/sts1/potions/explosive-potion.md — TOPIC-MISPLACED: "Do not hoard for a future fight if the current fight is lethal. An unused Explosive Potion on a death screen is a strategic failure." Generic lethal-turn maxim duplicated across potions; belongs in combat.md. FIX: keep multi-enemy + bypasses-block facts-applied; drop generic death-screen line.
[MED] heuristics/sts1/potions/smoke-bomb.md — TOPIC-MISPLACED: "An unused Smoke Bomb on a death screen is a strategic failure" + "Do not save it for 'a worse situation'" is the same generic maxim. Smoke-bomb-specific content (carry into Act 2, Gremlin Gang turn-1 22+ dmg) is good and stays. FIX: drop/relocate the generic death-screen line to combat.md.
[MED][VERIFY] ontology/sts1/potions/flex-potion.md — FACT-ERROR?: "Gain 2 temporary Strength". Flex Potion potency may be higher than 2 (the Flex card grants 2/4; the potion is commonly 5 temporary Strength). Verify exact potency. FIX: confirm value; if 5, correct to "Gain 5 temporary Strength (Sacred Bark: 10), lost at end of turn" and update heuristic "+2 damage".

[LOW] ontology/sts1/potions/blood-potion.md — FACT-INCOMPLETE: missing Sacred Bark note (heals 40% with Sacred Bark). FIX: append "(Sacred Bark: 40%)".
[LOW] ontology/sts1/potions/liquid-memories.md — FACT-INCOMPLETE: Sacred Bark returns 2 cards. FIX: note Sacred Bark = choose 2 cards.
[LOW] ontology/sts1/potions/snecko-oil.md — FACT-INCOMPLETE: Sacred Bark draws 10. FIX: append Sacred Bark = draw 10.
[LOW] ontology/sts1/potions/fruit-juice.md — FACT-INCOMPLETE: Sacred Bark grants +10 Max HP. FIX: append "(Sacred Bark: +10)".
[LOW] ontology/sts1/potions/fire-potion.md — FACT-INCOMPLETE: Sacred Bark 40 damage. FIX: append Sacred Bark value.
[LOW] ontology/sts1/potions/explosive-potion.md — FACT-INCOMPLETE: Sacred Bark 20 dmg all. FIX: append Sacred Bark value.
[LOW] ontology/sts1/potions/weak-potion.md — FACT-INCOMPLETE: Sacred Bark 6 Weak. FIX: append Sacred Bark value.
[LOW] ontology/sts1/potions/fear-potion.md — FACT-INCOMPLETE: Sacred Bark 6 Vulnerable. FIX: append Sacred Bark value.
[LOW] ontology/sts1/potions/strength-potion.md — FACT-INCOMPLETE: Sacred Bark 4 Strength. FIX: append Sacred Bark value.
[LOW] ontology/sts1/potions/essence-of-steel.md — FACT-INCOMPLETE: Sacred Bark 8 Plated Armor. FIX: append Sacred Bark value.
[LOW] ontology/sts1/potions/regen-potion.md — FACT-INCOMPLETE: Sacred Bark 10 Regeneration. FIX: append Sacred Bark value.
[LOW] ontology/sts1/potions/speed-potion.md — FACT-INCOMPLETE: Sacred Bark 10 Dexterity. FIX: append Sacred Bark value.
[LOW] ontology/sts1/potions/duplication-potion.md — FACT-INCOMPLETE: Sacred Bark duplicates next 2 cards. FIX: note Sacred Bark = next 2 cards.
[LOW] ontology/sts1/potions/flex-potion.md — FACT-INCOMPLETE: Sacred Bark doubles Strength. FIX: add once base potency confirmed.
[LOW] heuristics/sts1/potions/duplication-potion.md — FACT-ERROR (minor): "Iron Wave = double block + double damage (14/14 total)". Iron Wave base is 5/5 (→10/10 doubled); 14/14 only holds for Iron Wave+ (7/7). FIX: say "Iron Wave 5/5 → 10/10 (upgraded 7/7 → 14/14)".
[LOW] heuristics/sts1/potions/strength-potion.md — REDUNDANT: "Potions do not count as card plays (no Slow interaction)" is a generic ontology/interface fact, not Strength-specific. FIX: move to types/Slow or combat.md.
[LOW] heuristics/sts1/potions/snecko-oil.md — NO-EVIDENCE granularity: "Confirmed death: Run 185..." good as evidence but the run-log detail is borderline combat.md material; acceptable here. No change required (noted only).

## CLEAN
Ontology (effect/numbers correct, atomic, no contamination): attack-potion, cultist-potion, energy-potion, entropic-brew, gamblers-brew, power-potion, skill-potion, smoke-bomb, snecko-oil (effect line). (All "clean" ontology still carry the systemic missing-Sacred-Bark LOW noted above where applicable; listed clean = no error beyond that.)
Heuristics (actionable, concrete numbers/timing, not vacuous): blood-potion, cultist-potion, distilled-chaos (aside from card-count), duplication-potion, energy-potion, fairy-in-a-bottle, fear-potion, fire-potion, flex-potion, gamblers-brew, liquid-memories, power-potion, regen-potion, skill-potion, speed-potion, weak-potion, snecko-oil, essence-of-steel, attack-potion. Short heuristics (regen, weak, fruit-juice, blood, essence, flex) all carry a concrete number/comparison → GOOD, not stubs.

## PATTERNS
- NEW SYSTEMIC — missing-Sacred-Bark-fact: NO potion ontology file records the Sacred Bark doubling, even though potency-doubling is an atomic fact (and the task flags it as in-scope). This is uniform across all 26 ontology files. Recommend a standard "(Sacred Bark: <doubled>)" suffix convention.
- NEW SYSTEMIC — generic-lethal-turn-maxim-duplicated-in-potion-heuristics: the line "An unused X Potion on a death screen is a strategic failure" / "use ALL offensive potions before the window closes" recurs in strength-potion, explosive-potion, smoke-bomb. This generic combat advice belongs once in combat.md / hp-management.md, not per-potion (combat.md already hosts "Confirmed fatal Run 193" style lessons).
- KNOWN — agent-harness-advice-in-heuristics: Elixir's HAND_SELECT index-shifting block is interface guidance misfiled in a potion heuristic; belongs in development/interface/sts1.md.
- KNOWN — errors-mirrored-in-both-layers: Blessing of the Forge (random/permanent/out-of-combat) and Distilled Chaos (single card) factual errors propagate from ontology into the companion heuristic's reasoning.
- category-mismatch broken links: NONE found in potions (all targets resolve; Giant Head correctly in enemies/, the Act bosses correctly in bosses/).
- derived-examples-in-ontology: NONE — potion ontology files are clean single effect lines; all worked examples correctly live in heuristics.
