"""Generic knowledge-file loaders + link extraction.

Reads markdown from  <root>/<layer>/<domain>/<category>/<name>.md  (category omitted
for top-level files like game.md / combat.md). Generalized from games/sts1/cmd.py's
private loaders, with two fixes the originals lacked:
  - configurable root + layer + domain (cmd.py hard-coded a non-existent path),
  - link extraction handles the optional L:/D: qualifiers and the alias form
    [[cat/slug|Display]] and bare [[name]] top-level links, not just [[cat/Name]].
"""
import re
from pathlib import Path

_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
_QUALIFIER_RE = re.compile(r"^[LD]:[^/|]*$", re.IGNORECASE)


def name_to_filename(name: str) -> str:
    """'Shrug It Off+' -> 'shrug-it-off'; 'Charon's Ashes' -> 'charons-ashes'.

    Apostrophes are DROPPED (not hyphenated) to match the file-naming
    convention used everywhere else: the site resolver (site/build.py
    `_slugify`), the card generator (tools/regen/generate.py `slugify`), and
    the dominant relic file names (nilrys-codex, pandoras-box, charons-ashes).
    """
    name = name.rstrip("+").strip().lower()
    name = name.replace("'", "").replace(" ", "-")
    while "--" in name:
        name = name.replace("--", "-")
    return name.strip("-")


def ref_key(layer: str, domain: str, category, name: str) -> str:
    """Stable session-cache key. Bash / Bash+ / bash.md collapse to one stem."""
    return f"{layer}:{domain}:{category or ''}:{name_to_filename(name)}"


def extract_links(content: str):
    """Return [(category|None, name)] for each [[...]] link, alias + qualifiers stripped.

    Handles the linking grammar the site resolver uses: the id is the address, with
    OPTIONAL leading `L:`/`D:` qualifiers (layer/domain, order-free) and an optional
    `|Display` alias. The visible `category/` slash is preserved as the type.
      [[cards/bash|Bash]]        -> ('cards', 'bash')
      [[L:heuristics cards/bash]]-> ('cards', 'bash')   (qualifier dropped here)
      [[D:sts1 buffs/strength]]  -> ('buffs', 'strength')
      [[combat]]                 -> (None, 'combat')
    """
    out = []
    for inner in _LINK_RE.findall(content):
        target = inner.split("|", 1)[0].strip()  # drop |Display alias
        # drop any leading L:/D: qualifier tokens (whitespace-separated)
        tokens = [t for t in target.split() if not _QUALIFIER_RE.match(t)]
        target = " ".join(tokens).strip()
        if not target:
            continue
        if "/" in target:
            cat, name = target.split("/", 1)
            out.append((cat.strip(), name.strip()))
        else:
            out.append((None, target.strip()))
    return out


class KnowledgeLoader:
    def __init__(self, root, domain: str):
        self.root = Path(root)
        self.domain = domain

    def path(self, layer: str, category, name: str) -> Path:
        fn = name_to_filename(name) + ".md"
        base = self.root / layer / self.domain
        return (base / category / fn) if category else (base / fn)

    def load_file(self, layer: str, category, name: str):
        try:
            return self.path(layer, category, name).read_text(encoding="utf-8").strip()
        except (FileNotFoundError, NotADirectoryError):
            return None

    def load_top(self, layer: str, category, name: str):
        """Header + first non-empty line (compact form for deck-style listings)."""
        content = self.load_file(layer, category, name)
        if content is None:
            return None
        lines = [l for l in content.split("\n") if l.strip()]
        return "\n".join(lines[:2]) if lines else None
