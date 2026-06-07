#!/usr/bin/env python3
"""Split a staged book PDF into per-chapter PDFs for the reader pipeline.

  reader_split_book.py <book_slug> [plan|split]

Reads /home/pkis/docs/books/<book_slug>.pdf. Detects chapters from the table of contents
(no PDF bookmarks needed), calibrates the printed->PDF page offset by finding a chapter
title in the body, and computes each chapter's PDF page range.
  plan  — print the detected chapter map only (default).
  split — also write /home/pkis/docs/sources/<book_slug>-chNN/<book_slug>-chNN.pdf.

Chapter source cards + reader builds are handled downstream.
"""
import sys, os, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reader_build as rb  # env load + app + Anthropic _create + MODEL

BOOKS = "/home/pkis/docs/books"
DOCS_SOURCES = "/home/pkis/docs/sources"

TOC_SYSTEM = (
    "You read a book's (often OCR-noisy) table of contents and list its TOP-LEVEL chapters only — "
    "not sections like 3.2, and not front/back matter (preface, references, index, appendix unless "
    "it is a numbered chapter). Fix obvious OCR glitches in titles (e.g. 'T rees'->'Trees', "
    "'Classiﬁcation'->'Classification'). Some entries wrap across lines.\n"
    "OUTPUT: one chapter per line, EXACTLY as '<number>|<clean title>|<printed start page>'. "
    "Then a final line 'BACK|<printed page where References/Bibliography/Index begins, or blank>'. "
    "Output nothing else."
)


def _norm(s):
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())


def page_texts(reader, lo=0, hi=None):
    hi = hi if hi is not None else len(reader.pages)
    out = {}
    for i in range(lo, hi):
        try:
            out[i] = reader.pages[i].extract_text() or ""
        except Exception:
            out[i] = ""
    return out


def parse_toc(reader, scan=50):
    """Send the Contents-page text to Claude and parse chapters from its delimited reply.
    Returns ordered [(num, title, printed_page)] and the printed back-matter page (or None)."""
    toc_text = []
    for i in range(min(scan, len(reader.pages))):
        t = reader.pages[i].extract_text() or ""
        if "Contents" in t or (toc_text and re.search(r"^\s*\d{1,2}(\.\d+)?\s+\w", t, re.M)):
            toc_text.append(t)
        elif toc_text:
            break  # left the TOC region
    blob = "\n".join(toc_text)[:24000]
    resp = rb._create(model=rb.MODEL, max_tokens=2000, system=TOC_SYSTEM,
                      messages=[{"role": "user", "content": f"TABLE OF CONTENTS:\n\n{blob}"}])
    chapters, back_page = [], None
    for line in rb._resp_text(resp).splitlines():
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 2:
            continue
        if parts[0].upper() == "BACK":
            try: back_page = int(re.sub(r"\D", "", parts[1]))
            except Exception: back_page = None
            continue
        if parts[0].isdigit() and len(parts) >= 3 and re.sub(r"\D", "", parts[2]):
            chapters.append((int(parts[0]), parts[1], int(re.sub(r"\D", "", parts[2]))))
    return chapters, back_page


def calibrate_offset(reader, chapters, ptexts):
    """Find PDF-index = printed_page + offset, by locating chapter titles in the body."""
    body_lo = 0
    # body starts after the front matter; search from a bit past the TOC
    offsets = []
    for num, title, pg in chapters[:6]:
        target = _norm(title)
        for i in range(15, len(reader.pages)):
            # Search a wide window: some PDFs (e.g. MacKay) prefix every page with a
            # recurring copyright/watermark line that pushes the title past a short slice.
            head = _norm(ptexts.get(i, "")[:800])
            if target and target[:18] in head:
                offsets.append(i - pg)
                break
    if not offsets:
        return None
    # take the most common offset (robust to a stray miss)
    return max(set(offsets), key=offsets.count)


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    import pypdf
    slug = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "plan"
    # Optional manual printed->PDF page offset override for PDFs the heuristic can't calibrate.
    manual_offset = int(sys.argv[3]) if len(sys.argv) > 3 else None
    path = os.path.join(BOOKS, slug + ".pdf")
    reader = pypdf.PdfReader(path)
    n = len(reader.pages)
    chapters, back_page = parse_toc(reader)
    if not chapters:
        print("no chapters parsed from TOC"); sys.exit(2)
    ptexts = page_texts(reader, 0, n)
    offset = manual_offset if manual_offset is not None else calibrate_offset(reader, chapters, ptexts)
    if offset is None:
        print("could not calibrate page offset (pass a manual offset as the 3rd arg)"); sys.exit(3)
    # back-matter boundary: cap the last chapter before References/Bibliography
    back_pdf = (back_page + offset) if back_page else None
    if back_pdf is None:
        last_start = chapters[-1][2] + offset
        for i in range(max(last_start + 1, 0), n):
            if _norm(ptexts.get(i, "")[:40]).startswith(("references", "bibliography")):
                back_pdf = i; break
    print(f"book: {slug}  pages={n}  chapters={len(chapters)}  offset={offset}  back_matter_pdf={back_pdf}")
    # compute pdf page ranges
    rows = []
    for idx, (num, title, pg) in enumerate(chapters):
        start = pg + offset
        if idx + 1 < len(chapters):
            end = chapters[idx + 1][2] + offset - 1
        else:
            end = (back_pdf - 1) if back_pdf else n - 1
        start = max(0, min(start, n - 1)); end = max(start, min(end, n - 1))
        rows.append((num, title, start, end))
        print(f"  ch{num:02d}  pdf p{start+1:>4}-{end+1:<4} ({end-start+1:>3}p)  {title}")

    if mode != "split":
        return
    for num, title, start, end in rows:
        cslug = f"{slug}-ch{num:02d}"
        d = os.path.join(DOCS_SOURCES, cslug)
        os.makedirs(d, exist_ok=True)
        w = pypdf.PdfWriter()
        for i in range(start, end + 1):
            w.add_page(reader.pages[i])
        with open(os.path.join(d, cslug + ".pdf"), "wb") as f:
            w.write(f)
        print(f"  wrote {cslug}.pdf ({end-start+1}p)")
    print(f"=== split {len(rows)} chapters ===")


if __name__ == "__main__":
    main()
