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

In batched `turn()` commands, card indices shift after each play but the batch pre-computes all actions. This causes the wrong card to be played. For example, `turn(["play 1", "play 2 0", "play 3 0", "play 4", "end"])` can play Eruption+ instead of a Strike because indices shift after the first card is played, entering Wrath with no exit and causing death.

**RULE:** Always use card names in `turn()` sequences: `turn(["play Consecrate", "play Strike 0", "play Strike 0", "play Defend", "end"])`. Card names resolve against the current hand state at the time each action executes, so they are immune to index shifting.

If two copies of the same card exist in hand and you need to play a specific one, play each card individually via `send()` with a state check between plays instead of using `turn()`.

### 7. POTION ORDERING ON KILL TURNS

On kill turns, play all deterministic damage cards FIRST. Only use random-outcome potions (Distilled Chaos, Gambler's Brew) AFTER all known-value plays are exhausted — or never.

**Rationale:** If the kill is already in hand with deterministic cards, random effects are unnecessary and can only cause harm. If the kill is NOT in hand, playing deterministic damage first reduces the enemy to minimum HP, making the random effect more likely to finish the job and less costly if it fails.

Example: using Distilled Chaos BEFORE playing Smite and Strike (which together were exactly lethal) lets Distilled Chaos randomly play Meditate+ (ends turn, enters Calm, 0 block) against 102 incoming Hyper Beam — death, even though the kill was already in hand. The miscalculation was believing they were 12 damage short.

**Rule:** Deterministic cards first, random effects last, on EVERY kill turn. No exceptions.

### 8. VERIFY DEBUFF TYPE: VULNERABLE IS NOT WEAK

Thunderclap applies [[debuffs/Vulnerable]] (target takes 50% MORE damage). It does NOT reduce enemy damage. Vulnerable makes the TARGET take more damage from attacks -- it is an offensive amplifier, not a defensive tool.

**Ironclad Weak sources (reduce enemy damage dealt by 25%):**
- [[cards/Intimidate]] (mass Weak, exhausts, 0E)
- [[cards/Clothesline]] (single target Weak, 2E)
- [[cards/Shockwave]] (mass Weak + Vulnerable, exhausts, 2E)
- [[cards/Uppercut]] (single target Weak + Vulnerable, 2E)

**Ironclad Vulnerable sources (target takes 50% more damage from attacks):**
- [[cards/Bash]] (single target Vulnerable, 2E)
- [[cards/Thunderclap]] (mass Vulnerable, 1E)
- [[cards/Shockwave]] (mass Weak + Vulnerable, exhausts, 2E)
- [[cards/Uppercut]] (single target Weak + Vulnerable, 2E)

**CRITICAL:** Thunderclap and Intimidate are both mass debuff cards, but they apply OPPOSITE effects. Playing Thunderclap does NOT reduce incoming damage. If the survival plan depends on reducing enemy damage, you need a Weak source (Intimidate, Clothesline, Shockwave), NOT Thunderclap. Treating Thunderclap as Weak miscalculates incoming — it applies Vulnerable, not Weak, so enemy damage is NOT reduced. If your block plan relied on a 25% reduction, actual incoming is the full 30 (not 21) and you take the full hit.

### 9. WRATH DOUBLES DAMAGE — BUT NOT THE HIT THAT ENTERS WRATH

For Watcher: while you are **already in Wrath**, your attacks deal double damage (and you take double from attacks). But the card that **enters** Wrath does NOT double its own hit — it deals its damage first and enters Wrath after, so that hit lands before Wrath is active.

- **Eruption** deals its 9 at base (not 18); **Eruption+** is also 9.
- **Tantrum** deals `magicNumber x base` at base, THEN enters Wrath. Tantrum+ from Calm = 3x4 = 12 (NOT 24) on the turn it enters.
- Only attacks played **after** you are already in Wrath are doubled — subsequent cards the same turn, or any attack on a later turn while Wrath persists. (A second copy of Tantrum, or any Strike, played after you're in Wrath IS doubled.)

**Rule:** In kill math, the entering card's hit is base — do NOT double the Eruption/Tantrum that enters Wrath. DO double every attack you play after it while Wrath is active. Double-check the arithmetic before committing to end turn.

---

## Shockwave+ Timing Rule

Play Shockwave+ on the **FIRST ATTACK TURN** of multi-enemy fights.

- **Turn 1 is NOT always correct:** if all enemies are buffing (e.g., Cultists on turn 1), Weak is wasted on a non-attack turn.
- **Turn 2 is usually correct:** most multi-enemy fights begin attacking on turn 2.
- **NEVER save for turn 4+:** by then enemies have already accumulated Strength and you have taken unnecessary damage.
- **Priority on the first attack turn:** Shockwave+ (mass Weak + Vulnerable) > [[cards/Reaper]] (healing) > single-target damage.

---

## Potion Timing Rule

**Do not hoard potions until death.** Two of three runs in audit 216-218 died with usable potions that would have changed the outcome.

**Trigger for potion evaluation:** If ANY of these conditions are true, evaluate potion use THIS TURN:
1. **Turn 5+ in a tough fight** (elite, multi-enemy, hard-scaler) and potions are held.
2. **HP below 30%** in any fight.
3. **A damage potion would kill an enemy** that is generating status cards (Sentries generating Dazed, enemies applying debuffs). Killing the source earlier prevents compound damage from clogged draws.
4. **A Strength/damage potion would accelerate a kill by 2+ turns.** Faster kills mean fewer incoming damage turns.

**Anti-pattern: "saving for later."** There is no later if you die. A Fire Potion used on Turn 5 to kill a Sentry prevents 3+ turns of Dazed generation and incoming damage. A Strength Potion used mid-fight accelerates kills and reduces total damage taken. The value of a potion in the CURRENT fight is almost always higher than its speculative value in a FUTURE fight.

**Exception:** Fairy in a Bottle and potions specifically needed for the next boss fight (within 1-2 floors). These may be worth holding. All other potions should be evaluated for immediate use when the trigger conditions are met.
