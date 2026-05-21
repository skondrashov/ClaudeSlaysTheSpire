# STS1 Interface Development

Patterns, known issues, and architecture decisions for the STS1 game interface.

## Architecture

```
CommunicationMod (Java, Steam Workshop)
  ↕ stdin/stdout JSON
relay.py (Python, TCP bridge)
  ↕ TCP :19284
cmd.py (Python, agent-facing functions)
  ↕ function calls
Agent (Claude Code CLI)
```

CommunicationMod handles all game state reading and action execution. We don't modify it — we work with what it exposes. The relay translates its stdin/stdout protocol to TCP so Claude Code can connect.

## Design Principles

- **No custom game mods.** Everything runs through CommunicationMod. This means we're limited by what it exposes, but it also means zero mod maintenance burden.
- **One TCP connection.** The relay owns the CommunicationMod process. Only one client connects at a time.
- **Synchronous request-response.** Agent sends a command, waits for the result. No async, no callbacks, no event streams. Simple and debuggable.

## Known Issues

(None documented yet. Playing agents will flag issues as KNOWLEDGE GAP notes.)

## State Representation Decisions

(Document decisions about how game state is formatted in `state()` output here. Why certain information is shown/hidden, formatting choices, etc.)
