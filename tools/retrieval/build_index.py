"""Build the survey index: one `<blurb>: <path>` line per entry.

Contextual blurbs are LIFTED (not generated) from each phenomenon's authored
`- **Applies when:**` field. The upgrade rule is one more line, with a placeholder
path (`upgraded cards ('<name>+'): phenomena/<domain>/cards/<name>-plus`) — the
selector emits any placeholder line once per matching state entity. No schema.

Run: `python -m tools.retrieval.build_index sts1`
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
APPLIES_RE = re.compile(r"^- \*\*Applies when:\*\*\s*(.+)$", re.MULTILINE)


def build_index(domain: str) -> str:
    """Return the index as markdown text: `<blurb>: <path>` per line.

    A line whose path holds a `<name>` placeholder is a rule (the selector emits it
    once per matching state entity). The upgrade rule is exactly that — one line, no
    schema. Contextual blurbs are lifted from each phenomenon's `Applies when:` field.
    """
    lines = [f"upgraded cards ('<name>+'): phenomena/{domain}/cards/<name>-plus"]
    idir = ROOT / "phenomena" / domain / "interactions"
    for f in sorted(idir.glob("*.md")):
        if f.stem == "index":
            continue
        m = APPLIES_RE.search(f.read_text(encoding="utf-8"))
        if not m:
            print(f"WARN: no 'Applies when:' blurb in {f.name}", file=sys.stderr)
            continue
        blurb = m.group(1).strip().rstrip(".")
        lines.append(f"{blurb}: phenomena/{domain}/interactions/{f.stem}")
    return "\n".join(lines) + "\n"


def index_path(domain: str) -> Path:
    return ROOT / "awareness" / domain / "survey-index.md"


def write_index(domain: str) -> Path:
    p = index_path(domain)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(build_index(domain), encoding="utf-8")
    return p


if __name__ == "__main__":
    domain = sys.argv[1] if len(sys.argv) > 1 else "sts1"
    p = write_index(domain)
    n = sum(1 for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip())
    print(f"wrote {p.relative_to(ROOT)} — {n} lines (1 upgrade rule + {n - 1} contextual)")
