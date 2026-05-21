# Watcher

## The Energy Loop

The core engine is cycling between Calm and Wrath:
1. Enter Calm ([[cards/Vigilance]], [[cards/Inner Peace]], [[cards/Meditate]]).
2. Next turn, exit Calm into Wrath ([[cards/Eruption]], [[cards/Crescendo]]). Gain +2 Energy from leaving Calm.
3. Play attacks in Wrath at doubled damage using the bonus energy.
4. Exit Wrath before end of turn (Vigilance, Inner Peace, [[cards/Empty Body]], [[cards/Fear No Evil]]).
5. Repeat.

With Eruption+ (1E), entering Wrath from Calm costs net -1E. The Watcher effectively gets 2 free energy per cycle compared to no-stance play.

## End-of-Turn Stance Decision

Your end-of-turn stance is one of the most important decisions each turn. Don't default — think about it.

Consider:
- **What is the enemy doing?** If attacking, ending in Wrath means double damage taken. If buffing/debuffing, Wrath is free doubled damage next turn.
- **What do I need next turn?** Ending in Calm means +2E next turn on exit. Ending in Wrath means immediate doubled attacks but doubled incoming.
- **Do I have an exit next turn?** If ending in Wrath, you need a Calm-entry card in your next draw. If your deck is thin on exits, ending in Wrath is gambling.
- **Is this a boss fight?** More aggressive Wrath-staying is acceptable when HP management is looser.

**The dangerous default is staying in Wrath and hoping.** If you can't confidently exit Wrath next turn, don't end in it.

## Stance Sequencing

Play cards that trigger on stance change BEFORE changing stance. [[cards/Flurry of Blows]] must be in the discard pile before the stance change for the trigger to work. Check individual card files for play-order rules.

## Key Cards

**Power priority:** Mental Fortress > Rushdown > Battle Hymn > everything else. Mental Fortress+ provides 6 block per stance change with zero energy cost — it converts the stance dance engine into a passive block engine. Rushdown provides the draw density that makes burst turns possible.

- **[[cards/Mental Fortress]]** (Power, block on stance change) — best defensive Power. Mental Fortress+ gave 6 block per stance change in Run 192, turning every Calm/Wrath cycle into free block. Transforms the engine from "damage with risk" to "damage AND defense."
- **Flurry of Blows** (0E, returns from discard on stance change) — best common card. Free damage on every cycle. Take multiples.
- **Eruption+** — highest priority upgrade. 2E→1E makes the Calm loop net positive.
- **[[cards/Battle Hymn]]** (Power, generates Smite each turn) — best sustained damage for boss fights.
- **[[cards/Rushdown]]** (Power, draw 2-3 on Wrath entry) — enables massive burst turns.
- **[[cards/Wave of the Hand]]** (block gain applies [[debuffs/Weak]]) — primary Weak source.
- **[[cards/Talk to the Hand]]** (Block Return, Exhaust) — excellent against multi-hit enemies.
- **[[cards/Judgment]]** (instant kill at 30/40 HP) — powerful finisher.

## Boss Preparation

Need at minimum: (1) a Wrath exit in the deck (at least 2 sources), (2) a Weak source, (3) enough damage cards for Wrath burst windows.

## HP Sensitivity

The Watcher is more HP-sensitive than other characters because Wrath doubles incoming damage. A single turn ending in Wrath against an attacker can drain 20-40 HP from doubled multi-hits. Prioritize HP conservation. See "HP Management" below for relic interactions and boss math.

## Wrath Damage Arithmetic

ALL damage is doubled in Wrath, including multi-hit cards. Common source of miscalculation:

- **Tantrum+ in Wrath:** Base 2x5 = 10. In Wrath: 2x10 = 20. From Calm (entering Wrath): still 20 — the stance change happens before damage resolves, so the hits ARE doubled. Confirmed in Run 193: Tantrum+ dealt 24 (with other modifiers) not 12. The player miscalculated this as 12 and it was the fatal error that ended the run.
- **Conclude+ in Wrath:** Base 12 AOE. In Wrath: 24 AOE. Conclude also ends the turn — so any surviving enemies attack into Wrath (doubled incoming). Only use Conclude in Wrath if it kills all enemies.
- **Flurry of Blows in Wrath:** Base 4. In Wrath: 8. Free damage that adds up.

**Rule:** When calculating kill math in Wrath, double EVERY damage number. Do not selectively double some cards and not others.

## NEVER Use Distilled Chaos as Watcher

Distilled Chaos plays a random card from the draw pile. The Watcher's draw pile frequently contains cards that are CATASTROPHIC when played at the wrong time:

- **Meditate / Meditate+:** Enters Calm and ENDS YOUR TURN. If played randomly with 0 block against lethal incoming, you die instantly. Confirmed fatal: Run 193 — Distilled Chaos played Meditate+ with 0 block against 102 Hyper Beam.
- **Blasphemy:** Sets HP to 1. If played randomly, you die at end of next turn unless you kill everything.
- **Conclude / Conclude+:** ENDS YOUR TURN (after dealing damage). Same risk as Meditate.
- **Stance changers (Eruption, Crescendo, Tantrum):** May enter Wrath unexpectedly, doubling incoming damage.

**This is not a marginal risk.** A typical Watcher deck has 5-8 Skills in the draw pile at any time. At least 1-2 of those are turn-ending or stance-changing. The expected value of Distilled Chaos is negative for Watcher.

**Rule:** NEVER use Distilled Chaos as Watcher. If offered, skip it. If acquired from a random source, do not drink it. No exceptions.

## Hex / Chosen Counter-Strategy

The Chosen's Hex debuff adds a Dazed card to the draw pile every time a Skill is played. The Watcher is uniquely vulnerable because the stance dance engine depends heavily on Skills: Vigilance, Inner Peace, Empty Body, Meditate, and Defend are all Skills that trigger Hex.

**Mitigation:**
- Kill the Chosen FIRST. Hex stops when Chosen dies.
- Prefer Attack-based Wrath entries (Eruption, Tantrum) over Skill-based Calm entries (Vigilance, Inner Peace).
- Powers (Rushdown, Mental Fortress, Battle Hymn) do NOT trigger Hex. Set up Powers early.
- If Hex is already applied, minimize Skill plays. Accept some damage rather than flooding the draw pile with Dazed.
- Wave of the Hand is a Skill — using it for Weak triggers Hex. Accept the trade-off only if Weak prevents more damage than Dazed costs.

**Confirmed: Run 191 (F24)** — Chosen+Byrd hallway. Hex + Watcher's Skill-heavy engine caused deck collapse. The engine was functional before this fight but Dazed flooding made it impossible to draw the right cards.

## Execution Risks

The Watcher's stance mechanics create unique execution failure modes not present in other characters:

1. **Accidental Wrath entry via turn() index shifting.** Batched turn() commands with index-based card references can play the wrong card when indices shift after each play. If the wrong card enters Wrath, the result is often lethal. **Always use card names in turn() batches** (see combat.md rule 6). Confirmed fatal: Run 190.
2. **Blasphemy self-kill.** Blasphemy sets HP to 1 at end of next turn. The kill MUST be confirmed with exact arithmetic before playing. Confirmed fatal: Run 189.
3. **Missing Wrath exit.** Entering Wrath without a confirmed exit card in hand or guaranteed next draw is gambling with doubled incoming damage. Before entering Wrath, verify: "Do I have an exit in hand RIGHT NOW?" If no, do not enter Wrath.
4. **Wrath damage miscalculation.** Multi-hit cards entering Wrath (Tantrum, Ragnarok) are commonly miscalculated. The stance change resolves BEFORE damage, so all hits are doubled. See "Wrath Damage Arithmetic" above. Confirmed fatal: Run 193.

## HP Management

The Watcher is more HP-sensitive than other characters because Wrath doubles incoming damage. Additional considerations:

- **Reduced Max HP pools change boss math.** Council of Ghosts (-Max HP for Apparitions) is excellent but leaves absolute HP dangerously low. At 36 Max HP, a single unblocked Hyper Beam (45 base, 57+ with Str) is instantly lethal. When Max HP is reduced, boss entry HP percentage is less important than absolute HP — calculate survival against the worst single hit.
- **Sozu + Philosopher's Stone is a lethal combination.** Sozu prevents potion use (no emergency healing), and Philosopher's Stone gives enemies +1 Str (amplifies all incoming damage). Run 192 died at F25 with this combination — no healing and harder fights. Avoid both together.
- **Pantograph (+25 HP at boss start) is exceptional.** It changes the rest-vs-upgrade calculus at pre-boss rest sites. If Rest + Pantograph would overcap HP, always upgrade instead. Run 193 correctly identified this.

## Current Status

0 wins in 11 runs (128-132, 188-193), best Floor 33. Stance dance is the only engine tested. The engine assembles reliably and the strategic framework is sound. Directive 4 (execution cleanup, runs 191-193) eliminated all index-shift errors and Blasphemy self-kills — execution is now clean. Recent deaths are strategic/knowledge gaps, not execution failures:
- Run 191 (F24): Chosen+Byrd — Hex vulnerability, Skill-heavy engine collapsed.
- Run 192 (F25): Slavers elite at low HP — Sozu+Philosopher's Stone, no healing.
- Run 193 (F33): Bronze Automaton — Tantrum+ damage miscalculation led to unnecessary Distilled Chaos use that ended the turn. The kill was in hand.

The bottleneck has shifted from execution to matchup knowledge. The engine can reach Act 2 bosses; it needs better fight-specific heuristics to close out runs.
