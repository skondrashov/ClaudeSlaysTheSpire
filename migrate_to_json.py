#!/usr/bin/env python3
"""One-time migration: convert analyst/runs/run_*.md to run_*.json."""

import json
import os
import re
import sys
from glob import glob

RUNS_DIR = "analyst/runs"

HEADER_RE = re.compile(
    r"^## Run (\d+)\s*[—–-]+\s*"
    r"(.*?)\s+A(\d+),\s*"
    r"(Victory|VICTORY|Defeat|Death|Quick Death)"
    r"(?:\s+Floor\s+(\d+))?"
    r"(.*)$",
    re.IGNORECASE
)

def parse_character(raw: str) -> str:
    raw = raw.strip().lower()
    if "silent" in raw: return "THE_SILENT"
    if "ironclad" in raw: return "IRONCLAD"
    if "defect" in raw: return "DEFECT"
    if "watcher" in raw: return "WATCHER"
    return raw.upper()

def parse_field(lines, prefix):
    """Extract a field like 'DECK: ...' or 'CAUSE OF DEATH: ...' from lines."""
    for line in lines:
        if line.startswith(prefix):
            return line[len(prefix):].strip()
    return ""

def parse_numbered_list(lines, prefix):
    """Extract a numbered list following a prefix like 'KEY MOMENTS:'."""
    items = []
    found = False
    for line in lines:
        if line.startswith(prefix):
            # Content might be on the same line after the prefix
            rest = line[len(prefix):].strip()
            if rest:
                # Inline format: (1) ... (2) ... or 1. ... 2. ...
                # Try to split on numbered patterns
                parts = re.split(r'\(\d+\)\s*', rest)
                parts = [p.strip() for p in parts if p.strip()]
                if parts:
                    items.extend(parts)
                    continue
            found = True
            continue
        if found:
            m = re.match(r'^\d+[\.\)]\s*(.*)', line)
            if m:
                items.append(m.group(1).strip())
            elif line.strip() and not line.startswith(('DECK:', 'RELICS:', 'CAUSE', 'VICTORY:', 'KEY', 'LESSONS:')):
                # Continuation of previous item or inline format
                pass
            else:
                break
    return items

def migrate_file(md_path):
    with open(md_path, encoding="utf-8") as f:
        content = f.read()

    lines = [l.strip() for l in content.strip().split('\n')]
    if not lines:
        return None

    m = HEADER_RE.match(lines[0])
    if not m:
        print(f"  SKIP (can't parse header): {md_path}")
        return None

    run_num = int(m.group(1))
    character = parse_character(m.group(2))
    ascension = int(m.group(3))
    outcome = m.group(4).lower()
    floor = int(m.group(5)) if m.group(5) else 0
    victory = outcome == "victory"
    annotation = m.group(6).strip().strip('()')

    deck = parse_field(lines, "DECK:")
    relics = parse_field(lines, "RELICS:")
    cause_of_death = parse_field(lines, "CAUSE OF DEATH:") if not victory else ""
    victory_info = parse_field(lines, "VICTORY:") if victory else ""
    key_moments = parse_numbered_list(lines, "KEY MOMENTS:")
    lessons = parse_numbered_list(lines, "LESSONS:")

    run_data = {
        "run": run_num,
        "character": character,
        "ascension": ascension,
        "victory": victory,
        "floor": floor,
        "deck": deck,
        "relics": relics,
    }
    if victory:
        run_data["victory_info"] = victory_info
    else:
        run_data["cause_of_death"] = cause_of_death
    if annotation:
        run_data["annotation"] = annotation
    if key_moments:
        run_data["key_moments"] = key_moments
    if lessons:
        run_data["lessons"] = lessons

    return run_data

def main():
    md_files = sorted(glob(os.path.join(RUNS_DIR, "run_*.md")))
    print(f"Found {len(md_files)} .md run files")

    converted = 0
    skipped = 0
    for md_path in md_files:
        data = migrate_file(md_path)
        if data is None:
            skipped += 1
            continue

        json_path = md_path.replace(".md", ".json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        # Remove old .md file
        os.remove(md_path)
        converted += 1
        print(f"  {os.path.basename(md_path)} -> {os.path.basename(json_path)} (Run {data['run']}, {data['character']}, {'W' if data['victory'] else 'D'} F{data['floor']})")

    print(f"\nConverted: {converted}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
