# The Ontology/Heuristics Split

The most important structural decision in the system. Getting this wrong contaminates reasoning.

## The Rule

**Ontology entries answer "what is this?"** Heuristics entries answer "what should I do about it?"

If you can imagine a different strategy that would use the same fact differently, the fact belongs in ontology and the strategy belongs in heuristics.

## Atomic Facts Only — Derived Consequences Are Heuristics

Ontology holds **atomic** facts. Combining two of them to produce a third — a worked example or interaction result like "Block resolves before Fossilized Helix, so 6 damage into 5 Block leaves 1 HP for Helix to prevent" — is *reasoning*, not an atomic fact. Even though the derivation is deterministic, it does **not** go in ontology; it lives in heuristics (a topic file or the entity's heuristic). There is no separate layer or name for derived facts: ontology stores Block's timing and Helix's effect as two atomic entries, and a heuristic composes them when a decision needs the result.

Keeping ontology atomic protects its core property — *a correct entry never needs revision, only extension*. A derived fact can go stale when an input changes (a patch alters Block timing and the worked example is now wrong); an atomic fact can't. So the split has three buckets, not two:

- `"X triggers Y"` (a base mechanic) → atomic fact → **ontology**
- `"X before Y, so 6 into 5 leaves 1"` (a composition) → derivation → **heuristics**
- `"avoid X"` (a recommendation) → strategy → **heuristics**

The contamination test below catches the third bucket; this rule adds the second.

## Why This Matters

The split enables compositional reasoning. When facts and strategy are mixed:
- You can't reuse facts in new contexts without importing someone else's strategic opinion
- You can't update strategy without risking factual accuracy
- You can't compose two facts to derive a third because each comes with strategic baggage

Example: "Bash costs 2E, deals 8 damage, applies 2 Vulnerable" is a fact. "Bash is your highest-priority play on free turns" is strategy. If you put both in the same entry, an agent reading about Bash can't separate what Bash DOES from what someone THINKS about Bash.

## The Contamination Test

Read the entry. Circle every sentence that contains "should," "always," "never," "prioritize," "avoid," "best," "worst," or any imperative verb. If any of those sentences are in an ontology entry, they need to move to heuristics.

Read the entry again. Circle every sentence that states a game mechanic, numeric value, or behavioral pattern. If any of those sentences are in a heuristics entry AND they're not already in the companion ontology entry, they should be duplicated to (or replaced by a link to) ontology.

## When Heuristics Become Unnecessary

A heuristic is an admission that the model can't derive the correct action from first principles fast enough. "Don't play Skills against Gremlin Nob" exists because the reasoning chain (Nob gains 3 Strength per Skill → Strength increases all attacks → cumulative damage becomes lethal) takes too long to work through under time pressure.

If the model could reliably derive this in real time from the ontology facts alone, the heuristic wouldn't be needed.

Some heuristics will always be needed (complex multi-turn planning, probabilistic calculations). Others may become unnecessary as reasoning improves. Don't delete them preemptively — delete them when an agent demonstrably derives the correct action without consulting them.

## Edge Cases

- **Analysis methodology** (how to attribute lessons, how to evaluate runs) → ontology, because it describes a process, not a recommendation about game decisions
- **Archetypes** (Corruption+FNP engine, Snecko+expensive cards) → heuristics, because they're strategic recipes even though they describe mechanical interactions
- **Topic files** (combat.md, drafting.md) → heuristics, because they're decision algorithms, even though they reference mechanics heavily
