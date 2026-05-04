"""
Supervisor: launches Claude Code CLI sessions to play Slay the Spire.

Starts a Claude Code session with instructions to play the game.
When a session ends (context limit, crash, /exit), restarts with
a recovery prompt.

Usage:
    python play.py                    # Start playing (Ironclad A0)
    python play.py --character WATCHER --ascension 5
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path

PROJECT_DIR = Path(__file__).parent

INITIAL_PROMPT = """You are playing Slay the Spire. The game is running with CommunicationMod.

First, import the game interface:
    from cmd import state, send, play, end, choose, proceed, skip, potion_use, start

Check the current game state:
    print(state())

If no run is in progress, start one:
    print(start("{character}", {ascension}))

Then play. Each turn:
1. Read the game state carefully — enemies, intents, hand, energy, HP
2. Think about what to do — consider enemy damage, your block options, kill potential
3. Execute ONE action at a time and read the result

Key commands:
    play(card_index, target)  — Play a card (1-indexed). Target is enemy index for targeted cards.
    end()                     — End your turn
    choose(index_or_name)     — Choose an option (events, map, card rewards, shop)
    proceed()                 — Confirm/proceed
    skip()                    — Skip/cancel/leave
    potion_use(slot, target)  — Use a potion

Play continuously — make one decision at a time, never stop. When a run ends, start a new one.
Think out loud about your strategy. Explain your reasoning for key decisions.
"""

RECOVERY_PROMPT = """You are playing Slay the Spire. The previous session ended (likely context limit).

Import the game interface and check what's happening:
    from cmd import state, send, play, end, choose, proceed, skip, potion_use, start
    print(state())

Resume playing. If a run is in progress, continue it. If not, start a new one with start("{character}", {ascension}).
Play continuously — one decision at a time, think out loud.
"""


def run_session(prompt: str, session_num: int, resume: bool = False) -> int:
    """Launch one Claude Code session. Returns exit code."""
    cmd = ["claude", "--dangerously-skip-permissions"]
    if resume:
        cmd.append("--resume")
    cmd.extend(["--print", prompt])

    print(f"\n{'=' * 60}")
    print(f"Session {session_num} starting at {time.strftime('%H:%M:%S')}")
    print(f"{'=' * 60}\n")

    proc = subprocess.run(
        cmd,
        cwd=str(PROJECT_DIR),
        stdin=sys.stdin,
        stdout=sys.stdout,
        stderr=sys.stderr,
    )
    return proc.returncode


def main():
    parser = argparse.ArgumentParser(description="Launch Claude to play Slay the Spire")
    parser.add_argument("--character", default="IRONCLAD", help="Character class")
    parser.add_argument("--ascension", type=int, default=0, help="Ascension level")
    args = parser.parse_args()

    character = args.character.upper()
    ascension = args.ascension

    session_num = 0
    while True:
        session_num += 1
        if session_num == 1:
            prompt = INITIAL_PROMPT.format(character=character, ascension=ascension)
            code = run_session(prompt, session_num, resume=False)
        else:
            prompt = RECOVERY_PROMPT.format(character=character, ascension=ascension)
            code = run_session(prompt, session_num, resume=True)

        print(f"\nSession {session_num} ended with code {code}")
        print("Restarting in 3 seconds... (Ctrl+C to stop)")
        try:
            time.sleep(3)
        except KeyboardInterrupt:
            print("\nStopped.")
            break


if __name__ == "__main__":
    main()
