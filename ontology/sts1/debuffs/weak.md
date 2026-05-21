# Weak

- **Effect:** Affected entity deals 25% less [[types/Attack]] damage (x0.75 multiplier)
- **Formula:** `floor((base + strength) * 0.75)` -- [[buffs/Strength]] is added BEFORE the Weak multiplier
- **Direction:** On enemy = their Attacks deal 25% less. On player = player's Attacks deal 25% less. Applying Weak to an enemy does NOT reduce the player's own damage.
