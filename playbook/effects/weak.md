# Weak

Affected entity deals 25% less attack damage. Duration: N turns.

Formula: `floor((base + strength) * 0.75)` — Strength is added BEFORE the Weak multiplier.

- When on enemies (from Shockwave, Clothesline, Intimidate): THEIR attacks deal 25% less. YOUR attacks are UNAFFECTED.
- When on YOU (from enemy debuffs): YOUR attacks deal 25% less.

Direction matters: Weak on enemy = they deal less, you deal normal. Weak on you = you deal less.

**CRITICAL: Applying Weak to enemies does NOT reduce YOUR damage.** The 0.75 multiplier applies ONLY to the Weakened entity's own attacks. This is a confirmed recurring prediction error.
