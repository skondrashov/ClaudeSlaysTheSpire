"""Single-session helper to avoid lock conflicts between subprocess calls."""
import sys
import os
import json
import uuid

sys.path.insert(0, r'C:\Users\tkond\projects\autoplay\games\sts1')

# Set a consistent session ID so all calls from this script use the same session
FIXED_SESSION = "player-agent-fixed-session-001"
os.environ["PLAYER_SESSION"] = FIXED_SESSION

# Remove any stale lock before importing cmd
lock_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "player.lock")
if os.path.exists(lock_file):
    os.remove(lock_file)

from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, start, state_raw, _tcp_request
from bot.state_formatter import format_state

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python play.py <command>")
        sys.exit(1)

    cmd = sys.argv[1]
    args = sys.argv[2:] if len(sys.argv) > 2 else []

    if cmd == "state":
        print(state())
    elif cmd == "send":
        # python play.py send "choose 0" "reason text"
        command = args[0] if args else ""
        reason = args[1] if len(args) > 1 else "executing"
        print(send(command, reason=reason))
    elif cmd == "turn":
        # python play.py turn "play 1 0|play 2 0|end" "reason text"
        actions = args[0].split("|") if args else []
        reason = args[1] if len(args) > 1 else "executing turn"
        print(turn(actions, reason=reason))
    elif cmd == "raw":
        result = _tcp_request({'type': 'command', 'command': 'state'})
        print(format_state(result))
    else:
        print(f"Unknown command: {cmd}")
