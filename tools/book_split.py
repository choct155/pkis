#!/usr/bin/env python3
"""Split a whole-book PDF into per-chapter PDFs in the PKIS docstore.

Usage: book_split.py <book_pdf> <map_json>
  map_json: {"<slug>-chNN": [start_page, end_page], ...}  (1-indexed inclusive)
Writes each chapter to /home/pkis/docs/sources/<slug>-chNN/<slug>-chNN.pdf
"""
import sys, os, json, pypdf

book_pdf, map_json = sys.argv[1], sys.argv[2]
ranges = json.load(open(map_json))
r = pypdf.PdfReader(book_pdf)
npages = len(r.pages)
base = "/home/pkis/docs/sources"

for chslug, (start, end) in sorted(ranges.items()):
    start = max(1, int(start)); end = min(npages, int(end))
    w = pypdf.PdfWriter()
    for p in range(start - 1, end):  # 1-indexed inclusive -> 0-indexed range
        w.add_page(r.pages[p])
    d = os.path.join(base, chslug)
    os.makedirs(d, exist_ok=True)
    out = os.path.join(d, f"{chslug}.pdf")
    with open(out, "wb") as f:
        w.write(f)
    print(f"{chslug}: pages {start}-{end} ({end - start + 1}pp) -> {out}")
