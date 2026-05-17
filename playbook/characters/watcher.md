# Watcher

## Stances

The Watcher has four stances: **Wrath**, **Calm**, **Divinity**, and **No Stance** (neutral). Stance management is the core of the Watcher's gameplay.

| Stance | Effect | How to Enter | How to Exit |
|---|---|---|---|
| **Wrath** | ALL attack damage dealt is DOUBLED. ALL damage received is DOUBLED. | Eruption, Crescendo, Fear No Evil (conditional) | Vigilance, Inner Peace, Empty Body, Meditate, Fear No Evil (conditional) |
| **Calm** | No combat bonuses. When you LEAVE Calm, gain +2 Energy. | Vigilance, Inner Peace, Meditate, Fear No Evil (conditional) | Eruption, Crescendo (any Wrath entry), or any other stance-entry card |
| **Divinity** | ALL attack damage dealt is TRIPLED. Gain +3 Energy on entry. Exits automatically at end of turn. | Accumulate 10+ Mantra (via Worship, Prostrate, Devotion, Damaru, etc.) | Automatic at end of turn (returns to No Stance) |
| **No Stance** | Neutral. No bonuses or penalties. Starting stance. | Empty Body, or at combat start, or after Divinity ends | Any stance-entry card |

### The Energy Loop (Core Engine)

The Watcher's primary engine is cycling between Calm and Wrath:
1. Enter Calm (via Vigilance, Inner Peace, Meditate).
2. Next turn, exit Calm by entering Wrath (via Eruption, Crescendo). Gain +2 Energy from leaving Calm.
3. Play attacks in Wrath at doubled damage using the bonus energy.
4. Exit Wrath before end of turn if needed (via Vigilance, Inner Peace, Empty Body, Fear No Evil).
5. Repeat.

With Eruption+ (1E) and Calm exit (+2E), entering Wrath costs net -1E (gain 2, spend 1). This means the Watcher effectively gets 2 free energy per cycle compared to staying in no stance.

### End-of-Turn Stance Decision

**Your end-of-turn stance is one of the most important decisions each turn.** It determines your defensive profile AND your energy/damage setup for next turn. Don't default to one stance — think about it.

Consider:
- **What is the enemy doing this turn?** If attacking, ending in Wrath means double damage taken. If buffing/debuffing, Wrath is free damage next turn.
- **What do I need next turn?** Ending in Calm means +2E next turn when you exit. Ending in Wrath means doubled attacks immediately but doubled incoming.
- **Do I have an exit next turn?** If you end in Wrath, you need a Calm-entry card in your next draw to escape. If your deck is thin on exits, ending in Wrath is gambling.
- **Is this a boss fight?** In boss fights you can be more aggressive with Wrath since HP management is looser.

**The dangerous default is staying in Wrath and hoping.** If you can't confidently exit Wrath next turn, don't end in it.

### Stance Sequencing

- **Play cards that trigger on stance change BEFORE changing stance.** Cards like Flurry of Blows return from discard on stance change — they must already be in the discard pile for the trigger to work.
- **Check individual card files for play-order rules.** Many Watcher cards have specific sequencing requirements (e.g., Meditate ends your turn, Wave of the Hand must precede block cards).

## Starting Deck

- 4 Strike (Attack, 1E, 6 damage)
- 4 Defend (Skill, 1E, 5 block)
- 1 Eruption (Attack, 2E, 9 damage, enter Wrath)
- 1 Vigilance (Skill, 2E, 8 block, enter Calm)

**Starting Relic: Pure Water** — adds 1 Miracle to hand at the start of each combat.
