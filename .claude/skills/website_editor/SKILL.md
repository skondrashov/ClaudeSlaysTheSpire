---
description: Edit the claudeslaysthespire.org website. Use when the user asks to change website pages, add content, or update the site build.
---

## Website Editor

The STS1 website is a static site built from markdown + a Python build script. Lives in its own git repo at `github.com/skondrashov/ClaudeSlaysTheSpire`.

### Structure

- **Build script**: `games/sts1/site/build.py` — converts playbook markdown to static HTML
- **Output**: `games/sts1/site/out/` — generated HTML files, deployed via GitHub Actions
- **Playbook source**: `games/sts1/playbook/` — markdown files organized by category

### How the build works

`build.py` does everything:
1. Discovers playbook structure (categories as subdirs, entries as .md files)
2. Converts markdown to HTML with `md_to_html()` (custom, no dependencies)
3. Generates: index, playbook index, category pages, individual entry pages, changelog, human advice
4. Changelog comes from git history of `playbook/`, `agents/`, `AGENTS.md`

### Page template

All pages use the `page(title, content, active)` function which wraps content in:
- Standard CSS (dark theme, vars in `:root`)
- Nav bar with tabs (currently: Home, Playbook, Human Advice, Changelog)
- Footer with GitHub + Reddit links
- Plausible analytics

### Adding a new page

1. Add a nav entry in the `nav_items` list inside `page()`
2. Create the page content (either from a .md file or inline HTML)
3. Write it to `OUT / "filename.html"` using `page(title, content, "Nav Label")`
4. Increment `total_pages`

### After making changes

Rebuild the site:
```
cd games/sts1 && python site/build.py
```

To deploy: commit the `site/out/` changes and push to the ClaudeSlaysTheSpire repo. GitHub Actions handles deployment.

### Key conventions

- All styles are inline in `STYLES` constant — no external CSS
- Markdown conversion is custom (`md_to_html`, `inline`) — supports headers, lists, bold, italic, code, links, tables, code blocks
- Dark theme: `--bg: #0a0a0e`, `--accent: #c084fc` (purple)
- Mobile-responsive with `@media` queries for grids
