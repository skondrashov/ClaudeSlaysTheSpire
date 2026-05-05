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
import socket
import sys
import urllib.request

from bot.state_formatter import format_state

HOST = "127.0.0.1"
PORT = 19284
TIMEOUT = 120  # seconds — long timeout for slow animations
STREAM_URL = "http://127.0.0.1:3002/decision"


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
            options = ss.get("options", [])
            if 0 <= idx < len(options):
                import re
                text = options[idx].get("text", "?")
                return re.sub(r"<[^>]+>", "", text)[:50]
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


def _post_decision(command: str, reasoning: str = ""):
    """Post decision to stream server (best-effort, non-blocking)."""
    try:
        translated = _translate_command(command)
        data = json.dumps({
            "command": command,
            "translated": translated,
            "reasoning": reasoning,
        }).encode()
        req = urllib.request.Request(
            STREAM_URL, data=data,
            headers={"Content-Type": "application/json"},
        )
        urllib.request.urlopen(req, timeout=1)
    except Exception:
        pass  # Stream server might not be running


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
    # Fetch pre-command state so translation has current hand/enemies
    global _last_raw_state
    _last_raw_state = _tcp_request({"type": "state"})
    _post_decision(command, reason)
    raw = _tcp_request({"type": "command", "command": command})
    _last_raw_state = raw  # Update cache
    return format_state(raw)


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
