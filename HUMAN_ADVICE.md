# Human Advice Log

Historical record of knowledge explicitly injected into the system by a human player. This file is NOT read by the pipeline — it exists purely for provenance tracking. Everything here has been incorporated into the player system through player.md and strategy.md.

---

## 2026-05-09 — Session 1: The Reasoning Rework

**Context:** 130+ runs, 0 wins, floor average regressing from 25-26 to 23.1. The self-learning loop (analyst/strategist) had stalled. The strategist identified arithmetic errors as the bottleneck, but the human identified a deeper issue: the player's fundamental reasoning model was wrong.

**Human's key insight:** "One of the most consistent mistakes is thinking of fights with low health as different from fights with high health. It doesn't actually make any sense to take more or less damage in either scenario — health is a resource that carries through the whole act."

### Heuristics provided:

**1. HP is an act-level resource (not per-fight)**
- "The only time you can spend it shamelessly is if you're in a boss fight"
- "You can also afford to take 6 damage if you're at full health because of burning blood"
- "Or 25 damage before a boss cause of pantograph if you have it"

**2. Full block is the default combat algorithm**
- "The basic combat strategy is really as simple as 'full block if you can' a lot of the time"
- "There's some exceptions like cultists because they scale so aggressively"
- "You eventually have to make tradeoffs and let 1 or 2 hp through, but not in A0"

**3. Full act pathing before the first fight**
- "You're supposed to know how many elites, shops, and campfires you're hitting before you select the first fight in every act. We've simply never done that"

**4. Act 1 card evaluation is a tier list**
- "You nearly always have the same deck when you start a run, so a memorized tier list is just really good in the first act"
- "That tier list generally looks like 'take attacks so you don't die to gremlin nob'"
- "They're not always identical because of neow but yes" (re: starting deck)

**5. Draft for known encounters**
- "You can beat the slime boss for free if you just take any cards that say 'when you draw a status card' on them"
- "Knowing what fights are guaranteed to happen and picking cards and relics accordingly"
- "It's a very deep set of rules and you don't need any of them in a0 but it's important to understand that category of heuristic"

## 2026-05-12 — Session 2: Full Block Refinement

**Human's addition to full block:**
- "Killing something that's attacking is always something you look into. So there's alternatives."
- "In general the pipeline is not good at considering alternatives"
- "It's basically a template you would fill out to determine the paths toward full block, and you'd obviously prefer to kill something and then full block if you can"

## 2026-05-12 — Session 3: Hard Rules Abolished

**Context:** The player had accumulated 9 "Hard Rules" — NEVER-do prohibitions added after specific deaths. The human identified this as a fundamentally wrong approach for games.

**Human's key insight:** "Hard rules in general just aren't how games work. If the player doesn't understand how to use something it's something they need to explore, not just write a rule about with like one or two runs of data."

### Feedback on each hard rule:

**1. "NEVER TAKE RUNIC DOME"**
- "It's not like runic dome is something the developers put in to trick the player."
- "Realistically, what it means is we can't use runic dome until we've memorized all of the attack patterns in the game."
- Human says this guidance belongs under the Runic Dome playbook entry, not as a blanket prohibition.

**2. "ALWAYS USE CARD NAMES"**
- "It's not a gameplay rule, it's how to interact with the game, and ideally the player doesn't have to worry about it because the system makes it easy."
- Infrastructure issue, not gameplay. The system (cmd.py) already handles name→index resolution transparently.

**3. "UPGRADE AT EVERY REST SITE where HP is above threshold"**
- "Why is that a rule? Obviously you upgrade at a rest site if you don't need to rest. There's no 'HP threshold', everything is situational in games."

**4. "NEVER PLAY unupgraded True Grit with key cards"**
- "Kind of true but... never? Everything is situational."

**5. "USE ALL POTIONS below 40% HP"**
- "The only rule I kinda like, though again optimal potion use is much more complicated than that, and 40% is an arbitrary threshold."

**6. "NEVER PLAY BRUTALITY in long fights"**
- "Useless, how do you know if the fight is long?"

**7. "NEVER EXHAUST Spot Weakness/Reaper"**
- "Doesn't make sense on a lot of levels."

**8. "NEVER PLAY 3-cost Power turn 1 when attacked"**
- "Kind of reasonable but it belongs to the specific powers in question, and also again 'never' is stupid."

**9. "NEVER PLAY Corruption vs Guardian without Dead Branch/FNP"**
- "Specific to the point of being useless even aside from saying 'never'. Obviously you sometimes want to play corruption and sometimes you don't, and what does the guardian have to do with anything?"

### Resolution:
Hard Rules section removed from player.md entirely. Relevant guidance distributed as soft context to individual card/relic playbook entries (runic-dome.md, corruption.md, true-grit.md, brutality.md, etc.). Card name usage retained in the "Card Names and Enemy Targeting" section as infrastructure guidance, not a gameplay rule.

## 2026-05-12 — Session 4: Elite Readiness + Act 1 Attack Aggression

**Context:** Run 141 died Floor 8 after taking Sentries elite with a starter-quality deck. Run 140 skipped Wild Strike early. The human identified a critical missing heuristic: you must be aggressive about taking attacks in early Act 1 to prepare for elites.

### Human's key insights:

**1. Elites on purpose is correct, but you need attacks first**
- "Running into elites on purpose is correct, but you also have to be really aggressive about taking attacks."
- "You need to have a few attacks better than strikes in your deck by the middle of act 1" — this is a fundamental requirement, not optional.
- Skipping Wild Strike in Run 140 was a mistake: "it's a massive 1 [energy] damage card" (12 damage for 1 energy, double Strike's 6). In early Act 1, raw damage to beat elites matters more than Wound downside.

**2. Specific elite fight strategies are needed — detailed tactical plans, not just "needs AOE"**

**Gremlin Nob:**
- "Simplest in a way — you just have to have good attacks before you get there and not too many skills."
- "After you've seen the Nob you can grab other stuff (elites don't repeat twice in a row)."
- Implication: pre-Nob, bias toward attacks. Post-Nob, safe to pick up Skills.

**Lagavulin:**
- "Partly obvious — you get setup turns while it's asleep."
- "But in practice you also have to know that you need to hit it hard because the scaling is really rough otherwise — the debuffs are killer."
- The -1 Str/-1 Dex per Siphon Soul cycle makes the fight unwinnable if it goes long.

**Sentries:**
- "By far the most tactical."
- "You have to plan out attacks in such a way that you're hitting the correct target."
- "You rarely if ever kill the middle first so you avoid 20hp damage turns since first and last are synced."
- "Once you have 2 sentries left you have to kinda guess which one you're gonna be able to kill on the turn it's attacking."
- "You have to decide if it'll take you 2 or 3 or 4 turns to kill one of them and target appropriately, so you get to skip block on the turn that you kill one of them ideally."
- Key tactic: time your kill of a Sentry to coincide with its attack turn — killing it removes that turn's damage, effectively giving you a free turn.

**3. Strategist instructions (for next strategist run at ~150)**
- Work through exact mechanics of ALL Act 1 elite fights
- Make sure playbook entries for Nob, Lagavulin, and Sentries have really in-depth tactical plans
- Incorporate the "need attacks better than Strikes by mid Act 1" heuristic into strategy.md
- Address the tension between "take attacks aggressively early" and "don't bloat deck"

### Web Research: Act 1 Ironclad Expert Heuristics

The following was gathered from expert guides (Jorbs, Baalorlord, Reddit r/slaythespire, Steam guides, wiki) to supplement the human's advice:

**Card Drafting:**
- Offering is widely considered the single best Ironclad card — take whenever offered
- Bludgeon (32 damage for 3E) removes the need to pick up mediocre attack commons — "like taking 3 Twin Strikes that only cost one draw"
- Battle Trance (draw 3-4 for 0E) is outstanding Act 1 tempo
- Uppercut (13 dmg + Weak 1 + Vuln 1 for 2E) can replace Bash as Vuln source, freeing Bash from needing first upgrade
- Anger (0E for 6 damage, copies itself) can solo the Hexaghost fight by turn 6-7 with 3-4 copies
- Iron Wave trap: taking 3+ Iron Waves is a common mistake — they're fine as first pickup but bloat the deck
- Wild Strike: research says "generally avoid unless exhaust synergy" but human overrides this for early Act 1 — raw damage to beat elites outweighs Wound cost

**Elite Tactics (research confirms human advice + adds numbers):**
- Gremlin Nob: 82-86 HP. Gains +2 Str per Skill played. Need ~20-25 damage/turn over 4 turns. Bash is the ONE Skill worth playing turn 1 (Vuln amplifies all attacks 50%, worth the +2 Str). Inflame is a Skill — do NOT play vs Nob (+2 Str you gain is exactly canceled by +2 Nob gains). Flame Barrier is one of few defensive Skills worth considering (deals damage back).
- Lagavulin: 109-115 HP. 8 Metallicize while asleep. 3 free setup turns. Do NOT attack during sleep unless you deal >8 per hit (Metallicize blocks it). Siphon Soul: -1 Dex then -1 Str, repeats every 3 turns. Must kill before 2nd Siphon Soul or fight becomes unwinnable. Demon Form on sleep turn 1 = +6 Str by wakeup.
- Sentries: 38-42 HP each, 1 Artifact each. Outer two start by shuffling Dazed, middle attacks (9 dmg). They alternate each turn. Kill OUTER first (not middle) — killing middle means both outers attack same turn (18 dmg). First deck cycle (turns 1-3) is your best damage window before Dazed pollutes draws. Evolve completely neutralizes Sentries' gimmick.

**Strategic Principles:**
- Fight 2-3 elites in Act 1, not 0-1. Each elite = relic + better cards + gold. Dodging elites = arriving at boss with starter-quality deck.
- Take first 1-2 damage cards aggressively (floors 1-3), then become selective. Starter deck deals ~15 damage/turn, need ~20-25 for elites.
- Elites don't repeat back-to-back — after fighting Nob, safe to take Skills.
- Never rest at campfires in Act 1 (almost never). Burning Blood heals 6/fight. Upgrading Bash > 30% HP heal.
- HP is a resource to spend: 10 HP in a hallway fight to save a campfire rest (upgrade instead) is profitable.
- Target Act 1 ending deck: 12-18 cards. 25+ is bloated.
- Skipping card rewards is one of the most important "picks" — if nothing helps upcoming fights, skip.

**Boss-specific research additions:**
- Slime Boss: Ideal is to get close to 50% then burst past to trigger split at low HP. Slam (35 dmg) comes turn 2 — need 40+ HP entering.
- Hexaghost: Divider turn 1 scales with current HP (80 HP = 6x6 = 36 damage). Long fight (~8-9 turns), needs sustained ~28-30 damage/turn. Burns upgrade to 4 damage after first Inferno — soft timer.
- The Guardian: Mode Shift at 30 damage (increases by 10 each cycle). In Defensive Mode, Sharp Hide deals 3 Thorns per attack played — do NOT play attacks. Play Skills and Powers during Defensive Mode, unleash attacks during Offensive Mode. Few large hits > many small hits (Bludgeon ideal).
