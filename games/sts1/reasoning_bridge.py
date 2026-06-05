"""Reasoning bridge: stream a player agent's own deliberation to the overlay.

The player agent reasons in prose (assistant `text` blocks in its transcript) before
each action, but only the terse `reason=` arg it passes to cmd.py reaches the overlay.
This tails the agent's transcript and, whenever a reasoning block is followed by a real
game action (`play.py choose/play/turn/...`), posts that reasoning to stream.py's
/decision endpoint as a think-style event — so the overlay's Strategy panel shows the
agent's actual thinking, live, with zero changes to the agent or the game pipeline.

Read-only on the transcript; POST-only to the stream server. Safe to run mid-run.

    python reasoning_bridge.py <agent-transcript.jsonl> [--from-start]
"""
import json
import os
import sys
import time
import urllib.request

DECISION_URL = "http://127.0.0.1:3002/decision"

# play.py subcommands that are real decisions (vs. pure observation/lookup). The
# reasoning that precedes one of these IS the rationale for that decision.
ACTION_VERBS = {"choose", "play", "turn", "end", "proceed", "skip",
                "potion_use", "potion_discard"}


def post_reasoning(reasoning: str, label: str):
    try:
        data = json.dumps({
            "command": "reasoning",      # distinct tag: overlay routes to Strategy panel ONLY
            "translated": label,         # (not the decision log, not the action feed)
            "reasoning": reasoning,
            "skip_feed": True,
        }).encode()
        req = urllib.request.Request(DECISION_URL, data=data,
                                     headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=2)
        sys.stderr.write(f"[bridge] -> {label}: {reasoning[:70]!r}\n")
        sys.stderr.flush()
    except Exception as e:
        sys.stderr.write(f"[bridge] post failed: {e}\n")


def action_label(command: str) -> str:
    """A short heading for the upcoming action, from the raw play.py command.

    Only the verb (+ its first positional arg for targeted actions) — never the
    trailing reason= string, which is free prose and would clutter the heading.
    """
    toks = command.split()
    try:
        i = next(k for k, t in enumerate(toks) if t.endswith("play.py"))
        rest = toks[i + 1:]
    except StopIteration:
        rest = toks
    if not rest:
        return "Reasoning"
    verb = rest[0]
    if verb in ("play", "choose", "potion_use", "potion_discard") and len(rest) > 1:
        arg = rest[1].strip('"').strip()
        return f"{verb} {arg}"[:40]
    return verb


def extract_play_command(block: dict) -> str | None:
    """If a tool_use block runs `play.py <action-verb>`, return its command string."""
    if block.get("type") != "tool_use" or block.get("name") != "Bash":
        return None
    cmd = str(block.get("input", {}).get("command", ""))
    if "play.py" not in cmd:
        return None
    toks = cmd.split()
    try:
        i = next(k for k, t in enumerate(toks) if t.endswith("play.py"))
        verb = toks[i + 1] if i + 1 < len(toks) else ""
    except StopIteration:
        return None
    return cmd if verb in ACTION_VERBS else None


def handle_record(obj: dict, state: dict):
    """Track the latest reasoning text; flush it when an action follows."""
    if obj.get("type") != "assistant":
        return
    content = obj.get("message", {}).get("content", [])
    if not isinstance(content, list):
        return
    for block in content:
        bt = block.get("type")
        if bt == "text":
            txt = (block.get("text") or "").strip()
            if len(txt) >= 30:                       # skip terse acks ("Done.", "OK")
                state["pending"] = txt
        elif bt == "tool_use":
            cmd = extract_play_command(block)
            if cmd and state.get("pending"):
                post_reasoning(state["pending"], action_label(cmd))
                state["pending"] = None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit("usage: python reasoning_bridge.py <transcript.jsonl> [--from-start]")
    path = args[0]
    from_start = "--from-start" in sys.argv[1:]

    while not os.path.exists(path):
        time.sleep(1.0)

    pos = 0 if from_start else os.path.getsize(path)
    buf = b""
    state = {"pending": None}
    sys.stderr.write(f"[bridge] tailing {os.path.basename(path)} from byte {pos}\n")
    sys.stderr.flush()

    idle = 0
    while True:
        size = os.path.getsize(path)
        if size > pos:
            with open(path, "rb") as f:
                f.seek(pos)
                chunk = f.read()
                pos = f.tell()
            buf += chunk
            *lines, buf = buf.split(b"\n")
            for raw in lines:
                if not raw.strip():
                    continue
                try:
                    obj = json.loads(raw.decode("utf-8", "replace"))
                except json.JSONDecodeError:
                    continue
                handle_record(obj, state)
            idle = 0
        else:
            idle += 1
        time.sleep(1.0)


if __name__ == "__main__":
    main()
