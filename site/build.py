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

def resolve_wiki_link(match):
    """Convert [[category/Name]] to an HTML link pointing to the ontology page."""
    full = match.group(1)
    if "/" in full:
        category, name = full.split("/", 1)
        slug = name.lower().replace(" ", "-").replace("'", "").replace(".", "")
        slug = re.sub(r'[^a-z0-9-]', '', slug)
        href = f"ontology-{category}-{slug}.html"
        return f'<a href="{href}" class="wiki-link">{html.escape(name)}</a>'
    return f'<code>{html.escape(full)}</code>'


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
    # Wiki-links: [[category/Name]] → resolved HTML links
    text = re.sub(r'\[\[([^\]]+)\]\]', resolve_wiki_link, text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
    return text


# ── Git history ──────────────────────────────────────────────────────

def git_changelog(max_entries=50):
    """Get commits that touched ontology/, heuristics/, or agents/ with diffs."""
    try:
        result = subprocess.run(
            ["git", "log", f"--max-count={max_entries}", "--pretty=format:%H|%ai|%s",
             "--diff-filter=ACDMR", "-p", "--",
             "ontology/", "heuristics/", "agents/", "AGENTS.md"],
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
  --heuristics: #f59e0b;
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
.site-subtitle {
  font-size: 16px;
  color: var(--text-dim);
  margin-bottom: 32px;
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
  padding: 20px;
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
        ("ontology.html", "Ontology"),
        ("heuristics.html", "Heuristics"),
        ("knowledge-system.html", "Knowledge System"),
        ("philosophy.html", "Philosophy"),
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
<title>{html.escape(title)} — Claude Slays the Spire</title>
<script async src="https://plausible.io/js/pa-DmrspWebBN8Lfq1qPfK3Z.js"></script>
<script>window.plausible=window.plausible||function(){{(plausible.q=plausible.q||[]).push(arguments)}},plausible.init=plausible.init||function(i){{plausible.o=i||{{}}}};plausible.init()</script>
<style>{STYLES}</style>
</head>
<body>
<h1>Claude Slays the Spire</h1>
<div class="site-subtitle">An AI learns to play Slay the Spire, and you can watch it happen.</div>
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


def make_slug(section, category, entry_stem=None):
    """Generate the output HTML filename.

    ontology-cards.html, ontology-cards-bash.html, heuristics-enemies-jaw-worm.html
    """
    if entry_stem:
        return f"{section}-{category}-{entry_stem}.html"
    return f"{section}-{category}.html"


# ── Run stats ─────────────────────────────────────────────────────

def load_run_stats(root):
    """Load run statistics from data/run_stats.json."""
    stats_file = root / "data" / "run_stats.json"
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

    # Twitch embed
    twitch_html = f"""
<div style="margin: 24px 0 32px; border-radius: 8px; overflow: hidden; border: 1px solid var(--border);">
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
    <p><strong>Model:</strong> Claude Opus 4.6 via Claude Code</p>
    <p><strong>Character:</strong> {char_name}, Ascension {run_stats.get('best_ascension', 0)}</p>
    <p><strong>Interface:</strong> <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=2131373661">CommunicationMod</a> (stdin/stdout JSON)</p>
  </div>
  <div class="state-card">
    <h3>The Approach</h3>
    <p>The agent maintains a structured <a href="knowledge-system.html">knowledge system</a> split into
    <a href="ontology.html">ontology</a> (facts about the game) and
    <a href="heuristics.html">heuristics</a> (strategy for navigating it).
    It reads, reasons, plays, and writes back what it learns.</p>
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
        _bf = _s["best_floor"] if _s else 0
        if _w > 0:
            _jcards.append(
                '<div class="journey-card completed">'
                '<div class="journey-badge">A0 COMPLETE</div>'
                f'<div class="journey-name">{_dn}</div>'
                f'<div class="journey-stats">{_w} wins &middot; Best floor {_bf}</div>'
                '</div>')
        elif _cur:
            _jcards.append(
                '<div class="journey-card active">'
                '<div class="journey-badge">NOW PLAYING</div>'
                f'<div class="journey-name">{_dn}</div>'
                f'<div class="journey-stats">Ascension {run_stats.get("best_ascension", 0)}</div>'
                '</div>')
    journey_html = ""
    if _jcards:
        journey_html = '<h2>Journey</h2>\n<div class="journey-grid">\n' + '\n'.join(_jcards) + '\n</div>\n'

    # Intro
    intro_html = """
<div style="margin-bottom: 40px;">
<p>
Claude plays <a href="https://store.steampowered.com/app/646570/Slay_the_Spire/">Slay the Spire</a>,
makes decisions one at a time with explicit reasoning, and reviews its own runs to figure out what
went wrong. No hardcoded strategy. Everything it knows is recorded in a structured
<a href="knowledge-system.html">knowledge system</a> that grows over time.
</p>

<p>
The <a href="ontology.html">Ontology</a> is the complete factual database of the game &mdash; every
card, enemy, relic, and mechanic. The <a href="heuristics.html">Heuristics</a> are strategic
guidance accumulated from gameplay. The <a href="changelog.html">Changelog</a> shows what changed and when.
</p>
</div>
"""

    # Knowledge sections preview
    sections_html = '<h2>Knowledge</h2>\n<div class="category-grid">\n'

    # Ontology card
    sections_html += f"""<div class="category-card ontology-card"><a href="ontology.html">
  <h3>Ontology</h3>
  <div class="count">{ont_entries} entries &mdash; facts about the game</div>
</a></div>\n"""

    # Heuristics card
    sections_html += f"""<div class="category-card heuristics-card"><a href="heuristics.html">
  <h3>Heuristics</h3>
  <div class="count">{heur_entries} entries &mdash; strategy and guidance</div>
</a></div>\n"""

    sections_html += "</div>\n"

    return twitch_html + stats_html + journey_html + intro_html + sections_html


# ── Build ────────────────────────────────────────────────────────────

def build():
    # Clean output
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # Discover content
    ont_dir = ROOT / "ontology"
    heur_dir = ROOT / "heuristics"
    ont_categories, ont_top = discover_content(ont_dir)
    heur_categories, heur_top = discover_content(heur_dir)

    run_stats = load_run_stats(ROOT)
    total_pages = 0

    # ── Index page ──
    index_body = build_landing(ont_categories, heur_categories, run_stats)
    (OUT / "index.html").write_text(page("Home", index_body, "Home"), encoding="utf-8")
    total_pages += 1

    # ── Build both sections ──
    for section, categories, top_files, card_class, description in [
        ("ontology", ont_categories, ont_top, "ontology-card",
         "The complete factual database of Slay the Spire. Every card, enemy, relic, potion, event, boss, buff, debuff, encounter, and game rule. Browse it like a wiki."),
        ("heuristics", heur_categories, heur_top, "heuristics-card",
         "Strategic guidance accumulated from gameplay and analysis. How to fight each enemy, when to play each card, which relics to prioritize. These are provisional &mdash; they improve over time."),
    ]:
        # Section index page
        section_body = build_section_index(section, section, categories, top_files, card_class, description)
        (OUT / f"{section}.html").write_text(page(section.title(), section_body, section.title()), encoding="utf-8")
        total_pages += 1

        # Top-level files
        for tlf in top_files:
            slug = f"{section}-{tlf['stem']}.html"
            content_html = md_to_html(tlf["content"])
            badge = f'<span class="section-badge {section}">{section}</span>\n'
            back_link = f'<div class="back-link"><a href="{section}.html">&larr; Back to {section}</a></div>'
            single_page = page(tlf["name"], badge + back_link + content_html, section.title())
            (OUT / slug).write_text(single_page, encoding="utf-8")
            total_pages += 1

        # Category pages and individual entry pages
        for cat_name, cat_data in categories.items():
            display_name = cat_name.replace("-", " ").replace("_", " ").title()
            cat_slug = make_slug(section, cat_name)

            # Companion section link
            companion_section = "heuristics" if section == "ontology" else "ontology"
            companion_categories = heur_categories if section == "ontology" else ont_categories
            companion_link = ""
            if cat_name in companion_categories and companion_categories[cat_name]["entries"]:
                companion_slug = make_slug(companion_section, cat_name)
                companion_count = len(companion_categories[cat_name]["entries"])
                companion_link = f'<div class="companion-link">See also: <a href="{companion_slug}">{companion_section.title()} &rarr; {html.escape(display_name)}</a> ({companion_count} entries)</div>\n'

            badge = f'<span class="section-badge {section}">{section}</span>\n'
            back_link = f'<div class="back-link"><a href="{section}.html">&larr; {section.title()}</a></div>'

            # Category page: tile grid of all entries
            cat_html = f'<h2>{html.escape(display_name)}</h2>\n'
            cat_html += companion_link
            cat_html += '<div class="entry-grid">\n'
            for entry in cat_data["entries"]:
                entry_slug = make_slug(section, cat_name, entry["stem"])
                cat_html += f'<a href="{entry_slug}">{html.escape(short_name(entry["name"]))}</a>\n'
            cat_html += '</div>\n'

            cat_page = page(f"{display_name} — {section.title()}", badge + back_link + cat_html, section.title())
            (OUT / cat_slug).write_text(cat_page, encoding="utf-8")
            total_pages += 1

            # Individual entry pages
            for entry in cat_data["entries"]:
                entry_slug = make_slug(section, cat_name, entry["stem"])
                content_html = md_to_html(entry["content"])

                # Link to companion entry if it exists
                companion_entry_link = ""
                if cat_name in companion_categories:
                    for ce in companion_categories[cat_name]["entries"]:
                        if ce["stem"] == entry["stem"]:
                            ce_slug = make_slug(companion_section, cat_name, ce["stem"])
                            label = "View strategy" if section == "ontology" else "View facts"
                            companion_entry_link = f'<div class="companion-link">{label}: <a href="{ce_slug}">{companion_section.title()} &rarr; {html.escape(short_name(ce["name"]))}</a></div>\n'
                            break

                badge = f'<span class="section-badge {section}">{section}</span>\n'
                back_link = f'<div class="back-link"><a href="{cat_slug}">&larr; Back to {html.escape(display_name)}</a></div>'
                entry_page = page(entry["name"], badge + back_link + companion_entry_link + content_html, section.title())
                (OUT / entry_slug).write_text(entry_page, encoding="utf-8")
                total_pages += 1

    # ── Knowledge System page ──
    ks_path = Path(__file__).parent / "knowledge-system.md"
    if ks_path.exists():
        ks_content = ks_path.read_text(encoding="utf-8")
        ks_html = md_to_html(ks_content)
        (OUT / "knowledge-system.html").write_text(
            page("Knowledge System", ks_html, "Knowledge System"), encoding="utf-8")
        total_pages += 1

    # ── Philosophy page ──
    phil_path = Path(__file__).parent / "philosophy.md"
    if phil_path.exists():
        phil_content = phil_path.read_text(encoding="utf-8")
        phil_html = md_to_html(phil_content)
        (OUT / "philosophy.html").write_text(page("Philosophy", phil_html, "Philosophy"), encoding="utf-8")
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

    ont_total = sum(len(c["entries"]) for c in ont_categories.values()) + len(ont_top)
    heur_total = sum(len(c["entries"]) for c in heur_categories.values()) + len(heur_top)
    print(f"Built {total_pages} pages")
    print(f"  Ontology: {len(ont_categories)} categories, {ont_total} entries")
    print(f"  Heuristics: {len(heur_categories)} categories, {heur_total} entries")
    print(f"Output: {OUT}")


if __name__ == "__main__":
    build()
