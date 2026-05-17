# Player Agent — Prompt Composition

This file tells the orchestrator how to build the player prompt. It is NOT sent to the player directly.

## Layer Files

The player prompt is composed from these files, concatenated in this order:

1. **`agents/player-personality.md`** — LLM behavior shaping (humility, hedging). Not game-specific.
2. **`agents/player-core.md`** — General game-playing agent (stream integration, plan/think/reason workflow, run-end behavior).
3. **`agents/sts-player.md`** — Slay the Spire framework (Full Block Algorithm, turn/fight templates, cmd.py interface, act pathing, map routing).
4. **`playbook/characters/<character>.md`** — Character-specific mechanics. Watcher stances, Defect orbs, Ironclad identity, etc. This is foundational knowledge the player needs from the start — not something to look up mid-run.

After the four layer files, add:
- Session token instructions (PLAYER_SESSION env var)
- Start command (`start("CHARACTER", ascension)`)
- Recent run context (optional — 3-5 bullet points of key lessons from last few runs)

## Rules

1. **Read all layer files with the Read tool every time.** Do not rely on memory, cached versions, or summaries from previous sessions. The files may have been updated by the analyst or strategist.
2. **Include their complete, unmodified contents.** Do not summarize, trim, condense, paraphrase, or rewrite any part. Every section exists because its absence caused a regression. The prompt is sent once at the start of a 1-2 hour session — its size is negligible compared to the hundreds of tool calls that follow.
3. **If the prompt seems too long or you want to cut something, don't.** Talk to the human first. Modify the source layer files if changes are actually needed.
4. **Do not duplicate playbook content in the prompt.** Card tier lists, boss prep, upgrade priorities, individual card strategies — all of this lives in `playbook/` and is loaded dynamically via `plan()` and `reason()`. Don't put it in the prompt.

## What goes where

- **Agent behavior** (how to think, how to talk) → `player-personality.md` or `player-core.md`
- **Game framework** (how STS combat works, how to plan turns) → `sts-player.md`
- **Character identity** (stances, orbs, starting deck, core engine) → `playbook/characters/<character>.md`
- **Specific game knowledge** (card evaluations, enemy patterns, boss prep) → `playbook/` (loaded via plan/reason)
