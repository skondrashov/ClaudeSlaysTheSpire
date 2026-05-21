# Fossilized Helix

Prevents the first instance of HP loss each combat. Extremely strong in [[acts/Act 1]] where most enemies attack once per turn.

## Multi-Hit Interaction (CRITICAL)

Fossilized Helix prevents **HP loss**, not **damage**. Block is consumed BEFORE the Helix check. Against multi-hit attacks:

- Hit 1: Block absorbs what it can. If remaining damage exceeds block, HP loss would occur — Helix prevents it. **Block is still consumed.**
- Hit 2+: No Helix remaining. No block remaining. Full HP loss.

**Example:** Multi-Stab 6x2 with 5 block:
- Hit 1: 6 vs 5 block = 1 HP loss prevented by Helix. Block is now 0.
- Hit 2: 6 vs 0 block = 6 HP lost.
- Total: 6 HP lost, NOT 1.

**Wrong mental model:** "Helix absorbs the entire first hit, block handles the rest." This overestimates survivability by 5+ HP against multi-hit attacks.

**Correct mental model:** Block is consumed first. Helix catches the overflow from the first hit only. Against multi-hit, all block is gone after hit 1, and hits 2+ land in full.

## Valuation

- Against single-hit attacks: prevents the full hit. Excellent.
- Against multi-hit attacks ([[enemies/Book of Stabbing]], Byrds, Slimes): prevents only the overflow from hit 1. Much weaker. Plan block as if Helix does not exist for hits 2+.
- Against enemies with both single and multi-hit patterns: value depends on which pattern they use turn 1. Do not rely on Helix for survival against multi-hit enemies.
