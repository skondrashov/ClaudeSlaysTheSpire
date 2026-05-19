# Weak

- **Effect:** Affected entity deals 25% less attack damage (x0.75 multiplier)
- **Duration:** N turns, decrements at start of affected entity's turn
- **Formula:** `floor((base + strength) * 0.75)` — [[buffs/Strength]] is added BEFORE the Weak multiplier
- **Direction:** Weak on enemy = their attacks deal 25% less, player's attacks are UNAFFECTED. Weak on player = player's attacks deal 25% less.
- **Removed by:** [[buffs/Artifact]] (negates the application)

Applying Weak to an enemy does NOT reduce the player's own damage. The 0.75 multiplier applies only to the Weakened entity's own attacks.
