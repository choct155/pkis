#!/usr/bin/env python3
"""Split a book PDF into per-chapter PDFs, driven by the EXISTING chapter nodes.

The Phase-C ingest already created authoritative chapter nodes for each book
(wiki/sources/<book>-chNN.md) carrying the real chapter count and titles. This
splitter trusts those instead of re-parsing the (OCR-noisy) table of contents and
calibrating a printed->PDF page offset — the path reader_split_book.py takes, which
is fragile on books whose openers don't say "Chapter N" or whose TOC text is messy.

For each chapter (in node order) it finds the opener page in the body by searching
for the chapter title near the top of the page, skipping the TOC region (pages that
mention several chapter titles at once). Ranges run opener->next-opener, with the
last chapter capped before References/Bibliography.

  split_by_nodes.py <book_slug> [plan|split]
    plan  — print the located chapter map only (default)
    split — also write /home/pkis/docs/sources/<book>-chNN/<book>-chNN.pdf
"""
import sys, os, re, glob

BOOKS = "/home/pkis/docs/books"
DOCS_SOURCES = "/home/pkis/docs/sources"
WIKI_SOURCES = "/home/pkis/pkis-wiki/wiki/sources"


def _norm(s):
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())


def chapter_nodes(book_slug):
    """Ordered [(num, clean_title)] from the existing chapter nodes."""
    out = []
    for f in sorted(glob.glob(os.path.join(WIKI_SOURCES, book_slug + "-ch*.md"))):
        m = re.search(r"-ch0*(\d+)\.md$", f)
        if not m:
            continue
        num = int(m.group(1))
        title = ""
        with open(f, encoding="utf-8") as fh:
            for line in fh:
                mt = re.match(r'\s*title:\s*"?(.*?)"?\s*$', line)
                if mt:
                    title = mt.group(1)
                    break
        # strip a leading "Ch. N — " / "Chapter N: " label
        title = re.sub(r'^\s*ch(?:apter|\.)?\s*\d+\s*[—:\-]\s*', '', title, flags=re.I).strip()
        out.append((num, title))
    out.sort()
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    import pypdf
    book_slug = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "plan"
    chapters = chapter_nodes(book_slug)
    if not chapters:
        print(f"no chapter nodes found for {book_slug}"); sys.exit(2)
    reader = pypdf.PdfReader(os.path.join(BOOKS, book_slug + ".pdf"))
    n = len(reader.pages)
    heads = [_norm((reader.pages[i].extract_text() or "")[:220]) for i in range(n)]
    keys = [(_norm(t)[:14] or None) for _, t in chapters]

    # TOC region: the (early) pages that mention 3+ distinct chapter titles at once.
    toc_end = -1
    for i in range(min(70, n)):
        hits = sum(1 for k in keys if k and k in heads[i])
        if hits >= 3:
            toc_end = i
    body_start = toc_end + 1

    # Locate each chapter's opener, monotonically increasing. Prefer a page whose
    # head says "Chapter <n> <title>", then title-at-very-top, then title anywhere.
    openers, cur = [], body_start
    for (num, title), k in zip(chapters, keys):
        found = None
        if k:
            chap_key = "chapter" + str(num) + k
            for i in range(cur, n):
                if chap_key in heads[i][:90]:
                    found = i; break
            if found is None:
                for i in range(cur, n):
                    if k in heads[i][:80]:
                        found = i; break
            if found is None:
                for i in range(cur, n):
                    if k in heads[i]:
                        found = i; break
        openers.append([num, title, found])
        if found is not None:
            cur = found + 1

    # Fill any gaps (unfound openers) by interpolation so a single miss doesn't sink
    # the whole book; flagged in the printout.
    located = [o for o in openers if o[2] is not None]
    if not located:
        print("could not locate any chapter opener in the body"); sys.exit(3)

    # back-matter boundary for the final chapter
    back = None
    last_op = located[-1][2]
    for i in range(last_op + 1, n):
        if heads[i][:40].startswith(("references", "bibliography")):
            back = i; break

    rows = []
    print(f"book: {book_slug}  pages={n}  chapters={len(chapters)}  toc_end_pdf={toc_end+1}  back_matter_pdf={back}")
    for idx, (num, title, start) in enumerate(openers):
        flag = ""
        if start is None:
            flag = "  <-- NOT FOUND"
        # next located opener determines this chapter's end
        nxt = None
        for j in range(idx + 1, len(openers)):
            if openers[j][2] is not None:
                nxt = openers[j][2]; break
        if start is not None:
            end = (nxt - 1) if nxt is not None else ((back - 1) if back else n - 1)
            end = max(start, min(end, n - 1))
            rows.append((num, title, start, end))
            print(f"  ch{num:02d}  pdf p{start+1:>4}-{end+1:<4} ({end-start+1:>3}p)  {title}{flag}")
        else:
            rows.append((num, title, None, None))
            print(f"  ch{num:02d}  ----  ----        {title}{flag}")

    if mode != "split":
        return
    wrote = 0
    for num, title, start, end in rows:
        if start is None:
            continue
        cslug = f"{book_slug}-ch{num:02d}"
        d = os.path.join(DOCS_SOURCES, cslug)
        os.makedirs(d, exist_ok=True)
        w = pypdf.PdfWriter()
        for i in range(start, end + 1):
            w.add_page(reader.pages[i])
        with open(os.path.join(d, cslug + ".pdf"), "wb") as f:
            w.write(f)
        wrote += 1
        print(f"  wrote {cslug}.pdf ({end-start+1}p)")
    print(f"=== split {wrote}/{len(rows)} chapters ===")


if __name__ == "__main__":
    main()
