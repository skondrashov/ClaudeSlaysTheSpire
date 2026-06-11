"""
Command helper for Claude Code to interact with Slay the Spire.

Connects to relay.py's TCP server (localhost:19284) to read game state
and send commands. Each function is a single request-response.

Usage from Claude Code:
    from cmd import state, send
    state()           # See current game state
    send("play 1 0")  # Play card 1 targeting enemy 0
    send("end")       # End turn
    send("choose 2")  # Choose option 2
    send("proceed")   # Confirm/proceed
    send("return")    # Skip/cancel/leave
"""

import json
import os
import re
import socket
import subprocess
import sys
import time
import urllib.request

from bot.state_formatter import (format_state, monster_name,
                                 _build_shop_choice_list, _event_choice_options)

HOST = "127.0.0.1"
PORT = 19284
TIMEOUT = 120  # seconds — long timeout for slow animations
STREAM_URL = "http://127.0.0.1:3002/decision"
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Knowledge lives at the Praxis root (two levels up: games/sts1 -> praxis), under
# <layer>/sts1/. cmd.py previously pointed these at games/sts1/{ontology,heuristics},
# which don't exist — so every lookup silently returned None. Point at the real tree.
ROOT = os.path.dirname(os.path.dirname(_BASE_DIR))
LOCK_FILE = os.path.join(_BASE_DIR, "data", "player.lock")
ONTOLOGY_DIR = os.path.join(ROOT, "ontology", "sts1")
HEURISTICS_DIR = os.path.join(ROOT, "heuristics", "sts1")
PHENOMENA_DIR = os.path.join(ROOT, "phenomena", "sts1")
RUNS_DIR = os.path.join(_BASE_DIR, "analyst", "runs")
STATS_FILE = os.path.join(_BASE_DIR, "data", "run_stats.json")

# Direct event log — cmd.py is the single writer. stream.py reads this for
# real-time overlay display. On GAME_OVER, cmd.py reads it to build the
# permanent run JSON.
EVENT_LOG = os.path.join(_BASE_DIR, "data", "stream_events.jsonl")

# Session token: passed via PLAYER_SESSION env var by the orchestrator.
# All bash calls from one agent use the same token. The lock checks this.
_SESSION_ID = os.environ.get("PLAYER_SESSION", "")
if not _SESSION_ID:
    raise RuntimeError(
        "PLAYER_SESSION env var not set.\n"
        "Only the orchestrator can provide this token."
    )


def _acquire_lock():
    """Acquire the player lock at import time. Fails if another session holds it."""
    os.makedirs(os.path.dirname(LOCK_FILE), exist_ok=True)

    if os.path.exists(LOCK_FILE):
        try:
            with open(LOCK_FILE) as f:
                held_by = f.read().strip()
            if held_by == _SESSION_ID:
                return  # our lock from a previous call
            raise RuntimeError(
                f"PLAYER LOCK CONFLICT — lock held by {held_by[:12]}...\n"
                f"Another player agent is running. Only one at a time.\n"
                f"Orchestrator must delete data/player.lock before spawning a new agent."
            )
        except (OSError, ValueError):
            pass  # corrupted lock, take it

    with open(LOCK_FILE, "w") as f:
        f.write(_SESSION_ID)


# Acquire lock at import time.
# Orchestrator deletes this file before spawning a new agent.
_acquire_lock()


# ---------------------------------------------------------------------------
# Knowledge loading utilities (ontology + heuristics)
# ---------------------------------------------------------------------------

def _name_to_filename(name: str) -> str:
    """Convert a game entity name to its filename stem (robust slug, matches
    tools/regen): drop a trailing '+', lowercase, drop ' and ., then collapse any
    run of other non-alphanumerics to '-'.

    "Shrug It Off+" -> "shrug-it-off"
    "Charon's Ashes" -> "charons-ashes"
    "Spike Slime (M)" -> "spike-slime-m"
    "3 Cultists" -> "3-cultists"
    """
    name = name.rstrip("+").strip().lower().replace("'", "").replace(".", "")
    return re.sub(r"[^a-z0-9]+", "-", name).strip("-")


def _stem_candidates(name: str) -> list[str]:
    """Filename stems to try for a name. The slug first, then the 'the-' variant:
    in-game names and entry titles disagree about a leading "The" ("Champ" vs
    "The Champ", "Guardian" vs "The Guardian"), so a miss retries with the
    article added or removed."""
    s = _name_to_filename(name)
    return [s, s[4:] if s.startswith("the-") else "the-" + s]


def _load_entry(base_dir: str, category: str, name: str, suffix: str = ".md") -> str | None:
    for stem in _stem_candidates(name):
        path = os.path.join(base_dir, category, stem + suffix)
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except FileNotFoundError:
            continue
    return None


def _load_ontology(category: str, name: str) -> str | None:
    """Load an ontology file. Returns content or None if not found."""
    return _load_entry(ONTOLOGY_DIR, category, name)


def _load_phenomenon(category: str, name: str) -> str | None:
    """Load a phenomenon. Resolved upgraded cards live at
    phenomena/sts1/<category>/<stem>-plus.md (tried first); authored phenomena
    (recognitions) are plain <stem>.md files. None if absent."""
    return (_load_entry(PHENOMENA_DIR, category, name, suffix="-plus.md")
            or _load_entry(PHENOMENA_DIR, category, name))


def _load_heuristic(category: str, name: str) -> str | None:
    """Load a heuristic file. Returns content or None if not found."""
    return _load_entry(HEURISTICS_DIR, category, name)


def _load_heuristic_root(filename: str) -> str | None:
    """Load a root-level heuristic file (strategy.md)."""
    path = os.path.join(HEURISTICS_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def _load_knowledge(category: str, name: str) -> str | None:
    """Load ontology + heuristic for an entity, combined.

    For a '+'-suffixed (upgraded) name, the resolved phenomenon stands in for the
    ontology layer — so an upgraded card in hand shows its actual values, not the
    base — falling back to the base noumenon when no phenomenon exists.
    Returns both layers clearly separated, or None if neither exists.
    """
    ont = _load_phenomenon(category, name) if name.endswith("+") else None
    if ont is None:
        ont = _load_ontology(category, name)
    heur = _load_heuristic(category, name)
    if not ont and not heur:
        return None
    parts = []
    if ont:
        parts.append(ont)
    if heur:
        # Strip the duplicate "# Name" header from heuristic if ontology has it
        heur_lines = heur.split("\n")
        if heur_lines and heur_lines[0].startswith("# ") and ont:
            heur = "\n".join(heur_lines[1:]).strip()
        if heur:
            parts.append(f"### Strategy\n\n{heur}")
    return "\n\n".join(parts)


def _load_ontology_top(category: str, name: str) -> str | None:
    """Load just the header + first summary line of an ontology file.

    Used for compact deck reports in act planning.
    """
    content = _load_ontology(category, name)
    if content is None:
        return None
    lines = [l for l in content.split("\n") if l.strip()]
    if len(lines) >= 2:
        return lines[0] + "\n" + lines[1]
    elif lines:
        return lines[0]
    return None


_LINK_QUAL_RE = re.compile(r"^(layer|domain|category)\s*:\s*(.+)$", re.IGNORECASE)
_LINK_LAYERS = {"ontology", "phenomena", "heuristics", "goals"}


def _extract_links(content: str) -> list[tuple[str | None, str | None, str]]:
    """Extract [[...]] links as (layer, category, name).

    Mirrors the site resolver's grammar (site/build.py) and the awareness loader
    (tools/awareness/loaders.py) — keep all three in sync: comma-separated,
    order-free, spelled-out `layer:` / `domain:` / `category:` qualifiers; an
    optional `|Display` alias; a leading layer keyword in the address (`goals/next`).
    `layer` is None when unspecified.
    """
    out = []
    for inner in re.findall(r'\[\[([^\]]+)\]\]', content):
        full = inner.split("|", 1)[0]  # drop |Display alias
        layer = cat_q = addr = None
        for tok in full.split(","):
            tok = tok.strip()
            if not tok:
                continue
            m = _LINK_QUAL_RE.match(tok)
            if m:
                k, v = m.group(1).lower(), m.group(2).strip()
                if k == "layer":
                    layer = v
                elif k == "category":
                    cat_q = v
                # domain: captured-but-ignored (single-domain loaders)
            elif addr is None:
                addr = tok
        if addr is None:
            continue
        if "/" in addr:                  # leading layer keyword acts as the layer
            first, rest = addr.split("/", 1)
            if first in _LINK_LAYERS and layer is None:
                layer, addr = first, rest
        if "/" in addr:
            cat, name = addr.split("/", 1)
            cat = cat.strip() or None
            name = name.strip()
        else:
            cat, name = None, addr.strip()
        if cat_q:
            cat = cat_q
        if name:
            out.append((layer, cat, name))
    return out


def _resolve_links(content: str, already_loaded: set = None) -> str:
    """Resolve one level of categorized [[...]] links in content.

    Loads the ontology entry by default; an explicit `layer:heuristics` qualifier
    loads the heuristic instead. Bare top-level refs are not followed here.
    """
    if already_loaded is None:
        already_loaded = set()
    resolved = []
    for layer, cat, name in _extract_links(content):
        if not cat:
            continue
        layer = layer or "ontology"
        key = f"{layer}/{cat}/{name}"
        if key in already_loaded:
            continue
        already_loaded.add(key)
        entry = _load_heuristic(cat, name) if layer == "heuristics" else _load_ontology(cat, name)
        if entry:
            resolved.append(entry)
    if resolved:
        return "\n\n--- LINKED KNOWLEDGE ---\n\n" + "\n\n".join(resolved)
    return ""


_BASIC_CARDS = {"Strike", "Defend", "Strike+", "Defend+"}


def _tcp_request(request: dict) -> dict:
    """Send a JSON request to relay, get JSON response."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    try:
        sock.connect((HOST, PORT))
        sock.sendall(json.dumps(request).encode() + b"\n")

        data = b""
        while b"\n" not in data:
            chunk = sock.recv(65536)
            if not chunk:
                break
            data += chunk

        if not data.strip():
            return {"error": "empty response from relay"}
        return json.loads(data.strip())
    except ConnectionRefusedError:
        return {"error": "Cannot connect to relay. Is the game running with CommunicationMod?"}
    except socket.timeout:
        return {"error": "Timeout waiting for relay response"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        sock.close()


def state() -> str:
    """Get current game state, formatted for reading."""
    global _last_raw_state
    raw = _tcp_request({"type": "state"})
    if "error" in raw:
        # A stale queued-command error can shadow a perfectly good state —
        # retry once and only surface the error if it persists.
        retry = _tcp_request({"type": "state"})
        if "error" not in retry:
            raw = retry
    _remember(raw)
    # Auto-handle mechanical transitions before returning state
    raw = _auto_handle_mechanical(raw)
    return _interruption_notice(raw) + format_state(raw)


def state_raw() -> dict:
    """Get current game state as raw dict."""
    global _last_raw_state
    raw = _tcp_request({"type": "state"})
    _remember(raw)
    return raw


# Cached state for translating commands to readable text
_last_raw_state = None


def _healthy_state(raw) -> bool:
    """A response safe to cache: a real in-game state, or a real out-of-game
    state. Error dicts and transient relay acks ({"status":"ok","note":"command
    sent, state pending"}) are NOT healthy — caching one poisons name->index
    resolution for every subsequent command (a poisoned cache produced a
    zero-cards-played turn that lost a run)."""
    if not isinstance(raw, dict) or "error" in raw:
        return False
    if "game_state" in raw:
        return True
    return raw.get("in_game") is False and "available_commands" in raw


def _remember(raw):
    """Update the cached state ONLY when the response is healthy; always
    returns the response unchanged so callers can still inspect errors.

    Also maintains the run-live FILE marker (data/run_live.flag) behind the
    IB-012 tripwire: set while a run is in progress, cleared when the run ends
    legitimately (GAME_OVER/COMPLETE). If the game reports out-of-game while
    the marker is set, the run was INTERRUPTED (crash-to-menu), not finished —
    _interruption_notice() makes every state echo say so. A file, not memory:
    every play.py call is a fresh process."""
    global _last_raw_state
    if _healthy_state(raw):
        _last_raw_state = raw
        flag = os.path.join(_BASE_DIR, "data", "run_live.flag")
        if raw.get("in_game"):
            screen = (raw.get("game_state") or {}).get("screen_type", "")
            if screen in ("GAME_OVER", "COMPLETE"):
                if os.path.exists(flag):
                    os.remove(flag)
            elif not os.path.exists(flag):
                with open(flag, "w") as f:
                    f.write(str((raw.get("game_state") or {}).get("seed", "")))
        # out-of-game: leave the flag — its presence IS the interruption signal
    return raw


def _interruption_notice(raw) -> str:
    """A loud banner when the game is out-of-game but the run never ended
    (IB-012: crash to main menu with a live save). Empty string otherwise."""
    if not isinstance(raw, dict) or raw.get("in_game") is not False:
        return ""
    if not os.path.exists(os.path.join(_BASE_DIR, "data", "run_live.flag")):
        return ""
    return (
        "[RUN INTERRUPTED] The game is at the main menu but your run never "
        "reached GAME_OVER — it crashed out mid-run and the save is almost "
        "certainly intact (IB-012). Do NOT call start() (it DESTROYS the save). "
        "STOP issuing commands and report to the orchestrator, who can resume "
        "the run by clicking Continue in the game window.\n\n"
    )


def _resolve_enemy_name(monsters: list, name_ref: str) -> str | None:
    """Resolve an enemy name to its absolute index in the monsters array.

    CommunicationMod uses absolute indices into the full monsters array
    (including dead/gone enemies). This resolves a name to that index.

    Returns the index as a string, or None if no match.
    Raises ValueError when the name matches several living enemies — silently
    targeting the first match has hit the wrong enemy; the caller must surface
    the error so the player picks an index.
    """
    name_lower = name_ref.lower()
    # Exact match first — against the precise (id-disambiguated) name the agent
    # sees in the formatted state ("Blue Slaver"), falling back to the raw name.
    matches = [i for i, m in enumerate(monsters) if not m.get("is_gone")
               and name_lower in (monster_name(m).lower(), m.get("name", "").lower())]
    if not matches:
        # Substring match
        matches = [i for i, m in enumerate(monsters) if not m.get("is_gone")
                   and (name_lower in monster_name(m).lower()
                        or name_lower in m.get("name", "").lower())]
    if not matches:
        return None
    if len(matches) > 1:
        listing = ", ".join(
            f"[{i}] {monster_name(monsters[i])} "
            f"{monsters[i].get('current_hp', '?')}/{monsters[i].get('max_hp', '?')}"
            for i in matches)
        raise ValueError(
            f"'{name_ref}' matches {len(matches)} enemies: {listing} — use the index.")
    return str(matches[0])


def _card_identity(card: dict) -> tuple:
    """Return (name, upgrades) tuple for matching cards across hand changes.

    Ignores cost because Corruption/Madness/Enlightenment can modify costs
    mid-turn. Name + upgrade status is stable enough for identity matching.
    """
    return (card.get("name", ""), card.get("upgrades", 0))


def _find_card_in_current_hand(current_hand: list, identity: tuple) -> int | None:
    """Find a card matching the given identity in the current hand.

    Returns 1-indexed position (for CommunicationMod), or None if not found.
    Tries (name, upgrades) first, falls back to name-only for Armaments+ edge case.
    """
    name, upgrades = identity

    # Pass 1: exact match on (name, upgrades)
    for i, card in enumerate(current_hand):
        if _card_identity(card) == identity:
            return i + 1

    # Pass 2: name-only (handles Armaments+ upgrading cards mid-turn)
    for i, card in enumerate(current_hand):
        if card.get("name", "") == name:
            return i + 1

    return None


def _resolve_play_from_snapshot(snapshot_hand: list, current_state: dict, action: str) -> str:
    """Resolve a 'play N [target]' action using the snapshot hand for card identity.

    When the agent plans a turn, it sees a hand and references cards by index.
    As cards are played, indices shift. This function translates the agent's
    original index (referencing the snapshot) to the correct current index.

    Only handles numeric card indices — name-based actions pass through unchanged
    to be handled by _resolve_card_name.
    """
    if not action or not action.strip().lower().startswith("play "):
        return action

    parts = action.strip().split()
    if len(parts) < 2 or not parts[1].isdigit():
        return action  # Name-based, existing resolution handles it

    card_idx_0 = int(parts[1]) - 1  # Agent uses 1-indexed
    if card_idx_0 < 0 or card_idx_0 >= len(snapshot_hand):
        return action  # Out of range, let CommunicationMod error

    # Look up what card the agent meant
    identity = _card_identity(snapshot_hand[card_idx_0])

    # Find it in the current hand
    current_combat = (current_state.get("game_state") or {}).get("combat_state")
    if not current_combat:
        return action
    current_hand = current_combat.get("hand", [])

    current_idx = _find_card_in_current_hand(current_hand, identity)
    if current_idx is None:
        # Card gone (already played, discarded, etc.) — pass through, will fail naturally
        return action

    # Rebuild action with corrected index, preserve target
    target = " ".join(parts[2:]) if len(parts) > 2 else ""
    return f"play {current_idx} {target}".strip()


def _resolve_choose_from_snapshot(snapshot_cards: list, current_cards: list, action: str) -> str:
    """Resolve a 'choose N' action using a snapshot for card identity.

    Same logic as _resolve_play_from_snapshot but for HAND_SELECT/GRID screens
    where selecting a card removes it from the list, shifting indices.
    """
    parts = action.strip().split()
    if len(parts) < 2 or parts[0].lower() != "choose" or not parts[1].isdigit():
        return action

    idx = int(parts[1])
    if idx < 0 or idx >= len(snapshot_cards):
        return action  # Out of range

    identity = _card_identity(snapshot_cards[idx])

    # Find in current list
    for j, card in enumerate(current_cards):
        if _card_identity(card) == identity:
            return f"choose {j}"

    # Fallback: name-only match
    name = identity[0]
    for j, card in enumerate(current_cards):
        if card.get("name", "") == name:
            return f"choose {j}"

    return action  # Not found, pass through


def _resolve_card_name(raw_state: dict, action: str) -> str:
    """Translate card names and enemy names in play commands to indices.

    Supports card names, enemy names, or both:
        "play Bash Jaw Worm"    -> "play 2 0"   (card name + enemy name)
        "play Bash 0"           -> "play 2 0"   (card name + numeric target)
        "play Shrug It Off"     -> "play 3"     (card name, no target)
        "play Bash+ 0"          -> "play 2 0"   (upgraded card + target)
        "play 3 0"              -> "play 3 0"   (numeric, unchanged)
        "play 3 Jaw Worm"       -> "play 3 0"   (numeric card + enemy name)

    Enemy names are resolved to absolute indices in the monsters array
    (matching CommunicationMod's indexing which includes dead enemies).
    """
    if not action or not action.strip().lower().startswith("play "):
        return action

    parts = action.strip().split()
    if len(parts) < 2:
        return action

    if not raw_state:
        return action
    combat = (raw_state.get("game_state") or {}).get("combat_state")
    if not combat:
        return action
    hand = combat.get("hand", [])
    monsters = combat.get("monsters", [])

    # Extract everything after "play"
    after_play = action.strip()[len("play "):].strip()
    tokens = after_play.split()

    # --- Case 1: Card is a numeric index ---
    if tokens[0].isdigit():
        card_idx = tokens[0]
        target_ref = " ".join(tokens[1:]) if len(tokens) > 1 else None
        if target_ref:
            # Already numeric?
            try:
                int(target_ref)
                return action  # "play 3 0" — all numeric, unchanged
            except ValueError:
                pass
            # Resolve enemy name
            try:
                resolved_target = _resolve_enemy_name(monsters, target_ref)
            except ValueError as e:
                return f"[ERROR] {e}"
            if resolved_target is not None:
                return f"play {card_idx} {resolved_target}"
        return action  # "play 3" or unresolvable target

    # --- Case 2: Card is a name — find it in hand ---
    # Try matching hand card names against the token sequence (longest match wins).
    # This handles multi-word card names like "Shrug It Off".
    # When multiple cards match equally (e.g., two Strikes), pick the cheapest one.
    # This matters with Snecko Oil or other cost-randomizing effects.
    best_card_idx = None       # 1-indexed card position in hand
    best_token_count = 0       # how many tokens the card name consumed
    best_card_cost = float('inf')  # cost of the best match (prefer cheapest)

    for i, card in enumerate(hand):
        card_name = card.get("name", "")
        upgraded = card.get("upgrades", 0) > 0
        card_cost = card.get("cost", 99)

        # Build candidate names to try
        names_to_try = [card_name]
        if upgraded:
            names_to_try.append(card_name + "+")

        for try_name in names_to_try:
            try_tokens = try_name.lower().split()
            tc = len(try_tokens)
            if tc > len(tokens) or tc < best_token_count:
                continue
            # Same token count but more expensive — skip (keep cheapest)
            if tc == best_token_count and card_cost >= best_card_cost:
                continue
            candidate = " ".join(tokens[:tc]).lower()
            # Match against name (with or without +)
            if candidate == try_name.lower():
                best_card_idx = i + 1
                best_token_count = tc
                best_card_cost = card_cost
            elif candidate == try_name.rstrip("+").lower():
                # "play Bash" matches "Bash" even if upgraded
                if try_name.endswith("+"):
                    # Only match non-+ input to upgraded cards if no + specified
                    # (don't require_upgrade if they didn't type +)
                    pass  # handled by the base name in names_to_try[0]
                best_card_idx = i + 1
                best_token_count = tc
                best_card_cost = card_cost

    if best_card_idx is None:
        return action  # No card match, return unchanged

    # Whatever's left after the card name is the target
    remaining = " ".join(tokens[best_token_count:]).strip() if best_token_count < len(tokens) else ""

    if not remaining:
        return f"play {best_card_idx}"

    # Target is numeric?
    try:
        int(remaining)
        return f"play {best_card_idx} {remaining}"
    except ValueError:
        pass

    # Resolve enemy name to absolute index
    try:
        resolved_target = _resolve_enemy_name(monsters, remaining)
    except ValueError as e:
        return f"[ERROR] {e}"
    if resolved_target is not None:
        return f"play {best_card_idx} {resolved_target}"

    # Couldn't resolve target — return with card resolved at least
    return f"play {best_card_idx} {remaining}"


# _build_shop_choice_list lives in bot.state_formatter (imported above) so the
# shop display can render the same indices the choose command uses.


def _resolve_shop_choose(raw_state: dict, action: str) -> str:
    """Resolve card/relic/potion names in shop choose commands to indices.

    Supports:
        "choose Inflame"        -> "choose 3"  (finds Inflame in shop cards)
        "choose purge"          -> "choose 0"  (purge is always index 0 when affordable)
        "choose 3"              -> "choose 3"  (already numeric, pass through)

    CommunicationMod indexes shop items as:
        purge (if affordable) → affordable cards → affordable relics → affordable potions

    This must match that ordering exactly, or the wrong item gets bought.
    """
    gs = raw_state.get("game_state", {}) if raw_state else {}
    screen = gs.get("screen_type", "")
    if screen not in ("SHOP_ROOM", "SHOP_SCREEN"):
        return action  # Not in shop, pass through

    parts = action.strip().split()
    if len(parts) < 2 or parts[0].lower() != "choose":
        return action

    remainder = " ".join(parts[1:])

    # "return" leaves the shop — pass through
    if remainder.lower() == "return":
        return action

    # Already numeric — pass through (caller knows the index)
    try:
        int(remainder)
        return action
    except ValueError:
        pass

    # Build the choice list matching CommunicationMod's indexing
    items = _build_shop_choice_list(gs)
    if not items:
        return action

    search_name = remainder.lower().rstrip("+")
    search_clean = search_name.replace(" ", "").replace("'", "")

    # "choose purge" → find purge in the list
    if search_name == "purge":
        for idx, (cat, name, _) in enumerate(items):
            if cat == "purge":
                return f"choose {idx}"
        return action  # Purge not available/affordable

    # Search all items by name
    for idx, (cat, name, item) in enumerate(items):
        if cat == "purge":
            continue
        item_name = name.lower()
        item_clean = item_name.replace(" ", "").replace("'", "")
        if item_name == search_name or item_clean == search_clean:
            return f"choose {idx}"

    return action  # No match found, pass through unchanged


def _resolve_reward_choose(raw_state: dict, action: str) -> str:
    """Resolve item NAMES in choose commands on reward screens (COMBAT_REWARD /
    BOSS_REWARD) to indices. Multi-word relic/potion names previously only
    worked in shops; reward screens rejected them, forcing index-chaining --
    the error family behind two mis-taken keys."""
    parts = action.strip().split()
    if len(parts) < 2 or parts[0].lower() != "choose":
        return action
    arg = " ".join(parts[1:]).strip()
    if arg.isdigit():
        return action
    gs = (raw_state or {}).get("game_state") or {}
    screen = gs.get("screen_type", "")
    ss = gs.get("screen_state", {})
    name = arg.lower()
    if screen == "COMBAT_REWARD":
        for i, r in enumerate(ss.get("rewards", [])):
            label = (r.get("relic", {}).get("name")
                     or r.get("potion", {}).get("name")
                     or ("card" if r.get("reward_type") == "CARD" else "")
                     or r.get("reward_type", ""))
            if label and name in str(label).lower():
                return f"choose {i}"
    elif screen == "BOSS_REWARD":
        for i, r in enumerate(ss.get("relics", [])):
            if name in r.get("name", "").lower():
                return f"choose {i}"
    return action


def _resolve_choose_card_name(raw_state: dict, action: str) -> str:
    """Resolve card names in choose commands to indices for card-selection screens.

    Supports HAND_SELECT, CARD_REWARD, and GRID screens:
        "choose Sneaky Strike"  -> "choose 2"  (finds Sneaky Strike in the card list)
        "choose 3"              -> "choose 3"  (already numeric, pass through)
    """
    gs = raw_state.get("game_state", {}) if raw_state else {}
    screen = gs.get("screen_type", "")
    ss = gs.get("screen_state", {})

    # Determine which card list to search based on screen type
    if screen == "HAND_SELECT":
        cards = ss.get("hand", [])
    elif screen in ("CARD_REWARD", "GRID"):
        cards = ss.get("cards", [])
    else:
        return action  # Not a card-selection screen

    parts = action.strip().split()
    if len(parts) < 2 or parts[0].lower() != "choose":
        return action

    remainder = " ".join(parts[1:])

    # Already numeric — for GRID screens, warn if the index might be wrong
    # (agents often confuse hand indices with GRID indices)
    try:
        idx = int(remainder)
        if screen == "GRID" and cards:
            # Log what card is at this index in the GRID for debugging
            if 0 <= idx < len(cards):
                card_at_idx = cards[idx].get("name", "?")
                if cards[idx].get("upgrades", 0) > 0 and not card_at_idx.endswith("+"):
                    card_at_idx += "+"
                # Pass through — the index is valid for the GRID
            # else: index out of range, pass through and let CommunicationMod handle
        return action
    except ValueError:
        pass

    # Search for card name match (case-insensitive, handles upgraded names)
    search = remainder.lower().strip()
    search_no_plus = search.rstrip("+")

    best_idx = None
    best_token_count = 0

    for i, card in enumerate(cards):
        card_name = card.get("name", "")
        card_name_lower = card_name.lower()
        upgraded = card.get("upgrades", 0) > 0

        # Try matching with and without +
        candidates = [card_name_lower]
        if upgraded:
            candidates.append(card_name_lower + "+")

        for candidate in candidates:
            tc = len(candidate.split())
            if tc <= best_token_count:
                continue
            if search == candidate or search_no_plus == candidate or search == candidate.rstrip("+"):
                best_idx = i
                best_token_count = tc

    if best_idx is not None:
        return f"choose {best_idx}"

    return action  # No match found


def _translate_named_choose(name: str) -> str:
    """Translate named choose commands like 'choose rest'."""
    name_map = {
        "rest": "Rest",
        "smith": "Smith (Upgrade)",
        "dig": "Dig",
        "recall": "Recall",
        "lift": "Lift",
        "toke": "Toke",
        "purge": "Remove Card",
    }
    return name_map.get(name.lower(), name.capitalize())


def _translate_command(command: str) -> str:
    """Translate raw command into readable text using cached game state."""
    if not command:
        return command
    parts = command.strip().split()
    verb = parts[0]

    gs = (_last_raw_state or {}).get("game_state", {})
    combat = gs.get("combat_state")

    if verb == "play" and combat:
        # The card ref may be an index OR a multi-word name (an unresolved name
        # used to crash this translator with ValueError, killing the command).
        hand = combat.get("hand", [])
        target_tok = parts[-1] if len(parts) > 2 and parts[-1].lstrip("-").isdigit() else None
        ref_tokens = parts[1:-1] if target_tok is not None else parts[1:]
        ref = " ".join(ref_tokens)
        if ref.isdigit():
            card_idx = int(ref) - 1
            card = hand[card_idx] if 0 <= card_idx < len(hand) else None
            card_name = card["name"] if card else f"card {ref}"
        else:
            card_name = ref or "card ?"
        if target_tok is not None:
            monsters = combat.get("monsters", [])  # absolute index
            target_idx = int(target_tok)
            enemy = monsters[target_idx] if 0 <= target_idx < len(monsters) else None
            enemy_name = monster_name(enemy) if enemy else f"enemy {target_tok}"
            return f"{card_name} → {enemy_name}"
        return card_name

    if verb == "choose" and len(parts) > 1:
        screen = gs.get("screen_type", "")
        ss = gs.get("screen_state", {})
        try:
            idx = int(parts[1])
        except ValueError:
            # Named choice like "choose rest" or "choose smith"
            return _translate_named_choose(parts[1])

        if screen == "MAP":
            nodes = ss.get("next_nodes", [])
            if 0 <= idx < len(nodes):
                symbol = nodes[idx].get("symbol", "?")
                node_name = {"M": "Monster", "?": "Unknown", "$": "Shop",
                             "E": "Elite", "R": "Rest Site", "T": "Treasure",
                             "B": "Boss"}.get(symbol, symbol)
                return f"→ {node_name}"
        elif screen == "REST":
            options = ss.get("rest_options", [])
            if 0 <= idx < len(options):
                opt = options[idx] if isinstance(options[idx], str) else str(options[idx])
                return opt.capitalize()
        elif screen == "CARD_REWARD":
            cards = ss.get("cards", [])
            if 0 <= idx < len(cards):
                return f"Take {cards[idx].get('name', '?')}"
        elif screen == "COMBAT_REWARD":
            rewards = ss.get("rewards", [])
            if 0 <= idx < len(rewards):
                r = rewards[idx]
                rtype = r.get("reward_type", "?")
                if rtype == "GOLD":
                    return f"Take {r.get('gold', 0)}g"
                elif rtype == "CARD":
                    return "Take Card Reward"
                elif rtype == "POTION":
                    return f"Take {r.get('potion', {}).get('name', 'Potion')}"
                elif rtype == "RELIC":
                    return f"Take {r.get('relic', {}).get('name', 'Relic')}"
                elif rtype == "EMERALD_KEY":
                    return "Take Emerald Key"
                elif rtype == "SAPPHIRE_KEY":
                    return f"Take Sapphire Key"
                else:
                    return f"Take {rtype}"
        elif screen == "BOSS_REWARD":
            relics = ss.get("relics", [])
            if 0 <= idx < len(relics):
                return f"Take {relics[idx].get('name', 'Relic')}"
        elif screen in ("SHOP_ROOM", "SHOP_SCREEN"):
            # Index against CommunicationMod's REAL shop ordering (purge first,
            # then affordable cards/relics/potions). Translating against the raw
            # cards array mislabeled purchases by the purge offset and the
            # affordability filter ("Buy Armaments" while actually buying
            # Fiend Fire — run 230; "Buy Secret Weapon" → Skill Potion — IB-003).
            items = _build_shop_choice_list(gs)
            if 0 <= idx < len(items):
                cat, name, _item = items[idx]
                return "Remove Card (purge)" if cat == "purge" else f"Buy {name}"
        elif screen == "EVENT":
            # Index against the ENABLED options only — CommunicationMod's
            # choice_list excludes disabled ones, so translating against the
            # full display list mislabels every option after a disabled one
            # (IB-010/IB-013: echoed the relic offer, executed Leave).
            enabled = _event_choice_options(ss)
            if 0 <= idx < len(enabled):
                text = enabled[idx].get("text", "?")
                text = re.sub(r"<[^>]+>", "", text)[:50]
                return text
        elif screen == "GRID":
            cards = ss.get("cards", [])
            if 0 <= idx < len(cards):
                action = "Upgrade" if ss.get("for_upgrade") else "Remove" if ss.get("for_purge") else "Select"
                return f"{action} {cards[idx].get('name', '?')}"
        elif screen == "HAND_SELECT":
            hand = ss.get("hand", [])
            if 0 <= idx < len(hand):
                return f"Select {hand[idx].get('name', '?')}"

        # Fallback: use choice_list
        choices = gs.get("choice_list", [])
        if 0 <= idx < len(choices):
            return f"Choose: {choices[idx]}"

    if verb == "end":
        return "End Turn"
    if verb == "proceed":
        return "Proceed"
    if verb in ("skip", "return", "leave"):
        return "Skip"
    if verb == "potion":
        action = parts[1] if len(parts) > 1 else ""
        slot = parts[2] if len(parts) > 2 else "?"
        if action == "use":
            return f"Use Potion {slot}"
        if action == "discard":
            return f"Discard Potion {slot}"
    if verb == "start":
        return f"Start — {parts[1] if len(parts) > 1 else 'IRONCLAD'}"
    if verb == "confirm":
        return "Confirm"

    return command


_event_seq = 0

def _log_event(event: dict):
    """Write event directly to stream_events.jsonl (independent of stream.py).

    This is the reliability fix for Run 1's lost logs — when stream.py restarts,
    decisions posted via HTTP are silently dropped. cmd.py now writes every event
    to the log file itself, so the full run log always exists even if stream.py
    is down.

    Each event gets a unique sequence number to distinguish legitimate repeated
    actions (e.g., playing Strike twice) from tool-retry duplicates.
    """
    global _event_seq
    _event_seq += 1
    event["seq"] = _event_seq
    try:
        os.makedirs(os.path.dirname(EVENT_LOG), exist_ok=True)
        with open(EVENT_LOG, "a") as f:
            f.write(json.dumps(event) + "\n")
    except OSError:
        pass


def _snapshot(raw: dict) -> dict:
    """Extract a compact state snapshot from raw game state for logging."""
    gs = raw.get("game_state") or {}
    screen = gs.get("screen_type")
    snap = {
        "floor": gs.get("floor"),
        "hp": gs.get("current_hp"),
        "max_hp": gs.get("max_hp"),
        "gold": gs.get("gold"),
        "screen": screen,
    }
    combat = gs.get("combat_state")
    if combat:
        player = combat.get("player") or {}
        snap["block"] = player.get("block", 0)
        snap["energy"] = player.get("energy", 0)
        snap["hand"] = [c.get("name", "?") for c in combat.get("hand", [])]
        # Powers included so audits can verify buff/debuff claims — their absence
        # made a true burning-elite observation unverifiable (audits 228/229).
        snap["enemies"] = [
            {k: v for k, v in {
                "name": monster_name(m), "hp": m.get("current_hp"),
                "intent": m.get("intent"),
                "powers": [f"{p.get('name', '?')} {p.get('amount', '')}".strip()
                           for p in m.get("powers", [])] or None,
            }.items() if v is not None}
            for m in combat.get("monsters", []) if not m.get("is_gone")
        ]
        snap["player_powers"] = [
            f"{p.get('name', '?')} {p.get('amount', '')}".strip()
            for p in player.get("powers", [])
        ] or None
        snap["orbs"] = [
            {"name": o.get("name"), "passive": o.get("passive_amount"), "evoke": o.get("evoke_amount")}
            for o in combat.get("orbs", [])
        ] if combat.get("orbs") else None
    # Include map data on MAP screen (once per act for route analysis)
    if screen == "MAP":
        map_data = gs.get("map", [])
        if map_data:
            snap["map"] = _compact_map(map_data)
            boss = gs.get("act_boss")
            if boss:
                snap["boss"] = boss
    return {k: v for k, v in snap.items() if v is not None}


def _compact_map(map_data: list) -> list:
    """Compress full map data into a compact per-floor summary for the run log.

    Each entry: {"floor": N, "nodes": [{"x": X, "type": "M", "children": [X2, X3]}]}
    """
    floors = {}
    for node in map_data:
        y = node.get("y", 0)
        if y not in floors:
            floors[y] = []
        floors[y].append({
            "x": node.get("x"),
            "type": node.get("symbol", "?"),
            "children": [c.get("x") for c in node.get("children", [])],
        })
    return [
        {"floor": y + 1, "nodes": sorted(nodes, key=lambda n: n.get("x", 0))}
        for y, nodes in sorted(floors.items())
    ]


def _log_result(raw: dict):
    """Log the game state after a command executes."""
    event = {
        "type": "result",
        "state": _snapshot(raw),
        "timestamp": time.time(),
    }
    _log_event(event)


# ---------------------------------------------------------------------------
# Run capture — writes permanent run JSON on GAME_OVER
# ---------------------------------------------------------------------------

_game_over_handled = False
_potion_skip_warned = False
# Snapshot of HAND_SELECT card list from when the screen first appeared.
# Used to translate numeric indices across selections (cards get removed, shifting indices).
_hand_select_snapshot = None


def _get_next_run_number() -> int:
    """Get the next run number by finding the highest existing run file.

    Looks at actual filenames in analyst/runs/ to avoid collisions.
    Run numbers have gaps (from migration), so total_runs != max run number.
    """
    import glob as _glob
    existing = _glob.glob(os.path.join(RUNS_DIR, "run_*.json"))
    if not existing:
        return 1
    max_num = 0
    for path in existing:
        name = os.path.basename(path)
        try:
            num = int(name.replace("run_", "").replace(".json", ""))
            max_num = max(max_num, num)
        except ValueError:
            continue
    return max_num + 1


def _read_events_for_run() -> list:
    """Read all events from stream_events.jsonl for the run log.

    Returns all meaningful event types — the complete record of everything
    the player did, thought, looked up, and what happened.
    """
    events = []
    try:
        with open(EVENT_LOG, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    e = json.loads(line)
                    t = e.get("type")
                    if t == "decision":
                        events.append({
                            "type": "decision",
                            "command": e.get("command", ""),
                            "translated": e.get("translated", ""),
                            "reasoning": e.get("reasoning", ""),
                        })
                    elif t == "result":
                        events.append({
                            "type": "result",
                            "state": e.get("state", {}),
                        })
                    elif t == "plan":
                        events.append({
                            "type": "plan",
                            "mode": e.get("mode", ""),
                            "summary": e.get("summary", ""),
                        })
                    elif t == "feed":
                        events.append({
                            "type": "feed",
                            "text": e.get("text", ""),
                        })
                    elif t == "reason":
                        events.append({
                            "type": "reason",
                            "topic": e.get("topic", ""),
                            "category": e.get("category", ""),
                        })
                    elif t == "think":
                        events.append({
                            "type": "think",
                            "label": e.get("label", ""),
                            "reasoning": e.get("reasoning", ""),
                        })
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        pass
    return events


def _write_run_log(gs: dict, victory: bool):
    """Write structured run log to analyst/runs/run_NNN.json.

    Includes full game state (deck, relics, potions, HP, gold, seed) plus
    every decision and its result from the event log.
    """
    run_number = _get_next_run_number()
    os.makedirs(RUNS_DIR, exist_ok=True)

    deck = [c.get("name", "?") for c in gs.get("deck", [])]
    relics = [r.get("name", "?") for r in gs.get("relics", [])]
    potions = [p.get("name", "Empty") for p in gs.get("potions", []) if p.get("name")]
    events = _read_events_for_run()

    run_data = {
        "run": run_number,
        "character": gs.get("class", "UNKNOWN"),
        "ascension": gs.get("ascension_level", 0),
        "victory": victory,
        "floor": gs.get("floor", 0),
        "deck": deck,
        "relics": relics,
        "potions": potions,
        "gold": gs.get("gold", 0),
        "hp": gs.get("current_hp", 0),
        "max_hp": gs.get("max_hp", 0),
        "seed": gs.get("seed"),
        "events": events,
    }

    path = os.path.join(RUNS_DIR, f"run_{run_number:03d}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(run_data, f, indent=2)

    # Clear the event log now that the run JSON is written.
    # cmd.py owns this lifecycle — stream.py archives but does not clear.
    try:
        with open(EVENT_LOG, "w") as f:
            pass
    except OSError:
        pass

    # Reset the awareness session dedup cache so the next run starts fresh (same
    # lifecycle as the event log above). Guarded: the live bot must never crash
    # because the Praxis tool tree is unavailable.
    try:
        if ROOT not in sys.path:
            sys.path.insert(0, ROOT)
        from tools.awareness import reset as _aw_reset, AwarenessConfig
        _aw_reset(session=_SESSION_ID, reason="run-complete",
                  config=AwarenessConfig(knowledge_root=ROOT, domain="sts1"))
    except Exception:
        pass

    # Regenerate stats
    try:
        regen = os.path.join(_BASE_DIR, "regen_stats.py")
        subprocess.run([sys.executable, regen], cwd=_BASE_DIR,
                       timeout=10, capture_output=True)
    except Exception:
        pass

    # Tell stream.py to reload stats
    try:
        req = urllib.request.Request(
            "http://127.0.0.1:3002/reload",
            method="POST",
            headers={"Content-Type": "application/json"},
        )
        urllib.request.urlopen(req, timeout=5)
    except Exception:
        pass

    return run_number, path


def _check_game_over(raw: dict):
    """Check if the game just ended. If so, write the run log.

    Called after every send(). Fires once per run — idempotency is a FILE
    marker keyed by the ending (every play.py call is a fresh process, so the
    in-memory flag let a second GAME_OVER proceed write a duplicate run log:
    run_240/241 were the same death).
    """
    global _game_over_handled
    gs = raw.get("game_state") or {}
    screen = gs.get("screen_type")

    if screen == "GAME_OVER" and not _game_over_handled:
        marker = os.path.join(_BASE_DIR, "data", "gameover_captured.flag")
        ending = f"{gs.get('seed', '?')}|{gs.get('floor', '?')}"
        try:
            if os.path.exists(marker) and open(marker).read().strip() == ending:
                _game_over_handled = True
                return
            with open(marker, "w") as f:
                f.write(ending)
        except OSError:
            pass
        _game_over_handled = True
        ss = gs.get("screen_state", {})
        victory = ss.get("victory", False)
        try:
            run_num, path = _write_run_log(gs, victory)
            outcome = "VICTORY" if victory else "DEFEAT"
            print(f"\n{'='*50}", file=sys.stderr)
            print(f"  RUN {run_num} — {outcome} (floor {gs.get('floor', '?')})", file=sys.stderr)
            print(f"  Saved to {path}", file=sys.stderr)
            print(f"{'='*50}\n", file=sys.stderr)
        except Exception as e:
            print(f"[cmd] Failed to write run log: {e}", file=sys.stderr)
    elif screen != "GAME_OVER" and _game_over_handled:
        # Reset for next run
        _game_over_handled = False


def _post_decision(command: str, reasoning: str = "", translated_override: str = None,
                    skip_feed: bool = False):
    """Post decision to stream server AND log directly to file."""
    translated = translated_override or _translate_command(command)
    event = {
        "type": "decision",
        "command": command,
        "translated": translated,
        "reasoning": reasoning,
        "skip_feed": skip_feed,
        "timestamp": time.time(),
    }
    # Always log to file (survives stream.py restarts)
    _log_event(event)
    # Also post to stream server for live overlay (best-effort)
    try:
        data = json.dumps({
            "command": command,
            "translated": translated,
            "reasoning": reasoning,
            "skip_feed": skip_feed,
        }).encode()
        req = urllib.request.Request(
            STREAM_URL, data=data,
            headers={"Content-Type": "application/json"},
        )
        urllib.request.urlopen(req, timeout=1)
    except Exception:
        pass  # Stream server might not be running


def _post_feed(text: str, highlight: bool = False):
    """Post a feed-only entry to stream server AND log directly to file."""
    event = {
        "type": "feed",
        "text": text,
        "highlight": highlight,
        "timestamp": time.time(),
    }
    _log_event(event)
    try:
        data = json.dumps({"text": text, "highlight": highlight}).encode()
        req = urllib.request.Request(
            STREAM_URL.replace("/decision", "/feed"),
            data=data,
            headers={"Content-Type": "application/json"},
        )
        urllib.request.urlopen(req, timeout=1)
    except Exception:
        pass


def send(command: str, reason: str = "") -> str:
    """Send a command and return the resulting game state.

    Args:
        command: The game command to send. Card references in play commands
                 can be indices (1-indexed) or card names:
                   "play 3 0"          — play card at index 3 targeting enemy 0
                   "play Bash 0"       — play Bash targeting enemy 0 (resolved automatically)
                   "play Shrug It Off" — play Shrug It Off (no target)
                 Using card names avoids index-shift errors when playing multiple cards.
        reason: REQUIRED — reasoning for the overlay/stream. Explain WHY
                you're making this decision. Viewers need to see your thinking.
                The action will not execute without reasoning.

    Commands:
        play N [target]     — Play card N (1-indexed) at optional target
        end                 — End turn
        choose N            — Choose option N (events, map, rewards, shop)
        choose <name>       — Choose by name (e.g., choose rest, choose smith, choose purge)
        proceed             — Confirm/proceed button
        return              — Skip/cancel/leave button
        potion use N [T]    — Use potion in slot N on optional target T
        potion discard N    — Discard potion in slot N
        start CLASS [A] [S] — Start run (IRONCLAD/THE_SILENT/DEFECT/WATCHER, ascension, seed)
        state               — Re-request state
        key K [timeout]     — Press key K
        wait T              — Wait T frames (game time)
    """
    if not reason or not reason.strip():
        return (
            "[ERROR] reason= is REQUIRED. Explain WHY you're making this decision.\n"
            "Example: send('play Bash 0', reason='Applying Vulnerable for damage amplification next turn')\n"
            "The stream overlay shows your reasoning to viewers — it cannot be empty."
        )
    # Fetch pre-command state so translation has current hand/enemies
    global _last_raw_state
    _remember(_tcp_request({"type": "state"}))

    # Guard: prevent proceed on BOSS_REWARD (must choose a relic first)
    gs = (_last_raw_state or {}).get("game_state") or {}
    screen = gs.get("screen_type", "")
    cmd_verb = command.strip().split()[0].lower() if command.strip() else ""
    if cmd_verb == "proceed" and screen == "BOSS_REWARD":
        return (
            "[ERROR] Cannot proceed on BOSS_REWARD — you must choose a relic first!\n"
            "Use: send('choose 0', reason='...') to pick a boss relic.\n"
            "Skipping a boss relic is a devastating misplay."
        )

    # Guard: warn when proceeding past unclaimed potions with empty slots.
    # Uses a flag so the warning only fires once — second proceed goes through.
    global _potion_skip_warned
    if cmd_verb == "proceed" and screen == "COMBAT_REWARD":
        ss = gs.get("screen_state", {})
        rewards = ss.get("rewards", [])
        potions_available = [r for r in rewards if r.get("reward_type") == "POTION"]
        if potions_available and not _potion_skip_warned:
            player_potions = gs.get("potions", [])
            has_empty = any(p.get("id") == "Potion Slot" for p in player_potions)
            if has_empty:
                potion_names = [r.get("potion", {}).get("name", "?") for r in potions_available]
                _potion_skip_warned = True
                return (
                    f"[WARNING] You're leaving a potion behind with empty slots!\n"
                    f"Available: {', '.join(potion_names)}\n"
                    f"You have empty potion slots. Pick up the potion first with choose,\n"
                    f"or send proceed again if you intentionally want to skip it."
                )
    if screen != "COMBAT_REWARD":
        _potion_skip_warned = False

    # Guard: prevent choosing a potion reward when all potion slots are full.
    # CommunicationMod hangs/crashes if you try to pick up a potion with no empty slots.
    if cmd_verb == "choose" and screen == "COMBAT_REWARD":
        parts = command.strip().split()
        if len(parts) >= 2:
            try:
                reward_idx = int(parts[1])
                ss = gs.get("screen_state", {})
                rewards = ss.get("rewards", [])
                if 0 <= reward_idx < len(rewards):
                    reward = rewards[reward_idx]
                    if reward.get("reward_type") == "POTION":
                        potions = gs.get("potions", [])
                        has_empty = any(p.get("id") == "Potion Slot" for p in potions)
                        if not has_empty:
                            potion_name = reward.get("potion", {}).get("name", "potion")
                            return (
                                f"[ERROR] Cannot pick up {potion_name} — all potion slots are full!\n"
                                f"Current potions: {', '.join(p.get('name', '?') for p in potions)}\n"
                                f"Use potion_discard(slot, reason='...') to free a slot first, "
                                f"or use proceed to leave rewards."
                            )
            except ValueError:
                pass  # Non-numeric choose argument, pass through

    # HAND_SELECT snapshot: track the card list from when the screen first appeared.
    # When the agent sends 'choose 3', it means "the card at position 3 when I first
    # saw this screen." After each selection a card is removed and indices shift —
    # we translate the original index to the correct current index.
    global _hand_select_snapshot
    if screen == "HAND_SELECT":
        ss = gs.get("screen_state", {})
        current_cards = ss.get("hand", [])
        if _hand_select_snapshot is None:
            _hand_select_snapshot = list(current_cards)
        # Resolve numeric choose against snapshot
        if cmd_verb == "choose" and _hand_select_snapshot:
            command = _resolve_choose_from_snapshot(
                _hand_select_snapshot, current_cards, command
            )
    else:
        _hand_select_snapshot = None  # Clear when leaving HAND_SELECT

    # Guard: taking a KEY from a reward forfeits the linked relic — twice a
    # chained 'choose N' grabbed the Sapphire Key while the plan named the relic
    # (Sundial, War Paint). Warn once; an identical second choose proceeds.
    _key_flag = os.path.join(_BASE_DIR, "data", "key_confirm.flag")
    _expect_key = None
    if cmd_verb == "choose" and screen in ("COMBAT_REWARD", "CHEST"):
        parts_k = command.strip().split()
        if len(parts_k) >= 2 and parts_k[1].isdigit():
            rewards_k = gs.get("screen_state", {}).get("rewards", [])
            ridx = int(parts_k[1])
            if (0 <= ridx < len(rewards_k)
                    and rewards_k[ridx].get("reward_type") in ("SAPPHIRE_KEY", "EMERALD_KEY")):
                # Flag is a FILE: every play.py call is a fresh process, so an
                # in-memory flag warned forever and made keys uncollectable.
                if not os.path.exists(_key_flag):
                    with open(_key_flag, "w") as f:
                        f.write(str(ridx))
                    return ("[WARNING] choose {} selects the KEY - taking it forfeits "
                            "the linked relic. If you want the relic, choose its index "
                            "instead. If the key is intended, send the same choose "
                            "again.".format(ridx))
                os.remove(_key_flag)
                _expect_key = rewards_k[ridx]["reward_type"]
    elif os.path.exists(_key_flag):
        os.remove(_key_flag)

    # Guard: cancel/skip on a GRID selection screen has frozen CommunicationMod
    # (states stop flowing; required killing and relaunching the game). Refuse it.
    if cmd_verb in ("return", "cancel", "skip") and screen == "GRID":
        return (
            "[ERROR] cancel/skip on a card-selection grid can FREEZE the game "
            "(confirmed — required a full game restart). Complete the selection "
            "instead: choose <index> the required number of times, then proceed "
            "if a confirm is needed."
        )

    # MAP screens: support choosing by node type or x-coordinate, and resolve to
    # an index locally. Blind 'choose N' misroutes have decided runs.
    if cmd_verb == "choose" and screen == "MAP":
        command = _resolve_map_choose(gs, command)
        if command.startswith("[ERROR]"):
            return command

    # Resolve card names to indices using current hand state
    resolved = _resolve_card_name(_last_raw_state, command)
    if resolved.startswith("[ERROR]"):
        return resolved  # e.g., ambiguous enemy name — don't execute
    # Resolve card names in choose commands (HAND_SELECT, CARD_REWARD, GRID)
    resolved = _resolve_choose_card_name(_last_raw_state, resolved)
    # Resolve shop card/relic names to indices
    resolved = _resolve_shop_choose(_last_raw_state, resolved)
    # Resolve relic/potion names on reward screens
    resolved = _resolve_reward_choose(_last_raw_state, resolved)

    # Resolve what a choose actually selects BEFORE executing, and echo it at the
    # top of the response. Two consecutive runs were decided by an unverified
    # 'choose N' picking something other than what the reasoning named (a map
    # misroute; a chest taking the Sapphire Key while the plan said Meal Ticket).
    # The echo makes the selection visible in the very next thing the player reads.
    chose_echo = ""
    chose_label = ""
    if cmd_verb == "choose":
        chose_label = _translate_command(resolved)
        if chose_label and chose_label != resolved:
            chose_echo = f"[chose: {chose_label}]\n\n"

    def _fingerprint(r):
        g = (r or {}).get("game_state") or {}
        c = g.get("combat_state") or {}
        return (g.get("screen_type"), g.get("floor"), g.get("current_hp"),
                g.get("gold"), len(c.get("hand", [])),
                (c.get("player") or {}).get("energy"))

    pre_fp = _fingerprint(_last_raw_state)
    _post_decision(resolved, reason)
    raw = _tcp_request({"type": "command", "command": resolved})
    _remember(raw)  # Update cache (healthy responses only)
    stale_note = ""
    if cmd_verb not in ("state", "wait") and _healthy_state(raw) and _fingerprint(raw) == pre_fp:
        # The relay can return before the command processes; a blind retry then
        # double-fires it (one campfire healed twice this way). Say so.
        stale_note = ("[NOTE: state unchanged after this command - it may still be "
                      "processing. Re-read state before retrying; do NOT resend blindly.]\n\n")

    # The echo must not claim a choice happened when the command failed.
    if chose_echo and ("error" in raw
                       or (raw.get("in_game") and not raw.get("game_state"))):
        chose_echo = f"[attempted: {chose_label} — command FAILED, see error below]\n\n"

    # Auto-handle mechanical transitions (gold, chests, shop wait, intent settle)
    # BEFORE logging — the log must record the state the player actually saw,
    # not the transient pre-settle frame.
    raw = _auto_handle_mechanical(raw)
    _log_result(raw)
    _check_game_over(raw)

    # Confirmed key picks: verify possession — the relay's response to a key
    # choose is shape-identical for success and silent failure.
    if _expect_key and _healthy_state(raw):
        _g = raw.get("game_state") or {}
        _got = _g.get("has_emerald_key") if _expect_key == "EMERALD_KEY" else _g.get("has_sapphire_key")
        if not _got:
            stale_note = ("[WARNING] the key does NOT appear in your possession after "
                          "that choose - re-read state and retry before leaving the "
                          "screen.]\n\n") + stale_note
    return _interruption_notice(raw) + stale_note + chose_echo + format_state(raw)


def _auto_collect_gold(raw: dict) -> dict:
    """Auto-collect gold/stolen_gold from combat rewards — free value with no downside."""
    global _last_raw_state
    if not raw.get("in_game"):
        return raw
    gs = raw.get("game_state", {})
    if gs.get("screen_type") != "COMBAT_REWARD":
        return raw
    ss = gs.get("screen_state", {})
    rewards = ss.get("rewards", [])
    # Collect all gold rewards (iterate because indices shift after each pick)
    while True:
        gold_idx = None
        for i, r in enumerate(rewards):
            if r.get("reward_type") in ("GOLD", "STOLEN_GOLD"):
                gold_idx = i
                break
        if gold_idx is None:
            break
        # Pick up the gold — always beneficial, never a trade-off.
        raw = _tcp_request({"type": "command", "command": f"choose {gold_idx}"})
        _remember(raw)
        if not raw.get("in_game"):
            return raw
        gs = raw.get("game_state", {})
        if gs.get("screen_type") != "COMBAT_REWARD":
            # Gold was the only reward; screen changed. Return new state.
            return raw
        ss = gs.get("screen_state", {})
        rewards = ss.get("rewards", [])
    return raw


def _auto_wait_shop_screen(raw: dict) -> dict:
    """Wait for SHOP_ROOM → SHOP_SCREEN transition.

    When entering a shop, CommunicationMod briefly shows SHOP_ROOM (no items)
    before transitioning to SHOP_SCREEN (full inventory). This auto-retries
    state() to avoid the agent thrashing on the empty transitional state.
    """
    global _last_raw_state
    if not raw.get("in_game"):
        return raw
    gs = raw.get("game_state", {})
    if gs.get("screen_type") != "SHOP_ROOM":
        return raw
    ss = gs.get("screen_state", {})
    # If SHOP_ROOM already has items, return as-is
    if ss.get("cards") or ss.get("relics") or ss.get("potions"):
        return raw

    # Poll for SHOP_SCREEN (up to 3 seconds, 15 × 200ms)
    for _ in range(15):
        time.sleep(0.2)
        raw = _tcp_request({"type": "state"})
        _remember(raw)
        if not raw.get("in_game"):
            return raw
        gs = raw.get("game_state", {})
        if gs.get("screen_type") != "SHOP_ROOM":
            return raw
        ss = gs.get("screen_state", {})
        if ss.get("cards") or ss.get("relics") or ss.get("potions"):
            return raw
    return raw


def _auto_open_chest(raw: dict) -> dict:
    """Auto-open chests — there is never a reason not to open a chest.

    CommunicationMod shows CHEST screen for both treasure room chests and
    boss treasure chests.  The only available choice is "open".  After opening,
    the screen transitions to the relic reward (or BOSS_REWARD for boss chests).
    Calling proceed on a CHEST screen skips it entirely — a devastating bug.
    """
    global _last_raw_state
    if not raw.get("in_game"):
        return raw
    gs = raw.get("game_state", {})
    if gs.get("screen_type") != "CHEST":
        return raw
    # Send "choose 0" which corresponds to "open"
    raw = _tcp_request({"type": "command", "command": "choose 0"})
    _remember(raw)
    return raw


def _settle_debug_intents(raw: dict) -> dict:
    """Wait out unrolled enemy intents. CommunicationMod sometimes reports state
    before the game has rolled monster moves — intents read "DEBUG" (33 instances
    in one audited run), forcing blind conservative play on those turns. A short
    in-game wait lets the roll land; give up after a few tries (a few intents are
    legitimately hidden, e.g. while an enemy is stunned)."""
    global _last_raw_state

    def _has_debug(r):
        c = (r.get("game_state") or {}).get("combat_state") if r.get("in_game") else None
        if not c:
            return False
        return any(m.get("intent") == "DEBUG"
                   for m in c.get("monsters", []) if not m.get("is_gone"))

    if not _has_debug(raw):
        return raw
    tries = 0
    for _ in range(3):
        tries += 1
        nxt = _tcp_request({"type": "command", "command": "wait 30"})
        if not isinstance(nxt, dict) or "game_state" not in nxt:
            break                       # wait unsupported/errored — keep what we have
        raw = nxt
        _remember(raw)
        if not _has_debug(raw):
            break
    _log_event({"type": "settle_intents", "tries": tries,
                "resolved": not _has_debug(raw), "timestamp": time.time()})
    return raw


def _auto_handle_mechanical(raw: dict) -> dict:
    """Handle mechanical transitions that never involve a real decision."""
    raw = _auto_collect_gold(raw)
    raw = _auto_open_chest(raw)
    raw = _auto_wait_shop_screen(raw)
    raw = _settle_debug_intents(raw)
    return raw


def _validate_action(raw: dict, action: str) -> str | None:
    """Check whether the next action in a turn sequence is still valid.

    Returns None if valid, or a reason string if the action should be skipped
    (and the sequence stopped).
    """
    # 1. Still in game?
    if not raw.get("in_game"):
        return "not in game"

    gs = raw.get("game_state", {})
    combat = gs.get("combat_state")

    # 2. Still in combat?
    if not combat:
        screen = gs.get("screen_type", "unknown")
        return f"combat ended (screen: {screen})"

    parts = action.strip().split()
    verb = parts[0].lower() if parts else ""

    # 3. "end" is always valid during combat
    if verb == "end":
        return None

    # 4. "play N [target]" — validate card index and playability
    if verb == "play":
        if len(parts) < 2:
            return "play command missing card index"
        try:
            card_n = int(parts[1])
        except ValueError:
            return f"invalid card index: {parts[1]}"

        hand = combat.get("hand", [])
        if card_n < 1 or card_n > len(hand):
            return f"card index {card_n} out of range (hand has {len(hand)} cards)"

        card = hand[card_n - 1]
        if not card.get("is_playable", False):
            card_name = card.get("name", f"card {card_n}")
            return f"{card_name} is not playable (likely not enough energy)"

        # Validate target if specified (absolute index into full monsters array)
        if len(parts) > 2:
            try:
                target_idx = int(parts[2])
            except ValueError:
                return f"invalid target index: {parts[2]}"
            monsters = combat.get("monsters", [])
            if target_idx < 0 or target_idx >= len(monsters):
                return f"target index {target_idx} out of range ({len(monsters)} monsters)"
            if monsters[target_idx].get("is_gone"):
                return f"target {target_idx} ({monsters[target_idx].get('name', '?')}) is dead/gone"

        return None

    # 5. Potion commands — always valid (rare errors, recoverable)
    if verb == "potion":
        return None

    # Unknown verb — let it through, relay will handle errors
    return None


# Cards that ADD energy mid-turn — a batch containing one can't be summed naively.
_ENERGY_GAINERS = {"seeing red", "bloodletting", "offering", "adrenaline",
                   "turbo", "double energy", "aggregate", "concentrate"}


def _batch_energy_check(snapshot_hand: list, energy: int, actions: list) -> str | None:
    """Sum the energy cost of a turn() batch against available energy.

    Returns an error string when the plan is over budget, or None when it fits
    (or can't be safely summed: an energy-gaining card in the batch, a card not
    found in the hand snapshot, or an X-cost card — those consume the remainder
    and can't overdraw)."""
    remaining = list(snapshot_hand)  # multiset — duplicates consumed one at a time
    total = 0
    lines = []
    for a in actions:
        parts = a.strip().split()
        if not parts or parts[0].lower() != "play":
            continue
        ref = " ".join(parts[1:-1]) if len(parts) > 2 and parts[-1].isdigit() else " ".join(parts[1:])
        card = None
        if ref.isdigit():                      # snapshot 1-indexed position
            idx = int(ref) - 1
            if 0 <= idx < len(snapshot_hand):
                card = snapshot_hand[idx]
        else:
            for cand in remaining:
                if cand.get("name", "").lower() == ref.lower():
                    card = cand
                    remaining.remove(cand)
                    break
        if card is None:
            return None                        # can't identify — don't guess
        if card.get("name", "").lower() in _ENERGY_GAINERS:
            return None                        # energy math not naively summable
        cost = card.get("cost", 0)
        if cost is None or cost < 0:           # X-cost / unplayable markers
            if cost == -1 and a is not actions[-1] and any(
                    x.strip().lower().startswith("play ")
                    for x in actions[actions.index(a) + 1:]):
                return ("[ERROR] An X-cost card consumes ALL remaining energy when "
                        "played - nothing after it in the batch can be paid for. "
                        "Play the X-cost card LAST (combat.md rule 3), or spend the "
                        "energy you want to keep BEFORE it.")
            cost = 0
        total += cost
        lines.append(f"  {card.get('name', '?')} = {cost}E")
    if total > energy:
        return (f"[ERROR] Batch plans {total}E but you have {energy}E:\n"
                + "\n".join(lines) +
                f"\n  total = {total}E > {energy}E available.\n"
                "Trim the plan and resend. (X-cost cards count as 0 here; if the plan "
                "relies on an energy-gaining card, play it via send() first.)")
    return None


def turn(actions: list, reason: str = "") -> str:
    """Execute a full combat turn as a batch.

    Plan your entire turn, then execute it all at once. This is how you
    should play combat — reason about your whole hand, figure out the
    optimal sequence, then commit.

    Card references can be indices (1-indexed) or card names:
      "play 3 0"           — play card at index 3 targeting enemy 0
      "play Bash 0"        — play Bash targeting enemy 0 (index resolved automatically)
      "play Shrug It Off"  — play Shrug It Off (no target)
    Using card names avoids index-shift errors when playing multiple cards.

    Args:
        actions: List of command strings, e.g. ["play Bash 0", "play Strike 0", "play Defend", "end"]
                 Card names are resolved against the current hand at execution time,
                 so they're always correct regardless of what was played before.
                 Numeric indices still work: ["play 3 0", "play 2 0", "end"]
                 but indices shift as you play cards — names don't.
        reason: Your reasoning for the whole turn. Shows on stream overlay.

    Returns:
        Final game state after all actions executed.

    If any action fails validation (combat ended, card unplayable, etc.),
    the sequence stops early and returns the current state with a note
    about what happened.
    """
    if not actions:
        return state()

    if not reason or not reason.strip():
        return (
            "[ERROR] reason= is REQUIRED. Explain your combat plan.\n"
            "Example: turn(['play Bash 0', 'play Strike 0', 'end'],\n"
            "         reason='Bash for Vulnerable, Strike for 9 damage. 5 block vs 12 incoming, take 7 to 58 HP.')\n"
            "The stream overlay shows your reasoning to viewers — it cannot be empty."
        )

    # Fetch pre-turn state for translation and snapshot
    global _last_raw_state
    _remember(_tcp_request({"type": "state"}))

    # Snapshot the hand at turn start for index stability.
    # When the agent says "play 3 0", it means "the card I see at position 3."
    # As cards are played and indices shift, we use this snapshot to find
    # the intended card in the current hand by identity (name + upgrades).
    pre_combat = ((_last_raw_state or {}).get("game_state") or {}).get("combat_state")
    snapshot_hand = list(pre_combat.get("hand", [])) if pre_combat else []

    # Energy pre-check: refuse batches that plan more energy than is available.
    # Over-planned batches (4E of cards on 3E turns) recurred across runs no
    # matter how the discipline was worded; tool-level guards are what actually
    # stopped the comparable choose-N error family.
    # Skipped when a relic discounts costs MID-turn (Mummified Hand zeroes a
    # random card per Power play) — snapshot costs cannot model that, and the
    # guard false-positived on an affordable batch (run 235).
    _discount_relics = {"mummified hand", "necronomicon"}
    _gs_now = (_last_raw_state or {}).get("game_state") or {}
    _has_discounter = any(r.get("name", "").lower() in _discount_relics
                          for r in _gs_now.get("relics", []))
    if pre_combat and not _has_discounter:
        energy_err = _batch_energy_check(
            snapshot_hand, (pre_combat.get("player") or {}).get("energy", 0), actions)
        if energy_err:
            return energy_err

    # Resolve and translate all actions using pre-turn state for the stream
    # (Translation uses original names for readability; resolution happens per-action below)
    translated_actions = [_translate_command(_resolve_card_name(_last_raw_state, a)) for a in actions]
    translated_summary = " → ".join(translated_actions)

    # Post the full plan as one entry in both reasoning and feed
    _post_decision(
        command="; ".join(actions),
        reasoning=reason,
        translated_override=translated_summary,
    )

    total = len(actions)
    stopped_msg = None

    # Execute each action, resolving card references against CURRENT state
    for i, action in enumerate(actions):
        # For numeric indices: translate from snapshot position to current position.
        # For names: pass through to _resolve_card_name which handles them correctly.
        resolved_action = _resolve_play_from_snapshot(snapshot_hand, _last_raw_state, action)
        resolved_action = _resolve_card_name(_last_raw_state, resolved_action)
        if resolved_action.startswith("[ERROR]"):
            # e.g., ambiguous enemy name — stop without executing
            stopped_msg = (
                f"[SEQUENCE STOPPED at action {i + 1}/{total}: "
                f"{resolved_action.removeprefix('[ERROR]').strip()} "
                f"Remaining actions skipped.]"
            )
            break

        # Validate before sending (uses current game state)
        if i > 0:
            # First action uses pre-turn state which may not have combat_state
            # fields populated the same way; skip validation for it.
            # After the first action, we have fresh state from the relay.
            fail_reason = _validate_action(_last_raw_state, resolved_action)
            if fail_reason:
                stopped_msg = (
                    f"[SEQUENCE STOPPED after action {i}/{total}: "
                    f"{fail_reason}. Remaining actions skipped.]"
                )
                break

        # Capture hand size before action to detect draws
        pre_combat = ((_last_raw_state or {}).get("game_state") or {}).get("combat_state")
        pre_hand_size = len(pre_combat.get("hand", [])) if pre_combat else None

        raw = _tcp_request({"type": "command", "command": resolved_action.strip()})
        _remember(raw)
        if "error" in raw:
            # Auto-handle mechanical transitions even on error
            _remember(_auto_handle_mechanical(_last_raw_state))
            return format_state(_last_raw_state)

        # A choice screen opened mid-batch (potion card choice, Warcry discard,
        # combat over) — stop cleanly instead of crashing the next action into it.
        new_screen = (raw.get("game_state") or {}).get("screen_type", "")
        if (new_screen in ("HAND_SELECT", "GRID", "CARD_REWARD", "COMBAT_REWARD")
                and i < total - 1):
            stopped_msg = (
                f"[SEQUENCE STOPPED after action {i + 1}/{total}: {new_screen} opened — "
                f"resolve it with choose/proceed, then continue with send()]"
            )
            break

        # Detect draw: if we played a card but hand size didn't shrink, cards were drawn.
        # Stop the sequence so the player can see the new cards and re-plan.
        if (pre_hand_size is not None
                and resolved_action.startswith("play ")
                and i < total - 1  # more actions remain
                and actions[i + 1] != "end"  # next action isn't just "end" -- that's harmless to stop before
                ):
            post_combat = ((_last_raw_state or {}).get("game_state") or {}).get("combat_state")
            if post_combat:
                post_hand_size = len(post_combat.get("hand", []))
                if post_hand_size >= pre_hand_size:
                    # Hand didn't shrink — draw happened. Stop sequence.
                    remaining_actions = actions[i + 1:]
                    stopped_msg = (
                        f"[DRAW DETECTED after playing {resolved_action}: "
                        f"hand went from {pre_hand_size} to {post_hand_size} cards. "
                        f"Remaining actions skipped: {remaining_actions}. "
                        f"You drew new cards — read the state and plan the rest of your turn.]"
                    )
                    break

    # Check for game over (player may have died during the turn)
    _check_game_over(_last_raw_state)

    # Auto-handle mechanical transitions after the turn completes
    _remember(_auto_handle_mechanical(_last_raw_state))

    formatted = _interruption_notice(_last_raw_state) + format_state(_last_raw_state)
    if stopped_msg:
        return stopped_msg + "\n\n" + formatted
    return formatted


def play(card, target: int = None, reason: str = "") -> str:
    """Play a card by index or name. Target is enemy index (0-indexed), required for targeted cards.

    Args:
        card: Card index (1-indexed int) or card name (str).
              Examples: 3, "Bash", "Shrug It Off", "Bash+"
        target: Enemy index (0-indexed), required for targeted attack cards.
        reason: REQUIRED — why you're playing this card.
    """
    if target is not None:
        return send(f"play {card} {target}", reason=reason)
    return send(f"play {card}", reason=reason)


def end(reason: str = "End turn") -> str:
    """End turn."""
    return send("end", reason=reason)


_MAP_NODE_NAMES = {"M": "monster", "?": "unknown", "$": "shop",
                   "E": "elite", "R": "rest", "T": "treasure", "B": "boss"}


def _resolve_map_choose(gs: dict, command: str) -> str:
    """On MAP screens, resolve 'choose <type|x=N|index>' to 'choose <index>'.

    Numeric indices pass through (the post-send echo names what they picked).
    Type names ('choose rest', 'choose elite') and coordinates ('choose x=3')
    resolve locally; an ambiguous or unknown name errors with the labeled node
    list instead of guessing — a blind misroute loses runs.
    """
    parts = command.strip().split()
    if len(parts) < 2:
        return command
    arg = " ".join(parts[1:]).strip().lower()
    nodes = gs.get("screen_state", {}).get("next_nodes", [])
    if not nodes:
        # Pre-boss floor: the boss is the only (unlisted) choice at index 0.
        if arg == "boss":
            return "choose 0"
        return command
    try:
        int(arg)
        return command                      # numeric — pass through, echo covers it
    except ValueError:
        pass

    def options_list():
        return "\n".join(
            f"  [{i}] {_MAP_NODE_NAMES.get(n.get('symbol', '?'), n.get('symbol', '?'))} (x={n.get('x', '?')})"
            for i, n in enumerate(nodes))

    m = re.fullmatch(r"x\s*=?\s*(\d+)", arg)
    if m:
        x = int(m.group(1))
        hits = [i for i, n in enumerate(nodes) if n.get("x") == x]
    else:
        wanted = {"rest": "R", "rest site": "R", "campfire": "R", "monster": "M",
                  "fight": "M", "unknown": "?", "event": "?", "shop": "$",
                  "store": "$", "elite": "E", "treasure": "T", "chest": "T",
                  "boss": "B"}.get(arg)
        if wanted is None:
            return (f"[ERROR] '{arg}' is not a map node type. Available paths:\n"
                    f"{options_list()}\n"
                    f"Use: choose <index>, choose <type> (rest/monster/elite/shop/"
                    f"unknown/treasure/boss), or choose x=<N>.")
        hits = [i for i, n in enumerate(nodes) if n.get("symbol") == wanted]
    if len(hits) == 1:
        return f"choose {hits[0]}"
    if not hits:
        return (f"[ERROR] no '{arg}' node among the available paths:\n{options_list()}")
    return (f"[ERROR] '{arg}' is ambiguous — {len(hits)} matching nodes. "
            f"Use choose x=<N>:\n{options_list()}")


def choose(option, reason: str = "") -> str:
    """Choose an option by index or name. reason= is REQUIRED."""
    return send(f"choose {option}", reason=reason)


def proceed(reason: str = "Proceeding") -> str:
    """Press proceed/confirm."""
    return send("proceed", reason=reason)


def skip(reason: str = "Skipping") -> str:
    """Press skip/cancel/leave."""
    return send("return", reason=reason)


def potion_use(slot, target: int = None, reason: str = "") -> str:
    """Use a potion by SLOT NUMBER or by NAME. reason= is REQUIRED.

    Prefer names: slots renumber after every drink, so two `potion_use(0)` calls
    in a row hit different potions. A name resolves against the live belt.
    Automatically strips target for non-targeted potions (Block Potion, etc.)
    to prevent silent CommunicationMod failures.
    """
    global _last_raw_state
    if isinstance(slot, str) and not slot.isdigit():
        fresh = _remember(_tcp_request({"type": "state"}))
        potions = (fresh.get("game_state") or {}).get("potions", []) if _healthy_state(fresh) else []
        matches = [i for i, p in enumerate(potions)
                   if slot.lower() in p.get("name", "").lower() and p.get("id") != "Potion Slot"]
        if len(matches) != 1:
            belt = ", ".join(f"[{i}] {p.get('name', '?')}" for i, p in enumerate(potions))
            return (f"[ERROR] potion name '{slot}' matched {len(matches)} potions. "
                    f"Belt: {belt or '(unreadable)'} — use the slot number.")
        slot = matches[0]
    slot = int(slot)
    # Check if this potion actually requires a target
    if target is not None and _last_raw_state:
        potions = ((_last_raw_state or {}).get("game_state") or {}).get("potions", [])
        if slot < len(potions) and not potions[slot].get("requires_target", False):
            target = None  # Strip invalid target for non-targeted potions
    if target is not None:
        return send(f"potion use {slot} {target}", reason=reason)
    return send(f"potion use {slot}", reason=reason)


def potion_discard(slot: int, reason: str = "") -> str:
    """Discard a potion. reason= is REQUIRED."""
    return send(f"potion discard {slot}", reason=reason)


# ---------------------------------------------------------------------------
# Knowledge planning and reasoning (ontology + heuristics)
# ---------------------------------------------------------------------------

def _current_boundaries(raw: dict) -> list[str]:
    """Which decision boundaries the live state sits on — deterministic, from the
    screen alone (the boundary is fully determined by the screen, so it must not
    depend on selector judgment). Returns awareness handles for files that exist;
    mirrors the dispatch in bot/state_formatter.format_state.
    """
    names: list[str] = []
    if not raw.get("in_game", False):
        names = ["game-start"]
    else:
        gs = raw.get("game_state", {}) or {}
        screen = gs.get("screen_type", "NONE")
        phase = gs.get("room_phase", "")
        combat = gs.get("combat_state")
        floor = gs.get("floor", 0)
        if screen == "CARD_REWARD":
            names = ["card-reward"]
        elif screen in ("GRID", "HAND_SELECT") and combat:
            names = ["turn"]
        elif (phase == "COMBAT" or screen == "NONE") and combat:
            names = ["fight-start", "turn"] if combat.get("turn", 0) <= 1 else ["turn"]
        elif screen == "EVENT":
            ev = (gs.get("screen_state", {}) or {}).get("event_name", "")
            names = ["game-start", "event"] if "neow" in ev.lower() else ["event"]
        elif screen in ("SHOP_ROOM", "SHOP_SCREEN"):
            names = ["shop"]
        elif screen == "MAP":
            # First map view of an act: floor 0 (after Neow) or a boss floor
            # (16/33/50 — floor % 17 == 16) means the next pick opens a new act.
            at_act_start = floor == 0 or floor % 17 == 16
            names = ["act-start", "node-choice"] if at_act_start else ["node-choice"]
        elif screen == "REST":
            names = ["rest-site"]
        elif screen == "COMBAT_REWARD":
            names = ["card-reward"]
        elif screen == "BOSS_REWARD":
            names = ["boss-relic"]
    handles = []
    for n in names:
        if os.path.exists(os.path.join(ROOT, "awareness", "sts1", "boundaries", f"{n}.md")):
            handles.append(f"awareness/sts1/boundaries/{n}")
    return handles


def survey() -> str:
    """Survey what knowledge applies to the current state — a menu of recall()
    handles, not content.

    Two parts. First, the decision boundary: the screen you're on determines which
    boundary index applies (turn, card-reward, shop, ...), so those handles are
    included deterministically — code, not judgment. Second, one selector call
    (a small fast model) reads the live state + the ontology map and returns the
    handles worth pulling: the on-board entities (enemies, boss, non-basic hand
    cards, relics, current event), upgraded cards, and any phenomenon whose
    conditions match right now. Judgment, not a state echo — it surfaces the
    non-obvious (combos, contextual warnings) the way a deterministic list can't.
    Returns ONLY the menu; read what you want with recall().
    """
    try:
        if ROOT not in sys.path:
            sys.path.insert(0, ROOT)
        from tools import retrieval
    except Exception as e:
        return f"survey unavailable: {e}"
    try:
        raw = state_raw()
        boundary_handles = _current_boundaries(raw)
        state_text = format_state(raw)
        handles = retrieval.survey(state_text, retrieval.load_index("sts1"))
    except Exception as e:
        return f"survey failed: {e}"
    handles = [h for h in handles if h not in boundary_handles]
    _log_event({"type": "survey", "boundaries": boundary_handles, "handles": handles,
                "timestamp": time.time()})
    lines = []
    if boundary_handles:
        lines.append("this decision's boundary — consider its index:")
        lines.extend(f"  {h}" for h in boundary_handles)
    if handles:
        lines.append("survey — recall() any of these:")
        lines.extend(f"  {h}" for h in handles)
    if not lines:
        return "survey: nothing flagged. recall() entities by name as needed."
    return "\n".join(lines)



# Category search order for bare names. MUST match SEARCH_CATEGORIES in
# tools/retrieval/build_index.py — the committed map documents this order and the
# selector reads it; a divergence makes recall() resolve differently than promised.
_ONT_CATS = ["cards", "enemies", "bosses", "relics", "potions", "events", "buffs",
             "debuffs", "encounters", "rules", "types", "characters", "acts",
             "ascension", "shop"]
_HEUR_CATS = ["cards", "enemies", "bosses", "relics", "potions", "events", "characters"]


_ALIASES = None


def _load_aliases() -> dict:
    """In-game names that don't slug to their file, parsed from the ontology map
    (awareness/sts1/survey-index.md). {name_lower: ["category/stem", ...]}. The map
    auto-detects these (e.g. "The Transient" -> enemies/transient, "Centurion +
    Mystic" -> encounters/centurion-and-mystic, "Louse" -> both lice)."""
    global _ALIASES
    if _ALIASES is not None:
        return _ALIASES
    _ALIASES = {}
    try:
        path = os.path.join(ROOT, "awareness", "sts1", "survey-index.md")
        with open(path, encoding="utf-8") as f:
            in_aliases = False
            for line in f:
                line = line.strip()
                if line.startswith("## "):
                    # Only the aliases section holds name->entry lines; later
                    # sections (phenomena applies-when) also use ":" but are
                    # selector input, not aliases.
                    in_aliases = line == "## aliases (in-game name -> entry)"
                    continue
                if not in_aliases or not line or line.startswith("#") or ":" not in line:
                    continue
                name, targets = line.split(":", 1)
                name = name.strip()
                if name == "Ascension N":          # a rule, not a literal alias
                    continue
                targets = targets.split("(")[0].strip()   # drop a trailing "(note)"
                _ALIASES[name.lower()] = [t.strip() for t in targets.split("|") if t.strip()]
    except OSError:
        pass
    return _ALIASES


def _alias_targets(name: str) -> list[tuple[str, str]]:
    """Alias resolutions for an in-game name as (category, stem) pairs."""
    return [tuple(t.partition("/")[::2]) for t in _load_aliases().get(name.strip().lower(), [])]


def _recall_one(handle: str):
    """Resolve one recall handle -> text, or None. No link-following.

    Accepts a repo path, a wiki-style address (`enemies/Gremlin Nob`,
    `layer:heuristics, cards/Bash`, `cards/Bash+`), or a bare name (searched across
    ontology categories; the heuristic needs an explicit `layer:heuristics`).
    A bare name that exists in several categories returns every match (e.g.
    "Golden Idol" is both an event and a relic). Aliases (the map's in-game names
    that don't slug to their file) apply in every layer, not just ontology.
    """
    h = handle.strip()
    first = h.split("/", 1)[0]
    if "/" in h and first in ("ontology", "heuristics", "phenomena", "goals", "awareness"):
        rel = h if h.endswith(".md") else h + ".md"
        try:
            return open(os.path.join(ROOT, rel), encoding="utf-8").read().strip()
        except OSError:
            return None
    # The map's "Ascension N -> ascension/aN" rule ("Ascension 9" -> ascension/a9).
    m = re.fullmatch(r"(?i)ascension\s+(\d+)", h)
    if m:
        return _load_ontology("ascension", f"a{m.group(1)}")
    parsed = _extract_links(f"[[{h}]]")
    if not parsed:
        return None
    layer, cat, name = parsed[0]
    if cat == "recognitions" and layer in (None, "phenomena"):
        # Recognitions live only in phenomena — route the bare category there so
        # "recognitions/potion-use" and "category:recognitions, potion-use" resolve.
        layer = "phenomena"
    if cat == "boundaries" and layer in (None, "awareness"):
        # Boundary indexes live only in awareness — "boundaries/turn" and
        # "category:boundaries, turn" route straight to the file.
        for stem in _stem_candidates(name):
            try:
                path = os.path.join(ROOT, "awareness", "sts1", "boundaries", stem + ".md")
                return open(path, encoding="utf-8").read().strip()
            except OSError:
                continue
        return None
    layer = layer or "ontology"
    is_plus = name.endswith("+")
    if is_plus and layer != "heuristics":      # "Bash+" -> the resolved phenomenon
        return _load_phenomenon(cat or "cards", name)
    loader = (_load_heuristic if layer == "heuristics"
              else _load_phenomenon if layer == "phenomena"
              else _load_ontology)
    if cat:
        txt = loader(cat, name)
        if txt:
            return txt
        for tcat, stem in _alias_targets(name):    # alias fallback, same category
            if tcat == cat:
                txt = loader(cat, stem)
                if txt:
                    return txt
        return None
    cats = _HEUR_CATS if layer == "heuristics" else _ONT_CATS
    texts = []   # (address, text) — several categories can share a name
    if layer == "heuristics":
        # Root-level topic files (combat.md, map.md, hp-management.md, ...) —
        # "layer:heuristics, combat" must reach them; they have no category.
        for stem in _stem_candidates(name):
            e = _load_heuristic_root(stem + ".md")
            if e:
                texts.append((name, e))
                break
    for c in cats:
        e = loader(c, name)
        if e:
            texts.append((f"{c}/{name}", e))
    if not texts:
        for tcat, stem in _alias_targets(name):
            e = loader(tcat, stem)
            if e:
                texts.append((f"{tcat}/{stem}", e))
    if not texts:
        return None
    if len(texts) == 1:
        return texts[0][1]
    return "\n\n---\n\n".join(f"({addr})\n{e}" for addr, e in texts)


def recall(*handles: str) -> str:
    """Fetch knowledge by handle -- the single lookup verb (replaces reason()).

    A handle is any of:
      - a path from survey()   ("phenomena/sts1/interactions/corruption-dead-branch")
      - a wiki-style address    ("enemies/Gremlin Nob", "layer:heuristics, cards/Bash")
      - a bare name             ("Gremlin Nob" -> the ontology entry)
      - an upgraded card        ("Bash+" -> the resolved phenomenon)

    Returns exactly what you ask for, each labeled by handle. Does NOT follow links --
    links in the text are a menu; recall() them too if you want them. Pass several
    handles in one call to pull several things (an entity's ontology AND heuristic =
    two handles: "enemies/Gremlin Nob", "layer:heuristics, enemies/Gremlin Nob").
    """
    if not handles:
        return "recall: needs one or more handles (a path, an address, or a name)"
    out = []
    for h in handles:
        txt = _recall_one(h)
        out.append(f"### {h}\n\n{txt}" if txt else f"### {h}\n\n(not found)")
    _post_feed(f"RECALL -- {', '.join(handles)[:60]}", highlight=False)
    _log_event({"type": "recall", "handles": list(handles), "timestamp": time.time()})
    return "\n\n---\n\n".join(out)


def deck() -> str:
    """View your full deck. Use after transforming, adding, or removing cards
    to assess how the deck changed holistically.

    Returns the full deck sorted by type (Attacks, Skills, Powers, Curses/Status),
    with costs and upgrade status.
    """
    global _last_raw_state
    prev_raw = _last_raw_state
    _remember(_tcp_request({"type": "state"}))
    gs = (_last_raw_state or {}).get("game_state") or {}
    cards = gs.get("deck", [])

    # Some screens (e.g., GRID) omit the deck — fall back to the last known one.
    note = ""
    if not cards and prev_raw:
        cards = (prev_raw.get("game_state") or {}).get("deck", [])
        if cards:
            note = " (as of last state)"

    if not cards:
        return "[No deck found — are you in a run?]"

    # Group by type
    groups = {"ATTACK": [], "SKILL": [], "POWER": [], "STATUS": [], "CURSE": []}
    for c in cards:
        ctype = c.get("type", "UNKNOWN").upper()
        name = c.get("name", "?")
        cost = c.get("cost", "?")
        upgrades = c.get("upgrades", 0)
        # Some payloads already include '+' in the name — don't double it.
        display = name
        if upgrades > 0 and "+" not in name:
            display = f"{name}+{upgrades}" if upgrades > 1 else f"{name}+"
        groups.setdefault(ctype, []).append(f"  {display} ({cost}E)")

    lines = [f"=== DECK ({len(cards)} cards){note} ==="]
    for gtype in ["ATTACK", "SKILL", "POWER", "CURSE", "STATUS"]:
        group = groups.get(gtype, [])
        if group:
            lines.append(f"\n{gtype}S ({len(group)}):")
            lines.extend(sorted(group))

    # Summary stats
    costs = [c.get("cost", 0) for c in cards if isinstance(c.get("cost"), int) and c.get("cost", 0) >= 0]
    avg_cost = sum(costs) / len(costs) if costs else 0
    lines.append(f"\nAvg cost: {avg_cost:.1f}E | Total: {len(cards)} cards")

    return "\n".join(lines)


def think(reasoning: str, label: str = "Strategy") -> str:
    """Post your strategic reasoning to the stream overlay.

    Call this after survey()/recall() to share your analysis with viewers. The
    reasoning appears in the thinking panel and the action feed.

    This is how viewers see WHY you're making decisions — not just what
    knowledge entries were loaded, but your actual strategic synthesis.

    Args:
        reasoning: Your strategic analysis. This is the text viewers will read.
                   For combat: your fight strategy (win condition, survival plan, key cards, risks).
                   For act planning: your pathing logic, deck-building goals, boss prep.
        label: Short label for the action feed (default: "Strategy").
               Examples: "Fight Strategy", "Act Plan", "Boss Prep"

    Example:
        think('''
        WIN CONDITION: Rampage+ scales each play. Play it every cycle.
        SURVIVAL: 32-damage single hit is the threat. Need 3 Defends per cycle.
        KEY CARDS: Rampage+ (scaling), Bash+ (Vulnerable), True Grit (block + thin)
        RISKS: Over-exhausting block cards with True Grit.
        ESTIMATED TURNS: 12-14.
        ''', label="Fight Strategy")
    """
    if not reasoning or not reasoning.strip():
        return "[ERROR] reasoning is required. Share your strategic analysis."
    # Log as both a decision (for stream) and a think event (for run log)
    _post_decision("think", reasoning=reasoning.strip(), translated_override=label)
    _log_event({
        "type": "think",
        "label": label,
        "reasoning": reasoning.strip(),
        "timestamp": time.time(),
    })
    return f"[Reasoning posted to stream: {label}]"


_SAVES_DIR = os.path.join("C:\\", "Program Files (x86)", "Steam", "steamapps", "common", "SlayTheSpire", "saves")

# The game's seed-string alphabet (base 35, no 'O') — from the game's SeedHelper.
_SEED_CHARS = "0123456789ABCDEFGHIJKLMNPQRSTUVWXYZ"


def _encode_seed(seed) -> str:
    """Run logs store seeds as signed 64-bit integers, but the game (and
    CommunicationMod's start command) takes the base-35 STRING. Passing the
    digits raw silently starts the WRONG run (the digits decode as base 35) —
    a seed replay burned a run number this way. Numeric input is encoded the
    way the game's SeedHelper does: unsigned 64-bit, base 35."""
    s = str(seed).strip().upper().replace("O", "0")
    try:
        n = int(s)
    except ValueError:
        return s                      # already a seed string
    n &= (1 << 64) - 1                # Long.toUnsignedString semantics
    if n == 0:
        return "0"
    out = ""
    while n:
        n, r = divmod(n, 35)
        out = _SEED_CHARS[r] + out
    return out


def start(character: str = "IRONCLAD", ascension: int = 0, seed: str = None) -> str:
    """Start a new run.

    GUARDED: CommunicationMod's start silently DESTROYS any existing save for
    that character (there is no resume verb — a run in progress nearly got lost
    twice this way). If a save exists, the first call refuses; calling start
    again confirms you really want to abandon it.
    """
    saves = [os.path.join(_SAVES_DIR, f"{character.upper()}{ext}")
             for ext in (".autosave", ".autosaveBETA")]
    if any(os.path.exists(s) for s in saves):
        # ALWAYS require the two-call confirm when a save file exists. A clean
        # OUT OF GAME report does NOT mean the save is stale: a crash-to-menu
        # mid-run (IB-012, run 241) produces exactly that state with a LIVE save
        # that the orchestrator can resume by clicking Continue — and start()
        # DESTROYS it. (The confirm flag is a FILE because every play.py call is
        # a new process — an in-memory flag warned forever and never proceeded.)
        flag = os.path.join(_BASE_DIR, "data", "start_confirm.flag")
        if not os.path.exists(flag):
            with open(flag, "w") as f:
                f.write(character.upper())
            return (
                f"[WARNING] A save for {character.upper()} exists — starting DESTROYS "
                f"it, and there is no resume command. If the game dropped to the main "
                f"menu mid-run, the save is LIVE and recoverable (IB-012): STOP and "
                f"report to the orchestrator.\n"
                f"If you intend to abandon the save, call start again to confirm."
            )
        os.remove(flag)
    # A confirmed start abandons whatever run the live-marker tracked.
    live = os.path.join(_BASE_DIR, "data", "run_live.flag")
    if os.path.exists(live):
        os.remove(live)
    cmd = f"start {character}"
    if ascension > 0:
        cmd += f" {ascension}"
    if seed:
        cmd += f" {_encode_seed(seed)}"
    return send(cmd, reason=f"Starting {character} A{ascension}")


# Allow running directly: python cmd.py state / python cmd.py "play 1 0"
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cmd.py state | python cmd.py <command>")
        sys.exit(1)

    arg = " ".join(sys.argv[1:])
    if arg == "state":
        print(state())
    else:
        print(send(arg))
