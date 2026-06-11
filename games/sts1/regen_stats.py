#!/usr/bin/env python3
"""Regenerate data/run_stats.json from analyst/runs/run_*.json files.

This is the single source of truth for all run statistics. stream.py and the
overlay read the output; nothing else writes counters.

Each run is one JSON file: analyst/runs/run_NNN.json with at minimum:
  run, character, ascension, victory, floor
"""

import json
import os
import sys
import tempfile
from glob import glob

_BASE = os.path.dirname(os.path.abspath(__file__))
RUNS_DIR = os.path.join(_BASE, "analyst", "runs")
STATS_FILE = os.path.join(_BASE, "data", "run_stats.json")


def load_run_file(path: str) -> dict | None:
    """Load a run_NNN.json file."""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if "run" not in data or "floor" not in data or "victory" not in data:
            print(f"  WARNING: Missing required fields in {path}", file=sys.stderr)
            return None
        data.setdefault("class", data.get("character", "UNKNOWN"))
        return data
    except (json.JSONDecodeError, OSError) as e:
        print(f"  WARNING: Could not read {path}: {e}", file=sys.stderr)
        return None


def main():
    run_files = sorted(glob(os.path.join(RUNS_DIR, "run_*.json")))
    entries = []
    parse_errors = 0

    for path in run_files:
        entry = load_run_file(path)
        if entry:
            entries.append(entry)
        else:
            parse_errors += 1

    entries.sort(key=lambda e: e["run"])

    total_runs = len(entries)
    wins = sum(1 for e in entries if e["victory"])
    deaths = total_runs - wins
    best_floor = max((e["floor"] for e in entries), default=0)
    best_ascension = max((e.get("ascension", 0) for e in entries), default=0)

    def _best_key(e):
        # "Best" is ordered by ascension first: a deep A9 attempt outranks an A5
        # win. Within an ascension, a win outranks any floor.
        return (e.get("ascension", 0), 1 if e["victory"] else 0, e["floor"])

    char_stats = {}
    for e in entries:
        cls = e.get("class", e.get("character", "UNKNOWN"))
        if cls not in char_stats:
            char_stats[cls] = {"wins": 0, "best_floor": 0, "runs": 0,
                               "best": None, "best_won_ascension": None}
        cs = char_stats[cls]
        cs["runs"] += 1
        if e["victory"]:
            cs["wins"] += 1
            won_a = e.get("ascension", 0)
            if cs["best_won_ascension"] is None or won_a > cs["best_won_ascension"]:
                cs["best_won_ascension"] = won_a
        cs["best_floor"] = max(cs["best_floor"], e["floor"])
        if cs["best"] is None or _best_key(e) > (cs["best"]["ascension"],
                                                 1 if cs["best"]["victory"] else 0,
                                                 cs["best"]["floor"]):
            cs["best"] = {"ascension": e.get("ascension", 0),
                          "victory": e["victory"], "floor": e["floor"]}

    floor_history = [
        {
            "run": e["run"],
            "floor": e["floor"],
            "victory": e["victory"],
            "class": e.get("class", e.get("character", "UNKNOWN")),
            "ascension": e.get("ascension", 0),
        }
        for e in entries
    ]

    # Preserve live game state from existing stats file
    live_state = {"current_floor": 0, "current_hp": 0, "max_hp": 0, "current_class": "?"}
    try:
        with open(STATS_FILE) as f:
            existing = json.load(f)
        for key in live_state:
            if key in existing:
                live_state[key] = existing[key]
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    stats = {
        "total_runs": total_runs,
        "wins": wins,
        "deaths": deaths,
        "best_floor": best_floor,
        "best_ascension": best_ascension,
        **live_state,
        "floor_history": floor_history,
        "character_stats": char_stats,
    }

    # Atomic write
    os.makedirs(os.path.dirname(STATS_FILE), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(STATS_FILE), suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(stats, f)
        os.replace(tmp, STATS_FILE)
    except:
        os.unlink(tmp)
        raise

    print(f"total_runs: {total_runs}, wins: {wins}, deaths: {deaths}, best_floor: {best_floor}")
    for cls, cs in sorted(char_stats.items()):
        print(f"  {cls}: {cs['runs']} runs, {cs['wins']} wins, best F{cs['best_floor']}")
    if parse_errors:
        print(f"\n{parse_errors} files could not be parsed!", file=sys.stderr)


if __name__ == "__main__":
    main()
