# Select the Next Goal

After a session finishes, decide what goal to pursue next. This heuristic is read at the end of every session.

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
   → Check the most recent audit report in analyst/audits/ for curation flags.
   → YES and flags are piling up (3+): Run Curate early.

5. Default: Run Win.
```

## Quick Version

Most of the time, the answer is **Win**. The exceptions:
- Curate said to explore something → **Explore**
- It's been a few runs since we checked our work → **Audit**
- It's been ~10 runs since we stepped back → **Curate**

## Notes

- Never run two playing goals (Win/Tournament/Explore) simultaneously. One at a time.
- **Tournament Win** is the all-out variant — every token goes to winning, with no win% labeling or learning detours. Choose it for a clean benchmark of best play, or when a win matters most. Default (casual) Win plays to win but spends some slack labeling win% as a learning artifact. Both are auditable; only Casual Win and Explore carry the *live* labels a calibration check needs — the analyst labels Tournament runs retrospectively.
- Audit and Curate don't touch the game — they can theoretically run while a game is in progress, but keep it simple and run them between games.
- After a Curate session that produces exploration directives, the next session should be Explore (not Win) to act on those directives while they're fresh.
- After a notable victory or a surprising death, Audit is higher priority than usual — there's more to learn from extreme outcomes.
