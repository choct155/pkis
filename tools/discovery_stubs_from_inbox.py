#!/usr/bin/env python3
"""
Recast discovery_inbox.json candidates into wiki/discovery/ discovery-stub nodes
(Agent Roster v2, Build Order Phase 1c).

The discovery system (tools/discovery_openalex.py) writes a transient
`discovery_inbox.json` of candidate papers; the accept/dismiss loop and the PWA
discovery view read it. This converts each *pending* candidate into a durable,
graph-native `discovery-stub` node per SCHEMA.md § Discovery Stub — lightweight, no
Reading Path / Key Extractions, ≤2 primary concept links — so parked discoveries
live in the graph and surface when their primary concept becomes active.

Additive + idempotent: never touches discovery_inbox.json, skips a candidate whose
stub already exists. Run locally against a fetched copy, review, commit, let the VPS
pull (don't push stubs from the server).

  python3 tools/discovery_stubs_from_inbox.py --inbox <json> --out wiki/discovery [--dry-run]
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def slugify(text, maxlen=64):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    if len(s) <= maxlen:
        return s or "untitled"
    # Truncate at the last word boundary before maxlen (avoid mid-word cuts).
    cut = s[:maxlen]
    if "-" in cut:
        cut = cut[:cut.rfind("-")]
    return cut.strip("-") or "untitled"


def _slug_from_iri(iri):
    return (iri or "").split(":")[-1]


def pick_primary_concepts(cand, limit=2):
    """≤2 wikilinks: the frontier gap it fills first, then the highest-scoring
    distinct link. Returns a list of slug strings (for [[slug]] wikilinks)."""
    out, seen = [], set()
    nf = cand.get("nearest_frontier") or {}
    if isinstance(nf, dict) and nf.get("iri"):
        s = _slug_from_iri(nf["iri"])
        out.append(s); seen.add(s)
    links = cand.get("links") or []
    if isinstance(links, list):
        for ln in sorted(links, key=lambda x: x.get("score", 0), reverse=True):
            if len(out) >= limit:
                break
            s = _slug_from_iri(ln.get("iri", ""))
            if s and s not in seen:
                out.append(s); seen.add(s)
    return out[:limit]


def _yaml_list(items):
    if not items:
        return "[]"
    return "[" + ", ".join(f'"{i}"' for i in items) + "]"


def stub_markdown(cand):
    """Return (slug, markdown) for one candidate. Conformant discovery-stub:
    no Reading Path, no Key Extractions, ≤2 primary_concepts."""
    title = (cand.get("title") or "").strip()
    slug = slugify(title)
    iri = f"pkis:discovery-stub:{slug}"
    primary = [f"[[{s}]]" for s in pick_primary_concepts(cand)]
    date_added = (cand.get("discovered_at") or "")[:10] or \
        datetime.now(timezone.utc).date().isoformat()
    rationale = (cand.get("reason") or "").replace('"', "'").strip()
    domain = [d for d in (cand.get("subfield"), cand.get("field")) if d]
    src = cand.get("url") or cand.get("doi") or ""

    fm = [
        "---",
        f'id: "{iri}"',
        "aliases: []",
        f'title: "{title.replace(chr(34), chr(39))}"',
        f'authors: "{(cand.get("authors") or "").replace(chr(34), chr(39))}"',
        f"year: {cand.get('year') or 'null'}",
        "type: paper",
        f"domain: {_yaml_list(domain)}",
        "tags: []",
        f'source_url: "{src}"',
        f'doi: "{cand.get("doi") or ""}"',
        f'openalex_id: "{cand.get("openalex_id") or cand.get("id") or ""}"',
        "knowledge_type: discovery-stub",
        "status: parked",
        f"date_added: {date_added}",
        f'rationale: "{rationale}"',
        f"primary_concepts: {_yaml_list(primary)}",
        "promoted: false",
        'promoted_to: ""',
        "---",
        "",
        f"# {title}",
        "",
        f"**Parked discovery stub** — {rationale}",
        "",
    ]
    # Optional provenance prose (NOT a Reading Path / Key Extractions section).
    note = (cand.get("priority_note") or "").strip()
    if note:
        fm.append(f"Frontier note: {note}")
        fm.append("")
    prov = []
    if cand.get("venue"):
        prov.append(f"venue {cand['venue']}")
    if cand.get("sim"):
        prov.append(f"sim {cand['sim']}")
    if cand.get("cited_by"):
        prov.append(f"cited_by {cand['cited_by']}")
    if cand.get("channel"):
        prov.append(f"channel {cand['channel']}")
    if prov:
        fm.append("Provenance: " + ", ".join(prov) + ".")
        fm.append("")
    return slug, "\n".join(fm)


def existing_slugs(wiki_root):
    """All node slugs anywhere under the wiki (for global slug-uniqueness)."""
    slugs = set()
    if not os.path.isdir(wiki_root):
        return slugs
    for dirpath, _dirs, files in os.walk(wiki_root):
        for f in files:
            if f.endswith(".md") and f != "index.md":
                slugs.add(f[:-3])
    return slugs


def generate(inbox_path, out_dir, *, wiki_root=None, dry_run=False):
    d = json.load(open(inbox_path, encoding="utf-8"))
    cands = d.get("candidates", d if isinstance(d, list) else [])
    wiki_root = wiki_root or os.path.dirname(os.path.abspath(out_dir.rstrip("/")))
    taken = existing_slugs(wiki_root)
    written, skipped = [], []
    for c in cands:
        if str(c.get("status", "pending")) not in ("pending", "parked"):
            skipped.append((c.get("title"), f"status={c.get('status')}"))
            continue
        slug, md = stub_markdown(c)
        dest = os.path.join(out_dir, f"{slug}.md")
        if os.path.exists(dest) or (slug in taken and not os.path.exists(
                os.path.join(out_dir, f"{slug}.md"))):
            skipped.append((slug, "slug exists"))
            continue
        taken.add(slug)
        if not dry_run:
            os.makedirs(out_dir, exist_ok=True)
            with open(dest, "w", encoding="utf-8") as fh:
                fh.write(md)
        written.append(slug)
    return written, skipped


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--inbox", required=True)
    p.add_argument("--out", default="wiki/discovery")
    p.add_argument("--wiki-root", default=None,
                   help="wiki root for global slug-uniqueness (default: out's parent)")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)
    written, skipped = generate(args.inbox, args.out, wiki_root=args.wiki_root,
                                dry_run=args.dry_run)
    print(f"{'[dry-run] ' if args.dry_run else ''}wrote {len(written)} stub(s); "
          f"skipped {len(skipped)}")
    for s in written:
        print("  +", s)
    for slug, why in skipped:
        print("  -", slug, f"({why})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
