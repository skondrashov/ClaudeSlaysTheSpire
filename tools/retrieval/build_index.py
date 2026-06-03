"""Build the survey index: {blurb, target} entries the reranker searches.

Two kinds of entry (see ontology/praxis/retrieval.md):
  1. ONE rule entry for resolvable upgrade phenomena (target is a pattern).
  2. One entry per contextual interaction, blurb LIFTED (not generated) from the
     file's authored `- **Applies when:**` field.

This is the *programmatic extraction* half of the design — it never authors a blurb,
it only pulls already-authored ones. Run: `python -m tools.retrieval.build_index sts1`.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
APPLIES_RE = re.compile(r"^- \*\*Applies when:\*\*\s*(.+)$", re.MULTILINE)


def build_index(domain: str) -> dict:
    entries = []

    # 1. resolvable upgrades: a single rule entry, target is a pattern not a path.
    entries.append({
        "id": "rule:upgrades",
        "blurb": "For any upgraded ('+') card present in the state, its resolved "
                 "upgrade form applies.",
        "target": {"kind": "pattern", "value": f"phenomena/{domain}/cards/<slug>-plus"},
    })

    # 2. contextual interactions: one entry each, blurb lifted from the file.
    idir = ROOT / "phenomena" / domain / "interactions"
    for f in sorted(idir.glob("*.md")):
        if f.stem == "index":
            continue
        text = f.read_text(encoding="utf-8")
        m = APPLIES_RE.search(text)
        if not m:
            print(f"WARN: no 'Applies when:' blurb in {f.name}", file=sys.stderr)
            continue
        entries.append({
            "id": f.stem,
            "blurb": m.group(1).strip(),
            "target": {"kind": "path", "value": f"phenomena/{domain}/interactions/{f.stem}"},
        })

    return {"domain": domain, "entries": entries}


def index_path(domain: str) -> Path:
    return ROOT / "awareness" / domain / "survey-index.json"


def write_index(domain: str) -> Path:
    idx = build_index(domain)
    p = index_path(domain)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(idx, indent=2) + "\n", encoding="utf-8")
    return p


if __name__ == "__main__":
    domain = sys.argv[1] if len(sys.argv) > 1 else "sts1"
    p = write_index(domain)
    idx = json.loads(p.read_text(encoding="utf-8"))
    n_rule = sum(1 for e in idx["entries"] if e["id"].startswith("rule:"))
    print(f"wrote {p.relative_to(ROOT)} — {len(idx['entries'])} entries "
          f"({n_rule} rule, {len(idx['entries']) - n_rule} contextual)")
