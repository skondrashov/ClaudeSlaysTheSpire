"""survey() and recall() — the generic Praxis retrieval verbs.

Design: ontology/praxis/retrieval.md.

    survey(state, index) -> [handle, ...]   a MENU of paths the agent might want
    recall(handles)      -> {handle: text}  full text; DOES NOT follow links

`survey` is ONE reranker call: a small/fast model holds the {blurb, target} index
and is queried by the live state, returning the handles whose entries might apply.
It returns paths only — never content, never composed prose. The agent decides what
to recall. `recall` fetches; links inside returned text are an inline menu the agent
may recall next, never auto-followed.
"""
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RERANK_MODEL = os.environ.get("STS_RERANK_MODEL", "claude-haiku-4-5-20251001")

_INSTRUCTIONS = """\
You are a retrieval reranker for a game-playing agent. You are given the LIVE GAME \
STATE and an INDEX of knowledge entries. Each index entry has an `id`, an \
applicability `blurb` (when it applies), and a `target` (what to recall).

Return ONLY a JSON array of target path strings whose blurb applies to the current \
state — nothing else. No prose, no explanation, no knowledge content. Be inclusive \
at the margin: surface anything plausibly relevant; the agent decides what to read.

For the entry `rule:upgrades` (target kind "pattern", value \
".../cards/<slug>-plus"): for every upgraded card in the state (its name ends in \
'+'), emit the pattern with <slug> replaced by the card's lowercased, \
hyphenated name without the '+' (e.g. "Shrug It Off+" -> ".../cards/shrug-it-off-plus").

Output example: ["phenomena/sts1/interactions/corruption-dead-branch", \
"phenomena/sts1/cards/bash-plus"]"""

_JSON_ARRAY_RE = re.compile(r"\[.*\]", re.DOTALL)


def load_index(domain: str = "sts1") -> dict:
    """Load the committed {blurb, target} survey index for a domain."""
    p = ROOT / "awareness" / domain / "survey-index.json"
    return json.loads(p.read_text(encoding="utf-8"))


def survey(state: str, index: dict, *, model: str = None) -> list[str]:
    """Map live `state` -> handles that might apply, via one reranker call."""
    return _rerank(state=state, index=index, model=model or RERANK_MODEL)


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


def _rerank(state: str, index: dict, model: str) -> list[str]:
    """One call to the reranker model. The index is sent as a cached system block
    (stable across a session); the state is the query."""
    try:
        import anthropic
    except ImportError as e:
        raise RuntimeError("survey requires the 'anthropic' package "
                           "(pip install anthropic)") from e
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("survey requires ANTHROPIC_API_KEY in the environment")

    client = anthropic.Anthropic(api_key=api_key)
    resp = client.messages.create(
        model=model,
        max_tokens=1024,
        system=[
            {"type": "text", "text": _INSTRUCTIONS},
            # The index is stable within a run -> cache it so repeated surveys are cheap.
            {"type": "text", "text": "INDEX:\n" + json.dumps(index),
             "cache_control": {"type": "ephemeral"}},
        ],
        messages=[{"role": "user",
                   "content": "STATE:\n" + state +
                              "\n\nReturn the JSON array of applicable target paths."}],
    )
    text = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
    m = _JSON_ARRAY_RE.search(text)
    if not m:
        return []
    try:
        handles = json.loads(m.group(0))
    except json.JSONDecodeError:
        return []
    return [h for h in handles if isinstance(h, str)]
