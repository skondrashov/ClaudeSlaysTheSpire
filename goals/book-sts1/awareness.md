# Maintain Awareness

Curate the awareness manifests — the relevance index that decides what knowledge is preloaded for a goal or situation *before* the player encounters it. This is the standing job behind the **retrieval-miss** half of Codify: the book can hold exactly the right fact and still lose the game if that fact never reaches the player's context.

## Entry Points

- `awareness/sts1/*.json` — The manifests themselves (goal-tier payloads today; situation/entity tiers reserved).
- `tools/awareness/` — The loader that consumes them (payload shape, session dedup, link resolution).
- `goals/sts1/audit.md` — How retrieval misses are diagnosed and flagged.
- Recent audits (`analyst/audits/run_*.md`) — Mined for retrieval-miss flags.

## What to Do

1. **Collect retrieval-miss flags.** From recent audits, gather decisions where the player lacked a fact that *existed* in the book — present, but not loaded when it mattered. (Missing facts are a knowledge gap, not your job — that's Extend/Curate.)
2. **Attribute each to a situation.** A retrieval miss is always relative to a context: a goal, an act, a fight type, an on-screen entity. Identify which awareness payload *should* have carried the entity.
3. **Adjust the manifest.** Add the entity (or its category) to that payload's `refs`. Prefer the narrowest tier that fixes it — a goal-wide entity belongs in the goal tier; a fight-specific one belongs in a situation tier (once those exist), not bloated into every session's preload.
4. **Guard against over-loading.** Awareness is a budget; every ref preloaded is context spent. Don't add an entity the player can cheaply `reason()` for on demand. Add the ones needed *before* they appear on screen, or too costly to look up mid-decision.

## Output

- Updated `awareness/sts1/*.json` manifests.
- A note of which retrieval-miss flags each change resolves, so the next audit can confirm the fix landed.

## Not This

- You are not writing knowledge. Missing facts (knowledge gaps) are an Extend/Curate job. This goal only changes *what gets loaded*, never *what is true* or *what to do about it*.
