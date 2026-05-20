# Goal: Play a Run

Play Slay the Spire. Win by defeating the [[acts/Act 3]] boss. Make one decision at a time. Every action requires explicit reasoning.

Start from `ontology/index.md` to understand the game.

## Setup

```python
import sys
sys.path.insert(0, r"C:\Users\tkond\projects\autoplay\games\sts1")
from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, think, deck, start
```

Call `state()` to see the game. See `ontology/interface/tools.md` for the full tool reference.

Post reasoning to the stream overlay with `think()` so viewers can follow your decisions.

## Run End

When the run ends (GAME_OVER screen), proceed through it and STOP. Report:
- Victory or defeat, floor reached
- What went well, what went wrong
- Knowledge gaps encountered
