"""Praxis awareness: generic context preloader with session-level dedup.

Mechanism only — the *data* (what to load for a given key) lives in book-owned
JSON manifests under the top-level awareness/ tree (e.g. awareness/sts1/<goal>.json).
The single piece of state this package owns is the session dedup cache.
"""
from .awareness import (
    AwarenessConfig,
    load,
    load_one,
    load_goal,
    reset,
)

__all__ = ["AwarenessConfig", "load", "load_one", "load_goal", "reset"]
