# Evidence Standards

How to decide whether a gameplay observation justifies a heuristic claim — and how the claim should be worded at each level of evidence. The evidence itself (run logs, audits, statistics) lives in the analyst layer; the heuristic carries only the wording whose strength the evidence has earned. Domain knowledge never cites a run, an audit, or a date.

## The Strength Ladder

From weakest to strongest evidence:

1. **Theory.** "This should work because of these mechanics." Useful for generating hypotheses, not for writing heuristics.
2. **Single observation.** An existence proof — proves something IS possible, not that it's good or reliable. Justifies "can work" language, not "should" or "always."
3. **Repeated observation.** A pattern. Justifies "usually" and "often" language. Still might be coincidence or confounded.
4. **Controlled comparison.** Same seed, different strategy, different outcome. Eliminates card/enemy variance. Justifies "better than" claims for that context.
5. **Multiple controlled comparisons.** The same result across different seeds. Justifies general "better than" claims.

Most heuristics in a young system are at level 2-3. Very few reach level 4-5. This is fine — let the wording acknowledge the evidence level honestly rather than inflating confidence.

**A mechanical explanation upgrades the ladder.** A single observation whose game-mechanical cause is fully understood ("Fiend Fire hits once per exhausted card, so Thorns triggers once per card") supports firm language immediately — the rule follows from the mechanics, and the observation merely confirmed it. A single observation with no understood mechanism stays conditional no matter how dramatic the outcome was.

## Writing Claims at Each Level

| Evidence level | Language |
|---------------|----------|
| Theory | "I think," "should," "might" |
| Single observation | "can work," "watch out for" |
| Repeated observation | "usually," "tends to," "in my experience" |
| Controlled comparison | "better than," stated plainly |
| Multiple comparisons, or a clean mechanical explanation | "always," "never" (cautiously) |

## Where the Evidence Lives

The provenance — which runs, which audits, which statistics support a claim — stays in the analyst layer. A reader of a heuristic gets the lesson and the confidence; a maintainer who wants the trail follows it through the analyst records, not through the prose. This is what keeps domain knowledge about the domain: the game has no concept of a past run, so neither does its playbook.

## Handling Counter-Evidence

When a run contradicts an existing heuristic:
1. Check whether the run's context was comparable (different ascension level, different deck composition, unusual RNG).
2. If comparable: soften the heuristic's language to match the reduced evidence.
3. If not comparable: add the boundary as a condition ("always do X... unless Y").
4. If the counter-evidence is strong (controlled comparison, repeated): rewrite the heuristic.

Never ignore counter-evidence to preserve a clean narrative. The heuristic should reflect the full picture, not just the cases that support it.
