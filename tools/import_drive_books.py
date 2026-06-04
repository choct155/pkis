#!/usr/bin/env python3
"""Bulk-import book PDFs from Google Drive into the PKIS book staging area.

  import_drive_books.py <manifest.json> [outdir]

manifest.json: [{"id": "<drive file id>", "slug": "<book-slug>", "title": "..."}]
Files must be link-shareable ("anyone with the link") so gdown can fetch them
server-side without OAuth. Downloads to <outdir>/<slug>.pdf (default /home/pkis/docs/books).
Skips files already present. The per-book chapter split (reader_split_book.py) runs after.
"""
import sys, os, json


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    import gdown
    manifest = json.load(open(sys.argv[1]))
    outdir = sys.argv[2] if len(sys.argv) > 2 else "/home/pkis/docs/books"
    os.makedirs(outdir, exist_ok=True)
    ok = skip = fail = 0
    for it in manifest:
        dest = os.path.join(outdir, it["slug"] + ".pdf")
        if os.path.exists(dest) and os.path.getsize(dest) > 10000:
            print(f"SKIP {it['slug']} (exists, {os.path.getsize(dest)} bytes)"); skip += 1; continue
        print(f"GET  {it['slug']}  <- {it.get('title','')}")
        try:
            gdown.download(id=it["id"], output=dest, quiet=True)
            sz = os.path.getsize(dest) if os.path.exists(dest) else 0
            if sz < 10000:
                raise RuntimeError(f"downloaded only {sz} bytes (not shared / blocked?)")
            print(f"  OK {sz/1048576:.1f} MB"); ok += 1
        except Exception as e:
            print(f"  FAIL {e}"); fail += 1
            if os.path.exists(dest) and os.path.getsize(dest) < 10000:
                os.remove(dest)
    print(f"=== import done: ok={ok} skip={skip} fail={fail} ===")


if __name__ == "__main__":
    main()
