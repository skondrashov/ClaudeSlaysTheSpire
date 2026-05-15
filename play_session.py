import sys
from cmd import state, send, play, end, choose, proceed, skip, potion_use, start, turn

if len(sys.argv) < 2:
    print(state())
elif sys.argv[1] == "start":
    char = sys.argv[2] if len(sys.argv) > 2 else "IRONCLAD"
    asc = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    print(start(char, asc))
elif sys.argv[1] == "choose":
    idx = sys.argv[2]
    reason = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else "choosing"
    print(choose(idx, reason=reason))
elif sys.argv[1] == "play":
    card = sys.argv[2]
    try:
        card = int(card)
    except ValueError:
        pass
    reason_start = 3
    target = None
    if len(sys.argv) > 3:
        try:
            target = int(sys.argv[3])
            reason_start = 4
        except ValueError:
            pass
    reason = " ".join(sys.argv[reason_start:]) if len(sys.argv) > reason_start else "playing card"
    print(play(card, target=target, reason=reason))
elif sys.argv[1] == "end":
    reason = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "End turn"
    print(end(reason=reason))
elif sys.argv[1] == "proceed":
    reason = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "Proceeding"
    print(proceed(reason=reason))
elif sys.argv[1] == "skip":
    reason = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "Skipping"
    print(skip(reason=reason))
elif sys.argv[1] == "potion":
    slot = int(sys.argv[2])
    target = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else None
    reason_start = 4 if target is not None else 3
    reason = " ".join(sys.argv[reason_start:]) if len(sys.argv) > reason_start else "using potion"
    print(potion_use(slot, target=target, reason=reason))
elif sys.argv[1] == "send":
    cmd = sys.argv[2]
    reason = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else "sending command"
    print(send(cmd, reason=reason))
elif sys.argv[1] == "turn":
    import json
    actions = json.loads(sys.argv[2])
    reason = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else "executing turn"
    print(turn(actions, reason=reason))
else:
    print(f"Unknown command: {sys.argv[1]}")
