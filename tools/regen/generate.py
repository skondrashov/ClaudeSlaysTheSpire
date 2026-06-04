"""
R1 generator: emit card NOUMENA (base + upgrade delta) and PHENOMENA (resolved
upgraded cards) from canonical community data (data/sts1_cards.json).

Noumenon  ->  ontology/sts1/cards/<slug>.md   : base values + an Upgrade delta line.
Phenomenon -> phenomena/sts1/cards/<slug>-plus.md : the resolved upgraded card.

The delta NEVER parses numbers out of upgrade.description (junk for ~2 cards); it
comes from the dataset's structured fields (upgrade.damage/block/magic_number = "+N"
strings, upgrade.cost = abs int) plus flag word-diff, plus a small WORDED_DELTAS
table for genuine text-change upgrades. Cards that still can't be expressed are
flagged "(NEEDS WORDED DELTA)" rather than guessed.

The phenomenon's resolved Effect uses upgrade.description (reliable except the junk
cards, which get a PHENOMENON_EFFECT override).

Read-only: prints; writes nothing (apply_cards.py is the writer).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = Path(__file__).parent / "data" / "sts1_cards.json"
ONT = ROOT / "ontology" / "sts1"
CARDS_DIR = ONT / "cards"

COLOR_CHAR = {"ironclad": "Ironclad", "silent": "Silent", "defect": "Defect",
              "watcher": "Watcher", "colorless": "Colorless"}
RARITY_MAP = {"Basic": "Starter"}
FLAGS = ["innate", "ethereal", "retain", "exhaust"]

# Genuine text-change upgrades that structured fields + flags can't express.
WORDED_DELTAS = {
    "Armaments": "upgrades ALL cards in hand (was 1)",
    "Blind": "applies to ALL enemies",
    "Trip": "applies to ALL enemies",
    "Fission": "Evoke your Orbs instead of removing them",
    "Catalyst": "Triple the enemy's Poison (was Double)",
    "Enlightenment": "cost reduction lasts the combat (was this turn)",
    "Darkness": "also triggers the passive of all Dark orbs",
    "Transmutation": "the added cards are Upgraded",
    "True Grit": "Exhaust a chosen card (was random)",
    "Adrenaline": "+1 energy",
    "Outmaneuver": "+1 energy next turn",
    "Multi-Cast": "+1 to X (Evoke X+1 times)",
    "Tempest": "+1 to X (Channel X+1 Lightning)",
    "Doppelganger": "+1 to X (draw and energy)",
    "Malaise": "+1 to X (Strength loss and Weak)",
    "Collect": "+1 to X (one more turn of Miracles)",
    "Conjure Blade": "the Expunger's X becomes X+1",
    "Forethought": "put any number of cards (was 1)",
    "Foreign Influence": "the added card costs 0 this turn",
    "Loop": "triggers 1 additional time",          # base 1 implicit -> 2 times
    "Shockwave": "+2 Weak and Vulnerable",          # magic scales both
    "Fasting": "+1 Strength and Dexterity",         # magic scales both
}

# Resolved Effect override for cards whose upgrade.description is junk in the dataset.
PHENOMENON_EFFECT = {
    "Grand Finale": "Can only be played if there are no cards in your draw pile. Deal 60 damage to ALL enemies.",
    "Body Slam": "Deal damage equal to your current Block.",
}

# Cards whose dataset description dropped the [W]/[E] energy glyph (left a blank),
# and Fasting's upgraded Dexterity (wrongly 3). Restored verbatim from the game jar
# localization (localization/eng/cards.json), energy spelled out.
DESC_OVERRIDE = {
    "Deva Form": {
        "base": "Ethereal. At the start of your turn, gain 1 Energy and increase this gain by 1.",
        "upgrade": "At the start of your turn, gain 1 Energy and increase this gain by 1.",
    },
    "Fasting": {
        "base": "Gain 3 Strength. Gain 3 Dexterity. Gain 1 less Energy at the start of each turn.",
        "upgrade": "Gain 4 Strength. Gain 4 Dexterity. Gain 1 less Energy at the start of each turn.",
    },
    "Follow-Up": {
        "base": "Deal 7 damage. If the last card played this combat was an Attack, gain 1 Energy.",
        "upgrade": "Deal 11 damage. If the last card played this combat was an Attack, gain 1 Energy.",
    },
}


def _base_desc(card):
    o = DESC_OVERRIDE.get(card["name"])
    return o["base"] if o else card.get("description", "")


def _upg_desc(card):
    o = DESC_OVERRIDE.get(card["name"])
    if o:
        return o["upgrade"]
    return (card.get("upgrade") or {}).get("description")


def slugify(name):
    s = name.lower().replace("'", "").replace(".", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def _norm(s):  # numbers -> #, words only (for "did the text change beyond numbers?")
    return tuple(re.sub(r"[^a-z# ]", " ", re.sub(r"\d+", "#", (s or "").lower())).split())


def build_link_map():
    m = {}
    for cat in ("debuffs", "buffs"):
        d = ONT / cat
        if not d.exists():
            continue
        for p in d.glob("*.md"):
            title = None
            for line in p.read_text(encoding="utf-8").splitlines():
                mm = re.match(r"^#\s+(.+)", line)
                if mm:
                    title = mm.group(1).strip(); break
            if title:
                # Bare link, no alias: the resolver slugifies the target, so
                # [[debuffs/Vulnerable]] resolves to vulnerable.md and displays
                # "Vulnerable" — matching the de-aliased convention.
                m[title] = f"[[{cat}/{title}]]"
    return m


def inject_links(text, link_map):
    for name in sorted(link_map, key=len, reverse=True):
        text = re.sub(rf"(?<![\[\w]){re.escape(name)}(?!\w|\]\])", link_map[name], text)
    return text


def fmt_cost(cost):
    if cost is None:
        return None
    if cost == -1:
        return "X"
    if cost < 0:
        return None
    return f"{cost}E"


_ENERGY_RUN = re.compile(r"\[[RGBWPE]\](?:\s*\[[RGBWPE]\])*")


def energy(text):
    """Canonical energy symbols -> readable count: 'Gain [R] [R].' -> 'Gain 2 Energy.'"""
    return _ENERGY_RUN.sub(
        lambda m: f"{len(re.findall(r'\[[RGBWPE]\]', m.group(0)))} Energy", text or "")


def clean(text, link_map):
    t = energy(re.sub(r"\s+", " ", (text or "").replace("\n", " ")).strip())
    return inject_links(t, link_map)


def _changed_noun(base, upd, amount, skip=("damage", "block")):
    """The noun whose count changed by `amount` between base and upgraded text:
    Coolheaded 'Draw 1 card' -> 'Draw 2 cards', amount +1 -> 'card'. Diff-based so
    it isn't fooled when two stats share a number ('Channel 1 Frost. Draw 1 card.').
    `skip` excludes nouns already carried by their own delta (up.damage/up.block) —
    but a power like Feel No Pain scales Block via magic_number, so skip must be
    computed from which deltas are actually present, not hard-coded."""
    upd = upd or ""
    for n, noun in re.findall(r"(\d+)\s+([A-Za-z][A-Za-z\-]+)", base or ""):
        if noun.lower() in skip:
            continue
        target = int(n) + amount
        if re.search(rf"\b{target}\s+{re.escape(noun)}s?\b", upd):
            return noun
    return None


def render_delta(card):
    """The Upgrade delta line, from structured fields + flag word-diff + overrides."""
    name = card["name"]
    if name in WORDED_DELTAS:
        return WORDED_DELTAS[name]
    up = card.get("upgrade") or {}
    base = _base_desc(card)
    upd_desc = _upg_desc(card) or ""
    parts = []
    if up.get("cost") is not None and up["cost"] != card.get("cost"):
        c = fmt_cost(up["cost"])
        parts.append(f"cost {c}" if c is not None else "becomes unplayable")
    if up.get("damage"):
        parts.append(f"{up['damage']} damage")
    if up.get("block"):
        parts.append(f"{up['block']} Block")
    if up.get("magic_number"):
        skip = {n for n in ("damage", "block") if up.get(n)}
        try:
            noun = _changed_noun(base, upd_desc, int(up["magic_number"]), skip)
        except ValueError:
            noun = None
        parts.append(f"{up['magic_number']} {noun}" if noun else f"{up['magic_number']} (magic)")
    bw = set(re.findall(r"[a-z]+", base.lower()))
    uw = set(re.findall(r"[a-z]+", upd_desc.lower()))
    for flag in FLAGS:
        if flag in uw and flag not in bw:
            parts.append(f"becomes {flag.title()}")
        elif flag in bw and flag not in uw:
            parts.append(f"loses {flag.title()}")
    if parts:
        return ", ".join(parts)
    if upd_desc.strip() and _norm(base) != _norm(upd_desc):
        return "(NEEDS WORDED DELTA)"
    return ""  # no meaningful upgrade


def _meta_lines(card, cost_override=None):
    out = []
    ctype = (card.get("type") or "").title()
    is_special = ctype in ("Status", "Curse")
    cost = fmt_cost(cost_override if cost_override is not None else card.get("cost"))
    rarity = RARITY_MAP.get(card.get("rarity", ""), card.get("rarity", ""))
    char = COLOR_CHAR.get((card.get("color") or "").lower())
    if cost is not None:
        out.append(f"- **Cost:** {cost}")
    if ctype:
        out.append(f"- **Type:** [[types/{ctype}]]")
    if char and not is_special:
        out.append(f"- **Character:** {char}")
    if rarity and not is_special:
        out.append(f"- **Rarity:** {rarity}")
    return out


def render(card, link_map):
    """Base-card noumenon: base values only.

    The upgrade is NOT a property of the base card — it is its own entity
    (ontology/sts1/upgrades/<slug>.md, see render_upgrade). Base Bash states what
    Bash is; the delta lives in the upgrade noumenon; Bash+ is the phenomenon that
    composes the two.
    """
    out = [f"# {card['name']}", ""]
    out += _meta_lines(card)
    out.append(f"- **Effect:** {clean(_base_desc(card), link_map)}")
    return "\n".join(out) + "\n"


def render_upgrade(card):
    """Upgrade noumenon: the per-card delta as its own entity.

    Bash+ has as much to do with the upgrade as with Bash, so the delta is a
    first-class entity — base card on one side, the generic [[rules/upgrade]]
    mechanic on the other, this file the specific transformation between them.
    """
    name = card["name"]
    delta = render_delta(card) or "(no mechanical change)"
    out = [f"# Upgrade: {name}", ""]
    out.append(f"- **Base:** [[cards/{name}]]")
    out.append(f"- **Mechanic:** [[rules/upgrade]]")
    out.append(f"- **Delta:** {delta}")
    return "\n".join(out) + "\n"


def has_upgrade(card):
    up = card.get("upgrade") or {}
    if any(up.get(k) is not None for k in ("cost", "damage", "block", "magic_number")):
        return True
    return _norm(_base_desc(card)) != _norm(_upg_desc(card) or "")


def render_phenomenon(card, link_map):
    """Resolved upgraded card. Effect from upgrade.description (or override)."""
    name = card["name"]
    up = card.get("upgrade") or {}
    eff_src = PHENOMENON_EFFECT.get(name) or _upg_desc(card) or _base_desc(card)
    cost = up.get("cost") if up.get("cost") is not None else card.get("cost")
    slug = slugify(name)
    out = [f"# {name}+", ""]
    out.append(f"<!-- DO NOT EDIT - generated by tools/regen from")
    out.append(f"     ontology/sts1/cards/{slug}.md (base) + ontology/sts1/upgrades/{slug}.md (delta). -->")
    out.append("")
    out += _meta_lines(card, cost_override=cost)
    out.append(f"- **Effect:** {clean(eff_src, link_map)}")
    out.append("")
    # Composition of two noumena: the base card and the per-card upgrade delta,
    # joined by the generic Upgrade mechanic. Bare links (resolver slugifies).
    out.append(f"Resolves [[upgrades/{name}]] — [[rules/upgrade]] applied to [[cards/{name}]].")
    return "\n".join(out) + "\n"


def main():
    cards = json.loads(DATA.read_text(encoding="utf-8"))
    idx = {c["name"]: c for c in cards}
    link_map = build_link_map()
    names = sys.argv[1:] or ["Bash", "Crush Joints", "Grand Finale", "Armaments",
                             "Shrug It Off", "Coolheaded", "Body Slam", "Zap"]
    for nm in names:
        print("=" * 72)
        card = idx.get(nm)
        if not card:
            print(f"[{nm}] NOT FOUND"); continue
        print(f"--- NOUMENON: {nm} ---\n{render(card, link_map)}")
        if has_upgrade(card):
            print(f"--- PHENOMENON: {nm}+ ---\n{render_phenomenon(card, link_map)}")
        cur = CARDS_DIR / f"{slugify(nm)}.md"
        print(f"--- CURRENT ({cur.name}) ---\n{cur.read_text(encoding='utf-8') if cur.exists() else '(none)'}")


if __name__ == "__main__":
    main()
