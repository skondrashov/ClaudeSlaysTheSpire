# The Guardian

**Core rule:** Plan burst damage to trigger [[buffs/Mode Shift]] on lethal attack turns (32-damage and 5x4=20 attacks), canceling them. Do NOT over-exhaust -- this is a 12-14 turn fight.

## Preparation Checklist

1. One big block source for the 32-damage turn ([[cards/Impervious]], double [[cards/Metallicize]] + [[debuffs/Weak]], or mass block cards)
2. Burst damage for fast Mode Shift triggering ([[cards/Bludgeon]], [[cards/Carnage]], [[cards/Headbutt]] loops)
3. Passive block for the long fight (Metallicize is the best card; double Metallicize is exceptional)
4. Deck manipulation (Headbutt+ to guarantee key cards when needed)
5. Enough cards in deck to last 12+ turns -- do NOT over-exhaust

## Strategy

- **Turn 1 setup:** Play Metallicize, [[cards/Inflame]], or Powers on the first free turn
- **Attack Mode:** Block on attack turns (especially 32-damage). Damage on free turns. Refresh [[debuffs/Vulnerable]] with [[cards/Bash]] on free turns.
- **Defensive Mode:** Block first to absorb [[buffs/Sharp Hide]] retaliation, then play Attacks. Powers are safe.
- **Headbutt loops:** Top-deck Carnage+ for burst turns, Bash+ for Vulnerable refresh, Impervious for the 32-damage turn
- **Know your block ceiling:** If maximum block is less than 32, stop exhausting immediately

## What NOT to Do

- Over-exhaust (a 3-card deck cannot block 32 damage)
- Play unupgraded [[cards/True Grit]] (random exhaust destroys key cards)
- Ignore Sharp Hide (3 Attack cards in Sharp Hide mode = 9 HP)
- Play [[cards/Corruption]] without [[relics/Dead Branch]] or [[cards/Feel No Pain]] (burns through all Skills in 5-6 turns, leaving defenseless for second half)
- Waste Impervious on small attacks (save for 32-damage or 5x4=20)
- Play [[cards/Fiend Fire]] as primary exhaust engine (thins deck catastrophically)
- Play [[cards/Sever Soul]] (exhausts ALL non-Attack cards)
- Enter with fewer than 2 reliable block cards

## Character Matchups

**[[characters/Silent]]:** Mode Shift + Shivs: multiple Shivs accumulate toward Mode Shift quickly. [[cards/Cloak and Dagger]] (2 Shivs) is critical. [[cards/Noxious Fumes]] played Turn 1 deals 78 total poison over 12 turns. [[cards/Wraith Form]]: do NOT play early (Dex penalty compounds over 12+ turns). [[debuffs/Poison]] Potions bypass Sharp Hide.

**[[characters/Defect]]:** Frost wall sustains through the long fight. [[cards/Barrage]] with full orbs (5+) triggers Mode Shift in 1-2 plays. [[cards/Echo Form]] early on a free Charging Up turn. [[cards/Coolheaded]] cycling finds cards when needed.

**[[characters/Watcher]]:** The stance dance engine is powerful against Guardian but uniquely risky. Key considerations:
- **NEVER enter Wrath without a guaranteed exit in hand.** Sharp Hide deals 3 damage per attack played; in Wrath this effectively costs 6 HP per attack (doubled incoming + retaliation). If the next turn has no Wrath exit, you take doubled Guardian attacks (32 damage becomes 64, multi-hits become lethal).
- **Wrath exit density matters.** Death follows when the only Wrath exit (e.g. Tranquility) has been exhausted and the remaining exit (e.g. Vigilance) is stuck in the draw pile. Minimum 2 Wrath exit sources in deck for this fight. If only 1 exit source exists, do NOT enter Wrath unless the exit card is in hand.
- **Mode Shift burst:** Eruption+ (in Calm) -> attacks in Wrath -> Vigilance to Calm is the ideal cycle. Doubled attacks trigger Mode Shift quickly. But do NOT batch the whole sequence in turn() — use card names, not indices (see combat.md rule 6).
- **Sharp Hide in Wrath:** Playing 3 attacks in Wrath during Sharp Hide costs 9 HP from retaliation alone. Limit attacks per Sharp Hide turn or accept the cost only if it triggers Mode Shift.
