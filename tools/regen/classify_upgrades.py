"""Classify every card's upgrade by what actually changes. Tight output."""
import json, re
from pathlib import Path
from collections import Counter

cards = json.loads((Path(__file__).parent / "data" / "sts1_cards.json").read_text(encoding="utf-8"))
FLAGS = ["exhaust", "innate", "ethereal", "retain"]


def norm(s):                      # numbers -> #, keep words
    return tuple(re.sub(r"[^a-z# ]", " ", re.sub(r"\d+", "#", (s or "").lower())).split())


def words(s):
    return set(re.sub(r"[^a-z ]", " ", (s or "").lower()).split())


buckets, differs = Counter(), []
for c in cards:
    up = c.get("upgrade") or {}
    base, upd = c.get("description", ""), up.get("description", "")
    has = {k: up.get(k) is not None for k in ("cost", "damage", "block", "magic_number")}
    if not any(has.values()) and norm(base) == norm(upd):
        buckets["no change at all"] += 1
        continue
    if norm(base) != norm(upd):
        bw, uw = words(base), words(upd)
        tags = [f"-{k}" for k in FLAGS if k in bw and k not in uw] + \
               [f"+{k}" for k in FLAGS if k in uw and k not in bw]
        if len(bw & uw) / max(1, len(bw)) < 0.45:
            tags.append("JUNK-DESC?")
        differs.append((c["name"], tags, base.replace("\n", " "), upd.replace("\n", " ")))
        buckets["TEXT-DIFFERS"] += 1
        continue
    stats = [k.replace("magic_number", "magic") for k in ("damage", "block", "magic_number") if has[k]]
    if has["cost"] and stats:
        buckets[f"cost + {'/'.join(stats)}"] += 1
    elif has["cost"]:
        buckets["cost only"] += 1
    else:
        buckets[f"stat: {'/'.join(stats)}"] += 1

print(f"=== UPGRADE KINDS  ({len(cards)} cards) ===")
for k, v in buckets.most_common():
    print(f"{v:4}  {k}")

print(f"\n=== TEXT-DIFFERS / need a rule ({len(differs)}) ===")
clear = [d for d in differs if d[1] and "JUNK-DESC?" not in d[1]]
ambig = [d for d in differs if not d[1] or "JUNK-DESC?" in d[1]]
print(f"-- flag-only changes ({len(clear)}): " + ", ".join(f"{n}{t}" for n, t, _, _ in sorted(clear)))
print(f"\n-- ambiguous / junk-desc ({len(ambig)}) [base => upgrade]:")
for n, t, b, u in sorted(ambig):
    print(f"  {n} {t}: {b[:55]!r} => {u[:55]!r}")
