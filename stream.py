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
STATE_FILE = os.path.join(os.path.dirname(__file__), "data", "last_state.json")
EVENT_LOG = os.path.join(os.path.dirname(__file__), "data", "stream_events.jsonl")

# Connected overlay clients
clients = set()

# Recent events for new clients
recent_events = []
MAX_RECENT = 20

# Run stats
run_stats = {
    "total_runs": 0,
    "wins": 0,
    "deaths": 0,
    "best_floor": 0,
    "current_floor": 0,
    "current_hp": 0,
    "max_hp": 0,
    "current_class": "?",
}


async def broadcast(event: dict):
    """Send event to all connected overlay clients."""
    recent_events.append(event)
    if len(recent_events) > MAX_RECENT:
        recent_events.pop(0)

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
        # Send recent events to catch up
        for event in recent_events:
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


async def state_watcher():
    """Watch last_state.json for changes, broadcast state updates."""
    last_mtime = 0
    last_floor = 0
    was_in_game = False

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

                        run_stats["current_floor"] = floor
                        run_stats["current_hp"] = hp
                        run_stats["max_hp"] = max_hp
                        run_stats["current_class"] = cls
                        if floor > run_stats["best_floor"]:
                            run_stats["best_floor"] = floor

                        # Detect new run
                        if not was_in_game:
                            run_stats["total_runs"] += 1
                            await broadcast({
                                "type": "run_start",
                                "class": cls,
                                "run_number": run_stats["total_runs"],
                            })

                        # Detect game over
                        if screen == "GAME_OVER":
                            ss = gs.get("screen_state", {})
                            victory = ss.get("victory", False)
                            if victory:
                                run_stats["wins"] += 1
                            else:
                                run_stats["deaths"] += 1
                            await broadcast({
                                "type": "run_end",
                                "victory": victory,
                                "floor": floor,
                                "stats": dict(run_stats),
                            })

                        # Broadcast state
                        combat = gs.get("combat_state")
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
                            "enemies": [
                                {"name": m.get("name"), "hp": m.get("current_hp"), "max_hp": m.get("max_hp"), "intent": m.get("intent")}
                                for m in (combat or {}).get("monsters", [])
                                if not m.get("is_gone")
                            ] if combat else [],
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
                    "reasoning": data.get("reasoning", ""),
                    "timestamp": time.time(),
                }
                # Put into async queue
                asyncio.run_coroutine_threadsafe(event_queue.put(event), loop)

                # Also append to log file
                try:
                    os.makedirs(os.path.dirname(EVENT_LOG), exist_ok=True)
                    with open(EVENT_LOG, "a") as f:
                        f.write(json.dumps(event) + "\n")
                except OSError:
                    pass

                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'{"ok":true}')
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
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
