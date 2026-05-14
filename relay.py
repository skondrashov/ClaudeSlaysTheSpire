"""
Relay: bridges CommunicationMod's stdin/stdout to a TCP server.

CommunicationMod launches this as a child process. It sends JSON game state
on our stdin when the game stabilizes, and reads our command from stdout.

We run a TCP server on port 19284. Claude Code (via cmd.py) connects, reads
state, and sends commands. We forward commands to stdout.

CommunicationMod's protocol is lock-step: it sends a state, then waits for
a command before sending the next state. The relay keeps this cycle moving
even when no TCP client is active — if no command arrives within IDLE_TIMEOUT,
we send "state" as a keep-alive so CommunicationMod stays in sync with the
actual game state (e.g., if the user clicks Continue from the main menu).

Protocol (TCP side):
  - Client sends JSON request: {"type": "state"} or {"type": "command", "command": "..."}
  - "state" returns the latest cached game state immediately
  - "command" forwards to CommunicationMod and returns the resulting state
"""

import json
import os
import queue
import socket
import sys
import threading
import time

HOST = "127.0.0.1"
PORT = 19284
STATE_FILE = os.path.join(os.path.dirname(__file__), "data", "last_state.json")

# How long stdin_reader waits for a client command before sending a
# keep-alive "state" to CommunicationMod. Lower = more responsive to game
# state changes when idle, but more I/O. 1 second is a good balance.
IDLE_TIMEOUT = 1.0

# Shared state between stdin reader and TCP server
current_state = None
state_ready = threading.Event()       # Set once first state arrives, never cleared
command_queue = queue.Queue()          # TCP server puts commands, stdin_reader gets them
command_result = threading.Event()     # Signals that a command's result state is ready
result_state = None                    # The state resulting from the last client command
lock = threading.Lock()


def log(msg):
    print(f"[relay] {msg}", file=sys.stderr, flush=True)


def stdin_reader():
    """Read game state from CommunicationMod on stdin.

    Participates in CommunicationMod's lock-step protocol:
    receive state → send command → receive state → ...

    If a TCP client has submitted a command, we forward it.
    Otherwise, we send "state" as a keep-alive to prevent blocking.
    """
    global current_state, result_state
    waiting_for_result = False

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            state = json.loads(line)
        except json.JSONDecodeError:
            log(f"Bad JSON from stdin: {line[:100]}")
            continue

        # Check if this is an error or a real state
        is_error = "error" in state
        ready = state.get("ready_for_command", False)

        with lock:
            current_state = state

        # Write state to file for overlay/debugging
        try:
            os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
            with open(STATE_FILE, "w") as f:
                json.dump(state, f)
        except OSError:
            pass

        if is_error:
            log(f"Error from game: {state.get('error', '?')}")
        else:
            log(f"State received: screen={state.get('game_state', {}).get('screen_type', '?')}")

        # Signal that we have at least one state (for initial state requests)
        state_ready.set()

        # If this state is the result of a client command, deliver it
        if waiting_for_result:
            result_state = state
            command_result.set()
            waiting_for_result = False
            # Fall through to check for next command — CommunicationMod
            # is waiting for one.

        # CommunicationMod is ready for a command
        if ready or not is_error:
            try:
                cmd = command_queue.get(timeout=IDLE_TIMEOUT)
                log(f"Sending command: {cmd}")
                print(cmd, flush=True)
                waiting_for_result = True
            except queue.Empty:
                # No client command pending. Send "state" to keep
                # CommunicationMod's lock-step protocol moving. This way
                # it can push updated state when the game changes (e.g.,
                # user loads a save, enters combat, etc.).
                print("state", flush=True)
        else:
            log("Error without ready_for_command, skipping command wait")

    log("stdin closed, exiting")


def tcp_server():
    """TCP server that Claude Code connects to via cmd.py."""

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen(1)
    srv.settimeout(1.0)
    log(f"TCP server listening on {HOST}:{PORT}")

    while True:
        try:
            conn, addr = srv.accept()
        except socket.timeout:
            continue
        except OSError:
            break

        try:
            conn.settimeout(120.0)

            # Read request from client
            data = b""
            while b"\n" not in data:
                chunk = conn.recv(4096)
                if not chunk:
                    break
                data += chunk

            if not data.strip():
                conn.close()
                continue

            request = json.loads(data.strip())
            req_type = request.get("type", "")

            if req_type == "state":
                # Return current cached state (wait for first state if needed)
                if not state_ready.wait(timeout=60):
                    conn.sendall(json.dumps({"error": "timeout waiting for state"}).encode() + b"\n")
                    conn.close()
                    continue

                with lock:
                    state = current_state
                conn.sendall(json.dumps(state).encode() + b"\n")
                conn.close()

            elif req_type == "command":
                # Forward command to CommunicationMod via stdin_reader
                cmd = request.get("command", "").strip()
                if not cmd:
                    conn.sendall(json.dumps({"error": "empty command"}).encode() + b"\n")
                    conn.close()
                    continue

                command_result.clear()
                command_queue.put(cmd)

                # Wait for stdin_reader to forward our command and receive
                # the resulting state from CommunicationMod
                if command_result.wait(timeout=60):
                    conn.sendall(json.dumps(result_state).encode() + b"\n")
                else:
                    conn.sendall(json.dumps({"status": "ok", "note": "command sent, state pending"}).encode() + b"\n")
                conn.close()

            else:
                conn.sendall(json.dumps({"error": f"unknown request type: {req_type}"}).encode() + b"\n")
                conn.close()

        except Exception as e:
            log(f"TCP error: {e}")
            try:
                conn.close()
            except Exception:
                pass


def main():
    # Signal ready to CommunicationMod
    print("ready", flush=True)
    log("Sent ready signal")

    # Start stdin reader in background
    t = threading.Thread(target=stdin_reader, daemon=True)
    t.start()

    # Run TCP server in main thread
    tcp_server()


if __name__ == "__main__":
    main()
