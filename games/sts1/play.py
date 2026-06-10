"""Single-session helper to avoid lock conflicts between subprocess calls."""
import sys
import os
import json
import uuid

sys.path.insert(0, r'C:\Users\tkond\projects\praxis\games\sts1')

# Set a consistent session ID so all calls from this script use the same session
FIXED_SESSION = "player-agent-fixed-session-001"
os.environ["PLAYER_SESSION"] = FIXED_SESSION

# Remove any stale lock before importing cmd
lock_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "player.lock")
if os.path.exists(lock_file):
    os.remove(lock_file)

from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, start, think, deck, state_raw, _tcp_request, survey, recall
from bot.state_formatter import format_state

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
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
    elif cmd == "play":
        # python play.py play "card_index [target]" "reason text"
        play_args = args[0] if args else ""
        reason = args[1] if len(args) > 1 else "playing card"
        parts = play_args.split()
        card_idx = int(parts[0]) if parts else 1
        target = int(parts[1]) if len(parts) > 1 else None
        if target is not None:
            print(play(card_idx, target, reason=reason))
        else:
            print(play(card_idx, reason=reason))
    elif cmd == "end":
        reason = args[0] if args else "ending turn"
        print(end(reason=reason))
    elif cmd == "choose":
        # Accept an index OR a name (shops/rewards need by-name). cmd.choose handles both.
        raw = args[0] if args else "0"
        try:
            opt = int(raw)
        except ValueError:
            opt = raw
        reason = args[1] if len(args) > 1 else "choosing"
        print(choose(opt, reason=reason))
    elif cmd == "proceed":
        reason = args[0] if args else "proceeding"
        print(proceed(reason=reason))
    elif cmd == "skip":
        reason = args[0] if args else "skipping"
        print(skip(reason=reason))
    elif cmd == "think":
        text = args[0] if args else ""
        label = args[1] if len(args) > 1 else "THINKING"
        print(think(text, label))
    elif cmd == "deck":
        print(deck())
    elif cmd == "potion_use":
        # potion_use <slot-or-name> [target] [reason] — slot may be a potion NAME
        # (slots renumber after each drink; names are stable). Target optional, so
        # a non-numeric second arg is the reason.
        idx = args[0] if args else 0   # cmd.potion_use resolves names itself
        target = None
        reason = "using potion"
        if len(args) > 1:
            try:
                target = int(args[1])
                reason = args[2] if len(args) > 2 else reason
            except ValueError:
                reason = args[1]
        if target is not None:
            print(potion_use(idx, target, reason=reason))
        else:
            print(potion_use(idx, reason=reason))
    elif cmd == "potion_discard":
        idx = int(args[0]) if args else 0
        reason = args[1] if len(args) > 1 else "discarding potion"
        print(potion_discard(idx, reason=reason))
    elif cmd == "raw":
        result = _tcp_request({'type': 'command', 'command': 'state'})
        print(format_state(result))
    elif cmd == "start":
        char = args[0] if args else "IRONCLAD"
        asc = int(args[1]) if len(args) > 1 else 0
        seed = args[2] if len(args) > 2 else None
        print(start(char, asc, seed) if seed else start(char, asc))
    elif cmd == "survey":
        print(survey())
    elif cmd == "recall":
        print(recall(*args) if args else "recall: needs one or more handles")
    else:
        print(f"Unknown command: {cmd}")
