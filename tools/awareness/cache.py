"""Session dedup cache — the only stateful thing the awareness tool owns.

On disk (each agent Bash call is a fresh process, so an in-memory set never dedups
across a run). Keyed by session; carries an epoch so a post-compaction reset makes
the ledger forget in lockstep (the next load() then honestly re-emits everything).
The cache only ever records refs actually emitted into returned text — never
speculatively.
"""
import json
import os
import tempfile
from pathlib import Path


class SessionCache:
    def __init__(self, path):
        self.path = Path(path)
        self.data = self._read()

    def _read(self):
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except (FileNotFoundError, ValueError):
            return {"session": None, "epoch": 0, "loaded": []}

    def _write(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=str(self.path.parent), suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2)
            os.replace(tmp, self.path)
        except BaseException:
            if os.path.exists(tmp):
                os.remove(tmp)
            raise

    def ensure_session(self, session: str):
        """New session (new run / new player token) starts with an empty ledger."""
        if self.data.get("session") != session:
            self.data = {"session": session, "epoch": 0, "loaded": []}
            self._write()

    def as_set(self) -> set:
        return set(self.data.get("loaded", []))

    def seen(self, key: str) -> bool:
        return key in self.data.get("loaded", [])

    def mark(self, keys):
        keys = [k for k in keys]
        if not keys:
            return
        self.data["loaded"] = sorted(self.as_set() | set(keys))
        self._write()

    def reset(self, session: str, reason: str = None):
        self.data = {
            "session": session,
            "epoch": self.data.get("epoch", 0) + 1,
            "loaded": [],
            "last_reset": reason,
        }
        self._write()
