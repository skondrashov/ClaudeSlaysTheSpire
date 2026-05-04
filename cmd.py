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
    raw = _tcp_request({"type": "state"})
    return format_state(raw)


def state_raw() -> dict:
    """Get current game state as raw dict."""
    return _tcp_request({"type": "state"})


def _post_decision(command: str, reasoning: str = ""):
    """Post decision to stream server (best-effort, non-blocking)."""
    try:
        data = json.dumps({"command": command, "reasoning": reasoning}).encode()
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
    _post_decision(command, reason)
    raw = _tcp_request({"type": "command", "command": command})
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
