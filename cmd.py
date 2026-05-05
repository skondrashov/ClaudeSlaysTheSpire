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


def _log_event(event: dict):
    """Write event directly to stream_events.jsonl (independent of stream.py).

    This is the reliability fix for Run 1's lost logs — when stream.py restarts,
    decisions posted via HTTP are silently dropped. cmd.py now writes every event
    to the log file itself, so the full run log always exists even if stream.py
    is down.
    """
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
        command: The game command to send.
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
    _post_decision(command, reason)
    raw = _tcp_request({"type": "command", "command": command})
    _last_raw_state = raw  # Update cache
    return format_state(raw)


def turn(actions: list, reason: str = "") -> str:
    """Execute a full combat turn as a batch.

    Plan your entire turn, then execute it all at once. This is how you
    should play combat — reason about your whole hand, figure out the
    optimal sequence, then commit.

    Args:
        actions: List of command strings, e.g. ["play 1 0", "play 3", "play 2 0", "end"]
                 Card indices shift as you play cards! If you play card 3, what was card 4
                 becomes card 3. Plan your indices accordingly (play highest indices first
                 to avoid shifting, or account for the shifts).
        reason: Your reasoning for the whole turn. Shows on stream overlay.

    Returns:
        Final game state after all actions executed.

    If any action produces an error state, execution stops and returns that state.
    """
    if not actions:
        return state()

    _acquire_lock()
    # Fetch pre-turn state for translation
    global _last_raw_state
    _last_raw_state = _tcp_request({"type": "state"})

    # Translate all actions using pre-turn state for the stream
    translated_actions = [_translate_command(a) for a in actions]
    translated_summary = " → ".join(translated_actions)

    # Post the full plan as one reasoning entry (skip the combined feed entry)
    _post_decision(
        command="; ".join(actions),
        reasoning=reason,
        translated_override=translated_summary,
        skip_feed=True,
    )

    # Execute each action, posting individual feed entries
    for i, action in enumerate(actions):
        _post_feed(translated_actions[i])
        raw = _tcp_request({"type": "command", "command": action.strip()})
        _last_raw_state = raw
        if "error" in raw:
            return format_state(raw)

    return format_state(_last_raw_state)


def play(card: int, target: int = None) -> str:
    """Play a card. Card is 1-indexed. Target is enemy index (0-indexed), required for targeted cards."""
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
