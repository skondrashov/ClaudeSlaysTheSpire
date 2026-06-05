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
| `choose(option)` | Choose an option by index or name. |
| `proceed()` | Confirm / proceed / continue. |
| `skip()` | Skip / cancel / leave. |
| `potion_use(slot, target)` | Use a potion from a slot at a target. |
| `potion_discard(slot)` | Discard a potion from a slot. |
| `start(character, ascension)` | Start a new run with the given character and ascension level. |

## Communication

| Function | Description |
|----------|-------------|
| `think(reasoning, label)` | Post strategic analysis to the stream overlay. `reasoning` is the text viewers see. `label` is a short heading (default: "Strategy"). |

## Knowledge

| Function | Description |
|----------|-------------|
| `survey()` | Lists the entities in play (enemies, non-basic hand cards, the act boss/character, card rewards, relics) as a menu of `recall()` handles, flagging which also have a heuristic. Deterministic — it reads the live state, so it surfaces what's in front of you. Discovery, not content. Use at meaningful decision points (combat start, rewards, before elites/bosses), not every action. |
| `recall(*handles)` | Fetch knowledge by handle. A handle is a wiki-style address (`"enemies/Gremlin Nob"`, `"layer:heuristics, cards/Bash"`), a bare name (`"Gremlin Nob"` → ontology), or an upgraded card (`"Bash+"` → its resolved phenomenon). Names resolve robustly: variants (`"Spike Slime (M)"`), apostrophes (`"Charon's Ashes"`), and map aliases (`"The Transient"`, `"Centurion + Mystic"`, `"Louse"` → both lice) all work. Pass several handles for several entries (an entity's ontology AND heuristic = two handles). Does NOT follow links — `recall()` them too if you want them. **The single lookup verb.** |

## Known Issues

- **Double-end bug (Run 216, confirmed fatal):** Sending `end` when the turn has already ended or is resolving can cause an extra enemy turn. Do NOT send `end` more than once per turn. If using `turn()` batches, include exactly one `"end"` at the end. If using `send()`, call `end()` only once and verify turn state before acting again. The snapshot-based fix in cmd.py addresses card index issues but does not guard against duplicate `end` commands.

## Card and Enemy References

- Card names resolve against the current hand: `"play Bash 0"` finds Bash in hand
- Card indices are 1-indexed: `"play 1 0"` plays the first card
- Enemy indices are 0-indexed and absolute: they don't shift when enemies die
- Enemy names work when enemies have distinct names: `"play Bash Jaw Worm"`
- When enemies share names (e.g., multiple Byrds), use numeric indices
