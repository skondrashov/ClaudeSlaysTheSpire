# Goal: Play a Run

Play the game. Make one decision at a time. Load knowledge with `plan()` and `reason()` before decisions. Post reasoning with `think()`.

See [[interface/tools]] for the full tool reference. Setup:

```python
import sys
sys.path.insert(0, r"C:\Users\tkond\projects\autoplay\games\sts1")
from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, plan, reason, think, deck
```

Call `state()` to see the game. One decision at a time outside combat. In combat, plan your full turn, then execute with `turn()`.

## Combat: The Full Block Algorithm

**The default goal every turn in a hallway fight is ZERO DAMAGE TAKEN.** Not "minimize damage." Zero. HP lost in a hallway fight is permanent until a rest site. 8 damage at 80 HP is exactly as bad as 8 damage at 20 HP. Your HP level does NOT change how you play combat. You always full block.

### The Full Block Flowchart (execute every turn)

```
STEP 1: Read total incoming damage this turn.
        (Check intents. Sum all attacking enemies. Apply Weak if on them.)

STEP 2: Enumerate ALL paths to zero damage taken:
        PATH A — Kill attackers + block remainder
        PATH B — Pure block (block cards, Weak on attacker, etc.)
        PATH C — Debuff + block (apply Weak to reduce incoming, block the rest)
        PATH D — Potion-assisted (damage potion to kill, block potion to survive)

STEP 3: Compare paths that achieve zero damage:
        - Prefer paths that KILL enemies (removes future damage sources)
        - Among kill paths, prefer ones that also deal damage to non-attackers
        - Among pure-block paths, prefer ones with useful side effects

STEP 4: If NO path achieves zero damage:
        - Minimize damage taken
        - Consider potions (an unused potion on a death screen is a strategic failure)
        - Prioritize killing the highest-damage attacker

STEP 5: Execute the chosen path.
```

**Enumerate at least two paths before choosing.** Do not pick ONE plan and execute it.

### Exceptions (when you intentionally take damage)

1. **Boss fights.** HP resets via rest/heal after bosses. Spend HP freely to kill faster.
2. **Hard-scaling enemies (Ritual, Rally).** Kill speed prevents more total damage than blocking.

**Everything else is a hallway fight and the default applies: zero damage taken.**

### Fight Strategy (once per combat, before first turn)

After calling `plan()`, write a FIGHT STRATEGY and post to stream with `think()`:

```
FIGHT STRATEGY — [Enemy Name]

FIGHT TYPE: [Hallway (full block) | Boss (spend HP freely) | Hard-scaler (kill speed priority)]
WIN CONDITION: How do I kill this enemy?
ZERO DAMAGE PLAN: How do I take zero damage each turn?
KEY CARDS: Which cards are critical?
POTION PLAN: When do I use potions?
RISKS: What can go wrong?
```

### Turn Planning (every turn)

Plan the whole turn before executing:

```
TURN N — [fight type]

INCOMING: [total damage from all attackers]
PATHS TO ZERO:
  A) Kill [enemy] (costs XE) + block remainder → zero damage? [yes/no]
  B) Pure block → total block vs incoming → zero damage? [yes/no]
CHOSEN PATH: [A/B] because [reason]
PLAY: [numbered sequence]
```

Execute with `turn()`:
```python
turn(["play Bash Jaw Worm", "play Strike Jaw Worm", "play Defend", "end"], reason="Path A: kill Jaw Worm, Defend blocks remaining 0. Zero damage.")
```

### Card Names and Enemy Targeting

**Use card names:** `turn(["play Bash 0", "play Strike 0", "play Defend", "end"], reason="...")`

**Enemy targeting — use displayed index number.** Indices are absolute (don't shift when enemies die). When enemies share a name, use numeric index.

### Draw Effects — CRITICAL RULE

**NEVER include cards after a draw card in a `turn()` sequence.** If a card draws (Backflip, Shrug It Off, Pommel Strike, Battle Trance, Offering, etc.), it MUST be the last card before `"end"`. Play it via `send()` and re-read state before continuing.

## Outside Combat

### Full Act Pathing (MANDATORY at each act start)

Before choosing your FIRST room, read the ENTIRE map. Plan the full act as a route.

```
ACT PATHING — Act [N]

BOSS: [boss name]
ROUTES: [list viable paths with elite/shop/campfire/unknown counts]
CHOSEN ROUTE: [which path and why]
DRAFT TARGETS: What cards do I need for [boss name]?
```

**Follow your plan.** Only re-route if HP drops below safe thresholds.

### Card Rewards

Look up each offered card with `reason("Card Name")` before deciding.

### Rest Sites
- **Upgrade (smith) is the DEFAULT action.** Only rest when HP is genuinely low enough that the next fight would kill you.

### Events
- Call `reason("Event Name")` to look up the event before choosing.
- If you don't know an event, be cautious — say so and pick the safe option.

### Deck Review with `deck()`

Call `deck()` after events that change your deck (transforms, adds, removes, shop visits). Post assessment with `think()`.

## Potions

- Don't hoard potions forever — use them when they matter
- If slots are full and you see a potion reward, consider using one
- Damage potions are best against elites and bosses
- Block potions can save a rest

## When to Load Knowledge

| Moment | Action |
|--------|--------|
| Start of each act | `plan()` → `think()` |
| Start of each combat | `plan()` → `think()` |
| Before boss fights | `plan()` → `think()` |
| Card rewards | `reason("Card Name")` for each option |
| Events | `reason("Event Name")` |
| Shop browsing | `reason("Item Name")` for items considered |
| Unfamiliar mechanic | `reason("mechanic name")` |

## Run End

When the run ends (GAME_OVER screen), proceed through it and STOP. Report:
- Victory or defeat, floor reached
- What went well, what went wrong
- Knowledge gaps encountered
