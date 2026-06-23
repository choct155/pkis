#!/usr/bin/env python3
"""Relabel book + chapter source nodes with a visible [ABBREV Author] title tag,
add an `abbrev` frontmatter field, and rebuild each book's ## Chapters TOC so the
chapter numbers are visible.

Idempotent: an existing [...] prefix is replaced (not stacked), and the TOC is
regenerated from the chapter files each run.

Edits are surgical (title line + abbrev line + Chapters block only) to keep diffs
clean — the rest of the frontmatter is left byte-for-byte untouched.

Usage:
    python tools/relabel_books.py [--dry-run]
"""
import json
import os
import re
import sys

import frontmatter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_labels import ABBREV, title_prefix  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "wiki", "sources")

DRY = "--dry-run" in sys.argv

TAG_RE = re.compile(r"^\s*\[[^\]]*\]\s*")          # leading [ABBREV Author] tag
TITLE_LINE_RE = re.compile(r"(?m)^title:.*$")
ABBREV_LINE_RE = re.compile(r"(?m)^abbrev:.*$")
CHAPTERS_RE = re.compile(r"(?ms)^## Chapters[ \t]*\n.*?(?=^## |\Z)")
FM_RE = re.compile(r"(?s)^(---\n)(.*?)(\n---\n)(.*)$")
CHNN_RE = re.compile(r"-(ch\d+\w*|app\w+)$")


def strip_tag(title):
    return TAG_RE.sub("", title or "")


def parent_slug(pb):
    pb = str(pb).strip().strip("[]")
    if pb.startswith("pkis:source:"):
        pb = pb[len("pkis:source:"):]
    return pb


def chnn_of(slug, parent):
    if parent and slug.startswith(parent + "-"):
        return slug[len(parent) + 1:]
    m = CHNN_RE.search(slug)
    return m.group(1) if m else slug


def chnn_sort_key(chnn):
    m = re.match(r"(ch|app)0*(\d+)", chnn)
    if m:
        return (0 if m.group(1) == "ch" else 1, int(m.group(2)), "")
    return (2, 0, chnn)


def yaml_str(s):
    # JSON double-quoted strings are valid YAML; keep unicode (em-dash) literal.
    return json.dumps(s, ensure_ascii=False)


def split_file(text):
    m = FM_RE.match(text)
    if not m:
        return None
    return {"open": m.group(1), "fm": m.group(2), "close": m.group(3), "body": m.group(4)}


def set_title(fm_text, new_title):
    return TITLE_LINE_RE.sub(lambda _: f"title: {yaml_str(new_title)}", fm_text, count=1)


def set_abbrev(fm_text, ab):
    line = f"abbrev: {yaml_str(ab)}"
    if ABBREV_LINE_RE.search(fm_text):
        return ABBREV_LINE_RE.sub(lambda _: line, fm_text, count=1)
    return line + "\n" + fm_text


def main():
    files = sorted(f for f in os.listdir(SRC) if f.endswith(".md"))
    books = {}          # slug -> path
    chapters = {}       # parent_slug -> [(chapter_slug, chnn, clean_label, path, authors)]
    missing_abbrev = set()

    # ---- pass 1: classify ----
    for fn in files:
        path = os.path.join(SRC, fn)
        slug = fn[:-3]
        try:
            post = frontmatter.load(path)
        except Exception as e:
            print(f"  ! skip {fn}: parse error {e}")
            continue
        md = post.metadata
        if md.get("type") == "book" or md.get("source_type") == "book":
            books[slug] = path
        if md.get("parent_book"):
            parent = parent_slug(md["parent_book"])
            clean = strip_tag(md.get("title", slug))
            chapters.setdefault(parent, []).append(
                (slug, chnn_of(slug, parent), clean, path, md.get("authors", ""))
            )
            if parent not in ABBREV:
                missing_abbrev.add(parent)

    # Any chapter parent with a node file is a book, regardless of how its
    # `type`/`source_type` field is (mis)labeled (e.g. legacy source_type, or a
    # book mistagged as paper).
    for parent in chapters:
        if parent not in books:
            p = os.path.join(SRC, parent + ".md")
            if os.path.exists(p):
                books[parent] = p

    n_ch = sum(len(v) for v in chapters.values())
    print(f"Found {len(books)} books, {n_ch} chapters across {len(chapters)} parents.")
    if missing_abbrev:
        print(f"  ! no abbrev for parents (chapters get author-only tag): {sorted(missing_abbrev)}")

    touched = 0

    # ---- pass 2: chapters ----
    for parent, items in chapters.items():
        ab = ABBREV.get(parent, "")
        for slug, chnn, clean, path, authors in items:
            new_title = title_prefix(parent, authors, ab) + clean
            text = open(path, encoding="utf-8").read()
            parts = split_file(text)
            if not parts:
                print(f"  ! skip {slug}: no frontmatter block")
                continue
            fm = set_abbrev(set_title(parts["fm"], new_title), ab) if ab else set_title(parts["fm"], new_title)
            out = parts["open"] + fm + parts["close"] + parts["body"]
            if out != text:
                touched += 1
                if DRY:
                    if touched <= 6:
                        print(f"    {slug}: title -> {new_title}")
                else:
                    open(path, "w", encoding="utf-8").write(out)

    # ---- pass 3: books (title + abbrev + TOC) ----
    for slug, path in sorted(books.items()):
        post = frontmatter.load(path)
        ab = ABBREV.get(slug, "")
        authors = post.metadata.get("authors", "")
        new_title = title_prefix(slug, authors, ab) + strip_tag(post.metadata.get("title", slug))

        toc_items = sorted(chapters.get(slug, []), key=lambda t: chnn_sort_key(t[1]))
        toc_lines = "\n".join(f"- [[{cs}]] — {clean}" for cs, _chnn, clean, _p, _a in toc_items)
        new_toc = "## Chapters\n" + (toc_lines + "\n" if toc_lines else "")

        text = open(path, encoding="utf-8").read()
        parts = split_file(text)
        if not parts:
            print(f"  ! skip book {slug}: no frontmatter block")
            continue
        fm = set_abbrev(set_title(parts["fm"], new_title), ab) if ab else set_title(parts["fm"], new_title)
        body = parts["body"]
        if CHAPTERS_RE.search(body):
            body = CHAPTERS_RE.sub(lambda _: new_toc, body, count=1)
        elif toc_items:
            body = body.rstrip() + "\n\n" + new_toc
        out = parts["open"] + fm + parts["close"] + body
        if out != text:
            touched += 1
            if DRY:
                print(f"    BOOK {slug}: title -> {new_title}  ({len(toc_items)} chapters in TOC)")
            else:
                open(path, "w", encoding="utf-8").write(out)

    print(f"{'Would touch' if DRY else 'Touched'} {touched} files.")


if __name__ == "__main__":
    main()
