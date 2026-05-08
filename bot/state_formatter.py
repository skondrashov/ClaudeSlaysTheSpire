"""
Formats CommunicationMod JSON game state into readable text for Claude.

Each screen type gets its own formatter. The goal is to show Claude exactly
what it needs to reason about, with card indices matching what CommunicationMod
expects (1-indexed for play commands).
"""


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

    if phase == "COMBAT" or screen == "NONE":
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
    elif screen == "CARD_REWARD":
        parts.append(format_card_reward(gs))
    elif screen == "COMBAT_REWARD":
        parts.append(format_combat_reward(gs))
    elif screen == "BOSS_REWARD":
        parts.append(format_boss_reward(gs))
    elif screen == "GRID":
        parts.append(format_grid(gs))
    elif screen == "HAND_SELECT":
        parts.append(format_hand_select(gs))
    elif screen == "GAME_OVER":
        parts.append(format_game_over(gs))
    elif screen == "COMPLETE":
        parts.append(format_complete(gs))
    elif screen == "CHEST":
        parts.append("CHEST — Use PROCEED to open.")
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
        name = m.get("name", "?")

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

        flag_str = f" [{', '.join(flags)}]" if flags else ""
        lines.append(f"  [{idx}] {name} ({ctype}, {cost}E){flag_str}")

    # Pile contents — grouped summaries so the player knows what's coming
    draw_pile = cs.get("draw_pile", [])
    discard_pile = cs.get("discard_pile", [])
    exhaust_pile = cs.get("exhaust_pile", [])

    lines.append(f"\nDRAW PILE ({len(draw_pile)}): {_summarize_pile(draw_pile)}")
    lines.append(f"DISCARD ({len(discard_pile)}): {_summarize_pile(discard_pile)}")
    if exhaust_pile:
        lines.append(f"EXHAUST ({len(exhaust_pile)}): {_summarize_pile(exhaust_pile)}")

    return "\n".join(lines)


def format_event(gs: dict) -> str:
    ss = gs.get("screen_state", {})
    event_name = ss.get("event_name", "Unknown Event")
    body = ss.get("body_text", "")
    options = ss.get("options", [])

    lines = [f"\n=== EVENT: {event_name} ==="]
    if body:
        # Strip HTML tags from body text
        import re
        clean = re.sub(r"<[^>]+>", "", body)
        lines.append(clean)

    lines.append("")
    for i, opt in enumerate(options):
        text = opt.get("text", "?")
        disabled = opt.get("disabled", False)
        label = opt.get("label", "")
        # Strip HTML
        import re
        text = re.sub(r"<[^>]+>", "", text)
        status = " (DISABLED)" if disabled else ""
        lines.append(f"  [{i}] {text}{status}")

    lines.append("\nUse: choose <index>")
    return "\n".join(lines)


def format_shop(gs: dict) -> str:
    ss = gs.get("screen_state", {})
    cards = ss.get("cards", [])
    relics = ss.get("relics", [])
    potions = ss.get("potions", [])
    purge_available = ss.get("purge_available", False)
    purge_cost = ss.get("purge_cost", 0)

    # SHOP_ROOM is the "entering shop" transitional state — items may not be
    # populated yet. Call state() again to get the full SHOP_SCREEN inventory.
    # Do NOT send proceed — that leaves the shop without buying anything.
    screen = gs.get("screen_type", "")
    if screen == "SHOP_ROOM" and not cards and not relics and not potions:
        lines = ["\n=== SHOP (entering) ==="]
        lines.append("Shop inventory loading. Call state() to refresh — items will appear shortly.")
        lines.append("Do NOT use proceed here — that leaves the shop.")
        lines.append(f"\nGold: {gs.get('gold', 0)}")
        return "\n".join(lines)

    lines = ["\n=== SHOP ==="]

    if cards:
        lines.append("Cards:")
        for i, card in enumerate(cards):
            name = card.get("name", "?")
            price = card.get("price", "?")
            affordable = " " if gs.get("gold", 0) >= (card.get("price", 0) or 0) else " (can't afford) "
            if card.get("upgrades", 0) > 0 and not name.endswith("+"):
                name += "+"
            lines.append(f"  {name} — {price}g{affordable}")

    if relics:
        lines.append("Relics:")
        for i, relic in enumerate(relics):
            name = relic.get("name", "?")
            price = relic.get("price", "?")
            affordable = " " if gs.get("gold", 0) >= (relic.get("price", 0) or 0) else " (can't afford) "
            lines.append(f"  {name} — {price}g{affordable}")

    if potions:
        lines.append("Potions:")
        for i, pot in enumerate(potions):
            name = pot.get("name", "?")
            price = pot.get("price", "?")
            affordable = " " if gs.get("gold", 0) >= (pot.get("price", 0) or 0) else " (can't afford) "
            lines.append(f"  {name} — {price}g{affordable}")

    if purge_available:
        lines.append(f"Card removal: {purge_cost}g")

    lines.append(f"\nGold: {gs.get('gold', 0)}")
    lines.append("Buy with: choose <Name> (e.g., choose Inflame, choose purge). Use return to leave.")
    return "\n".join(lines)


def format_map(gs: dict) -> str:
    map_data = gs.get("map", [])
    next_nodes = gs.get("screen_state", {}).get("next_nodes", [])
    current_floor = gs.get("floor", 0)

    lines = ["\n=== MAP ==="]

    if next_nodes:
        lines.append("Available paths:")
        for i, node in enumerate(next_nodes):
            symbol = node.get("symbol", "?")
            x = node.get("x", "?")
            y = node.get("y", "?")
            node_type = {
                "M": "Monster", "?": "Unknown", "$": "Shop",
                "E": "Elite", "R": "Rest", "T": "Treasure",
                "B": "Boss"
            }.get(symbol, symbol)
            lines.append(f"  [{i}] {node_type} (x={x}, y={y})")
    else:
        # Show next floor nodes from map data
        next_floor = current_floor + 1
        nodes_at_floor = [n for n in map_data if n.get("y") == next_floor - 1]
        if nodes_at_floor:
            lines.append(f"Nodes at floor {next_floor}:")
            for i, node in enumerate(nodes_at_floor):
                symbol = node.get("symbol", "?")
                x = node.get("x", "?")
                node_type = {
                    "M": "Monster", "?": "Unknown", "$": "Shop",
                    "E": "Elite", "R": "Rest", "T": "Treasure",
                    "B": "Boss"
                }.get(symbol, symbol)
                lines.append(f"  [{i}] {node_type} (x={x})")

    lines.append("\nUse: choose <index> or proceed")
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
    else:
        lines.append("Options: rest (heal), smith (upgrade card)")

    lines.append("\nUse: choose <option_name> (e.g., choose rest, choose smith)")
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

    lines = ["\n=== COMBAT REWARDS ==="]
    for i, reward in enumerate(rewards):
        rtype = reward.get("reward_type", "?")
        if rtype == "GOLD":
            lines.append(f"  [{i}] Gold: {reward.get('gold', 0)}")
        elif rtype == "CARD":
            lines.append(f"  [{i}] Card reward")
        elif rtype == "POTION":
            lines.append(f"  [{i}] Potion: {reward.get('potion', {}).get('name', '?')}")
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

    lines.append("\nUse: choose <index> to take, return to skip")
    return "\n".join(lines)


def format_grid(gs: dict) -> str:
    ss = gs.get("screen_state", {})
    cards = ss.get("cards", [])
    for_upgrade = ss.get("for_upgrade", False)
    for_transform = ss.get("for_transform", False)
    for_purge = ss.get("for_purge", False)
    num_cards = ss.get("num_cards", 1)
    any_number = ss.get("any_number", False)

    action = "upgrade" if for_upgrade else "transform" if for_transform else "purge" if for_purge else "select"
    lines = [f"\n=== CARD SELECT ({action.upper()}) ==="]
    select_str = "any number" if any_number else str(num_cards)
    lines.append(f"Select {select_str} card(s) to {action}:")

    for i, card in enumerate(cards):
        name = card.get("name", "?")
        if card.get("upgrades", 0) > 0 and not name.endswith("+"):
            name += "+"
        cost = card.get("cost", "?")
        ctype = card.get("type", "?").lower()
        lines.append(f"  [{i}] {name} ({ctype}, {cost}E)")

    lines.append("\nUse: choose <index>, then confirm/proceed")
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


def format_power(power: dict) -> str:
    """Format a single power/buff/debuff."""
    name = power.get("name", "?")
    amount = power.get("amount", 0)
    if amount != 0:
        return f"{name} {amount}"
    return name
