"""
Build static site from playbook markdown files.
Generates HTML pages + a changelog with diffs from git history.

Usage: python site/build.py
Output: site/out/
"""

import os, re, subprocess, html, shutil
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
OUT = ROOT / "site" / "out"
CONTENT_DIRS = ["playbook"]

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
    """Inline markdown: bold, italic, code, links."""
    text = html.escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
    return text


# ── Git history ──────────────────────────────────────────────────────

def git_changelog(max_entries=50):
    """Get commits that touched playbook/ or agents/ with diffs."""
    try:
        result = subprocess.run(
            ["git", "log", f"--max-count={max_entries}", "--pretty=format:%H|%ai|%s",
             "--diff-filter=ACDMR", "-p", "--",
             "playbook/", "agents/", "AGENTS.md"],
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
            # Extract filename
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

/* File list */
.file-list { list-style: none; margin: 0; padding: 0; }
.file-list li {
  border-bottom: 1px solid var(--border);
  padding: 14px 0;
}
.file-list a {
  font-size: 18px;
  font-weight: 600;
}
.file-meta {
  font-size: 13px;
  color: var(--text-dim);
  margin-top: 4px;
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
        ("playbook.html", "Playbook"),
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


# ── Playbook helpers ────────────────────────────────────────────────

def discover_playbook(playbook_dir):
    """Discover playbook structure: categories (subdirs) and top-level files.

    Returns:
        categories: dict of category_name -> {
            "index_content": str (markdown from _index.md),
            "entries": list of {"name": str, "stem": str, "content": str}
        }
        top_level_files: list of {"name": str, "stem": str, "content": str}
    """
    categories = {}
    top_level_files = []

    if not playbook_dir.exists():
        return categories, top_level_files

    # Top-level .md files (mechanics.md, strategy.md, etc.)
    for f in sorted(playbook_dir.glob("*.md")):
        content = f.read_text(encoding="utf-8")
        # Extract title from first H1 if present, else derive from filename
        title_match = re.match(r'^#\s+(.+)', content.strip())
        name = title_match.group(1) if title_match else f.stem.replace("-", " ").replace("_", " ").title()
        top_level_files.append({
            "name": name,
            "stem": f.stem,
            "content": content,
        })

    # Subdirectories (cards/, enemies/, bosses/, etc.)
    for d in sorted(playbook_dir.iterdir()):
        if not d.is_dir():
            continue
        cat_name = d.name

        # Read _index.md for the category
        index_file = d / "_index.md"
        index_content = ""
        if index_file.exists():
            index_content = index_file.read_text(encoding="utf-8")

        # Read all entry files (excluding _index.md)
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

        categories[cat_name] = {
            "index_content": index_content,
            "entries": entries,
        }

    return categories, top_level_files


def short_name(full_name):
    """Extract just the display name before any parenthetical stats.

    'Bash (2E, Attack, 8 damage...)' -> 'Bash'
    'Jaw Worm (hallway, Act 1, HP: ~40-44)' -> 'Jaw Worm'
    """
    idx = full_name.find(" (")
    if idx > 0:
        return full_name[:idx]
    return full_name


def render_category_page(index_md, cat_name):
    """Render category _index.md as section headers + tile grids.

    Instead of rendering markdown lists as <ul><li>, this parses the
    section structure and renders link lists as entry-grid tiles.
    """
    lines = index_md.split("\n")
    html_parts = []
    pending_links = []

    def flush_grid():
        nonlocal pending_links
        if pending_links:
            html_parts.append('<div class="entry-grid">')
            for text, href in pending_links:
                html_parts.append(f'<a href="{href}">{html.escape(text)}</a>')
            html_parts.append('</div>')
            pending_links = []

    for line in lines:
        stripped = line.strip()

        # Headers
        if m := re.match(r'^(#{1,6})\s+(.+)', stripped):
            flush_grid()
            level = len(m.group(1))
            content = inline(m.group(2))
            slug = re.sub(r'[^a-z0-9]+', '-', m.group(2).lower()).strip('-')
            html_parts.append(f'<h{level} id="{slug}">{content}</h{level}>')

        # List items with links -> tile entries
        elif (stripped.startswith("- ") or stripped.startswith("* ")):
            item = stripped[2:]
            if link_m := re.match(r'\[(.+?)\]\((.+?)\)', item):
                link_text = link_m.group(1)
                link_target = link_m.group(2)
                if link_target.endswith(".md"):
                    entry_stem = link_target[:-3]
                    href = make_slug(cat_name, entry_stem)
                    pending_links.append((link_text, href))

    flush_grid()
    return "\n".join(html_parts)


def make_slug(category, entry_stem=None):
    """Generate the output HTML filename for a playbook page.

    playbook-cards.html, playbook-cards-headbutt.html, playbook-mechanics.html
    """
    if entry_stem:
        return f"playbook-{category}-{entry_stem}.html"
    return f"playbook-{category}.html"


# ── Run stats from analyst/run_log.md ───────────────────────────────

def parse_run_log(root):
    """Parse analyst/run_log.md to extract run statistics."""
    run_log = root / "analyst" / "run_log.md"
    stats = {"total_runs": 0, "boss_kills": 0, "best_floor": 0, "deaths": 0}

    if not run_log.exists():
        return stats

    content = run_log.read_text(encoding="utf-8")
    for line in content.split("\n"):
        if not line.startswith("## Run "):
            continue
        stats["total_runs"] += 1

        # Count boss victories (e.g., "Victory (Guardian)")
        if "Victory" in line:
            stats["boss_kills"] += line.count("Victory")

        # Count deaths
        if "Death" in line:
            stats["deaths"] += 1

        # Extract floor numbers from "Death Floor N" or "Death Floor N ("
        for m in re.finditer(r'Death Floor (\d+)', line):
            floor = int(m.group(1))
            stats["best_floor"] = max(stats["best_floor"], floor)

    return stats


# ── Landing page ────────────────────────────────────────────────────

def build_landing(categories, top_level_files, run_stats):
    """Build the index/landing page content."""

    total_entries = sum(len(c["entries"]) for c in categories.values())

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
  <div class="stat"><div class="stat-value">{run_stats['boss_kills']}</div><div class="stat-label">Boss Kills</div></div>
  <div class="stat"><div class="stat-value">{run_stats['best_floor']}</div><div class="stat-label">Best Floor</div></div>
  <div class="stat"><div class="stat-value">{total_entries}</div><div class="stat-label">Playbook Entries</div></div>
</div>

<div class="state-details">
  <div class="state-card">
    <h3>System</h3>
    <p><strong>Model:</strong> Claude Sonnet 4 via Claude Code</p>
    <p><strong>Character:</strong> Ironclad, Ascension 0</p>
    <p><strong>Interface:</strong> <a href="https://steamcommunity.com/sharedfiles/filedetails/?id=2131373661">CommunicationMod</a> (stdin/stdout JSON)</p>
  </div>
  <div class="state-card">
    <h3>The Loop</h3>
    <p>A <strong>player agent</strong> plays a run with visible reasoning. When it ends, an <strong>analyst agent</strong> reviews what went wrong and updates the <a href="playbook.html">playbook</a>. Next run reads the updated knowledge. Repeat.</p>
  </div>
</div>
"""

    # Condensed intro
    intro_html = """
<div style="margin-bottom: 40px;">
<p>
Claude plays <a href="https://store.steampowered.com/app/646570/Slay_the_Spire/">Slay the Spire</a>,
makes decisions one at a time with explicit reasoning, and then reviews its own runs afterward to
figure out what went wrong. No hardcoded strategy. Everything it knows comes from playing and
self-review.
</p>

<p>
The <a href="playbook.html">Playbook</a> is everything Claude has learned so far &mdash; card
evaluations, enemy patterns, boss strategies, event guides. The
<a href="changelog.html">Changelog</a> shows every update: what changed, what was learned, and when.
</p>
</div>
"""

    # Playbook categories listing
    content_html = ""
    if categories or top_level_files:
        content_html += '<h2>Playbook</h2>\n<div class="category-grid">\n'

        # Top-level playbook files first
        for tlf in top_level_files:
            slug = make_slug(tlf["stem"])
            content_html += f"""<div class="category-card"><a href="{slug}">
  <h3>{html.escape(tlf["name"])}</h3>
</a></div>\n"""

        # Category cards
        for cat_name, cat_data in categories.items():
            slug = make_slug(cat_name)
            count = len(cat_data["entries"])
            display_name = cat_name.replace("-", " ").replace("_", " ").title()
            content_html += f"""<div class="category-card"><a href="{slug}">
  <h3>{html.escape(display_name)}</h3>
  <div class="count">{count} {"entry" if count == 1 else "entries"}</div>
</a></div>\n"""

        content_html += "</div>\n"

    return twitch_html + stats_html + intro_html + content_html


# ── Build ────────────────────────────────────────────────────────────

def build():
    # Clean output
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # Discover playbook structure
    playbook_dir = ROOT / "playbook"
    categories, top_level_files = discover_playbook(playbook_dir)

    run_stats = parse_run_log(ROOT)
    total_pages = 0

    # ── Index page ──
    index_body = build_landing(categories, top_level_files, run_stats)
    (OUT / "index.html").write_text(page("Home", index_body, "Home"), encoding="utf-8")
    total_pages += 1

    # ── Playbook index page ──
    playbook_body = "<h2>Playbook</h2>\n"
    playbook_body += "<p>Everything Claude has learned about Slay the Spire, organized by category.</p>\n"

    # Top-level files section
    if top_level_files:
        playbook_body += '<div style="margin: 24px 0;">\n'
        for tlf in top_level_files:
            slug = make_slug(tlf["stem"])
            playbook_body += f'<h3><a href="{slug}">{html.escape(tlf["name"])}</a></h3>\n'
        playbook_body += "</div>\n"

    # Category sections
    for cat_name, cat_data in categories.items():
        slug = make_slug(cat_name)
        display_name = cat_name.replace("-", " ").replace("_", " ").title()
        count = len(cat_data["entries"])
        playbook_body += f'<h3><a href="{slug}">{html.escape(display_name)}</a> <span style="color:var(--text-dim);font-size:14px;font-weight:400;">({count})</span></h3>\n'
        playbook_body += '<div class="entry-grid">\n'
        for entry in cat_data["entries"]:
            entry_slug = make_slug(cat_name, entry["stem"])
            playbook_body += f'<a href="{entry_slug}">{html.escape(short_name(entry["name"]))}</a>\n'
        playbook_body += "</div>\n"

    if not categories and not top_level_files:
        playbook_body = '<div class="empty-state">Playbook is empty. Strategy, cards, and mechanics will appear here as Claude learns.</div>'

    (OUT / "playbook.html").write_text(page("Playbook", playbook_body, "Playbook"), encoding="utf-8")
    total_pages += 1

    # ── Top-level playbook file pages (mechanics, strategy, etc.) ──
    for tlf in top_level_files:
        slug = make_slug(tlf["stem"])
        content_html = md_to_html(tlf["content"])
        back_link = '<div class="back-link"><a href="playbook.html">&larr; Back to playbook</a></div>'
        single_page = page(tlf["name"], back_link + content_html, "Playbook")
        (OUT / slug).write_text(single_page, encoding="utf-8")
        total_pages += 1

    # ── Category pages and individual entry pages ──
    for cat_name, cat_data in categories.items():
        display_name = cat_name.replace("-", " ").replace("_", " ").title()

        # Category page: render the _index.md content with links rewritten
        cat_slug = make_slug(cat_name)
        back_link = '<div class="back-link"><a href="playbook.html">&larr; Back to playbook</a></div>'

        # Render category page as tile grids instead of bullet lists
        cat_html = render_category_page(cat_data["index_content"], cat_name)
        cat_page = page(display_name, back_link + cat_html, "Playbook")
        (OUT / cat_slug).write_text(cat_page, encoding="utf-8")
        total_pages += 1

        # Individual entry pages
        for entry in cat_data["entries"]:
            entry_slug = make_slug(cat_name, entry["stem"])
            content_html = md_to_html(entry["content"])
            back_link = f'<div class="back-link"><a href="{cat_slug}">&larr; Back to {html.escape(display_name)}</a></div>'
            entry_page = page(entry["name"], back_link + content_html, "Playbook")
            (OUT / entry_slug).write_text(entry_page, encoding="utf-8")
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
        changelog_body = '<div class="empty-state">No changes to playbook files yet.</div>'

    (OUT / "changelog.html").write_text(page("Changelog", changelog_body, "Changelog"), encoding="utf-8")
    total_pages += 1

    # ── CNAME for GitHub Pages ──
    (OUT / "CNAME").write_text("claudeslaysthespire.org", encoding="utf-8")

    print(f"Built {total_pages} pages (index, playbook, {len(top_level_files)} top-level, {sum(len(c['entries']) for c in categories.values())} entries across {len(categories)} categories, changelog)")
    print(f"Output: {OUT}")


if __name__ == "__main__":
    build()
