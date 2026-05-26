# Goal: Develop the Interface

Improve the code that lets agents interact with the game. You are not playing the game and you are not evaluating strategy — you are working on the tools, the relay, the state reader, the stream overlay, and anything else that bridges reasoning to execution.

## Knowledge Entry Points

Read these at the start of the session:

**Ontology:**
- `ontology/sts1/game.md` — Game domain (you need to understand what the game exposes to know what the interface should capture)

**Interface:**
- `interface/sts1/tools.md` — Current tool surface: what commands exist, what they do
- `interface/sts1/stream.md` — Current streaming setup

**Heuristics:**
- [[development/interface/sts1]] — Development patterns, known issues, architecture decisions (read what exists)

## Inputs

- **Knowledge gaps from playing agents.** Win and Explore agents drop `KNOWLEDGE GAP:` notes when the interface doesn't expose something they need. These are your primary work queue.
- **Audit flags.** The Audit agent may flag UI misplays caused by confusing tool behavior — that's an interface problem, not a player problem.
- **Curate observations.** The Curate agent may note that certain game states are poorly represented in `state()` output.
- **Direct requests.** The orchestrator may ask for a specific feature (new command, better state formatting, stream overlay improvement).

## What You Work On

### State Reading
- Does `state()` expose everything the playing agents need? Missing information (enemy intents not shown, potion slots unclear, relic effects invisible) causes blind spots.
- Is the state format clear and parseable? Ambiguous formatting causes arithmetic errors.

### Action Execution
- Are commands reliable? Do they fail silently? Do they have confusing edge cases?
- Are there actions the game supports that the interface doesn't expose?

### Stream Overlay
- Does the overlay render correctly? Is the reasoning visible and readable?
- Are there viewer experience improvements (layout, timing, information hierarchy)?

### Relay / Connection
- Is the TCP relay stable? Are there timeout issues, reconnection bugs, state desync?
- Error handling: what happens when the game is in an unexpected state?

## Codebase

The interface code lives at:
- `cmd.py` — Python client functions (what agents import)
- `relay.py` — TCP relay bridging CommunicationMod stdin/stdout to TCP
- `stream.py` — WebSocket + HTTP server for the OBS overlay
- `overlay/` — Browser source HTML/JS for the stream overlay

The game mod stack (CommunicationMod, BaseMod, SuperFastMode) is installed via Steam Workshop — you don't modify it. You work with what it exposes.

## Output

1. **Code changes.** Fix bugs, add features, improve reliability. Commit with clear messages.
2. **Interface doc updates.** If you change what tools.md describes, update tools.md.
3. **Knowledge gap responses.** For each gap you address, note which agent flagged it and what you did.
4. **Known issues.** Document things you found but didn't fix in [[development/interface/sts1]].

## Principles

- **The dumbest reliable interface wins.** Don't add complexity unless it solves a real problem a playing agent reported. The STS2 lesson: JSON file + clicks beat complex MCP/named-pipe architecture.
- **State completeness over state beauty.** An ugly but complete state representation is better than a clean one that hides information.
- **Test with a real agent.** If you change the interface, the next run should be Win or Explore to validate it works in practice.

## Next Goal

At the end of your output, read [[goals/next]] and recommend which goal the next agent should pursue (Win, Explore, Audit, Curate, or Develop) and why.
