"""
R1 cross-compare (part 1): canonical game WORDING vs. our card ontology effect text.

Source of truth for wording = Slay the Spire's own localization (cards.json in the
game jar). It carries the exact description template ("Deal !D! damage. Apply !M!
Vulnerable.") but NOT numbers/cost/rarity (those need a community dataset — added
later). This pass therefore flags WORDING/KEYWORD drift, which is the paraphrase
class: wrong debuff (Weak vs Vulnerable), missing/extra clauses, wrong effect.

No web. Read-only. Prints a report; writes nothing.
"""
import json, re, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
JAR = Path(r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\desktop-1.0.jar")
CARDS_DIR = ROOT / "ontology" / "sts1" / "cards"


def load_loc(name):
    with zipfile.ZipFile(JAR) as z:
        with z.open(f"localization/eng/{name}") as f:
            return json.loads(f.read().decode("utf-8-sig"))


# ── keyword vocabulary (the terms whose presence/absence is the real signal) ──
def build_vocab():
    vocab = set()
    kw = load_loc("keywords.json")
    items = kw.values() if isinstance(kw, dict) else kw
    for it in items:
        if not isinstance(it, dict):
            continue
        for key in ("PROPER_NAME", "NAME"):
            if isinstance(it.get(key), str):
                vocab.add(it[key].lower())
        for key in ("NAMES", "NAME"):
            v = it.get(key)
            if isinstance(v, list):
                vocab.update(str(x).lower() for x in v)
    for p in load_loc("powers.json").values():
        if isinstance(p, dict) and isinstance(p.get("NAME"), str):
            vocab.add(p["NAME"].lower())
    # core mechanic words that matter for effect equivalence
    vocab.update(["damage", "block", "draw", "exhaust", "energy", "strength",
                  "dexterity", "vulnerable", "weak", "weakened", "frail", "poison",
                  "discard", "channel", "scry", "wound", "dazed", "burn", "void"])
    # drop noise tokens
    vocab.discard("")
    return {w for w in vocab if len(w) >= 3}


def strip_markup(s):
    s = s.replace(" NL ", " ").replace("NL", " ")
    s = re.sub(r"#[a-z]", "", s)            # color codes #y #b #r ...
    s = re.sub(r"![A-Za-z]+!", "#", s)       # !D! !M! !B! -> number marker
    s = s.replace("[E]", " energy ")         # energy icon -> word
    s = re.sub(r"\[[A-Z]\]", " ", s)         # other icons
    s = re.sub(r"\s+", " ", s).strip()
    return s


def game_card_text(entry):
    """Return normalized description for a card localization entry."""
    desc = entry.get("DESCRIPTION", "")
    if isinstance(desc, list):
        desc = " ".join(desc)
    return strip_markup(desc)


def keywords_in(text, vocab):
    t = " " + re.sub(r"[^a-z ]", " ", text.lower()) + " "   # drop digits too
    t = re.sub(r"\s+", " ", t)
    return {w for w in vocab if f" {w} " in t}


def parse_our_card(md_path):
    text = md_path.read_text(encoding="utf-8")
    title = None
    m = re.match(r"^#\s+(.+)", text.strip())
    if m:
        title = m.group(1).strip()
    fields = {}
    for line in text.splitlines():
        fm = re.match(r"\s*-\s*\*\*(.+?):\*\*\s*(.+)", line)
        if fm:
            fields[fm.group(1).strip().lower()] = fm.group(2).strip()

    def delink(s):
        return re.sub(r"\[\[([^\]]+)\]\]", lambda mm: mm.group(1).split("/")[-1], s or "")

    return {
        "title": title,
        "stem": md_path.stem,
        "effect": delink(fields.get("effect", "")),
        "upgraded": delink(fields.get("upgraded", "")),
        "cost": fields.get("cost", ""),
        "type": fields.get("type", ""),
        "rarity": fields.get("rarity", ""),
    }


def main():
    vocab = build_vocab()
    loc = load_loc("cards.json")
    # index game cards by display NAME (lowercased); collisions (Strike_R/G/B) merge
    game = {}
    for cid, entry in loc.items():
        name = entry.get("NAME", cid)
        game.setdefault(name.lower(), game_card_text(entry))

    ours = [parse_our_card(p) for p in sorted(CARDS_DIR.glob("*.md"))]

    print(f"vocab terms: {len(vocab)} | game cards: {len(game)} | our cards: {len(ours)}\n")

    mismatches, not_in_game, missing_effect, power_delegating = [], [], [], []
    for c in ours:
        key = (c["title"] or "").lower()
        if key not in game:
            not_in_game.append(c)
            continue
        if not c["effect"]:
            missing_effect.append(c)
            continue
        # Power-granting cards: our entries write "Apply N <Power> to self" and
        # delegate the real effect to the linked power entry, while the game
        # inlines it. That's our composable style, not drift — bucket separately.
        if c["type"].lower() == "power" and c["effect"].lower().startswith("apply"):
            power_delegating.append(c)
            continue
        g_text = game[key]
        g_kw = keywords_in(g_text, vocab)
        o_kw = keywords_in(c["effect"] + " " + c["upgraded"], vocab)
        only_game = g_kw - o_kw
        only_ours = o_kw - g_kw
        if only_game or only_ours:
            mismatches.append((c, g_text, sorted(only_game), sorted(only_ours)))

    print(f"=== KEYWORD MISMATCHES ({len(mismatches)}) — likely wording drift ===")
    for c, g_text, only_game, only_ours in sorted(mismatches, key=lambda x: x[0]["title"]):
        print(f"\n{c['title']}")
        print(f"  game : {g_text}")
        print(f"  ours : {c['effect']}")
        if only_game:
            print(f"  game has, ours missing: {only_game}")
        if only_ours:
            print(f"  ours has, game missing: {only_ours}")

    print(f"\n=== POWER-DELEGATING CARDS ({len(power_delegating)}) — our 'Apply X to self' vs game's inline effect ===")
    print(", ".join(sorted(c["title"] for c in power_delegating)))

    print(f"\n=== OUR CARDS NOT FOUND IN GAME ({len(not_in_game)}) — naming or phantom ===")
    print(", ".join(sorted(c["title"] or c["stem"] for c in not_in_game)))


if __name__ == "__main__":
    main()
