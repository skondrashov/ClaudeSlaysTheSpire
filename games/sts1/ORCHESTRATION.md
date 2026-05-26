# STS1 Pipeline Orchestration

How to run the Claude Plays Slay the Spire pipeline. Read this before starting a session.

## Architecture

```
Slay the Spire (game)
    ↕ stdin/stdout
CommunicationMod (Java mod, in-process)
    ↕ stdin/stdout
relay.py (TCP server, port 19284)
    ↕ TCP JSON
cmd.py (Python client, imported by player agent)
    → HTTP POST to stream.py (port 3002)
stream.py (WebSocket server, port 3001 + HTTP 3002)
    ↕ WebSocket
OBS browser source (overlay/index.html)
```

## Port Assignments

| Port  | Protocol | Service                     |
|-------|----------|-----------------------------|
| 19284 | TCP      | relay.py ↔ cmd.py           |
| 3001  | WS       | stream.py → overlay clients |
| 3002  | HTTP     | cmd.py → stream.py decisions|

## Starting the Pipeline

### Quick start (use this)

```powershell
# Kill any existing game/relay processes
.\scripts\kill.ps1

# Launch game with mods, auto-click Play, wait for relay
.\scripts\launch.ps1
```

`launch.ps1` handles everything: launches ModTheSpire, waits for the mod selection window, sends Enter to click Play, waits for the relay on port 19284. When it prints "Ready." the pipeline is good to go.

### Manual start (if scripts fail)

Order matters. Each component depends on the one above it.

### 1. Launch the game
Start Slay the Spire through Steam with mods enabled (ModTheSpire → BaseMod → CommunicationMod → SuperFastMode). The game must be running before relay.py can connect.

### 2. Start relay.py
CommunicationMod launches relay.py automatically as its child process — do NOT start relay.py manually. If the relay dies, the game must be restarted (CommunicationMod won't re-spawn it).

### 3. Start stream.py
```powershell
cd C:\Users\tkond\projects\autoplay\games\sts1
python stream.py
```
WebSocket server for overlay + HTTP endpoint for decisions. Independent of relay — can restart without affecting gameplay.

### 4. Add OBS browser source
Point OBS browser source at `C:\Users\tkond\projects\autoplay\games\sts1\overlay\index.html`, 1920x1080, transparent background. Only needs to be set up once.

### 5. Run the pipeline
Check `data/pipeline_state.json` for what agent to spawn next. See "Pipeline Loop" below. One agent at a time.

## Stopping / Restarting

### Kill zombie processes
Before restarting, check for zombies holding ports:
```powershell
Get-NetTCPConnection -LocalPort 3001 -ErrorAction SilentlyContinue | Select-Object OwningProcess
Get-NetTCPConnection -LocalPort 3002 -ErrorAction SilentlyContinue | Select-Object OwningProcess
Get-NetTCPConnection -LocalPort 19284 -ErrorAction SilentlyContinue | Select-Object OwningProcess
Stop-Process -Id <PID> -Force
```

### Restart order
- **stream.py** can restart independently. The overlay reconnects automatically (1s → 15s backoff). Run counter won't inflate on restart (guarded by `floor <= 1` check).
- **relay.py** restart requires the game to still be running. cmd.py reconnects per-request so no agent restart needed.
- **Player agent** must be killed and respawned if cmd.py changes (Python module caching — see Pitfalls).

## Agent Management

### Spawning a player agent
Use the Agent tool with `run_in_background: true`. The agent imports cmd.py once at startup and plays the game in a loop.

Key points for the agent prompt:
- Import from cmd: `from cmd import state, send, turn, play, end, choose, proceed, skip, potion_use, potion_discard, plan, reason, think, start`
- Always call `state()` first to see the game
- Use the `reason` parameter on `send()` — it shows on the overlay for stream viewers
- Card indices are 1-indexed, enemy indices are 0-indexed
- One action at a time, read the new state after each action
- Don't automate — reason about each decision

### Killing stale agents
Use `TaskList` to see running agents, `TaskStop` with the task ID to kill them. Always verify no duplicate agents are running before spawning a new one.

### Python module caching
**This is the #1 pitfall.** When you edit cmd.py, stream.py, or any imported module, running agents still use the old version. Python caches modules at import time. The only fix is to kill the agent and spawn a new one. There is no way to force a reimport from the orchestrator.

## Overlay

### Hot-reload
After editing overlay/index.html, trigger a reload without touching OBS:
```powershell
Invoke-WebRequest -Uri http://127.0.0.1:3002/reload -Method POST -Body '{}' -ContentType 'application/json'
```
Or from bash:
```bash
curl -s -X POST http://127.0.0.1:3002/reload
```

### Layout
L-shaped: right sidebar (420px) + bottom bar (236px). Top-left 1500x844 is transparent for the game. All text sized for mobile Twitch viewers (22px reasoning, 17px feed actions, 26px header).

### Feed persistence
Action feed persists to `data/action_feed.json` (max 30 entries). Survives overlay refreshes and stream.py restarts. New WebSocket clients receive the full feed on connect.

### Command translation
Raw commands like `play 2 0` display as `Strike → Cultist` on the overlay. Translation happens server-side in cmd.py using cached game state. The `translated` field is stored in persisted events so it survives refreshes.

cmd.py fetches state before each `send()` to ensure the translation cache is warm. If translation shows raw numbers, the cache was empty — this shouldn't happen in normal operation.

## Run Stats

Persisted in `data/run_stats.json`. Fields: total_runs, wins, deaths, best_floor, current_floor, current_hp, max_hp, current_class.

- Run counter increments only on `not was_in_game and floor <= 1` — won't inflate on stream.py restarts mid-run.
- Best floor updates automatically as the game progresses.
- Game over detection reads `screen_type == "GAME_OVER"` and `screen_state.victory`.

If stats get corrupted, manually edit `data/run_stats.json`.

## Common Pitfalls

1. **Port conflicts on restart**: Always kill old processes before starting new ones. `errno 10048` = address already in use.

2. **Module caching**: Editing cmd.py does nothing for running agents. Kill and respawn.

3. **Multiple agents competing**: Never run two player agents simultaneously. They'll both try to send commands and corrupt the game state. Use TaskList to check before spawning.

4. **Overlay shows raw commands after refresh**: Means the `translated` field wasn't stored. Check that cmd.py's `_post_decision` is sending the translated text.

5. **Run counter wrong**: If stream.py restarts while a run is in progress at floor > 1, it won't count as a new run. If it restarts while at floor 0-1 (main menu or floor 1), it will incorrectly count. This is an acceptable tradeoff — the alternative is worse.

6. **State fetch timeout**: relay.py has a 120s timeout. If the game is in a long animation, the state fetch might time out. SuperFastMode mod helps but doesn't eliminate this.

7. **Bash doesn't work for Windows paths**: Use PowerShell for any commands involving Windows paths. Bash tries to interpret backslashes.

## Pipeline Loop

**You are a pipeline manager.** You have no opinion about the game. The pipeline cycles through four agent types. Your only job is to keep the cycle turning.

### After EVERY agent completes — do this FIRST

1. Read `data/pipeline_state.json` — what did the last agent recommend?
2. Read the agent's result — note the outcome and their next-goal recommendation
3. Update `data/pipeline_state.json` with the completed agent's info
4. Commit and push all changes (run data, playbook edits, analyst reports)
5. **Spawn the recommended agent** — not Win by default. Whatever the pipeline says.

If `pipeline_state.json` doesn't exist or is corrupt, read `heuristics/sts1/goals/next.md` and apply the decision logic manually.

### pipeline_state.json format

```json
{
  "last_agent": "win",
  "last_run": 215,
  "next_recommended": "audit",
  "reason": "Run 215 was first Watcher win — notable outcome, audit is high priority",
  "runs_since_last_audit": 3,
  "runs_since_last_curate": 12,
  "outstanding_directives": ["Directive 4: Watcher execution cleanup"]
}
```

Update this file after every agent completes. The `next_recommended` field is what you follow.

### Spawning a PLAYER (Win or Explore)

1. Generate new session token and clear old lock:
   ```python
   python -c "
   import uuid, os
   token = str(uuid.uuid4())
   lock = 'data/player.lock'
   if os.path.exists(lock): os.remove(lock)
   print(token)
   "
   ```
2. Spawn player as background agent with token in prompt
3. Do NOT activate overlay — player uses normal game overlay

### Spawning an ANALYST (Audit)

1. **ACTIVATE OVERLAY FIRST:**
   ```python
   python -c "
   import json, urllib.request
   data = json.dumps({
       'action': 'start',
       'title': 'POST-GAME ANALYSIS',
       'jsonl_path': '<ANALYST_JSONL_PATH>',
       'run_summary': '<PLAYER_SUMMARY_TEXT>'
   }).encode('utf-8')
   req = urllib.request.Request('http://127.0.0.1:3002/agent', data=data, headers={'Content-Type': 'application/json'})
   urllib.request.urlopen(req)
   "
   ```
   JSONL path: `C:/Users/tkond/.claude/projects/C--Users-tkond-projects-autoplay/<SESSION_ID>/subagents/agent-<ANALYST_TASK_ID>.jsonl`
2. Spawn analyst as background agent with audit.md instructions + run summary

### Spawning a CURATOR (Curate)

1. **ACTIVATE OVERLAY FIRST** — title: `STRATEGIC REVIEW`, use the curator's agent task ID for the JSONL path
2. Spawn curator as background agent with curate.md instructions + review context

### Stopping overlay (after Audit or Curate completes)

```python
python -c "
import json, urllib.request
data = json.dumps({'action': 'stop'}).encode('utf-8')
req = urllib.request.Request('http://127.0.0.1:3002/agent', data=data, headers={'Content-Type': 'application/json'})
urllib.request.urlopen(req)
"
```

### Common mistakes

- **Defaulting to Win** — the #1 pipeline failure. ALWAYS check pipeline_state.json first. If context compression made you forget the cycle, the file remembers.
- **Forgetting overlay for non-player agents** — EVERY Audit/Curate agent gets overlay activation BEFORE spawning
- **Using wrong task ID for JSONL path** — use the NEW agent's task ID, not the completed one
- **Forgetting to push** — site rebuild triggers on push, not commit
- **Skipping Audit after notable runs** — first wins, surprising deaths, and new archetype attempts all deserve audits

---

## Data Files (gitignored via `data/`)

| File | Purpose |
|------|---------|
| `data/last_state.json` | Latest game state from relay (written by relay.py) |
| `data/run_stats.json` | Persistent run statistics |
| `data/action_feed.json` | Persistent action feed for overlay |
| `data/stream_events.jsonl` | Full event log (append-only) |
