#!/usr/bin/env python3
"""One-time migration: split analyst/run_log.md into individual files in analyst/runs/."""

import re
import os

SRC = "analyst/run_log.md"
DST = "analyst/runs"

os.makedirs(DST, exist_ok=True)

content = open(SRC, encoding="utf-8").read()
lines = content.split("\n")

# Find all section boundaries (## headers)
sections = []
current_start = None
current_header = None

for i, line in enumerate(lines):
    if line.startswith("## "):
        if current_start is not None:
            sections.append((current_header, current_start, i))
        current_header = line
        current_start = i
if current_start is not None:
    sections.append((current_header, current_start, len(lines)))

print(f"Found {len(sections)} sections")

summary_map = {
    "Runs 0-45": "runs_000-045_summary.md",
    "Runs 48-78": "runs_048-078_summary.md",
    "Runs 81-100": "runs_081-100_summary.md",
    "Runs 101-110": "runs_101-110_summary.md",
    "Runs 111-123": "runs_111-123_gap.md",
}

for header, start, end in sections:
    body = "\n".join(lines[start:end]).rstrip() + "\n"

    # Check if it's a summary section
    matched_summary = False
    for key, filename in summary_map.items():
        if key in header:
            path = os.path.join(DST, filename)
            with open(path, "w", encoding="utf-8") as f:
                f.write(body)
            print(f"  Summary: {filename} ({end - start} lines)")
            matched_summary = True
            break

    if matched_summary:
        continue

    # Individual run entry
    m = re.match(r"## Run (\d+)", header)
    if m:
        run_num = int(m.group(1))
        filename = f"run_{run_num:03d}.md"
        path = os.path.join(DST, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(body)
        print(f"  Run {run_num}: {filename} ({end - start} lines)")
    else:
        print(f"  UNKNOWN section: {header[:60]}")

print(f"\nDone. Files written to {DST}/")
