"""Locate + parse a book-owned awareness manifest into a payload.

A manifest is the machine-readable twin of a goal file's "Knowledge Entry Points":
  awareness/<domain>/<goal>.json  ->  { schema, goal, domain, tiers: { <tier>: Payload } }
Only the 'goal' tier is consumed today; situation/entity tiers are reserved.
"""
import json
from pathlib import Path


def load_manifest(manifest_dir, goal: str) -> dict:
    path = Path(manifest_dir) / f"{goal}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def get_payload(manifest: dict, tier: str = "goal") -> dict:
    tiers = manifest.get("tiers", {})
    payload = tiers.get(tier)
    if payload is None:
        raise KeyError(
            f"manifest for goal '{manifest.get('goal')}' has no tier '{tier}' "
            f"(available: {sorted(tiers)})"
        )
    return dict(payload)
