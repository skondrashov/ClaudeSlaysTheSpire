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
If you can block all incoming damage this turn, do it. Attack with leftover energy only. On A0, you should almost never voluntarily take damage in hallway fights.

**Exceptions:**
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
