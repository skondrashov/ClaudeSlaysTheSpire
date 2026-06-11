"""
Formats CommunicationMod JSON game state into readable text for Claude.

Each screen type gets its own formatter. The goal is to show Claude exactly
what it needs to reason about, with card indices matching what CommunicationMod
expects (1-indexed for play commands).
"""

import re

# Display names that under-report the variant: the game distinguishes these
# monsters by id (and shows the player a red vs green sprite), but their display
# name is identical. Recover the precise name from the id so the knowledge layer
# never sees an ambiguous entity. Ids verified against the game code
# (LouseNormal/LouseDefensive/SlaverBlue/SlaverRed classes).
_MONSTER_ID_NAMES = {
    "FuzzyLouseNormal": "Red Louse",
    "FuzzyLouseDefensive": "Green Louse",
    "SlaverBlue": "Blue Slaver",
    "SlaverRed": "Red Slaver",
}


def monster_name(m: dict) -> str:
    """A monster's precise display name (id-disambiguated where needed)."""
    return _MONSTER_ID_NAMES.get(m.get("id"), m.get("name", "?"))


def format_state(state: dict) -> str:
    """Main entry point. Dispatches to screen-specific formatter."""
    if "error" in state:
        return f"ERROR: {state['error']}"

    if not state.get("in_game", False):
        return format_out_of_game(state)

    gs = state.get("game_state", {})
    screen = gs.get("screen_type", "NONE")
    phase = gs.get("room_phase", "")

    parts = [format_header(gs)]

    # GRID and HAND_SELECT can appear mid-combat (e.g., Omniscience, Meditate).
    # Always show them first when active, then show combat context below.
    if screen == "GRID":
        parts.append(format_grid(gs))
        if gs.get("combat_state"):
            parts.append(format_combat(gs))
    elif screen == "HAND_SELECT":
        parts.append(format_hand_select(gs))
        if gs.get("combat_state"):
            parts.append(format_combat(gs))
    elif screen == "CARD_REWARD":
        # Can appear mid-combat too (e.g., potion card choices) — render the
        # options first, then combat context below.
        parts.append(format_card_reward(gs))
        if gs.get("combat_state"):
            parts.append(format_combat(gs))
    elif phase == "COMBAT" or screen == "NONE":
        if gs.get("combat_state"):
            parts.append(format_combat(gs))
    elif screen == "EVENT":
        parts.append(format_event(gs))
    elif screen in ("SHOP_ROOM", "SHOP_SCREEN"):
        parts.append(format_shop(gs))
    elif screen == "MAP":
        parts.append(format_map(gs))
    elif screen == "REST":
        parts.append(format_rest(gs))
    elif screen == "COMBAT_REWARD":
        parts.append(format_combat_reward(gs))
    elif screen == "BOSS_REWARD":
        parts.append(format_boss_reward(gs))
    elif screen == "GAME_OVER":
        parts.append(format_game_over(gs))
    elif screen == "COMPLETE":
        parts.append(format_complete(gs))
    elif screen == "CHEST":
        if (gs.get("screen_state") or {}).get("chest_open"):
            parts.append("CHEST (already opened) — contents collected. Use 'proceed' to continue.")
        else:
            parts.append("CHEST — Use 'choose open' to open the chest and collect the relic.")
            parts.append("WARNING: Do NOT use proceed here — it will skip the chest entirely.")
    else:
        parts.append(f"SCREEN: {screen} (no specific formatter)")

    commands = state.get("available_commands", [])
    parts.append(f"\nAvailable commands: {', '.join(commands)}")

    return "\n".join(parts)


def format_out_of_game(state: dict) -> str:
    commands = state.get("available_commands", [])
    lines = ["OUT OF GAME — No run in progress."]
    lines.append(f"Available commands: {', '.join(commands)}")
    lines.append("")
    lines.append("To start a run: start IRONCLAD [ascension_level] [seed]")
    lines.append("Characters: IRONCLAD, THE_SILENT, DEFECT, WATCHER")
    return "\n".join(lines)


def format_header(gs: dict) -> str:
    """Common header for all in-game screens."""
    floor = gs.get("floor", 0)
    act = gs.get("act", 1)
    hp = gs.get("current_hp", 0)
    max_hp = gs.get("max_hp", 0)
    gold = gs.get("gold", 0)
    asc = gs.get("ascension_level", 0)
    cls = gs.get("class", "?")
    boss = gs.get("act_boss", "?")
    screen = gs.get("screen_type", "?")
    phase = gs.get("room_phase", "?")

    hp_pct = int(hp / max_hp * 100) if max_hp > 0 else 0
    hp_bar = f"{hp}/{max_hp} ({hp_pct}%)"

    lines = [
        f"--- {cls} A{asc} | Act {act} Floor {floor} | Boss: {boss} ---",
        f"HP: {hp_bar} | Gold: {gold}",
    ]

    # Potions
    potions = gs.get("potions", [])
    pot_strs = []
    for p in potions:
        if p.get("id") == "Potion Slot":
            pot_strs.append("[empty]")
        else:
            pot_strs.append(p.get("name", "?"))
    if pot_strs:
        lines.append(f"Potions: {', '.join(pot_strs)}")

    # Relics (with counters where relevant)
    relics = gs.get("relics", [])
    if relics:
        relic_strs = []
        for r in relics:
            name = r.get("name", "?")
            counter = r.get("counter", -1)
            # counter of -1 or -2 means "not applicable" — don't show
            if counter >= 0:
                relic_strs.append(f"{name} [{counter}]")
            else:
                relic_strs.append(name)
        lines.append(f"Relics ({len(relics)}): {', '.join(relic_strs)}")

    # Keys
    keys = []
    if gs.get("has_emerald_key"):
        keys.append("Emerald")
    if gs.get("has_ruby_key"):
        keys.append("Ruby")
    if gs.get("has_sapphire_key"):
        keys.append("Sapphire")
    if keys:
        lines.append(f"Keys: {', '.join(keys)}")

    lines.append(f"Screen: {screen} | Phase: {phase}")
    return "\n".join(lines)


def format_combat(gs: dict) -> str:
    cs = gs["combat_state"]
    player = cs.get("player", {})
    monsters = cs.get("monsters", [])
    hand = cs.get("hand", [])
    turn = cs.get("turn", 0)

    lines = [f"\n=== COMBAT (Turn {turn}) ==="]

    # Player status
    energy = player.get("energy", 0)
    block = player.get("block", 0)
    lines.append(f"Energy: {energy} | Block: {block}")

    powers = player.get("powers", [])
    if powers:
        power_strs = [format_power(p) for p in powers]
        lines.append(f"Powers: {', '.join(power_strs)}")

    # Orbs (Defect)
    orbs = player.get("orbs", [])
    if orbs:
        orb_strs = [f"{o.get('name', '?')}({o.get('passive_amount', 0)}/{o.get('evoke_amount', 0)})" for o in orbs]
        lines.append(f"Orbs: {', '.join(orb_strs)}")

    # Enemies (indices are absolute positions — matching CommunicationMod's targeting)
    lines.append("")
    lines.append("ENEMIES:")
    for i, m in enumerate(monsters):
        if m.get("is_gone"):
            continue
        hp = m.get("current_hp", 0)
        max_hp = m.get("max_hp", 0)
        block = m.get("block", 0)
        intent = m.get("intent", "?")
        name = monster_name(m)

        parts = [f"  [{i}] {name} — HP: {hp}/{max_hp}"]
        if block > 0:
            parts.append(f"Block: {block}")

        # Intent with damage info
        dmg = m.get("move_adjusted_damage", -1)
        hits = m.get("move_hits", 1)
        if dmg > 0:
            if hits > 1:
                intent_str = f"{intent} ({dmg}x{hits} = {dmg * hits})"
            else:
                intent_str = f"{intent} ({dmg})"
        else:
            intent_str = intent
        parts.append(f"Intent: {intent_str}")

        monster_powers = m.get("powers", [])
        if monster_powers:
            power_strs = [format_power(p) for p in monster_powers]
            parts.append(f"Powers: {', '.join(power_strs)}")

        lines.append(" | ".join(parts))

    # Hand
    lines.append("")
    lines.append(f"HAND ({len(hand)} cards):")
    for i, card in enumerate(hand):
        idx = i + 1  # 1-indexed for CommunicationMod
        name = card.get("name", "?")
        cost = card.get("cost", "?")
        ctype = card.get("type", "?").lower()
        playable = card.get("is_playable", False)
        has_target = card.get("has_target", False)
        exhausts = card.get("exhausts", False)
        ethereal = card.get("ethereal", False)

        flags = []
        if not playable:
            flags.append("UNPLAYABLE")
        if has_target:
            flags.append("targeted")
        if exhausts:
            flags.append("exhaust")
        if ethereal:
            flags.append("ethereal")
        if card.get("upgrades", 0) > 0 and not name.endswith("+"):
            name += "+"

        # Cost sentinels: -1 is X-cost, -2 is unplayable (curses/statuses)
        cost_str = "X" if cost == -1 else "-" if cost == -2 else f"{cost}E"
        flag_str = f" [{', '.join(flags)}]" if flags else ""
        lines.append(f"  [{idx}] {name} ({ctype}, {cost_str}){flag_str}")

    # Pile contents — grouped summaries so the player knows what's coming
    draw_pile = cs.get("draw_pile", [])
    discard_pile = cs.get("discard_pile", [])
    exhaust_pile = cs.get("exhaust_pile", [])

    lines.append(f"\nDRAW PILE ({len(draw_pile)}): {_summarize_pile(draw_pile)}")
    lines.append(f"DISCARD ({len(discard_pile)}): {_summarize_pile(discard_pile)}")
    if exhaust_pile:
        lines.append(f"EXHAUST ({len(exhaust_pile)}): {_summarize_pile(exhaust_pile)}")

    return "\n".join(lines)


def _event_choice_options(ss: dict) -> list:
    """The event options that `choose N` actually indexes, in order.

    CommunicationMod's choice_list for an EVENT contains only the ENABLED
    options. Numbering the full display list (disabled included) shifts every
    index after a disabled option — run 241 chose the on-screen relic offer
    and executed Leave (IB-013); run 237's Red Mask desync (IB-010) is the
    same mechanism. Single source of truth for the formatter, the command
    translation, and any guard.
    """
    return [opt for opt in ss.get("options", []) if not opt.get("disabled", False)]


def format_event(gs: dict) -> str:
    ss = gs.get("screen_state", {})
    event_name = ss.get("event_name", "Unknown Event")
    body = ss.get("body_text", "")
    options = ss.get("options", [])

    lines = [f"\n=== EVENT: {event_name} ==="]
    if body:
        # Strip HTML tags from body text
        clean = re.sub(r"<[^>]+>", "", body)
        lines.append(clean)

    lines.append("")
    # Indices must match CommunicationMod's choice_list (enabled options only) —
    # disabled options get NO index so a shifted number can never be chosen.
    idx = 0
    for opt in options:
        text = re.sub(r"<[^>]+>", "", opt.get("text", "?"))
        if opt.get("disabled", False):
            lines.append(f"  [-] {text} (DISABLED — not choosable, has no index)")
        else:
            lines.append(f"  [{idx}] {text}")
            idx += 1

    lines.append("\nUse: choose <index>")
    return "\n".join(lines)


def _build_shop_choice_list(gs: dict) -> list:
    """Build the ordered choice list matching CommunicationMod's getAvailableShopItems().

    CommunicationMod orders shop items as:
        1. Purge (if available AND affordable)
        2. Affordable cards (colored then colorless — same order as screen_state)
        3. Affordable relics
        4. Affordable potions

    Only items the player can afford appear in the choice list.
    This matches CommunicationMod's internal indexing for "choose N".

    Returns list of (category, name, item_dict) tuples.
    """
    ss = gs.get("screen_state", {})
    gold = gs.get("gold", 0)
    cards = ss.get("cards", [])
    relics = ss.get("relics", [])
    potions = ss.get("potions", [])
    purge_available = ss.get("purge_available", False)
    purge_cost = ss.get("purge_cost", 0)

    items = []

    if purge_available and gold >= purge_cost:
        items.append(("purge", "purge", None))

    for card in cards:
        if gold >= card.get("price", float("inf")):
            items.append(("card", card.get("name", ""), card))

    for relic in relics:
        if gold >= relic.get("price", float("inf")):
            items.append(("relic", relic.get("name", ""), relic))

    for pot in potions:
        if gold >= pot.get("price", float("inf")):
            items.append(("potion", pot.get("name", ""), pot))

    return items


def format_shop(gs: dict) -> str:
    ss = gs.get("screen_state", {})
    cards = ss.get("cards", [])
    relics = ss.get("relics", [])
    potions = ss.get("potions", [])
    purge_available = ss.get("purge_available", False)
    purge_cost = ss.get("purge_cost", 0)

    # SHOP_ROOM is the "entering shop" state — the merchant's wares aren't open
    # yet. choose 0 opens the shop screen; proceed leaves the room.
    screen = gs.get("screen_type", "")
    if screen == "SHOP_ROOM" and not cards and not relics and not potions:
        lines = ["\n=== SHOP (entering) ==="]
        lines.append("Use: choose 0 to browse the merchant's wares; proceed to leave the room.")
        lines.append(f"\nGold: {gs.get('gold', 0)}")
        return "\n".join(lines)

    # Real choice indices (purge first, then affordable cards/relics/potions).
    # Unaffordable items have NO index — they aren't in the choice list at all.
    items = _build_shop_choice_list(gs)
    idx_by_id = {id(item): i for i, (cat, _name, item) in enumerate(items) if item is not None}
    purge_idx = next((i for i, (cat, _n, _it) in enumerate(items) if cat == "purge"), None)

    def _item_line(item: dict, name: str) -> str:
        price = item.get("price", "?")
        idx = idx_by_id.get(id(item))
        if idx is not None:
            return f"  [{idx}] {name} — {price}g"
        return f"  {name} — {price}g (can't afford)"

    lines = ["\n=== SHOP ==="]

    if cards:
        lines.append("Cards:")
        for card in cards:
            name = card.get("name", "?")
            if card.get("upgrades", 0) > 0 and not name.endswith("+"):
                name += "+"
            lines.append(_item_line(card, name))

    if relics:
        lines.append("Relics:")
        for relic in relics:
            lines.append(_item_line(relic, relic.get("name", "?")))

    if potions:
        belt = gs.get("potions", [])
        belt_full = bool(belt) and not any(p.get("id") == "Potion Slot" for p in belt)
        if belt_full:
            lines.append("Potions: [CANNOT BUY — your potion slots are FULL; drink or discard first]")
        else:
            lines.append("Potions:")
        for pot in potions:
            lines.append(_item_line(pot, pot.get("name", "?")))

    if purge_available:
        if purge_idx is not None:
            lines.append(f"Card removal: [{purge_idx}] Remove Card — {purge_cost}g")
        else:
            lines.append(f"Card removal: {purge_cost}g (can't afford)")

    lines.append(f"\nGold: {gs.get('gold', 0)}")
    lines.append("Buy by NAME (preferred): choose <Name> (e.g., choose Inflame, choose purge), "
                 "or choose <index> using the indices above. Use return to leave.")
    return "\n".join(lines)


def format_map(gs: dict) -> str:
    map_data = gs.get("map", [])
    next_nodes = gs.get("screen_state", {}).get("next_nodes", [])
    current_floor = gs.get("floor", 0)
    boss = gs.get("screen_state", {}).get("boss", {})

    SYMBOLS = {
        "M": "Monster", "?": "Unknown", "$": "Shop",
        "E": "Elite", "R": "Rest", "T": "Treasure",
        "B": "Boss",
    }

    lines = ["\n=== MAP ==="]

    # Show available next choices
    if next_nodes:
        lines.append("Available paths (choose one):")
        for i, node in enumerate(next_nodes):
            symbol = node.get("symbol", "?")
            x = node.get("x", "?")
            node_type = SYMBOLS.get(symbol, symbol)
            lines.append(f"  [{i}] {node_type} (x={x})")
    else:
        # Pre-boss floor: next_nodes is empty but the boss is the (only) choice.
        ss = gs.get("screen_state", {})
        boss_name = (boss.get("name") if isinstance(boss, dict) else boss) \
            or gs.get("act_boss", "?")
        if ss.get("boss_available") or boss or gs.get("act_boss"):
            lines.append("Available paths (choose one):")
            lines.append(f"  [0] Boss ({boss_name})")

    # Show full map for act pathing — group by floor, show connections
    if map_data:
        lines.append("")
        lines.append("FULL MAP (for route planning):")
        # Build lookup: (x,y) → node
        node_lookup = {}
        floors = {}
        for node in map_data:
            x, y = node.get("x", 0), node.get("y", 0)
            node_lookup[(x, y)] = node
            if y not in floors:
                floors[y] = []
            floors[y].append(node)

        for y in sorted(floors.keys()):
            floor_num = y + 1  # map y is 0-indexed, floors are 1-indexed
            marker = " <<<" if floor_num == current_floor + 1 else ""
            node_strs = []
            for n in sorted(floors[y], key=lambda n: n.get("x", 0)):
                sym = SYMBOLS.get(n.get("symbol", "?"), n.get("symbol", "?"))
                x = n.get("x", "?")
                children = n.get("children", [])
                if children:
                    child_xs = ",".join(str(c.get("x", "?")) for c in children)
                    node_strs.append(f"{sym}(x={x})→[{child_xs}]")
                else:
                    node_strs.append(f"{sym}(x={x})")
            lines.append(f"  F{floor_num}: {'  '.join(node_strs)}{marker}")

    if boss:
        lines.append(f"  BOSS: {boss.get('name', '?')}")

    lines.append("\nUse: choose <type> (rest/monster/elite/shop/unknown/treasure/boss), "
                 "choose x=<N>, or choose <index>. The response echoes [chose: ...] — "
                 "verify it matches your plan before acting further.")
    return "\n".join(lines)


def format_rest(gs: dict) -> str:
    ss = gs.get("screen_state", {})
    options = ss.get("rest_options", [])
    hp = gs.get("current_hp", 0)
    max_hp = gs.get("max_hp", 0)
    heal_amount = int(max_hp * 0.3)

    lines = ["\n=== REST SITE ==="]
    lines.append(f"HP: {hp}/{max_hp} (rest heals ~{heal_amount})")

    if options:
        lines.append("Options:")
        for i, opt in enumerate(options):
            label = opt if isinstance(opt, str) else opt.get("label", str(opt))
            lines.append(f"  [{i}] {label}")
        lines.append("\nUse: choose <option_name> (e.g., choose rest, choose smith)")
    else:
        lines.append("(already used — proceed to continue)")
    return "\n".join(lines)


def format_card_reward(gs: dict) -> str:
    ss = gs.get("screen_state", {})
    cards = ss.get("cards", [])

    lines = ["\n=== CARD REWARD ==="]
    lines.append("Choose a card (or skip):")
    for i, card in enumerate(cards):
        name = card.get("name", "?")
        ctype = card.get("type", "?").lower()
        cost = card.get("cost", "?")
        rarity = card.get("rarity", "?").lower()
        if card.get("upgrades", 0) > 0 and not name.endswith("+"):
            name += "+"
        lines.append(f"  [{i}] {name} ({ctype}, {cost}E, {rarity})")

    lines.append("\nUse: choose <index> to take, return to skip")
    return "\n".join(lines)


def format_combat_reward(gs: dict) -> str:
    ss = gs.get("screen_state", {})
    rewards = ss.get("rewards", [])

    # Check if potion slots are full
    potions = gs.get("potions", [])
    has_empty_slot = any(p.get("id") == "Potion Slot" for p in potions)

    lines = ["\n=== COMBAT REWARDS ==="]
    for i, reward in enumerate(rewards):
        rtype = reward.get("reward_type", "?")
        if rtype == "GOLD":
            lines.append(f"  [{i}] Gold: {reward.get('gold', 0)}")
        elif rtype == "CARD":
            lines.append(f"  [{i}] Card reward")
        elif rtype == "POTION":
            potion_name = reward.get('potion', {}).get('name', '?')
            if has_empty_slot:
                lines.append(f"  [{i}] Potion: {potion_name}")
            else:
                lines.append(f"  [{i}] Potion: {potion_name} [CANNOT TAKE — potion slots full!]")
        elif rtype == "RELIC":
            lines.append(f"  [{i}] Relic: {reward.get('relic', {}).get('name', '?')}")
        elif rtype == "STOLEN_GOLD":
            lines.append(f"  [{i}] Stolen gold: {reward.get('gold', 0)}")
        elif rtype == "EMERALD_KEY":
            lines.append(f"  [{i}] Emerald Key")
        elif rtype == "SAPPHIRE_KEY":
            lines.append(f"  [{i}] Sapphire Key (linked relic: {reward.get('relic', {}).get('name', '?')})")
        else:
            lines.append(f"  [{i}] {rtype}")

    if not has_empty_slot and any(r.get("reward_type") == "POTION" for r in rewards):
        lines.append("\nWARNING: Potion slots full. Discard a potion first to pick up a new one.")

    lines.append("\nUse: choose <index> to collect, proceed when done")
    return "\n".join(lines)


def format_boss_reward(gs: dict) -> str:
    ss = gs.get("screen_state", {})
    relics = ss.get("relics", [])

    lines = ["\n=== BOSS REWARD ==="]
    lines.append("Choose a boss relic:")
    for i, relic in enumerate(relics):
        name = relic.get("name", "?")
        lines.append(f"  [{i}] {name}")

    lines.append("\nYou MUST choose a boss relic — use: choose <index>")
    lines.append("WARNING: Skipping a boss relic is almost never correct. Boss relics are extremely powerful.")
    return "\n".join(lines)


def format_grid(gs: dict) -> str:
    ss = gs.get("screen_state", {})
    cards = ss.get("cards", [])
    selected = ss.get("selected_cards", [])
    for_upgrade = ss.get("for_upgrade", False)
    for_transform = ss.get("for_transform", False)
    for_purge = ss.get("for_purge", False)
    num_cards = ss.get("num_cards", 1)
    any_number = ss.get("any_number", False)

    action = "upgrade" if for_upgrade else "transform" if for_transform else "purge" if for_purge else "select"
    lines = [f"\n=== CARD SELECT ({action.upper()}) ==="]
    select_str = "any number" if any_number else str(num_cards)
    lines.append(f"Select {select_str} card(s) to {action}:")

    def _grid_name(card: dict) -> str:
        name = card.get("name", "?")
        if card.get("upgrades", 0) > 0 and not name.endswith("+"):
            name += "+"
        return name

    if selected:
        lines.append(f"Selected ({len(selected)}/{select_str}): "
                     f"{', '.join(_grid_name(c) for c in selected)}")

    # Mark already-selected cards in the list (matched by name + upgrades,
    # consuming one match per selected copy).
    sel_remaining = {}
    for c in selected:
        key = (c.get("name", ""), c.get("upgrades", 0))
        sel_remaining[key] = sel_remaining.get(key, 0) + 1

    for i, card in enumerate(cards):
        name = _grid_name(card)
        cost = card.get("cost", "?")
        ctype = card.get("type", "?").lower()
        mark = ""
        key = (card.get("name", ""), card.get("upgrades", 0))
        if sel_remaining.get(key, 0) > 0:
            sel_remaining[key] -= 1
            mark = " [SELECTED]"
        lines.append(f"  [{i}] {name} ({ctype}, {cost}E){mark}")

    lines.append("\nUse the indices above: choose 0, choose 1, etc. These are GRID indices (NOT hand indices — they differ!).")
    return "\n".join(lines)


def format_hand_select(gs: dict) -> str:
    ss = gs.get("screen_state", {})
    hand = ss.get("hand", [])
    num_cards = ss.get("num_cards", 1)
    can_pick_zero = ss.get("can_pick_zero", False)

    lines = ["\n=== HAND SELECT ==="]
    lines.append(f"Select {num_cards} card(s) from hand:")
    for i, card in enumerate(hand):
        name = card.get("name", "?")
        if card.get("upgrades", 0) > 0 and not name.endswith("+"):
            name += "+"
        lines.append(f"  [{i}] {name}")

    lines.append("\nUse: choose <index>")
    if can_pick_zero:
        lines.append("Or: return to skip")
    return "\n".join(lines)


def format_game_over(gs: dict) -> str:
    ss = gs.get("screen_state", {})
    victory = ss.get("victory", False)
    score = ss.get("score", 0)
    floor = gs.get("floor", 0)

    if victory:
        lines = [f"\n=== VICTORY! === Floor {floor}, Score: {score}"]
    else:
        lines = [f"\n=== DEFEAT === Died on floor {floor}, Score: {score}"]

    lines.append("\nUse: proceed to continue, then start a new run")
    return "\n".join(lines)


def format_complete(gs: dict) -> str:
    return "\n=== RUN COMPLETE ===\nUse: proceed"


def _summarize_pile(cards: list) -> str:
    """Summarize a pile of cards as grouped counts: '2x Strike, 1x Bash, 1x Defend+'."""
    if not cards:
        return "(empty)"
    counts = {}
    for card in cards:
        name = card.get("name", "?")
        if card.get("upgrades", 0) > 0 and not name.endswith("+"):
            name += "+"
        counts[name] = counts.get(name, 0) + 1
    # Sort by count descending, then name
    sorted_cards = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    parts = []
    for name, count in sorted_cards:
        if count > 1:
            parts.append(f"{count}x {name}")
        else:
            parts.append(name)
    return ", ".join(parts)


# Powers where a negative amount is REAL information (reduced Strength from
# Disarm/Shackled, Dexterity decay from Wraith Form, negative Focus) — never
# suppress these. For everything else a negative amount is a no-amount sentinel
# (Split -1, Minion -1).
_SIGNED_POWERS = {"strength", "dexterity", "focus"}


def format_power(power: dict) -> str:
    """Format a single power/buff/debuff.

    Negative amounts are usually sentinels for "no amount" (Split -1, Minion -1)
    — show just the name — EXCEPT for signed stats, where negative is real.
    """
    name = power.get("name", "?")
    amount = power.get("amount", 0)
    if amount > 0 or (amount < 0 and name.lower() in _SIGNED_POWERS):
        return f"{name} {amount}"
    return name
