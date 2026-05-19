# Buffs and Debuffs

## Buffs

A buff is a positive status effect on an entity (player or enemy). Displayed as green icons.

- Buffs persist until their stacks reach 0, at which point they disappear
- Most buffs have fixed stacks that don't change on their own (e.g., [[buffs/Strength]] 3 stays at 3)
- Some buffs have stacks that decrement each turn (e.g., [[buffs/Intangible]] loses 1 stack per turn)
- Some buffs have stacks consumed by events (e.g., [[buffs/Buffer]] loses 1 stack when HP loss is prevented)
- Some buffs have stacks that increase via other effects (e.g., [[buffs/Ritual]] adds [[buffs/Strength]] each turn)
- All buffs are removed between combats unless otherwise noted

## Debuffs

A debuff is a negative status effect on an entity. Displayed as red icons.

- Most debuffs have stacks that decrement at the start of the affected entity's turn
- When stacks reach 0, the debuff disappears
- [[buffs/Artifact]] prevents debuff application (consumes 1 Artifact stack per prevented debuff)
- All debuffs are removed between combats

## Stacking

When a buff/debuff is applied and the entity already has it:
- Stack values are added (e.g., applying 2 [[debuffs/Weak]] to an entity with 1 [[debuffs/Weak]] = 3 stacks)
