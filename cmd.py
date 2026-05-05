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

import atexit
import json
import os
import socket
import sys
import time
import urllib.request
import uuid

from bot.state_formatter import format_state

HOST = "127.0.0.1"
PORT = 19284
TIMEOUT = 120  # seconds — long timeout for slow animations
STREAM_URL = "http://127.0.0.1:3002/decision"
LOCK_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "player.lock")
LOCK_STALE_SECONDS = 300  # lock expires after 5 minutes of inactivity

# Direct event log — backup for when stream.py is down.
# stream.py restarts during a run used to silently lose decisions.
# Now cmd.py always writes to this file, so the full run log survives.
EVENT_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "stream_events.jsonl")

# Each import of cmd.py gets a unique session ID.
# Two agents importing cmd.py = two sessions = lock conflict.
_SESSION_ID = str(uuid.uuid4())


def _acquire_lock():
    """Acquire the player lock. Explodes if another session holds it."""
    os.makedirs(os.path.dirname(LOCK_FILE), exist_ok=True)

    if os.path.exists(LOCK_FILE):
        try:
            with open(LOCK_FILE) as f:
                lock = json.load(f)
            other_id = lock.get("session_id", "")
            lock_time = lock.get("timestamp", 0)

            # Our lock — just refresh the timestamp
            if other_id == _SESSION_ID:
                lock["timestamp"] = time.time()
                with open(LOCK_FILE, "w") as f:
                    json.dump(lock, f)
                return

            age = time.time() - lock_time
            if age < LOCK_STALE_SECONDS:
                raise RuntimeError(
                    f"\n{'='*60}\n"
                    f"PLAYER LOCK CONFLICT\n"
                    f"{'='*60}\n"
                    f"Another player agent is already running!\n"
                    f"  Session: {other_id[:12]}...\n"
                    f"  Last active: {int(age)}s ago\n"
                    f"\n"
                    f"Only ONE player agent can run at a time.\n"
                    f"Kill the other agent before starting a new one.\n"
                    f"To force-break: from cmd import force_unlock; force_unlock()\n"
                    f"{'='*60}\n"
                )
            else:
                print(f"[cmd] Stale lock from {other_id[:12]}... ({int(age)}s old) — taking over",
                      file=sys.stderr)
        except (json.JSONDecodeError, OSError):
            pass  # corrupted lock, take it

    # Write our lock
    with open(LOCK_FILE, "w") as f:
        json.dump({"session_id": _SESSION_ID, "timestamp": time.time()}, f)


def _release_lock():
    """Release our lock on exit (best-effort)."""
    try:
        if os.path.exists(LOCK_FILE):
            with open(LOCK_FILE) as f:
                lock = json.load(f)
            if lock.get("session_id") == _SESSION_ID:
                os.remove(LOCK_FILE)
                print("[cmd] Player lock released", file=sys.stderr)
    except Exception:
        pass


def force_unlock():
    """Force-break the player lock. Use when a stale agent left a lock behind."""
    try:
        if os.path.exists(LOCK_FILE):
            with open(LOCK_FILE) as f:
                lock = json.load(f)
            print(f"Removing lock from session {lock.get('session_id', '?')[:12]}...")
        os.remove(LOCK_FILE)
        print("Lock removed.")
    except FileNotFoundError:
        print("No lock file found.")
    except Exception as e:
        print(f"Error: {e}")


# Release lock when this process exits
atexit.register(_release_lock)


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
    _acquire_lock()
    global _last_raw_state
    raw = _tcp_request({"type": "state"})
    _last_raw_state = raw
    return format_state(raw)


def state_raw() -> dict:
    """Get current game state as raw dict."""
    global _last_raw_state
    raw = _tcp_request({"type": "state"})
    _last_raw_state = raw
    return raw


# Cached state for translating commands to readable text
_last_raw_state = None


def _resolve_card_name(raw_state: dict, action: str) -> str:
    """Translate card names in play commands to indices at execution time.

    If the action is a 'play' command with a card name instead of an index,
    look up the card in the current hand and replace the name with its index.

    Examples:
        "play Bash 0"       -> "play 2 0"   (if Bash is at index 2)
        "play Shrug It Off"  -> "play 3"     (if Shrug It Off is at index 3)
        "play Bash+ 0"      -> "play 2 0"   (matches upgraded Bash specifically)
        "play 3 0"           -> "play 3 0"   (numeric index, unchanged)
    """
    if not action or not action.strip().lower().startswith("play "):
        return action

    parts = action.strip().split()
    if len(parts) < 2:
        return action

    # Extract everything after "play"
    after_play = action.strip()[len("play "):].strip()

    # Determine if the last token is a target (a digit)
    tokens = after_play.split()
    if tokens and tokens[-1].isdigit() and len(tokens) > 1:
        target = tokens[-1]
        card_ref = " ".join(tokens[:-1])
    else:
        target = None
        card_ref = after_play

    # If card_ref is a pure number, it's already an index — leave as-is
    try:
        int(card_ref)
        return action  # backwards compatible
    except ValueError:
        pass

    # Look up the card by name in the current hand
    if not raw_state:
        return action
    combat = (raw_state.get("game_state") or {}).get("combat_state")
    if not combat:
        return action
    hand = combat.get("hand", [])
    if not hand:
        return action

    # Check if the name ends with '+' (upgrade-specific match)
    require_upgrade = card_ref.endswith("+")
    search_name = card_ref[:-1] if require_upgrade else card_ref

    # Find first matching card (case-insensitive)
    for i, card in enumerate(hand):
        card_name = card.get("name", "")
        if card_name.lower() == search_name.lower():
            if require_upgrade and card.get("upgrades", 0) < 1:
                continue
            idx = i + 1  # 1-indexed
            if target is not None:
                return f"play {idx} {target}"
            else:
                return f"play {idx}"

    # No match found — return unchanged, let relay handle the error
    return action


def _translate_named_choose(name: str, screen: str) -> str:
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
            monsters = [m for m in combat.get("monsters", []) if not m.get("is_gone")]
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
            return _translate_named_choose(parts[1], screen)

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
                if event_name:
                    return f"{event_name}: {text}"
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
        reason: Optional reasoning for the overlay/stream. Explain why
                you're making this decision — viewers want to understand.

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
    _acquire_lock()
    # Fetch pre-command state so translation has current hand/enemies
    global _last_raw_state
    _last_raw_state = _tcp_request({"type": "state"})
    # Resolve card names to indices using current hand state
    resolved = _resolve_card_name(_last_raw_state, command)
    _post_decision(resolved, reason)
    raw = _tcp_request({"type": "command", "command": resolved})
    _last_raw_state = raw  # Update cache

    # Auto-handle mechanical transitions (shop, chest, gold collection)
    raw = _auto_handle_mechanical(raw)

    return format_state(raw)


def _auto_proceed_shop(raw: dict) -> dict:
    """If we landed on an empty SHOP_ROOM, auto-proceed to get the real shop screen."""
    global _last_raw_state
    if not raw.get("in_game"):
        return raw
    gs = raw.get("game_state", {})
    if gs.get("screen_type") != "SHOP_ROOM":
        return raw
    ss = gs.get("screen_state", {})
    # Only auto-proceed if shop inventory is empty (the transition state)
    if ss.get("cards") or ss.get("relics") or ss.get("potions"):
        return raw
    # Auto-proceed to load the actual shop
    raw = _tcp_request({"type": "command", "command": "proceed"})
    _last_raw_state = raw
    return raw


def _auto_proceed_chest(raw: dict) -> dict:
    """Auto-open chests — there's never a reason not to open them."""
    global _last_raw_state
    if not raw.get("in_game"):
        return raw
    gs = raw.get("game_state", {})
    if gs.get("screen_type") != "CHEST":
        return raw
    # Chests always contain loot; opening is never a decision.
    raw = _tcp_request({"type": "command", "command": "proceed"})
    _last_raw_state = raw
    return raw


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


def _auto_handle_mechanical(raw: dict) -> dict:
    """Handle mechanical transitions that never involve a real decision."""
    raw = _auto_proceed_shop(raw)
    raw = _auto_proceed_chest(raw)
    raw = _auto_collect_gold(raw)
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

        # Validate target if specified
        if len(parts) > 2:
            try:
                target_idx = int(parts[2])
            except ValueError:
                return f"invalid target index: {parts[2]}"
            monsters = combat.get("monsters", [])
            alive = [m for m in monsters if not m.get("is_gone")]
            if target_idx < 0 or target_idx >= len(alive):
                return f"target index {target_idx} out of range ({len(alive)} alive monsters)"

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

    _acquire_lock()
    # Fetch pre-turn state for translation
    global _last_raw_state
    _last_raw_state = _tcp_request({"type": "state"})

    # Resolve and translate all actions using pre-turn state for the stream
    # (Translation uses original names for readability; resolution happens per-action below)
    translated_actions = [_translate_command(_resolve_card_name(_last_raw_state, a)) for a in actions]
    translated_summary = " → ".join(translated_actions)

    # Post the full plan as one reasoning entry (skip the combined feed entry)
    _post_decision(
        command="; ".join(actions),
        reasoning=reason,
        translated_override=translated_summary,
        skip_feed=True,
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

        # Re-translate with resolved action for accurate feed display
        _post_feed(_translate_command(resolved_action))
        raw = _tcp_request({"type": "command", "command": resolved_action.strip()})
        _last_raw_state = raw
        if "error" in raw:
            # Auto-handle mechanical transitions even on error
            _last_raw_state = _auto_handle_mechanical(_last_raw_state)
            return format_state(_last_raw_state)

    # Auto-handle mechanical transitions after the turn completes
    _last_raw_state = _auto_handle_mechanical(_last_raw_state)

    formatted = format_state(_last_raw_state)
    if stopped_msg:
        return stopped_msg + "\n\n" + formatted
    return formatted


def play(card, target: int = None) -> str:
    """Play a card by index or name. Target is enemy index (0-indexed), required for targeted cards.

    Args:
        card: Card index (1-indexed int) or card name (str).
              Examples: 3, "Bash", "Shrug It Off", "Bash+"
        target: Enemy index (0-indexed), required for targeted attack cards.
    """
    if target is not None:
        return send(f"play {card} {target}")
    return send(f"play {card}")


def end() -> str:
    """End turn."""
    return send("end")


def choose(option) -> str:
    """Choose an option by index or name."""
    return send(f"choose {option}")


def proceed() -> str:
    """Press proceed/confirm."""
    return send("proceed")


def skip() -> str:
    """Press skip/cancel/leave."""
    return send("return")


def potion_use(slot: int, target: int = None) -> str:
    """Use a potion."""
    if target is not None:
        return send(f"potion use {slot} {target}")
    return send(f"potion use {slot}")


def potion_discard(slot: int) -> str:
    """Discard a potion."""
    return send(f"potion discard {slot}")


def start(character: str = "IRONCLAD", ascension: int = 0, seed: str = None) -> str:
    """Start a new run."""
    cmd = f"start {character}"
    if ascension > 0:
        cmd += f" {ascension}"
    if seed:
        cmd += f" {seed}"
    return send(cmd)


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
