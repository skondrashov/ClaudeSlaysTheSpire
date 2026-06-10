# Heuristic Updates

Heuristics live in `heuristics/`. Each entity can have a heuristic file mirroring the ontology structure (`heuristics/cards/`, `heuristics/enemies/`, `heuristics/bosses/`, etc.). Topic-level heuristics cover cross-cutting concerns (`heuristics/combat.md`, `heuristics/map.md`, etc.).

Write like an expert — clear, direct, actionable.

## Rules

1. **No run numbers.** State conclusions, not history.
2. **No confidence tags.** If confident, state it. If uncertain, put it in [[layer:heuristics, analysis/observations]].
3. **Surgical updates.** One file per entry. Add a note, refine a threshold, adjust language.
4. **Wrong info gets fixed.** Don't flag it — correct it.
5. **Expert voice.** Reader should get exactly what they need.

## Rot prevention — how single-run lessons go bad

These are the ways past analyst sessions have written heuristics that made play *worse*. Check every new or edited entry against them:

6. **Write disciplines as defaults, not crisis triggers.** A rule gated on "lethal turns," "below 30% HP," or "turn 5+" fires only after the damage is done — it codifies waiting until it's too late. Test: *would this rule have fired before the situation became desperate?* If a resource or check matters in emergencies, it almost always matters as an every-turn default; write it that way.
7. **Resource warnings must cut both ways, and expiring resources default to spend.** A warning against wasting a resource, with no statement of when holding it is the error, teaches hoarding. For anything that expires (potions, once-per-fight effects), the spend side is the default and the hold side is the exception that needs naming.
8. **Keep the mechanism, strip the incident.** A death teaches a game mechanism, not a story. Specific HP totals, exact damage sequences, and the particular fight are the incident; the rule is the mechanism that generalizes. If you cannot name the mechanism, the lesson is not ready for a heuristic — it goes to observations.
9. **One observation licenses conditional language only.** Absolutes (NEVER/ALWAYS/NON-NEGOTIABLE) need either a clean mechanical explanation or repeated evidence in the analyst layer. A threshold invented from one run ("enter above 60%") is a hypothesis; mark it as the current guess, not law.
10. **Disposition lessons go to topic files.** If the mistake was a pattern across many small decisions (greed, hoarding, deferred checks) rather than a single wrong choice, no entity page can hold it — it belongs in [[layer:heuristics, domain:sts1, combat]] / hp-management / drafting, where every session reads it.

## Don't

- Don't rewrite heuristic files from scratch
- Don't speculate beyond evidence — uncertain goes in observations
- Don't update for things that didn't come up in the run
