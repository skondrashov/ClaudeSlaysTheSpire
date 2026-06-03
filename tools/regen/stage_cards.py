"""
R1 rollout (cards): stage NOUMENA + PHENOMENA + a review report. NO overwrite.

For every card it:
  1. generates the noumenon (base + Upgrade delta) -> staging/cards/<slug>.md
     and, when it upgrades, the phenomenon -> staging/phenomena/cards/<slug>-plus.md
  2. diffs metadata vs the current entry and CATEGORIZES each diff:
       AUTO     - safe to take the generated value (cost-double-encoding -> clean base)
       PRESERVE - keep the current value (Special provenance, shared-card 'All')
       REVIEW   - a genuine disagreement you should eyeball (rarity/cost/character error)
  3. diffs effect MEANING (numbers + keywords, ignoring phrasing)
  4. 3-way checks community wording vs the GAME JAR template (combat/turn-style slips)
  5. flags extra-facts (current keyword absent from generated) and phantom/coverage

Writes staging/ (gitignored) + staging-report.md. Touches no real entries.
"""
import json, re, sys, zipfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import generate as G

HERE = Path(__file__).parent
STAGE_NOUM = HERE / "staging" / "cards"
STAGE_PHEN = HERE / "staging" / "phenomena" / "cards"
REPORT = HERE / "staging-report.md"
JAR = Path(r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\desktop-1.0.jar")
STOP = {"a", "an", "the", "to", "of", "your", "you", "this", "is", "are", "and", "or",
        "for", "in", "on", "at", "it", "its", "be", "by", "all", "each", "deal", "gain",
        "apply", "card", "cards", "damage"}


def delink(s):
    def repl(m):
        inner = m.group(1)
        return inner.split("|", 1)[1] if "|" in inner else inner.split("/")[-1]
    return re.sub(r"\[\[([^\]]+)\]\]", repl, s or "")


def load_loc():
    try:
        with zipfile.ZipFile(JAR) as z:
            with z.open("localization/eng/cards.json") as f:
                raw = json.loads(f.read().decode("utf-8-sig"))
    except (FileNotFoundError, OSError):
        return None
    out = {}
    for cid, e in raw.items():
        d = e.get("DESCRIPTION", "")
        if isinstance(d, list):
            d = " ".join(d)
        out.setdefault(e.get("NAME", cid).lower(), d)
    return out


def norm_words(text):
    text = delink(text).replace("NL", " ")
    text = re.sub(r"#[a-z]", "", text)
    text = re.sub(r"![A-Za-z]+!", "", text)
    text = re.sub(r"\[[A-Z]\]", " energy ", text)
    text = re.sub(r"[^a-zA-Z ]", " ", text).lower()
    return {w for w in text.split() if w not in STOP and len(w) > 1}


def sig(text, vocab, drop=()):
    """(keywords, number-SET) for meaning comparison. Energy symbols normalized,
    number multiplicity ignored (base+upgrade repetition is a representation
    artifact, not a meaning change), and the card's own name dropped (a card
    naming itself isn't a fact)."""
    t = G.energy(delink(text)).lower()
    for d in drop:
        if d:
            t = t.replace(d.lower(), " ")
    nums = frozenset(re.findall(r"\d+", t))
    kw = frozenset(w for w in vocab if re.search(rf"(?<![a-z]){re.escape(w)}s?(?![a-z])", t))
    return (kw, nums)


def parse_current(path):
    if not path.exists():
        return None
    f = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*-\s*\*\*(.+?):\*\*\s*(.+)", line)
        if m:
            f[m.group(1).strip().lower()] = m.group(2).strip()
    return f


def classify_meta(field, cur, gen):
    """AUTO / PRESERVE / REVIEW for one metadata disagreement."""
    cl = cur.lower()
    if field == "cost" and "(" in cur:
        return "AUTO", f"cost-encoding {cur!r} -> base {gen!r}"
    if field == "rarity" and ("special" in cl or "(from" in cl or "generated" in cl):
        return "PRESERVE", f"keep provenance {cur!r} (gen: {gen!r})"
    if field == "character" and cur.strip() == "All":
        return "PRESERVE", f"keep shared-card 'All' (gen: {gen!r})"
    return "REVIEW", f"{field} {cur!r} -> {gen!r}"


def main():
    cards = json.loads((HERE / "data" / "sts1_cards.json").read_text(encoding="utf-8"))
    link_map = G.build_link_map()
    loc = load_loc()
    vocab = {k.lower() for k in link_map} | {"attack", "skill", "power", "status", "curse",
            "block", "draw", "exhaust", "energy", "scry", "channel", "strength",
            "dexterity", "vulnerable", "weak", "frail", "poison"}
    STAGE_NOUM.mkdir(parents=True, exist_ok=True)
    STAGE_PHEN.mkdir(parents=True, exist_ok=True)

    meta = {"AUTO": [], "PRESERVE": [], "REVIEW": []}
    effect_diffs, threeway, extra_facts, phantom, style_only = [], [], [], [], []
    current_names = {p.stem for p in G.CARDS_DIR.glob("*.md")}
    seen = set()
    n_phen = 0

    for card in cards:
        nm = card["name"]
        slug = G.slugify(nm)
        seen.add(slug)
        (STAGE_NOUM / f"{slug}.md").write_text(G.render(card, link_map), encoding="utf-8")
        if G.has_upgrade(card):
            (STAGE_PHEN / f"{slug}-plus.md").write_text(G.render_phenomenon(card, link_map), encoding="utf-8")
            n_phen += 1

        cur = parse_current(G.CARDS_DIR / f"{slug}.md")
        if cur is None:
            phantom.append((nm, "in dataset, no current entry (uncovered)"))
            continue

        gcost = G.fmt_cost(card.get("cost")) or ""
        gchar = G.COLOR_CHAR.get((card.get("color") or "").lower(), "")
        grar = G.RARITY_MAP.get(card.get("rarity", ""), card.get("rarity", ""))
        for field, gen_val in (("cost", gcost), ("character", gchar), ("rarity", grar)):
            cur_val = cur.get(field, "")
            if cur_val and gen_val and cur_val != gen_val:
                bucket, detail = classify_meta(field, cur_val, gen_val)
                meta[bucket].append((nm, detail))

        # effect meaning: current (effect+upgraded) vs generated (base + resolved upgrade)
        cur_eff = (cur.get("effect", "") + " " + cur.get("upgraded", "")).strip()
        gen_resolved = G.PHENOMENON_EFFECT.get(nm) or G._upg_desc(card) or ""
        gen_eff = (G._base_desc(card) + " " + gen_resolved).strip()
        cs, gs = sig(cur_eff, vocab, drop=[nm]), sig(gen_eff, vocab, drop=[nm])
        if cs != gs:
            ck, cn = cs; gk, gn = gs
            d = []
            if gk - ck: d.append(f"gen adds {sorted(gk-ck)}")
            if ck - gk: d.append(f"cur has not-in-gen {sorted(ck-gk)}")
            if cn != gn: d.append(f"nums cur-only {sorted(cn-gn)} gen-only {sorted(gn-cn)}")
            effect_diffs.append((nm, "; ".join(d) or "wording"))
            if ck - gk:
                extra_facts.append((nm, sorted(ck - gk)))
        else:
            style_only.append(nm)

        if loc and nm.lower() in loc:
            gw, cw = norm_words(loc[nm.lower()]), norm_words(G._base_desc(card))
            if (gw - cw) or (cw - gw):
                threeway.append((nm, sorted(gw - cw), sorted(cw - gw)))

    for slug in sorted(current_names - seen):
        phantom.append((slug, "current entry, NOT in dataset (phantom/naming)"))

    L = ["# Card Regeneration — Staging Review\n",
         f"- dataset: {len(cards)} | current: {len(current_names)} | staged noumena: {len(seen)} | staged phenomena: {n_phen}",
         f"- METADATA: AUTO {len(meta['AUTO'])} | PRESERVE {len(meta['PRESERVE'])} | **REVIEW {len(meta['REVIEW'])}**",
         f"- EFFECT-meaning diffs: {len(effect_diffs)} | style-only (safe): {len(style_only)}",
         f"- 3-WAY (community vs jar): {len(threeway)} | EXTRA-FACTS at risk: {len(extra_facts)} | PHANTOM/coverage: {len(phantom)}\n",
         "## METADATA — REVIEW (genuine disagreements; eyeball before apply)\n"]
    for nm, d in sorted(meta["REVIEW"]): L.append(f"- **{nm}** — {d}")
    L.append("\n## METADATA — AUTO (cost-encoding cleaned to base; safe)\n")
    for nm, d in sorted(meta["AUTO"]): L.append(f"- **{nm}** — {d}")
    L.append("\n## METADATA — PRESERVE (kept from current)\n")
    for nm, d in sorted(meta["PRESERVE"]): L.append(f"- **{nm}** — {d}")
    L.append("\n## EFFECT-meaning diffs (numbers / keywords; phrasing ignored)\n")
    for nm, d in sorted(effect_diffs): L.append(f"- **{nm}** — {d}")
    L.append("\n## 3-WAY — community wording vs GAME JAR (prefer the jar)\n")
    for nm, g, c in sorted(threeway): L.append(f"- **{nm}** — jar-only: {g} | community-only: {c}")
    L.append("\n## EXTRA-FACTS at risk (current keyword absent from generated — verify)\n")
    for nm, kws in sorted(extra_facts): L.append(f"- **{nm}** — {kws}")
    L.append("\n## PHANTOM / coverage\n")
    for nm, d in sorted(phantom): L.append(f"- **{nm}** — {d}")

    REPORT.write_text("\n".join(L), encoding="utf-8")
    print(f"staged {len(seen)} noumena + {n_phen} phenomena -> {STAGE_NOUM.parent}")
    print(f"report -> {REPORT}\n")
    print("\n".join(L[1:5]))


if __name__ == "__main__":
    main()
