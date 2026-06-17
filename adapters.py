"""
PKIS external-API adapters (B2 split).

Network fetchers for third-party bibliographic / metadata services, carved out of
app.py. Pure: args in, dict/list out; they touch only stdlib + their own logger
(no app state, no config needed). Re-imported by app.py. More adapters (URL
metadata, Readwise, podcast/transcript lookups) move here in later increments;
several of those are monkeypatched by the contract tests, so app.py keeps
re-importing them by name and callers resolve them as app-module globals.
"""

import json
import logging
import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

from config import *  # READWISE_TOKEN, PODCAST_INDEX_KEY, etc. (config-only deps)

logger = logging.getLogger(__name__)

# Exported so app.py can `from adapters import *` and bind these (underscore-named)
# functions as its own globals — that's what keeps the contract-test monkeypatches
# (setattr(app, "_fetch_url_metadata", ...)) landing on the names the tools resolve.
__all__ = [
    "_fetch_arxiv_metadata", "_fetch_crossref_metadata", "_search_semantic_scholar",
    "_detect_readwise_category", "_CATEGORY_TO_WIKI_TYPE", "_fetch_url_metadata",
    "_readwise_save",
]


def _fetch_arxiv_metadata(arxiv_id: str) -> dict:
    """Fetch paper metadata from arXiv Atom API."""
    url = f"https://export.arxiv.org/api/query?id_list={arxiv_id}&max_results=1"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "PKIS-Wiki/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            xml_data = resp.read()
        root = ET.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entry = root.find("atom:entry", ns)
        if entry is None:
            return {}
        title = entry.findtext("atom:title", namespaces=ns) or ""
        abstract = entry.findtext("atom:summary", namespaces=ns) or ""
        published = entry.findtext("atom:published", namespaces=ns) or ""
        year = int(published[:4]) if published and len(published) >= 4 else None
        authors = [
            a.findtext("atom:name", namespaces=ns) or ""
            for a in entry.findall("atom:author", ns)
        ]
        return {
            "title": title.strip().replace("\n", " "),
            "authors": ", ".join(authors),
            "year": year,
            "abstract": abstract.strip().replace("\n", " "),
            "venue": "arXiv",
            "source_type": "paper",
        }
    except Exception as e:
        logger.error(f"arXiv fetch failed for {arxiv_id}: {e}")
        return {}


def _fetch_crossref_metadata(doi: str) -> dict:
    """Fetch paper metadata from CrossRef API."""
    encoded_doi = urllib.parse.quote(doi, safe="")
    url = f"https://api.crossref.org/works/{encoded_doi}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "PKIS-Wiki/1.0 (mailto:pkis@pkis.dev)"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        msg = data.get("message", {})
        title = (msg.get("title") or [""])[0]
        authors = ", ".join(
            f"{a.get('given', '')} {a.get('family', '')}".strip()
            for a in msg.get("author", [])
        )
        year = None
        for date_field in ("published-print", "published-online", "created"):
            if date_field in msg:
                parts = msg[date_field].get("date-parts", [[]])
                if parts and parts[0]:
                    year = parts[0][0]
                    break
        abstract = msg.get("abstract", "")
        venue = (msg.get("container-title") or [""])[0]
        return {
            "title": title,
            "authors": authors,
            "year": year,
            "abstract": abstract,
            "venue": venue,
            "source_type": "paper",
        }
    except Exception as e:
        logger.error(f"CrossRef fetch failed for {doi}: {e}")
        return {}


def _search_semantic_scholar(query: str, limit: int = 5) -> list:
    """Search Semantic Scholar for candidate papers by title/keywords.

    Used to suggest canonical references for sourceless node stubs. Returns a
    list of {title, year, url, doi, arxiv} dicts ready to feed create_source_stub.
    """
    q = urllib.parse.quote(query)
    url = (
        "https://api.semanticscholar.org/graph/v1/paper/search"
        f"?query={q}&limit={limit}&fields=title,year,externalIds,url"
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "PKIS-Wiki/1.0 (mailto:pkis@pkis.dev)"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        out = []
        for p in data.get("data", []):
            ext = p.get("externalIds") or {}
            ref_url = p.get("url") or ""
            if ext.get("ArXiv"):
                ref_url = f"https://arxiv.org/abs/{ext['ArXiv']}"
            elif ext.get("DOI"):
                ref_url = f"https://doi.org/{ext['DOI']}"
            out.append({
                "title": p.get("title", ""),
                "year": p.get("year"),
                "url": ref_url,
                "doi": ext.get("DOI", ""),
                "arxiv": ext.get("ArXiv", ""),
            })
        return out
    except Exception as e:
        logger.error(f"Semantic Scholar search failed for '{query[:40]}': {e}")
        return []


# ── Readwise + URL-metadata adapters (B2 split step 4) ──────────────────────

def _detect_readwise_category(url: str) -> str:
    """Infer the best Readwise category from URL patterns."""
    u = url.lower()
    if any(d in u for d in ("youtube.com/watch", "youtu.be/", "vimeo.com/")):
        return "video"
    if any(d in u for d in ("twitter.com/", "x.com/")):
        return "tweet"
    if any(d in u for d in ("substack.com", "mailchimp.com", "beehiiv.com")):
        return "email"
    return "article"


# Maps Readwise category → PKIS wiki source type
_CATEGORY_TO_WIKI_TYPE = {
    "article": "article",
    "video":   "talk",
    "tweet":   "article",
    "email":   "article",
    "pdf":     "paper",
    "epub":    "book",
}


def _fetch_url_metadata(url: str) -> dict:
    """
    Best-effort title/author extraction from a URL.
    Tries YouTube oEmbed first; falls back to HTML <title> and Open Graph tags.
    Returns dict with keys: title, author, source_type (maps to wiki type).
    """
    # YouTube oEmbed
    if "youtube.com/watch" in url or "youtu.be/" in url:
        try:
            oembed = (f"https://www.youtube.com/oembed"
                      f"?url={urllib.parse.quote(url, safe='')}&format=json")
            req = urllib.request.Request(oembed, headers={"User-Agent": "PKIS/1.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                data = json.loads(r.read())
            return {
                "title":       data.get("title", ""),
                "author":      data.get("author_name", ""),
                "source_type": "talk",
            }
        except Exception:
            pass

    # Generic HTML meta / Open Graph
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "PKIS/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read(30_000).decode("utf-8", errors="replace")

        title = ""
        author = ""

        # OG title → <title> fallback
        m = re.search(
            r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\'<]+)',
            html, re.I)
        if m:
            title = m.group(1).strip()
        if not title:
            m = re.search(r'<title[^>]*>([^<]+)</title>', html, re.I)
            if m:
                title = re.sub(r'\s+', ' ', m.group(1)).strip()

        # meta author → OG site_name fallback
        m = re.search(
            r'<meta[^>]+name=["\']author["\'][^>]+content=["\']([^"\'<]+)',
            html, re.I)
        if m:
            author = m.group(1).strip()
        if not author:
            m = re.search(
                r'<meta[^>]+property=["\']og:site_name["\'][^>]+content=["\']([^"\'<]+)',
                html, re.I)
            if m:
                author = m.group(1).strip()

        return {"title": title, "author": author, "source_type": "article"}
    except Exception:
        pass

    return {"title": "", "author": "", "source_type": "article"}


def _readwise_save(doc_url: str, title: str = "", author: str = "",
                   slug: str = "", abstract: str = "",
                   year: int = None, arxiv_id: str = "",
                   category: str = "", html: str = "") -> dict:
    """
    Push a document to Readwise Reader. Returns Readwise response dict.

    Priority order for push_url / category:
      1. arxiv_id provided → ar5iv HTML URL, category: article
      2. category explicitly provided → doc_url pushed as-is with that category
      3. fallback → doc_url, category: pdf

    Full metadata (title, author, summary, published_date) is sent in all cases.
    """
    if not READWISE_TOKEN:
        return {"error": "READWISE_TOKEN not configured"}

    tags = [f"pkis:source:{slug}"] if slug else []

    if arxiv_id:
        push_url      = f"https://ar5iv.org/abs/{arxiv_id}"
        category      = "article"
        notes         = f"VPS copy: {doc_url}" if doc_url else ""
    elif category:
        push_url      = doc_url
        notes         = ""
    else:
        push_url      = doc_url
        category      = "pdf"
        notes         = ""

    payload: dict = {
        "url":      push_url,
        "location": "new",   # "new" = Inbox; "later" = Later shelf (not visible in inbox)
        "category": category,
    }
    if title:    payload["title"]          = title
    if author:   payload["author"]         = author
    if tags:     payload["tags"]           = tags
    if abstract: payload["summary"]        = abstract[:600]
    if year:     payload["published_date"] = f"{year}-01-01T00:00:00+00:00"
    if notes:    payload["notes"]          = notes
    if html:
        payload["html"]             = html[:50_000]  # Readwise cap ~50 KB
        payload["should_clean_html"] = False

    try:
        data = json.dumps(payload).encode()
        req = urllib.request.Request(
            "https://readwise.io/api/v3/save/",
            data=data,
            headers={
                "Authorization": f"Token {READWISE_TOKEN}",
                "Content-Type":  "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except Exception as e:
        logger.error(f"Readwise save failed: {e}")
        return {"error": str(e)}
