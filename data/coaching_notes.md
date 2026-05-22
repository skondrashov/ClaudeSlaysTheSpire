# Human Coaching Notes for Analyst

These notes are from human coaching and should be incorporated into playbook updates during the next analyst run. After processing, clear the notes that have been addressed.

## Pending

(No pending items.)

## Addressed (Runs 174-177 analysis)

### Watcher card sequencing is terrible (Runs 174-177) -- ADDRESSED
- Created playbook entries for ALL Watcher cards encountered with explicit PLAY ORDER sections in each: flurry-of-blows.md (ALWAYS play before stance change), miracle.md (ONLY play when energy is useful), eruption.md, vigilance.md, crescendo.md, inner-peace.md, fear-no-evil.md, meditate.md (play LAST -- ends turn), wave-of-the-hand.md (play BEFORE block cards), empty-body.md
- Added CARD SEQUENCING RULES section to mechanics.md (Watcher Stance Mechanics) with 5 explicit rules
- Added Watcher-Specific Strategy section to strategy.md

### Transient Shifting mechanic was wrong in playbook -- FIXED BY HUMAN, VERIFIED BY ANALYST
- Verified: transient.md correctly describes Shifting as "LOSES that much Strength for the rest of the turn" and "Attacking is strictly better than blocking"
- No incorrect info re-introduced. Entry is accurate.

## Addressed (Run 152 analysis)

### Curse management and event routing (Run 152 - Silent) -- ADDRESSED
- Created `playbook/events/sssserpent.md` with decision framework for curse + shop routing
- Added "Curse Management and Shop Routing" section to `playbook/strategy.md`

### Draw card sequencing (Run 152 - Silent) -- ADDRESSED
- Noted in run log. Fix was applied in player prompt and cmd.py (auto-stops sequences on draw effects). The run log shows the player did play Backflip first then plan the rest in most fights, suggesting the fix was partially effective. Monitoring.

### Slime Boss — missed split timing (Run 152 - Silent) -- ADDRESSED
- Added "SPLITTING A SLIME THAT IS ABOUT TO ATTACK IS YOUR BLOCK" section to `playbook/bosses/slime-boss.md` under STRATEGY

### Gremlin Gang fight analysis (Run 152 - Silent) -- ADDRESSED
- Created `playbook/enemies/gremlin-gang.md` with kill priority order, gremlin types, and strategy
- Updated `playbook/enemies/_index.md`

## 2026-05-21 — Human Coaching: Watcher Fundamentals

**Source:** Human override of Curate's Ironclad pivot.

**Key insight:** Watcher is actually the STRONGEST class at A0. Our 0/14 record means our heuristics are fundamentally wrong, not that the class is weak.

**The fundamental error:** We've been playing Watcher as "Calm→Wrath cycling for incremental damage each turn." This is WRONG.

**Correct pattern:** Watcher is a SETUP → ONE-SHOT engine:
1. Stay in Calm. Generate block. Draw cards. Accumulate energy (+2E from Calm exit).
2. Wait for the right moment — when you have enough damage cards in hand.
3. Enter Wrath and deal 100+ damage in ONE EXPLOSIVE TURN. Kill everything.
4. Exit Wrath (or everything is dead so it doesn't matter).

**Why this matters:**
- Fights should end in 2-3 turns, not 6-7 turns of chip damage
- HP attrition stops being a problem if fights are SHORT
- "No healing" is irrelevant when you take minimal damage per fight
- Hex/Chosen/status effects matter less if the enemy dies before they accumulate
- Full block turns in Calm mean near-zero damage taken on setup turns

**What needs to change in heuristics:**
- Combat heuristic: reframe from "energy cycling" to "setup + burst"
- Drafting: prioritize cards that enable one-shot turns (high damage, draw, energy)
- Fight planning: calculate "what do I need in hand to kill everything in one Wrath turn?"

**Status:** UNADDRESSED — needs Curate to rewrite Watcher combat approach.
