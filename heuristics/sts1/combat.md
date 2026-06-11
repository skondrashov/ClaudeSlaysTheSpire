# Combat Execution

## The Full Block Algorithm

**The default goal every turn in a hallway fight is ZERO DAMAGE TAKEN.** Not "minimize damage." Zero. HP lost in a hallway fight is permanent until a rest site. 8 damage at 80 HP is exactly as bad as 8 damage at 20 HP.

Every turn:

1. Read total incoming damage (sum all attacking enemies, apply [[debuffs/Weak]] if on them).
2. Enumerate ALL paths to zero damage:
   - **Kill attackers** + block remainder
   - **Pure block** (block cards, Weak on attacker)
   - **Debuff + block** (apply Weak to reduce, block the rest)
   - **Potion-assisted** (damage potion to kill, block potion to survive)
3. Compare paths that achieve zero: prefer kill paths (removes future damage).
4. If NO path achieves zero: minimize damage. Use potions. Kill the highest-damage attacker.
5. **Premises decay mid-turn.** After any mid-turn kill or state change, re-derive incoming from the LIVING enemies before playing block — block bought against a dead enemy's attack is wasted energy. Before each card, confirm the fact that put it in the plan still holds (target alive, draws unlocked, stance unchanged).

**Enumerate at least two paths before choosing.** Do not pick ONE plan and execute.

### Exceptions

1. **Boss fights.** HP resets via rest/heal. Spend HP freely to kill faster.
2. **Hard-scaling enemies ([[buffs/Ritual]], Rally).** Kill speed prevents more total damage than blocking. This sets the fight TYPE (race, spend HP), not the kill ORDER — in multi-enemy fights, target priority still follows the enemy pages (e.g. Chosen+Cultist: [[enemies/Chosen]]'s branch), and whichever target is chosen gets ALL the damage.

Everything else is a hallway fight: zero damage taken.

### Fight Strategy (once per combat)

Before the first turn, write and post via `think()`:

```
FIGHT STRATEGY — [Enemy Name]
FIGHT TYPE: [Hallway (full block) | Boss (spend HP freely) | Hard-scaler (kill speed)]
WIN CONDITION: How do I kill this?
ZERO DAMAGE PLAN: How do I block each turn?
KEY CARDS: Which cards matter most?
POTION PLAN: When to use potions?
RISKS: What can go wrong?
```

### Turn Planning (every turn)

```
TURN N — INCOMING: [damage] — PATHS TO ZERO:
  A) Kill [enemy] (XE) + block remainder → zero? [y/n]
  B) Pure block → total block vs incoming → zero? [y/n]
CHOSEN: [A/B] because [reason]
```

### Draw Effects — CRITICAL

**NEVER include cards after a draw card in a `turn()` sequence.** If a card draws ([[cards/Backflip]], [[cards/Shrug It Off]], [[cards/Pommel Strike]], [[cards/Battle Trance]], [[cards/Offering]], etc.), it must be the LAST action in the batch — and **never batch `end` right after a draw card while energy remains.** A trailing `end` is honored even after the draw stop, committing the turn before you see the drawn cards (the drawn card and leftover energy are forfeited). Play the draw card via `send()`, read the result, THEN end. turn() does NOT auto-end — an open turn stays open until you send `end`.

**No Draw kills every later draw effect this turn.** Once No Draw is active ([[cards/Battle Trance]] applies it), ALL further draw effects this turn are dead — Pommel Strike digs find nothing, Shrug It Off's draw is gone, [[potions/Snecko Oil]] is wasted whole. Sequence the draw effects you intend to use BEFORE Battle Trance, or drop them from the turn. Before any draw-motivated play (a dig for block, a draw potion), check whether a draw lock is active.

---

## Combat Arithmetic Checklist

Before every turn, verify these items.

### 1. Am I using UPGRADED values?

Check the + suffix on every card. Common errors:

- Shrug It Off+ = 11 block (not 8)
- [[cards/Flame Barrier]] = 16 block AND 6 counter-damage
- [[cards/Armaments]] = 5 block AND upgrades ALL cards in hand
- [[cards/Bash]] = 10 damage, 3 [[debuffs/Vulnerable]] (not 2)
- [[cards/Spot Weakness]] = +3 [[buffs/Strength]] unupgraded / +4 Strength upgraded
- [[cards/Heavy Blade]] = Str multiplier 3x unupgraded / 5x upgraded (at Str 9: 41 vs 59 damage)

### 2. VERIFY KILL MATH BEFORE ENDING TURN

On kill turns, NEVER include `end` in the same command as the final attack. Play the attack, verify the kill, THEN end the turn separately.

### 3. X-COST CARDS: PLAY LAST

Always play X-cost cards LAST. To control the value of X, spend energy on other cards first. This applies INSIDE batches too: an X-cost play consumes ALL remaining energy at the moment it resolves, so any play queued after it in the same batch fizzles — a batch like `play Whirlwind; play Defend; end` spends the Defend's energy on X and never blocks.

### 4. WRAITH FORM: TIME IT BY FIGHT LENGTH

[[cards/Wraith Form]] gives [[buffs/Intangible]] but applies permanent -1 [[buffs/Dexterity]] per turn. In long fights, play it as a finisher only — see [[cards/Wraith Form]] for the timing framework by fight length.

### 5. VERIFY CARD IDENTITY BEFORE PLAYING

Hand indices shift after each play. Before entering `play N`, confirm the card at index N matches your plan. Re-read hand state after each card play.

### 6. USE CARD NAMES IN turn() BATCHES — NEVER INDICES

In batched `turn()` commands, card indices shift after each play but the batch pre-computes all actions. This causes the wrong card to be played. For example, `turn(["play 1", "play 2 0", "play 3 0", "play 4", "end"])` can play Eruption+ instead of a Strike because indices shift after the first card is played, entering Wrath with no exit and causing death.

**RULE:** Always use card names in `turn()` sequences: `turn(["play Consecrate", "play Strike 0", "play Strike 0", "play Defend", "end"])`. Card names resolve against the current hand state at the time each action executes, so they are immune to index shifting.

If two copies of the same card exist in hand and you need to play a specific one, play each card individually via `send()` with a state check between plays instead of using `turn()`.

### 7. POTION ORDERING ON KILL TURNS

On kill turns, play all deterministic damage cards FIRST. Only use random-outcome potions (Distilled Chaos, Gambler's Brew) AFTER all known-value plays are exhausted — or never.

**Rationale:** If the kill is already in hand with deterministic cards, random effects are unnecessary and can only cause harm. If the kill is NOT in hand, playing deterministic damage first reduces the enemy to minimum HP, making the random effect more likely to finish the job and less costly if it fails.

A random effect can play a turn-ender or a zero-value card while leaving the kill unfinished and your block at zero — converting a won turn into a lost fight. The usual root cause is a kill-math error: believing the hand is short on damage when it isn't. Verify the kill arithmetic before reaching for randomness.

**Rule:** Deterministic cards first, random effects last, on EVERY kill turn. No exceptions.

### 8. VERIFY DEBUFF TYPE: VULNERABLE IS NOT WEAK

Thunderclap applies [[debuffs/Vulnerable]] (target takes 50% MORE damage). It does NOT reduce enemy damage. Vulnerable makes the TARGET take more damage from attacks -- it is an offensive amplifier, not a defensive tool.

**Ironclad Weak sources (reduce enemy damage dealt by 25%):** [[cards/Intimidate]], [[cards/Clothesline]], [[cards/Shockwave]] (which also applies Vulnerable).

**Ironclad Vulnerable sources (target takes 50% more damage from attacks):** [[cards/Bash]], [[cards/Thunderclap]], [[cards/Uppercut]] (which also applies Weak).

**CRITICAL:** Thunderclap and Intimidate are both mass debuff cards, but they apply OPPOSITE effects. Playing Thunderclap does NOT reduce incoming damage. If the survival plan depends on reducing enemy damage, you need a Weak source (Intimidate, Clothesline, Shockwave), NOT Thunderclap. Treating Thunderclap as Weak miscalculates incoming — it applies Vulnerable, not Weak, so enemy damage is NOT reduced. If your block plan relied on a 25% reduction, actual incoming is the full 30 (not 21) and you take the full hit.

### 9. WRATH DOUBLES DAMAGE — BUT NOT THE HIT THAT ENTERS WRATH

For Watcher: while you are **already in Wrath**, your attacks deal double damage (and you take double from attacks). But the card that **enters** Wrath does NOT double its own hit — it deals its damage first and enters Wrath after, so that hit lands before Wrath is active.

- **Eruption** deals its 9 at base (not 18); **Eruption+** is also 9.
- **Tantrum** deals `magicNumber x base` at base, THEN enters Wrath. Tantrum+ from Calm = 3x4 = 12 (NOT 24) on the turn it enters.
- Only attacks played **after** you are already in Wrath are doubled — subsequent cards the same turn, or any attack on a later turn while Wrath persists. (A second copy of Tantrum, or any Strike, played after you're in Wrath IS doubled.)

**Rule:** In kill math, the entering card's hit is base — do NOT double the Eruption/Tantrum that enters Wrath. DO double every attack you play after it while Wrath is active. Double-check the arithmetic before committing to end turn.

### 10. INCLUDE YOUR OWN DEBUFFS IN EVERY CALC

Your own [[debuffs/Weak]] cuts YOUR attack damage by 25%; your own [[debuffs/Frail]] cuts YOUR block by 25%. Both multipliers round DOWN (Defend 5 under Frail = 3 block, not 4). Run every kill-math and every block total with your own active debuffs applied — a "lethal" line computed without your Weak comes up short by exactly the discount, and a block plan that ignores Frail under-blocks at the worst margins.

### 11. SEND DISCIPLINE UNDER INTERFACE LAG

When state echoes come back empty (`{}`) or unchanged, the interface is racing — slow down before anything else:

- **Never re-send `end` after an empty echo.** WAIT and re-poll the state. A queued duplicate `end` ends the NEXT turn with zero cards played — an entire discarded hand.
- **Re-send lost actions by card NAME, never by index.** If a batch's result never echoed, your hand model is stale; an index computed against it plays the wrong card.
- **Single-card sends bypass the batch energy guard.** When lag forces one-send-per-echo play, re-sum the turn's energy plan by hand before each play — the error family the guard retired comes back exactly here.

---

## Shockwave+ Timing Rule

Play Shockwave+ on the **FIRST ATTACK TURN** of multi-enemy fights.

- **Turn 1 is NOT always correct:** if all enemies are buffing (e.g., Cultists on turn 1), Weak is wasted on a non-attack turn.
- **Turn 2 is usually correct:** most multi-enemy fights begin attacking on turn 2.
- **NEVER save for turn 4+:** by then enemies have already accumulated Strength and you have taken unnecessary damage.
- **Priority on the first attack turn:** Shockwave+ (mass Weak + Vulnerable) > [[cards/Reaper]] (healing) > single-target damage.

---

## Potion Economy

**Potions are expiring resources; HP is the resource that does not come back.** A potion held to the end of the run was worth zero. A potion that converts unblocked damage to zero converts directly into HP, the scarcest thing in the game. So the default is to DRINK, and it is *holding* that requires justification — not the other way around.

**The check runs every fight, not just in emergencies.** Before ending any turn where unblocked damage will get through, or where a potion would shorten the fight by a full enemy turn, ask: does a potion close this gap? If yes, the default is to use it. Holding it instead requires naming the specific upcoming fight where it is clearly worth more — a named fight within the next 1-2 floors, not "later." If you cannot name the fight, drink.

**Slot economics:** slots are part of the economy. Combat rewards regularly offer potions, and a full belt forces you to skip them. A potion drunk while your slots are full costs nothing: you were about to be offered its replacement. Err on the side of keeping a slot open. Winning a fight at full slots without drinking anything usually means a future potion was wasted.

Situations where drinking is almost always right:
- A damage potion kills an enemy that is scaling or generating status cards (a Cultist ramping Strength, Sentries adding Dazed). Killing the source early prevents compound damage.
- A Strength or damage potion removes a full enemy turn from the fight. Fewer enemy turns is the cleanest damage prevention there is.
- A block potion covers a hit your hand cannot — in ANY fight. Chip damage in an "easy" hallway fight is the same HP as boss damage.

**Exception:** [[potions/Fairy in a Bottle]], and a potion held for a *named* fight within the next 1-2 floors (the boss behind the next door, an elite already routed into). Everything else is evaluated for use in the fight you are in.
