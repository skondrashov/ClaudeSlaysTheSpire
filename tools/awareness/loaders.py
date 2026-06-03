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
_QUAL_RE = re.compile(r"^(layer|domain|category)\s*:\s*(.+)$", re.IGNORECASE)
_LINK_LAYERS = {"ontology", "phenomena", "heuristics", "goals"}


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


def parse_link(inner: str):
    """Parse one [[...]] body to (layer, category, name), mirroring the site
    resolver in site/build.py. Grammar: comma-separated, spelled-out and order-free
    `layer:` / `domain:` / `category:` qualifiers; an optional `|Display` alias; a
    leading layer keyword in the address (`goals/next`); `category/id` or flat `id`.
    `layer` is None when unspecified (the caller applies its default). `domain:` is
    parsed-but-ignored here (loaders are bound to a single domain).

      [[cards/bash|Bash]]                 -> (None, 'cards', 'bash')
      [[layer:heuristics, cards/bash]]    -> ('heuristics', 'cards', 'bash')
      [[layer:goals, next]]               -> ('goals', None, 'next')
      [[goals/next]]                      -> ('goals', None, 'next')
      [[combat]]                          -> (None, None, 'combat')
    """
    full = inner.split("|", 1)[0]  # drop |Display alias
    layer = cat_q = addr = None
    for tok in full.split(","):
        tok = tok.strip()
        if not tok:
            continue
        m = _QUAL_RE.match(tok)
        if m:
            key, val = m.group(1).lower(), m.group(2).strip()
            if key == "layer":
                layer = val
            elif key == "category":
                cat_q = val
            # domain: captured-but-ignored (single-domain loaders)
        elif addr is None:
            addr = tok
    if addr is None:
        return (layer, cat_q, None)
    if "/" in addr:                      # leading layer keyword acts as the layer
        first, rest = addr.split("/", 1)
        if first in _LINK_LAYERS and layer is None:
            layer, addr = first, rest
    if "/" in addr:
        category, name = addr.split("/", 1)
        category = category.strip() or None
        name = name.strip()
    else:
        category, name = None, addr.strip()
    if cat_q:
        category = cat_q
    return (layer, category, name)


def extract_links(content: str):
    """Return [(layer, category, name)] for each [[...]] link. `layer` is None when
    the link does not specify one — the caller applies its default."""
    out = []
    for inner in _LINK_RE.findall(content):
        layer, cat, name = parse_link(inner)
        if name:
            out.append((layer, cat, name))
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
