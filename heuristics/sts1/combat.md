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

Before every turn, verify these items. Game mechanics are in [[combat]] (ontology) — this checklist catches common reasoning errors.

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

---

## Shockwave+ Timing Rule

Play Shockwave+ on the **FIRST ATTACK TURN** of multi-enemy fights.

- **Turn 1 is NOT always correct:** if all enemies are buffing (e.g., Cultists on turn 1), Weak is wasted on a non-attack turn.
- **Turn 2 is usually correct:** most multi-enemy fights begin attacking on turn 2.
- **NEVER save for turn 4+:** by then enemies have already accumulated Strength and you have taken unnecessary damage.
- **Priority on the first attack turn:** Shockwave+ (mass Weak + Vulnerable) > [[cards/Reaper]] (healing) > single-target damage.
