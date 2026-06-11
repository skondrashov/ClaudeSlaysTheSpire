# Audit — Heuristics

How to evaluate a run's EXECUTION quality. The method behind the [[layer:goals, audit]] goal.

## Win-Probability, Regret, and Calibration (the primary lens)

**Label a win% at EVERY state.** Walk the run start to finish and assign each state — every combat turn, card reward, path choice, shop, rest, event — a win probability. Judge each one FORWARD: use only what was knowable at that node, with the run's actual ending deliberately blinded. You hold more context about each node than the live player did (you can see how the fight unfolded), but you must throw out the one thing that poisons the estimate — the outcome.

This converts a single terminal label ("the run was lost") into a dense win% trajectory you can read directly. No state gets special weight for *when* it happened — proximity to the death carries no information. The death fight is labeled like any other state: its regret may be large (a winnable fight fumbled) or near zero (arrived at 2%, the dice finished it). You find that out by labeling it, not by assuming.

**Regret = the avoidable drop.** A fall in win% from one state to the next mixes two things: your choice and the dice. To separate them, at each meaningful drop estimate the win% of the best action that was available, and subtract: `regret = win%(best available) − win%(chosen)`. A fight where the player drew badly and cratered has ~zero regret if the line was correct — that is variance, not a mistake. Rank decisions by regret. The steepest one or two, wherever they sit in the run, are what the audit is about.

**Calibration = belief error.** If the run carries the player's own live win% labels (Casual Win and Explore runs do), compare them to your forward estimates. A large gap is a place the player's *beliefs* were wrong, independent of whether they won — and it shows up in won runs too, so mine those as well. High regret with good calibration is an EXECUTION flag (knew better, didn't do it); a large calibration gap is a CURATOR flag (the playbook taught a wrong prior). Check the label's ANCHOR separately from its moves: a baseline inherited from prior runs rather than derived from the situation (ascension level, the character's actual record there), or a label re-affirmed unchanged across a material state change, is a calibration finding even when every relative update is well-sized.

**Win-side calibration reference (A9 Ironclad):** the one compliant winning trail on record ran ~28 flat through Act 1, +4 to +7 per boss kill/engine milestone, ~38 at Act 2 boss entry, ~45 at Act 3 entry, ~60 at final-boss entry — with the honest forward sitting ~5 higher from the engine-online point onward. Two implications: winners can err conservative (do not "correct" a winning trail upward into the old inflation pattern), and a winning trail with zero negative ticks is consistent with a run that genuinely had no setback — it is not by itself a calibration failure, and not a new norm.

The combat and non-combat checks below are how you EXPLAIN a regret once you have found it — the mechanism behind the lost win%.

## Diagnosing a book failure: knowledge gap vs retrieval miss

When a regret traces to the player not *knowing* something — a blind spot, not a misplay — separate two causes, because they have different fixes and different owners:

- **Knowledge gap** — the fact was not in the book at all. Fix: *write* it (an Extend/Curate job — a new ontology fact or heuristic).
- **Retrieval miss (awareness gap)** — the fact existed in the book but was not in the player's context when it mattered. The player cannot read what was never loaded. Fix: not new knowledge but better *awareness* — add the entity to the relevant situation's awareness manifest (`awareness/sts1/`) so it preloads next time.

To tell them apart, check whether an entry exists under `ontology/sts1/` or `heuristics/sts1/`. Exists → retrieval miss (flag the awareness manifest, not the content). Absent → knowledge gap. A third case — the fact was present *and* loaded and the player ignored it — is an execution error, not a book failure.

## Combat Decisions

For each fight, evaluate:
1. **Arithmetic.** Did the player calculate damage and block correctly? Common errors: forgetting Vulnerable (+50%), miscounting multi-hit, wrong Strength multiplier on Heavy Blade, not accounting for enemy block.
2. **Intent reading.** Did the player check enemy intents and plan accordingly? Missed an attacker intent = took avoidable damage.
3. **Card order.** Did draw cards come last in the sequence? Did the player play cards in an order that makes sense (buffs before attacks, block cards on defense turns)?
4. **Heuristic compliance.** Read the relevant heuristic files for each card played and enemy fought. Did the player follow the guidance? If they deviated, was it justified by the specific situation?
5. **Potion economy.** Potions are expiring resources: were they spent to prevent unblocked damage or shorten fights, or held while HP drained? Ending a fight with damage taken AND full potion slots is a flag by default. (The rare opposite error — drinking for no gain when a named harder fight was 1-2 floors away — is also worth a note, but hoarding is the recurring failure, not waste.)
6. **Lethal awareness.** On turns where the player was at risk of dying, did they recognize it and play accordingly?
7. **Premise staleness.** Per turn, recompute the actual end-of-turn incoming from LIVING enemies and compare it to block gained. Block exceeding the real incoming by a full card's value gets examined: legitimate over-block exists (Burns resolving at end of turn while block is live, Buffer preservation, Body Slam/Juggernaut decks) — anything else is flagged premise-stale. Generally, for each card played, ask whether the fact that justified it still held at play time: target still alive, draws still unlocked, stance unchanged. RECORD every instance in the disposition findings even at ~zero regret — cheap instances of this shape (block bought against a dead enemy, a dig played under a draw lock) are leading indicators of the family that kills runs.
8. **The cheaper line.** For every fight — including the ones that went well — ask whether a cheaper line existed: a kill order, a debuff, a burst window, a potion that reduces the HP paid. NEVER grade a fight's cost against a stored price ("within the book's range" is not a verdict — there are no book ranges; what a fight costs is a function of the deck that fought it). When a fight's paid cost is notable — unusually cheap, unusually dear, or structurally interesting — append it to analyst/fight-costs.md with the deck shape that produced it; that file is where cost patterns accumulate.

## Non-Combat Decisions
1. **Card rewards.** Did the player look up card heuristics before choosing? Did the choice make sense for the deck's archetype and current needs?
2. **Map pathing.** Did the player plan a full act route? Did they follow it? Were deviations justified?
3. **Shop purchases.** Did the player prioritize correctly (card removal, key relics, key cards)?
4. **Rest sites.** Upgrade vs rest — was the choice correct given HP and upcoming threats?
5. **Events.** Did the player look up the event? Did they choose the best option?

## Disposition errors — the pattern with no entity

Some recurring losses are not caused by any one fight, card, or choice: they are a *disposition* spread across many small decisions. Greedy resource play (chip damage accepted to conserve resources, potions hoarded, removes deferred) is the canonical one — each individual decision looks locally fine, and the death two fights later gets attributed to whatever fight it happened in. Per-entity attribution systematically loses these.

So in every audit, after ranking regrets, ask explicitly: **do several small regrets share a shape?** A dozen 2-3 HP leaks with full potion slots is ONE finding (a hoarding disposition), not twelve trivia. Disposition findings go to the topic files ([[combat]], [[hp-management]]), and when flagging them for Curate, say the kind, not just the instances.

And when a death IS the finding: the state immediately before it is the least informative place to write the lesson. Low HP at the death fight is the residue of upstream regrets, not a regret itself — walk the win% trajectory backward to where the HP actually went, and attribute there. Never flag "entered the fight too low" as the root cause; flag whatever made the player low.

## What You're NOT Doing
- You are NOT evaluating whether the playbook's strategy is correct. If the heuristic says "prioritize Strength" and you followed it but died anyway, that's a Curate problem, not an Audit problem.
- You are NOT rewriting heuristics. Flag issues; don't fix them.
- You are NOT making code changes.
