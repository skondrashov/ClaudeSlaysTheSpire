"""Build the survey index: a condensed map from any game entity to its ontology entry.

Not a list of every entity → path (that would be ~800 lines). Instead a *rule* plus
the handful of exceptions:

  1. A slug rule that resolves the vast majority of names by convention.
  2. The category search order.
  3. The upgrade rule ("<name>+" → the resolved upgraded card).
  4. An alias table — only the entries whose in-game name does NOT slug to its file
     (auto-detected: title-slug ≠ filename), plus a few generic display names.

Run: `python -m tools.retrieval.build_index sts1`
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

# Categories a bare name is searched against, in priority order. `upgrades` is
# excluded — it is reached via the upgrade rule or an explicit `upgrades/<name>`
# address, never by bare-name search (every upgrade shares a card's name).
SEARCH_CATEGORIES = ["cards", "enemies", "bosses", "relics", "potions", "events",
                     "buffs", "debuffs", "encounters", "rules", "types",
                     "characters", "acts", "ascension", "shop"]

# NO hand-maintained alias dict: every alias in the map is auto-detected
# (title-slug != filename), so regenerating keeps it true. Display-name ambiguity
# (the game showing "Louse"/"Slaver" for two different variants) is a PERCEPTION
# problem — the state formatter disambiguates via monster id
# (games/sts1/bot/state_formatter.py) so knowledge never sees an ambiguous name.


def slug(s: str) -> str:
    """Robust slug, matching tools/regen: lowercase, drop ' and ., runs of other
    non-alphanumerics → '-'. So 'Spike Slime (M)' → 'spike-slime-m'."""
    s = s.lower().replace("'", "").replace(".", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def _title(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"#\s+(.+)", line.strip())
        if m:
            return m.group(1).strip()
    return None


def build_index(domain: str) -> str:
    ont = ROOT / "ontology" / domain
    lines = [
        f"# {domain} ontology map — resolve any game entity to its entry.",
        "#",
        "# slug(name): lowercase, drop ' and ., other non-alphanumeric runs -> '-'.",
        "#   e.g. \"Spike Slime (M)\" -> spike-slime-m, \"Gremlin Nob\" -> gremlin-nob.",
        "# A bare name resolves to <category>/slug(name), searching these categories in",
        "# order; a miss retries with a leading \"the-\" added or removed (\"Champ\" ->",
        "# the-champ); a name in several categories returns every match:",
        f"#   {' '.join(SEARCH_CATEGORIES)}",
        "# Upgraded card: \"<name>+\" -> phenomena/" + domain + "/cards/slug(name)-plus.",
        "# The names below override the slug rule (in-game name doesn't slug to the file).",
        "",
    ]

    # Auto-detected aliases: title doesn't slug to its filename. Skip `upgrades`
    # (systematic "Upgrade: " prefix) and `ascension` (systematic aN — its own rule).
    aliases = []
    for cat in SEARCH_CATEGORIES:
        if cat == "ascension":      # covered by the "Ascension N: ascension/aN" rule
            continue
        d = ont / cat
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            if f.stem == "index":
                continue
            title = _title(f)
            if title and slug(title) != f.stem:
                aliases.append(f"{title}: {cat}/{f.stem}")

    lines.append("## aliases (in-game name -> entry)")
    lines.append("Ascension N: ascension/aN   (e.g. \"Ascension 15\" -> ascension/a15)")
    lines.extend(sorted(aliases))
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
    print(p.read_text(encoding="utf-8"))
