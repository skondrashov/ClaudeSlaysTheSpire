# Evidence Standards

How to decide whether a gameplay observation justifies a heuristic claim.

## The Strength Ladder

From weakest to strongest evidence:

1. **Theory.** "This should work because of these mechanics." Useful for generating hypotheses, not for writing heuristics. Mark as "untested."
2. **Single observation.** "This happened once in Run 185." An existence proof — proves something IS possible, not that it's good or reliable. Justifies "can work" language, not "should" or "always."
3. **Repeated observation.** "This happened in Runs 185, 192, and 201." A pattern. Justifies "usually" and "often" language. Still might be coincidence or confounded.
4. **Controlled comparison.** "Same seed, different strategy. Strategy A died Floor 38, Strategy B won." Eliminates card/enemy variance. Justifies "better than" claims for that context.
5. **Multiple controlled comparisons.** Same experiment across different seeds. Justifies general "better than" claims.

Most heuristics in the system are at level 2-3. Very few reach level 4-5. This is fine — acknowledge the evidence level honestly rather than inflating confidence.

## Writing Claims at Each Level

| Evidence level | Language | Example |
|---------------|----------|---------|
| Theory | "I think," "should," "might" | "Corruption without FNP might be underrated" |
| Single observation | "In Run 185," "can work" | "Snecko Eye + expensive cards can win (Run 185)" |
| Repeated observation | "Usually," "tends to," "in my experience" | "Nob usually kills you if you play 3+ Skills" |
| Controlled comparison | "Better than," "confirmed" | "Confirmed: exhaust beats pure strength on seed X" |
| Multiple comparisons | "ALWAYS," "NEVER" (cautiously) | "NEVER play Fiend Fire against Thorns — fatal in Runs 182, 195, 208" |

## When to Cite

Always cite when:
- Making a negative claim ("NEVER do X") — cite the death/failure
- Making a positive claim ("ALWAYS do X") — cite the success
- Contradicting conventional wisdom or a previous heuristic
- Describing a non-obvious interaction

Don't cite when:
- Stating something obvious from ontology facts ("Bash applies Vulnerable")
- Restating a well-established heuristic that already has citations in its own file

## Handling Counter-Evidence

When a run contradicts an existing heuristic:
1. Check whether the run's context was comparable (different ascension level, different deck composition, unusual RNG)
2. If comparable: soften the heuristic's language and note the counter-example
3. If not comparable: note the exception as a condition ("ALWAYS do X... unless Y, which occurred in Run 203")
4. If the counter-evidence is strong enough (controlled comparison, repeated): rewrite the heuristic

Never delete counter-evidence to preserve a clean narrative. The heuristic should reflect the full picture, not just the cases that support it.
