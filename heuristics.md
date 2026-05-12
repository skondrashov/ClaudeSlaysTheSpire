# Heuristic Rework (Pending)

Collected 2026-05-09. These are human-provided heuristics that the self-learning loop has not discovered after 130+ runs. The goal is NOT to dump these as rules — it's to find ways of thinking about the game that make these heuristics discoverable. But for A0, encoding them directly may be sufficient.

## The List

### 1. HP is an act-level resource
Damage taken in a hallway fight is permanent until a rest site. There is no "I can afford to take damage" in hallway fights — the goal is always zero damage taken. The player currently plays differently at high HP vs low HP, but this is wrong. 8 damage at 80 HP is exactly as bad as 8 damage at 20 HP.

**Free spending exceptions:**
- Burning Blood refunds 6 HP per fight (only "free" if at max HP)
- Boss fights (HP refills via healing/rest after)
- Pantograph (25 HP before boss if equipped)

### 2. Full block is the default combat algorithm
The goal every turn in a hallway fight is **zero damage taken**. "Full block" doesn't just mean "play block cards" — it means finding ANY path to taking zero damage. On A0, you should almost never voluntarily take damage in hallway fights.

**The full block flowchart:**
1. What's total incoming damage this turn?
2. Can I **kill** any attacking enemies? What incoming remains after?
3. Can I **block** whatever remains? (block cards, Weak on attacker, etc.)
4. If kill + block = zero damage → **best line** (took zero AND removed future damage)
5. If pure block = zero damage → do that
6. If neither achieves zero → minimize damage, consider potions

Killing an attacker IS a form of blocking — it removes their damage this turn AND every future turn. Kill + partial block is almost always better than pure block when both achieve zero damage taken. The player must enumerate alternatives, not just pick one plan.

**The pipeline problem:** The player currently picks ONE plan and executes. It doesn't consider "what if I kill that enemy instead of blocking?" Good play requires evaluating multiple paths to zero damage and choosing the one with the best side effects (enemy killed, damage dealt, cards drawn).

**Exceptions (where you spend HP intentionally):**
- Boss fights (HP is free to spend — kill fast)
- Hard-scaling enemies (Cultists with Ritual) where kill speed prevents more total damage than blocking
- At full HP, up to 6 damage is "free" (Burning Blood)

### 3. Full act pathing before the first fight
Before choosing your first room in each act, read the entire map. Count elites, shops, and campfires on every viable route. You should know how many of each you're hitting before floor 1. Plan the act as a route, not room-by-room.

### 4. Act 1 card evaluation is a tier list, not reasoning
The starting deck is (nearly) identical every run (adjusted for Neow). An experienced player doesn't reason about Act 1 picks — they know the tier list. The core shaping constraint: "take attacks so you don't die to Gremlin Nob."

Categories: must-takes, never-takes, and a narrow band where judgment matters. The player should not be reasoning from first principles for Act 1 card rewards.

### 5. Draft for known encounters
You can see the boss from the start. You know which elites exist in each act. Evaluate cards against fights you're guaranteed or likely to face, not generically.

Examples:
- Status-synergy cards (Evolve, Fire Breathing) trivialize Slime Boss (floods deck with Slimed)
- Attacks for Gremlin Nob (punishes Skills)
- This is a whole category of knowledge: "card X counters fight Y"

---

## Meta-Questions

- How do we differentiate between injected human heuristics and self-learned knowledge?
- The holy grail: ways of thinking that make these heuristics discoverable
- Humans don't derive most of this through reasoning — we steal from watching, asking, looking up, other games, and experiments
- The analyst/strategist loop does pure self-discovery, which may never arrive at certain insights
- For A0, direct encoding may be sufficient. For higher ascensions, the thinking frameworks matter more.
