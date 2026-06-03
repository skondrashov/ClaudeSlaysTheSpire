# Curate the Playbook

Step back and evaluate the knowledge system. You are not playing the game and you are not reviewing individual decisions — you are assessing whether the strategic framework is healthy, balanced, and serving the player well.

## Knowledge Entry Points

Read these at the start of the session:

**Ontology:**
- `ontology/sts1/game.md` — Game domain (you need to understand the game to assess whether strategy makes sense)

**Heuristics:**
- [[layer:heuristics, curate]] — Overfitting detection, coverage analysis, evidence standards, formatting (read what exists)
- The ENTIRE heuristic tree is your review target — browse it to assess health, don't just read individual files

## Inputs

- `analyst/audits/` — Audit reports flagging tactical errors and patterns
- `analyst/runs/` — Raw run logs (skim for context, don't re-audit)
- `data/run_stats.json` — Win/death/floor statistics
- The full strategic playbook (heuristic tree)
- `ontology/` — Game facts
- Win margin notes (in run logs or analyst summaries)
- Explore experiment results (in run logs)

## Method

What to evaluate (overfitting, coverage, consistency, quality, strategic framework), the editing rules (what you can vs cannot change directly), and the curation principles are in [[layer:heuristics, curate]]. Read it before starting.


## Output

1. **Assessment** (10-15 lines): What's working, what's not, what's the biggest issue.
2. **Exploration directives**: Specific hypotheses to test during Explore sessions. This is your PRIMARY output — most insights should become directives, not immediate edits.
3. **Playbook edits**: Only for changes with strong evidence. See editing rules below.
4. **Cleanup**: Dedup, trim, fix contradictions, formatting.

Write directives to `analyst/directives.md`. Be conservative with direct playbook edits.

## Next Goal

At the end of your output, read [[layer:goals, next]] and recommend which goal to pursue next (Win, Explore, Audit, or Curate) and why. If you wrote exploration directives, the answer is almost certainly Explore.
