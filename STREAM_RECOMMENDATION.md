# Stream UI Recommendation

Opinions on what the overlay should become, thought from scratch. The canvas is fixed by the format: the game shrinks into the top-left, leaving a full-height **side bar** (~25% width) and a full-width **bottom bar** (~20-25% height). The question is what those two surfaces are *for*.

## The framing problem

A Twitch viewer arrives mid-run and gives us about ten seconds. In those ten seconds, almost every "AI plays a game" stream communicates the same thing: a model is pressing buttons and narrating. That is not this project, and the UI's only real job is to make the difference visible without anyone reading an About page.

The difference is: **the player is reading a book that the system wrote about its own past failures, and the book is getting better on screen.** Everything below follows from making that one sentence ambient.

So the two surfaces get distinct jobs:

- **Side bar: NOW.** What is the agent doing this second, and why.
- **Bottom bar: THE ARC.** Where this run sits in a campaign, and where the knowledge came from.

A viewer who only watches the side bar should understand the current fight. A viewer who only watches the bottom bar should understand the project.

## Side bar (NOW)

Top to bottom, in priority order:

1. **Title + one-line thesis.** Not just "CLAUDE SLAYS THE SPIRE" but a permanent subtitle: *"playing from a knowledge base it writes itself"*. Ten words, always visible, does the framing job for every drive-by viewer. The current header spends this space on the title alone.

2. **The decision feed (keep, but invert the hierarchy).** Right now entries lead with the command badge and the reasoning hangs below it. Invert: the *reasoning* is the content, the command is the annotation. Viewers don't care that it was literally `play Bash 0`; they care about "Bash first so Vulnerable amplifies the next two hits." One to two clamped lines per entry, command badge small and to the right. The current full kill-math dumps are wonderful for us and illegible at 1080p compression; clamp with expansion only during idle moments (shops, map).

3. **A win% gauge with memory.** The agent already labels win% at every meaningful decision. Render it: a simple meter plus a sparkline of the last ~20 labels. This is the single most engaging element we are not showing. It creates stakes ("it thinks it's at 26%"), it makes calibration into content (the sparkline crashing when a fight goes wrong is the drama), and it is honest: these are the agent's actual beliefs, which an audit will later grade. Add the delta annotation it already produces ("-10: entered elite low").

4. **Knowledge-in-use panel.** When the player recalls a page, show it: entry title, the two or three lines it read, with a book icon. This is the thesis made visible. When the player then follows the rule ("kill the Mystic first"), the viewer just watched the book work. When it dies to something, the next stream shows the same panel containing the *new* sentence that death produced. Nothing else we could render says "this is a learning system" as directly. (The data already exists: every recall is logged with its handles; the bridge can carry the text.)

## Bottom bar (THE ARC)

The bottom bar currently cycles between panel sets on a timer. I'd stop cycling the important things; a viewer who tabs in during the wrong 20 seconds misses the entire point. Lay it out as four fixed zones:

1. **Campaign strip (the headline).** The last ~15 runs as compact markers: ascension level, floor reached, win/death, one-word cause. The current run draws live at the right edge, climbing as it progresses, with the best-by-ascension waterline marked. This single element communicates progress-over-time, which IS the project. It also makes losing legible as part of an arc instead of as failure: the strip visibly trends upward across sessions. (Best is ordered by ascension now: F36 at A9 over a win at A5; the strip should sort visually the same way.)

2. **"Recently learned" ticker.** Rotating one-liners sourced from the changelog and observations: *"After run 233: draw effects are dead once Battle Trance resolves."* / *"New page: Neow — the floor-0 blessing."* Each ties a lesson to the run that taught it. This is the flywheel narrated in present tense, and it writes itself from data we already produce.

3. **The book card.** Knowledge counts (entries by layer), the site URL, and a standing line: *"every entry browsable at claudeslaysthespire.org."* The site is the second screen; the stream should constantly hand viewers to it. Keep this compact; counts alone mean little to a new viewer, so the URL and the framing line matter more than the numbers.

4. **Deck + relics (contextual, may cycle).** The current DECK panel is genuinely useful during draft decisions and dead weight otherwise. This is the one zone where cycling is fine: deck during reward/shop screens, run history table during fights, post-mortem audit summary when a run ends (the agent-watch mode already exists for this; lean into it between runs, when the screen is otherwise a menu).

## Moments, not just panels

The strongest version of this UI reacts to events rather than laying everything out statically:

- **Fight start:** flash the enemy's expected-cost row ("Spheric Guardian: 30-50 HP even played well") next to its intent. Sets stakes instantly.
- **Run end:** take over the bottom bar with a three-line post-mortem (cause, the decisive turn, what the audit will examine). On death this is the emotional beat that converts a loss into the project's story; on a win it's the celebration with provenance.
- **Knowledge edit (between runs):** when an audit/curate session lands, a brief "the book changed" moment showing the diff headline. Viewers who stay across runs see the loop close.

## Style notes

- One consistent color per information kind across both bars: combat math, knowledge/book, routing, meta. The current palette is close; formalize it.
- Type sizes assume Twitch's 1080p compression: nothing meaningful below ~18px equivalent. The current action-feed columns flirt with illegibility.
- Mojibake (the `RUN 231 � DEFEAT` banner) and placeholder reasons are credibility leaks for a project whose pitch is rigor; treat display bugs as P1 the way we now treat interface bugs.
- Resist adding chat-driven features until the static layer is right, but the natural ones later: `!why` reposts the current reasoning, `!book <entity>` links the site page, `!run` links the campaign strip data.

## What I would build first

Ordered by (viewer value × implementation cost):

1. Permanent thesis subtitle (an hour, mostly CSS).
2. Win% gauge + sparkline (the labels already flow through the decision events).
3. Campaign strip (run_stats has everything; one canvas element).
4. Knowledge-in-use panel (recall events already carry handles; add text payload).
5. Recently-learned ticker (changelog exists; needs a small formatter).
6. Fight-start expected-cost flash (the heuristic pages now carry cost rows).
7. Stop cycling the core panels; keep cycling only zone 4.

Items 1-3 alone would make a cold viewer understand the project in under a minute, which no amount of polish on the current layout achieves.
