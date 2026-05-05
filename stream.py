"""
Stream server: WebSocket broadcast for OBS overlay.

Watches game state and decisions, broadcasts to overlay clients.
Runs independently of the relay — connect overlay to ws://localhost:3001.

Also accepts HTTP POSTs from cmd.py to log reasoning:
  POST /decision  {"command": "play 1 0", "reasoning": "Kill before Ritual stacks"}
"""

import asyncio
import json
import os
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
        defaults = {"total_runs": 0, "wins": 0, "deaths": 0, "best_floor": 0,
                     "current_floor": 0, "current_hp": 0, "max_hp": 0, "current_class": "?"}
        defaults.update(saved)
        return defaults
    except (FileNotFoundError, json.JSONDecodeError):
        return {"total_runs": 0, "wins": 0, "deaths": 0, "best_floor": 0,
                "current_floor": 0, "current_hp": 0, "max_hp": 0, "current_class": "?"}

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
        # Send persistent feed to populate action panel
        for event in action_feed:
            await websocket.send(json.dumps(event))
        # Send recent reasoning events
        for event in recent_events:
            if event.get("type") == "decision":
                await websocket.send(json.dumps(event))
        # Send current stats
        await websocket.send(json.dumps({"type": "stats", **run_stats}))

        # Keep alive until disconnect
        async for _ in websocket:
            pass
    finally:
        clients.discard(websocket)
        print(f"[stream] Overlay disconnected ({len(clients)} clients)")


# Event queue for cross-thread communication (HTTP -> async)
event_queue = asyncio.Queue()


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
    # Debounce run starts: only count a run once it progresses past floor 1.
    # This prevents false starts (retried start commands) from inflating the counter.
    pending_run_start = False
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
                print(f"[stream] Game already in progress on startup (floor {init_state.get('game_state', {}).get('floor', '?')})")
                run_counted = True  # Don't count the in-progress run again
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
                        if floor > run_stats["best_floor"]:
                            run_stats["best_floor"] = floor
                            _save_stats()
                            await _broadcast_stats()

                        # Detect new run start — mark as pending, don't count yet.
                        # Only count once the run progresses past floor 1.
                        if not was_in_game and floor <= 1:
                            pending_run_start = True
                            run_counted = False
                            game_over_handled = False
                            # Clear feed for the new run
                            action_feed.clear()
                            _save_feed()
                            recent_events.clear()

                        # Count the run once it actually progresses (floor > 1)
                        # This prevents false starts from inflating the counter
                        if pending_run_start and not run_counted and floor > 1:
                            run_counted = True
                            pending_run_start = False
                            run_stats["total_runs"] += 1
                            _save_stats()
                            await broadcast({
                                "type": "run_start",
                                "class": cls,
                                "run_number": run_stats["total_runs"],
                            })
                            await _broadcast_stats()

                        # Detect game over (only process once per run)
                        if screen == "GAME_OVER" and not game_over_handled:
                            game_over_handled = True
                            # If run was never counted (died on floor 1), count it now
                            if not run_counted:
                                run_counted = True
                                pending_run_start = False
                                run_stats["total_runs"] += 1
                            victory = ss.get("victory", False)
                            if victory:
                                run_stats["wins"] += 1
                            else:
                                run_stats["deaths"] += 1
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
                        })

                    was_in_game = in_game

        except Exception as e:
            print(f"[stream] State watcher error: {e}")

        await asyncio.sleep(0.3)


async def event_consumer():
    """Consume events posted by cmd.py via HTTP."""
    while True:
        event = await event_queue.get()
        await broadcast(event)


class DecisionHandler(BaseHTTPRequestHandler):
    """HTTP handler for decision posts from cmd.py."""

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
                # Put into async queue for live overlay broadcast
                asyncio.run_coroutine_threadsafe(event_queue.put(event), loop)
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
                asyncio.run_coroutine_threadsafe(event_queue.put(event), loop)
                # Note: cmd.py now writes feed events to stream_events.jsonl
                # directly, so we don't duplicate the file write here.
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
        )


if __name__ == "__main__":
    asyncio.run(main())
