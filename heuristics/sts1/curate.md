# Curate — Heuristics

How to evaluate the health of the knowledge system. The method behind the [[layer:goals, curate]] goal. General curation/quality standards live in the Praxis heuristics ([[layer:heuristics, domain:praxis, overfitting]], [[layer:heuristics, domain:praxis, evidence]], [[layer:heuristics, domain:praxis, entry-quality]]).

## What to Evaluate

### 1. Overfitting

The most dangerous failure mode. Signs:
- **Single-cause attribution.** Are deaths being attributed to the same cause repeatedly? ("no Strength" appearing in 5 of 8 death analyses suggests the diagnosis is too narrow, not that Strength is literally the only thing that matters.)
- **Archetype tunnel vision.** Does the playbook present one archetype as dominant and others as inferior? Check [[archetypes]] — are all viable archetypes documented with equal conviction? Or does one get a paragraph and the others get a sentence?
- **Confirmation loop.** The knowledge cycle can self-reinforce: agent dies without X → analyst writes "need X" → next agent forces X → wins with X → "X confirmed critical." Check whether alternative explanations for deaths were considered.

When you detect overfitting:
- **Write an exploration directive.** Specify what to test during the next Explore session. Be specific: "Play 3 runs building around Corruption+FNP without Inflame/Spot Weakness/Demon Form. Goal: determine whether the exhaust archetype can win independently of Strength scaling."
- **Rebalance the playbook.** Downgrade absolutist language ("non-negotiable," "always," "never") to conditional language when the evidence base is thin.

### 2. Coverage

- **Entity coverage.** Which cards, enemies, bosses, relics, events have heuristic entries? Which don't? Gaps in frequently-encountered entities are higher priority than gaps in rare ones.
- **Archetype coverage.** Are all proven winning archetypes documented? Check win logs — what archetypes actually won, and are they reflected in [[archetypes]]?
- **Act coverage.** Is Act 1, 2, and 3 guidance balanced, or is one act under-documented?
- **Character coverage.** If we're playing multiple characters, is guidance balanced across them?

### 3. Consistency

- **Contradictions.** Do two heuristic files give conflicting advice? (e.g., one card entry says "always play early" while the combat heuristic says "save for later turns")
- **Ontology/heuristic bleed.** Are ontology files (facts) leaking strategic advice? Are heuristic files stating facts that belong in ontology?
- **Stale entries.** Are there heuristic entries that reference outdated information, old run numbers, or strategies that have been superseded?

### 4. Quality

- **Evidence grounding.** Does each heuristic claim cite evidence (run numbers, confirmed kills, observed mechanics)? Unsupported claims should be flagged or demoted.
- **Actionability.** Can the player actually use this guidance? "Be careful with Fiend Fire" is not actionable. "NEVER use Fiend Fire against Thorns enemies — confirmed Run 182 death" is.
- **Signal-to-noise.** Are entries concise? Every sentence should help the player make a decision. History, caveats, and edge cases that don't change behavior should be trimmed.
- **Formatting.** Are entries structurally consistent? Do they follow the patterns established in the category?

### 5. Strategic Framework

The big picture:
- **Are we improving?** Floor-reached trends, win rate, death distribution by act.
- **What's the bottleneck?** Not "play better" but specifically "we keep entering Act 2 without scaling because card reward evaluation doesn't weight it enough" or "we lose to Act 3 elites because we don't adjust pathing when HP is low."
- **Is the knowledge system the right shape?** Would some topics be better consolidated or split? Are index files useful?

## Editing Rules

### What you CAN edit directly
- **Remove clearly wrong claims** (contradicted by evidence, with cited run numbers)
- **Soften absolutist language** when evidence is thin ("non-negotiable" → "strongly preferred", "always" → "usually")
- **Fix contradictions** between files
- **Formatting and structural cleanup**
- **Factual corrections** (wrong damage numbers, wrong mechanics)

### What you CANNOT edit directly
- **Promoting unproven strategies** to high priority. One win is an existence proof, not a tier list change. Write an exploration directive instead.
- **Rewriting tier lists** based on hypotheses. Explore needs to validate first.
- **Adding prescriptive guidance** ("TAKE this card if X") based on < 3 confirming runs. Flag it as worth testing.

The pattern is: Curate identifies the question → Explore generates evidence → THEN the playbook updates. Skipping Explore means replacing one form of overconfidence with another.

## Principles

- **Be willing to delete.** Smaller and accurate beats comprehensive and noisy.
- **Name the bottleneck.** Every plateau has a specific reason. Find it.
- **Measure, don't vibe.** Use run statistics, not impressions.
- **Diversify, don't narrow.** The playbook should expand the player's repertoire, not restrict it to what worked last time.
