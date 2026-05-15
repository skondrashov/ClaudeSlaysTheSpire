#!/usr/bin/env python3
"""Regenerate data/run_stats.json from analyst/runs/ files.

This is the single source of truth for all run statistics. Run after every
analyst completion. stream.py reads the output; it never writes counters.

Run files are JSON: analyst/runs/run_NNN.json with fields:
  run, character, ascension, victory, floor, deck, relics, cause_of_death, etc.
"""

import json
import os
import sys
import tempfile
from glob import glob

RUNS_DIR = "analyst/runs"
STATS_FILE = "data/run_stats.json"

# Baseline: runs that predate individual tracking. Extracted from summary files.
# These are all deaths (no wins before run 147).
SUMMARY_COUNTS = {
    "runs_000-045_summary.md": 37,  # "37 runs total"
    "runs_048-078_summary.md": 31,  # "31 runs"
    "runs_081-100_summary.md": 10,  # "10 logged deaths"
    "runs_101-110_summary.md": 4,   # "4 logged deaths"
    "runs_111-123_gap.md": 6,       # 6 known death floors mentioned
}


def load_run_file(path: str) -> dict | None:
    """Load a run_NNN.json file."""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        # Minimal validation
        if "run" not in data or "floor" not in data or "victory" not in data:
            print(f"  WARNING: Missing required fields in {path}", file=sys.stderr)
            return None
        # Normalize character field to class for stats output
        data.setdefault("class", data.get("character", "UNKNOWN"))
        return data
    except (json.JSONDecodeError, OSError) as e:
        print(f"  WARNING: Could not read {path}: {e}", file=sys.stderr)
        return None


def compute_baseline() -> int:
    """Count runs from archived summary files."""
    total = 0
    for filename, count in SUMMARY_COUNTS.items():
        path = os.path.join(RUNS_DIR, filename)
        if os.path.exists(path):
            total += count
        else:
            print(f"  WARNING: Missing summary file {path}, adding {count} anyway", file=sys.stderr)
            total += count
    return total


def main():
    # Parse all individual run files
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

    # Compute baseline from summaries (pre-tracking runs, all deaths)
    baseline_runs = compute_baseline()

    # Build stats
    individual_runs = len(entries)
    total_runs = baseline_runs + individual_runs
    wins = sum(1 for e in entries if e["victory"])
    deaths = total_runs - wins  # baseline runs are all deaths
    best_floor = max((e["floor"] for e in entries), default=0)
    best_ascension = max((e.get("ascension", 0) for e in entries), default=0)

    # Character stats from individual entries only
    char_stats = {}
    for e in entries:
        cls = e.get("class", e.get("character", "UNKNOWN"))
        if cls not in char_stats:
            char_stats[cls] = {"wins": 0, "best_floor": 0, "runs_tracked": 0}
        char_stats[cls]["runs_tracked"] += 1
        if e["victory"]:
            char_stats[cls]["wins"] += 1
        char_stats[cls]["best_floor"] = max(char_stats[cls]["best_floor"], e["floor"])

    # floor_history for the overlay graph (slim entries only)
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

    # Preserve live game state from existing stats file if present
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
        "baseline_runs": baseline_runs,
        "tracked_runs": individual_runs,
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

    # Report
    print(f"total_runs: {total_runs} ({baseline_runs} baseline + {individual_runs} tracked)")
    print(f"wins: {wins}, deaths: {deaths}")
    print(f"best_floor: {best_floor}")
    for cls, cs in sorted(char_stats.items()):
        print(f"  {cls}: {cs['runs_tracked']} runs, {cs['wins']} wins, best F{cs['best_floor']}")
    if parse_errors:
        print(f"\n{parse_errors} files could not be parsed!", file=sys.stderr)

    if "--json" in sys.argv:
        print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
