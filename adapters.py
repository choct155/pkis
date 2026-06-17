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
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

from config import *  # READWISE_TOKEN, PODCAST_INDEX_KEY, etc. (config-only deps)

logger = logging.getLogger(__name__)

# Exported so app.py can `from adapters import *` and bind these (underscore-named)
# functions as its own globals — that's what keeps the contract-test monkeypatches
# (setattr(app, "_fetch_url_metadata", ...)) landing on the names the tools resolve.
__all__ = [
    "_fetch_arxiv_metadata", "_fetch_crossref_metadata", "_search_semantic_scholar",
    "_detect_readwise_category", "_CATEGORY_TO_WIKI_TYPE", "_fetch_url_metadata",
    "_readwise_save",
    # podcast / transcript cluster (B2 split step 5)
    "_is_podcast_url", "_podcast_index_auth_headers", "_extract_youtube_id",
    "_youtube_get_transcript", "_fetch_podcast_page_metadata", "_parse_vtt", "_parse_srt",
    "_fetch_transcript_url", "_podcast_index_search_episode", "_podcast_index_get_transcript",
    "_apple_podcasts_get_transcript", "_listen_notes_get_metadata", "_podchaser_get_metadata",
    "_segments_to_markdown", "_segments_to_html",
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

# ── Podcast / transcript adapters (B2 split step 5) ──────────────────

def _is_podcast_url(url: str) -> bool:
    """True when URL points to a known podcast platform episode or show."""
    u = url.lower()
    return any(p in u for p in _PODCAST_URL_PATTERNS)


def _podcast_index_auth_headers() -> dict:
    """Generate Podcast Index API authentication headers (HMAC-SHA1)."""
    if not PODCAST_INDEX_KEY or not PODCAST_INDEX_SECRET:
        return {}
    import hashlib, time
    ts        = str(int(time.time()))
    auth_hash = hashlib.sha1(
        (PODCAST_INDEX_KEY + PODCAST_INDEX_SECRET + ts).encode("utf-8")
    ).hexdigest()
    return {
        "User-Agent":    "PKIS/1.0 (+https://pkis.dev)",
        "X-Auth-Key":    PODCAST_INDEX_KEY,
        "X-Auth-Date":   ts,
        "Authorization": auth_hash,
    }


def _extract_youtube_id(url: str) -> str:
    """Extract YouTube video ID from any YouTube URL format."""
    for pattern in (
        r'youtu\.be/([^?&/]+)',
        r'youtube\.com/watch\?.*v=([^&]+)',
        r'youtube\.com/embed/([^?&/]+)',
        r'youtube\.com/v/([^?&/]+)',
    ):
        m = re.search(pattern, url)
        if m:
            return m.group(1)
    return ""


def _youtube_get_transcript(url: str) -> list:
    """
    Fetch YouTube transcript via youtube-transcript-api.
    Returns [{start, text}] or [].
    Install: pip install youtube-transcript-api
    """
    video_id = _extract_youtube_id(url)
    if not video_id:
        return []
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        segs = YouTubeTranscriptApi.get_transcript(video_id)
        return [{"start": s.get("start", 0), "text": s.get("text", "")} for s in segs]
    except ImportError:
        logger.warning("youtube-transcript-api not installed; run: pip install youtube-transcript-api")
        return []
    except Exception as e:
        logger.warning(f"YouTube transcript fetch failed ({video_id}): {e}")
        return []


def _fetch_podcast_page_metadata(url: str) -> dict:
    """
    Extract basic metadata from a podcast episode page via Open Graph tags.
    Returns {title, show, description}.
    """
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (compatible; PKIS/1.0)"
        })
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read(60_000).decode("utf-8", errors="replace")
    except Exception as e:
        logger.warning(f"Could not fetch podcast page {url}: {e}")
        return {}

    def og(prop):
        m = re.search(
            rf'<meta[^>]+property=["\']og:{prop}["\'][^>]+content=["\']([^"\'<]+)',
            html, re.I)
        if not m:
            m = re.search(
                rf'<meta[^>]+content=["\']([^"\'<]+)["\'][^>]+property=["\']og:{prop}["\']',
                html, re.I)
        return m.group(1).strip() if m else ""

    raw_title   = og("title") or ""
    description = og("description") or ""

    # Normalise: "Episode Title | Show Name" / "Episode · Show" etc.
    title, show = raw_title, ""
    for sep in (" | ", " · ", " — ", " - "):
        if sep in raw_title:
            parts = raw_title.split(sep, 1)
            title = parts[0].strip()
            show  = parts[1].strip()
            # Drop trailing platform name: "| Spotify", "| Podcast on Spotify"
            show = re.sub(
                r'\s*[\|·\-—]\s*(Spotify|Apple Podcasts|Podcasts?.*)?$',
                '', show, flags=re.I
            ).strip()
            break

    return {"title": title, "show": show, "description": description}


def _parse_vtt(vtt: str) -> list:
    """Parse WebVTT into [{start, text}] segments."""
    segments, i = [], 0
    lines = vtt.split("\n")
    while i < len(lines):
        m = re.match(r'(\d{1,2}:\d{2}:\d{2}[.,]\d{3})\s*-->', lines[i].strip())
        if m:
            t     = m.group(1).replace(",", ".").split(":")
            h, mi, s = int(t[0]), int(t[1]), float(t[2])
            start = h * 3600 + mi * 60 + s
            i += 1
            texts = []
            while i < len(lines) and lines[i].strip():
                texts.append(lines[i].strip())
                i += 1
            text = re.sub(r'<[^>]+>', '', " ".join(texts)).strip()
            if text:
                segments.append({"start": start, "text": text})
        i += 1
    return segments


def _parse_srt(srt: str) -> list:
    """Parse SRT subtitle format into [{start, text}] segments."""
    segments = []
    for block in re.split(r'\n\n+', srt.strip()):
        lines = block.strip().split("\n")
        if len(lines) < 3:
            continue
        m = re.match(r'(\d{2}:\d{2}:\d{2}[,.]\d{3})\s*-->', lines[1])
        if not m:
            continue
        t     = m.group(1).replace(",", ".").split(":")
        h, mi, s = int(t[0]), int(t[1]), float(t[2])
        start = h * 3600 + mi * 60 + s
        text  = " ".join(lines[2:]).strip()
        if text:
            segments.append({"start": start, "text": text})
    return segments


def _fetch_transcript_url(url: str) -> list:
    """
    Fetch a transcript from a URL and parse it.
    Handles JSON (Podcast Index / Whisper), WebVTT, SRT, and plain text.
    Returns [{start, text}] or [].
    """
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "PKIS/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read().decode("utf-8", errors="replace")
    except Exception as e:
        logger.warning(f"Transcript URL fetch failed ({url}): {e}")
        return []

    low      = url.lower()
    stripped = raw.lstrip()

    # JSON
    if low.endswith(".json") or stripped.startswith("{") or stripped.startswith("["):
        try:
            data = json.loads(raw)
            if isinstance(data, list):
                return [{"start": s.get("start", 0), "text": s.get("text", "")} for s in data]
            if "segments" in data:
                return [{"start": s.get("start", 0), "text": s.get("text", "")}
                        for s in data["segments"]]
            if "transcript" in data:
                return [{"start": t.get("startTime", t.get("start", 0)),
                         "text":  t.get("body",      t.get("text", ""))}
                        for t in data["transcript"]]
        except json.JSONDecodeError:
            pass

    # VTT
    if low.endswith(".vtt") or stripped.startswith("WEBVTT"):
        return _parse_vtt(raw)

    # SRT
    if low.endswith(".srt") or re.match(r'^\d+\s*\n\d{2}:\d{2}', stripped):
        return _parse_srt(raw)

    # Plain text fallback — one line per segment
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    return [{"start": float(i * 5), "text": ln} for i, ln in enumerate(lines)]


def _podcast_index_search_episode(show_name: str = "", episode_title: str = "",
                                   feed_url: str = "") -> dict:
    """
    Search Podcast Index for the best-matching episode.
    Returns episode data dict (with 'transcripts' list) or {}.
    """
    if not PODCAST_INDEX_KEY:
        return {}
    headers = _podcast_index_auth_headers()

    # Resolve feed URL from show name if needed
    if not feed_url and show_name:
        try:
            q   = urllib.parse.quote(show_name)
            req = urllib.request.Request(
                f"https://api.podcastindex.org/api/1.0/search/byterm?q={q}&max=5",
                headers=headers,
            )
            with urllib.request.urlopen(req, timeout=10) as r:
                feeds = json.loads(r.read()).get("feeds", [])
            if not feeds:
                return {}
            feed_url = feeds[0].get("url", "")
        except Exception as e:
            logger.warning(f"Podcast Index show search failed: {e}")
            return {}

    if not feed_url:
        return {}

    try:
        enc = urllib.parse.quote(feed_url, safe="")
        req = urllib.request.Request(
            f"https://api.podcastindex.org/api/1.0/episodes/byfeedurl?url={enc}&max=50",
            headers=headers,
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            items = json.loads(r.read()).get("items", [])
        if not items:
            return {}
    except Exception as e:
        logger.warning(f"Podcast Index episode fetch failed: {e}")
        return {}

    if episode_title:
        q_words = set(episode_title.lower().split())
        scored = sorted(
            [(len(q_words & set((it.get("title") or "").lower().split())) / max(len(q_words), 1), it)
             for it in items],
            reverse=True,
        )
        if scored and scored[0][0] > 0.25:
            return scored[0][1]

    return items[0]  # most recent if no title match


def _podcast_index_get_transcript(show_name: str = "", episode_title: str = "",
                                   feed_url: str = "") -> tuple:
    """
    Returns (segments, episode_meta_dict).
    segments: [{start, text}] if transcript found, else [].
    """
    episode = _podcast_index_search_episode(show_name, episode_title, feed_url)
    if not episode:
        return [], {}

    meta = {
        "title":          episode.get("title", ""),
        "show":           episode.get("feedTitle", show_name),
        "description":    (episode.get("description") or "")[:600],
        "pub_date":       episode.get("datePublishedPretty", ""),
        "feed_url":       episode.get("feedUrl", feed_url),
        "episode_url":    episode.get("link", ""),
        "transcript_url": "",
    }

    t_url = ""
    for t in (episode.get("transcripts") or []):
        t_type = (t.get("type") or "").lower()
        t_u    = t.get("url") or ""
        if not t_u:
            continue
        if any(x in t_type for x in ("json", "vtt", "srt", "txt", "plain")):
            t_url = t_u
            break
        if not t_url:
            t_url = t_u

    meta["transcript_url"] = t_url
    if not t_url:
        return [], meta

    return _fetch_transcript_url(t_url), meta


def _apple_podcasts_get_transcript(show_name: str = "",
                                    episode_title: str = "") -> tuple:
    """
    Search iTunes for a show's RSS feed, parse it for podcast:transcript elements.
    Returns (segments, meta_dict).
    """
    if not show_name:
        return [], {}
    try:
        q   = urllib.parse.quote(show_name)
        req = urllib.request.Request(
            f"https://itunes.apple.com/search?term={q}&entity=podcast&limit=3",
            headers={"User-Agent": "PKIS/1.0"},
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            results = json.loads(r.read()).get("results", [])
        if not results:
            return [], {}
        feed_url = results[0].get("feedUrl", "")
        if not feed_url:
            return [], {}
    except Exception as e:
        logger.warning(f"iTunes search failed: {e}")
        return [], {}

    try:
        req = urllib.request.Request(feed_url, headers={"User-Agent": "PKIS/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            rss_data = r.read()
        root    = ET.fromstring(rss_data)
        channel = root.find("channel")
        items   = channel.findall("item") if channel is not None else []
    except Exception as e:
        logger.warning(f"RSS feed parse failed ({feed_url}): {e}")
        return [], {}

    best_item, best_score = None, 0.0
    if episode_title:
        q_words = set(episode_title.lower().split())
        for item in items:
            t_el = item.find("title")
            if t_el is None or not t_el.text:
                continue
            overlap = len(q_words & set(t_el.text.lower().split())) / max(len(q_words), 1)
            if overlap > best_score:
                best_score, best_item = overlap, item
    if not best_item and items:
        best_item = items[0]
    if not best_item or (episode_title and best_score < 0.2):
        return [], {}

    t_el = best_item.find(f"{{{_PI_NS}}}transcript")
    if t_el is None:
        return [], {}
    t_url = t_el.get("url", "")
    if not t_url:
        return [], {}

    title_el = best_item.find("title")
    date_el  = best_item.find("pubDate")
    meta = {
        "title":          title_el.text.strip() if title_el is not None and title_el.text else episode_title,
        "show":           show_name,
        "feed_url":       feed_url,
        "pub_date":       date_el.text.strip() if date_el is not None and date_el.text else "",
        "transcript_url": t_url,
    }
    return _fetch_transcript_url(t_url), meta


def _listen_notes_get_metadata(show_name: str = "", episode_title: str = "") -> dict:
    """Fetch episode metadata from Listen Notes API (fallback when no transcript found)."""
    if not LISTEN_NOTES_KEY:
        return {}
    try:
        q   = urllib.parse.quote(f"{episode_title} {show_name}".strip())
        req = urllib.request.Request(
            f"https://listen-api.listennotes.com/api/v2/search?q={q}&type=episode&offset=0&len_min=0",
            headers={"X-ListenAPI-Key": LISTEN_NOTES_KEY, "User-Agent": "PKIS/1.0"},
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            results = json.loads(r.read()).get("results", [])
        if not results:
            return {}
        ep = results[0]
        return {
            "title":       ep.get("title_original", ""),
            "show":        (ep.get("podcast") or {}).get("title_original", show_name),
            "description": ep.get("description_original", ""),
            "pub_date":    str(ep.get("pub_date_ms", "")),
        }
    except Exception as e:
        logger.warning(f"Listen Notes metadata fetch failed: {e}")
        return {}


def _podchaser_get_metadata(show_name: str = "", episode_title: str = "") -> dict:
    """Fetch episode metadata from Podchaser GraphQL API (fallback)."""
    if not PODCHASER_KEY:
        return {}
    gql = (
        "query SearchEpisodes($q: String!) {"
        "  searchEpisodes(searchTerm: $q, first: 3) {"
        "    edges { node { title description airDate podcast { title } } }"
        "  }"
        "}"
    )
    try:
        payload = json.dumps({
            "query":     gql,
            "variables": {"q": f"{episode_title} {show_name}".strip()},
        }).encode()
        req = urllib.request.Request(
            "https://api.podchaser.com/graphql",
            data=payload,
            headers={
                "Authorization": f"Bearer {PODCHASER_KEY}",
                "Content-Type":  "application/json",
                "User-Agent":    "PKIS/1.0",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            edges = (json.loads(r.read())
                     .get("data", {})
                     .get("searchEpisodes", {})
                     .get("edges", []))
        if not edges:
            return {}
        node = edges[0]["node"]
        return {
            "title":       node.get("title", ""),
            "show":        (node.get("podcast") or {}).get("title", show_name),
            "description": node.get("description", ""),
            "pub_date":    node.get("airDate", ""),
        }
    except Exception as e:
        logger.warning(f"Podchaser metadata fetch failed: {e}")
        return {}


def _segments_to_markdown(segments: list, title: str = "", show: str = "",
                           source: str = "", episode_url: str = "") -> str:
    """Convert [{start, text}] transcript segments to markdown."""
    lines = [f"# Transcript: {title}"]
    if show:        lines.append(f"**Show:** {show}")
    if source:      lines.append(f"**Source:** {source}")
    if episode_url: lines.append(f"**Episode:** {episode_url}")
    lines.append(f"**Retrieved:** {datetime.now(timezone.utc).strftime('%Y-%m-%d')}")
    lines += ["\n---\n"]
    for seg in segments:
        if isinstance(seg, dict):
            start = seg.get("start", 0)
            text  = (seg.get("text") or "").strip()
            m_, s_ = int(start // 60), int(start % 60)
            if text:
                lines.append(f"[{m_:02d}:{s_:02d}] {text}")
        elif str(seg).strip():
            lines.append(str(seg))
    return "\n".join(lines)


def _segments_to_html(segments: list, title: str = "") -> str:
    """Convert [{start, text}] transcript segments to HTML for Readwise Reader."""
    parts = [f"<h1>{title}</h1>"] if title else []
    for seg in segments:
        text = ((seg.get("text") if isinstance(seg, dict) else str(seg)) or "").strip()
        if text:
            parts.append(f"<p>{text}</p>")
    return "\n".join(parts)


