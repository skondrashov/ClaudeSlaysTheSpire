# Attribution

Where to put lessons from gameplay. Getting this wrong scatters knowledge across entries where it can't be found or compounds incorrectly.

## The Rule

Attribute lessons to the entity that CAUSED the outcome, not the context where it happened.

**Test:** "Would this lesson apply in a different context?" If yes, it doesn't belong on the context.

## Examples

| What happened | Wrong attribution | Right attribution | Why |
|--------------|-------------------|-------------------|-----|
| Fiend Fire exhausted block cards during Champ fight | Champ heuristic: "keep block cards" | Fiend Fire heuristic: "don't exhaust block cards you'll need" | Same mistake would happen in any fight with Fiend Fire |
| Took too much damage from Gremlin Nob because played Skills | Combat heuristic: "be careful with Skills" | Gremlin Nob heuristic: "play ZERO Skills" | This is Nob-specific, not a general combat rule |
| Died to Hexaghost burns because no way to handle status cards | Hexaghost heuristic: "bring burn handling" | Hexaghost heuristic (correct) | This IS Hexaghost-specific — burns are its mechanic |
| Didn't have enough block cards entering Act 2 | Act 2 heuristic: "need block" | Drafting heuristic: "draft sufficient block by end of Act 1" | The drafting decision happened before Act 2 |

## Attribution Levels

From most specific to most general:

1. **Entity-specific** → per-entity heuristic file (cards/fiend-fire.md, enemies/gremlin-nob.md)
2. **Category-level** → category-wide pattern (enemies generally, cards generally)
3. **Topic-level** → cross-cutting document (combat.md, drafting.md, map.md)
4. **System-level** → pipeline/process change (agent goals, pipeline cadence)

**Default to the most specific level that captures the lesson.** If a lesson applies to one entity, put it there. If you find yourself writing the same lesson on three entities, promote it to a topic file.

## Common Mistakes

- **Context attribution.** "We lost to The Champ" when the actual cause was a card choice or drafting decision many floors earlier. The Champ was the context, not the cause.
- **Vague attribution.** "We need better scaling" attributed to no specific entry. WHERE should this guidance go? Drafting? Archetypes? A specific card tier list?
- **Double attribution.** Same lesson written on both the card and the enemy. Pick one. If it's really about the card's behavior, put it on the card. If it's really about the enemy's pressure, put it on the enemy.
