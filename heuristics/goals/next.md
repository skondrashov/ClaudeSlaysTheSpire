# Selecting the Next Goal

After an agent finishes, decide what to run next. This heuristic is read by the orchestrator (or by any agent advising on what comes next).

## Decision Logic

```
1. Is there a Curate directive requesting Explore runs?
   → Check analyst/directives.md for outstanding exploration requests.
   → YES: Run Explore with the directive as the hypothesis.

2. Have 3+ runs completed since the last Audit?
   → Check analyst/audits/ — compare latest audit run number to latest run number.
   → YES: Run Audit on the most recent unaudited run.

3. Have 10+ runs completed since the last Curate?
   → Check when Curate last ran (analyst/directives.md timestamp or git log).
   → YES: Run Curate.

4. Are there unaddressed Audit flags?
   → Check the most recent audit report in analyst/audits/ for Curator flags.
   → YES and flags are piling up (3+): Run Curate early.

5. Default: Run Win.
```

## Quick Version

Most of the time, the answer is **Win**. The exceptions:
- Curate said to explore something → **Explore**
- It's been a few runs since we checked our work → **Audit**
- It's been ~10 runs since we stepped back → **Curate**

## Notes

- Never run two playing agents (Win/Explore) simultaneously. One at a time.
- Audit and Curate don't touch the game — they can theoretically run while a game is in progress, but keep it simple and run them between games.
- After a Curate run that produces exploration directives, the next run should be Explore (not Win) to act on those directives while they're fresh.
- After a notable victory or a surprising death, Audit is higher priority than usual — there's more to learn from extreme outcomes.
