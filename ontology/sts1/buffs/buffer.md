# Buffer

- **Effect:** Prevents the next N instances of HP loss. Each time HP loss would occur, it is negated and Buffer decreases by 1.
- **Interactions:** Prevents ALL HP loss including [[debuffs/Poison]] damage, not just attack damage. Does NOT prevent [[rules/Block]] loss. [[rules/Block]] is consumed before Buffer checks — if an attack deals 6 damage and you have 5 Block, Block absorbs 5 and Buffer prevents the remaining 1 HP loss. Against multi-hit attacks, each hit is a separate instance: Block is consumed by early hits, Buffer prevents HP loss from one hit only, remaining hits land in full.
