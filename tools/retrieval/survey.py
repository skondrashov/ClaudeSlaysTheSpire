"""survey() and recall() — the generic Praxis retrieval verbs.

Design: ontology/praxis/retrieval.md.

    survey(state, index) -> [handle, ...]   a MENU of paths the agent might want
    recall(handles)      -> {handle: text}  full text; DOES NOT follow links

`survey` is ONE selector call: a small/fast model reads the live state + the
`blurb: path` index and returns the handles whose blurb applies. It returns paths
only — never content, never composed prose; the agent decides what to recall.

The selector runs via the **`claude` CLI** (`claude -p`), not the API — a nested,
non-interactive Claude invocation, consistent with the rest of the system and using
subscription auth. `recall` fetches; links inside returned text are an inline menu
the agent may recall next, never auto-followed.
"""
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SELECT_MODEL = os.environ.get("STS_SELECT_MODEL", "claude-haiku-4-5-20251001")

_INSTRUCTIONS = """\
You are a retrieval selector for a Slay the Spire agent. You are given the LIVE GAME \
STATE and an ontology MAP — how to address any entity (a slug rule, the category \
search order, the upgrade rule, an alias table) plus any `<applies-when>: <path>` \
phenomenon lines.

Return ONLY a JSON array of recall handles relevant to the current state — nothing \
else (no prose, no knowledge content). Be inclusive at the margin; the agent decides \
what to read.

Use each entity's EXACT in-game name verbatim — "The Guardian", not "guardian" or \
"the-guardian"; "Spike Slime (M)", not "spike-slime-m". recall resolves names to \
files; do NOT slugify, abbreviate, or drop words. (Only the alias table tells you a \
canonical name to use instead, for the few names listed there.)

Surface:
1. Each entity present in the state — enemies, the act boss, non-basic cards in hand, \
relics, the current event — as its name handle (e.g. "Cultist", "Gremlin Nob"). For \
anything with a real decision attached (enemies, bosses, notable cards/relics) ALSO \
emit the heuristic handle "layer:heuristics, <category>/<exact name>".
2. Each UPGRADED card in hand: emit "<exact name>+" (e.g. "Shrug It Off+").
3. Any phenomenon whose `<applies-when>` matches the current state: emit its path.

Output example: ["Jaw Worm", "layer:heuristics, enemies/Jaw Worm", "The Guardian", \
"layer:heuristics, bosses/The Guardian", "Eruption+", \
"phenomena/sts1/interactions/wrath-burst-the-threat"]"""

_JSON_ARRAY_RE = re.compile(r"\[.*\]", re.DOTALL)


def load_index(domain: str = "sts1") -> str:
    """Load the committed survey index (markdown: `<blurb>: <path>` per line)."""
    return (ROOT / "awareness" / domain / "survey-index.md").read_text(encoding="utf-8")


def survey(state: str, index: str, *, model: str = None) -> list[str]:
    """Map live `state` -> handles that might apply, via one selector call."""
    return _select(state=state, index=index, model=model or SELECT_MODEL)


def recall(handles: list[str]) -> dict[str, str]:
    """Return full text for each handle (a path under the repo root). Missing handles
    are omitted. Does NOT follow links in the returned text."""
    out = {}
    for h in handles:
        rel = h if h.endswith(".md") else h + ".md"
        try:
            out[h] = (ROOT / rel).read_text(encoding="utf-8").strip()
        except (FileNotFoundError, NotADirectoryError):
            continue
    return out


def _select(state: str, index: str, model: str) -> list[str]:
    """One selector call via `claude -p` (nested CLI invocation, subscription auth)."""
    claude = shutil.which("claude") or shutil.which("claude.exe") or shutil.which("claude.cmd")
    if not claude:
        raise RuntimeError("claude CLI not found on PATH; the selector runs via "
                           "`claude -p`, not the API")

    system = _INSTRUCTIONS + "\n\nINDEX:\n" + index
    user = "STATE:\n" + state + "\n\nReturn the JSON array of applicable paths."

    cmd = [claude, "-p", "--model", model]
    # System+index is small and stable; pass on argv when it fits (Windows argv is
    # capped), else fold it into stdin and suppress the default system prompt.
    if len(system) <= 6000:
        cmd += ["--system-prompt", system]
        stdin_text = user
    else:
        cmd += ["--system-prompt", ""]
        stdin_text = f"[SYSTEM INSTRUCTIONS]\n{system}\n[END]\n\n{user}"

    # Use subscription/OAuth auth (drop API-key vars); run from a clean cwd so the
    # nested claude doesn't auto-load CLAUDE.md / project context.
    env = os.environ.copy()
    for k in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN"):
        env.pop(k, None)

    # Force UTF-8 for the pipe: the live state contains non-cp1252 glyphs (e.g. the
    # map's "→" arrows), and text=True alone uses the Windows locale codec, which
    # raised UnicodeEncodeError and broke every survey on the first live run.
    proc = subprocess.run(cmd, input=stdin_text, capture_output=True, text=True,
                          encoding="utf-8", errors="replace",
                          env=env, cwd=tempfile.gettempdir(), timeout=90)
    if proc.returncode != 0:
        raise RuntimeError(f"selector CLI failed (exit {proc.returncode}): "
                           f"{(proc.stderr or proc.stdout).strip()[:500]}")

    m = _JSON_ARRAY_RE.search(proc.stdout)
    if not m:
        return []
    try:
        handles = json.loads(m.group(0))
    except json.JSONDecodeError:
        return []
    return [h for h in handles if isinstance(h, str)]
