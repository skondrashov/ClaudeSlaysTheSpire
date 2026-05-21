# Tools

The agent interacts with the game through Python functions imported from `cmd.py`.

## Setup

```python
import sys
sys.path.insert(0, r"C:\Users\tkond\projects\autoplay\games\sts1")
from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, think, deck, start
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

## Card and Enemy References

- Card names resolve against the current hand: `"play Bash 0"` finds Bash in hand
- Card indices are 1-indexed: `"play 1 0"` plays the first card
- Enemy indices are 0-indexed and absolute: they don't shift when enemies die
- Enemy names work when enemies have distinct names: `"play Bash Jaw Worm"`
- When enemies share names (e.g., multiple Byrds), use numeric indices
