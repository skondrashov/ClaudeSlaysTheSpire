"""
Build static site from ontology and heuristics markdown files.
Generates HTML pages + a changelog with diffs from git history.

Usage: python site/build.py
Output: site/out/
"""

import os, re, subprocess, html, shutil, json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
OUT = ROOT / "site" / "out"

# ── Wiki-link resolution ────────────────────────────────────────────

_wiki_link_node = "sts1"      # Set before rendering each page
_wiki_link_source = None      # "section/node[/category]/stem" of the page being rendered
_valid_pages = set()          # every entry/top-level page filename that build() will emit
_broken_links = []            # (source, "category/Name", href) for links with no target page

# Knowledge layers that are link-addressable (md entries). Substrate layers
# (awareness = memory/JSON, tools/interface = body/code) are NOT here — you
# call them, you don't [[link]] them.
LINK_LAYERS = {"ontology", "phenomena", "heuristics", "goals"}


def _slugify(name):
    slug = name.strip().lower().replace(" ", "-").replace("'", "").replace(".", "")
    return re.sub(r'[^a-z0-9-]', '', slug)


def resolve_wiki_link(match):
    """Resolve a [[...]] wiki-link to an HTML <a>.

    Grammar — comma-separated, optional `|Display` alias:
        [[ (layer:<layer>,)? (domain:<domain>,)? <category>/<id> ]]  categorized
        [[ (layer:<layer>,)? (domain:<domain>,)? <id> ]]            flat (goals)

    The id is the address; `category` annotates it (and tells the reader the
    target's type without a lookup). Qualifiers are spelled out in full,
    lowercase — `layer:`, `domain:`, and the rare `category:` — all optional and
    defaulting to the CURRENT page's layer/domain; layer further defaults to
    `ontology` (ontology-canonical). A leading layer keyword in the address
    (e.g. `goals/next`) is still read as the layer (tolerant fallback).
    `[[category/]]` (empty id) points at the category index page.

    A bare `[[word]]` with no '/' and no qualifier stays inline code, not a link
    (unchanged behaviour — needs the resolver index to be safe, future work).

    When _valid_pages is populated (during build()), a link whose target page
    does not exist is recorded in _broken_links and marked with a CSS class.
    """
    # inline() HTML-escapes before link resolution, so undo it here (e.g. an
    # apostrophe arrives as &#x27; and would otherwise corrupt the slug); the
    # display text is re-escaped on output.
    full = html.unescape(match.group(1))
    # Optional Obsidian-style alias: [[target|Display]] (split before commas).
    target, _sep, label = full.partition("|")
    target = target.strip()

    layer = domain = cat_q = addr = None
    for tok in target.split(","):
        tok = tok.strip()
        if not tok:
            continue
        m = re.match(r'^(layer|domain|category)\s*:\s*(.+)$', tok, re.I)
        if m:
            key, val = m.group(1).lower(), m.group(2).strip()
            if key == "layer":
                layer = val
            elif key == "domain":
                domain = val
            else:
                cat_q = val
        elif addr is None:
            addr = tok

    has_qual = layer is not None or domain is not None or cat_q is not None

    # No address, or a bare unqualified word: not a link (unchanged behaviour).
    if addr is None or ("/" not in addr and not has_qual):
        return f'<code>{html.escape(full)}</code>'

    # A leading layer keyword in the address acts as the layer (tolerant fallback).
    if "/" in addr:
        first, rest = addr.split("/", 1)
        if first in LINK_LAYERS and layer is None:
            layer, addr = first, rest

    # Remaining address → category / id (empty id = category index page).
    if "/" in addr:
        category, _s, name = (p.strip() for p in (addr.partition("/")))
        category = category or None
    else:
        category, name = None, addr.strip()

    if cat_q:                      # explicit `category:` qualifier wins
        category = cat_q

    layer = layer or "ontology"
    domain = domain or _wiki_link_node

    if name:
        href = make_slug(layer, domain, category, _slugify(name)) if category \
            else make_slug(layer, domain, _slugify(name))
        display = label or name
    else:
        href = make_slug(layer, domain, category)
        display = label or category or addr

    cls = "wiki-link"
    if _valid_pages and href not in _valid_pages:
        _broken_links.append((_wiki_link_source, target, href))
        cls = "wiki-link wiki-link-broken"
    return f'<a href="{href}" class="{cls}">{html.escape(display)}</a>'


# ── Minimal markdown → HTML ──────────────────────────────────────────

def md_to_html(text):
    """Dead-simple markdown to HTML. No dependencies."""
    lines = text.split("\n")
    out = []
    in_code = False
    in_list = False
    in_table = False
    pending_table_header = None

    for line in lines:
        # Code blocks
        if line.strip().startswith("```"):
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                lang = line.strip()[3:]
                out.append(f'<pre><code class="lang-{html.escape(lang)}">' if lang else "<pre><code>")
                in_code = True
            continue
        if in_code:
            out.append(html.escape(line))
            continue

        stripped = line.strip()

        # Close list if needed
        if in_list and not stripped.startswith("- ") and not stripped.startswith("* "):
            out.append("</ul>")
            in_list = False

        # Table handling
        is_table_line = stripped.startswith("|") and stripped.endswith("|") and len(stripped) > 2
        if is_table_line:
            cells = [c.strip() for c in stripped[1:-1].split("|")]
            is_separator = all(re.match(r'^:?-+:?$', c) for c in cells if c)
            if is_separator and pending_table_header:
                header_cells = [c.strip() for c in pending_table_header[1:-1].split("|")]
                out.append('<table><thead><tr>')
                for cell in header_cells:
                    out.append(f'<th>{inline(cell)}</th>')
                out.append('</tr></thead><tbody>')
                in_table = True
                pending_table_header = None
            elif in_table:
                out.append('<tr>')
                for cell in cells:
                    out.append(f'<td>{inline(cell)}</td>')
                out.append('</tr>')
            else:
                if pending_table_header:
                    out.append(f"<p>{inline(pending_table_header)}</p>")
                pending_table_header = stripped
            continue

        # Close table state if not a table line
        if pending_table_header:
            out.append(f"<p>{inline(pending_table_header)}</p>")
            pending_table_header = None
        if in_table:
            out.append('</tbody></table>')
            in_table = False

        # Horizontal rules
        if stripped in ('---', '***', '___'):
            out.append('<hr>')
            continue

        # Headers
        if m := re.match(r'^(#{1,6})\s+(.+)', stripped):
            level = len(m.group(1))
            content = inline(m.group(2))
            slug = re.sub(r'[^a-z0-9]+', '-', m.group(2).lower()).strip('-')
            out.append(f'<h{level} id="{slug}">{content}</h{level}>')
        # List items
        elif stripped.startswith("- ") or stripped.startswith("* "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(stripped[2:])}</li>")
        # Empty line
        elif not stripped:
            out.append("")
        # Paragraph
        else:
            out.append(f"<p>{inline(stripped)}</p>")

    if in_list:
        out.append("</ul>")
    if in_code:
        out.append("</code></pre>")
    if in_table:
        out.append('</tbody></table>')
    if pending_table_header:
        out.append(f"<p>{inline(pending_table_header)}</p>")

    return "\n".join(out)


def inline(text):
    """Inline markdown: bold, italic, code, links, wiki-links."""
    text = html.escape(text)
    # Protect inline code spans FIRST: their contents are literal, so [[links]],
    # **bold**, etc. inside backticks are not processed. This is why doc examples
    # like `[[category/Name]]` render as text instead of resolving to a (broken) link.
    codes = []
    def _stash(m):
        codes.append(m.group(1))
        return f"\x00C{len(codes) - 1}\x00"
    text = re.sub(r'`(.+?)`', _stash, text)
    # Wiki-links: [[category/Name]] → resolved HTML links
    text = re.sub(r'\[\[([^\]]+)\]\]', resolve_wiki_link, text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\x00C(\d+)\x00', lambda m: f'<code>{codes[int(m.group(1))]}</code>', text)
    return text


# ── Git history ──────────────────────────────────────────────────────

def git_changelog(max_entries=50):
    """Get commits that touched ontology/, phenomena/, heuristics/, or agents/ with diffs."""
    try:
        result = subprocess.run(
            ["git", "log", f"--max-count={max_entries}", "--pretty=format:%H|%ai|%s",
             "--diff-filter=ACDMR", "-p", "--",
             "ontology/", "phenomena/", "heuristics/", "goals/", "agents/"],
            capture_output=True, text=True, cwd=ROOT, encoding="utf-8"
        )
        if result.returncode != 0:
            return []
    except Exception:
        return []

    entries = []
    current = None

    for line in result.stdout.split("\n"):
        if "|" in line and len(line.split("|")) >= 3 and not line.startswith(("+", "-", " ", "@", "d", "i", "n")):
            parts = line.split("|", 2)
            if len(parts[0]) == 40:  # SHA
                if current:
                    entries.append(current)
                current = {
                    "sha": parts[0][:8],
                    "date": parts[1].strip()[:10],
                    "message": parts[2].strip(),
                    "diff_lines": []
                }
                continue

        if current is not None:
            current["diff_lines"].append(line)

    if current:
        entries.append(current)

    return entries


def format_diff_html(diff_lines):
    """Turn unified diff lines into styled HTML."""
    out = []
    in_file = False
    for line in diff_lines:
        if line.startswith("diff --git"):
            if in_file:
                out.append("</div>")
            parts = line.split(" b/")
            fname = parts[-1] if len(parts) > 1 else line
            out.append(f'<div class="diff-file"><div class="diff-filename">{html.escape(fname)}</div>')
            in_file = True
        elif line.startswith("+++") or line.startswith("---"):
            continue
        elif line.startswith("@@"):
            out.append(f'<div class="diff-hunk">{html.escape(line)}</div>')
        elif line.startswith("+"):
            out.append(f'<div class="diff-add">{html.escape(line)}</div>')
        elif line.startswith("-"):
            out.append(f'<div class="diff-del">{html.escape(line)}</div>')
        elif line.startswith("index") or line.startswith("new file") or line.startswith("deleted file"):
            continue
        elif in_file:
            out.append(f'<div class="diff-ctx">{html.escape(line)}</div>')

    if in_file:
        out.append("</div>")

    return "\n".join(out)


# ── Templates ────────────────────────────────────────────────────────

STYLES = """
:root {
  --bg: #0a0a0e;
  --surface: #111116;
  --border: #222;
  --text: #e8e8e8;
  --text-dim: #888;
  --accent: #c084fc;
  --accent-dim: #5a2090;
  --ontology: #60a5fa;
  --phenomena: #22d3ee;
  --heuristics: #f59e0b;
  --goals: #34d399;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  font-size: 17px;
  line-height: 1.65;
  max-width: 900px;
  margin: 0 auto;
  padding: 40px 24px;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
a.wiki-link { color: var(--ontology); border-bottom: 1px dotted var(--ontology); }
a.wiki-link:hover { border-bottom-style: solid; text-decoration: none; }
a.wiki-link-broken { color: #c0392b; border-bottom-color: #c0392b; }
nav {
  display: flex;
  gap: 24px;
  padding: 16px 0;
  border-bottom: 2px solid var(--border);
  margin-bottom: 40px;
  font-size: 15px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  flex-wrap: wrap;
}
nav a { color: var(--text-dim); }
nav a:hover, nav a.active { color: var(--accent); }
h1 {
  font-size: 32px;
  font-weight: 800;
  color: var(--accent);
  margin-bottom: 8px;
  letter-spacing: 1px;
}
h2 { font-size: 24px; font-weight: 700; margin: 32px 0 16px; color: #f0f0f0; }
h3 { font-size: 20px; font-weight: 600; margin: 24px 0 12px; color: #ddd; }
h4 { font-size: 17px; font-weight: 600; margin: 20px 0 10px; color: #ccc; }
p { margin: 10px 0; }
ul { margin: 10px 0 10px 24px; }
li { margin: 6px 0; }
pre {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 16px;
  overflow-x: auto;
  margin: 16px 0;
  font-size: 14px;
  line-height: 1.5;
}
code {
  font-family: 'Consolas', 'Fira Code', monospace;
  font-size: 0.9em;
  background: var(--surface);
  padding: 2px 6px;
  border-radius: 3px;
}
pre code { background: none; padding: 0; font-size: 14px; }
strong { color: #f0f0f0; }
hr {
  border: none;
  border-top: 1px solid var(--border);
  margin: 28px 0;
}

/* Tables */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
  font-size: 15px;
}
th, td {
  padding: 10px 14px;
  text-align: left;
  border: 1px solid var(--border);
}
th {
  background: var(--surface);
  font-weight: 600;
  color: #f0f0f0;
}
tr:nth-child(even) td {
  background: rgba(255,255,255,0.02);
}

/* Category grid */
.category-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px;
  margin: 24px 0;
}
.category-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  transition: border-color 0.2s;
}
.category-card:hover {
  border-color: var(--accent-dim);
}
.category-card h3 {
  margin: 0 0 8px;
  font-size: 20px;
}
.category-card .count {
  font-size: 14px;
  color: var(--text-dim);
}
.category-card a {
  text-decoration: none;
  color: inherit;
  display: block;
  padding: 20px;
}
.category-card a:hover {
  text-decoration: none;
}
.category-card a h3 {
  color: var(--accent);
}
.category-card.ontology-card { border-left: 3px solid var(--ontology); }
.category-card.ontology-card a h3 { color: var(--ontology); }
.category-card.heuristics-card { border-left: 3px solid var(--heuristics); }
.category-card.heuristics-card a h3 { color: var(--heuristics); }
.category-card.goals-card { border-left: 3px solid var(--goals); }
.category-card.goals-card a h3 { color: var(--goals); }
.category-card.phenomena-card { border-left: 3px solid var(--phenomena); }
.category-card.phenomena-card a h3 { color: var(--phenomena); }

/* Node rows (section index: game / book / framework) */
.node-rows {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin: 24px 0;
}
.node-row {
  display: block;
  background: var(--surface);
  border: 1px solid var(--border);
  border-left: 4px solid var(--border);
  border-radius: 10px;
  padding: 20px 24px;
  color: inherit;
  transition: border-color 0.2s, transform 0.1s, background 0.2s;
}
.node-row:hover {
  text-decoration: none;
  transform: translateY(-2px);
  background: #15151c;
}
.node-row-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 16px;
}
.node-row-title {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: 0.3px;
}
.node-row-tagline {
  font-size: 14px;
  color: var(--text-dim);
  text-transform: uppercase;
  letter-spacing: 1.2px;
  margin-top: 2px;
}
.node-row-count {
  font-size: 14px;
  color: var(--text-dim);
  white-space: nowrap;
  font-family: 'Consolas', monospace;
}
.node-row-blurb {
  margin: 12px 0 0;
  color: var(--text);
  font-size: 16px;
  line-height: 1.6;
  max-width: 70ch;
}
.node-row.ontology-card { border-left-color: var(--ontology); }
.node-row.ontology-card:hover { border-color: var(--ontology); }
.node-row.ontology-card .node-row-title { color: var(--ontology); }
.node-row.heuristics-card { border-left-color: var(--heuristics); }
.node-row.heuristics-card:hover { border-color: var(--heuristics); }
.node-row.heuristics-card .node-row-title { color: var(--heuristics); }
.node-row.goals-card { border-left-color: var(--goals); }
.node-row.goals-card:hover { border-color: var(--goals); }
.node-row.goals-card .node-row-title { color: var(--goals); }
.node-row.phenomena-card { border-left-color: var(--phenomena); }
.node-row.phenomena-card:hover { border-color: var(--phenomena); }
.node-row.phenomena-card .node-row-title { color: var(--phenomena); }

/* Faceted card view */
.facet-controls {
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
  margin: 20px 0 8px;
  padding: 14px 18px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  font-size: 14px;
  color: var(--text-dim);
}
.facet-controls label {
  display: flex;
  align-items: center;
  gap: 8px;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 600;
}
.facet-controls select {
  background: var(--bg);
  color: var(--text);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 6px 10px;
  font-size: 14px;
  font-family: inherit;
  text-transform: none;
  letter-spacing: 0;
}
.facet-summary { margin-left: auto; font-family: 'Consolas', monospace; }
.facet-group { margin: 28px 0; }
.facet-group h3 {
  margin: 0 0 12px;
  padding-bottom: 6px;
  border-bottom: 1px solid var(--border);
  color: #f0f0f0;
}
.facet-head { cursor: pointer; user-select: none; }
.facet-head:hover { color: var(--accent); }
.facet-caret {
  display: inline-block;
  width: 1em;
  margin-right: 4px;
  font-size: 0.8em;
  color: var(--text-dim);
  transition: transform 0.15s;
}
.facet-group.collapsed .facet-caret { transform: rotate(-90deg); }
.facet-group.collapsed .card-grid { display: none; }
.facet-group.collapsed h3 { margin-bottom: 0; }
.facet-count {
  font-size: 14px;
  color: var(--text-dim);
  font-weight: 400;
  font-family: 'Consolas', monospace;
}
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
  gap: 10px;
}
.card-tile {
  position: relative;
  display: block;
  background: var(--surface);
  border: 1px solid var(--border);
  border-left: 3px solid var(--text-dim);
  border-radius: 6px;
  padding: 12px 14px;
  color: inherit;
  transition: border-color 0.15s, transform 0.1s;
}
.card-tile:hover { text-decoration: none; transform: translateY(-1px); border-color: var(--accent-dim); }
.card-cost {
  position: absolute;
  top: 10px;
  right: 12px;
  font-size: 12px;
  font-family: 'Consolas', monospace;
  color: var(--text-dim);
}
.card-name { display: block; font-weight: 600; font-size: 15px; padding-right: 64px; }
.cost-up { color: #6fcf97; }
.card-meta { display: block; font-size: 12px; color: var(--text-dim); margin-top: 3px; }
.card-tile.rarity-starter   { border-left-color: #8a8f98; }
.card-tile.rarity-common    { border-left-color: #c9ced6; }
.card-tile.rarity-uncommon  { border-left-color: #5aa9e6; }
.card-tile.rarity-rare      { border-left-color: #f5c518; }
.card-tile.rarity-special   { border-left-color: var(--accent); }

/* Entry grid */
.entry-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 10px;
  margin: 16px 0;
}
.entry-grid a {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 10px 14px;
  font-weight: 600;
  font-size: 15px;
  transition: border-color 0.2s;
}
.entry-grid a:hover {
  border-color: var(--accent-dim);
  text-decoration: none;
}

/* Back link */
.back-link {
  margin-bottom: 24px;
  font-size: 15px;
}
.back-link a {
  color: var(--text-dim);
}
.back-link a:hover {
  color: var(--accent);
}

/* Section badge */
.section-badge {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: 4px;
  margin-bottom: 12px;
}
.section-badge.ontology { background: rgba(96,165,250,0.15); color: var(--ontology); }
.section-badge.heuristics { background: rgba(245,158,11,0.15); color: var(--heuristics); }
.section-badge.goals { background: rgba(52,211,153,0.15); color: var(--goals); }
.section-badge.phenomena { background: rgba(34,211,238,0.15); color: var(--phenomena); }

/* Companion link (ontology ↔ heuristics) */
.companion-link {
  margin: 20px 0;
  padding: 12px 16px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 6px;
  font-size: 15px;
}

/* Changelog */
.changelog-entry {
  border: 1px solid var(--border);
  border-radius: 8px;
  margin: 20px 0;
  overflow: hidden;
}
.changelog-header {
  background: var(--surface);
  padding: 14px 18px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
}
.changelog-header:hover { background: #181820; }
.changelog-date {
  font-size: 14px;
  color: var(--text-dim);
  font-family: 'Consolas', monospace;
}
.changelog-sha {
  font-size: 12px;
  color: var(--accent-dim);
  font-family: 'Consolas', monospace;
}
.changelog-msg {
  font-weight: 600;
  font-size: 16px;
}
.changelog-diff {
  border-top: 1px solid var(--border);
  padding: 0;
  font-family: 'Consolas', monospace;
  font-size: 13px;
  line-height: 1.5;
}
.diff-file {
  border-bottom: 1px solid var(--border);
}
.diff-file:last-child { border-bottom: none; }
.diff-filename {
  background: #161622;
  padding: 8px 16px;
  font-weight: 700;
  color: var(--accent);
  font-size: 14px;
}
.diff-hunk { color: #6ab0f3; padding: 2px 16px; background: #0d1117; }
.diff-add { color: #4ade80; padding: 2px 16px; background: rgba(74,222,128,0.07); }
.diff-del { color: #f87171; padding: 2px 16px; background: rgba(248,113,113,0.07); }
.diff-ctx { color: var(--text-dim); padding: 2px 16px; }

/* Stats panel */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin: 20px 0;
}
@media (max-width: 600px) {
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
}
.stat {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px;
  text-align: center;
}
.stat-value {
  font-size: 32px;
  font-weight: 800;
  color: var(--accent);
  line-height: 1.1;
}
.stat-label {
  font-size: 13px;
  color: var(--text-dim);
  margin-top: 4px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.state-details {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin: 16px 0 32px;
}
@media (max-width: 600px) {
  .state-details { grid-template-columns: 1fr; }
}
.state-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px 20px;
}
.state-card h3 {
  margin: 0 0 8px;
  font-size: 15px;
  color: var(--accent);
  text-transform: uppercase;
  letter-spacing: 1px;
}
.state-card p {
  margin: 4px 0;
  font-size: 15px;
  color: var(--text-dim);
}
.state-card strong {
  color: var(--text);
}

.empty-state {
  text-align: center;
  padding: 80px 20px;
  color: var(--text-dim);
  font-size: 18px;
}

/* Journey / character progress */
.journey-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
  margin: 16px 0 40px;
}
.journey-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 20px;
}
.journey-card.completed {
  border-color: #4ade80;
  background: linear-gradient(135deg, var(--surface), rgba(74, 222, 128, 0.04));
}
.journey-card.active {
  border-color: var(--accent);
}
.journey-badge {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  margin-bottom: 6px;
}
.journey-card.completed .journey-badge { color: #4ade80; }
.journey-card.active .journey-badge { color: var(--accent); }
.journey-name {
  font-size: 22px;
  font-weight: 800;
  color: #f0f0f0;
  margin-bottom: 6px;
}
.journey-stats {
  font-size: 14px;
  color: var(--text-dim);
}

footer {
  margin-top: 60px;
  padding-top: 20px;
  border-top: 1px solid var(--border);
  font-size: 13px;
  color: var(--text-dim);
  text-align: center;
}
"""

TWITCH_CHANNEL = "ClaudeSlaysTheSpire"

def page(title, content, active=""):
    nav_items = [
        ("index.html", "Home"),
        ("philosophy.html", "Philosophy"),
        ("goals.html", "Goals"),
        ("ontology.html", "Ontology"),
        ("phenomena.html", "Phenomena"),
        ("heuristics.html", "Heuristics"),
        ("changelog.html", "Changelog"),
    ]
    nav_html = "\n".join(
        f'<a href="{href}" class="{"active" if name.lower() == active.lower() else ""}">{name}</a>'
        for href, name in nav_items
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)} &middot; Claude Slays the Spire</title>
<script async src="https://plausible.io/js/pa-DmrspWebBN8Lfq1qPfK3Z.js"></script>
<script>window.plausible=window.plausible||function(){{(plausible.q=plausible.q||[]).push(arguments)}},plausible.init=plausible.init||function(i){{plausible.o=i||{{}}}};plausible.init()</script>
<style>{STYLES}</style>
</head>
<body>
<h1>Claude Slays the Spire</h1>
<nav>{nav_html}</nav>
{content}
<footer>
  <a href="https://github.com/skondrashov/ClaudeSlaysTheSpire">GitHub</a> &middot;
  <a href="https://www.reddit.com/r/ClaudeSlaysTheSpire/">Reddit</a>
</footer>
</body>
</html>"""


# ── Content discovery ────────────────────────────────────────────────

def discover_content(content_dir):
    """Discover content structure: categories (subdirs) and top-level files.

    Returns:
        categories: dict of category_name -> {
            "entries": list of {"name": str, "stem": str, "content": str}
        }
        top_level_files: list of {"name": str, "stem": str, "content": str}
    """
    categories = {}
    top_level_files = []

    if not content_dir.exists():
        return categories, top_level_files

    # Top-level .md files
    for f in sorted(content_dir.glob("*.md")):
        content = f.read_text(encoding="utf-8")
        title_match = re.match(r'^#\s+(.+)', content.strip())
        name = title_match.group(1) if title_match else f.stem.replace("-", " ").replace("_", " ").title()
        top_level_files.append({
            "name": name,
            "stem": f.stem,
            "content": content,
        })

    # Subdirectories
    for d in sorted(content_dir.iterdir()):
        if not d.is_dir():
            continue
        cat_name = d.name

        entries = []
        for f in sorted(d.glob("*.md")):
            if f.name == "_index.md":
                continue
            content = f.read_text(encoding="utf-8")
            title_match = re.match(r'^#\s+(.+)', content.strip())
            name = title_match.group(1) if title_match else f.stem.replace("-", " ").replace("_", " ").title()
            entries.append({
                "name": name,
                "stem": f.stem,
                "content": content,
            })

        categories[cat_name] = {"entries": entries}

    return categories, top_level_files


def short_name(full_name):
    """Extract just the display name before any parenthetical stats."""
    idx = full_name.find(" (")
    if idx > 0:
        return full_name[:idx]
    return full_name


def make_slug(section, node, category=None, entry_stem=None):
    """Generate the output HTML filename.

    ontology-sts1.html, ontology-sts1-cards.html, ontology-sts1-cards-bash.html
    """
    parts = [section, node]
    if category:
        parts.append(category)
    if entry_stem:
        parts.append(entry_stem)
    return "-".join(parts) + ".html"


# ── Run stats ─────────────────────────────────────────────────────

def load_run_stats(root):
    """Load run statistics from data/run_stats.json."""
    stats_file = root / "games" / "sts1" / "data" / "run_stats.json"
    defaults = {"total_runs": 0, "wins": 0, "best_floor": 0, "deaths": 0,
                "current_class": "?", "best_ascension": 0, "character_stats": {}}

    if not stats_file.exists():
        return defaults

    try:
        raw = json.loads(stats_file.read_text(encoding="utf-8"))
        return {
            "total_runs": raw.get("total_runs", 0),
            "wins": raw.get("wins", 0),
            "best_floor": raw.get("best_floor", 0),
            "deaths": raw.get("deaths", 0),
            "current_class": raw.get("current_class", "?"),
            "best_ascension": raw.get("best_ascension", 0),
            "character_stats": raw.get("character_stats", {}),
        }
    except (ValueError, KeyError):
        return defaults


# ── Section index builder ────────────────────────────────────────────

def build_section_index(section, section_label, categories, top_level_files, card_class, description):
    """Build the index page for ontology or heuristics."""
    body = f'<span class="section-badge {section}">{section_label}</span>\n'
    body += f"<h2>{section_label.title()}</h2>\n"
    body += f"<p>{description}</p>\n"
    body += '<div class="category-grid">\n'

    # Top-level files
    for tlf in top_level_files:
        slug = f"{section}-{tlf['stem']}.html"
        body += f"""<div class="category-card {card_class}"><a href="{slug}">
  <h3>{html.escape(tlf["name"])}</h3>
</a></div>\n"""

    # Category cards
    for cat_name, cat_data in categories.items():
        slug = make_slug(section, cat_name)
        count = len(cat_data["entries"])
        display_name = cat_name.replace("-", " ").replace("_", " ").title()
        body += f"""<div class="category-card {card_class}"><a href="{slug}">
  <h3>{html.escape(display_name)}</h3>
  <div class="count">{count} {"entry" if count == 1 else "entries"}</div>
</a></div>\n"""

    body += "</div>\n"

    if not categories and not top_level_files:
        body = f'<div class="empty-state">No {section} entries yet.</div>'

    return body


# ── Landing page ────────────────────────────────────────────────────

def build_landing(ont_categories, heur_categories, run_stats):
    """Build the index/landing page content."""

    ont_entries = sum(len(c["entries"]) for c in ont_categories.values())
    heur_entries = sum(len(c["entries"]) for c in heur_categories.values())

    _char_names = {"IRONCLAD": "Ironclad", "THE_SILENT": "Silent", "DEFECT": "Defect", "WATCHER": "Watcher"}
    char_name = _char_names.get(run_stats.get("current_class", "IRONCLAD"), "Unknown")

    # Stream-down notice + Twitch embed
    twitch_html = f"""
<div style="margin: 24px 0 16px; padding: 16px 20px; border-radius: 8px; border: 1px solid var(--border); background: rgba(212, 160, 255, 0.07);">
  <p style="margin: 0; font-weight: 600;">The live stream is paused for now.</p>
  <p style="margin: 8px 0 0; color: var(--text-dim);">Claude Fable 5, the model behind the stream, is offline while we wait to hear how its situation resolves. The run will pick back up once we know more. In the meantime, the past broadcasts are worth a watch: find them under Videos on the Twitch channel below, or on YouTube.</p>
</div>
<div style="margin: 0 0 32px; border-radius: 8px; overflow: hidden; border: 1px solid var(--border);">
  <iframe
    src="https://player.twitch.tv/?channel={TWITCH_CHANNEL}&parent=claudeslaysthespire.org&muted=true"
    height="360"
    width="100%"
    allowfullscreen
    style="border: none; display: block;">
  </iframe>
</div>
"""

    # Stats panel
    stats_html = f"""
<div class="stats-grid">
  <div class="stat"><div class="stat-value">{run_stats['total_runs']}</div><div class="stat-label">Runs</div></div>
  <div class="stat"><div class="stat-value">{run_stats['wins']}</div><div class="stat-label">Wins</div></div>
  <div class="stat"><div class="stat-value">{ont_entries}</div><div class="stat-label">Ontology Entries</div></div>
  <div class="stat"><div class="stat-value">{heur_entries}</div><div class="stat-label">Heuristics</div></div>
</div>

<div class="state-details">
  <div class="state-card">
    <h3>System</h3>
    <p><strong>Model:</strong> Claude Fable 5 via Claude Code</p>
    <p><strong>Character:</strong> {char_name}, Ascension {run_stats.get('best_ascension', 0)}</p>
    <p><strong>Interface:</strong> <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=2131373661">CommunicationMod</a> (stdin/stdout JSON)</p>
  </div>
  <div class="state-card">
    <h3>The Approach</h3>
    <p>The agent reads from a structured <a href="knowledge-system.html">knowledge system</a>:
    <a href="ontology.html">ontology</a> (facts about the game),
    <a href="phenomena.html">phenomena</a> (derived facts, generated from the ontology), and
    <a href="heuristics.html">heuristics</a> (strategy, graded by results).
    Playing agents only read; analysis sessions write the lessons back.</p>
  </div>
</div>
"""

    # Journey section
    _cstats = run_stats.get("character_stats", {})
    _ccls = run_stats.get("current_class", "IRONCLAD")
    _jcards = []
    for _cls in ["IRONCLAD", "THE_SILENT", "DEFECT", "WATCHER"]:
        _s = _cstats.get(_cls)
        _cur = (_cls == _ccls)
        if not _s and not _cur:
            continue
        _dn = _char_names[_cls]
        _w = _s["wins"] if _s else 0
        _runs = _s["runs"] if _s else 0
        _wins_label = f"{_w} win" + ("s" if _w != 1 else "")
        # "Best" is ordered by ascension first: a deep A9 attempt outranks an
        # A5 win; within an ascension a win outranks any floor.
        _b = (_s or {}).get("best") or {}
        _won_a = (_s or {}).get("best_won_ascension")
        _complete = f"A{_won_a} complete" if _won_a is not None else "no win yet"
        if _cur:
            _best_bit = (f"best A{_b.get('ascension', 0)} "
                         + ("WIN" if _b.get("victory") else f"F{_b.get('floor', 0)}"))
            _jcards.append(
                '<div class="journey-card active">'
                '<div class="journey-badge">NOW PLAYING</div>'
                f'<div class="journey-name">{_dn}</div>'
                f'<div class="journey-stats">Ascension {run_stats.get("best_ascension", 0)} '
                f'&middot; {_best_bit} &middot; {_complete}</div>'
                '</div>')
        elif _b.get("victory"):
            _jcards.append(
                '<div class="journey-card completed">'
                f'<div class="journey-badge">A{_b.get("ascension", 0)} COMPLETE</div>'
                f'<div class="journey-name">{_dn}</div>'
                f'<div class="journey-stats">{_wins_label} &middot; {_runs} runs</div>'
                '</div>')
        elif _s:
            _jcards.append(
                '<div class="journey-card active">'
                f'<div class="journey-badge">BEST A{_b.get("ascension", 0)} F{_b.get("floor", 0)}</div>'
                f'<div class="journey-name">{_dn}</div>'
                f'<div class="journey-stats">{_complete} &middot; {_runs} runs</div>'
                '</div>')
    journey_html = ""
    if _jcards:
        journey_html = '<h2>Journey</h2>\n<div class="journey-grid">\n' + '\n'.join(_jcards) + '\n</div>\n'

    # Intro
    intro_html = """
<div style="margin-bottom: 40px;">
<p>
Claude plays <a href="https://store.steampowered.com/app/646570/Slay_the_Spire/">Slay the Spire</a>,
one decision at a time, with its reasoning written out at every step. There is no hardcoded
strategy and no fine-tuning. Everything Claude knows about the game lives in a structured
knowledge system called <a href="ontology-praxis.html">Praxis</a>, and all of it is browsable here.
</p>

<p>
The project is less about Slay the Spire than about how an LLM can learn. When a person learns
a game, they do not play ten thousand matches and let the statistics settle. They read, they
take notes, they go over their losses, and they come back with a corrected understanding of how
the game works and what they should be doing in it. This project gives Claude that loop. A
playing agent makes decisions and leaves behind a record of every one. Analysis sessions read
that record, work out which decisions were wrong and why, and write the lessons into the
knowledge system: facts about the game into the <a href="ontology.html">ontology</a>, advice
about how to play into the <a href="heuristics.html">heuristics</a>. The next run reads the
improved knowledge. The agents themselves are ephemeral. The knowledge is what accumulates,
and the <a href="changelog.html">changelog</a> shows it accumulating.
</p>

<p>
The split between facts and strategy is deliberate. A fact about the game is either correct or
incomplete, and once correct it never needs to change, so facts can be composed and built on
indefinitely. Strategy is provisional by nature: it is graded by how the runs actually go, and
it gets rewritten when it turns out to be wrong. A heuristic is a conclusion the model caches
because it could not reliably re-derive it in the middle of a fight, which means every
heuristic is also an admission of a reasoning gap. As models improve, heuristics should become
unnecessary and fall away, while the ontology keeps its value. The longer aim is transfer: to
find out whether this way of organizing and building knowledge works for the next game, with
none of the Slay the Spire content carried over. The <a href="philosophy.html">philosophy
page</a> covers what that experiment is trying to establish.
</p>
</div>
"""

    # Knowledge sections preview
    sections_html = '<h2>Knowledge</h2>\n<div class="category-grid">\n'

    # Goals card
    sections_html += f"""<div class="category-card goals-card"><a href="goals.html">
  <h3>Goals</h3>
  <div class="count">Agent operating modes</div>
</a></div>\n"""

    # Ontology card
    sections_html += f"""<div class="category-card ontology-card"><a href="ontology.html">
  <h3>Ontology</h3>
  <div class="count">{ont_entries} game entries &middot; facts</div>
</a></div>\n"""

    # Phenomena card
    sections_html += f"""<div class="category-card phenomena-card"><a href="phenomena.html">
  <h3>Phenomena</h3>
  <div class="count">Derived facts &middot; generated</div>
</a></div>\n"""

    # Heuristics card
    sections_html += f"""<div class="category-card heuristics-card"><a href="heuristics.html">
  <h3>Heuristics</h3>
  <div class="count">{heur_entries} game entries &middot; strategy</div>
</a></div>\n"""

    sections_html += "</div>\n"

    return twitch_html + stats_html + journey_html + intro_html + sections_html


# ── Node discovery ──────────────────────────────────────────────────

NODE_NAMES = {
    "praxis": "Praxis",
    "sts1": "Slay the Spire",
    "book-sts1": "Slay the Spire Book",
}

NODE_DESCRIPTIONS = {
    "praxis": "The framework for building domain knowledge through structured practice.",
    "sts1": "The game domain &mdash; cards, enemies, relics, mechanics, strategy.",
    "book-sts1": "The knowledge system itself &mdash; its structure, coverage, and maintenance.",
}

# Display order for nodes on every section page: the game first, then the book
# about the game, then the framework underneath both.
NODE_ORDER = ["sts1", "book-sts1", "praxis"]

# Short tagline shown under each node title on a section page.
NODE_TAGLINES = {
    "sts1": "The game",
    "book-sts1": "The knowledge system about the game",
    "praxis": "The framework underneath it all",
}

# The 9 cells: what each node means within each layer (ontology / heuristics / goals).
# These are the most conceptually loaded pages in the project, so each gets a real
# explanation rather than a one-liner.
NODE_SECTION_BLURB = {
    "ontology": {
        "sts1": "The complete factual database of Slay the Spire &mdash; every card, enemy, "
                "boss, relic, event, buff, and rule. Deterministic and composable: a correct "
                "fact never needs revision, only extension.",
        "book-sts1": "Facts about the knowledge system itself &mdash; how the book is structured, "
                     "how entries link together, how coverage is measured, and how the pipeline "
                     "and site are wired up.",
        "praxis": "The framework's own vocabulary &mdash; what layers, nodes, entries, and "
                  "evidence are, and how theory-informed action turns experience into reusable "
                  "knowledge.",
    },
    "heuristics": {
        "sts1": "Strategy for actually playing &mdash; combat execution, card evaluation, map "
                "routing, per-enemy and per-boss guidance, and proven archetypes. Provisional and "
                "evidence-grounded; these improve and get replaced as understanding deepens.",
        "book-sts1": "How to maintain and grow the book well &mdash; what makes a good entry, when "
                     "to split or merge, how to keep coverage honest, and how to avoid drift.",
        "praxis": "Principles for practicing the framework anywhere &mdash; demanding evidence, "
                  "resisting overfitting, attributing outcomes, and keeping knowledge maintained.",
    },
    "goals": {
        "sts1": "Operating modes for the game agent &mdash; Win, Explore, Audit, Curate, Develop. "
                "Each defines what to read, what to do, and what to write back.",
        "book-sts1": "Operating modes for tending the book &mdash; curating strategy and extending "
                     "coverage so the knowledge system keeps getting sharper.",
        "praxis": "The mode for evolving the framework itself &mdash; developing Praxis as a "
                  "reusable practice rather than a one-off.",
    },
}

SECTION_META = {
    "ontology": {
        "card_class": "ontology-card",
        "description": "Facts about how things work. Deterministic, composable, permanent.",
    },
    "phenomena": {
        "card_class": "phenomena-card",
        "description": "Derived facts, materialized from ontology — resolved upgraded cards and the like. Generated; do not edit.",
    },
    "heuristics": {
        "card_class": "heuristics-card",
        "description": "Strategy and guidance. Provisional, evidence-grounded, improvable.",
    },
    "goals": {
        "card_class": "goals-card",
        "description": "Agent operating modes. What to read, what to do, what to output.",
    },
}

# ── Faceted card view (STS-specific presentation) ───────────────────
# The cards/ directory is flat on disk (agent looks cards up by name/link).
# For human browsing we parse the per-entry fields and let the reader
# group/sort the dump however reads best. This is deliberately not
# game-agnostic — it knows what a Slay the Spire card looks like.

CARD_CHAR_ORDER = ["Ironclad", "Silent", "Defect", "Watcher", "Colorless", "All"]
CARD_TYPE_ORDER = ["Attack", "Skill", "Power", "Status", "Curse"]
CARD_RARITY_ORDER = ["Starter", "Common", "Uncommon", "Rare", "Special"]


def parse_entry_fields(content):
    """Pull a leading '- **Key:** value' definition list into a dict."""
    fields = {}
    for line in content.split("\n"):
        m = re.match(r'^\s*[-*]\s*\*\*([A-Za-z][A-Za-z ]*):\*\*\s*(.+?)\s*$', line)
        if m:
            fields[m.group(1).strip().lower()] = m.group(2).strip()
    return fields


def _strip_wiki(val):
    m = re.search(r'\[\[(?:[^\]]*/)?([^\]]+)\]\]', val)
    return m.group(1) if m else val


def _parse_cost(val):
    """Return (base, upgraded, star) energy costs.

    Clean single cost ('1E', 'X')         -> ('1E', '', False)
    Upgrade form ('1E (0E upgraded)')      -> ('1E', '0E', False)
    Reversed form ('0E (1E unupgraded)')   -> ('1E', '0E', False)  # base = unupgraded
    Conditional w/ base ('3E (reduced…)')  -> ('3E', '', True)     # base kept, '*' appended
    No numeric base ('Unplayable')         -> ('*', '', False)
    """
    v = (val or "").strip()
    token = r'(?:\d+|X)E?'
    if re.fullmatch(token, v):
        return v, "", False
    m = re.fullmatch(rf'({token})\s*\(({token})\s+upgraded\)', v)
    if m:
        return m.group(1), m.group(2), False
    m = re.fullmatch(rf'({token})\s*\(({token})\s+unupgraded\)', v)
    if m:
        return m.group(2), m.group(1), False
    # Conditional/prose: keep the leading base cost if there is one, flag with '*'.
    m = re.match(rf'({token})\b', v)
    if m:
        return m.group(1), "", True
    return "*", "", False


def render_faceted_cards(entries, section, node_key, cat_name, companion_link):
    """Interactive group/sort view for the cards dump, parsed from entry fields."""
    cards = []
    for entry in entries:
        f = parse_entry_fields(entry["content"])
        cost, up, star = _parse_cost(f.get("cost", ""))
        cards.append({
            "name": short_name(entry["name"]),
            "href": make_slug(section, node_key, cat_name, entry["stem"]),
            "cost": cost,
            "up": up,
            "star": star,
            "type": _strip_wiki(f.get("type", "—")) or "—",
            "character": f.get("character", "—") or "—",
            "rarity": f.get("rarity", "—") or "—",
        })
    data_json = json.dumps(cards)
    orders_json = json.dumps({
        "character": CARD_CHAR_ORDER,
        "type": CARD_TYPE_ORDER,
        "rarity": CARD_RARITY_ORDER,
    })

    head = f'<h2>Cards</h2>\n{companion_link}'
    controls = """
<div class="facet-controls">
  <label>Group by
    <select id="facet-group">
      <option value="character">Character</option>
      <option value="type">Type</option>
      <option value="rarity">Rarity</option>
      <option value="cost">Cost</option>
      <option value="none">Nothing</option>
    </select>
  </label>
  <label>Sort by
    <select id="facet-sort">
      <option value="name">Name</option>
      <option value="cost">Cost</option>
      <option value="rarity">Rarity</option>
    </select>
  </label>
  <span class="facet-summary" id="facet-summary"></span>
</div>
<div id="facet-out"></div>
"""
    script = """
<script>
(function(){
  var CARDS = __DATA__;
  var ORDERS = __ORDERS__;
  var gSel = document.getElementById('facet-group');
  var sSel = document.getElementById('facet-sort');
  var cont = document.getElementById('facet-out');
  var summary = document.getElementById('facet-summary');
  function esc(s){ return String(s).replace(/[&<>"]/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  function costNum(c){ var n = parseInt(c, 10); return isNaN(n) ? 999 : n; }
  function rank(arr, v){ var i = arr ? arr.indexOf(v) : -1; return i < 0 ? 999 : i; }
  function render(){
    var groupBy = gSel.value, sortBy = sSel.value;
    var groups = {};
    CARDS.forEach(function(c){
      var k = groupBy === 'none' ? 'All cards' : (c[groupBy] || '—');
      (groups[k] = groups[k] || []).push(c);
    });
    var ord = ORDERS[groupBy];
    var keys = Object.keys(groups).sort(function(a,b){
      if(groupBy === 'cost'){ var dc = costNum(a) - costNum(b); return dc !== 0 ? dc : a.localeCompare(b); }
      var d = rank(ord, a) - rank(ord, b);
      return d !== 0 ? d : a.localeCompare(b);
    });
    function cmp(a,b){
      if(sortBy === 'cost'){ var d = costNum(a.cost) - costNum(b.cost); if(d) return d; }
      else if(sortBy === 'rarity'){ var d = rank(ORDERS.rarity, a.rarity) - rank(ORDERS.rarity, b.rarity); if(d) return d; }
      return a.name.localeCompare(b.name);
    }
    var out = '';
    keys.forEach(function(k){
      var list = groups[k].slice().sort(cmp);
      out += '<div class="facet-group"><h3 class="facet-head"><span class="facet-caret">&#9662;</span>' + esc(k) + ' <span class="facet-count">' + list.length + '</span></h3><div class="card-grid">';
      list.forEach(function(c){
        var costHtml = esc(c.cost) + (c.star ? '*' : '') + (c.up ? '<span class="cost-up"> (' + esc(c.up) + ')+</span>' : '');
        out += '<a class="card-tile rarity-' + esc((c.rarity||'').toLowerCase()) + '" href="' + esc(c.href) + '">'
             + '<span class="card-cost">' + costHtml + '</span>'
             + '<span class="card-name">' + esc(c.name) + '</span>'
             + '<span class="card-meta">' + esc(c.type) + ' &middot; ' + esc(c.character) + '</span></a>';
      });
      out += '</div></div>';
    });
    cont.innerHTML = out;
    summary.textContent = CARDS.length + ' cards';
  }
  cont.addEventListener('click', function(e){
    var head = e.target.closest('.facet-head');
    if(head){ head.parentNode.classList.toggle('collapsed'); }
  });
  gSel.addEventListener('change', render);
  sSel.addEventListener('change', render);
  render();
})();
</script>
"""
    script = script.replace("__DATA__", data_json).replace("__ORDERS__", orders_json)
    return head + controls + script


def discover_nodes(section_dir):
    """Discover all nodes in a section directory."""
    nodes = {}
    if not section_dir.exists():
        return nodes
    for d in sorted(section_dir.iterdir()):
        if d.is_dir() and not d.name.startswith("."):
            categories, top_files = discover_content(d)
            nodes[d.name] = {"categories": categories, "top_level_files": top_files}
    return nodes


# ── Build ────────────────────────────────────────────────────────────

def build(strict=False):
    global _wiki_link_node, _wiki_link_source, _valid_pages, _broken_links

    # Clean output
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # Discover all nodes across all sections
    all_sections = {}
    for section in ["goals", "ontology", "phenomena", "heuristics"]:
        all_sections[section] = discover_nodes(ROOT / section)

    # Build the set of every entry/top-level page filename so wiki-links can be
    # validated against real targets (see resolve_wiki_link).
    _valid_pages = set()
    for sec, nodes in all_sections.items():
        for node_key, node_data in nodes.items():
            _valid_pages.add(make_slug(sec, node_key))  # node index page
            for tlf in node_data["top_level_files"]:
                _valid_pages.add(make_slug(sec, node_key, tlf["stem"]))
            for cat_name, cat_data in node_data["categories"].items():
                _valid_pages.add(make_slug(sec, node_key, cat_name))  # category index page
                for entry in cat_data["entries"]:
                    _valid_pages.add(make_slug(sec, node_key, cat_name, entry["stem"]))
    _broken_links = []

    run_stats = load_run_stats(ROOT)
    total_pages = 0

    # ── Index page ──
    ont_sts1 = all_sections["ontology"].get("sts1", {"categories": {}, "top_level_files": []})
    heur_sts1 = all_sections["heuristics"].get("sts1", {"categories": {}, "top_level_files": []})
    index_body = build_landing(ont_sts1["categories"], heur_sts1["categories"], run_stats)
    (OUT / "index.html").write_text(page("Home", index_body, "Home"), encoding="utf-8")
    total_pages += 1

    # ── Static doc pages (site/*.md) ──
    # philosophy.md is the project's purpose statement; knowledge-system.html is
    # linked from the landing page. Both previously 404'd — the .md files existed
    # but were never built.
    for md_stem, doc_title, nav_name in (
        ("philosophy", "Philosophy", "Philosophy"),
        ("knowledge-system", "The Knowledge System", ""),
    ):
        md_path = ROOT / "site" / f"{md_stem}.md"
        if md_path.exists():
            doc_body = md_to_html(md_path.read_text(encoding="utf-8"))
            (OUT / f"{md_stem}.html").write_text(
                page(doc_title, doc_body, nav_name), encoding="utf-8")
            total_pages += 1

    # ── Build all sections (ontology, heuristics, goals) ──
    for section, nodes in all_sections.items():
        meta = SECTION_META[section]
        card_class = meta["card_class"]

        # Section index page — lists all nodes as full-width rows.
        body = f'<span class="section-badge {section}">{section}</span>\n'
        body += f"<h2>{section.title()}</h2>\n"
        body += f"<p>{meta['description']}</p>\n"
        body += '<div class="node-rows">\n'

        # Order nodes: game first, then the book, then the framework. Any node
        # not in NODE_ORDER falls in afterward, alphabetically.
        ordered_keys = [k for k in NODE_ORDER if k in nodes]
        ordered_keys += [k for k in sorted(nodes) if k not in NODE_ORDER]

        for node_key in ordered_keys:
            node_data = nodes[node_key]
            node_display = NODE_NAMES.get(node_key, node_key.title())
            tagline = NODE_TAGLINES.get(node_key, "")
            blurb = NODE_SECTION_BLURB.get(section, {}).get(node_key) \
                or NODE_DESCRIPTIONS.get(node_key, "")
            node_slug = make_slug(section, node_key)
            top_count = len(node_data["top_level_files"])
            cat_count = len(node_data["categories"])
            entry_count = sum(len(c["entries"]) for c in node_data["categories"].values()) + top_count

            meta_bits = f"{entry_count} entries"
            if cat_count:
                meta_bits += f" &middot; {cat_count} categor{'y' if cat_count == 1 else 'ies'}"

            body += f"""<a class="node-row {card_class}" href="{node_slug}">
  <div class="node-row-head">
    <div>
      <div class="node-row-title">{html.escape(node_display)}</div>
      <div class="node-row-tagline">{html.escape(tagline)}</div>
    </div>
    <div class="node-row-count">{meta_bits}</div>
  </div>
  <p class="node-row-blurb">{blurb}</p>
</a>\n"""

        body += "</div>\n"
        if not nodes:
            body = f'<div class="empty-state">No {section} entries yet.</div>'

        (OUT / f"{section}.html").write_text(page(section.title(), body, section.title()), encoding="utf-8")
        total_pages += 1

        # ── Per-node pages ──
        for node_key, node_data in nodes.items():
            _wiki_link_node = node_key
            node_display = NODE_NAMES.get(node_key, node_key.title())
            categories = node_data["categories"]
            top_files = node_data["top_level_files"]
            node_slug = make_slug(section, node_key)

            # Get companion node data (ontology ↔ heuristics within same node)
            companion_section = "heuristics" if section == "ontology" else "ontology"
            companion_node = all_sections.get(companion_section, {}).get(node_key, {"categories": {}, "top_level_files": []})
            companion_categories = companion_node["categories"]

            # Node index page — lists categories + top-level files
            node_body = f'<span class="section-badge {section}">{section}</span>\n'
            node_body += f'<div class="back-link"><a href="{section}.html">&larr; {section.title()}</a></div>'
            node_body += f"<h2>{html.escape(node_display)}</h2>\n"
            node_body += '<div class="category-grid">\n'

            for tlf in top_files:
                tlf_slug = make_slug(section, node_key, tlf["stem"])
                node_body += f"""<div class="category-card {card_class}"><a href="{tlf_slug}">
  <h3>{html.escape(short_name(tlf["name"]))}</h3>
</a></div>\n"""

            for cat_name, cat_data in categories.items():
                cat_slug = make_slug(section, node_key, cat_name)
                count = len(cat_data["entries"])
                display = cat_name.replace("-", " ").replace("_", " ").title()
                node_body += f"""<div class="category-card {card_class}"><a href="{cat_slug}">
  <h3>{html.escape(display)}</h3>
  <div class="count">{count} {"entry" if count == 1 else "entries"}</div>
</a></div>\n"""

            node_body += "</div>\n"
            (OUT / node_slug).write_text(page(f"{node_display} — {section.title()}", node_body, section.title()), encoding="utf-8")
            total_pages += 1

            # Top-level file pages
            for tlf in top_files:
                tlf_slug = make_slug(section, node_key, tlf["stem"])
                _wiki_link_source = f"{section}/{node_key}/{tlf['stem']}"
                content_html = md_to_html(tlf["content"])
                badge = f'<span class="section-badge {section}">{section} &middot; {html.escape(node_display)}</span>\n'
                back = f'<div class="back-link"><a href="{node_slug}">&larr; {html.escape(node_display)}</a></div>'
                (OUT / tlf_slug).write_text(page(tlf["name"], badge + back + content_html, section.title()), encoding="utf-8")
                total_pages += 1

            # Category pages and entry pages
            for cat_name, cat_data in categories.items():
                display_name = cat_name.replace("-", " ").replace("_", " ").title()
                cat_slug = make_slug(section, node_key, cat_name)

                # Companion link
                companion_link = ""
                if cat_name in companion_categories and companion_categories[cat_name]["entries"]:
                    comp_slug = make_slug(companion_section, node_key, cat_name)
                    comp_count = len(companion_categories[cat_name]["entries"])
                    companion_link = f'<div class="companion-link">See also: <a href="{comp_slug}">{companion_section.title()} &rarr; {html.escape(display_name)}</a> ({comp_count} entries)</div>\n'

                badge = f'<span class="section-badge {section}">{section} &middot; {html.escape(node_display)}</span>\n'
                back = f'<div class="back-link"><a href="{node_slug}">&larr; {html.escape(node_display)}</a></div>'

                if section in ("ontology", "phenomena") and node_key == "sts1" and cat_name == "cards":
                    cat_html = render_faceted_cards(cat_data["entries"], section, node_key, cat_name, companion_link)
                else:
                    cat_html = f'<h2>{html.escape(display_name)}</h2>\n'
                    cat_html += companion_link
                    cat_html += '<div class="entry-grid">\n'
                    for entry in cat_data["entries"]:
                        entry_slug = make_slug(section, node_key, cat_name, entry["stem"])
                        cat_html += f'<a href="{entry_slug}">{html.escape(short_name(entry["name"]))}</a>\n'
                    cat_html += '</div>\n'

                (OUT / cat_slug).write_text(page(f"{display_name} — {section.title()}", badge + back + cat_html, section.title()), encoding="utf-8")
                total_pages += 1

                for entry in cat_data["entries"]:
                    entry_slug = make_slug(section, node_key, cat_name, entry["stem"])
                    _wiki_link_source = f"{section}/{node_key}/{cat_name}/{entry['stem']}"
                    content_html = md_to_html(entry["content"])

                    companion_entry_link = ""
                    if cat_name in companion_categories:
                        for ce in companion_categories[cat_name]["entries"]:
                            if ce["stem"] == entry["stem"]:
                                ce_slug = make_slug(companion_section, node_key, cat_name, ce["stem"])
                                label = "View strategy" if section == "ontology" else "View facts"
                                companion_entry_link = f'<div class="companion-link">{label}: <a href="{ce_slug}">{companion_section.title()} &rarr; {html.escape(short_name(ce["name"]))}</a></div>\n'
                                break

                    badge = f'<span class="section-badge {section}">{section} &middot; {html.escape(node_display)}</span>\n'
                    back = f'<div class="back-link"><a href="{cat_slug}">&larr; {html.escape(display_name)}</a></div>'
                    (OUT / entry_slug).write_text(page(entry["name"], badge + back + companion_entry_link + content_html, section.title()), encoding="utf-8")
                    total_pages += 1

    # ── Changelog ──
    entries = git_changelog()
    if entries:
        changelog_body = ""
        for entry in entries:
            diff_html = format_diff_html(entry["diff_lines"])
            changelog_body += f"""
<div class="changelog-entry">
  <div class="changelog-header" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">
    <div>
      <div class="changelog-msg">{html.escape(entry['message'])}</div>
      <div class="changelog-sha">{entry['sha']}</div>
    </div>
    <div class="changelog-date">{entry['date']}</div>
  </div>
  <div class="changelog-diff" style="display:none">
    {diff_html}
  </div>
</div>"""
    else:
        changelog_body = '<div class="empty-state">No knowledge changes committed yet.</div>'

    (OUT / "changelog.html").write_text(page("Changelog", changelog_body, "Changelog"), encoding="utf-8")
    total_pages += 1

    # ── CNAME for GitHub Pages ──
    (OUT / "CNAME").write_text("claudeslaysthespire.org", encoding="utf-8")

    # Summary
    for section, nodes in all_sections.items():
        for node_key, node_data in nodes.items():
            entry_count = sum(len(c["entries"]) for c in node_data["categories"].values()) + len(node_data["top_level_files"])
            print(f"  {section}/{node_key}: {len(node_data['categories'])} categories, {entry_count} entries")
    print(f"Built {total_pages} pages")
    print(f"Output: {OUT}")

    # ── Wiki-link validation ──
    if _broken_links:
        lines = [f"{src or '?'}\t[[{link}]]\t{href}" for src, link, href in _broken_links]
        (OUT / "broken-links.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        unique = {}
        for src, link, href in _broken_links:
            unique.setdefault(link, []).append(src or "?")
        print(f"\n  WARNING: {len(_broken_links)} broken wiki-link occurrence(s) across "
              f"{len(unique)} unique missing target(s):")
        for link in sorted(unique):
            srcs = unique[link]
            print(f"    [[{link}]]  ({len(srcs)}x, e.g. {srcs[0]})")
        print(f"  Full list: {OUT / 'broken-links.txt'}")
        if strict:
            raise SystemExit(f"Build failed: {len(_broken_links)} broken wiki-link(s) (strict mode)")
    else:
        print("\n  Wiki-links: all targets resolve")


if __name__ == "__main__":
    # Link validation is warn-only by default so a known broken-link backlog
    # never breaks the build. Opt into hard-fail with STS_STRICT_LINKS=1.
    build(strict=os.environ.get("STS_STRICT_LINKS") == "1")
