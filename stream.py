"""
Stream server: WebSocket broadcast for OBS overlay.

Watches game state and decisions, broadcasts to overlay clients.
Runs independently of the relay — connect overlay to ws://localhost:3001.

Also accepts HTTP POSTs from cmd.py to log reasoning:
  POST /decision  {"command": "play 1 0", "reasoning": "Kill before Ritual stacks"}
"""

import asyncio
import atexit
import json
import os
import re
import signal
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

try:
    import websockets
    import websockets.server
except ImportError:
    print("Install websockets: pip install websockets")
    raise

WS_PORT = 3001
HTTP_PORT = 3002
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
STATE_FILE = os.path.join(DATA_DIR, "last_state.json")
EVENT_LOG = os.path.join(DATA_DIR, "stream_events.jsonl")
STATS_FILE = os.path.join(DATA_DIR, "run_stats.json")
RUNS_DIR = os.path.join(DATA_DIR, "runs")
PID_FILE = os.path.join(DATA_DIR, "stream.pid")
PLAYBOOK_DIR = os.path.join(os.path.dirname(__file__), "playbook")

# Connected overlay clients
clients = set()

# Recent events for new clients (decisions/reasoning)
recent_events = []
MAX_RECENT = 20

# Separate feed for action entries (survives overlay refresh)
FEED_FILE = os.path.join(os.path.dirname(__file__), "data", "action_feed.json")
MAX_FEED = 30

def _load_feed():
    try:
        with open(FEED_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def _save_feed():
    os.makedirs(os.path.dirname(FEED_FILE), exist_ok=True)
    with open(FEED_FILE, "w") as f:
        json.dump(action_feed, f)

action_feed = _load_feed()

# Run stats — persisted to disk
def _load_stats():
    try:
        with open(STATS_FILE) as f:
            saved = json.load(f)
        # Merge with defaults so new fields don't break
        defaults = {"total_runs": 0, "wins": 0, "deaths": 0, "best_floor": 0, "best_ascension": 0,
                     "current_floor": 0, "current_hp": 0, "max_hp": 0, "current_class": "?",
                     "floor_history": []}
        defaults.update(saved)
        # Derive wins/deaths from floor_history (source of truth) to prevent
        # double-counting when stream.py restarts and re-hits GAME_OVER.
        # total_runs is kept separate — floor_history doesn't include early
        # runs that predate tracking (runs 0-80).
        fh = defaults.get("floor_history", [])
        if fh:
            defaults["wins"] = sum(1 for e in fh if e.get("victory"))
            defaults["deaths"] = defaults["total_runs"] - defaults["wins"]
            defaults["best_floor"] = max(e.get("floor", 0) for e in fh)
        return defaults
    except (FileNotFoundError, json.JSONDecodeError):
        return {"total_runs": 0, "wins": 0, "deaths": 0, "best_floor": 0, "best_ascension": 0,
                "current_floor": 0, "current_hp": 0, "max_hp": 0, "current_class": "?",
                "floor_history": []}

def _save_stats():
    os.makedirs(os.path.dirname(STATS_FILE), exist_ok=True)
    with open(STATS_FILE, "w") as f:
        json.dump(run_stats, f)

run_stats = _load_stats()


def _archive_run(run_number: int, victory: bool, floor: int, cls: str):
    """Archive current run's event log to data/runs/run_NNN.jsonl and reset."""
    os.makedirs(RUNS_DIR, exist_ok=True)
    result = "win" if victory else f"death_f{floor}"
    archive_name = f"run_{run_number:03d}_{cls.lower()}_{result}.jsonl"
    archive_path = os.path.join(RUNS_DIR, archive_name)

    try:
        if os.path.exists(EVENT_LOG) and os.path.getsize(EVENT_LOG) > 0:
            import shutil
            shutil.copy2(EVENT_LOG, archive_path)
            print(f"[stream] Archived run {run_number} → {archive_name}")
            # Clear the event log for the next run
            with open(EVENT_LOG, "w") as f:
                pass
        else:
            print(f"[stream] No events to archive for run {run_number}")
    except OSError as e:
        print(f"[stream] Archive error: {e}")


async def broadcast(event: dict):
    """Send event to all connected overlay clients."""
    recent_events.append(event)
    if len(recent_events) > MAX_RECENT:
        recent_events.pop(0)

    # Track feed-worthy events separately for persistence
    if event.get("type") in ("decision", "feed", "run_start", "run_end"):
        action_feed.append(event)
        if len(action_feed) > MAX_FEED:
            action_feed.pop(0)
        _save_feed()

    if clients:
        msg = json.dumps(event)
        await asyncio.gather(
            *[client.send(msg) for client in clients],
            return_exceptions=True,
        )


async def ws_handler(websocket):
    """Handle a new overlay WebSocket connection."""
    clients.add(websocket)
    print(f"[stream] Overlay connected ({len(clients)} clients)")
    try:
        # Send persistent feed to populate action panel + reasoning
        for event in action_feed:
            await websocket.send(json.dumps(event))
        # Send current stats
        await websocket.send(json.dumps({"type": "stats", **run_stats}))
        # Send agent mode state if active
        if agent_watch_path:
            await websocket.send(json.dumps({
                "type": "agent_mode",
                "active": True,
                "title": agent_watch_title or "ANALYSIS",
                "run_summary": agent_run_summary or "",
                "run_stats": dict(run_stats),
                "timestamp": time.time(),
            }))

        # Keep alive until disconnect
        async for _ in websocket:
            pass
    finally:
        clients.discard(websocket)
        print(f"[stream] Overlay disconnected ({len(clients)} clients)")


# No event queue needed — HTTP handlers call broadcast() directly via
# asyncio.run_coroutine_threadsafe (same pattern as /agent and /reload).


async def _broadcast_stats():
    """Broadcast current stats to all overlay clients."""
    await broadcast({"type": "stats", **run_stats})


async def state_watcher():
    """Watch last_state.json for changes, broadcast state updates."""
    last_mtime = 0
    last_floor = 0
    was_in_combat = False
    game_over_handled = False
    last_event_name = ""
    # Neow-based run counting: a new run is counted when Neow's event screen appears.
    # run_counted is False when in_game transitions true, set True on Neow detection.
    run_counted = False

    # Initialize was_in_game from current state so we don't
    # false-count a new run when stream.py restarts mid-game
    was_in_game = False
    try:
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE) as f:
                init_state = json.load(f)
            was_in_game = init_state.get("in_game", False)
            if was_in_game:
                init_gs = init_state.get("game_state", {})
                init_screen = init_gs.get("screen_type", "")
                print(f"[stream] Game already in progress on startup (floor {init_gs.get('floor', '?')}, screen {init_screen})")
                run_counted = True  # Don't count the in-progress run again
                if init_screen == "GAME_OVER":
                    game_over_handled = True  # Don't re-process game over on restart
    except Exception:
        pass

    while True:
        try:
            if os.path.exists(STATE_FILE):
                mtime = os.path.getmtime(STATE_FILE)
                if mtime > last_mtime:
                    last_mtime = mtime
                    with open(STATE_FILE) as f:
                        state = json.load(f)

                    gs = state.get("game_state", {})
                    in_game = state.get("in_game", False)

                    if in_game:
                        floor = gs.get("floor", 0)
                        hp = gs.get("current_hp", 0)
                        max_hp = gs.get("max_hp", 0)
                        gold = gs.get("gold", 0)
                        cls = gs.get("class", "?")
                        screen = gs.get("screen_type", "?")
                        phase = gs.get("room_phase", "?")
                        ss = gs.get("screen_state", {})

                        run_stats["current_floor"] = floor
                        run_stats["current_hp"] = hp
                        run_stats["max_hp"] = max_hp
                        run_stats["current_class"] = cls
                        current_asc = gs.get("ascension_level", 0)
                        if (current_asc, floor) > (run_stats.get("best_ascension", 0), run_stats["best_floor"]):
                            run_stats["best_floor"] = floor
                            run_stats["best_ascension"] = current_asc
                            _save_stats()
                            await _broadcast_stats()

                        # Detect new game session (in_game transitions true)
                        # Only reset run_counted if game_over was already handled
                        # (meaning we went through: game over → main menu → new run).
                        # This prevents in_game flickers during Neow from double-counting.
                        if not was_in_game:
                            if game_over_handled or not run_counted:
                                run_counted = False
                                game_over_handled = False
                                # Clear feed for the new run
                                action_feed.clear()
                                _save_feed()
                                recent_events.clear()

                        # Detect run start when Neow event appears
                        if (not run_counted
                                and screen == "EVENT"
                                and "neow" in ss.get("event_name", "").lower()):
                            run_counted = True
                            # Don't increment total_runs here — counters are derived
                            # from floor_history at GAME_OVER to prevent double-counting
                            await broadcast({
                                "type": "run_start",
                                "class": cls,
                                "run_number": run_stats["total_runs"] + 1,
                            })
                            await _broadcast_stats()

                        # Detect game over (only process once per run)
                        if screen == "GAME_OVER" and not game_over_handled:
                            game_over_handled = True
                            if not run_counted:
                                run_counted = True
                            victory = ss.get("victory", False)
                            # Track floor history for the graph
                            if "floor_history" not in run_stats:
                                run_stats["floor_history"] = []
                            seed = gs.get("seed", None)
                            asc = gs.get("ascension_level", 0)
                            # Dedupe: don't re-log same seed (each seed is unique per run)
                            already_logged = any(
                                e.get("seed") == seed and e.get("floor") == floor
                                for e in run_stats["floor_history"]
                            )
                            if not already_logged:
                                run_stats["total_runs"] += 1
                                run_stats["floor_history"].append({
                                    "floor": floor,
                                    "victory": victory,
                                    "seed": seed,
                                    "class": cls,
                                    "ascension": asc,
                                })
                            # Derive wins/deaths from floor_history (prevents double-count)
                            fh = run_stats["floor_history"]
                            run_stats["wins"] = sum(1 for e in fh if e.get("victory"))
                            run_stats["deaths"] = run_stats["total_runs"] - run_stats["wins"]
                            run_stats["best_floor"] = max((e.get("floor", 0) for e in fh), default=0)
                            _save_stats()
                            await broadcast({
                                "type": "run_end",
                                "victory": victory,
                                "floor": floor,
                                "stats": dict(run_stats),
                            })
                            await _broadcast_stats()
                            # Archive this run's event log
                            _archive_run(
                                run_stats["total_runs"], victory, floor, cls
                            )

                        # Detect event screen
                        if screen == "EVENT":
                            event_name = ss.get("event_name", "")
                            if event_name and event_name != last_event_name:
                                last_event_name = event_name
                                await broadcast({
                                    "type": "feed",
                                    "text": f"EVENT — {event_name}",
                                    "highlight": True,
                                    "timestamp": time.time(),
                                })
                        else:
                            last_event_name = ""

                        # Detect combat start
                        combat = gs.get("combat_state")
                        in_combat = combat is not None
                        if in_combat and not was_in_combat:
                            monsters = []
                            if combat:
                                for m in combat.get("monsters", []):
                                    if not m.get("is_gone"):
                                        monsters.append(m.get("name", "?"))
                            enemy_str = " + ".join(monsters) if monsters else "?"
                            await broadcast({
                                "type": "feed",
                                "text": f"COMBAT — {enemy_str}",
                                "highlight": True,
                                "timestamp": time.time(),
                            })
                        was_in_combat = in_combat

                        # Broadcast state
                        hand = []
                        if combat:
                            for c in combat.get("hand", []):
                                hand.append({"name": c.get("name", "?")})
                        enemies = []
                        if combat:
                            for m in combat.get("monsters", []):
                                if not m.get("is_gone"):
                                    enemies.append({"name": m.get("name"), "hp": m.get("current_hp"), "max_hp": m.get("max_hp"), "intent": m.get("intent")})
                        choices = gs.get("choice_list", [])

                        # Deck summary for overlay
                        deck = []
                        for c in gs.get("deck", []):
                            deck.append(c.get("name", "?"))

                        await broadcast({
                            "type": "state",
                            "floor": floor,
                            "hp": hp,
                            "max_hp": max_hp,
                            "gold": gold,
                            "screen": screen,
                            "phase": phase,
                            "class": cls,
                            "in_combat": combat is not None,
                            "enemies": enemies,
                            "hand": hand,
                            "choices": choices,
                            "deck": deck,
                        })

                    was_in_game = in_game

        except Exception as e:
            print(f"[stream] State watcher error: {e}")

        await asyncio.sleep(0.3)


async def event_consumer():
    """No-op — kept as placeholder. Events now go directly to broadcast()."""
    await asyncio.Event().wait()  # sleep forever


# ---------------------------------------------------------------------------
# Agent JSONL watcher — streams analyst/strategist output to overlay
# ---------------------------------------------------------------------------

agent_watch_path = None    # Path to JSONL file being watched
agent_watch_title = None   # Title shown on overlay (e.g., "POST-GAME ANALYSIS")
agent_watch_offset = 0     # Lines already processed
agent_run_summary = None   # Run summary text to show in bottom bar during agent mode


async def agent_watcher():
    """Watch an agent's JSONL conversation file and broadcast text to overlay."""
    global agent_watch_path, agent_watch_offset

    while True:
        if agent_watch_path and os.path.exists(agent_watch_path):
            try:
                with open(agent_watch_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                new_lines = lines[agent_watch_offset:]
                agent_watch_offset = len(lines)

                for line in new_lines:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue

                    entry_type = entry.get("type", "")
                    msg = entry.get("message", {})
                    if not isinstance(msg, dict):
                        continue
                    content = msg.get("content", "")

                    if entry_type == "assistant" and isinstance(content, list):
                        for block in content:
                            if block.get("type") == "text":
                                text = block.get("text", "").strip()
                                if text:
                                    await broadcast({
                                        "type": "agent_text",
                                        "text": text,
                                        "timestamp": time.time(),
                                    })
                            elif block.get("type") == "tool_use":
                                tool_name = block.get("name", "?")
                                tool_input = block.get("input", {})
                                # Show a brief summary of what the agent is doing
                                summary = _summarize_tool_use(tool_name, tool_input)
                                if summary:
                                    await broadcast({
                                        "type": "agent_tool",
                                        "tool": tool_name,
                                        "summary": summary,
                                        "timestamp": time.time(),
                                    })

            except Exception as e:
                print(f"[stream] Agent watcher error: {e}")

        await asyncio.sleep(0.5)


def _summarize_tool_use(tool_name: str, tool_input: dict) -> str:
    """Create a brief human-readable summary of a tool call."""
    if tool_name == "Read":
        path = tool_input.get("file_path", "?")
        fname = os.path.basename(path)
        return f"Reading {fname}"
    elif tool_name == "Edit":
        path = tool_input.get("file_path", "?")
        fname = os.path.basename(path)
        return f"Editing {fname}"
    elif tool_name == "Write":
        path = tool_input.get("file_path", "?")
        fname = os.path.basename(path)
        return f"Writing {fname}"
    elif tool_name == "Grep":
        pattern = tool_input.get("pattern", "?")
        return f'Searching for "{pattern[:40]}"'
    elif tool_name == "Glob":
        pattern = tool_input.get("pattern", "?")
        return f"Finding {pattern}"
    elif tool_name == "Bash":
        cmd = tool_input.get("command", "?")
        return f"Running: {cmd[:50]}"
    return ""


class DecisionHandler(BaseHTTPRequestHandler):
    """HTTP handler for decision posts from cmd.py."""

    def do_GET(self):
        if self.path == "/playbook-stats":
            # Count .md files in each playbook subdirectory (excluding _index.md)
            stats = {}
            try:
                for d in sorted(os.listdir(PLAYBOOK_DIR)):
                    full = os.path.join(PLAYBOOK_DIR, d)
                    if os.path.isdir(full):
                        count = sum(
                            1 for f in os.listdir(full)
                            if f.endswith(".md") and f != "_index.md"
                        )
                        stats[d] = count
            except FileNotFoundError:
                pass
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(stats).encode())
        elif self.path == "/run-history":
            # Return last 20 run floor results for the overlay graph
            history = run_stats.get("floor_history", [])[-20:]
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(history).encode())
        elif self.path == "/character-stats":
            # Per-character breakdown from run log filenames + floor_history
            # Build ascension lookup from floor_history (keyed by run number)
            asc_lookup = {}
            for entry in run_stats.get("floor_history", []):
                asc_lookup[entry.get("run")] = entry.get("ascension", 0)

            chars = {}
            seen_runs = set()
            pattern = re.compile(r"^run_(\d+)_(.+?)_(death_f(\d+)|win)\.jsonl$")
            try:
                for fname in sorted(os.listdir(RUNS_DIR)):
                    m = pattern.match(fname)
                    if not m:
                        continue
                    run_num = int(m.group(1))
                    if run_num in seen_runs:
                        continue  # dedupe: only count each run number once (keep first/lowest floor)
                    seen_runs.add(run_num)
                    cls = m.group(2).upper().replace(" ", "_")
                    is_win = m.group(3) == "win"
                    floor = int(m.group(4)) if m.group(4) else 0
                    asc = asc_lookup.get(run_num, 0)

                    if cls not in chars:
                        chars[cls] = {"runs": 0, "best_asc": 0, "best_win": False, "best_floor": 0, "best_count": 0}

                    chars[cls]["runs"] += 1
                    c = chars[cls]

                    # Compare: higher ascension > win > higher floor
                    cur = (asc, is_win, floor if not is_win else 999)
                    prev = (c["best_asc"], c["best_win"], c["best_floor"] if not c["best_win"] else 999)
                    if cur > prev:
                        c["best_asc"] = asc
                        c["best_win"] = is_win
                        c["best_floor"] = floor if not is_win else 0
                        c["best_count"] = 1
                    elif cur == prev:
                        c["best_count"] += 1
            except FileNotFoundError:
                pass
            total = sum(c["runs"] for c in chars.values())
            result = {"characters": chars, "total_runs": total}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
        elif self.path == "/overview":
            notes_path = os.path.join(DATA_DIR, "overview.md")
            try:
                with open(notes_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except FileNotFoundError:
                content = ""
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        elif self.path == "/notes":
            # Read static dev notes file
            notes_path = os.path.join(DATA_DIR, "notes.md")
            try:
                with open(notes_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except FileNotFoundError:
                content = "No dev notes yet."
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        elif self.path == "/reload":
            # Broadcast reload to all overlay clients
            if loop:
                asyncio.run_coroutine_threadsafe(broadcast({"type": "reload"}), loop)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/decision":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body)
                event = {
                    "type": "decision",
                    "command": data.get("command", ""),
                    "translated": data.get("translated", data.get("command", "")),
                    "reasoning": data.get("reasoning", ""),
                    "skip_feed": data.get("skip_feed", False),
                    "timestamp": time.time(),
                }
                # Broadcast directly to overlay clients
                asyncio.run_coroutine_threadsafe(broadcast(event), loop)
                # Note: cmd.py now writes to stream_events.jsonl directly,
                # so we don't duplicate the file write here.

                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"ok":true}')
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        elif self.path == "/feed":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body)
                event = {
                    "type": "feed",
                    "text": data.get("text", ""),
                    "highlight": data.get("highlight", False),
                    "timestamp": time.time(),
                }
                asyncio.run_coroutine_threadsafe(broadcast(event), loop)
                # Note: cmd.py now writes feed events to stream_events.jsonl
                # directly, so we don't duplicate the file write here.
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"ok":true}')
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        elif self.path == "/agent":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body)
                action = data.get("action", "")
                if action == "start":
                    global agent_watch_path, agent_watch_title, agent_watch_offset, agent_run_summary
                    agent_watch_path = data.get("jsonl_path", "")
                    agent_watch_title = data.get("title", "ANALYSIS")
                    agent_watch_offset = 0
                    agent_run_summary = data.get("run_summary", "")
                    print(f"[stream] Agent mode ON: {agent_watch_title}")
                    print(f"[stream]   Watching: {agent_watch_path}")
                    asyncio.run_coroutine_threadsafe(
                        broadcast({
                            "type": "agent_mode",
                            "active": True,
                            "title": agent_watch_title,
                            "run_summary": data.get("run_summary", ""),
                            "run_stats": dict(run_stats),
                            "timestamp": time.time(),
                        }), loop
                    )
                elif action == "stop":
                    agent_watch_path = None
                    agent_watch_title = None
                    agent_watch_offset = 0
                    agent_run_summary = None
                    print(f"[stream] Agent mode OFF")
                    asyncio.run_coroutine_threadsafe(
                        broadcast({
                            "type": "agent_mode",
                            "active": False,
                            "timestamp": time.time(),
                        }), loop
                    )
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"ok":true}')
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        elif self.path == "/reload":
            asyncio.run_coroutine_threadsafe(
                broadcast({"type": "reload"}), loop
            )
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # Suppress default logging


def run_http_server():
    """Run HTTP server for decision posts in a background thread."""
    server = HTTPServer(("127.0.0.1", HTTP_PORT), DecisionHandler)
    print(f"[stream] HTTP server on http://127.0.0.1:{HTTP_PORT}")
    server.serve_forever()


loop = None


async def main():
    global loop
    loop = asyncio.get_event_loop()

    # Start HTTP server in background thread
    http_thread = threading.Thread(target=run_http_server, daemon=True)
    http_thread.start()

    # Start WebSocket server
    print(f"[stream] WebSocket server on ws://127.0.0.1:{WS_PORT}")
    async with websockets.server.serve(ws_handler, "127.0.0.1", WS_PORT):
        await asyncio.gather(
            state_watcher(),
            event_consumer(),
            agent_watcher(),
        )


def _kill_previous():
    """If a previous stream.py is still running, kill it."""
    try:
        with open(PID_FILE) as f:
            old_pid = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return

    if old_pid == os.getpid():
        return

    try:
        os.kill(old_pid, signal.SIGTERM)
        print(f"[stream] Killed previous instance (PID {old_pid})")
        # Give it a moment to release ports
        for _ in range(20):
            try:
                os.kill(old_pid, 0)  # Check if still alive
                time.sleep(0.15)
            except OSError:
                break  # Process is gone
    except OSError:
        pass  # Already dead


def _write_pid():
    os.makedirs(os.path.dirname(PID_FILE), exist_ok=True)
    with open(PID_FILE, "w") as f:
        f.write(str(os.getpid()))


def _cleanup_pid():
    try:
        with open(PID_FILE) as f:
            if int(f.read().strip()) == os.getpid():
                os.remove(PID_FILE)
    except Exception:
        pass


if __name__ == "__main__":
    _kill_previous()
    _write_pid()
    atexit.register(_cleanup_pid)
    asyncio.run(main())
