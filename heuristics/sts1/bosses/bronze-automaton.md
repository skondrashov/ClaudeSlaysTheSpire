# Bronze Automaton

**Core rule:** Enter at 70%+ HP. Use ONLY non-exhausting debuffs ([[cards/Bash]], [[cards/Thunderclap]]) for [[buffs/Artifact]] stripping. SAVE exhausting [[debuffs/Weak]] sources ([[cards/Intimidate]], [[cards/Shockwave]]) for Hyper Beam survival. Basic Defends cannot survive Hyper Beam.

## Preparation Checklist

1. Enter at 70%+ HP
2. Artifact strippers (non-exhausting): Thunderclap, Bash+. Need 3+ applications.
3. Weak source saved for Hyper Beam: Intimidate, Shockwave+, or [[potions/Weak Potion]]
4. Block scaling: [[cards/Shrug It Off]], [[cards/Flame Barrier]], [[cards/Metallicize]], [[cards/Impervious]], [[cards/Ghostly Armor]] (basic Defends are NOT enough)
5. Burst damage for post-Hyper Beam stun window
6. Redundant key cards (Stasis steals cards -- single copies are fragile)

## Fight Phases

1. **Turns 1-3 (Artifact Strip):** Strip 3 Artifact with Bash+ and Thunderclap. Do NOT use Intimidate or Shockwave.
2. **Turn 3-4 (Debuff Window):** Once Artifact is 0, apply Shockwave+ (Weak 3 + Vuln 3).
3. **Turns 4-7 (Burst Phase):** With Vuln active, unload burst damage. Goal: 150+ damage in 3-4 turns.
4. **Turn 6-8 (Hyper Beam #1):** MUST have 30+ block AND Weak active. Impervious+ covers cleanly.
5. **Stun Window #1:** Free damage turn. Maximize output.
6. **Turn 12-13 (Hyper Beam #2):** +12 Str means 57+ damage. Need second massive block source or Weak + multiple block cards.

## What NOT to Do

- Use Intimidate or Shockwave for Artifact stripping (they exhaust -- save for Hyper Beam)
- Play Impervious on non-Hyper-Beam turns when Hyper Beam is approaching
- Enter below 60% HP
- Enter without block scaling beyond basic Defends
- Rely on a single irreplaceable card (Stasis will steal something)
- Take [[relics/Runic Dome]] (cannot predict Hyper Beam timing without intent visibility)
- Plan to recover exhausted cards with [[potions/Liquid Memories]] (retrieves from DISCARD only, not EXHAUST)

## Dark Shackles Interaction

Reduces Hyper Beam by ~9 damage but NOT sufficient alone. Still need 30+ block on top. [[cards/Dark Shackles]] + Metallicize + Ghostly Armor + 2 Defends = ~31 block vs reduced Hyper Beam = survivable at 70%+ HP.

## Character Matchups

**[[characters/Watcher]]:** The stance dance engine has unique advantages and dangers against Bronze Automaton.

**Advantages:**
- Wrath burst damage can kill Automaton quickly (down to 36/300 HP by Turn 6 is achievable).
- Apparitions provide Intangible, which is the cleanest Hyper Beam survival tool (reduces 45+ damage to 1).
- Battle Hymn provides sustained Smite generation for long fights.
- Calm energy bonus (+2E on exit) funds large burst turns.

**Dangers:**
- **Hyper Beam in Wrath = 90+ damage (45 base x2).** If caught in Wrath with no block and no Intangible, Hyper Beam is instantly lethal at any HP total. NEVER end a turn in Wrath when Hyper Beam is possible unless Intangible is active.
- **Reduced Max HP + Hyper Beam.** If the Watcher took Council of Ghosts (-Max HP for Apparitions), absolute HP is low (often 36-40). Hyper Beam at 45 base is lethal from full HP without block or Intangible. The 70% HP entry threshold means nothing when Max HP is 36 — calculate absolute survival instead.
- **Artifact does NOT affect stance changes.** Artifact blocks debuffs, not stance mechanics. Wrath/Calm cycling works normally.
- **NEVER use Distilled Chaos in this fight.** Meditate ends the turn, Conclude ends the turn, Blasphemy sets HP to 1. Any of these randomly played against Hyper Beam leaves you with 0 block against 90+ doubled damage — you die. See watcher.md for full explanation.

**Watcher strategy:**
1. **Turns 1-2 (Setup):** Play Powers (Rushdown, Mental Fortress, Battle Hymn). Use Apparitions for Intangible on attack turns. Enter Calm at end of turn for energy next turn.
2. **Turns 3-5 (Burst):** Calm -> Wrath burst with doubled attacks. Use Apparitions to cover Hyper Beam turns. Pen Nib (if available) for doubled finisher.
3. **Hyper Beam turn:** Must have either (a) Intangible from Apparition, (b) sufficient block in Calm (NOT Wrath), or (c) confirmed kill before Hyper Beam resolves. Option (a) is by far the safest.
4. **Kill math:** Verify all damage numbers are doubled in Wrath. Tantrum+ = 2x10 = 20 in Wrath (not 2x5 = 10). See combat.md rule 8.

**A representative near-win:** Watcher can get Automaton to 36/300 HP by Turn 6 with the kill in hand (Smite + Strike = 36 damage in Wrath = exact lethal), then lose to Distilled Chaos randomly playing Meditate+ (ends turn, 0 block) against 102 Hyper Beam. An arithmetic error on Tantrum+ damage triggers the unnecessary potion use.

## Key Lessons from Deaths

- Insufficient block scaling (basic Defends = 20 max vs 38+ Hyper Beam) is the central danger — basic block can't cover Hyper Beam, so it lands for lethal
- Wasting Intimidate on Artifact stripping leaves no Weak for Hyper Beam, which then lands unreduced for lethal
- Long fights (12+ turns) face a second Hyper Beam at 57+ damage -- need kill speed or second Impervious
- Distilled Chaos with turn-ending cards in draw pile against Hyper Beam ends your turn with 0 block and gets you killed
- Wrath damage miscalculation leads to unnecessary risk-taking when the kill is already achievable
