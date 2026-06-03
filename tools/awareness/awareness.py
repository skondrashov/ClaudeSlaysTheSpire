"""Awareness loader: payload -> dedup vs session cache -> resolve links -> assemble.

Public API:
  load(payload, session=...)       aggregate many refs (preload)
  load_one(ref, session=...)       a single entity (the reason()/RETRIEVE path)
  load_goal(goal, session=...)     read the goal manifest, then load()
  reset(session=..., reason=...)   new-session / post-compaction invalidation

Both load() and load_one() dedup against the SAME on-disk session cache, so a
preload followed by an on-demand lookup never re-emits the same knowledge.
"""
import os
from dataclasses import dataclass, field
from pathlib import Path

from .loaders import KnowledgeLoader, ref_key, extract_links
from .cache import SessionCache
from .manifest import load_manifest, get_payload

ROOT = Path(__file__).resolve().parents[2]


@dataclass
class AwarenessConfig:
    knowledge_root: Path = ROOT
    domain: str = "sts1"
    manifest_dir: Path = field(default=None)
    cache_path: Path = field(default=None)

    def __post_init__(self):
        if self.manifest_dir is None:
            self.manifest_dir = self.knowledge_root / "awareness" / self.domain
        if self.cache_path is None:
            self.cache_path = self.knowledge_root / "games" / self.domain / "data" / "awareness_cache.json"


DEFAULT = AwarenessConfig()


def _expand(ref: dict, default_layer: str = "ontology"):
    """A Ref -> concrete (layer, category, name, render) loads.

    mode 'knowledge'/'full' loads BOTH layers for an entity; 'top' loads the
    compact header form; 'entry' (default) loads the ref's own layer.
    """
    layer = ref.get("layer", default_layer)
    cat = ref.get("category")
    name = ref["name"]
    mode = ref.get("mode", "entry")
    if mode in ("knowledge", "full"):
        return [("ontology", cat, name, "whole"), ("heuristics", cat, name, "whole")]
    if mode == "top":
        return [(layer, cat, name, "top")]
    return [(layer, cat, name, "whole")]


def _block(layer, category, name, text):
    head = f"### {layer}/{(category + '/') if category else ''}{name}"
    return f"{head}\n\n{text}"


def _resolve_links(content, loader, domain, frontier):
    """One level of [[link]] expansion. category links -> ontology facts;
    bare [[name]] links -> heuristics top-level files. Deduped against frontier."""
    resolved, keys = [], []
    for layer_q, cat, name in extract_links(content):
        # explicit `layer:` wins; else ontology-canonical for categorized links,
        # heuristics for bare top-level references (combat, archetypes, ...).
        layer = layer_q or ("ontology" if cat else "heuristics")
        key = ref_key(layer, domain, cat, name)
        if key in frontier:
            continue
        frontier.add(key)
        entry = loader.load_file(layer, cat, name)
        if entry:
            resolved.append(_block(layer, cat, name, entry))
            keys.append(key)
    if resolved:
        return "\n\n--- LINKED KNOWLEDGE ---\n\n" + "\n\n".join(resolved), keys
    return "", []


def load(payload: dict, session: str = None, config: AwarenessConfig = DEFAULT) -> dict:
    domain = payload.get("domain", config.domain)
    loader = KnowledgeLoader(config.knowledge_root, domain)
    sc = SessionCache(config.cache_path)
    session = session or os.environ.get("PLAYER_SESSION") or "default"
    sc.ensure_session(session)
    frontier = sc.as_set()

    blocks, loaded, skipped_dup, missing = [], [], [], []
    new_keys = set()
    for ref in payload.get("refs", []):
        for layer, cat, name, render in _expand(ref):
            key = ref_key(layer, domain, cat, name)
            if key in frontier or key in new_keys:
                skipped_dup.append(key)
                continue
            text = loader.load_top(layer, cat, name) if render == "top" else loader.load_file(layer, cat, name)
            if text is None:
                missing.append(key)
                continue
            blocks.append(_block(layer, cat, name, text))
            loaded.append(key)
            new_keys.add(key)

    links_loaded = []
    if payload.get("resolve_links", True) and blocks:
        seen = set(frontier) | new_keys
        link_text, links_loaded = _resolve_links("\n\n".join(blocks), loader, domain, seen)
        if link_text:
            blocks.append(link_text)
            new_keys |= set(links_loaded)

    sc.mark(new_keys)
    text = "\n\n".join(blocks)
    return {
        "text": text,
        "loaded": loaded,
        "skipped_dup": skipped_dup,
        "missing": missing,
        "links_loaded": links_loaded,
        "chars": len(text),
        "label": payload.get("label"),
    }


def load_one(ref, session: str = None, config: AwarenessConfig = DEFAULT) -> dict:
    """Single-entity load. `ref` is a Ref dict; a bare string is treated as an
    entity name looked up across both layers (mode 'knowledge')."""
    if isinstance(ref, str):
        ref = {"name": ref, "mode": "knowledge"}
    payload = {"domain": ref.get("domain", config.domain), "resolve_links": True, "refs": [ref]}
    return load(payload, session=session, config=config)


def load_goal(goal: str, tier: str = "goal", session: str = None, config: AwarenessConfig = DEFAULT) -> dict:
    manifest = load_manifest(config.manifest_dir, goal)
    payload = get_payload(manifest, tier)
    payload.setdefault("domain", manifest.get("domain", config.domain))
    return load(payload, session=session, config=config)


def reset(session: str = None, reason: str = None, config: AwarenessConfig = DEFAULT):
    sc = SessionCache(config.cache_path)
    session = session or os.environ.get("PLAYER_SESSION") or "default"
    sc.reset(session, reason)
    return {"reset": True, "session": session, "reason": reason}
