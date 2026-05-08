# Bronze Automaton (Act 2 Boss)
HP: 300. Starts with Artifact 3. Accompanied by 2 Orbs (50 HP each).

## Key Mechanics
- **Artifact 3**: First 3 debuff applications are negated. Must strip all Artifact before Vulnerable/Weak will stick. Thunderclap+ strips 1 per enemy per cast. Bash+ strips 1. Shockwave+ strips 1 per debuff type (Weak + Vuln = 2 charges consumed). Plan 3 debuff applications minimum before relying on Vulnerable/Weak.
- **Hyper Beam**: 45 raw damage (observed 38-45 depending on buffs). Automaton is stunned the turn AFTER Hyper Beam. This is the most dangerous attack in the fight -- basic Defends (4x5=20 block) cannot survive it. Requires block scaling (Shrug It Off, Flame Barrier, Metallicize, Impervious, Ghostly Armor) or significant Weak uptime.
- **Stasis (Orbs)**: Orbs steal a card from your deck via Stasis. Killing the Orb returns the stolen card. Do not rely on a single copy of any critical card. If Fiend Fire or Shockwave+ is stolen, kill that Orb to recover it.
- **Strength scaling**: +3 Str per buff cycle. Fight is a DPS race -- long fights become unsurvivable as Hyper Beam damage scales.
- **Stun turn**: After Hyper Beam, Automaton is stunned for 1 turn. This is a free damage window. Use it for burst (Fiend Fire+, Rampage, Spot Weakness setup).

## Fight Phases
1. **Artifact Strip (Turns 1-3)**: Use cheap debuffs to strip Artifact 3. Thunderclap+ (1E, strips 1 from all enemies) is ideal. Bash+ strips 1. Goal: all Artifact gone by turn 3-4.
2. **Debuff Window (Turn 3-4)**: Once Artifact is 0, apply Shockwave+ (Weak 3 + Vuln 3). This is the pivot point of the fight.
3. **Burst Phase (Turns 4-7)**: With Vuln active, unload burst damage. Fiend Fire+, Rampage scaling, Hemokinesis. Goal: deal 150+ damage in 3-4 turns.
4. **Hyper Beam Survival (Turn 6-8)**: Hyper Beam hits for 38-45. MUST have 30+ block or Weak active. Basic Defends (5 each) are NOT sufficient. Need block scaling cards or relic-based block (Calipers retained block, Metallicize, etc).
5. **Stun Window**: After Hyper Beam, Automaton is stunned. Free damage turn. Use Spot Weakness, Fiend Fire, or Rampage here.

## What Kills You
- **Insufficient block for Hyper Beam**: Run 105 died here. Deck had 4 basic Defends (5 block each = 20 max). Hyper Beam dealt 38+ unblocked damage. With no Shrug It Off, Flame Barrier, Metallicize, Ghostly Armor, or Impervious, the Hyper Beam was unsurvivable even with partial Weak reduction.
- **Low HP entry**: Run 114 entered at 39/85 (45%) with all 4 readiness criteria met and Dark Shackles for Hyper Beam reduction. Dark Shackles reduced Hyper Beam from ~51 to ~42, but 42 + Orb damage (6) = 48 incoming against 13 block = 35 unblocked. At 31 HP, this was lethal. The deck had the tools (Metallicize, Ghostly Armor, Shrug It Off, Dark Shackles) but HP was too low to absorb even a partially-mitigated Hyper Beam. The 70% entry threshold exists because even GOOD block hands cannot fully absorb Hyper Beam + Orb damage.
- **Stasis stealing a key card**: Orbs use Stasis to steal a card from your deck. Run 114: Stasis stole Metallicize (best passive block source), removing 3 block/turn for the rest of the fight. This made Hyper Beam survival math impossible. **Priority: Kill Stasis Orbs BEFORE they steal a critical card.** If an Orb has already stolen a card (visible in the Stasis tooltip), killing that Orb returns the card. Prioritize killing the Orb that stole your most important card. If Metallicize, Impervious, or your only Weak source is stolen, that Orb becomes kill priority #1 -- above dealing damage to the Automaton itself.
- **Long fights**: +3 Str/cycle means Hyper Beam grows. By turn 10, Hyper Beam deals 50+. Kill before turn 10 if possible.

## Dark Shackles Interaction
Dark Shackles (0E, reduce enemy Str by 15 for 1 turn) is excellent for Hyper Beam survival but NOT sufficient alone. Run 114 math: Automaton had ~6 Str when Hyper Beam fired. Dark Shackles reduced to -9 Str, changing Hyper Beam from ~51 to ~42 damage. This is a ~9 damage reduction, NOT a full neutralization. You still need 30+ block on top of Dark Shackles. Dark Shackles + Metallicize + Ghostly Armor + 2 Defends = ~31 block vs 42 = take 11. At 70% HP (60/85), this is survivable. At 45% HP (39/85), it was not because prior turns had already chipped HP.

## Required Cards/Tools
- **Artifact strippers** (MANDATORY): Thunderclap+, Bash+, any cheap debuff. Need 3+ applications.
- **Block scaling** (MANDATORY): Shrug It Off, Flame Barrier, Metallicize, Impervious, Ghostly Armor. Basic Defends are NOT enough for Hyper Beam. Need 30+ block capability in a single turn.
- **Burst damage**: Fiend Fire+, Rampage, Bludgeon. DPS race against Strength scaling.
- **Strength source**: Spot Weakness, Inflame. Needed to race the damage check.
- **Weak source**: Shockwave+ reduces Hyper Beam by 25%. Critical for survival.

## Odd Mushroom Anti-Synergy
Odd Mushroom reduces Vulnerable multiplier from 1.5x to 1.25x. This significantly reduces damage output in a fight where DPS racing is critical. Run 105 had Odd Mushroom, reducing effective burst by ~17% on Vulnerable targets. With 300 HP to burn through, this anti-synergy extends the fight by 1-2 turns, which means facing another Hyper Beam cycle.

## HP Entry Threshold
70%+ or Pantograph. Hyper Beam demands a large HP buffer. Run 105 entered at 92/92 (Pantograph) and still died because block cards were missing -- HP alone does not save you without block scaling. Run 114 entered at 39/85 (45%) with ALL block scaling tools (Metallicize, Ghostly Armor, Shrug It Off, Dark Shackles) and still died because HP was too low. Both HP AND block scaling are required -- neither alone is sufficient.
