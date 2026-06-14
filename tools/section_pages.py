#!/usr/bin/env python3
"""Annotate reader payloads with a section -> PDF-page mapping (for synced PDF view).

For each reader payload that has a corresponding chapter PDF at
/docs/sources/<slug>/<slug>.pdf, compute which PDF page each section starts on by
token-overlap scoring (the paper_md is reflowed/paraphrased, so exact substring
matching fails) under a monotonic non-decreasing constraint (a section can't start
before the previous one). Writes `page` onto each section and a top-level
`pdf_url` onto the payload. Free — no model calls. Idempotent: skips payloads that
already carry pages unless --force.

Usage:
  /home/pkis/venv/bin/python section_pages.py            # all reader payloads
  /home/pkis/venv/bin/python section_pages.py <slug> ... # specific slugs
  /home/pkis/venv/bin/python section_pages.py --force    # recompute existing
"""
import json
import os
import re
import sys

READER = "/home/pkis/pkis-wiki/wiki/reader"
DOCS = "/home/pkis/docs/sources"
DOCS_URL = "/docs/sources"

STOP = set(
    "the a an of to in and or for is are be on by with as that this we it its from "
    "at can not if then so each one two into has have was were will would there here "
    "such these those than but also more most some any all".split()
)


def toks(s):
    return [w for w in re.sub(r"[^a-z0-9 ]", " ", (s or "").lower()).split()
            if len(w) > 3 and w not in STOP]


def page_for_sections(sections, page_tokens):
    """Assign each section a starting PDF page by token overlap, regularized by a
    positional prior so a single spurious late match can't drag the rest forward.

    Sections are ordered and their text length tells us roughly how far through the
    document each one sits; we expect its page near that fraction. Score a page by
    (fraction of probe tokens it contains) minus a penalty for deviating from the
    expected page. Then enforce non-decreasing pages with a final cumulative-max.
    """
    npages = len(page_tokens)
    if npages == 0:
        return [1] * len(sections)
    # Expected page per section from its cumulative share of the chapter text.
    lengths = [max(1, len(s.get("paper_md", ""))) for s in sections]
    total = sum(lengths)
    cum = 0.0
    LAMBDA = 0.55  # weight of the positional prior vs. token evidence
    raw = []
    for s, ln in zip(sections, lengths):
        frac = (cum + ln / 2) / total
        cum += ln
        expected = frac * (npages - 1)  # 0-based
        probe = toks(s.get("title", "") + " " + s.get("paper_md", ""))[:40]
        if not probe:
            raw.append(int(round(expected)))
            continue
        best, bi = -1e9, int(round(expected))
        for i in range(npages):
            overlap = sum(1 for w in probe if w in page_tokens[i]) / len(probe)
            score = overlap - LAMBDA * abs(i - expected) / npages
            if score > best:
                best, bi = score, i
        raw.append(bi)
    # Enforce monotonic non-decreasing, then to 1-based.
    out = []
    run = 0
    for p in raw:
        run = max(run, p)
        out.append(run + 1)
    return out


def process(slug, force=False):
    pj = os.path.join(READER, slug, "payload.json")
    pdf = os.path.join(DOCS, slug, f"{slug}.pdf")
    if not os.path.isfile(pj):
        return f"SKIP {slug}: no payload"
    if not os.path.isfile(pdf):
        return f"SKIP {slug}: no PDF (not a split chapter)"
    d = json.load(open(pj))
    secs = d.get("sections", [])
    if not secs:
        return f"SKIP {slug}: no sections"
    if not force and all("page" in s for s in secs):
        return f"SKIP {slug}: already paged"
    from pypdf import PdfReader
    pages = [set(toks(p.extract_text())) for p in PdfReader(pdf).pages]
    assigned = page_for_sections(secs, pages)
    for s, pg in zip(secs, assigned):
        s["page"] = pg
    d["pdf_url"] = f"{DOCS_URL}/{slug}/{slug}.pdf"
    d["pdf_pages"] = len(pages)
    json.dump(d, open(pj, "w"), ensure_ascii=False)
    span = f"{assigned[0]}-{assigned[-1]}" if assigned else "?"
    return f"OK   {slug}: {len(secs)} sections over {len(pages)}pp (pages {span})"


def main(argv):
    force = "--force" in argv
    slugs = [a for a in argv if not a.startswith("--")]
    if not slugs:
        slugs = sorted(d for d in os.listdir(READER)
                       if os.path.isfile(os.path.join(READER, d, "payload.json")))
    ok = paged = skipped = 0
    for slug in slugs:
        try:
            msg = process(slug, force)
        except Exception as ex:  # noqa: BLE001
            msg = f"FAIL {slug}: {ex}"
        print(msg)
        if msg.startswith("OK"):
            ok += 1
        elif "no PDF" in msg or "already paged" in msg:
            skipped += 1
    print(f"\n== paged={ok} skipped={skipped} of {len(slugs)} ==")


if __name__ == "__main__":
    main(sys.argv[1:])
