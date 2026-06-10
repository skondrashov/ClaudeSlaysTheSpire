# Tools

The agent interacts with the game through Python functions imported from `cmd.py`.

## Setup

```python
import sys
sys.path.insert(0, r"C:\Users\tkond\projects\praxis\games\sts1")
from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, think, deck, start, survey, recall
```

## Observation

| Function | Description |
|----------|-------------|
| `state()` | Returns formatted text of the current game state (HP, enemies, hand, map, etc.) |
| `deck()` | Returns full deck contents sorted by type with costs and upgrade status |

## Action

| Function | Description |
|----------|-------------|
| `send(command, reason="...")` | Execute a single game action. `reason` is displayed on stream overlay. |
| `turn([actions], reason="...")` | Execute a full combat turn as a batch of actions. Each action is a string like `"play Bash 0"` or `"end"`. |
| `play(card, target)` | Play a card at a target. Card is 1-indexed or name. Target is 0-indexed enemy. |
| `end()` | End the current turn. |
| `choose(option)` | Choose an option by index or name. On MAP screens prefer names: `choose("rest")`, `choose("elite")`, `choose("x=3")` — an ambiguous or wrong name errors with the labeled node list instead of misrouting. Every choose response begins with `[chose: ...]` naming what was actually selected — READ IT; if it isn't what your plan named, deal with it immediately. |
| `proceed()` | Confirm / proceed / continue. |
| `skip()` | Skip / cancel / leave. |
| `potion_use(slot_or_name, target)` | Use a potion. **Prefer the potion's NAME** — slots renumber after every drink, so two `potion_use(0)` calls in a row hit different potions. |
| `potion_discard(slot)` | Discard a potion from a slot. |
| `start(character, ascension)` | Start a new run with the given character and ascension level. |

## Communication

| Function | Description |
|----------|-------------|
| `think(reasoning, label)` | Post strategic analysis to the stream overlay. `reasoning` is the text viewers see. `label` is a short heading (default: "Strategy"). |

## Knowledge

| Function | Description |
|----------|-------------|
| `survey()` | One selector call maps the live state → a menu of `recall()` handles worth pulling: the on-board entities (with their heuristic handles), upgraded cards, and any phenomenon whose conditions match right now. Judgment, not a state echo — it surfaces the non-obvious (combos, contextual warnings). Discovery, not content. Use at meaningful decision points (combat start, rewards, before elites/bosses), not every action. |
| `recall(*handles)` | Fetch knowledge by handle. A handle is a wiki-style address (`"enemies/Gremlin Nob"`, `"layer:heuristics, cards/Bash"`), a bare name (`"Gremlin Nob"` → ontology), or an upgraded card (`"Bash+"` → its resolved phenomenon). Names resolve robustly: variants (`"Spike Slime (M)"`), apostrophes (`"Charon's Ashes"`), a leading "The" added or removed (`"Champ"` → The Champ), `"Ascension N"` → its modifier entry, and map aliases (`"The Transient"`, `"Centurion + Mystic"`). The state always names the precise enemy variant (`"Red Louse"`, `"Blue Slaver"`) — recall that name, not a generic one. A bare name in several categories returns every match. Pass several handles for several entries (an entity's ontology AND heuristic = two handles). Does NOT follow links — `recall()` them too if you want them. **The single lookup verb.** |

## State Semantics

- **Intent damage numbers are final.** The displayed intent damage (e.g. `Intent: ATTACK (30x2)`) already includes every active modifier — the enemy's Strength, its Weak, your Vulnerable. Use the number as-is in block math; re-applying modifiers double-counts them (a confirmed source of under-blocking).

## Known Issues

- **The map cannot show which elite is burning.** With the final act unlocked, one elite per act carries the Emerald Key and buffs every monster in its fight (see `ontology/sts1/rules/burning-elite.md`) — but CommunicationMod doesn't expose the flag, so the text map shows all elites identically. If an elite fight opens with an unexpected buff on every enemy (Strength, +25% HP, Metallicize, or Regenerate), it's the burning elite; expect the Emerald Key in its rewards and price the fight higher.

- **Double-end bug (Run 216, confirmed fatal):** Sending `end` when the turn has already ended or is resolving can cause an extra enemy turn. Do NOT send `end` more than once per turn. If using `turn()` batches, include exactly one `"end"` at the end. If using `send()`, call `end()` only once and verify turn state before acting again. The snapshot-based fix in cmd.py addresses card index issues but does not guard against duplicate `end` commands.

## Card and Enemy References

- Card names resolve against the current hand: `"play Bash 0"` finds Bash in hand
- Card indices are 1-indexed: `"play 1 0"` plays the first card
- Enemy indices are 0-indexed and absolute: they don't shift when enemies die
- Enemy names work when enemies have distinct names: `"play Bash Jaw Worm"`
- When enemies share names (e.g., multiple Byrds), use numeric indices
