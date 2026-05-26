# The Compendium: A Knowledge Graph Architecture for Autonomous Decision-Making Agents

Design document for autoplay's next-generation knowledge system. This replaces the current layered-prompt + scripted-loading architecture with an agent-driven knowledge graph that the agent navigates on its own terms.

The architecture described here is not specific to card games, or games at all. It is an architecture for any system where an autonomous agent must: observe state, decide what knowledge it needs, load it, decide an action, observe the result, and learn. Games are the proving ground — but the pattern generalizes to any domain with sequential decisions and a growing knowledge base.

---

## Table of Contents

1. [The Problem](#the-problem)
2. [The Current Architecture](#the-current-architecture)
3. [The Compendium Architecture](#the-compendium-architecture)
4. [How Lookup Works](#how-lookup-works)
5. [Entry Design](#entry-design)
6. [The Knowledge Graph](#the-knowledge-graph)
7. [Recursive Loading](#recursive-loading)
8. [The Agent Prompt](#the-agent-prompt)
9. [Analyst and Strategist Roles](#analyst-and-strategist-roles)
10. [Testing Generalizability: STS vs. Balatro](#testing-generalizability-sts-vs-balatro)
11. [Migration Path](#migration-path)
12. [Open Questions and Honest Answers](#open-questions-and-honest-answers)
13. [Why This Matters](#why-this-matters)

---

## The Problem

The autoplay project has AI agents make sequential decisions in complex environments — Slay the Spire, Balatro, ARC-AGI, and eventually others. The agents learn from experience: an analyst reviews each session and updates a knowledge base, a strategist periodically restructures it, and the decision-making agent uses it to improve over time.

This works. Six STS wins in 176 runs. Balatro scaling from Ante 3 failures to consistent Ante 6 clears. The system is learning. But the architecture has five structural problems that will prevent it from scaling further.

### Problem 1: Knowledge baked into identity

The agent prompt is assembled from layer files that mix behavioral directives with domain knowledge. In STS, the Full Block Algorithm appears alongside humility instructions. In Balatro, the scoring formula sits next to "express uncertainty honestly." These are fundamentally different things: one is a behavioral directive that persists across all domains, the other is domain-specific knowledge that should live alongside joker entries and enemy patterns.

The consequence: there is no principled answer to "should this go in the prompt or the knowledge base?" The boundary between agent and knowledge is undefined. The STS prompt is 236 lines and growing. The Balatro prompt has the same problem — scoring mechanics, shop decision frameworks, and joker evaluation heuristics all live in the identity prompt because removing them causes regressions.

### Problem 2: Script-driven knowledge loading

A Python script decides what knowledge the agent needs based on state:

In STS, `plan()` loads enemy files for current enemies, card files for the current hand, and relic files. But it can't load status effects the agent sees, cross-references between relics and enemies (Brimstone + Book of Stabbing), or strategic concepts about when to deviate from the standard algorithm.

In Balatro, knowledge loading is even more ad hoc — the playbook README describes a boot protocol, but there's no equivalent of `plan()`. The agent loads the full playbook at session start and hopes it covers what's needed. When the agent faces The Needle (must beat blind in one hand) and doesn't know to prioritize high-chip hands over mult-scaling, nothing loads that knowledge on demand.

Every new category of relevant knowledge requires modifying Python code. The script becomes a bottleneck — an ever-expanding attempt to anticipate what the agent might need, implemented in a language that can't reason about relevance.

### Problem 3: Knowledge lives in two places

Some knowledge is in the prompt (algorithms, frameworks, evaluation heuristics). Other knowledge is in the playbook (individual entities, strategy principles). The analyst can update the playbook but not the prompt. This creates a coherence problem.

In STS: the strategy in `sts-player.md` was written at run ~50. The strategy in `playbook/strategy.md` has been updated through 176 runs. They sometimes contradict each other.

In Balatro: the scoring formula in the prompt says "Chips × Mult" but the detailed evaluation order (left-to-right joker triggering, additive mult before xMult) lives in `playbook/mechanics.md`. The agent gets two sources of truth with no reconciliation mechanism.

### Problem 4: Domain switching requires prompt surgery

To switch characters within STS, the orchestrator swaps a layer file. To switch from STS to Balatro entirely, it replaces the domain-specific prompt. But domain-specific prompts contain both domain knowledge (the scoring formula, the combat algorithm) and domain-agnostic patterns (the "enumerate options before choosing" principle, the "consider opportunity cost" heuristic). There's no way to preserve general insights while replacing domain-specific ones.

Each game independently invented its own knowledge-loading patterns. Balatro has a playbook README with a boot protocol. ARC-AGI has a `get_system_prompt()` that concatenates files. Each reinvented the wheel because the architecture doesn't provide a shared knowledge-loading abstraction.

### Problem 5: Prompt growth is unbounded

Every regression adds text to the prompt. In STS: missed a kill because of arithmetic → add the combat arithmetic checklist. Played past a draw card → add the draw effect rule. In Balatro: misordered jokers → add the left-to-right evaluation reminder. Used a Tarot card on the wrong card → add the "check enhancement interactions first" rule.

Each addition is justified — removing it causes a regression. But there's no mechanism for knowledge to graduate from the prompt into the knowledge base. The prompt becomes a write-only medium.

---

## The Current Architecture

For reference, here's how knowledge flows in the STS and Balatro systems today.

### STS: At session start

```
player-personality.md      (20 lines — LLM behavior)
  + player-core.md         (60 lines — agent framework)
  + sts-player.md          (236 lines — STS framework + commands)
  + characters/watcher.md  (varies — character mechanics)
  = ~400-500 lines of system prompt
```

During gameplay, the agent has `plan()` (scripted context loading), `reason(topic)` (single-entry lookup), and `think()` (stream communication). The `plan()` function loads enemy files, card files, and relic files based on game state. It cannot load status effects, cross-cutting concerns, or strategic concepts.

### Balatro: At session start

```
player.md                  (agent behavior + Balatro-specific framework)
  + playbook/README.md     (boot protocol + playbook overview)
  = ~300 lines of system prompt, plus full playbook loaded at boot
```

During gameplay, the agent has no equivalent of `plan()`. It reads the full playbook at session start and relies on that static context for all decisions. When facing an unfamiliar joker interaction or boss blind constraint, there's no on-demand lookup.

### What works across both

The per-entity file structure is excellent. STS has 200+ individual files for cards, enemies, bosses, events, relics, and potions. Balatro has files for jokers, consumables, blinds, bosses, and mechanics. Each entity is its own markdown file, independently maintainable. The analyst can surgically update any entry.

The three-agent loop (player → analyst → strategist) produces compounding improvement in both games. The analyst catches prediction errors; the strategist catches systemic patterns. Learning is real and measurable.

### What doesn't work across both

The knowledge-loading mechanism is game-specific and inflexible. Both games suffer from the same structural issues — knowledge split between prompt and playbook, loading mechanisms that can't adapt, prompts that grow without bound — but each has its own implementation of these problems. There's no shared solution.

---

## The Compendium Architecture

Replace the multi-layer prompt + scripted loading with a single knowledge store and a single lookup mechanism that the agent drives. This applies identically regardless of the decision domain.

### Core principles

**1. All knowledge lives in the compendium.**

There is no "prompt knowledge" separate from "playbook knowledge." The STS combat algorithm, the Balatro scoring formula, character mechanics, joker interactions, strategic frameworks — everything that is currently split between prompt files and playbook directories merges into the compendium. The only thing in the agent prompt is how to be an agent.

**2. The agent decides what to load.**

No Python script anticipates what's relevant. The agent reads the current state, decides what it needs to know, and requests it. If a STS agent sees Gremlin Nob, it requests the Gremlin Nob entry. If a Balatro agent sees The Needle as the upcoming boss blind, it requests The Needle entry. If either agent is unsure about a mechanic, it asks.

**3. Entries reference other entries by name.**

The knowledge graph is implicit in the text. A STS entry for "Wrath" mentions Eruption, Vigilance, Calm, and "end-of-turn stance safety." A Balatro entry for "Blueprint" mentions "joker copying," "left-to-right evaluation," and specific jokers worth copying. The agent reads these names and can choose to look them up. No formal link syntax — just natural language references.

**4. The compendium grows from experience.**

The analyst creates and updates entries after each session. The strategist restructures entries periodically. The compendium is the cumulative experience of every session, encoded as navigable knowledge. This applies whether the sessions are STS runs, Balatro runs, code reviews, or diagnostic tasks.

**5. The lookup mechanism is domain-agnostic.**

`lookup("Gremlin Nob")` and `lookup("Blueprint joker")` and `lookup("fractal symmetry")` and `lookup("differential diagnosis: chest pain")` all use the same function. Different domains have different entries, but the mechanism is identical.

---

## How Lookup Works

### The function signature

```python
def lookup(*topics: str) -> str:
    """Look up one or more compendium entries by topic.
    
    Args:
        *topics: One or more topic strings. Each is matched against 
                 all compendium entries using fuzzy matching.
    
    Returns:
        All matching entries concatenated, with headers indicating
        where each was found. If no match, returns a helpful message
        suggesting alternatives.
    
    Examples:
        # STS
        lookup("Gremlin Nob")
        lookup("Eruption", "Wrath", "Flurry of Blows")
        lookup("combat fundamentals")
        
        # Balatro
        lookup("Blueprint")
        lookup("scoring formula", "left-to-right evaluation")
        lookup("The Needle", "high-chip hands")
    """
```

### Search mechanics

The lookup function searches across ALL compendium directories for the current domain. The directory structure differs by domain but the mechanism is identical:

**STS compendium:**
```
compendium/
  cards/          # Individual card entries
  enemies/        # Individual enemy entries
  bosses/         # Boss entries
  events/         # Event entries
  relics/         # Relic entries
  potions/        # Potion entries
  effects/        # Status effects (Vulnerable, Weak, etc.)
  characters/     # Character overviews
  concepts/       # Strategic concepts (Full Block Algorithm, act pathing)
  mechanics/      # Game mechanics (damage calculation, stance rules)
  meta/           # Navigation entries (game context, "start here")
```

**Balatro compendium:**
```
compendium/
  jokers/         # Individual joker entries
  consumables/    # Tarots, planets, spectrals
  blinds/         # Boss blind entries
  hand-types/     # Flush, Full House, etc. with scoring details
  vouchers/       # Voucher entries
  concepts/       # Strategic concepts (scaling checkpoints, build archetypes)
  mechanics/      # Scoring formula, evaluation order, enhancement rules
  meta/           # Navigation entries (game context, "start here")
```

Matching logic (in priority order):

1. **Exact filename match** — `_name_to_filename(topic) + ".md"` in any directory
2. **Substring match** — topic appears in any filename
3. **Heading match** — topic appears as a `#` heading inside any file
4. **Fuzzy match** — Levenshtein distance or similar, for typos ("Gremlen Nob", "Blueprnt")

When multiple entries match, return all of them. When nothing matches, return a "not found" message listing the directories and suggesting the agent try a different name.

### Batching

The agent often needs multiple entries at once. Rather than calling lookup five times:

```python
# STS: Loading for a combat encounter
lookup("Gremlin Nob", "Sentry", "Vulnerable", "Strike", "Bash")

# Balatro: Loading for a hand decision
lookup("Blueprint", "Hack", "scoring formula", "The Needle")
```

This returns all entries in one call, reducing tool call overhead. The current STS `plan()` function already does this batching — the difference is that the agent chooses the topics, not a script.

### What lookup replaces

| Current tool | Compendium equivalent |
|---|---|
| STS `plan()` in combat mode | Agent calls `lookup()` with enemy names, card names, relevant effects |
| STS `plan()` in act mode | Agent calls `lookup()` with boss name, strategy concepts, character overview |
| STS `reason(topic)` | `lookup(topic)` — identical interface, broader search scope |
| Balatro full-playbook boot load | Agent calls `lookup()` with what it needs per decision point |

The `plan()` function disappears entirely. The Balatro boot protocol disappears. The agent does what scripts did, but with the ability to include or exclude topics based on actual relevance.

---

## Entry Design

### What makes a good compendium entry

A compendium entry should be:

1. **Self-contained** — Readable without loading other entries. A reader should understand the core information from this entry alone.
2. **Cross-referenced** — Mentions related entries by name so the agent can follow the graph if it wants more depth.
3. **Actionable** — Tells the agent what to DO, not just what things ARE. "Vulnerable: 50% more damage" is facts. "Apply Vulnerable before your big attacks, not after" is actionable. "Blueprint copies the joker to its right" is facts. "Place Blueprint to the left of your strongest xMult joker" is actionable.
4. **Sized for context** — Short enough that loading 5-10 entries at once doesn't overwhelm the context window. An entity entry should be 5-15 lines. A strategic concept might be 30-60 lines. A boss entry might be 40-80 lines.

### Entry format

No rigid template, but a consistent structure helps the agent parse entries quickly:

```markdown
# Entry Name (Category, Context)

One-line summary of what this is and what to do about it.

[Core information — mechanics, stats, behavior]

[Decision points — when to use, when to avoid, key interactions]

Related: [names of related entries the agent might want to look up]
```

### Example: STS card entry (existing, already good)

```markdown
# Eruption (Watcher Starter Attack, 2E / 1E+)

Base: 9 damage, enter Wrath stance. Upgraded: 1E cost (from 2E).

Eruption is the Watcher's primary Wrath entry card. Playing it switches 
you from your current stance to Wrath, where all attack damage is doubled
but all incoming damage is also doubled.

## Key Interactions

- Exits Calm when played in Calm: Leaving Calm grants +2 energy. With 
  upgraded Eruption+ (1E), the Calm exit energy gain makes it effectively 
  free: spend 1E, gain 2E from Calm = net +1E. This is the core Watcher 
  energy loop.
- Enters Wrath: All attacks deal double damage, but all incoming is also 
  doubled. Do NOT end your turn in Wrath unless you can survive doubled 
  incoming damage.
- Stance change triggers: Entering Wrath returns Flurry of Blows from 
  discard to hand.

## Upgrade Priority

High. Reducing cost from 2E to 1E doubles the efficiency of the Calm 
energy loop.

## When NOT to Play

- Do NOT play if you cannot exit Wrath this turn and the enemy is attacking.
- Hexaghost Turn 1: Do NOT enter Wrath. Turn 2 Divider would be doubled.

Related: Wrath, Calm, Flurry of Blows, Vigilance, stance cycling
```

### Example: Balatro joker entry

```markdown
# Blueprint (Uncommon Joker, $10)

Copies the ability of the joker to its right. Evaluated in left-to-right 
order, so Blueprint fires at its own position with the copied ability.

## Key Interactions

- Copies the joker IMMEDIATELY to its right. If that slot is empty, 
  Blueprint does nothing.
- The copy happens at evaluation time, not at purchase time. Reordering 
  jokers changes what Blueprint copies.
- If Blueprint copies an xMult joker (like Ride the Bus), it adds a 
  second instance of that xMult. Two xMult triggers compound 
  multiplicatively.
- If Blueprint copies another Blueprint (chained), the second Blueprint 
  copies the joker to ITS right, giving you three instances of that 
  joker's effect.

## Positioning

ALWAYS place Blueprint immediately to the left of your highest-value 
joker. Common targets:
- xMult jokers (The Duo, The Trio, Ride the Bus)
- Scaling jokers (Steel Joker, Hanging Chad)
- High flat-mult jokers in early game (Joker, Scary Face)

## When NOT to Buy

- If you have no strong joker to copy (Blueprint + weak joker = overpaying)
- If your joker slots are full and you'd need to sell something better

Related: joker ordering, left-to-right evaluation, The Duo, 
Brainstorm, xMult scaling
```

### Example: STS strategic concept (currently in prompt)

```markdown
# Full Block Algorithm (STS Combat Concept)

The default goal every turn in a hallway fight is ZERO DAMAGE TAKEN.

HP lost in a hallway fight is permanent until a rest site. 8 damage at 
80 HP is exactly as bad as 8 damage at 20 HP.

## The Flowchart

STEP 1: Read total incoming damage (check intents, sum attackers, apply Weak).
STEP 2: Enumerate ALL paths to zero damage:
  A) Kill attackers + block remainder
  B) Pure block
  C) Debuff + block (apply Weak, block the rest)
  D) Potion-assisted
STEP 3: Compare paths that achieve zero damage:
  - Prefer kill paths (removes future damage)
  - Among kills, prefer ones that also damage non-attackers
  - Among block paths, prefer useful side effects (draw, exhaust junk)
STEP 4: If NO path achieves zero:
  - Minimize damage taken
  - Consider potions (unused potion on death screen = strategic failure)
  - Prioritize killing highest-damage attacker
STEP 5: Execute.

Do NOT pick ONE plan and execute. Enumerate at least two paths before 
choosing.

## Exceptions (intentional HP spend)

1. Boss fights: HP resets after bosses. Spend HP freely.
2. Hard-scaling enemies (Ritual, Rally): Kill speed prevents more total 
   damage than blocking.

Related: turn planning template, combat arithmetic checklist, hallway 
vs boss classification
```

### Example: Balatro strategic concept (currently in prompt)

```markdown
# Scaling Checkpoints (Balatro Strategy Concept)

Each ante has a chip target that grows roughly 3-4x per ante. Your 
scoring must scale to match. If you fall behind the scaling curve, 
no amount of perfect hand selection will save you.

## Target Progression (approximate)

Ante 1: 300 / 450 / 600 (Small / Big / Boss)
Ante 2: 800 / 1200 / 1600
Ante 3: 2800 / 3600 / 5000
Ante 4: 8000 / 12000 / 16000
Ante 5: 20000 / 30000 / 36000
Ante 6: 50000 / 60000 / 80000
Ante 7: 120000 / 150000 / 200000
Ante 8: 300000 / 400000 / 500000

## Scaling Sources (in build order)

1. Planet cards (level up hand types) — reliable early scaling
2. Additive mult jokers — good through Ante 4
3. xMult jokers — necessary by Ante 5, dominant by Ante 7
4. Scaling jokers (Steel Joker, Ride the Bus) — exponential when supported
5. Retrigger effects — multiply everything else

## The Checkpoint Test

At the end of each ante, ask: "Can my best hand beat the NEXT boss 
blind target?" If no, the next shop MUST prioritize scaling. Skip 
utility purchases. Buy damage or lose.

## Common Failure Mode

Buying utility (negative jokers, card removal) when you haven't secured 
scaling for the next ante. Utility is worthless if you can't beat the 
blind.

Related: build archetypes, xMult scaling, planet strategy, shop 
decision framework
```

### Example: Cross-cutting concept entry

```markdown
# Brimstone Anti-Synergies (STS Relic Interaction)

Brimstone gives ALL characters (including enemies) +2 Strength at the 
start of each combat. The player Strength is valuable. The enemy 
Strength is the cost.

## Lethal combinations

Book of Stabbing + Brimstone: AVOID AT ALL COSTS. Book natively gains 
+3 Str/turn AND adds +1 hit/turn. Brimstone adds +2 Str/turn on top. 
Combined scaling is quadratic. Two confirmed deaths. Even at 75% HP 
with strong player Str scaling, the fight is unwinnable by turn 5.

## Routing with Brimstone

When holding Brimstone, avoid elite paths entirely if HP is below 70%. 
If Book of Stabbing is a possible encounter, do NOT take the elite path 
regardless of HP.

Related: Brimstone (relic), Book of Stabbing, elite risk assessment
```

### Example: Balatro cross-cutting concept

```markdown
# Joker Ordering (Balatro Core Mechanic)

Jokers evaluate LEFT TO RIGHT. This is not cosmetic — it determines 
your score. Additive mult jokers must be to the LEFT of xMult jokers, 
or the multiplication has nothing to scale.

## Correct Order (left to right)

1. Chip-adding jokers (Banner, Scary Face)
2. Flat mult jokers (Joker, Misprint, Sly Joker)
3. xMult jokers (The Duo, Ride the Bus, Blackboard)
4. Conditional xMult jokers that you can't always trigger (rightmost)
5. Blueprint/Brainstorm (immediately left of what they should copy)

## The Compounding Error

Wrong order: [Ride the Bus x3] [Sly Joker +50mult] → 
  Chips get x3 first (useless on base), then +50mult added flat.
Right order: [Sly Joker +50mult] [Ride the Bus x3] → 
  +50mult added first, then ENTIRE score multiplied by 3.

With base hand of 40 chips × 4 mult:
  Wrong: (40 × (4×3)) + 50 = 40 × 12 + 50 = 530 total? No — 
  Actually: (40 × 4) × 3 = 480, then 480 + (40 × 50) = bad mental model.
  
  The actual formula: chips × (mult + flat_additions) × xMult_product.
  Order determines WHICH multipliers see which additions.

## When to Reorder

Reorder jokers EVERY TIME you buy a new joker. The correct order after 
adding a joker is almost never "place it at the end."

Related: left-to-right evaluation, scoring formula, Blueprint, 
Brainstorm, xMult scaling
```

### Example: Meta entry (navigation root)

```markdown
# Game Context: Slay the Spire

Single-player deckbuilding roguelike. Build a deck through branching 
maps of combat, events, shops, and campfires. Manage HP as a finite 
resource across the entire act. Boss fight at the end of each act.

## What to load first

1. Your character entry (Ironclad, Silent, Defect, or Watcher)
2. "Full Block Algorithm" — the combat decision framework
3. "STS act pathing" — how to plan routes
4. The boss entry for your current act

## During combat

Load: each enemy, unfamiliar cards in hand, status effects you see, 
relevant relic interactions.

## At rewards, shops, events

Load entries for each option before deciding.

Related: Full Block Algorithm, STS act pathing, card evaluation 
framework, your character entry
```

```markdown
# Game Context: Balatro

Poker-based roguelike. Build a scoring engine from jokers, enhanced 
cards, and leveled-up hand types. Beat increasingly large chip targets 
across 8 antes, each with Small Blind → Big Blind → Boss Blind.

## What to load first

1. "Scoring formula" — Chips × Mult, evaluation order
2. "Scaling checkpoints" — targets per ante and what scaling you need
3. "Joker ordering" — left-to-right evaluation (critical)
4. The boss blind entry for your current ante

## During a hand

Load: jokers you're unsure about (interaction questions), the current 
boss blind's constraint, hand type scoring if comparing options.

## At shops

Load: any joker you're considering buying, "shop decision framework," 
current build archetype entry.

Related: scoring formula, joker ordering, scaling checkpoints, 
shop decision framework, build archetypes
```

---

## The Knowledge Graph

### How the graph forms

The compendium is not a formal graph with typed edges and schema. It's a collection of markdown files where entries mention other entries by name. The graph is implicit in the text.

When the STS agent reads the Wrath entry and sees "Related: Calm, Eruption, Vigilance, Flurry of Blows, end-of-turn stance safety," those are five potential edges. When the Balatro agent reads the Blueprint entry and sees "Related: joker ordering, left-to-right evaluation, The Duo, Brainstorm," those are four potential edges. The agent can follow any of them.

This is intentional. A formal graph would require the analyst to maintain link integrity, handle renames, and define relationship types. Natural language references are cheaper to write, easier to maintain, and the agent is perfectly capable of understanding references as navigation prompts.

### Graph topology

The compendium naturally forms clusters regardless of domain:

**STS character cluster:** Watcher → stance entries (Wrath, Calm, Divinity) → card entries (Eruption, Vigilance) → timing concepts (end-of-turn stance safety).

**STS enemy cluster:** Hexaghost → mechanics (Burns, Inferno) → counter-strategies (Evolve, Fire Breathing) → card entries.

**Balatro build cluster:** "Flush build archetype" → relevant jokers (Splash, Smeared Joker) → hand type entry (Flush scoring) → planet strategy → enhancement strategy (Wild cards).

**Balatro boss cluster:** The Needle → "one-hand strategies" → high-chip hand types → jokers that boost first hand → planet investment priorities.

**Strategy cluster (both games):** High-level strategy → HP/scaling thresholds → specific dangerous situations → counter-strategies → entity entries.

**Meta cluster (both games):** "Game Context" → character/build overview → core frameworks → entity types. These are the roots of the graph — starting points for navigation.

### Navigation patterns

The agent navigates the graph in predictable ways regardless of domain:

**Depth-first:** STS agent encounters Gremlin Nob → loads Nob entry → sees "Skill cards trigger Enrage" → loads Enrage entry. Balatro agent sees Blueprint in shop → loads Blueprint entry → sees "copies joker to its right" → loads joker ordering entry.

**Breadth-first:** STS agent at card reward → loads all three offered cards simultaneously. Balatro agent at shop → loads all available jokers simultaneously.

**Goal-directed:** STS agent preparing for Act 3 boss → loads boss entry → sees requirements → evaluates deck. Balatro agent preparing for Boss Blind → loads boss blind entry → sees constraint → evaluates which hands are still viable.

The graph doesn't dictate a navigation pattern — the agent chooses how to traverse it based on its current need.

---

## Recursive Loading

### How it looks in practice: STS combat

A fresh agent session with the Watcher facing combat on floor 7:

**Wave 1: Session bootstrap**
```
Agent: lookup("game context")
  → Gets "Game Context: Slay the Spire"
  → Sees: load character entry, Full Block Algorithm, act pathing, boss

Agent: lookup("Watcher", "Full Block Algorithm", "STS act pathing")
  → Gets Watcher overview, combat decision framework, act routing
  → Now understands the game, its character, and how to approach decisions
```

**Wave 2: Combat context**
```
State shows: Floor 7, Combat vs Gremlin Nob + Sentry

Agent: lookup("Gremlin Nob", "Sentry")
  → Gets both enemy patterns
  → Nob entry says "Skill cards trigger Enrage — avoid skills"
  → Sentry entry says "Dazed cards clog deck — kill fast or exhaust"

Agent sees Vulnerable applied, unsure of exact math:
Agent: lookup("Vulnerable")
  → Gets "50% more damage from attacks, direction matters"
```

**Wave 3: Hand evaluation**
```
Hand: Eruption, Vigilance, Strike, Defend, Flurry of Blows

Agent: lookup("Eruption")  (already loaded Watcher entry, but wants detail)
  → Sees "Do NOT enter Wrath if enemy is attacking and you can't exit"
  → Nob is attacking for 14. Wrath would double it to 28.
  → Decides: play Strike and Defend this turn, save Eruption for kill turn
```

### How it looks in practice: Balatro hand selection

A fresh agent session at Ante 4, facing the Big Blind:

**Wave 1: Session bootstrap**
```
Agent: lookup("game context")
  → Gets "Game Context: Balatro"
  → Sees: load scoring formula, scaling checkpoints, joker ordering, boss blind

Agent: lookup("scoring formula", "scaling checkpoints", "joker ordering")
  → Understands Chips × Mult, evaluation order, ante targets
  → Sees Ante 4 Big Blind target: 12000
```

**Wave 2: Hand context**
```
State shows: Ante 4 Big Blind, target 12000
Jokers: [Sly Joker] [Hack] [Ride the Bus x5]
Dealt hand: K♠ K♥ K♦ 7♣ 4♠ 9♥ 2♦ 8♣

Agent: lookup("Sly Joker", "Hack", "Ride the Bus")
  → Sly Joker: +50 mult on hands with pairs or better
  → Hack: retriggers each played card once
  → Ride the Bus: x1 for each consecutive hand without face card; 
    currently x5

Agent considers: Three Kings = Three of a Kind.
Agent: lookup("Three of a Kind scoring")
  → Base: 30 chips, 3 mult. Each King adds 10 chips.
  → With Hack retriggering: each King's 10 chips counted twice = 60 extra
  → Score estimate: (30 + 60) × (3 + 50) × 5 = 90 × 53 × 5 = 23,850
  → Beats 12000 target. But playing face cards resets Ride the Bus.
```

**Wave 3: Tradeoff evaluation**
```
Agent reconsiders: playing Kings resets Ride the Bus from x5 to x1.
Alternative: play 7♣ 4♠ 9♥ 2♦ 8♣ — no face cards, keeps Ride the Bus.
That's a High Card or nothing. Not enough to beat 12000.

Agent: "Three Kings scores 23,850 but resets Ride the Bus. No alternative 
reaches 12000. Must play the Kings. Accept the reset."

Decision: play K♠ K♥ K♦ (three of a kind).
```

### The key observation

In both examples, the agent loaded exactly what it needed, nothing more. No script anticipated the Vulnerable lookup in STS or the Ride the Bus reset calculation in Balatro. The agent identified its own knowledge gaps and filled them.

A scripted loader would have either:
- Loaded too much (all relics, all jokers) — wasting context
- Loaded too little (missed the Vulnerable mechanic, missed the Ride the Bus reset implication) — causing errors
- Required code changes every time a new type of relevant knowledge emerged

### When NOT to load

The agent shouldn't reload entries it already has in context. If it loaded the Full Block Algorithm at session start, it doesn't reload it every turn. If it loaded Ride the Bus earlier, it doesn't need the entry again unless it forgot the mechanic.

This is natural — entries are in the conversation context once loaded. The compendium architecture doesn't force redundant loading.

### Context window management

If the agent loads 15 entries at combat/hand start plus 5 more mid-decision, that's potentially 1000+ lines. Two mitigations:

1. **Entries should be concise.** Entity entries: 5-15 lines. Concept entries: 30-60 lines. Boss entries: 40-80 lines. Anything longer should be split into a core entry with references to detail entries.

2. **The agent should be selective.** It doesn't need every card in its hand — only unfamiliar ones or ones with complex interactions. It doesn't need every joker — only the ones relevant to the current decision. Agent-driven loading naturally economizes.

The strategist monitors context usage from run logs. If runs show the agent loading too much, the strategist restructures entries (splits long ones, creates summary variants) and coaches selectivity.

---

## The Agent Prompt

### What stays in the prompt

The prompt shrinks to ONLY:

**1. LLM behavior shaping** (~20 lines)
```
You are not an expert. You are learning. Express uncertainty honestly. 
Never say "clearly" or "obviously" about strategic decisions. After a 
failure, don't rationalize — identify what you actually got wrong.
```

This stays because it's about how the LLM reasons, not what it knows about any domain.

**2. Agent framework** (~40 lines)
```
You are a decision-making agent. You make one decision at a time.

Use lookup() to request knowledge from the compendium. Start each 
session by requesting your game context. Load what you need, when you 
need it.

Post reasoning with think() at key decision points. Provide reason= 
with every action.
```

**3. Tool documentation** (~30 lines)
```
lookup(*topics)    — Request compendium entries
state()            — Read current state
send(cmd, reason)  — Execute single action
think(text, label) — Post reasoning to stream
...
```

**4. Session context** (~5 lines, from orchestrator)
```
Domain: Slay the Spire
Character: Watcher
Ascension: 0
```
or
```
Domain: Balatro
Stake: Red
Deck: Red Deck
```

That's it. Maybe 80-100 lines total instead of 400-500. All domain knowledge — combat algorithms, scoring formulas, strategic frameworks, entity details — lives in the compendium.

### What moves to the compendium

**From STS prompt → compendium:**

| Current prompt section | Compendium entry |
|---|---|
| The Full Block Algorithm | "Full Block Algorithm" (concept) |
| Turn Planning template | "STS turn planning template" (concept) |
| Draw effects rule | "draw effects: stop and replan" (concept) |
| Full Act Pathing | "STS act pathing" (concept) |
| Card Rewards guidance | "STS card evaluation framework" (concept) |
| Rest Site decisions | "STS rest site decisions" (concept) |
| Potions guidance | "STS potion timing" (concept) |

**From Balatro prompt → compendium:**

| Current prompt section | Compendium entry |
|---|---|
| Scoring formula | "scoring formula" (mechanics) |
| Joker evaluation order | "left-to-right evaluation" (mechanics) |
| Shop decision framework | "shop decision framework" (concept) |
| Build order guidance | "build archetypes" (concept) |
| Hand selection heuristics | "hand selection framework" (concept) |
| Boss blind preparation | Individual boss blind entries |

**From STS strategy.md → individual entries:**

The 700-line `strategy.md` monolith becomes ~25 focused entries of 20-60 lines each. Similarly, Balatro's `playbook/strategy.md` decomposes into individual concept entries.

---

## Analyst and Strategist Roles

### Analyst changes

The analyst's core job stays the same: review completed sessions, identify prediction errors and strategic mistakes, update the knowledge base. What changes:

**Expanded scope.** The analyst can now create entries for anything — strategic concepts, mechanical rules, cross-cutting concerns, domain-specific techniques, interaction warnings. Previously limited to entity files + strategy.md; now the full entry taxonomy is available.

**No prompt boundary.** The analyst never needs to think "should this go in the prompt or the playbook?" Everything goes in the compendium. If the STS player lost because it didn't know the draw effect rule, the analyst creates the "draw effects" entry. If the Balatro player lost because it didn't understand The Needle's constraint, the analyst creates or updates The Needle entry.

**Entry size discipline.** Keep entries focused. If a boss entry grows beyond 60-80 lines, split it. If a concept entry tries to cover too many situations, decompose it into linked entries.

### Strategist changes

The strategist's role becomes more important:

**Graph coherence.** Are entries well-connected? Can the agent navigate from high-level concepts to specific details through natural references? Are there orphan entries? In STS: does the Watcher entry link to all relevant stance entries? In Balatro: does the scoring formula entry link to joker ordering?

**Entry sizing.** Monitor context window usage from session logs. Restructure entries that cause problems.

**Coverage gaps.** With all knowledge in one place, gaps are visible. "We have 50 joker entries but no entry explaining how xMult stacking works" is obvious when everything is in the compendium.

**Navigation quality.** Does the agent find what it needs? Session logs include lookup events — the strategist sees what was requested and whether useful results came back. If the agent keeps requesting topics that don't match any entry, create entries or aliases.

**Meta-entries.** The strategist maintains "start here" entries that orient new sessions. Game context entries and navigation guides are the strategist's responsibility.

### What they produce

The analyst produces:
- New compendium entries (one file per entry)
- Updates to existing entries (surgical edits based on observed errors)
- Observations about uncertain items (for later confirmation)

The strategist produces:
- Restructured entries (splits, merges, rewrites for clarity)
- New concept entries that synthesize patterns across sessions
- Meta-entries and navigation improvements
- Coverage assessments and gap analysis

---

## Testing Generalizability: STS vs. Balatro

The architecture claims to be domain-agnostic. STS and Balatro are different enough to test this claim rigorously.

### The differences that matter

| Dimension | STS | Balatro |
|---|---|---|
| Core mechanic | Attack/Block against enemies | Score Chips × Mult to beat targets |
| Adversary | Enemies with intents | Blind targets (passive) + boss constraints |
| Decision unit | Which cards to play + targets | Which cards to play from hand |
| Resource | HP (permanent across floors) | Hands/Discards per blind |
| Progression | Map pathing through acts | Ante progression (linear) |
| Build axis | Deck composition + relics | Jokers + hand type levels + enhancements |
| Interaction complexity | Cards + relics + effects | Jokers (ordered) + cards + enhancements |
| Knowledge density | 200+ entities across 6 types | 150+ entities across 5 types |
| Critical ordering | Turn order (which cards first) | Joker order (left-to-right) |

### Same mechanism, different entries

The architecture handles both because both follow the same fundamental pattern:

**1. Observe state → identify knowledge needs**

STS: "I see Gremlin Nob. I need to know its pattern."
Balatro: "I see The Needle boss blind. I need to know its constraint."

Same mechanism: agent reads state, identifies gaps, calls `lookup()`.

**2. Load knowledge → reason about decision**

STS: Nob entry says "punishes skills." Agent avoids playing Defend.
Balatro: Needle entry says "must beat in one hand." Agent loads high-scoring hand types.

Same mechanism: entries are self-contained, actionable, cross-referenced.

**3. Execute → observe result → learn**

STS: Agent plays attacks-only turn. Takes 0 damage. Analyst confirms strategy.
Balatro: Agent plays Three of a Kind for 23,850. Beats target. Analyst notes Ride the Bus reset was acceptable.

Same mechanism: analyst reviews outcomes, updates entries based on prediction accuracy.

### Where the architecture is tested hardest

**Ordered interactions (Balatro jokers):**

Balatro's left-to-right joker evaluation creates a knowledge type that STS doesn't have: positional interaction knowledge. The entry for "Blueprint" must describe not just what it does but WHERE it should be relative to other jokers. The entry for "Ride the Bus" must note that playing face cards resets it.

Does the compendium handle this? Yes — these are just entries with actionable positioning guidance in their "decision points" section. The entry format accommodates this naturally. No new mechanism needed.

**Conditional constraints (Balatro boss blinds):**

Boss blinds in Balatro impose constraints that change which hands are legal or scoring. The Flint halves base chips and mult. The Needle allows only one hand. The Verdant debuffs all cards of one suit.

This is analogous to STS enemy patterns (Gremlin Nob punishes skills), but the constraints are more varied and affect hand construction differently each time. The compendium handles this the same way: each boss blind is an entry describing the constraint and how to play around it.

**Scoring math (Balatro):**

Balatro requires exact scoring calculations to decide between hands. The agent needs to compute "will this hand beat the target?" which requires loading the scoring formula, knowing each joker's contribution, and understanding evaluation order.

STS has analogous math (damage calculation with Strength, Vulnerable, multi-hit), but it's less central to every decision. The compendium handles both: the scoring formula entry and the damage calculation entry are both "mechanics" entries that the agent loads when it needs to do math.

**Emergent interactions (both):**

STS: Brimstone + Book of Stabbing is a lethal interaction not obvious from either entry alone. The compendium solves this with cross-cutting concept entries ("Brimstone Anti-Synergies").

Balatro: Blueprint + Ride the Bus (at x8) + face-card-free hand = massive scaling. This interaction isn't in any single joker entry. Solution: same pattern — a "Blueprint combos" or "xMult stacking" concept entry that documents discovered synergies.

The mechanism is identical: cross-cutting knowledge lives in concept entries that reference the entities involved.

### The generalizability test result

Every knowledge type in both games maps cleanly to the compendium architecture:

| STS knowledge type | Balatro knowledge type | Compendium mechanism |
|---|---|---|
| Card entries | Joker entries | Entity file in relevant directory |
| Enemy patterns | Boss blind constraints | Entity file with decision guidance |
| Relic interactions | Joker ordering effects | Cross-cutting concept entries |
| Status effects | Enhancement rules | Mechanics entries |
| Combat algorithm | Scoring calculation | Concept entry (framework) |
| Act pathing | Ante planning | Concept entry (strategy) |
| Character mechanics | Deck-type strategies | Concept entry (build-specific) |
| Mistakes log | Mistakes log | Running entry of confirmed errors |

No new mechanism was needed for Balatro. No special case. No "but Balatro is different because..." The same directories (entities, concepts, mechanics, meta), the same lookup function, the same analyst/strategist roles, the same agent prompt. Only the entries differ.

### Beyond games

This same pattern works for any sequential decision-making domain:

| Domain | State observation | Knowledge need | Compendium entry types |
|---|---|---|---|
| STS | Combat state, map, deck | Enemy patterns, card interactions | Cards, enemies, concepts |
| Balatro | Hand, jokers, blind target | Scoring math, joker synergies | Jokers, mechanics, concepts |
| Code review | Diff, file context | Style rules, past decisions | Patterns, rules, precedents |
| Medical diagnosis | Symptoms, history | Differential criteria, drug interactions | Conditions, treatments, protocols |
| Puzzle solving | Grid state, constraints | Known patterns, transforms | Patterns, strategies, heuristics |

The mechanism is always: observe → identify knowledge gap → load → reason → act → learn. The compendium is the accumulated experience that makes each subsequent decision better-informed. The specifics are just different entries.

---

## Migration Path

The migration from the current system to the compendium doesn't have to happen in one step. Here's the incremental path, applicable to both STS and Balatro simultaneously.

### Phase 1: Build lookup(), keep everything else

Implement `lookup()` as a superset of the current `reason()` (STS) and playbook loading (Balatro):
- Searches all directories (not just current categories)
- Accepts multiple topics
- Adds fuzzy matching
- Add new directories: `concepts/`, `mechanics/`, `meta/`

The agents still have their full prompts. STS still has `plan()`. Balatro still has boot loading. But both also have `lookup()` for things the current mechanisms don't cover. Purely additive — nothing breaks.

**Effort:** Modify both game `cmd.py` files to add `lookup()`. Create a few concept entries per game. A few hours of work.

### Phase 2: Create concept entries from prompt content

Extract strategic concepts from both games' prompts into individual compendium entries. Don't remove them from prompts yet — just create the compendium versions.

STS: Full Block Algorithm, turn planning, act pathing, card evaluation → individual entries.
Balatro: scoring formula, scaling checkpoints, shop decisions, joker evaluation → individual entries.

**Effort:** 2-3 hours of writing/editing per game. No code changes.

### Phase 3: Teach both agents to use lookup()

Update both agents' prompts to instruct them to use `lookup()` for knowledge they need. Monitor a few sessions per game to see if agents use it effectively.

**Effort:** Small prompt edits + observation across a few sessions per game.

### Phase 4: Shrink the prompts

Start removing content from both game prompts that is now covered by compendium entries. Do this gradually — remove one section, play a few sessions, verify no regression.

STS: Remove Full Block Algorithm from prompt → verify agent loads it via lookup.
Balatro: Remove scoring formula from prompt → verify agent loads it via lookup.

**Effort:** Incremental over many sessions. Each removal is a small edit + verification.

### Phase 5: Deprecate scripted loading

Once both agents reliably load their own context via `lookup()`, scripted loaders become redundant. STS `plan()` and Balatro boot protocol are no longer needed.

Keep them available as fallbacks but stop instructing agents to use them.

**Effort:** Small prompt edits. No immediate code removal needed.

### Phase 6: Compendium-only

Both agents' prompts are now just behavior + tools + session context. All domain knowledge is in the compendium. The full architecture is live.

### What not to do

**Don't migrate all at once.** Both current systems work and are producing learning. Cold replacement risks regression in both games simultaneously.

**Don't break the analyst.** The analyst's workflow of creating and updating individual entity files is already compendium-compatible. The analyst just needs to know about new directories and wider scope.

**Don't over-engineer lookup().** The current STS `reason()` function is 70 lines and works. `lookup()` should be an evolution: fuzzy matching, multi-topic support, broader directory search. Not a rewrite.

**Don't force identical directory structures.** STS needs `cards/` and `enemies/`. Balatro needs `jokers/` and `blinds/`. The lookup mechanism is identical; the directory taxonomy is domain-specific. That's fine.

---

## Open Questions and Honest Answers

### How does the agent know what to request if it's never seen a domain before?

**The bootstrap problem.** A brand new agent has empty context and needs to figure out what it's doing and what knowledge exists.

**Answer: A "start here" entry.** The agent prompt says: "Start each session by requesting your game context." The orchestrator provides session context (Domain: Slay the Spire, Character: Watcher), and the agent's first lookup is `lookup("game context")`. That entry tells it what to request next.

For a truly brand new domain with an empty compendium, the agent needs a minimal seed — a game context entry describing the domain and basic actions. The agent plays, makes mistakes, and the analyst creates entries from the experience. First sessions are bad. That's fine — learning requires it.

### How much context is too much?

**The context window concern.** If the agent loads 20 entries at decision time, that's 500-1000 lines competing with state, previous turns, and reasoning.

**Answer: Monitor, not prevent.** The agent should be selective ("load what you need, not everything"). The strategist monitors lookup patterns from logs.

Concrete mitigations:
- Keep entries concise (5-15 lines for entities, 30-60 for concepts)
- The agent naturally skips familiar entries
- The agent can load selectively (just the scoring formula, not all mechanics)
- The strategist splits bloated entries

No hard token budget. The right amount is "enough to decide well, not so much the agent can't process it." Fuzzy but manageable through strategist review.

### Should entries have summary vs. full modes?

**Answer: Not as a formal mechanism, but yes as a design pattern.** The first line of every entry should be a self-contained summary. "Blueprint: copies the joker to its right. Place left of your best joker." The agent can stop reading after the first line for quick assessments, or read the full entry for interaction details.

Rather than a separate "summary mode" in lookup, front-load the most important information in every entry.

### How do you handle wrong knowledge?

**The trust problem.** The agent trusts the compendium. If an entry says "Vulnerable is 75% more damage" (wrong — it's 50%), the agent miscalculates until corrected. If a Balatro entry says "Ride the Bus caps at x5" (wrong — it keeps growing), the agent makes suboptimal decisions.

**Answer: Same solution as always — the analyst corrects errors based on prediction mismatches.** When predicted outcome doesn't match actual outcome, the analyst traces the error to an entry and fixes it.

The compendium architecture makes errors more visible because they're in explicit, searchable entries rather than buried in a giant strategy.md or a prompt section nobody re-reads.

### Should there be meta-entries about how to use the compendium?

**Answer: Yes, absolutely.** The "game context" entries are meta-entries. They describe how to navigate the compendium for this domain. Additional meta-entries include:
- "Compendium structure" — what categories exist and what's in each
- "What to load at combat start" (STS) / "What to load per hand" (Balatro)
- "How to evaluate options" — the process, not the evaluation itself

These are maintained by the strategist as part of graph coherence.

### What happens when the agent requests something that doesn't exist?

**Answer: Clear "not found" message.** The agent plays its best guess, and the analyst creates the entry after the session. This already happens today when STS encounters an unknown enemy. The compendium architecture just extends this to all knowledge types.

Coverage grows from gameplay. Early sessions have gaps; later sessions don't.

### Does this make the agent slower?

**Answer: Slightly more tool calls, but negligible latency.** Batching (`lookup("Nob", "Strike", "Vulnerable")`) mitigates call count. Each lookup is a local file read, not an API call.

The bigger factor is decision quality. Better-informed decisions mean fewer misplays, fewer deaths, fewer wasted sessions. Avoiding one 30-minute run that dies to an avoidable mistake outweighs milliseconds of extra file I/O across hundreds of decisions.

### Can two games share knowledge?

**Answer: Probably not worth the complexity.** Some knowledge is genuinely cross-domain ("evaluate opportunity cost," "scaling beats frontloaded value in long games"). But implementing a shared compendium namespace adds complexity for minimal benefit.

Better approach: the strategist copies general principles into domain-specific compendiums and adds concrete examples. "Scaling beats frontloaded value" becomes "xMult jokers beat flat mult jokers by Ante 5" in Balatro and "Demon Form beats Inflame in long fights" in STS. Domain-specific framing with domain-specific examples.

### How does this interact with the brain-body architecture?

Both STS and Balatro use the same brain-body split: the "brain" (LLM agent) sends decisions; the "body" (game interface via TCP) executes them and reports results. The compendium is purely a brain-side mechanism. It affects what the agent knows and how it retrieves knowledge, but it doesn't change the body interface at all.

STS body: TCP to Java mod on :41140. Balatro body: TCP to Lua mod on :19283. Neither changes. The agent still sends the same commands. It just makes better-informed decisions about which commands to send.

---

## Why This Matters

The autoplay project exists to answer a question: can an autonomous agent learn to make good decisions in a complex domain through experience — getting better over time through a cycle of acting, analyzing, and updating a knowledge base?

The answer so far is yes. Six STS wins. Consistent Balatro scaling improvement. Measurable learning curves in both games. The analyst catches errors, the strategist identifies patterns, the agent improves.

But the current architecture limits how well this can work:
- Knowledge is split between prompts and playbooks with no principled boundary
- Loading mechanisms are game-specific Python scripts that can't adapt without code changes
- Prompts grow without bound as every regression adds more text
- Each new domain requires reimplementing the knowledge layer from scratch

The compendium architecture resolves all of these by establishing one principle: **the agent navigates its own knowledge.**

The prompt contains identity. The compendium contains knowledge. The boundary is sharp:
- **Identity** = how the agent thinks (behavioral directives, reasoning style, tool interfaces)
- **Knowledge** = what the agent knows (domain rules, strategies, entity details, cross-cutting concerns)

The agent can look up any knowledge at any time, following references through the graph. The same prompt works for STS and Balatro. The same lookup mechanism works for both. The same analyst and strategist roles work for both. Only the compendium entries differ.

This makes the system:

**More adaptive.** The agent loads what it needs, not what a script anticipated. When new knowledge types emerge (joker ordering concerns, boss blind constraints, cross-entity interactions), the agent accesses them immediately via the same lookup mechanism. No code changes.

**More maintainable.** All knowledge is in one place, in one format, updated by one process. No more "is this a prompt thing or a playbook thing?" decision. There's only the compendium.

**More portable.** Proven across two very different games (combat deckbuilder vs. scoring poker roguelike). The mechanism handles enemies and blinds, cards and jokers, relics and vouchers, status effects and enhancements — all through the same architecture. Adding a third domain means creating a compendium directory and a game context entry, not writing new loading code.

**More principled.** The boundary between agent and knowledge is defined: if removing it would change the agent's reasoning style, it's identity. If removing it would change what the agent knows about a domain, it's knowledge. Both STS combat algorithms and Balatro scoring formulas fail this test clearly — they're knowledge, not identity. They belong in the compendium.

### The fundamental insight

STS and Balatro are superficially different games. One is about attacking and blocking against enemies with patterns. The other is about constructing high-scoring poker hands with multiplicative joker interactions. But at the level of the decision-making agent, they share the same structure:

1. Agent observes a state (combat / dealt hand)
2. Agent identifies what knowledge would help it decide (enemy pattern / joker interaction)
3. Agent requests that knowledge from the compendium (lookup)
4. Agent reasons with the knowledge and acts (play cards / select hand)
5. After the session, an analyst reviews outcomes and updates the compendium
6. Knowledge accumulates over time, decisions improve

The specifics — cards vs. jokers, enemies vs. blinds, HP vs. hands remaining, damage vs. chip score — are just different compendium entries. The mechanism is identical. And if the mechanism works for two games this different, it works for any sequential decision-making domain with learnable knowledge.

The compendium is not a game-playing architecture. It is a knowledge-navigating architecture for autonomous agents that learn from experience. Games are where we prove it works. The architecture itself is general.

### The practical claim

Even setting aside generalizability: for STS alone, moving 236 lines of `sts-player.md` into navigable entries produces a more capable agent. It loads the Full Block Algorithm when entering combat instead of carrying it through every conversation turn. It loads act pathing at map screens instead of during fights. Context contains relevant knowledge instead of everything-just-in-case knowledge.

For Balatro alone: decomposing the boot-loaded playbook into on-demand entries means the agent loads scoring math when calculating, shop frameworks when shopping, and boss blind constraints when preparing — instead of carrying all of it in every message.

The migration is incremental, verifiable at each step, backwards-compatible until the final prompt reduction, and applicable to both games simultaneously.

The compendium is how autoplay scales — from one game to many, from rigid scripts to adaptive navigation, from growing prompts to a growing graph of knowledge that the agent explores on its own terms. It works because both games (and non-game domains) share the same fundamental pattern: an agent that gets better by accumulating and navigating knowledge.
