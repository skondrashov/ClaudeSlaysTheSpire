"""Collapse redundant capitalization-only wiki-link aliases.

An alias [[TARGET|DISPLAY]] is REDUNDANT when slugify(name(TARGET)) ==
slugify(DISPLAY) — i.e. the alias exists only to fix display capitalization,
because the resolver slugifies the target anyway. Collapse to [[.../DISPLAY]].

An alias is GENUINE when the display differs from the id meaningfully
(e.g. [[encounters/Jaw Worm Solo|Jaw Worm]]) — keep it.

Dry-run by default; pass --apply to write.
"""
import re, sys, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIRS = ["ontology", "heuristics", "goals", "phenomena"]
LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
QUAL_RE = re.compile(r'^(layer|domain|category)\s*:\s*(.+)$', re.I)
LINK_LAYERS = {"ontology", "heuristics", "goals", "phenomena"}


def slugify(name):
    slug = name.strip().lower().replace(" ", "-").replace("'", "").replace(".", "")
    return re.sub(r'[^a-z0-9-]', '', slug)


def parse_target(target):
    """Return (qualifier_tokens, category, name, has_qual). Mirrors resolver."""
    quals, addr = [], None
    for tok in target.split(","):
        t = tok.strip()
        if not t:
            continue
        if QUAL_RE.match(t):
            quals.append(t)
        elif addr is None:
            addr = t
    has_qual = bool(quals)
    if addr is None:
        return quals, None, None, has_qual
    # leading layer keyword acts as layer
    if "/" in addr:
        first, rest = addr.split("/", 1)
        if first in LINK_LAYERS:
            quals = quals + [f"layer:{first}"]
            addr = rest
    if "/" in addr:
        category, _s, name = (p.strip() for p in addr.partition("/"))
        category = category or None
    else:
        category, name = None, addr.strip()
    return quals, category, name, has_qual


def main():
    apply = "--apply" in sys.argv
    redundant = genuine = 0
    redundant_samples, genuine_samples = [], []
    files_changed = 0

    for d in DIRS:
        for f in (ROOT / d).rglob("*.md"):
            text = f.read_text(encoding="utf-8")
            changed = False

            def repl(m):
                nonlocal redundant, genuine, changed
                full = html.unescape(m.group(1))
                if "|" not in full:
                    return m.group(0)
                target, _sep, display = full.partition("|")
                target, display = target.strip(), display.strip()
                quals, category, name, has_qual = parse_target(target)
                if name is None:
                    return m.group(0)
                if slugify(name) == slugify(display):
                    redundant += 1
                    # Reconstruct without alias, name -> display.
                    if category:
                        new_addr = f"{category}/{display}"
                    elif has_qual:
                        new_addr = display
                    else:
                        # bare, no category, no qualifier: dropping alias would
                        # make it inline-code (not a link). Leave untouched.
                        if len(redundant_samples) < 12:
                            redundant_samples.append(("SKIP-bare", full))
                        redundant -= 1
                        return m.group(0)
                    parts = quals + [new_addr]
                    new_full = ", ".join(parts)
                    changed = True
                    if len(redundant_samples) < 12:
                        redundant_samples.append((f"{d}", f"[[{full}]] -> [[{new_full}]]"))
                    return f"[[{new_full}]]"
                else:
                    genuine += 1
                    if len(genuine_samples) < 15:
                        genuine_samples.append((f"{d}", f"[[{full}]]"))
                    return m.group(0)

            new_text = LINK_RE.sub(repl, text)
            if changed:
                files_changed += 1
                if apply:
                    f.write_text(new_text, encoding="utf-8")

    print(f"{'APPLIED' if apply else 'DRY-RUN'}")
    print(f"Redundant (collapsed): {redundant}")
    print(f"Genuine (kept):        {genuine}")
    print(f"Files changed:         {files_changed}")
    print("\n--- redundant samples ---")
    for d, s in redundant_samples:
        print(f"  [{d}] {s}")
    print("\n--- genuine samples (kept) ---")
    for d, s in genuine_samples:
        print(f"  [{d}] {s}")


if __name__ == "__main__":
    main()
