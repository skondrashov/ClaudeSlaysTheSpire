"""
Command helper for Claude Code to interact with Slay the Spire.

Connects to relay.py's TCP server (localhost:19284) to read game state
and send commands. Each function is a single request-response.

Usage from Claude Code:
    from cmd import state, send
    state()           # See current game state
    send("play 1 0")  # Play card 1 targeting enemy 0
    send("end")       # End turn
    send("choose 2")  # Choose option 2
    send("proceed")   # Confirm/proceed
    send("return")    # Skip/cancel/leave
"""

import json
import os
import socket
import sys
import time
import urllib.request

from bot.state_formatter import format_state

HOST = "127.0.0.1"
PORT = 19284
TIMEOUT = 120  # seconds — long timeout for slow animations
STREAM_URL = "http://127.0.0.1:3002/decision"
LOCK_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "player.lock")
PLAYBOOK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "playbook")

# Direct event log — backup for when stream.py is down.
EVENT_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "stream_events.jsonl")

# Session token: passed via PLAYER_SESSION env var by the orchestrator.
# All bash calls from one agent use the same token. The lock checks this.
_SESSION_ID = os.environ.get("PLAYER_SESSION", "")
if not _SESSION_ID:
    raise RuntimeError(
        "PLAYER_SESSION env var not set.\n"
        "Only the orchestrator can provide this token."
    )


def _acquire_lock():
    """Acquire the player lock at import time. Fails if another session holds it."""
    os.makedirs(os.path.dirname(LOCK_FILE), exist_ok=True)

    if os.path.exists(LOCK_FILE):
        try:
            with open(LOCK_FILE) as f:
                held_by = f.read().strip()
            if held_by == _SESSION_ID:
                return  # our lock from a previous call
            raise RuntimeError(
                f"PLAYER LOCK CONFLICT — lock held by {held_by[:12]}...\n"
                f"Another player agent is running. Only one at a time.\n"
                f"Orchestrator must delete data/player.lock before spawning a new agent."
            )
        except (OSError, ValueError):
            pass  # corrupted lock, take it

    with open(LOCK_FILE, "w") as f:
        f.write(_SESSION_ID)


# Acquire lock at import time.
# Orchestrator deletes this file before spawning a new agent.
_acquire_lock()


# ---------------------------------------------------------------------------
# Playbook loading utilities
# ---------------------------------------------------------------------------

def _name_to_filename(name: str) -> str:
    """Convert a game entity name to its playbook filename (without extension).

    "Shrug It Off+" -> "shrug-it-off"
    "Charon's Ashes" -> "charon-s-ashes"
    "3 Cultists" -> "3-cultists"
    """
    name = name.rstrip("+").strip()
    name = name.lower()
    name = name.replace("'", "-")
    name = name.replace(" ", "-")
    while "--" in name:
        name = name.replace("--", "-")
    return name


def _load_playbook(category: str, name: str) -> str | None:
    """Load a playbook file. Returns content or None if not found.

    category: "cards", "enemies", "bosses", "events", "relics", "potions"
    name: game entity name (e.g., "Shrug It Off", "Gremlin Nob")
    """
    filename = _name_to_filename(name) + ".md"
    path = os.path.join(PLAYBOOK_DIR, category, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def _load_playbook_top(category: str, name: str) -> str | None:
    """Load just the header + first summary line of a playbook file.

    Returns the first non-empty line (title) + second non-empty line (summary),
    or None if not found. Used for compact deck reports.
    """
    content = _load_playbook(category, name)
    if content is None:
        return None
    lines = [l for l in content.split("\n") if l.strip()]
    if len(lines) >= 2:
        return lines[0] + "\n" + lines[1]
    elif lines:
        return lines[0]
    return None


def _load_playbook_root(filename: str) -> str | None:
    """Load a root-level playbook file (strategy.md, mechanics.md)."""
    path = os.path.join(PLAYBOOK_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


_BASIC_CARDS = {"Strike", "Defend", "Strike+", "Defend+"}


def _tcp_request(request: dict) -> dict:
    """Send a JSON request to relay, get JSON response."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    try:
        sock.connect((HOST, PORT))
        sock.sendall(json.dumps(request).encode() + b"\n")

        data = b""
        while b"\n" not in data:
            chunk = sock.recv(65536)
            if not chunk:
                break
            data += chunk

        if not data.strip():
            return {"error": "empty response from relay"}
        return json.loads(data.strip())
    except ConnectionRefusedError:
        return {"error": "Cannot connect to relay. Is the game running with CommunicationMod?"}
    except socket.timeout:
        return {"error": "Timeout waiting for relay response"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        sock.close()


def state() -> str:
    """Get current game state, formatted for reading."""
    global _last_raw_state
    raw = _tcp_request({"type": "state"})
    _last_raw_state = raw
    # Auto-handle mechanical transitions before returning state
    raw = _auto_handle_mechanical(raw)
    return format_state(raw)


def state_raw() -> dict:
    """Get current game state as raw dict."""
    global _last_raw_state
    raw = _tcp_request({"type": "state"})
    _last_raw_state = raw
    return raw


# Cached state for translating commands to readable text
_last_raw_state = None


def _resolve_enemy_name(monsters: list, name_ref: str) -> str | None:
    """Resolve an enemy name to its absolute index in the monsters array.

    CommunicationMod uses absolute indices into the full monsters array
    (including dead/gone enemies). This resolves a name to that index.

    Returns the index as a string, or None if no match.
    """
    name_lower = name_ref.lower()
    # Exact match first
    for i, m in enumerate(monsters):
        if m.get("is_gone"):
            continue
        if m.get("name", "").lower() == name_lower:
            return str(i)
    # Substring match
    for i, m in enumerate(monsters):
        if m.get("is_gone"):
            continue
        if name_lower in m.get("name", "").lower():
            return str(i)
    return None


def _resolve_card_name(raw_state: dict, action: str) -> str:
    """Translate card names and enemy names in play commands to indices.

    Supports card names, enemy names, or both:
        "play Bash Jaw Worm"    -> "play 2 0"   (card name + enemy name)
        "play Bash 0"           -> "play 2 0"   (card name + numeric target)
        "play Shrug It Off"     -> "play 3"     (card name, no target)
        "play Bash+ 0"          -> "play 2 0"   (upgraded card + target)
        "play 3 0"              -> "play 3 0"   (numeric, unchanged)
        "play 3 Jaw Worm"       -> "play 3 0"   (numeric card + enemy name)

    Enemy names are resolved to absolute indices in the monsters array
    (matching CommunicationMod's indexing which includes dead enemies).
    """
    if not action or not action.strip().lower().startswith("play "):
        return action

    parts = action.strip().split()
    if len(parts) < 2:
        return action

    if not raw_state:
        return action
    combat = (raw_state.get("game_state") or {}).get("combat_state")
    if not combat:
        return action
    hand = combat.get("hand", [])
    monsters = combat.get("monsters", [])

    # Extract everything after "play"
    after_play = action.strip()[len("play "):].strip()
    tokens = after_play.split()

    # --- Case 1: Card is a numeric index ---
    if tokens[0].isdigit():
        card_idx = tokens[0]
        target_ref = " ".join(tokens[1:]) if len(tokens) > 1 else None
        if target_ref:
            # Already numeric?
            try:
                int(target_ref)
                return action  # "play 3 0" — all numeric, unchanged
            except ValueError:
                pass
            # Resolve enemy name
            resolved_target = _resolve_enemy_name(monsters, target_ref)
            if resolved_target is not None:
                return f"play {card_idx} {resolved_target}"
        return action  # "play 3" or unresolvable target

    # --- Case 2: Card is a name — find it in hand ---
    # Try matching hand card names against the token sequence (longest match wins).
    # This handles multi-word card names like "Shrug It Off".
    # When multiple cards match equally (e.g., two Strikes), pick the cheapest one.
    # This matters with Snecko Oil or other cost-randomizing effects.
    best_card_idx = None       # 1-indexed card position in hand
    best_token_count = 0       # how many tokens the card name consumed
    best_card_cost = float('inf')  # cost of the best match (prefer cheapest)

    for i, card in enumerate(hand):
        card_name = card.get("name", "")
        upgraded = card.get("upgrades", 0) > 0
        card_cost = card.get("cost", 99)

        # Build candidate names to try
        names_to_try = [card_name]
        if upgraded:
            names_to_try.append(card_name + "+")

        for try_name in names_to_try:
            try_tokens = try_name.lower().split()
            tc = len(try_tokens)
            if tc > len(tokens) or tc < best_token_count:
                continue
            # Same token count but more expensive — skip (keep cheapest)
            if tc == best_token_count and card_cost >= best_card_cost:
                continue
            candidate = " ".join(tokens[:tc]).lower()
            # Match against name (with or without +)
            if candidate == try_name.lower():
                best_card_idx = i + 1
                best_token_count = tc
                best_card_cost = card_cost
            elif candidate == try_name.rstrip("+").lower():
                # "play Bash" matches "Bash" even if upgraded
                if try_name.endswith("+"):
                    # Only match non-+ input to upgraded cards if no + specified
                    # (don't require_upgrade if they didn't type +)
                    pass  # handled by the base name in names_to_try[0]
                best_card_idx = i + 1
                best_token_count = tc
                best_card_cost = card_cost

    if best_card_idx is None:
        return action  # No card match, return unchanged

    # Whatever's left after the card name is the target
    remaining = " ".join(tokens[best_token_count:]).strip() if best_token_count < len(tokens) else ""

    if not remaining:
        return f"play {best_card_idx}"

    # Target is numeric?
    try:
        int(remaining)
        return f"play {best_card_idx} {remaining}"
    except ValueError:
        pass

    # Resolve enemy name to absolute index
    resolved_target = _resolve_enemy_name(monsters, remaining)
    if resolved_target is not None:
        return f"play {best_card_idx} {resolved_target}"

    # Couldn't resolve target — return with card resolved at least
    return f"play {best_card_idx} {remaining}"


def _build_shop_choice_list(gs: dict) -> list[tuple[str, str, dict | None]]:
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

    items: list[tuple[str, str, dict | None]] = []

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


def _resolve_shop_choose(raw_state: dict, action: str) -> str:
    """Resolve card/relic/potion names in shop choose commands to indices.

    Supports:
        "choose Inflame"        -> "choose 3"  (finds Inflame in shop cards)
        "choose purge"          -> "choose 0"  (purge is always index 0 when affordable)
        "choose 3"              -> "choose 3"  (already numeric, pass through)

    CommunicationMod indexes shop items as:
        purge (if affordable) → affordable cards → affordable relics → affordable potions

    This must match that ordering exactly, or the wrong item gets bought.
    """
    gs = raw_state.get("game_state", {}) if raw_state else {}
    screen = gs.get("screen_type", "")
    if screen not in ("SHOP_ROOM", "SHOP_SCREEN"):
        return action  # Not in shop, pass through

    parts = action.strip().split()
    if len(parts) < 2 or parts[0].lower() != "choose":
        return action

    remainder = " ".join(parts[1:])

    # "return" leaves the shop — pass through
    if remainder.lower() == "return":
        return action

    # Already numeric — pass through (caller knows the index)
    try:
        int(remainder)
        return action
    except ValueError:
        pass

    # Build the choice list matching CommunicationMod's indexing
    items = _build_shop_choice_list(gs)
    if not items:
        return action

    search_name = remainder.lower().rstrip("+")
    search_clean = search_name.replace(" ", "").replace("'", "")

    # "choose purge" → find purge in the list
    if search_name == "purge":
        for idx, (cat, name, _) in enumerate(items):
            if cat == "purge":
                return f"choose {idx}"
        return action  # Purge not available/affordable

    # Search all items by name
    for idx, (cat, name, item) in enumerate(items):
        if cat == "purge":
            continue
        item_name = name.lower()
        item_clean = item_name.replace(" ", "").replace("'", "")
        if item_name == search_name or item_clean == search_clean:
            return f"choose {idx}"

    return action  # No match found, pass through unchanged


def _resolve_choose_card_name(raw_state: dict, action: str) -> str:
    """Resolve card names in choose commands to indices for card-selection screens.

    Supports HAND_SELECT, CARD_REWARD, and GRID screens:
        "choose Sneaky Strike"  -> "choose 2"  (finds Sneaky Strike in the card list)
        "choose 3"              -> "choose 3"  (already numeric, pass through)
    """
    gs = raw_state.get("game_state", {}) if raw_state else {}
    screen = gs.get("screen_type", "")
    ss = gs.get("screen_state", {})

    # Determine which card list to search based on screen type
    if screen == "HAND_SELECT":
        cards = ss.get("hand", [])
    elif screen in ("CARD_REWARD", "GRID"):
        cards = ss.get("cards", [])
    else:
        return action  # Not a card-selection screen

    parts = action.strip().split()
    if len(parts) < 2 or parts[0].lower() != "choose":
        return action

    remainder = " ".join(parts[1:])

    # Already numeric — pass through
    try:
        int(remainder)
        return action
    except ValueError:
        pass

    # Search for card name match (case-insensitive, handles upgraded names)
    search = remainder.lower().strip()
    search_no_plus = search.rstrip("+")

    best_idx = None
    best_token_count = 0

    for i, card in enumerate(cards):
        card_name = card.get("name", "")
        card_name_lower = card_name.lower()
        upgraded = card.get("upgrades", 0) > 0

        # Try matching with and without +
        candidates = [card_name_lower]
        if upgraded:
            candidates.append(card_name_lower + "+")

        for candidate in candidates:
            tc = len(candidate.split())
            if tc <= best_token_count:
                continue
            if search == candidate or search_no_plus == candidate or search == candidate.rstrip("+"):
                best_idx = i
                best_token_count = tc

    if best_idx is not None:
        return f"choose {best_idx}"

    return action  # No match found


def _translate_named_choose(name: str) -> str:
    """Translate named choose commands like 'choose rest'."""
    name_map = {
        "rest": "Rest",
        "smith": "Smith (Upgrade)",
        "dig": "Dig",
        "recall": "Recall",
        "lift": "Lift",
        "toke": "Toke",
        "purge": "Remove Card",
    }
    return name_map.get(name.lower(), name.capitalize())


def _translate_command(command: str) -> str:
    """Translate raw command into readable text using cached game state."""
    if not command:
        return command
    parts = command.strip().split()
    verb = parts[0]

    gs = (_last_raw_state or {}).get("game_state", {})
    combat = gs.get("combat_state")

    if verb == "play" and combat:
        hand = combat.get("hand", [])
        card_idx = int(parts[1]) - 1 if len(parts) > 1 else -1
        card = hand[card_idx] if 0 <= card_idx < len(hand) else None
        card_name = card["name"] if card else f"card {parts[1]}"
        if len(parts) > 2 and combat:
            monsters = combat.get("monsters", [])  # absolute index
            target_idx = int(parts[2])
            enemy = monsters[target_idx] if 0 <= target_idx < len(monsters) else None
            enemy_name = enemy["name"] if enemy else f"enemy {parts[2]}"
            return f"{card_name} → {enemy_name}"
        return card_name

    if verb == "choose" and len(parts) > 1:
        screen = gs.get("screen_type", "")
        ss = gs.get("screen_state", {})
        try:
            idx = int(parts[1])
        except ValueError:
            # Named choice like "choose rest" or "choose smith"
            return _translate_named_choose(parts[1])

        if screen == "MAP":
            nodes = ss.get("next_nodes", [])
            if 0 <= idx < len(nodes):
                symbol = nodes[idx].get("symbol", "?")
                node_name = {"M": "Monster", "?": "Unknown", "$": "Shop",
                             "E": "Elite", "R": "Rest Site", "T": "Treasure",
                             "B": "Boss"}.get(symbol, symbol)
                return f"→ {node_name}"
        elif screen == "REST":
            options = ss.get("rest_options", [])
            if 0 <= idx < len(options):
                opt = options[idx] if isinstance(options[idx], str) else str(options[idx])
                return opt.capitalize()
        elif screen == "CARD_REWARD":
            cards = ss.get("cards", [])
            if 0 <= idx < len(cards):
                return f"Take {cards[idx].get('name', '?')}"
        elif screen == "COMBAT_REWARD":
            rewards = ss.get("rewards", [])
            if 0 <= idx < len(rewards):
                r = rewards[idx]
                rtype = r.get("reward_type", "?")
                if rtype == "GOLD":
                    return f"Take {r.get('gold', 0)}g"
                elif rtype == "CARD":
                    return "Take Card Reward"
                elif rtype == "POTION":
                    return f"Take {r.get('potion', {}).get('name', 'Potion')}"
                elif rtype == "RELIC":
                    return f"Take {r.get('relic', {}).get('name', 'Relic')}"
                elif rtype == "EMERALD_KEY":
                    return "Take Emerald Key"
                elif rtype == "SAPPHIRE_KEY":
                    return f"Take Sapphire Key"
                else:
                    return f"Take {rtype}"
        elif screen == "BOSS_REWARD":
            relics = ss.get("relics", [])
            if 0 <= idx < len(relics):
                return f"Take {relics[idx].get('name', 'Relic')}"
        elif screen in ("SHOP_ROOM", "SHOP_SCREEN"):
            cards = ss.get("cards", [])
            relics = ss.get("relics", [])
            potions = ss.get("potions", [])
            if 0 <= idx < len(cards):
                return f"Buy {cards[idx].get('name', '?')}"
            # Relics/potions use different indexing in CommunicationMod
        elif screen == "EVENT":
            event_name = ss.get("event_name", "")
            options = ss.get("options", [])
            if 0 <= idx < len(options):
                import re
                text = options[idx].get("text", "?")
                text = re.sub(r"<[^>]+>", "", text)[:50]
                return text
        elif screen == "GRID":
            cards = ss.get("cards", [])
            if 0 <= idx < len(cards):
                action = "Upgrade" if ss.get("for_upgrade") else "Remove" if ss.get("for_purge") else "Select"
                return f"{action} {cards[idx].get('name', '?')}"
        elif screen == "HAND_SELECT":
            hand = ss.get("hand", [])
            if 0 <= idx < len(hand):
                return f"Select {hand[idx].get('name', '?')}"

        # Fallback: use choice_list
        choices = gs.get("choice_list", [])
        if 0 <= idx < len(choices):
            return f"Choose: {choices[idx]}"

    if verb == "end":
        return "End Turn"
    if verb == "proceed":
        return "Proceed"
    if verb in ("skip", "return", "leave"):
        return "Skip"
    if verb == "potion":
        action = parts[1] if len(parts) > 1 else ""
        slot = parts[2] if len(parts) > 2 else "?"
        if action == "use":
            return f"Use Potion {slot}"
        if action == "discard":
            return f"Discard Potion {slot}"
    if verb == "start":
        return f"Start — {parts[1] if len(parts) > 1 else 'IRONCLAD'}"
    if verb == "confirm":
        return "Confirm"

    return command


_event_seq = 0

def _log_event(event: dict):
    """Write event directly to stream_events.jsonl (independent of stream.py).

    This is the reliability fix for Run 1's lost logs — when stream.py restarts,
    decisions posted via HTTP are silently dropped. cmd.py now writes every event
    to the log file itself, so the full run log always exists even if stream.py
    is down.

    Each event gets a unique sequence number to distinguish legitimate repeated
    actions (e.g., playing Strike twice) from tool-retry duplicates.
    """
    global _event_seq
    _event_seq += 1
    event["seq"] = _event_seq
    try:
        os.makedirs(os.path.dirname(EVENT_LOG), exist_ok=True)
        with open(EVENT_LOG, "a") as f:
            f.write(json.dumps(event) + "\n")
    except OSError:
        pass


def _post_decision(command: str, reasoning: str = "", translated_override: str = None,
                    skip_feed: bool = False):
    """Post decision to stream server AND log directly to file."""
    translated = translated_override or _translate_command(command)
    event = {
        "type": "decision",
        "command": command,
        "translated": translated,
        "reasoning": reasoning,
        "skip_feed": skip_feed,
        "timestamp": time.time(),
    }
    # Always log to file (survives stream.py restarts)
    _log_event(event)
    # Also post to stream server for live overlay (best-effort)
    try:
        data = json.dumps({
            "command": command,
            "translated": translated,
            "reasoning": reasoning,
            "skip_feed": skip_feed,
        }).encode()
        req = urllib.request.Request(
            STREAM_URL, data=data,
            headers={"Content-Type": "application/json"},
        )
        urllib.request.urlopen(req, timeout=1)
    except Exception:
        pass  # Stream server might not be running


def _post_feed(text: str, highlight: bool = False):
    """Post a feed-only entry to stream server AND log directly to file."""
    event = {
        "type": "feed",
        "text": text,
        "highlight": highlight,
        "timestamp": time.time(),
    }
    _log_event(event)
    try:
        data = json.dumps({"text": text, "highlight": highlight}).encode()
        req = urllib.request.Request(
            STREAM_URL.replace("/decision", "/feed"),
            data=data,
            headers={"Content-Type": "application/json"},
        )
        urllib.request.urlopen(req, timeout=1)
    except Exception:
        pass


def send(command: str, reason: str = "") -> str:
    """Send a command and return the resulting game state.

    Args:
        command: The game command to send. Card references in play commands
                 can be indices (1-indexed) or card names:
                   "play 3 0"          — play card at index 3 targeting enemy 0
                   "play Bash 0"       — play Bash targeting enemy 0 (resolved automatically)
                   "play Shrug It Off" — play Shrug It Off (no target)
                 Using card names avoids index-shift errors when playing multiple cards.
        reason: REQUIRED — reasoning for the overlay/stream. Explain WHY
                you're making this decision. Viewers need to see your thinking.
                The action will not execute without reasoning.

    Commands:
        play N [target]     — Play card N (1-indexed) at optional target
        end                 — End turn
        choose N            — Choose option N (events, map, rewards, shop)
        choose <name>       — Choose by name (e.g., choose rest, choose smith, choose purge)
        proceed             — Confirm/proceed button
        return              — Skip/cancel/leave button
        potion use N [T]    — Use potion in slot N on optional target T
        potion discard N    — Discard potion in slot N
        start CLASS [A] [S] — Start run (IRONCLAD/THE_SILENT/DEFECT/WATCHER, ascension, seed)
        state               — Re-request state
        key K [timeout]     — Press key K
        wait T              — Wait T milliseconds
    """
    if not reason or not reason.strip():
        return (
            "[ERROR] reason= is REQUIRED. Explain WHY you're making this decision.\n"
            "Example: send('play Bash 0', reason='Applying Vulnerable for damage amplification next turn')\n"
            "The stream overlay shows your reasoning to viewers — it cannot be empty."
        )
    # Fetch pre-command state so translation has current hand/enemies
    global _last_raw_state
    _last_raw_state = _tcp_request({"type": "state"})

    # Guard: prevent proceed on BOSS_REWARD (must choose a relic first)
    gs = _last_raw_state.get("game_state") or {}
    screen = gs.get("screen_type", "")
    cmd_verb = command.strip().split()[0].lower() if command.strip() else ""
    if cmd_verb == "proceed" and screen == "BOSS_REWARD":
        return (
            "[ERROR] Cannot proceed on BOSS_REWARD — you must choose a relic first!\n"
            "Use: send('choose 0', reason='...') to pick a boss relic.\n"
            "Skipping a boss relic is a devastating misplay."
        )

    # Guard: prevent choosing a potion reward when all potion slots are full.
    # CommunicationMod hangs/crashes if you try to pick up a potion with no empty slots.
    if cmd_verb == "choose" and screen == "COMBAT_REWARD":
        parts = command.strip().split()
        if len(parts) >= 2:
            try:
                reward_idx = int(parts[1])
                ss = gs.get("screen_state", {})
                rewards = ss.get("rewards", [])
                if 0 <= reward_idx < len(rewards):
                    reward = rewards[reward_idx]
                    if reward.get("reward_type") == "POTION":
                        potions = gs.get("potions", [])
                        has_empty = any(p.get("id") == "Potion Slot" for p in potions)
                        if not has_empty:
                            potion_name = reward.get("potion", {}).get("name", "potion")
                            return (
                                f"[ERROR] Cannot pick up {potion_name} — all potion slots are full!\n"
                                f"Current potions: {', '.join(p.get('name', '?') for p in potions)}\n"
                                f"Use potion_discard(slot, reason='...') to free a slot first, "
                                f"or use proceed to leave rewards."
                            )
            except ValueError:
                pass  # Non-numeric choose argument, pass through

    # Resolve card names to indices using current hand state
    resolved = _resolve_card_name(_last_raw_state, command)
    # Resolve card names in choose commands (HAND_SELECT, CARD_REWARD, GRID)
    resolved = _resolve_choose_card_name(_last_raw_state, resolved)
    # Resolve shop card/relic names to indices
    resolved = _resolve_shop_choose(_last_raw_state, resolved)
    _post_decision(resolved, reason)
    raw = _tcp_request({"type": "command", "command": resolved})
    _last_raw_state = raw  # Update cache

    # Auto-handle mechanical transitions (gold, chests, shop wait)
    raw = _auto_handle_mechanical(raw)

    return format_state(raw)


def _auto_collect_gold(raw: dict) -> dict:
    """Auto-collect gold/stolen_gold from combat rewards — free value with no downside."""
    global _last_raw_state
    if not raw.get("in_game"):
        return raw
    gs = raw.get("game_state", {})
    if gs.get("screen_type") != "COMBAT_REWARD":
        return raw
    ss = gs.get("screen_state", {})
    rewards = ss.get("rewards", [])
    # Collect all gold rewards (iterate because indices shift after each pick)
    while True:
        gold_idx = None
        for i, r in enumerate(rewards):
            if r.get("reward_type") in ("GOLD", "STOLEN_GOLD"):
                gold_idx = i
                break
        if gold_idx is None:
            break
        # Pick up the gold — always beneficial, never a trade-off.
        raw = _tcp_request({"type": "command", "command": f"choose {gold_idx}"})
        _last_raw_state = raw
        if not raw.get("in_game"):
            return raw
        gs = raw.get("game_state", {})
        if gs.get("screen_type") != "COMBAT_REWARD":
            # Gold was the only reward; screen changed. Return new state.
            return raw
        ss = gs.get("screen_state", {})
        rewards = ss.get("rewards", [])
    return raw


def _auto_wait_shop_screen(raw: dict) -> dict:
    """Wait for SHOP_ROOM → SHOP_SCREEN transition.

    When entering a shop, CommunicationMod briefly shows SHOP_ROOM (no items)
    before transitioning to SHOP_SCREEN (full inventory). This auto-retries
    state() to avoid the agent thrashing on the empty transitional state.
    """
    global _last_raw_state
    if not raw.get("in_game"):
        return raw
    gs = raw.get("game_state", {})
    if gs.get("screen_type") != "SHOP_ROOM":
        return raw
    ss = gs.get("screen_state", {})
    # If SHOP_ROOM already has items, return as-is
    if ss.get("cards") or ss.get("relics") or ss.get("potions"):
        return raw

    # Poll for SHOP_SCREEN (up to 3 seconds, 15 × 200ms)
    for _ in range(15):
        time.sleep(0.2)
        raw = _tcp_request({"type": "state"})
        _last_raw_state = raw
        if not raw.get("in_game"):
            return raw
        gs = raw.get("game_state", {})
        if gs.get("screen_type") != "SHOP_ROOM":
            return raw
        ss = gs.get("screen_state", {})
        if ss.get("cards") or ss.get("relics") or ss.get("potions"):
            return raw
    return raw


def _auto_open_chest(raw: dict) -> dict:
    """Auto-open chests — there is never a reason not to open a chest.

    CommunicationMod shows CHEST screen for both treasure room chests and
    boss treasure chests.  The only available choice is "open".  After opening,
    the screen transitions to the relic reward (or BOSS_REWARD for boss chests).
    Calling proceed on a CHEST screen skips it entirely — a devastating bug.
    """
    global _last_raw_state
    if not raw.get("in_game"):
        return raw
    gs = raw.get("game_state", {})
    if gs.get("screen_type") != "CHEST":
        return raw
    # Send "choose 0" which corresponds to "open"
    raw = _tcp_request({"type": "command", "command": "choose 0"})
    _last_raw_state = raw
    return raw


def _auto_handle_mechanical(raw: dict) -> dict:
    """Handle mechanical transitions that never involve a real decision."""
    raw = _auto_collect_gold(raw)
    raw = _auto_open_chest(raw)
    raw = _auto_wait_shop_screen(raw)
    return raw


def _validate_action(raw: dict, action: str) -> str | None:
    """Check whether the next action in a turn sequence is still valid.

    Returns None if valid, or a reason string if the action should be skipped
    (and the sequence stopped).
    """
    # 1. Still in game?
    if not raw.get("in_game"):
        return "not in game"

    gs = raw.get("game_state", {})
    combat = gs.get("combat_state")

    # 2. Still in combat?
    if not combat:
        screen = gs.get("screen_type", "unknown")
        return f"combat ended (screen: {screen})"

    parts = action.strip().split()
    verb = parts[0].lower() if parts else ""

    # 3. "end" is always valid during combat
    if verb == "end":
        return None

    # 4. "play N [target]" — validate card index and playability
    if verb == "play":
        if len(parts) < 2:
            return "play command missing card index"
        try:
            card_n = int(parts[1])
        except ValueError:
            return f"invalid card index: {parts[1]}"

        hand = combat.get("hand", [])
        if card_n < 1 or card_n > len(hand):
            return f"card index {card_n} out of range (hand has {len(hand)} cards)"

        card = hand[card_n - 1]
        if not card.get("is_playable", False):
            card_name = card.get("name", f"card {card_n}")
            return f"{card_name} is not playable (likely not enough energy)"

        # Validate target if specified (absolute index into full monsters array)
        if len(parts) > 2:
            try:
                target_idx = int(parts[2])
            except ValueError:
                return f"invalid target index: {parts[2]}"
            monsters = combat.get("monsters", [])
            if target_idx < 0 or target_idx >= len(monsters):
                return f"target index {target_idx} out of range ({len(monsters)} monsters)"
            if monsters[target_idx].get("is_gone"):
                return f"target {target_idx} ({monsters[target_idx].get('name', '?')}) is dead/gone"

        return None

    # 5. Potion commands — always valid (rare errors, recoverable)
    if verb == "potion":
        return None

    # Unknown verb — let it through, relay will handle errors
    return None


def turn(actions: list, reason: str = "") -> str:
    """Execute a full combat turn as a batch.

    Plan your entire turn, then execute it all at once. This is how you
    should play combat — reason about your whole hand, figure out the
    optimal sequence, then commit.

    Card references can be indices (1-indexed) or card names:
      "play 3 0"           — play card at index 3 targeting enemy 0
      "play Bash 0"        — play Bash targeting enemy 0 (index resolved automatically)
      "play Shrug It Off"  — play Shrug It Off (no target)
    Using card names avoids index-shift errors when playing multiple cards.

    Args:
        actions: List of command strings, e.g. ["play Bash 0", "play Strike 0", "play Defend", "end"]
                 Card names are resolved against the current hand at execution time,
                 so they're always correct regardless of what was played before.
                 Numeric indices still work: ["play 3 0", "play 2 0", "end"]
                 but indices shift as you play cards — names don't.
        reason: Your reasoning for the whole turn. Shows on stream overlay.

    Returns:
        Final game state after all actions executed.

    If any action fails validation (combat ended, card unplayable, etc.),
    the sequence stops early and returns the current state with a note
    about what happened.
    """
    if not actions:
        return state()

    if not reason or not reason.strip():
        return (
            "[ERROR] reason= is REQUIRED. Explain your combat plan.\n"
            "Example: turn(['play Bash 0', 'play Strike 0', 'end'],\n"
            "         reason='Bash for Vulnerable, Strike for 9 damage. 5 block vs 12 incoming, take 7 to 58 HP.')\n"
            "The stream overlay shows your reasoning to viewers — it cannot be empty."
        )

    # Fetch pre-turn state for translation
    global _last_raw_state
    _last_raw_state = _tcp_request({"type": "state"})

    # Resolve and translate all actions using pre-turn state for the stream
    # (Translation uses original names for readability; resolution happens per-action below)
    translated_actions = [_translate_command(_resolve_card_name(_last_raw_state, a)) for a in actions]
    translated_summary = " → ".join(translated_actions)

    # Post the full plan as one entry in both reasoning and feed
    _post_decision(
        command="; ".join(actions),
        reasoning=reason,
        translated_override=translated_summary,
    )

    total = len(actions)
    stopped_msg = None

    # Execute each action, resolving card names against CURRENT state
    for i, action in enumerate(actions):
        # Resolve card name to index using current hand (not pre-turn hand)
        resolved_action = _resolve_card_name(_last_raw_state, action)

        # Validate before sending (uses current game state)
        if i > 0:
            # First action uses pre-turn state which may not have combat_state
            # fields populated the same way; skip validation for it.
            # After the first action, we have fresh state from the relay.
            fail_reason = _validate_action(_last_raw_state, resolved_action)
            if fail_reason:
                stopped_msg = (
                    f"[SEQUENCE STOPPED after action {i}/{total}: "
                    f"{fail_reason}. Remaining actions skipped.]"
                )
                break

        # Capture hand size before action to detect draws
        pre_combat = (_last_raw_state.get("game_state") or {}).get("combat_state")
        pre_hand_size = len(pre_combat.get("hand", [])) if pre_combat else None

        raw = _tcp_request({"type": "command", "command": resolved_action.strip()})
        _last_raw_state = raw
        if "error" in raw:
            # Auto-handle mechanical transitions even on error
            _last_raw_state = _auto_handle_mechanical(_last_raw_state)
            return format_state(_last_raw_state)

        # Detect draw: if we played a card but hand size didn't shrink, cards were drawn.
        # Stop the sequence so the player can see the new cards and re-plan.
        if (pre_hand_size is not None
                and resolved_action.startswith("play ")
                and i < total - 1  # more actions remain
                and actions[i + 1] != "end"  # next action isn't just "end" -- that's harmless to stop before
                ):
            post_combat = (_last_raw_state.get("game_state") or {}).get("combat_state")
            if post_combat:
                post_hand_size = len(post_combat.get("hand", []))
                if post_hand_size >= pre_hand_size:
                    # Hand didn't shrink — draw happened. Stop sequence.
                    remaining_actions = actions[i + 1:]
                    stopped_msg = (
                        f"[DRAW DETECTED after playing {resolved_action}: "
                        f"hand went from {pre_hand_size} to {post_hand_size} cards. "
                        f"Remaining actions skipped: {remaining_actions}. "
                        f"You drew new cards — read the state and plan the rest of your turn.]"
                    )
                    break

    # Auto-handle mechanical transitions after the turn completes
    _last_raw_state = _auto_handle_mechanical(_last_raw_state)

    formatted = format_state(_last_raw_state)
    if stopped_msg:
        return stopped_msg + "\n\n" + formatted
    return formatted


def play(card, target: int = None, reason: str = "") -> str:
    """Play a card by index or name. Target is enemy index (0-indexed), required for targeted cards.

    Args:
        card: Card index (1-indexed int) or card name (str).
              Examples: 3, "Bash", "Shrug It Off", "Bash+"
        target: Enemy index (0-indexed), required for targeted attack cards.
        reason: REQUIRED — why you're playing this card.
    """
    if target is not None:
        return send(f"play {card} {target}", reason=reason)
    return send(f"play {card}", reason=reason)


def end(reason: str = "End turn") -> str:
    """End turn."""
    return send("end", reason=reason)


def choose(option, reason: str = "") -> str:
    """Choose an option by index or name. reason= is REQUIRED."""
    return send(f"choose {option}", reason=reason)


def proceed(reason: str = "Proceeding") -> str:
    """Press proceed/confirm."""
    return send("proceed", reason=reason)


def skip(reason: str = "Skipping") -> str:
    """Press skip/cancel/leave."""
    return send("return", reason=reason)


def potion_use(slot: int, target: int = None, reason: str = "") -> str:
    """Use a potion. reason= is REQUIRED.

    Automatically strips target for non-targeted potions (Block Potion, etc.)
    to prevent silent CommunicationMod failures.
    """
    # Check if this potion actually requires a target
    if target is not None and _last_raw_state:
        potions = (_last_raw_state.get("game_state") or {}).get("potions", [])
        if slot < len(potions) and not potions[slot].get("requires_target", False):
            target = None  # Strip invalid target for non-targeted potions
    if target is not None:
        return send(f"potion use {slot} {target}", reason=reason)
    return send(f"potion use {slot}", reason=reason)


def potion_discard(slot: int, reason: str = "") -> str:
    """Discard a potion. reason= is REQUIRED."""
    return send(f"potion discard {slot}", reason=reason)


# ---------------------------------------------------------------------------
# Playbook planning and reasoning
# ---------------------------------------------------------------------------

def plan() -> str:
    """Load strategic context for the current situation.

    Auto-detects mode based on game state:
    - In combat: loads enemy files + hand card files + relevant relics
    - Outside combat: loads strategy.md + boss file + full deck/relic/potion notes

    Returns formatted playbook knowledge. Call at the start of each act
    and at the start of each combat.
    """
    global _last_raw_state
    raw = _tcp_request({"type": "state"})
    _last_raw_state = raw

    if not raw.get("in_game", False):
        return "Not in game. Start a run first."

    gs = raw.get("game_state", {})
    combat = gs.get("combat_state")

    if combat:
        return _plan_combat(gs, combat)
    else:
        return _plan_act(gs)


def _plan_combat(gs: dict, combat: dict) -> str:
    """Combat plan: enemy patterns + hand card details + relic effects."""
    lines = ["=== COMBAT PLAN ===", ""]

    # Enemies — load playbook for each unique monster
    monsters = combat.get("monsters", [])
    alive = [m for m in monsters if not m.get("is_gone")]
    enemy_names = []
    seen = set()
    for m in alive:
        name = m.get("name", "?")
        enemy_names.append(name)
        if name in seen:
            continue
        seen.add(name)
        # Try enemies/ first, then bosses/
        entry = _load_playbook("enemies", name)
        if entry is None:
            entry = _load_playbook("bosses", name)
        if entry:
            lines.append(entry)
            lines.append("")
        else:
            lines.append(f"[No playbook entry for enemy: {name}]")
            lines.append("")

    # Hand cards — full playbook entries
    hand = combat.get("hand", [])
    if hand:
        lines.append("--- HAND CARD REFERENCE ---")
        seen_cards = set()
        for card in hand:
            name = card.get("name", "?")
            if card.get("upgrades", 0) > 0 and not name.endswith("+"):
                name += "+"
            base = name.rstrip("+")
            if base in seen_cards or base in _BASIC_CARDS:
                continue
            seen_cards.add(base)
            entry = _load_playbook("cards", name)
            if entry:
                lines.append(entry)
                lines.append("")

    # Relics — all of them (entries are short)
    relics = gs.get("relics", [])
    if relics:
        lines.append("--- RELICS ---")
        for r in relics:
            name = r.get("name", "?")
            counter = r.get("counter", -1)
            entry = _load_playbook("relics", name)
            if entry:
                counter_note = f" [counter: {counter}]" if counter >= 0 else ""
                lines.append(f"{entry}{counter_note}")
                lines.append("")

    summary = f"Combat: vs {' + '.join(enemy_names)}"
    _post_feed(f"PLAN — {summary}", highlight=True)
    _log_event({
        "type": "plan",
        "mode": "combat",
        "summary": summary,
        "timestamp": time.time(),
    })

    return "\n".join(lines)


def _plan_act(gs: dict) -> str:
    """Act plan: strategy + boss prep + deck/relic/potion report."""
    act = gs.get("act", 1)
    boss = gs.get("act_boss", "?")
    deck = gs.get("deck", [])

    lines = ["=== ACT PLAN ===", ""]

    # Strategy overview
    strat = _load_playbook_root("strategy.md")
    if strat:
        lines.append("--- STRATEGY ---")
        lines.append(strat)
        lines.append("")

    # Boss file
    boss_entry = _load_playbook("bosses", boss)
    if boss_entry:
        lines.append(f"--- BOSS: {boss} ---")
        lines.append(boss_entry)
        lines.append("")
    else:
        lines.append(f"[No playbook entry for boss: {boss}]")
        lines.append("")

    # Deck composition summary
    attacks, skills, powers, statuses = 0, 0, 0, 0
    total_cost = 0
    card_count = 0
    for c in deck:
        ctype = c.get("type", "").upper()
        cost = c.get("cost", 0)
        if isinstance(cost, int) and cost >= 0:
            total_cost += cost
            card_count += 1
        if ctype == "ATTACK":
            attacks += 1
        elif ctype == "SKILL":
            skills += 1
        elif ctype == "POWER":
            powers += 1
        else:
            statuses += 1
    avg_cost = round(total_cost / card_count, 1) if card_count > 0 else 0

    lines.append(f"--- DECK ({len(deck)} cards) ---")
    lines.append(f"Attacks: {attacks} | Skills: {skills} | Powers: {powers}" +
                 (f" | Status/Curse: {statuses}" if statuses else ""))
    lines.append(f"Avg cost: {avg_cost}E")
    lines.append("")

    # Card notes — compact (first 2 lines) for non-basic cards
    missing_cards = []
    lines.append("Card Notes:")
    seen_cards = set()
    for c in deck:
        name = c.get("name", "?")
        if c.get("upgrades", 0) > 0 and not name.endswith("+"):
            name += "+"
        base = name.rstrip("+")
        if base in seen_cards or name in _BASIC_CARDS or base in _BASIC_CARDS:
            continue
        seen_cards.add(base)
        top = _load_playbook_top("cards", name)
        if top:
            # Indent under "Card Notes:"
            lines.append(f"  {top.replace(chr(10), chr(10) + '  ')}")
        else:
            missing_cards.append(name)
    lines.append("")

    # Relics
    relics = gs.get("relics", [])
    if relics:
        lines.append(f"--- RELICS ({len(relics)}) ---")
        for r in relics:
            name = r.get("name", "?")
            entry = _load_playbook("relics", name)
            if entry:
                counter = r.get("counter", -1)
                counter_note = f" [counter: {counter}]" if counter >= 0 else ""
                lines.append(f"  {entry}{counter_note}")
                lines.append("")
            else:
                missing_cards.append(f"relic:{name}")

    # Potions
    potions = gs.get("potions", [])
    active_potions = [p for p in potions if p.get("id") != "Potion Slot"]
    if active_potions:
        lines.append("--- POTIONS ---")
        for p in active_potions:
            name = p.get("name", "?")
            entry = _load_playbook("potions", name)
            if entry:
                lines.append(f"  {entry}")
                lines.append("")
            else:
                missing_cards.append(f"potion:{name}")

    # Missing entries
    if missing_cards:
        lines.append("--- MISSING PLAYBOOK ENTRIES ---")
        for m in missing_cards:
            lines.append(f"  {m}")
        lines.append("")

    summary = f"Act {act}: {len(deck)} cards vs {boss}"
    _post_feed(f"PLAN — {summary}", highlight=True)
    _log_event({
        "type": "plan",
        "mode": "act",
        "summary": summary,
        "timestamp": time.time(),
    })

    return "\n".join(lines)


def reason(topic: str) -> str:
    """Look up a specific playbook entry by name.

    Args:
        topic: Name of a card, enemy, boss, event, relic, or potion.
               Examples: "Shrug It Off", "Gremlin Nob", "Hexaghost",
                         "Big Fish", "Pen Nib", "Flex Potion"

    Returns the full playbook entry, or a helpful error if not found.
    """
    categories = ["cards", "enemies", "bosses", "events", "relics", "potions"]

    # Try exact match in each category
    for cat in categories:
        entry = _load_playbook(cat, topic)
        if entry:
            _post_feed(f"LOOKUP — {topic}", highlight=False)
            _log_event({
                "type": "reason",
                "topic": topic,
                "category": cat,
                "timestamp": time.time(),
            })
            return f"=== PLAYBOOK: {topic} ({cat}) ===\n\n{entry}"

    # No exact match — try substring search across all categories
    target = _name_to_filename(topic)
    matches = []
    for cat in categories:
        cat_dir = os.path.join(PLAYBOOK_DIR, cat)
        if not os.path.isdir(cat_dir):
            continue
        for fname in os.listdir(cat_dir):
            if fname.startswith("_"):
                continue
            if target in fname.replace(".md", ""):
                matches.append(f"{cat}/{fname}")

    if matches:
        # Load the first match
        first = matches[0]
        cat, fname = first.split("/", 1)
        path = os.path.join(PLAYBOOK_DIR, cat, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        display_name = fname.replace(".md", "").replace("-", " ").title()
        _post_feed(f"LOOKUP — {display_name}", highlight=False)
        _log_event({
            "type": "reason",
            "topic": topic,
            "category": cat,
            "found": first,
            "timestamp": time.time(),
        })

        if len(matches) == 1:
            return f"=== PLAYBOOK: {display_name} ({cat}) ===\n\n{content}"

        result = f"Multiple matches for \"{topic}\":\n"
        for m in matches:
            result += f"  - {m}\n"
        result += f"\nShowing: {first}\n\n{content}"
        return result

    return (
        f"No playbook entry found for \"{topic}\".\n"
        f"Try the exact game name (e.g., \"Shrug It Off\", \"Gremlin Nob\").\n"
        f"Use reason(\"bash\") for cards, reason(\"hexaghost\") for bosses, etc."
    )


def deck() -> str:
    """View your full deck. Use after transforming, adding, or removing cards
    to assess how the deck changed holistically.

    Returns the full deck sorted by type (Attacks, Skills, Powers, Curses/Status),
    with costs and upgrade status.
    """
    global _last_raw_state
    _last_raw_state = _tcp_request({"type": "state"})
    gs = _last_raw_state.get("game_state", {})
    cards = gs.get("deck", [])

    if not cards:
        return "[No deck found — are you in a run?]"

    # Group by type
    groups = {"ATTACK": [], "SKILL": [], "POWER": [], "STATUS": [], "CURSE": []}
    for c in cards:
        ctype = c.get("type", "UNKNOWN").upper()
        name = c.get("name", "?")
        cost = c.get("cost", "?")
        upgraded = c.get("upgrades", 0) > 0
        display = f"{name}+" if upgraded else name
        groups.setdefault(ctype, []).append(f"  {display} ({cost}E)")

    lines = [f"=== DECK ({len(cards)} cards) ==="]
    for gtype in ["ATTACK", "SKILL", "POWER", "CURSE", "STATUS"]:
        group = groups.get(gtype, [])
        if group:
            lines.append(f"\n{gtype}S ({len(group)}):")
            lines.extend(sorted(group))

    # Summary stats
    costs = [c.get("cost", 0) for c in cards if isinstance(c.get("cost"), int) and c.get("cost", 0) >= 0]
    avg_cost = sum(costs) / len(costs) if costs else 0
    lines.append(f"\nAvg cost: {avg_cost:.1f}E | Total: {len(cards)} cards")

    return "\n".join(lines)


def think(reasoning: str, label: str = "Strategy") -> str:
    """Post your strategic reasoning to the stream overlay.

    Call this after plan() to share your analysis with viewers. The reasoning
    appears in the thinking panel and the action feed.

    This is how viewers see WHY you're making decisions — not just what
    playbook entries were loaded, but your actual strategic synthesis.

    Args:
        reasoning: Your strategic analysis. This is the text viewers will read.
                   For combat: your fight strategy (win condition, survival plan, key cards, risks).
                   For act planning: your pathing logic, deck-building goals, boss prep.
        label: Short label for the action feed (default: "Strategy").
               Examples: "Fight Strategy", "Act Plan", "Boss Prep"

    Example:
        think('''
        WIN CONDITION: Rampage+ scales each play. Play it every cycle.
        SURVIVAL: 32-damage single hit is the threat. Need 3 Defends per cycle.
        KEY CARDS: Rampage+ (scaling), Bash+ (Vulnerable), True Grit (block + thin)
        RISKS: Over-exhausting block cards with True Grit.
        ESTIMATED TURNS: 12-14.
        ''', label="Fight Strategy")
    """
    if not reasoning or not reasoning.strip():
        return "[ERROR] reasoning is required. Share your strategic analysis."
    _post_decision("think", reasoning=reasoning.strip(), translated_override=label)
    return f"[Reasoning posted to stream: {label}]"


def start(character: str = "IRONCLAD", ascension: int = 0, seed: str = None) -> str:
    """Start a new run."""
    cmd = f"start {character}"
    if ascension > 0:
        cmd += f" {ascension}"
    if seed:
        cmd += f" {seed}"
    return send(cmd, reason=f"Starting {character} A{ascension}")


# Allow running directly: python cmd.py state / python cmd.py "play 1 0"
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cmd.py state | python cmd.py <command>")
        sys.exit(1)

    arg = " ".join(sys.argv[1:])
    if arg == "state":
        print(state())
    else:
        print(send(arg))
