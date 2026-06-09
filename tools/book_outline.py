#!/usr/bin/env python3
"""Dump a PDF's nested outline (bookmarks) with 1-indexed page numbers.
Usage: book_outline.py /path/to/book.pdf
"""
import sys, pypdf
r = pypdf.PdfReader(sys.argv[1])
print(f"PAGES: {len(r.pages)}")
def walk(items, depth=0):
    for o in items:
        if isinstance(o, list):
            walk(o, depth + 1)
        else:
            try:
                pg = r.get_destination_page_number(o) + 1
            except Exception:
                pg = "?"
            print(f"{'  ' * depth}p{pg}: {str(o.title)[:75]}")
try:
    walk(r.outline)
except Exception as e:
    print(f"OUTLINE ERROR: {e}")
