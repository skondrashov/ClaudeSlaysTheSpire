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

RUNS_DIR = "analyst/runs"
STATS_FILE = "data/run_stats.json"


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

    char_stats = {}
    for e in entries:
        cls = e.get("class", e.get("character", "UNKNOWN"))
        if cls not in char_stats:
            char_stats[cls] = {"wins": 0, "best_floor": 0, "runs": 0}
        char_stats[cls]["runs"] += 1
        if e["victory"]:
            char_stats[cls]["wins"] += 1
        char_stats[cls]["best_floor"] = max(char_stats[cls]["best_floor"], e["floor"])

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
