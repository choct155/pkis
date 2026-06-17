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
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)


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
