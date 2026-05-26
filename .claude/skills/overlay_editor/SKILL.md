---
description: Edit the STS1 OBS overlay. Use when the user asks to change the overlay layout, styling, panels, tiles, or content.
---

## Overlay Editor

The STS1 overlay is a single HTML file at `games/sts1/overlay/index.html`. It's an OBS browser source at 1920x1080.

### Naming conventions

- **Sidebar** (`.sidebar`) — right bar, full height. Contains header, reasoning log, floor graph.
- **Bottom bar** (`.bottom-bar`) — left bottom strip. Cycles between three **panels** on a 30s timer.
- **Panel** (`.panel`) — a cycling view in the bottom bar: gameplay, context, or strategy panel.
- **Tile** (`.tile`) — an individual content block within a panel. Each tile has a CSS class like `.tile.overview-tile`, `.tile.feed-tile`, etc.

CSS classes follow this hierarchy: `.bottom-bar > .panel > .tile`.

### Layout

- **Sidebar** (right, 420px, full height): header + reasoning log + floor graph ("Previous Runs")
- **Bottom bar** (left, 1500x236px): cycles between three panels with a countdown bar
  - **Gameplay panel** (`#panelGameplay`): actions tile + deck tile
  - **Context panel** (`#panelContext`): overview tile | playbook tile | run history tile | notes tile
  - **Strategy panel** (`#panelStrategy`): latest strategy reasoning (auto-fits font 16px→9px, force-switches on new think() event)
- **Agent panel** (fullscreen overlay, hidden unless analyst/steward is running)

### Dynamic sizing

- **Deck tile**: font scales by unique card count (18px at ~10 cards, 12px at ~35+). Set in JS `updateDeck()`, not CSS.
- **Strategy tile**: auto-fits text from 16px down to 9px via `fitStrategyText()`.

### Editable content files

- `data/overview.md` — overview tile text (refreshes every 30s)
- `data/notes.md` — notes tile text (refreshes every 30s)

### Data sources

The overlay connects to `stream.py` which serves:
- **WebSocket** `ws://127.0.0.1:3001` — real-time state, decisions, feed events
- **HTTP** `http://127.0.0.1:3002` — REST endpoints:
  - `GET /playbook-stats` — entry counts per category
  - `GET /character-stats` — per-class run/win/best breakdown from run log filenames
  - `GET /overview` — reads `data/overview.md`
  - `GET /notes` — reads `data/notes.md`
  - `GET /run-history` — last 20 floor results for sparkline graph
  - `GET /reload` — broadcasts reload to all connected overlay clients

### Visual guidelines

- Minimum text contrast: `#888` or above. Never use dark grays (#444, #555, #666) — all information on screen is meant to be visible.
- "Tiniest bit" size changes = 1px, not 2px. The user is precise about visual adjustments.
- Don't vertically center tile content by default — user tried it and reverted.

### After making changes

Always reload the overlay by running:
```
curl -s http://127.0.0.1:3002/reload
```

If stream.py itself was modified, restart it (it auto-kills the previous instance via PID file):
```
python games/sts1/stream.py
```
Then wait a few seconds and curl `/reload`.
