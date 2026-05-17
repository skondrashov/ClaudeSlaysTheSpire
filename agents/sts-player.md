# STS Player — Slay the Spire Game Framework

How to play Slay the Spire. Combat framework, turn planning, map routing, tool interface. Applies to all characters.

## Setup

```python
import sys
sys.path.insert(0, r"C:\Users\tkond\projects\autoplay\games\sts1")
from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, plan, reason, think, deck
```

Call `state()` to see the game. One decision at a time outside combat. In combat, plan your full turn, then execute with `turn()`.

## Combat: The Full Block Algorithm

**The default goal every turn in a hallway fight is ZERO DAMAGE TAKEN.** Not "minimize damage." Not "how much can I afford." Zero. HP lost in a hallway fight is permanent until a rest site. 8 damage at 80 HP is exactly as bad as 8 damage at 20 HP — both bring you 8 HP closer to death. Your HP level does NOT change how you play combat. You always full block.

### The Full Block Flowchart (execute every turn)

```
STEP 1: Read total incoming damage this turn.
        (Check intents. Sum all attacking enemies. Apply Weak if on them.)

STEP 2: Enumerate ALL paths to zero damage taken:
        PATH A — Kill attackers + block remainder
                 (Killing an attacker removes their damage THIS turn AND every future turn.
                  This is the best form of "blocking" when achievable.)
        PATH B — Pure block (block cards, Weak on attacker, etc.)
        PATH C — Debuff + block (apply Weak to reduce incoming, block the rest)
        PATH D — Potion-assisted (damage potion to kill, block potion to survive)

STEP 3: Compare paths that achieve zero damage:
        - Prefer paths that KILL enemies (removes future damage sources)
        - Among kill paths, prefer ones that also deal damage to non-attackers
        - Among pure-block paths, prefer ones with useful side effects (draw, exhaust junk)

STEP 4: If NO path achieves zero damage:
        - Minimize damage taken
        - Consider potions (an unused potion on a death screen is a strategic failure)
        - Prioritize killing the highest-damage attacker even if you take some hits

STEP 5: Execute the chosen path.
```

**The pipeline problem the player MUST avoid:** Do not pick ONE plan and execute it. Enumerate at least two paths before choosing. "I'll block everything" might be worse than "I'll kill that enemy and block the rest" even when both reach zero damage — because the kill path removes a future damage source.

### Exceptions (when you intentionally take damage)

These are the ONLY situations where taking damage in combat is acceptable:

1. **Boss fights.** HP resets via rest/heal after bosses. Spend HP freely to kill faster.
2. **Hard-scaling enemies (Ritual, Rally).** Cultists gain +3 Str/turn. Kill speed prevents more total damage than blocking. If killing one turn faster saves 15+ future damage, spend HP now.

**Everything else is a hallway fight and the default applies: zero damage taken.**

### Fight Strategy (once per combat, before your first turn)

After calling `plan()` at combat start, write a FIGHT STRATEGY before making any moves. Classify the fight type first — this determines your combat algorithm. Then **post it to the stream with `think()`**.

```
FIGHT STRATEGY — [Enemy Name]

FIGHT TYPE: [Hallway (full block) | Boss (spend HP freely) | Hard-scaler (kill speed priority)]
WIN CONDITION: How do I kill this enemy? What's my damage source?
ZERO DAMAGE PLAN: How do I take zero damage each turn? What's my block budget?
KEY CARDS: Which cards are critical for blocking AND killing?
RELIC INTERACTIONS: Which relics matter this fight?
POTION PLAN: When do I use potions? What triggers potion use?
RISKS: What can go wrong? What kills me if I'm not careful?
ESTIMATED TURNS: How long will this fight take?
```

### Turn Planning (every turn)

Do NOT play one card at a time. Plan the whole turn using the Full Block Flowchart before executing.

```
TURN N — [fight type: hallway/boss/hard-scaler]

INCOMING: [total damage from all attackers]
PATHS TO ZERO:
  A) Kill [enemy] (costs XE, removes Y incoming) + block remainder (costs ZE) → zero damage? [yes/no]
  B) Pure block (list block cards + values) → total block vs incoming → zero damage? [yes/no]
  C) [any other path]
CHOSEN PATH: [A/B/C] because [best side effects / only option / kills enemy]
PLAY: [numbered sequence]
RESULT: [block vs incoming = damage taken], [enemy HP remaining]
```

Then execute with `turn()`:
```python
turn(["play Bash Jaw Worm", "play Strike Jaw Worm", "play Defend", "end"], reason="Path A: kill Jaw Worm (11 HP, Bash 10 + Strike 6 = 16 vs 11 HP, dead) removes 11 incoming. Defend 5 blocks remaining 0. Zero damage taken.")
```

The `reason` should show the path evaluation — which paths you considered and why you chose the one you did.

### Card Names and Enemy Targeting

**ALWAYS use card names instead of card indices:**
```python
turn(["play Bash 0", "play Strike 0", "play Defend", "end"], reason="...")
```
Card names are resolved against the current hand at execution time, so they're always correct regardless of what was played before.

**Enemy targeting — use the displayed index number.** Enemy indices are absolute positions that DON'T change when other enemies die. If the display shows:
```
ENEMIES:
  [0] Byrd — HP: 25/25
  [1] Byrd — HP: 25/25
  [2] Byrd — HP: 25/25
```
And Byrd [0] dies, the remaining enemies keep their indices:
```
ENEMIES:
  [1] Byrd — HP: 20/25
  [2] Byrd — HP: 15/25
```
Target them as `play Strike 1` and `play Strike 2` — NOT 0 and 1.

**Enemy names work when enemies have distinct names:**
```python
turn(["play Bash Blue Slaver", "play Strike Red Slaver", "end"], reason="...")
```
When enemies share a name (Byrds, Cultists, etc.), use the numeric index.

### Draw Effects — CRITICAL RULE

**NEVER include cards after a draw card in a `turn()` sequence.** If any card in your hand draws cards (Backflip, Acrobatics, Shrug It Off, Pommel Strike, Battle Trance, Prepared, Offering, Dagger Throw, Cut Through Fate, etc.), it MUST be the last card before `"end"` in the sequence, or you must play it via `send()` and re-read state before continuing.

The drawn cards might be playable and change your entire plan. Pre-planning past a draw is always wrong — you're deciding to ignore cards you haven't seen yet.

**Correct — draw card ends the sequence:**
```python
turn(["play Defend", "play Backflip", "end"], reason="Block first, Backflip for block + draw. Will plan remaining cards after seeing what I draw.")
# Read new state, see drawn cards, then plan the rest
```

**WRONG — planning past a draw:**
```python
# NEVER DO THIS:
turn(["play Backflip", "play Strike 0", "play Defend", "end"], reason="...")
# You don't know what you'll draw from Backflip! The drawn cards might be better than Strike/Defend.
```

The `turn()` function will automatically stop your sequence if it detects a draw happened, but don't rely on that — plan correctly from the start.

## Outside Combat

Non-combat decisions (map, events, rewards, shops, rest sites) are made one at a time with `send()`.

### Full Act Pathing (MANDATORY at the start of each act)

Before choosing your FIRST room in each act, read the ENTIRE map. Do not path room-by-room. Plan the full act as a route.

**At act start, answer these questions and post to stream with `think()`:**

```
ACT PATHING — Act [N]

BOSS: [boss name] (visible from floor 1 — draft cards for this fight)
ROUTES: List every viable path from bottom to top. For each route, count:
  - Elites: [count] (relics, but cost HP)
  - Shops: [count] (card removal, potions, relics)
  - Campfires: [count] (upgrade or heal)
  - Unknown rooms: [count] (treat as monsters in Act 2)
CHOSEN ROUTE: [which path and why]
  - How many elites am I hitting? (1-2 is ideal in Act 1)
  - Where are my campfires relative to elites? (campfire BEFORE elite = heal/upgrade)
  - Where's my last campfire before the boss? (need one in last 2-3 floors)
DRAFT TARGETS: What cards do I need for [boss name]?
```

**Do NOT re-path from scratch every floor.** Follow your plan. Only re-route if:
- HP drops below safe thresholds for the planned path
- A relic or card fundamentally changes your strategy
- You discover the map branches differently than expected

### Card Rewards

Look up each offered card with `reason("Card Name")` before deciding. The playbook has character-specific tier lists and card evaluations. Don't reason from first principles when the playbook has an answer.

### Rest Sites
- **Upgrade (smith) is the DEFAULT action.** Only rest (heal) when HP is genuinely low enough that the next fight would kill you.
- Check `plan()` output for upgrade priorities — the playbook ranks which cards benefit most from upgrading.

### Map Pathing
- **You should already have a full act route from your Act Pathing plan.** Follow it. Only re-route when HP drops below safe thresholds or strategy changes.
- **At each floor, verify your planned route is still viable.** If HP has dropped, count forced combats remaining to the next rest site. If the path forces 2+ combats and HP is below 50%, re-route to the safest available path.
- Elites give relics but cost HP — only fight them when your act route planned for it AND HP is sufficient
- Rest sites and shops are resources — your act route should already account for them

### Events
- Read the options carefully. Many events have hidden costs or benefits.
- If you don't know an event, be cautious — say so and pick the safe option.
- Call `reason("Event Name")` to look up the event before choosing.

### Deck Review with `deck()`

Call `deck()` after any event that changes your deck composition:
- **After transform effects** (Astrolabe, etc.) — review what you got
- **After adding or removing cards** at key moments
- **After shop visits** where you bought/removed multiple cards

Post your deck assessment with `think()`.

## Potions

- Don't hoard potions forever — use them when they matter
- Potion slots are limited — if you're full and see a potion reward, consider using one
- Damage potions are best against elites and bosses
- Block potions can save a rest (heal instead of resting because you'll survive with the potion)

## Commands

```
state()                          — Read current game state
deck()                           — View full deck (use after transforms, adds, removes)
plan()                           — Load strategic context (auto-detects combat vs act mode)
think(reasoning, label)          — Post your strategic analysis to the stream overlay
reason("topic")                  — Look up a specific playbook entry
send(command, reason="...")      — Single action with reasoning
turn([actions], reason="...")    — Full combat turn as batch
play(card, target)               — Play card (1-indexed) at target (0-indexed)
end()                            — End turn
choose(option)                   — Choose by index or name
proceed()                        — Confirm/proceed
skip()                           — Skip/cancel/leave
potion_use(slot, target)         — Use potion
potion_discard(slot)             — Discard potion
```

Use card names and enemy names when possible. Card indices are 1-indexed, enemy indices are 0-indexed absolute (don't shift when enemies die).

**ALWAYS provide `reason=` to `send()` and `turn()` calls.** This is critical for the stream overlay — viewers need to see WHY each decision is made.
