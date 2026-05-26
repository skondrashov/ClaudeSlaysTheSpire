# The Knowledge System

A persistent web of information that an autonomous agent reads from, writes to, and navigates across many sessions. The agent is ephemeral and goal-driven. The knowledge web is what persists and accumulates. Learning happens through the interaction between them.

---

## Ontology and Heuristics

The web contains two kinds of knowledge, and only two.

### Ontology

Facts about the environment. What exists, how it behaves, how things relate. Deterministic, composable, permanent.

"Vulnerable causes the target to take 1.5x damage from attacks."
"Jokers evaluate left to right."
"The draw pile reshuffles from the discard pile when empty."

Ontological knowledge is always worth recording. It composes — knowing A and B lets you derive what happens when A and B interact. A correct ontological entry is never revised, only extended. The aspiration is completeness: a full ontology of the domain means you know everything there is to know about how the world works.

### Heuristics

Everything else. Cached reasoning about how to navigate the environment. Provisional, contextual, bounded by the intelligence of whatever produced them.

"Don't end your turn in Wrath."
"Prioritize xMult jokers in the late game."
"Kill scaling enemies fast."

A heuristic is an admission: the reasoning engine cannot reliably derive the right action from ontology alone in real time, so here is a pre-baked conclusion. Heuristics are useful — they let the agent act well in situations it can't fully think through. But they are fundamentally limited by the intelligence of whoever wrote them.

The ideal trajectory: as the agent improves at reasoning (or as the model improves), heuristics become unnecessary and fall away. A perfectly intelligent agent with complete ontological knowledge needs zero heuristics — it derives optimal play from first principles every time. Heuristics exist in the gap between what you know about the system and what you can figure out from what you know.

### The Collapse

This two-part distinction is exhaustive. Everything in the web is either a fact about the world (ontology) or a provisional shortcut for navigating it (heuristic). This includes knowledge at every level of meta:

- **Action heuristics** — how to act in the domain. "Kill scaling enemies fast."
- **Epistemic heuristics** — how to learn about the domain. "Use isolation to study unfamiliar enemies." "Test mechanics by replaying seeds."
- **Querying heuristics** — how to navigate the web itself. "Look up the enemy file before planning a fight." "Follow references to discover related entries."

These are all heuristics — provisional, improvable, replaceable by better reasoning. The only thing that isn't a heuristic is a fact. Epistemology is heuristics of ontology: strategies for acquiring facts are themselves provisional shortcuts, not truths.

The epistemic heuristics (learning strategies) apply equally to both kinds of knowledge. You can use isolation or testing to discover an ontological fact ("does Vulnerable apply before or after the triggering hit?") or to validate an action heuristic ("does rushing Lagavulin actually work better than blocking?"). The strategies are the same regardless of what kind of knowledge they produce.

---

## The Agent

There is one kind of agent. It gets a goal, reads from the knowledge web, takes actions in the world, and writes back to the web. Different goals produce different behavior:

- **"Win this run"** — requests ontology and heuristics relevant to the current state, reasons, acts. Learning is incidental: notices gaps in passing, records them, but attention is on performance.

- **"Learn how Reptomancer works"** — routes toward that fight, observes carefully, maybe sacrifices the run to test hypotheses. Primary output is ontological entries, not progress. This is isolation as a learning strategy.

- **"Fill in missing status effect entries"** — plays many runs with attention on cataloging. Game performance is secondary to building ontology.

- **"Review what went wrong last run"** — reads the event log, identifies whether mistakes were ontology gaps (didn't know how something worked) or reasoning failures (knew the ontology but drew the wrong conclusion). Updates the web accordingly — new ontology for the first, new heuristics for the second.

- **"Assess what we're bad at and plan what to learn next"** — looks at the whole web, identifies systematic gaps, recurring failures, dead-weight heuristics, and decides where to direct attention.

- **"Improve the knowledge web"** — queries the web to understand its own structure, identifies problems (gaps, contradictions, bloat), takes editorial actions. The web is the environment; its structure is the ontology; the actions are edits.

These are not different agents. They are the same agent with different goals, taking different paths through the same knowledge web.

---

## The Queue

When the agent is pursuing one goal and notices something it doesn't understand, it does not derail. It makes a note and continues.

"Reptomancer daggers — what's the mechanic? Seed: XYZ, floor 34."
"Third time Malleable surprised me. Need to actually look this up."
"That joker interaction was weird. Investigate: does Mime copy the enhanced chip value or base?"

The queue is the bridge between the agent-as-performer and the agent-as-learner. Entries carry context: where encountered, how urgent, whether recurring. Recurring entries naturally rise in priority — if you keep running into something you don't understand, that's a strong signal.

A session produces two outputs:
1. Progress toward the goal (won or lost, how far, what happened)
2. Queue entries (things noticed but not pursued)

A learning session consumes queue entries and produces web updates.

---

## Gap-Filling Strategies

Epistemic heuristics — how the agent acquires new knowledge. These are finite and describable. They work for filling ontological gaps or validating/developing action heuristics equally.

### Isolation

Direct attention at one thing. Ignore everything else — outcomes, efficiency, other concerns. "This run I'm only paying attention to how stance changes work." You might play badly because your attention is elsewhere, and that's fine.

### Testing

Set up a specific scenario to answer a specific question. More deliberate than isolation — you have a hypothesis and engineer a situation to confirm or reject it. Seeds enable exact replay.

### Observation

Watch what happens without a specific hypothesis. Passive data collection. You encounter something new, record what it did. One clean observation often suffices for an ontological fact.

### Inquiry

Reach for existing information. Look it up in the web, search externally, read documentation. The agent asks a question and the web either has an answer or doesn't.

### Coaching

Ask someone who knows. A human provides information the agent couldn't acquire on its own (or only very slowly). Can inject ontology ("daggers have 1 HP each") or heuristics ("kill the daggers first").

### Reflection

After the fact, examine what happened and extract meaning. This is where heuristics get proposed ("every time I ignored the daggers, I lost") and where bad heuristics get identified ("I followed this rule and it cost me").

---

## Querying the Web

The hardest problem in the system. The agent's ability to navigate its own knowledge determines how much value that knowledge provides. A complete ontology you can't query is worthless.

### The Impedance Mismatch

Human recall is associative — you encounter something and related knowledge activates by similarity, context, recency. LLM internal knowledge works similarly: say "Vulnerable" and everything the model knows about Vulnerable is available without explicit lookup.

But the knowledge web lives in text files. Files have addresses, not associations. You navigate by path and name, not by relevance. The structure of the files IS the query interface — naming conventions, directory structure, and reference patterns determine what's findable and what's buried.

This means the web's structure is not just an organizational convenience. It is the primary constraint on how effectively knowledge gets used. Every structural decision (file granularity, naming, hierarchy, cross-referencing) is a decision about queryability.

### Querying Heuristics Are Domain-Specific

In STS: "look up the enemy you're facing" is an obvious querying heuristic because combat is discrete encounters with named entities. In Balatro: "check boss blind constraint for this ante" because pressure comes from scoring thresholds. In code review: "look up the module's API contract."

The meta-heuristic "look up what you're interacting with" transfers across domains. But what counts as "what you're interacting with" is entirely domain-specific. Entering a new domain means building querying heuristics from scratch alongside the ontology itself.

### The Web Describes Itself

The web contains entries about its own structure — and these are just ontology. "Enemy files live in playbook/enemies/ and contain attack patterns and HP values" is a fact about the environment where the environment is the web. An agent improving the web queries the web to understand how it's structured, just as a player queries the web to understand how enemies work. Same mechanism, different domain.

### Conventions as the Generalizable Layer

What transfers across domains isn't specific queries but structural conventions: naming schemes, file granularity standards, reference formats, index files. Good conventions make querying heuristics easier to develop. Bad conventions force the agent to memorize where things live rather than derive it from patterns.

---

## The Flow

```
Agent spawns with a goal
    |
    v
Queries the web (ontology + heuristics relevant to goal)
    |
    v
Takes actions in the world
    |
    v
Observes results
    |
    v
Notices gaps — things it needed to know but didn't
    |
    v
Either: fills the gap immediately (observation, inquiry)
   Or: records it to the queue (don't derail, investigate later)
    |
    v
Session ends → progress + queue entries
    |
    v
Next session's goal may be informed by the queue
    |
    v
Ontology grows permanently. Heuristics are proposed, tested, and sometimes discarded.
```

---

## The Ceiling

The quality of decisions is bounded by two things:

1. **Ontological completeness.** If you don't know how something works, you can't reason about it. This is fillable — observe more, ask more, test more.

2. **Reasoning capacity.** Given complete ontology, can the agent derive the right action? This is the hard ceiling. A heuristic exists precisely when the answer is "no, not reliably." Better models raise this ceiling. When it rises, heuristics that were necessary become unnecessary and the web sheds them.

The system should be honest about which ceiling it's hitting. "I lost because I didn't know Flight halves damage" is ceiling 1 — fixable by recording the ontology. "I lost because I couldn't figure out the right turn sequence even though I knew all the mechanics" is ceiling 2 — only addressable by being smarter, or by caching the conclusion as a heuristic.

---

## Sanity Check: Two Domains

**Slay the Spire.** Ontology: card effects, enemy patterns, relic triggers, status effect interactions. Heuristics: "rush scaling enemies," "take Offering in Act 1," "don't play powers against Awakened One P2." Querying heuristics: "look up the enemy before combat," "check relic interactions with current hand," "review boss mechanics before Act boss floor." The agent plays to win, notices gaps, queues them, fills them later.

**Balatro.** Ontology: scoring formula, joker effects, left-to-right evaluation, boss blind constraints, tarot/planet interactions. Heuristics: "prioritize xMult in late game," "don't break a flush build for a single high-chip card." Querying heuristics: "check boss blind constraint before building for this ante," "look up joker interactions when considering shop purchases." Same flow, different domain-specific queries.

Both fit the same system. The ontology is domain-specific, the action heuristics are domain-specific, even the querying heuristics are domain-specific. What's shared: the flow, the two-kind distinction, the queue mechanism, the epistemic strategies, and the structural conventions that make any domain's web navigable.
