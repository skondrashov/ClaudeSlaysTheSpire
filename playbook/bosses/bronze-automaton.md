# Bronze Automaton (Act 2, HP: 300)

PATTERN:
- **Turn 1**: Spawns 2 Orb minions (~50 HP each). Orbs use **Stasis** to steal a card from the player's hand, removing it from combat entirely.
- **Subsequent turns**: Cycles between attacks, Strength gain (+3 Str per cycle), and Hyper Beam (a massive single-hit attack). Orbs continue stealing cards via Stasis.
- **Hyper Beam**: Extremely high single-hit damage. After firing, Automaton loses all block (vulnerability window). Without intent visibility (e.g. Runic Dome), this turn is impossible to predict and prepare for.
- **Strength scaling**: Gains +3 Strength per cycle. By turn 6-7, all attacks hit significantly harder than their base values. The fight becomes unwinnable if it goes too long.
- **Artifact 3**: Starts with 3 stacks of Artifact, which negate the first 3 debuff applications. Must strip all Artifact before Vulnerable, Weak, or Disarm take effect.

KEY MECHANICS:
- **Stasis (Orbs)**: Each Orb steals one card from the player's hand and holds it. The stolen card is completely removed from combat -- it cannot be drawn, played, or retrieved. Stasis targets Power and Skill cards preferentially. Losing key cards (Double Tap, Inflame, scaling Powers) to Stasis can cripple the deck mid-fight. This is the Automaton's most disruptive mechanic.
- **Artifact stripping**: Three debuff applications are needed before any debuff sticks. Thunderclap (1 Vulnerable = 1 Artifact stripped per enemy), Bash+ (applies Vulnerable = strips 1 Artifact), Disarm (applies -Str = strips 1 Artifact). Plan the first 2-3 turns around stripping Artifact before applying real debuffs.
- **Hyper Beam window**: After Hyper Beam fires, the Automaton is temporarily weakened. This is the burst window. Save high-damage plays (Bludgeon, Blood for Blood, Double Tap + big Attack) for this moment.

PREPARATION CHECKLIST:
1. **Enter at 70%+ HP** -- 300 HP boss with Strength scaling demands a large HP buffer. At 57% HP, there is no margin for error.
2. **Artifact strippers** -- Thunderclap, Bash+, any debuff card. Need 3 applications before Vulnerable/Weak/Disarm take effect.
3. **Burst damage** -- Bludgeon, Blood for Blood, Double Tap + Attacks. The fight must end before Strength scaling (+3/cycle) outpaces your block capacity.
4. **Redundant key cards** -- Stasis steals cards. If your strategy depends on a single copy of Double Tap or Inflame, Stasis can destroy the plan. Multiple copies of key effects or alternative win conditions provide resilience.
5. **Intent visibility** -- Runic Dome removes enemy intent display, making Hyper Beam timing unpredictable. Without intent, block allocation becomes guesswork. Avoid Runic Dome if Bronze Automaton is a possible Act 2 boss.

STRATEGY:
- **Turns 1-2 (Artifact stripping)**: Apply 3 debuffs to strip all Artifact stacks. Thunderclap is ideal (strips 1 from each enemy). Bash+ strips 1. Disarm strips 1. Once Artifact is gone, Vulnerable and Weak stick and amplify all subsequent damage and mitigation.
- **Kill Orbs early if possible**: Each surviving Orb steals one card per turn via Stasis. Removing Orbs stops the card drain. However, Orbs have ~50 HP -- committing too much damage to Orbs delays killing the 300 HP Automaton. Evaluate based on what cards have already been stolen.
- **Race the Strength scaling**: +3 Str/cycle means every turn the fight extends, incoming damage grows. By turn 6, attacks deal 15-20+ more than their base. Prioritize damage output over conservative blocking once Artifact is stripped and Vulnerable is applied.
- **Post-Hyper Beam burst**: After Hyper Beam fires, the Automaton loses all block. This is the burst window. Bludgeon + Vulnerable = 48+ damage. Double Tap + Bludgeon = 96+. Maximize damage output on this turn.

RUN 105 DEATH CASE STUDY (DEFEAT, Floor 33):
- Entered at 92/92 (Pantograph healed to full). Deck met 3 of 4 readiness criteria: Thunderclap+ (AOE), Spot Weakness (Str), Feed+ (Healing). MISSING: block scaling beyond basic Defends.
- Artifact stripping executed correctly: Thunderclap+ (x2) + Bash+ stripped all 3 Artifacts by turn 3. Shockwave+ applied Weak 3 + Vuln 3 on turn 4.
- Hyper Beam dealt 38 damage on turn 6. With only basic Defends (4x5=20 max block), absorbed only 5 block. Dropped to 7 HP.
- Post-Hyper Beam stun turn: dealt 37 damage to Automaton (300->200 HP) but at 7 HP with no recovery.
- Turn 8: 24 incoming with only 5 block available. Dead.
- **ROOT CAUSE**: Zero block scaling cards (no Shrug It Off, no Flame Barrier, no Metallicize, no Impervious). Basic Defends cannot survive Hyper Beam. This death directly caused block scaling to be added as the 4th mandatory readiness criterion.
- **LESSON**: Impervious alone would have saved this run -- 30 block absorbs Hyper Beam (38-30=8 damage taken instead of 33). The deck's offensive preparation was excellent but defensive preparation was fatally inadequate.

WHAT NOT TO DO:
- Enter below 60% HP. The 300 HP + Str scaling creates a clock. Low entry HP means dying to scaling before killing the boss.
- Enter without block scaling beyond basic Defends. Run 105 entered at full HP with correct Artifact stripping and died because 4 basic Defends (20 max block) cannot survive Hyper Beam (38 damage). Impervious, Shrug It Off, Flame Barrier, or Metallicize are mandatory.
- Rely on a single irreplaceable card. Stasis WILL steal something important. If the entire strategy depends on one copy of Double Tap+ or Inflame, the strategy is fragile.
- Take Runic Dome into this fight. Without intent visibility, you cannot predict Hyper Beam timing and will either waste block on non-attack turns or take full Hyper Beam damage unblocked.
- Ignore Artifact. Applying Vulnerable or Weak before stripping 3 Artifact wastes the debuff application entirely.

MULTI-HIT WARNING: Whirlwind and Pummel trigger Stasis on Orbs the same as any other attack but are not specifically penalized. However, these cards are better directed at the Automaton itself for raw damage rather than Orbs.

---
