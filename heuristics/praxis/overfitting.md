# Overfitting

The most dangerous failure mode in a knowledge system that updates itself.

## What It Looks Like

The knowledge cycle can self-reinforce: agent dies without X → analyst writes "need X" → next agent forces X → wins with X → "X confirmed critical." Now the system believes X is mandatory, even though the original death might have had multiple causes and X was just one of many solutions.

### Signs

- **Single-cause attribution.** Are deaths repeatedly attributed to the same root cause? If "no Strength" appears in 5 of 8 death analyses, the diagnosis is probably too narrow.
- **Archetype tunnel vision.** Does one archetype get a paragraph in archetypes.md while others get a sentence? Does the drafting tier list heavily favor one playstyle?
- **Absolutist language inflation.** "Useful" → "important" → "critical" → "non-negotiable" over successive Curate passes, without new evidence at each step.
- **Declining variance.** Are recent runs all playing the same strategy? Are card choices becoming more predictable? Narrowing behavior is a symptom.

## Why It Happens

1. **Confirmation bias in the pipeline.** Audit checks execution against heuristics. If heuristics say "prioritize X," deviations get flagged as errors even when they might have been correct.
2. **Survivorship in evidence.** Wins get studied for what worked. Deaths get studied for what was missing. This asymmetry biases toward "add more of what winners had" rather than "what else could have worked."
3. **Compounding over Curate cycles.** Each Curate pass reads the current heuristics and adjusts them. Without fresh data from alternative strategies (Explore runs), adjustments just reinforce the current framework.

## How to Detect

- **Count the absolute claims.** Read drafting.md and archetypes.md. How many "MUST," "NEVER," "non-negotiable" claims are there? How many have ≥3 confirming run citations?
- **Check the Explore cadence.** When was the last Explore run? If it's been 20+ Win runs since the last experiment, the system is probably overfitting.
- **Compare win strategies.** Do the 10 wins all use the same archetype? If yes, the system hasn't proven alternatives work — it's proven one thing works and assumed nothing else does.
- **Look for disconfirming evidence.** Has any run violated a "NEVER" heuristic and survived? If so, the heuristic is overstated.

## How to Correct

1. **Write exploration directives.** Don't rewrite the heuristic yourself — tell Explore what to test. "Play 3 runs building around Corruption+FNP without Strength scaling. Goal: determine whether exhaust can win independently."
2. **Soften language.** Downgrade absolutist claims to conditional claims when evidence is thin. "Non-negotiable" → "strongly preferred." "NEVER" → "avoid unless."
3. **Diversify Win's opening heuristics.** If win.md says "look for Strength scaling," add explicit instruction to also evaluate exhaust, block, and other archetypes on equal footing.
4. **Increase Explore cadence.** If the last 15 runs were all Win, schedule Explore runs more frequently even without directives.

## The Meta-Trap

Overfitting detection can itself overfit. If Curate always finds overfitting and always writes the same kind of corrective directive ("diversify more"), the correction becomes rote. Check whether previous diversification directives actually produced useful data, or whether they just added noise.
