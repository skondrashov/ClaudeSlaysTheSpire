# Bronze Automaton (Act 2, HP: 300)

PATTERN:
- **Turn 1**: Spawns 2 Orb minions (~50 HP each). Orbs use **Stasis** to steal a card from the player's hand, removing it from combat entirely.
- **Subsequent turns**: Cycles between attacks, Strength gain (+3 Str per cycle), and Hyper Beam (a massive single-hit attack). Orbs continue stealing cards via Stasis.
- **Hyper Beam**: Extremely high single-hit damage (observed 38-51 depending on accumulated Strength). Fires around turn 6. After firing, Automaton loses all block (vulnerability window). Without intent visibility (e.g. Runic Dome), this turn is impossible to predict and prepare for.
- **Strength scaling**: Gains +3 Strength per cycle. By turn 6-7, all attacks hit significantly harder than their base values. Hyper Beam at turn 6 with accumulated Strength can reach 51 damage. The fight becomes unwinnable if it goes too long.
- **Artifact 3**: Starts with 3 stacks of Artifact, which negate the first 3 debuff applications. Must strip all Artifact before Vulnerable, Weak, or Disarm take effect. Red Mask relic applies Weak at combat start, which strips 1 Artifact automatically (3->2) before the player's first turn.

KEY MECHANICS:
- **Stasis (Orbs)**: Each Orb steals one card from the player's hand and holds it. The stolen card is completely removed from combat -- it cannot be drawn, played, or retrieved until the Orb is killed. Stasis targets Power and Skill cards preferentially. Observed stolen: Demon Form (Power), Flame Barrier+ (Skill), Metallicize (Power). Losing key cards to Stasis can cripple the deck mid-fight. This is the Automaton's most disruptive mechanic. Killing the Orb returns the stolen card to the player's hand.
- **Artifact stripping**: Three debuff applications are needed before any debuff sticks. Thunderclap (1 Vulnerable = 1 Artifact stripped per enemy), Bash+ (applies Vulnerable = strips 1 Artifact), Disarm (applies -Str = strips 1 Artifact). Plan the first 2-3 turns around stripping Artifact before applying real debuffs.
- **Hyper Beam window**: After Hyper Beam fires, the Automaton is temporarily weakened. This is the burst window. Save high-damage plays (Bludgeon, Blood for Blood, Double Tap + big Attack) for this moment.

PREPARATION CHECKLIST:
1. **Enter at 70%+ HP** -- 300 HP boss with Strength scaling demands a large HP buffer. 75% HP entry is achievable and was first reached successfully.
2. **Artifact strippers (non-exhausting)** -- Thunderclap, Bash+. Use ONLY non-exhausting debuffs for Artifact stripping. Do NOT use Intimidate or Shockwave for stripping -- they exhaust and are needed for Hyper Beam.
3. **Weak source saved for Hyper Beam** -- Intimidate, Shockwave+, or Weak Potion. MUST be available when Hyper Beam fires (~Turn 6). Weak reduces Hyper Beam by 25% (51 -> 38). This is the survival margin. If the only Weak source is Intimidate, do NOT play it before the Hyper Beam turn.
4. **Block scaling** -- Shrug It Off, Flame Barrier, Metallicize, Impervious, Ghostly Armor. Hyper Beam at 51 damage demands 30+ block. Basic Defends are not enough even with Weak active.
5. **Burst damage** -- Bludgeon, Blood for Blood, Double Tap + Attacks, Rampage. The fight must end before Strength scaling (+3/cycle) outpaces your block capacity.
6. **Redundant key cards** -- Stasis steals cards. If your strategy depends on a single copy of Double Tap or Inflame, Stasis can destroy the plan. Multiple copies of key effects or alternative win conditions provide resilience.
7. **Intent visibility** -- Runic Dome removes enemy intent display, making Hyper Beam timing unpredictable. Without intent, block allocation becomes guesswork. Avoid Runic Dome if Bronze Automaton is a possible Act 2 boss.

STRATEGY:
- **Turns 1-2 (Artifact stripping)**: Apply 3 debuffs to strip all Artifact stacks. Use Bash+ and Thunderclap for Artifact stripping -- these are cheap and non-exhausting. **Do NOT use Intimidate or Shockwave for Artifact stripping.** These exhaust after use and are needed for Hyper Beam survival. Save them for when Artifact is gone and Weak/Vuln will actually stick. Red Mask (if equipped) strips 1 Artifact at combat start, reducing the stripping requirement to 2.
- **SAVE Weak sources for Hyper Beam**: Intimidate, Shockwave+, and Weak Potion must be held until the Hyper Beam turn. Weak reduces Hyper Beam by 25% (e.g., 51 -> 38). This 13-damage reduction is often the difference between survival and death. Using Intimidate on Turn 1 to strip Artifact wastes the only Weak source -- when Hyper Beam fires on Turn 6, no Weak is available and the player dies.
- **Kill Orbs early if possible**: Each surviving Orb steals one card per turn via Stasis. Removing Orbs stops the card drain. However, Orbs have ~50 HP -- committing too much damage to Orbs delays killing the 300 HP Automaton. Evaluate based on what cards have already been stolen.
- **Race the Strength scaling**: +3 Str/cycle means every turn the fight extends, incoming damage grows. By turn 6, attacks deal 15-20+ more than their base. Prioritize damage output over conservative blocking once Artifact is stripped and Vulnerable is applied.
- **Post-Hyper Beam burst**: After Hyper Beam fires, the Automaton loses all block. This is the burst window. Bludgeon + Vulnerable = 48+ damage. Double Tap + Bludgeon = 96+. Maximize damage output on this turn.

CASE STUDY — BLOCK SCALING GAP (DEFEAT, Floor 33):
- Entered at 92/92 (Pantograph healed to full). Deck met 3 of 4 readiness criteria: Thunderclap+ (AOE), Spot Weakness (Str), Feed+ (Healing). MISSING: block scaling beyond basic Defends.
- Artifact stripping executed correctly: Thunderclap+ (x2) + Bash+ stripped all 3 Artifacts by turn 3. Shockwave+ applied Weak 3 + Vuln 3 on turn 4.
- Hyper Beam dealt 38 damage on turn 6. With only basic Defends (4x5=20 max block), absorbed only 5 block. Dropped to 7 HP.
- Post-Hyper Beam stun turn: dealt 37 damage to Automaton (300->200 HP) but at 7 HP with no recovery.
- Turn 8: 24 incoming with only 5 block available. Dead.
- **ROOT CAUSE**: Zero block scaling cards (no Shrug It Off, no Flame Barrier, no Metallicize, no Impervious). Basic Defends cannot survive Hyper Beam. This death directly caused block scaling to be added as the 4th mandatory readiness criterion.
- **LESSON**: Impervious alone would have saved this run -- 30 block absorbs Hyper Beam (38-30=8 damage taken instead of 33). The deck's offensive preparation was excellent but defensive preparation was fatally inadequate.

CASE STUDY — WEAK TIMING (DEFEAT, Floor 33):
- Entered at 60/80 (75%). Deck met all 4 readiness criteria: Immolate (AOE), Inflame+Demon Form (Str), Reaper (Healing), Shrug It Off++Flame Barrier+ (Block scaling). Red Mask relic for free Weak turn 1.
- **Artifact stripping used Intimidate on Turn 1** to strip Artifact. Intimidate exhausted. This consumed the deck's only Weak source. Bash+ and Thunderclap were also used for stripping (correct). Red Mask stripped 1 automatically.
- Stasis stole Demon Form and Flame Barrier+. Both recovered by killing Orbs over Turns 3-5, but Demon Form was never played -- primary scaling card was stuck in Stasis/discard the entire fight.
- **Hyper Beam fired Turn 6 for 51 damage** (higher than any prior observation -- Str scaling pushes it well past 45). Player had 27 block (SIO+ 11 + SIO+ 11 + Defend 5) and 24 HP. Took 51-27=24 = exactly lethal.
- Player attempted to recover Intimidate from exhaust using Liquid Memories, but **Liquid Memories retrieves from DISCARD, not EXHAUST**. Retrieved Shrug It Off+ instead (which was in the discard pile).
- **ROOT CAUSE**: Intimidate wasted on Artifact stripping Turn 1. If Intimidate had been saved for the Hyper Beam turn, Weak would have reduced 51 to 38 damage. 38 minus 27 block = 11 damage at 24 HP = survived at 13 HP.
- **SECONDARY CAUSE**: Liquid Memories mechanics misunderstanding -- planned a potion interaction that cannot work.
- **LESSON**: Against Bronze Automaton, use only non-exhausting debuffs (Bash+, Thunderclap, Red Mask) for Artifact stripping. Save exhausting Weak sources (Intimidate, Shockwave) for Hyper Beam. The Hyper Beam turn is where Weak has maximum survival value.

WHAT NOT TO DO:
- Enter below 60% HP. The 300 HP + Str scaling creates a clock. Low entry HP means dying to scaling before killing the boss.
- Enter without block scaling beyond basic Defends. Basic Defends (20 max block) cannot survive Hyper Beam (38-51 damage). Impervious, Shrug It Off, Flame Barrier, or Metallicize are mandatory.
- **Use Intimidate or Shockwave for Artifact stripping.** These cards exhaust and are the primary Weak sources for surviving Hyper Beam. Wasting them on Artifact stripping leaves no Weak available when Hyper Beam fires. Use Bash+ and Thunderclap (non-exhausting) for Artifact stripping instead.
- Rely on a single irreplaceable card. Stasis WILL steal something important. If the entire strategy depends on one copy of Double Tap+ or Inflame, the strategy is fragile.
- Take Runic Dome into this fight. Without intent visibility, you cannot predict Hyper Beam timing and will either waste block on non-attack turns or take full Hyper Beam damage unblocked.
- Ignore Artifact. Applying Vulnerable or Weak before stripping 3 Artifact wastes the debuff application entirely.
- **Plan to recover exhausted cards with Liquid Memories.** Liquid Memories retrieves from the DISCARD pile only, not the exhaust pile. Exhausted cards cannot be recovered.

MULTI-HIT WARNING: Whirlwind and Pummel trigger Stasis on Orbs the same as any other attack but are not specifically penalized. However, these cards are better directed at the Automaton itself for raw damage rather than Orbs.

---
