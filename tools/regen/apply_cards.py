"""The ONLY writer for regenerated cards.

Writes generated NOUMENA -> ontology/sts1/cards/<slug>.md and PHENOMENA ->
phenomena/sts1/cards/<slug>-plus.md, with three safety properties:

  1. PRESERVE — curated provenance the dataset lacks is spliced back in:
       Strike/Defend keep Character: All (shared starters, not per-color);
       Apparition/Bite keep their Rarity line (carries event provenance).
  2. DATA-LOSS GUARD — a current entry carrying prose beyond the recognized
     fields (hand-written facts) is SKIPPED, not clobbered, unless --force.
  3. NO DELETES — only dataset cards are touched; current-only entries
     (token cards: shiv/smite/miracle/beta/omega/…) are left alone.

  python tools/regen/apply_cards.py                 # dry-run (default): plan only
  python tools/regen/apply_cards.py --apply         # write
  python tools/regen/apply_cards.py --apply --only Bash
  python tools/regen/apply_cards.py --apply --force # write even entries with extra prose
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import generate as G

ONT_CARDS = G.CARDS_DIR
PHEN_CARDS = G.ROOT / "phenomena" / "sts1" / "cards"
DATA = G.DATA

PRESERVE_CHAR = {"Strike", "Defend"}        # shared starters -> Character: All
PRESERVE_RARITY = {"Apparition", "Bite"}    # rarity line carries event provenance

FIELD_RE = re.compile(r"^\s*-\s*\*\*(.+?):\*\*\s*(.+?)\s*$")


def current_fields(path):
    """(fields, extra_lines). fields: name->(raw_line, value). extra_lines: any
    content line that isn't the title, blank, or a recognized field — i.e. prose
    the generator would drop."""
    fields, extra = {}, []
    if not path.exists():
        return fields, extra
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("# "):
            continue
        m = FIELD_RE.match(line)
        if m:
            fields[m.group(1).strip().lower()] = (line.rstrip(), m.group(2).strip())
        else:
            extra.append(line.rstrip())
    return fields, extra


def merge_noumenon(card, gen_text, cur_fields):
    """Splice PRESERVE overrides into the generated noumenon."""
    name = card["name"]
    out = []
    for line in gen_text.split("\n"):
        m = FIELD_RE.match(line)
        if m:
            field = m.group(1).strip().lower()
            if name in PRESERVE_CHAR and field == "character":
                out.append("- **Character:** All"); continue
            if name in PRESERVE_RARITY and field == "rarity" and "rarity" in cur_fields:
                out.append(cur_fields["rarity"][0]); continue
        out.append(line)
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="actually write (default: dry-run)")
    ap.add_argument("--only", help="restrict to one card name")
    ap.add_argument("--force", action="store_true", help="overwrite entries with extra prose too")
    args = ap.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    cards = json.loads(DATA.read_text(encoding="utf-8"))
    link_map = G.build_link_map()
    if args.only:
        cards = [c for c in cards if c["name"].lower() == args.only.lower()]
        if not cards:
            ap.error(f"no dataset card named {args.only!r}")

    if args.apply:
        ONT_CARDS.mkdir(parents=True, exist_ok=True)
        PHEN_CARDS.mkdir(parents=True, exist_ok=True)

    noum_new, noum_upd, phen_w, skipped, preserved, meta_changes = [], [], [], [], [], []

    for card in cards:
        name = card["name"]
        slug = G.slugify(name)
        ont_path = ONT_CARDS / f"{slug}.md"
        cur_fields, extra = current_fields(ont_path)

        # data-loss guard
        if extra and not args.force:
            skipped.append((name, len(extra)))
            continue

        gen = G.render(card, link_map)
        merged = merge_noumenon(card, gen, cur_fields)
        if name in PRESERVE_CHAR or name in PRESERVE_RARITY:
            preserved.append(name)

        # record metadata changes for the audit trail
        new_fields, _ = {}, None
        for line in merged.split("\n"):
            m = FIELD_RE.match(line)
            if m:
                new_fields[m.group(1).strip().lower()] = m.group(2).strip()
        for f in ("cost", "character", "rarity"):  # type changes are link-format only
            cv = cur_fields.get(f, (None, None))[1]
            nv = new_fields.get(f)
            if cv is not None and nv is not None and cv != nv:
                meta_changes.append((name, f, cv, nv))

        if not ont_path.exists():
            noum_new.append(name)
        elif merged.strip() != ont_path.read_text(encoding="utf-8").strip():
            noum_upd.append(name)
        if args.apply:
            ont_path.write_text(merged, encoding="utf-8")

        if G.has_upgrade(card):
            phen_path = PHEN_CARDS / f"{slug}-plus.md"
            phen_w.append(name)
            if args.apply:
                phen_path.write_text(G.render_phenomenon(card, link_map), encoding="utf-8")

    mode = "APPLIED" if args.apply else "DRY-RUN (no writes)"
    print(f"=== apply_cards — {mode} ===")
    print(f"noumena: {len(noum_new)} new, {len(noum_upd)} updated, {len(skipped)} skipped (extra prose)")
    print(f"phenomena: {len(phen_w)} written")
    print(f"preserved provenance: {len(preserved)} ({', '.join(sorted(set(preserved)))})")
    if skipped:
        print("\nSKIPPED (hand-written prose — rerun with --force to include):")
        for nm, n in sorted(skipped):
            print(f"  - {nm} ({n} extra line(s))")
    if meta_changes:
        print(f"\nMETADATA CHANGES ({len(meta_changes)}) — current -> generated (dataset):")
        for nm, f, cv, nv in sorted(meta_changes):
            print(f"  - {nm}: {f} {cv!r} -> {nv!r}")
    if noum_new:
        print(f"\nNEW coverage ({len(noum_new)}): {', '.join(sorted(noum_new))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
