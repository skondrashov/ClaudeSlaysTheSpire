# Game Mechanics

Core game systems that apply to all characters. For character-specific mechanics (Watcher stances, Defect orbs, etc.), see `playbook/characters/`.

---

## Damage Formula

Base formula: `floor((card_base_damage + strength) * multipliers)`

Order of operations:
1. Add Strength to base damage.
2. Apply multipliers (Weak, Vulnerable).
3. Floor the result (round down).

### Multipliers

- **Vulnerable** (on target): x1.5 damage taken from attacks.
- **Weak** (on attacker): x0.75 damage dealt by attacks.
- These stack multiplicatively: `floor(base * 0.75 * 1.5)`

### Examples

| Scenario | Formula | Result |
|---|---|---|
| Strike (6) | 6 | 6 |
| Strike + Vulnerable | floor(6 * 1.5) | 9 |
| Strike + 2 Str | 6 + 2 | 8 |
| Strike + 2 Str + Vulnerable | floor((6+2) * 1.5) | 12 |
| Strike + 2 Str + Weakened | floor((6+2) * 0.75) | 6 |
| Strike + Weakened + Vuln target | floor(6 * 0.75 * 1.5) | 6 |

---

## Status Effects

See `playbook/effects/` for individual effect files (Vulnerable, Weak, Frail, Strength, Dexterity).

---

## Block Mechanics

- Block absorbs damage before HP.
- Block expires at the start of your turn (resets to 0).
- Exception: Barricade (enemy passive) — block does NOT expire. Accumulates turn over turn.
- Metallicize and Plated Armor add block at end of turn (before enemy attacks resolve).
- Plated Armor decreases by 1 each time you take unblocked HP damage. Multiple hits in one attack each count separately.
- Flame Barrier / Thorns: Counter damage triggers AFTER each individual hit. Against multi-hit attacks, counter fires once per hit. Counter damage ignores the attacker's block.
- Pen Nib: Tracks total Attack cards played across ALL combats. Every 10th Attack card deals double damage. Counter persists between fights.

---

## Status Cards

| Card | Cost | Effect | Source | Persistence |
|---|---|---|---|---|
| Slimed | 1E | Exhaust (does nothing else) | Slime enemies | Cycles until played for 1E |
| Burn | Unplayable | 2 damage at end of turn if in hand | Hexaghost | Permanent deck clog |
| Dazed | Unplayable | Ethereal (exhausts at end of turn if in hand) | Chosen (Hex), Sentries | Self-exhausts but keeps being added |
| Wound | Unplayable | Nothing — pure hand clog | Book of Stabbing | Most persistent status |

**Removal methods:**
- True Grit+ can exhaust any of these from hand.
- Burning Pact exhausts a chosen card from hand.
- Fiend Fire exhausts ALL cards in hand.
- Slimed can be played for 1E to exhaust it (always correct).
- Dazed self-exhausts via Ethereal at end of turn.

---

## Keywords

### Exhaust
Removes a card from THIS COMBAT ONLY. The card goes to the exhaust pile and will not be drawn again for the rest of this fight. Your full deck resets between fights.

WHAT THIS MEANS: Exhaust has zero long-term cost. Never "save" an exhausting card for a later fight. Exhaust is NOT card removal — permanent removal only happens at shops or certain events.

### Ethereal
- Ethereal cards exhaust at end of turn if still in hand (not played).
- ALWAYS play Ethereal cards if possible — permanent loss is worse than wasted block/damage.

### Innate
- Innate cards are always in your opening hand (turn 1 draw).
- Bottled Flame/Lightning/Tornado relics make a chosen card Innate.

### Retain
- Retained cards stay in hand at end of turn instead of being discarded.
- Watcher makes heavy use of Retain — see `playbook/characters/watcher.md`.

---

## Card Index Shifting (CRITICAL — RECURRING FATAL ERROR)

When you play a card by numeric index, all cards after it shift down by 1. Multi-card commands using numeric indices will play WRONG CARDS.

**THE FIX: USE CARD NAMES, NOT NUMBERS.** Card names are resolved against the current hand at execution time. This eliminates the entire class of index shift errors.

**THIS ALSO APPLIES TO SHOP PURCHASES.** Use card names when buying from shops.

The only exception: two copies of the same card in hand where you need a specific one.

---

## Energy System

- Base energy: 3 per turn (no modifiers).
- Energy resets each turn — unspent energy is WASTED.
- X-cost cards (Whirlwind, Malaise, Skewer) use ALL remaining energy. **Always play X-cost cards LAST.** See individual card files for details.

---

## Card Draw

- Standard draw: 5 cards per turn.
- Cards that draw add to hand mid-turn. Play draw cards first, then reassess.
- When draw pile is empty and a draw triggers, discard pile shuffles into draw pile.

---

## Enemy Intent Display

Enemy intent numbers show the FINAL damage including all modifiers (Vulnerable on player, Weak on enemy, enemy Strength). **Use the displayed number directly for block calculations.** Do not recalculate modifiers on top of it.

---

## Enemy Mechanics

### Artifact
- Artifact N: next N debuffs are negated.
- Strip with cheap debuffs (Thunderclap at 1E), then apply real debuffs.

### Barricade (enemy)
- Block does NOT expire. Accumulates. Need burst damage to break through.

### Mode Shift (Guardian)
- Damage counter in Attack Mode. When enough damage dealt, switches to Defensive Mode.
- Counter: 30 (first cycle), 40 (second), 50 (third).
- Triggering Mode Shift mid-attack CANCELS the current attack.

### Sharp Hide (Guardian Defensive Mode)
- Deals N damage per Attack card played. Block before playing Attacks.

### Flight (Byrds)
- All damage halved while Flight > 0. Each hit decrements Flight by 1. Multi-hit strips faster.

### Hex (Chosen)
- When you play a Skill, a Dazed is added to draw pile. Minimize Skill usage.

### Curl Up (Louse)
- First attack triggers 5-7 block. Follow up with more attacks same turn.

### Ritual (Cultist)
- +3 Strength per activation, permanent and stacking. Kill fast.

### Malleable (Snake Plant)
- Gains increasing block each time attacked within a single turn. Resets each turn. Use one large hit per turn.

---

## Power Card Priority in Boss Fights

Play Power cards early in boss fights. Powers are permanent — every turn unplayed is missed value. Especially critical for scaling Powers (Noxious Fumes, Demon Form, Metallicize, Infinite Blades).

**Exception: Awakened One Phase 2** — do NOT play Powers (each gives +2 Str to boss).
