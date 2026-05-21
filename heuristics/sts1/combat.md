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

**Enumerate at least two paths before choosing.** Do not pick ONE plan and execute.

### Exceptions

1. **Boss fights.** HP resets via rest/heal. Spend HP freely to kill faster.
2. **Hard-scaling enemies ([[buffs/Ritual]], Rally).** Kill speed prevents more total damage than blocking.

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

**NEVER include cards after a draw card in a `turn()` sequence.** If a card draws ([[cards/Backflip]], [[cards/Shrug It Off]], [[cards/Pommel Strike]], [[cards/Battle Trance]], [[cards/Offering]], etc.), it MUST be the last card before `"end"`. Play it via `send()` and re-read state before continuing.

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

Always play X-cost cards LAST. To control the value of X, spend energy on other cards first.

### 4. WRAITH FORM: FINISHER ONLY

[[cards/Wraith Form]] gives [[buffs/Intangible]] but applies permanent -1 [[buffs/Dexterity]] per turn. Three recorded deaths from playing it too early. DO NOT play until the enemy is within 5 turns of dying.

### 5. VERIFY CARD IDENTITY BEFORE PLAYING

Hand indices shift after each play. Before entering `play N`, confirm the card at index N matches your plan. Re-read hand state after each card play.

### 6. USE CARD NAMES IN turn() BATCHES — NEVER INDICES

In batched `turn()` commands, card indices shift after each play but the batch pre-computes all actions. This causes the wrong card to be played. **Confirmed fatal in Run 190:** `turn(["play 1", "play 2 0", "play 3 0", "play 4", "end"])` played Eruption+ instead of a Strike because indices shifted after the first card was played, entering Wrath with no exit and causing death.

**RULE:** Always use card names in `turn()` sequences: `turn(["play Consecrate", "play Strike 0", "play Strike 0", "play Defend", "end"])`. Card names resolve against the current hand state at the time each action executes, so they are immune to index shifting.

If two copies of the same card exist in hand and you need to play a specific one, play each card individually via `send()` with a state check between plays instead of using `turn()`.

### 7. POTION ORDERING ON KILL TURNS

On kill turns, play all deterministic damage cards FIRST. Only use random-outcome potions (Distilled Chaos, Gambler's Brew) AFTER all known-value plays are exhausted — or never.

**Rationale:** If the kill is already in hand with deterministic cards, random effects are unnecessary and can only cause harm. If the kill is NOT in hand, playing deterministic damage first reduces the enemy to minimum HP, making the random effect more likely to finish the job and less costly if it fails.

**Confirmed fatal in Run 193:** Player used Distilled Chaos BEFORE playing Smite and Strike, which together were exactly lethal. Distilled Chaos randomly played Meditate+ (ends turn, enters Calm, 0 block) against 102 incoming Hyper Beam. The kill was already in hand but the player miscalculated and thought they were 12 damage short.

**Rule:** Deterministic cards first, random effects last, on EVERY kill turn. No exceptions.

### 8. WRATH DOUBLES ALL DAMAGE

For Watcher: ALL damage is doubled in Wrath, including multi-hit cards. When a card enters Wrath (e.g., Tantrum from Calm), the stance change resolves BEFORE damage, so all hits are doubled.

Common miscalculation: Tantrum+ base is 2x5=10. In Wrath: 2x10=20. Players sometimes calculate the base damage and forget to double it, or assume "entering Wrath" means the first hit is undoubled. It is not. Every hit is doubled.

**Rule:** When in Wrath or entering Wrath, multiply EVERY damage number by 2 in kill math. Double-check the arithmetic before committing to end turn.

---

## Shockwave+ Timing Rule

Play Shockwave+ on the **FIRST ATTACK TURN** of multi-enemy fights.

- **Turn 1 is NOT always correct:** if all enemies are buffing (e.g., Cultists on turn 1), Weak is wasted on a non-attack turn.
- **Turn 2 is usually correct:** most multi-enemy fights begin attacking on turn 2.
- **NEVER save for turn 4+:** by then enemies have already accumulated Strength and you have taken unnecessary damage.
- **Priority on the first attack turn:** Shockwave+ (mass Weak + Vulnerable) > [[cards/Reaper]] (healing) > single-target damage.
