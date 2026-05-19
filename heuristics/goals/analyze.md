# Goal: Analyze a Run

Review a completed run and update the knowledge base. Extract what was learned. Write it down so the next play session is better.

## Inputs

- Run log at `analyst/runs/run_NNN.json` — decision log with game state after each action
- Ontology files in `ontology/` — facts about the game
- Heuristic files in `heuristics/` — strategic guidance
- Working notes in `analyst/observations.md`

**Read the run JSON first.** It has everything.

## Priority 1: Prediction Errors

Before analyzing strategy, analyze understanding. The player fills out combat plans with predictions. The run log has both the decision (with reasoning) and the result (actual state). Compare them.

Prediction errors reveal broken mental models. More important than bad strategy because they're upstream.

Look for:
- **Damage miscalculations**: Predicted taking 5 but took 15
- **Kill miscalculations**: Predicted killing enemy but it survived
- **Mechanic misunderstandings**: Didn't know an enemy does X, didn't know a card exhausts
- **Missing information**: Player said "I don't know what this does"

For each prediction error: fix ontology if facts are wrong, update heuristic if strategy was wrong.

## Priority 2: Strategic Patterns

Decisions that were technically correct (math right) but strategically wrong (plan bad).

## What You Write

### Heuristics (`heuristics/`) — Strategic guidance

Each entity can have a heuristic file. Write like an expert — clear, direct, actionable.

Rules:
1. **No run numbers.** State conclusions, not history.
2. **No confidence tags.** If confident, state it. If uncertain, put it in `analyst/observations.md`.
3. **Surgical updates.** One file per entry. Add a note, refine a threshold, adjust language.
4. **Wrong info gets fixed.** Don't flag it — correct it.
5. **Expert voice.** Reader should get exactly what they need.

### Ontology (`ontology/`) — Corrections only

Fix only factual errors: wrong damage numbers, missing attacks, incorrect mechanics. Do NOT add strategic commentary to ontology. Ontology is formally closed — entities describe what they ARE and DO, with `[[category/Name]]` links. No opinions.

### Observations (`analyst/observations.md`)

Things noticed but not confirmed:
```
## Unconfirmed
- [item]: [what we think, what needs verification]

## Open Questions
- [question]: [context]
```

Promote confirmed observations to heuristics and remove from observations.

## Process

1. Read the run JSON. First pass: prediction errors. Second pass: strategic mistakes.
2. Read existing heuristic files for entities encountered.
3. Make surgical updates to `heuristics/`. Fix wrong info, add new entries, refine existing.
4. Fix ontology only if facts are wrong.
5. Add uncertain items to `analyst/observations.md`.
6. Promote confirmed observations.

## Don't

- Don't rewrite heuristic files from scratch
- Don't speculate beyond evidence — uncertain goes in observations
- Don't update for things that didn't come up in the run
- Don't add strategic commentary to ontology files
- Don't create or modify files in `analyst/runs/`
