# Bronze Automaton

- **Type:** Boss
- **Act:** 2
- **HP:** 300 (A0), 320 (A9)

## Starting State

[[buffs/Artifact]] 3. Accompanied by 2 Bronze Orbs (52-58 HP each).

## Pattern

- **Turn 1:** Always Spawn Orbs -- summons 2 Bronze Orbs.
- **Subsequent turns:** Fixed repeating cycle: Flail -> Boost -> Flail -> Boost -> HYPER BEAM -> Stunned.

## Attacks

| Move | Damage | Effect |
|------|--------|--------|
| Flail | 7x2 = 14 (8x2 = 16 at A4) | -- |
| Boost | -- | Gains 3 [[buffs/Strength]] + 9 Block |
| HYPER BEAM | 45 (50 at A4) | Automaton is Stunned next turn |
| Stunned | -- | Free damage window |

## Bronze Orbs

- HP: 52-58
- [[debuffs/Stasis]] (75% chance each turn until used, once per combat): steals highest-rarity card from draw pile. Killing Orb returns stolen card.
- After [[debuffs/Stasis]]: 70% Support Beam (Automaton gains 12 Block), 30% Beam (8 damage).

## Mechanics

**[[buffs/Artifact]] 3:** First 3 debuff applications are negated. [[relics/Red Mask]] relic strips 1 at combat start.

**Hyper Beam Timing:** First Hyper Beam at ~Turn 6 (45-51 damage with accumulated Str). Second at ~Turn 12 (57+ damage). Automaton is stunned the turn AFTER Hyper Beam (free damage window).

**[[buffs/Strength]] Scaling:** +3 [[buffs/Strength]] per Boost cycle. Fight is a DPS race.

**[[debuffs/Stasis]]:** Orbs steal a card from the player's deck. The stolen card is completely removed from combat until the Orb is killed. Targets [[types/Power]] and [[types/Skill]] cards preferentially.

**Stun Window:** After Hyper Beam, Automaton loses all block. This is the burst window.
