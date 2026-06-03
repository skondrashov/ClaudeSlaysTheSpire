"""survey() and recall() — the generic Praxis retrieval verbs (SKETCH).

Design: ontology/praxis/retrieval.md. This is a signature-level sketch, not a wired
implementation — the reranker call (`_rerank`) is a stub. The shapes are real so the
sts1 interface can be a one-line pass-through over these.

    survey(state)   -> [handle, ...]      a MENU of paths the agent might want
    recall(handles) -> {handle: text}     full text; DOES NOT follow links
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def survey(state: str, index: dict, *, model: str = "haiku") -> list[str]:
    """Map live state -> handles that might apply. ONE reranker call.

    The reranker holds `index` ({blurb, target} entries) and is queried by `state`.
    It returns *paths only* (handles) — never content, never composed prose. The
    agent decides what to recall. Resolvable upgrades arrive via the rule entry; the
    reranker expands the pattern against `+` cards it sees in `state`.
    """
    return _rerank(state=state, index=index, model=model)


def recall(handles: list[str]) -> dict[str, str]:
    """Return full text for each handle. Links in the text are an inline menu the
    agent may recall next — they are NOT auto-followed (that would re-introduce
    force-feeding). Missing handles are simply omitted."""
    out = {}
    for h in handles:
        p = ROOT / (h if h.endswith(".md") else h + ".md")
        try:
            out[h] = p.read_text(encoding="utf-8").strip()
        except (FileNotFoundError, NotADirectoryError):
            continue
    return out


def _rerank(state: str, index: dict, model: str) -> list[str]:
    """STUB. Wire to a small model (e.g. Haiku). Prompt contract:

      System: You are a retrieval reranker. You are given LIVE GAME STATE and an
        INDEX of knowledge entries, each with an `id`, an applicability `blurb`, and
        a `target`. Return ONLY the list of `target` paths whose blurb applies to the
        state. Return paths, nothing else — no prose, no explanation, no content.
        For the rule entry `rule:upgrades`, emit the resolved path for each upgraded
        ('+') card you see in the state, substituting <slug> with the card's slug.

      User: STATE:\n{state}\n\nINDEX:\n{json.dumps(index)}

    Returns the parsed list of handles.
    """
    raise NotImplementedError("wire to the reranker model; see docstring contract")
