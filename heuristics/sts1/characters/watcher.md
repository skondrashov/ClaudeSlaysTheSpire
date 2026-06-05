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

- **[[cards/Mental Fortress]]** (Power, block on stance change) — best defensive Power. Mental Fortress+ gives 6 block per stance change, turning every Calm/Wrath cycle into free block. Transforms the engine from "damage with risk" to "damage AND defense."
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

While you are IN Wrath, your attacks deal double damage (and you take double incoming). The catch, verified vs the game jar: the card that ENTERS Wrath does NOT double its own hit — its damage resolves *before* the stance turns on (see combat.md rule 9). Common miscalculations:

- **Tantrum** (3 dmg x 3 hits = 9; Tantrum+ = 3 x 4 = 12): Played while ALREADY in Wrath → doubled to 18 / 24. But if Tantrum is the card ENTERING Wrath (from Calm/Neutral), its own hits are NOT doubled — it deals 9 / 12, and Wrath only doubles the attacks you play AFTER it. A Tantrum+ dealing 24 is the already-in-Wrath case.
- **Conclude+ in Wrath:** Base 12 AOE. In Wrath: 24 AOE. Conclude also ends the turn — so any surviving enemies attack into Wrath (doubled incoming). Only use Conclude in Wrath if it kills all enemies.
- **Flurry of Blows in Wrath:** Base 4. In Wrath: 8. Free damage that adds up.

**Rule:** When calculating kill math in Wrath, double EVERY damage number. Do not selectively double some cards and not others.

## NEVER Use Distilled Chaos as Watcher

Distilled Chaos plays a random card from the draw pile. The Watcher's draw pile frequently contains cards that are CATASTROPHIC when played at the wrong time:

- **Meditate / Meditate+:** Enters Calm and ENDS YOUR TURN. If played randomly with 0 block against lethal incoming, you die instantly. Distilled Chaos can play Meditate+ (ends your turn, 0 block) — against a 102-damage Hyper Beam that is 102 unblocked.
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

**Confirmed dangerous:** Chosen+Byrd hallway. Hex + Watcher's Skill-heavy engine causes deck collapse. A functional engine can still fail here because Dazed flooding makes it impossible to draw the right cards.

## Execution Risks

The Watcher's stance mechanics create unique execution failure modes not present in other characters:

1. **Accidental Wrath entry via turn() index shifting.** Batched turn() commands with index-based card references can play the wrong card when indices shift after each play. If the wrong card enters Wrath, the result is often lethal. **Always use card names in turn() batches** (see combat.md rule 6).
2. **Blasphemy self-kill.** Blasphemy sets HP to 1 at end of next turn. The kill MUST be confirmed with exact arithmetic before playing.
3. **Missing Wrath exit.** Entering Wrath without a confirmed exit card in hand or guaranteed next draw is gambling with doubled incoming damage. Before entering Wrath, verify: "Do I have an exit in hand RIGHT NOW?" If no, do not enter Wrath.
4. **Wrath damage miscalculation.** Two distinct cases, commonly conflated: a card that ENTERS Wrath does NOT double its own hit (jar-verified — see combat.md rule 9), but any attack played while ALREADY in Wrath IS doubled. Track which case you are in. See "Wrath Damage Arithmetic" above.

## HP Management

The Watcher is more HP-sensitive than other characters because Wrath doubles incoming damage. Additional considerations:

- **Reduced Max HP pools change boss math.** Council of Ghosts (-Max HP for Apparitions) is excellent but leaves absolute HP dangerously low. At 36 Max HP, a single unblocked Hyper Beam (45 base, 57+ with Str) is instantly lethal. When Max HP is reduced, boss entry HP percentage is less important than absolute HP — calculate survival against the worst single hit.
- **Sozu + Philosopher's Stone is a lethal combination.** Sozu prevents potion use (no emergency healing), and Philosopher's Stone gives enemies +1 Str (amplifies all incoming damage). With no healing and harder fights, HP attrition through Act 3 becomes unsurvivable. Avoid both together.
- **Pantograph (+25 HP at boss start) is exceptional.** It changes the rest-vs-upgrade calculus at pre-boss rest sites. If Rest + Pantograph would overcap HP, always upgrade instead.

## Relic Warnings

**Runic Pyramid (retain hand between turns):** Dangerous for Watcher. Burns, Wounds, Slimed, Dazed, and other unplayable status cards are retained permanently, consuming hand slots every turn. The Watcher needs specific cards in hand each turn for stance sequencing (Eruption/Crescendo for Wrath entry, Vigilance/Inner Peace/Empty Body for Calm exit). Retained junk cards reduce the effective hand size, making it impossible to sequence stance changes reliably. Against Nemesis, Burns retained by Runic Pyramid clog the hand and starve the stance-change cards you need each turn. Avoid Runic Pyramid unless the deck has very few sources of status cards AND a way to play/exhaust them.

**Sozu (no potions):** Removes the Watcher's only emergency healing and burst tools. Combined with Philosopher's Stone (+1 enemy Str), the Watcher takes amplified damage with no recovery option — a deadly pairing.

## Spire Growth Counter-Strategy

Spire Growth (170 HP, Act 3) applies **Constricted X** on its STRONG_DEBUFF turns. Constricted deals X damage at end of every subsequent turn, and this damage IS affected by block. However, it stacks with the attack damage each turn, so the effective incoming damage per turn is (attack + Constricted).

**At low HP, Constricted is lethal.** Constricted 10 means you need 10 EXTRA block every turn beyond blocking the attack. If the attack is 16 (Weakened), that's 26 block needed per turn. Without massive block generation or Wrath burst to kill quickly, this is unsurvivable at low HP.

**Mitigation:**
- Enter the fight at high HP (40+). Constricted is manageable if you can absorb a few turns of damage.
- Kill FAST. Wrath burst with the full engine (Rushdown 4, Deva Form, Divinity) can output 50-100+ damage per turn.
- Do NOT waste the first free debuff turn on setup if your HP is critical — prioritize block infrastructure over power setup.
- Wave of the Hand + Wallop combo is key: Wallop generates block equal to damage dealt, Wave converts that to Weak, reducing attack component.

Entering at low HP is unsurvivable: at 9 HP, Constricted 10 + 16 attack = 26 damage per turn while a hand maxes out at ~12 block, so you die within a couple of turns.

## Key Lessons

The stance dance engine assembles reliably, but the recurring causes of death are strategic/knowledge gaps and HP management:

- **No built-in healing:** The Watcher has NO built-in healing. Without healing cards/relics/potions, HP attrition through Act 3 kills even with a strong engine. Stance dance generates damage and block but cannot recover HP. Prioritize acquiring healing sources (potions, Meal Ticket, events) to sustain through Act 3.
- **NEVER end in Wrath without a guaranteed exit:** Ending in Wrath (e.g. against Orb Walker) with Burns in hand and no exit doubles incoming damage and causes catastrophic HP loss.
- **Runic Pyramid is dangerous for Watcher:** Burns and other unplayable cards are retained by Runic Pyramid, permanently consuming hand slots. The Watcher needs specific cards in hand each turn for stance sequencing. Retained junk cards break the engine. Avoid Runic Pyramid unless the deck has very few status/curse sources.
- **Slime Boss requires special preparation:** The Watcher's stance dance engine is single-target focused. Slimed flooding is uniquely punishing because drawing the right stance-change cards in the right order is critical. See Slime Boss matchup notes.
