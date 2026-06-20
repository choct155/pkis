#!/usr/bin/env python3
"""link_sources_driver.py — Librarian pass: connect unlinked standalone sources to
the concepts they support, so the Priority "why read it" rationale lights up.

For each unlinked standalone source (in wiki/sources/, NOT a book chapter — those
are a separate granularity question, skipped here), semantically retrieve candidate
concepts, have Haiku CONSERVATIVELY confirm which the source genuinely supports,
and append the source to those concepts' `sources` frontmatter (via tool_edit_node
— the sanctioned write path: correct YAML, commit, push, cache refresh).

Runs on the server in the app venv (imports app for the graph + Anthropic client +
write tools). Resumable via a state file. Use --dry-run to preview matches with NO
writes.

    python tools/link_sources_driver.py --dry-run
    python tools/link_sources_driver.py           # apply
    python tools/link_sources_driver.py --limit 5 # first N (testing)
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Load the service env (ANTHROPIC_API_KEY etc.) BEFORE importing app — app builds
# the Anthropic client at import time, so the key must be present first.
_envfile = os.environ.get("PKIS_ENV", "/home/pkis/.env")
if os.path.exists(_envfile):
    for _line in open(_envfile):
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip().strip('"').strip("'"))

import app  # noqa: E402

MODEL = "claude-haiku-4-5"
CONCEPT_FOLDERS = ["concepts", "techniques", "results", "principles", "frameworks", "problems"]
STATE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), ".link_sources_state.json")

PROMPT = """You are the PKIS Librarian. Decide which knowledge-graph CONCEPTS a SOURCE \
genuinely supports — i.e. the source provides direct evidence for, substantially \
covers, or is a primary reference for that concept. Be CONSERVATIVE: only include a \
concept when the connection is specific and real. It is better to omit a weak match \
than to assert a spurious one. A paper typically supports 1-4 concepts and a book \
chapter 2-8; some support none of the candidates.

SOURCE
title: {title}
abstract/notes: {abstract}

CANDIDATE CONCEPTS (id │ title │ excerpt)
{candidates}

Return ONLY a JSON array of the `id`s of the concepts this source genuinely supports \
(e.g. ["pkis:concept:foo","pkis:technique:bar"]). Empty array if none fit."""


def unlinked_sources(chapters=False):
    """Unlinked sources to process. chapters=False → standalone papers/books (no
    parent_book); chapters=True → book chapters (parent_book set, matched on their
    topical title + summary)."""
    nodes = app.load_all_nodes()
    concepts = [n for n in nodes if n.get("frontmatter", {}).get("knowledge_type") in
                ("concept", "technique", "result", "principle", "framework", "problem")]
    referenced = set()
    for c in concepts:
        for s in (c.get("frontmatter", {}).get("sources") or []):
            referenced.add(app._norm_source_ref(s))
    out = []
    for n in nodes:
        if n.get("node_type") != "sources":
            continue
        is_chapter = bool(n.get("frontmatter", {}).get("parent_book"))
        if is_chapter != chapters:
            continue
        if n["slug"] in referenced:
            continue
        out.append(n)
    return out


def confirm_concepts(source, candidates):
    cand_lines = "\n".join(
        f"{c['iri']} │ {c['canonical_title']} │ {(c.get('excerpt') or '')[:160]}"
        for c in candidates)
    prompt = PROMPT.format(
        title=source["frontmatter"].get("title", source["slug"]),
        abstract=(source.get("content") or "").strip()[:1500] or "(no abstract on file)",
        candidates=cand_lines)
    resp = app.anthropic_client.messages.create(
        model=MODEL, max_tokens=300, messages=[{"role": "user", "content": prompt}])
    app.log_usage(app.USAGE_DB_PATH, resp, origin="pkis-librarian-link", project="pkis",
                  attributes={"source": source["slug"]})
    txt = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text").strip()
    txt = txt[txt.find("["): txt.rfind("]") + 1] if "[" in txt else "[]"
    try:
        ids = json.loads(txt)
    except Exception:
        return []
    valid = {c["iri"] for c in candidates}
    return [i for i in ids if i in valid]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--chapters", action="store_true", help="process book chapters (parent_book)")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    state = {}
    if os.path.exists(STATE_PATH):
        state = json.loads(open(STATE_PATH).read())

    sources = unlinked_sources(chapters=args.chapters)
    if args.limit:
        sources = sources[:args.limit]
    print(f"{len(sources)} unlinked standalone sources to consider"
          f"{' (DRY RUN)' if args.dry_run else ''}\n")

    # concept_iri -> set(source_slug) to append
    additions = {}
    for i, src in enumerate(sources, 1):
        slug = src["slug"]
        if state.get(slug) == "done" and not args.dry_run:
            continue
        q = (src["frontmatter"].get("title", "") + ". " + (src.get("content") or "")).strip()[:1200]
        cands = app.hybrid_search(q, node_types=CONCEPT_FOLDERS, max_results=12)
        if not cands:
            print(f"[{i}/{len(sources)}] {slug}: no candidates"); state[slug] = "done"; continue
        confirmed = confirm_concepts(src, cands)
        titles = {c["iri"]: c["canonical_title"] for c in cands}
        print(f"[{i}/{len(sources)}] {slug} → {len(confirmed)}: "
              + ", ".join(titles.get(c, c) for c in confirmed))
        for ciri in confirmed:
            additions.setdefault(ciri, set()).add(slug)
        state[slug] = "done"

    if args.dry_run:
        print(f"\nDRY RUN — would touch {len(additions)} concepts, "
              f"{sum(len(v) for v in additions.values())} new source links. No writes.")
        return

    # Apply: one edit_node per concept (append to its sources, deduped).
    print(f"\nApplying to {len(additions)} concepts…")
    for ciri, slugs in additions.items():
        p = app.find_node_path_by_iri(ciri)
        if not p:
            continue
        cur = app.load_node(p).get("frontmatter", {}).get("sources") or []
        cur_norm = {app._norm_source_ref(s) for s in cur}
        new = list(cur) + [s for s in sorted(slugs) if s not in cur_norm]
        if len(new) == len(cur):
            continue
        try:
            app.tool_edit_node(iri=ciri, frontmatter_updates={"sources": new},
                               commit_message=f"librarian: link {len(slugs)} source(s) to {ciri}")
        except Exception as e:
            print(f"  ! {ciri}: {e}")
    open(STATE_PATH, "w").write(json.dumps(state))
    print("done.")


if __name__ == "__main__":
    main()
