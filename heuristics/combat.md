# Combat Execution

## The Full Block Algorithm

**The default goal every turn in a hallway fight is ZERO DAMAGE TAKEN.** Not "minimize damage." Zero. HP lost in a hallway fight is permanent until a rest site. 8 damage at 80 HP is exactly as bad as 8 damage at 20 HP.

Every turn:

1. Read total incoming damage (sum all attacking enemies, apply Weak if on them).
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

**NEVER include cards after a draw card in a `turn()` sequence.** If a card draws (Backflip, Shrug It Off, Pommel Strike, Battle Trance, Offering, etc.), it MUST be the last card before `"end"`. Play it via `send()` and re-read state before continuing.

---

## Combat Arithmetic Checklist

Before every turn, verify each of these eight items.

### 1. WHO has Weak?

- **Weak on ENEMY** = their attacks deal 25% less damage; YOUR damage is UNAFFECTED.
- **Weak on YOU** = your attacks deal 25% less damage.
- NEVER apply the 0.75 multiplier to your own damage when the enemy is the one who is Weakened.

### 2. Am I using UPGRADED values?

Check the + suffix on every card. Common errors:

- Shrug It Off+ = 11 block (not 8)
- Flame Barrier+ = 16 block AND 6 counter-damage
- Armaments+ = 5 block AND upgrades ALL cards in hand
- Bash+ = 10 damage, 3 Vulnerable (not 2)
- Intimidate+ = 2 Weak (not 1)
- Spot Weakness = +3 Strength unupgraded / +4 Strength upgraded

### 3. Does my Strength reset?

- **Inflame, Spot Weakness, Demon Form:** per-combat only, resets between fights.
- **Vajra (relic):** permanent, persists across combats.
- **Strength Potion:** temporary, lasts one combat.
- **Rampage counter:** also resets between fights.
- NEVER carry Strength values from a previous fight into the current one.

### 4. VERIFY KILL MATH BEFORE ENDING TURN

On kill turns, NEVER include `end` in the same command as the final attack. Play the attack, verify the kill, THEN end the turn separately.

**Example fatal error:** played Iron Wave (13 damage) against a 20 HP Hexaghost and submitted `end` in the same command, when Headbutt (17 damage) was still in hand with 2 energy remaining.

### 5. X-COST CARDS USE ALL REMAINING ENERGY

X-cost cards (Malaise, Whirlwind, Skewer) consume ALL remaining energy automatically. Always PLAY THEM LAST. To control the value of X, spend energy on other cards first.

**Example fatal error:** intended Malaise X=1 but played it first with 4 energy available. It consumed all energy, leaving zero block, and died.

### 6. FOSSILIZED HELIX / BUFFER: BLOCK IS CONSUMED FIRST

Fossilized Helix and Buffer prevent HP loss, not damage. Block is consumed BEFORE the prevention check. Against multi-hit attacks, this means Block is depleted by hit 1 (Helix/Buffer catches overflow), then hits 2+ land with no Block remaining.

**Wrong:** "Helix absorbs hit 1 entirely, my 5 Block handles hit 2." (Overestimates survivability)
**Right:** "Hit 1 (6) eats my 5 Block, Helix catches the 1 overflow. Hit 2 (6) lands in full." (5 HP worse)

When calculating damage against multi-hit enemies with Helix/Buffer, assume Block is gone after hit 1.

### 7. WRAITH FORM: DO NOT PLAY UNTIL ENEMY IS WITHIN 5 TURNS OF DYING

Wraith Form gives Intangible but applies a permanent -1 Dexterity per turn. Three recorded deaths from playing it too early. Estimate the number of turns remaining before playing. Wraith Form is a FINISHER, not an opener.

### 8. VERIFY CARD IDENTITY BEFORE PLAYING

Before entering a `play N` command, confirm the card at index N matches the card in your plan. Hand indices shift after each play. Especially dangerous for 2E cards that look similar in reasoning (Bash vs Shockwave are both 2E and both target enemies, but Bash is single-target Attack damage while Shockwave is mass Weak+Vulnerable). Playing Bash when you mean Shockwave wastes 2E on minimal damage instead of critical debuffs.

**Process:** After each card play, re-read the hand state. The card you intend to play next may have shifted index.

---

## Shockwave+ Timing Rule

Play Shockwave+ on the **FIRST ATTACK TURN** of multi-enemy fights.

- **Turn 1 is NOT always correct:** if all enemies are buffing (e.g., Cultists on turn 1), Weak is wasted on a non-attack turn.
- **Turn 2 is usually correct:** most multi-enemy fights begin attacking on turn 2.
- **NEVER save for turn 4+:** by then enemies have already accumulated Strength and you have taken unnecessary damage.
- **Priority on the first attack turn:** Shockwave+ (mass Weak + Vulnerable) > Reaper (healing) > single-target damage.
