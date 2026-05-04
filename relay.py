"""
Relay: bridges CommunicationMod's stdin/stdout to a TCP server.

CommunicationMod launches this as a child process. It sends JSON game state
on our stdin when the game stabilizes, and reads our command from stdout.

We run a TCP server on port 19284. Claude Code (via cmd.py) connects, reads
state, and sends commands. We forward commands to stdout.

Protocol (TCP side):
  - Client connects
  - We send: JSON game state line (newline-terminated)
  - Client sends: command string (newline-terminated), e.g. "play 1 0\n"
  - We write command to stdout for CommunicationMod
  - Connection closes
  - Next state arrives from stdin, cycle repeats
"""

import json
import os
import socket
import sys
import threading
import time

HOST = "127.0.0.1"
PORT = 19284
STATE_FILE = os.path.join(os.path.dirname(__file__), "data", "last_state.json")

# Shared state between stdin reader and TCP server
current_state = None
state_ready = threading.Event()
command_received = threading.Event()
command_value = None
lock = threading.Lock()


def log(msg):
    print(f"[relay] {msg}", file=sys.stderr, flush=True)


def stdin_reader():
    """Read game state from CommunicationMod on stdin."""
    global current_state
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

        # Signal that state is available
        state_ready.set()

        # Only wait for a command if the game is ready for one
        if ready or not is_error:
            command_received.wait()
            command_received.clear()

            # Write command to stdout for CommunicationMod
            with lock:
                cmd = command_value
            log(f"Sending command: {cmd}")
            print(cmd, flush=True)
        else:
            log("Error without ready_for_command, skipping command wait")

    log("stdin closed, exiting")


def tcp_server():
    """TCP server that Claude Code connects to via cmd.py."""
    global command_value

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
                # Return current state (wait for it if not ready yet)
                if not state_ready.wait(timeout=60):
                    conn.sendall(json.dumps({"error": "timeout waiting for state"}).encode() + b"\n")
                    conn.close()
                    continue

                with lock:
                    state = current_state
                conn.sendall(json.dumps(state).encode() + b"\n")
                conn.close()

            elif req_type == "command":
                # Forward command to CommunicationMod
                cmd = request.get("command", "").strip()
                if not cmd:
                    conn.sendall(json.dumps({"error": "empty command"}).encode() + b"\n")
                    conn.close()
                    continue

                with lock:
                    command_value = cmd
                state_ready.clear()
                command_received.set()

                # Wait for next state to arrive (confirms command was processed)
                if state_ready.wait(timeout=60):
                    with lock:
                        state = current_state
                    conn.sendall(json.dumps(state).encode() + b"\n")
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
