"""CLI:  python -m tools.awareness --goal win [--json] [--domain sts1]
        python -m tools.awareness --reset [--reason compaction]
"""
import argparse
import json
import sys

from .awareness import AwarenessConfig, load_goal, reset, ROOT


def main(argv=None):
    try:  # Windows consoles default to cp1252; knowledge text has → etc.
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    ap = argparse.ArgumentParser(prog="tools.awareness")
    ap.add_argument("--goal")
    ap.add_argument("--tier", default="goal")
    ap.add_argument("--domain", default="sts1")
    ap.add_argument("--session")
    ap.add_argument("--json", action="store_true", help="print the structured Result (minus text), then the text")
    ap.add_argument("--reset", action="store_true")
    ap.add_argument("--reason")
    args = ap.parse_args(argv)

    cfg = AwarenessConfig(domain=args.domain)

    if args.reset:
        print(json.dumps(reset(session=args.session, reason=args.reason, config=cfg)))
        return 0

    if not args.goal:
        ap.error("--goal is required (or use --reset)")

    res = load_goal(args.goal, tier=args.tier, session=args.session, config=cfg)
    if args.json:
        meta = {k: v for k, v in res.items() if k != "text"}
        print(json.dumps(meta, indent=2))
        print("\n--- TEXT ---\n")
    print(res["text"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
