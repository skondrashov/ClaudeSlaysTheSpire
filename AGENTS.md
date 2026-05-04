# Slay the Spire

Deckbuilder roguelike. CommunicationMod reads game state and executes actions. Claude Code CLI plays via TCP relay.

**DO NOT AUTOPLAY.** No scripts, loops, or automation that sends game actions. Every action is a deliberate, reasoned choice made in conversation.

## How It Connects

```
CommunicationMod (in-game Java mod, stdin/stdout)
        |
    relay.py (TCP server on localhost:19284)
        |
    Claude Code CLI (via cmd.py functions)
```

CommunicationMod sends JSON game state on stdin when the game stabilizes (no pending animations). We respond with a command on stdout. The relay bridges this to TCP so Claude Code can connect per-action.

## Commands (cmd.py)

```python
from cmd import state, send, play, end, choose, proceed, skip, potion_use, start

state()              # See current game state
play(1, 0)           # Play card 1 targeting enemy 0 (1-indexed cards!)
end()                # End turn
choose(2)            # Choose option 2 (events, map, rewards, shop)
choose("smith")      # Choose by name (rest site)
choose("purge")      # Card removal at shop
proceed()            # Confirm/proceed
skip()               # Skip/cancel/leave
potion_use(0, 1)     # Use potion slot 0 on enemy 1
potion_discard(0)    # Discard potion slot 0
start("IRONCLAD", 5) # Start Ironclad A5 run
```

**Card indices are 1-indexed.** This is a CommunicationMod convention.

## Mod Stack (all Steam Workshop)

1. ModTheSpire — mod loader
2. BaseMod — modding API
3. CommunicationMod — game state + action protocol
4. SuperFastMode — speed up animations for bot play

## Game Model

Act 1-3 (+ optional Act 4). Each act: ~15 floors of monsters, elites, events, shops, rest sites, then a boss. Card rewards after combat. Upgrade cards at rest sites. Build synergistic decks. Don't die.

## Key Differences from Balatro

- No custom mod needed — CommunicationMod does everything
- stdin/stdout, not TCP (relay bridges to TCP)
- Synchronous lock-step — mod waits for our command
- Draw pile order is leaked (CommunicationMod known behavior)
- 1-indexed card positions
