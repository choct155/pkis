#!/usr/bin/env python3
"""Create book + chapter source stubs and a chapter->page split map from a config.

Usage: book_setup.py <config.json>
config schema:
{
  "slug": "bishop-prml", "title": "...", "authors": "...", "isbn": "...",
  "year": 2006, "domain": ["statistical-learning"], "tags": ["...","textbook"],
  "source_url": "https://...", "alias": ["PRML"],
  "chapters": [["ch01","Introduction",21,86], ["ch02","Probability Distributions",87,156], ...]
}
Writes wiki/sources/<slug>.md (+ ## Chapters), wiki/sources/<slug>-chNN.md stubs,
and /home/pkis/proposals/<slug>_map.json  {"<slug>-chNN":[start,end], ...}
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_labels import title_prefix, abbrev_for  # noqa: E402

SRC = "/home/pkis/pkis-wiki/wiki/sources"
MAPDIR = "/home/pkis/proposals"
cfg = json.load(open(sys.argv[1]))
slug = cfg["slug"]
dom = "\n".join(f"- {d}" for d in cfg.get("domain", []))
tags = "\n".join(f"- {t}" for t in cfg.get("tags", []))
aliases = "\n".join(f"- {a}" for a in cfg.get("alias", [])) or "[]"
alias_block = ("aliases:\n" + aliases) if cfg.get("alias") else "aliases: []"

# Visible [ABBREV Author] tag — see book_labels. Config may supply "abbrev";
# otherwise it falls back to the ABBREV registry (empty -> author-only tag).
ab = abbrev_for(slug, cfg.get("abbrev"))
prefix = title_prefix(slug, cfg["authors"], ab)
abbrev_line = f"abbrev: {json.dumps(ab, ensure_ascii=False)}\n" if ab else ""


def ch_label(chnn):
    return chnn.replace("ch", "Ch. ").replace("app", "App. ") if chnn.startswith(("ch", "app")) else chnn

book = f"""---
{abbrev_line}{alias_block}
authors: {cfg['authors']}
coverage: 0
domain:
{dom}
id: pkis:source:{slug}
isbn: '{cfg.get('isbn','')}'
maturity: evolving
source_url: {cfg.get('source_url','')}
status: unread
tags:
{tags}
title: {json.dumps(prefix + cfg['title'], ensure_ascii=False)}
toc_source: document
type: book
understanding: 0
year: {cfg.get('year','')}
---

## Summary
[Book node — {cfg['title']} ({cfg['authors']}). Chapter stubs below; deepen per chapter from the reader extraction.]

## Chapters
"""
for chnn, title, *_ in cfg["chapters"]:
    book += f"- [[{slug}-{chnn}]] — {ch_label(chnn)} — {title}\n"
os.makedirs(SRC, exist_ok=True)
open(os.path.join(SRC, f"{slug}.md"), "w").write(book)

def chapter_md(chnn, title):
    label = ch_label(chnn)
    return f"""---
{abbrev_line}aliases: []
authors: {cfg['authors']}
coverage: 0
domain:
{dom}
id: pkis:source:{slug}-{chnn}
maturity: stub
parent_book: pkis:source:{slug}
status: unread
tags:
{tags}
title: {json.dumps(prefix + f'{label} — {title}', ensure_ascii=False)}
type: chapter
understanding: 0
year: {cfg.get('year','')}
---

## Summary
[Chapter stub — {cfg['title']} {chnn}: {title}. To be deepened from the chapter reader extraction.]

## Reading Path
- Parent: [[{slug}]]
"""

for chnn, title, *_ in cfg["chapters"]:
    open(os.path.join(SRC, f"{slug}-{chnn}.md"), "w").write(chapter_md(chnn, title))

mp = {f"{slug}-{chnn}": [int(s), int(e)] for chnn, title, s, e in cfg["chapters"]}
os.makedirs(MAPDIR, exist_ok=True)
json.dump(mp, open(os.path.join(MAPDIR, f"{slug}_map.json"), "w"), indent=1)
print(f"{slug}: wrote book + {len(cfg['chapters'])} chapter stubs; map {len(mp)} entries")
