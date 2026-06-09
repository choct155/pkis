"""
PKIS Wiki MCP Server
====================
Implements the full PKIS MCP API as defined in the system design.
Serves the pkis-wiki repository as a knowledge service accessible
from Claude.ai, Claude Code, and any MCP-compatible client.

Deployed to: https://pkis.dev
Wiki source: /home/pkis/pkis-wiki/wiki/
"""

import os
import re
import json
import glob
import uuid
import hashlib
import logging
import subprocess
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import yaml
import frontmatter
import networkx as nx
import numpy as np
from rank_bm25 import BM25Okapi
from functools import wraps
from flask import Flask, request, jsonify, Response, send_from_directory
from anthropic import Anthropic

# ============================================================
# Configuration
# ============================================================

WIKI_DIR = Path(os.environ.get("WIKI_DIR", "/home/pkis/pkis-wiki/wiki"))
RAW_DIR = Path(os.environ.get("RAW_DIR", "/home/pkis/pkis-wiki/raw"))
REPO_DIR = Path(os.environ.get("REPO_DIR", "/home/pkis/pkis-wiki"))
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

KNOWLEDGE_DIRS = [
    "concepts", "techniques", "results",
    "frameworks", "problems", "principles", "sources",
    "hypotheses", "clusters", "assets", "bridge-notes"
]

FOLDER_TO_TYPE = {
    "concepts":    "concept",
    "techniques":  "technique",
    "results":     "result",
    "frameworks":  "framework",
    "problems":    "problem",
    "principles":  "principle",
    "sources":     "source",
    "hypotheses":  "hypothesis",
    "clusters":    "research-cluster",
    "assets":      "asset",
    "bridge-notes": "bridge-note",
}

TYPE_TO_FOLDER = {v: k for k, v in FOLDER_TO_TYPE.items()}

# Component names per node type — used to compute anatomy_assessed / anatomy_total
COMPONENT_SCORES_BY_TYPE = {
    "concept":   ["definition", "prerequisites", "boundary", "scope", "application", "formal_statement", "dependents", "transfer"],
    "technique": ["operational_mechanism", "principled_mechanism", "conditions", "implementation", "diagnostics", "alternatives", "failure_modes"],
    "framework": ["structure", "purpose", "primitives", "scope", "application", "limits"],
    "result":    ["statement", "proof_sketch", "conditions", "implications", "limitations"],
    "problem":   ["formulation", "why_hard", "solution_landscape", "instances"],
    "principle": ["statement", "justification", "implications", "violations"],
}

STAGING_DIR = Path(os.environ.get("WIKI_DIR", "/home/pkis/pkis-wiki/wiki")) / "staging"

# Edge type weights for structural ranking (prerequisite-of highest)
EDGE_WEIGHTS = {
    "prerequisite-of": 1.0,
    "uses": 0.8,
    "specializes": 0.6,
    "generalizes": 0.6,
    "extends": 0.5,
    "applies": 0.5,
    "instantiates": 0.4,
    "contrasts-with": 0.2,
    "analogous-to": 0.3,  # structural analogy across domains (same structure, different mechanism)
}

# Trusted client token — set via env var in production
TRUSTED_TOKEN = os.environ.get("PKIS_TRUSTED_TOKEN", "")

# Write endpoint key — separate from read token; required for write operations
WRITE_KEY = os.environ.get("PKIS_MCP_WRITE_KEY", "")

# ============================================================
# OAuth (MCP Resource Server) — DORMANT until PKIS_OAUTH_ISSUER is set.
# With no issuer configured, OAUTH_ENABLED is False and every code path below
# is a no-op: auth falls back exactly to the static WRITE_KEY/TRUSTED_TOKEN
# behavior. To activate (after WorkOS/Stytch setup): set PKIS_OAUTH_ISSUER,
# PKIS_OAUTH_JWKS_URL, PKIS_OAUTH_AUDIENCE (=https://pkis.dev/mcp), PKIS_ROLES_PATH,
# `pip install "PyJWT[crypto]"`, restart. See OAUTH_PLAN.md. Static key stays valid
# (machine-to-machine escape hatch for desktop Claude Code).
# ============================================================
OAUTH_ISSUER   = os.environ.get("PKIS_OAUTH_ISSUER", "").rstrip("/")
OAUTH_AUDIENCE = os.environ.get("PKIS_OAUTH_AUDIENCE", "https://pkis.dev/mcp")
OAUTH_JWKS_URL = os.environ.get("PKIS_OAUTH_JWKS_URL", "") or (
    OAUTH_ISSUER + "/.well-known/jwks.json" if OAUTH_ISSUER else "")
OAUTH_ALGS     = [a.strip() for a in os.environ.get("PKIS_OAUTH_ALGS", "RS256").split(",") if a.strip()]
ROLES_PATH     = os.environ.get("PKIS_ROLES_PATH", "")
PUBLIC_BASE    = os.environ.get("PKIS_PUBLIC_BASE", "https://pkis.dev").rstrip("/")
OAUTH_ENABLED  = bool(OAUTH_ISSUER and OAUTH_JWKS_URL)
_jwk_client = None
_roles_cache = {"mtime": 0.0, "data": {}}


class OAuthChallenge(PermissionError):
    """Unauthorized write while OAuth is enabled and caller is anonymous —
    triggers a 401 + WWW-Authenticate so the connector starts the OAuth flow."""

# Document store + Readwise integration
DOCS_DIR          = Path(os.environ.get("DOCS_DIR", "/home/pkis/docs"))
DOCS_BASE_URL     = os.environ.get("DOCS_BASE_URL", "https://pkis.dev/docs")
READWISE_TOKEN    = os.environ.get("READWISE_TOKEN", "")
READWISE_WEBHOOK_SECRET = os.environ.get("READWISE_WEBHOOK_SECRET", "")
DOCS_USERNAME     = os.environ.get("DOCS_USERNAME", "")
DOCS_PASSWORD     = os.environ.get("DOCS_PASSWORD", "")

# Podcast transcript lookup APIs
PODCAST_INDEX_KEY    = os.environ.get("PODCAST_INDEX_KEY", "")
PODCAST_INDEX_SECRET = os.environ.get("PODCAST_INDEX_SECRET", "")
LISTEN_NOTES_KEY     = os.environ.get("LISTEN_NOTES_KEY", "")
PODCHASER_KEY        = os.environ.get("PODCHASER_KEY", "")

# MCP JSON-RPC 2.0 Streamable HTTP transport constants
JSONRPC_VERSION = "2.0"
# Protocol versions we can speak, newest first. We negotiate: on `initialize`
# we echo back the client's requested version if we support it, otherwise our
# newest. Advertising only the legacy 2024-11-05 made claude.ai's connector fall
# back to the legacy HTTP+SSE transport, which POSTs to a session-scoped URL
# (`/mcp/<session>`) our single-endpoint route never matched → persistent 404s.
MCP_SUPPORTED_PROTOCOL_VERSIONS = ["2025-06-18", "2025-03-26", "2024-11-05"]
MCP_PROTOCOL_VERSION = MCP_SUPPORTED_PROTOCOL_VERSIONS[0]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 200 * 1024 * 1024  # 200 MB — matches nginx client_max_body_size
anthropic_client = Anthropic(api_key=ANTHROPIC_API_KEY)

# ============================================================
# In-memory caches (invalidated on git pull via /refresh)
# ============================================================

_alias_registry: dict = {}
_node_cache: dict = {}
_graph: Optional[nx.DiGraph] = None
_bm25_index = None
_bm25_corpus: list = []
_bm25_slugs: list = []

# Cross-worker cache freshness. Each gunicorn worker holds its own in-memory
# caches, so a write handled by one worker leaves the others stale (and writes
# never rebuilt the BM25 index at all) — new nodes were invisible to search until
# a restart. We use the git HEAD commit sha as a content signature: every live
# write commits, so HEAD changes; a worker rebuilds its caches lazily when its
# built generation falls behind. Result: writes are searchable everywhere with no
# restart. (Staged-only creates don't commit, so they don't trigger a rebuild.)
_cache_gen: Optional[str] = None


def _content_signature() -> str:
    """Live-content signature = git HEAD sha of REPO_DIR (changes on every
    committed write). Empty string if it can't be read — in which case we leave
    caches as-is rather than rebuild on every call."""
    try:
        head = (REPO_DIR / ".git" / "HEAD").read_text().strip()
        if head.startswith("ref:"):
            ref = head.split(" ", 1)[1].strip()
            ref_path = REPO_DIR / ".git" / ref
            if ref_path.exists():
                return ref_path.read_text().strip()
            packed = REPO_DIR / ".git" / "packed-refs"
            if packed.exists():
                for line in packed.read_text().splitlines():
                    parts = line.split()
                    if len(parts) == 2 and parts[1] == ref:
                        return parts[0]
            return ""
        return head  # detached HEAD: the line itself is the sha
    except Exception:
        return ""


def ensure_fresh():
    """Rebuild this worker's caches if live content changed since it last built
    (cross-worker invalidation via the git HEAD signature). Cheap when unchanged
    (one small file read + string compare)."""
    global _cache_gen
    sig = _content_signature()
    if sig and sig != _cache_gen:
        try:
            refresh_caches()
            _cache_gen = sig
        except Exception as e:
            logger.warning(f"ensure_fresh rebuild failed: {e}")


# ============================================================
# Core helpers
# ============================================================

def slug_from_path(path: Path) -> str:
    return path.stem


def iri_from_slug(node_type: str, slug: str) -> str:
    """Generate a stable IRI from node type and slug."""
    return f"pkis:{node_type}:{slug}"


def parse_iri(iri: str) -> tuple:
    """Parse IRI into (namespace, node_type, slug)."""
    parts = iri.split(":")
    if len(parts) >= 3:
        return parts[0], parts[1], parts[2]
    return None, None, None


def find_node_path(slug: str) -> Optional[Path]:
    """Find the file path for a slug, searching all knowledge dirs."""
    for kdir in KNOWLEDGE_DIRS:
        p = WIKI_DIR / kdir / f"{slug}.md"
        if p.exists():
            return p
    return None


def find_node_path_by_iri(iri: str) -> Optional[Path]:
    """Resolve an IRI to a file path."""
    _, node_type, slug = parse_iri(iri)
    if not slug:
        return None
    # Try the typed directory first (using TYPE_TO_FOLDER for correct mapping)
    folder = TYPE_TO_FOLDER.get(node_type, node_type) if node_type else None
    if folder:
        p = WIKI_DIR / folder / f"{slug}.md"
        if p.exists():
            return p
    # Fall back to searching all dirs
    return find_node_path(slug)


def load_node(path: Path) -> dict:
    """Load and parse a wiki node file."""
    if str(path) in _node_cache:
        return _node_cache[str(path)]

    try:
        post = frontmatter.load(str(path))
        node_type = path.parent.name
        slug = path.stem

        # Generate IRI if not in frontmatter
        iri = post.metadata.get("id") or iri_from_slug(node_type, slug)

        result = {
            "iri": iri,
            "slug": slug,
            "node_type": node_type,
            "path": str(path),
            "frontmatter": dict(post.metadata),
            "content": post.content,
            "title": post.metadata.get("title", slug),
            "domain": post.metadata.get("domain", []),
            "aliases": post.metadata.get("aliases", []),
            "coverage": post.metadata.get("coverage", 0),
            "understanding": post.metadata.get("understanding", 0),
            "confidence": post.metadata.get("confidence", 0),
            "date_updated": post.metadata.get("date_updated", ""),
        }
        _node_cache[str(path)] = result
        return result
    except Exception as e:
        logger.error(f"Error loading {path}: {e}")
        return {}


def load_all_nodes() -> list:
    """Load all wiki nodes across all knowledge directories."""
    nodes = []
    for kdir in KNOWLEDGE_DIRS:
        dir_path = WIKI_DIR / kdir
        if not dir_path.exists():
            continue
        for md_file in dir_path.glob("*.md"):
            node = load_node(md_file)
            if node:
                nodes.append(node)
    return nodes


def build_alias_registry() -> dict:
    """Build flat alias → IRI registry from all node frontmatter."""
    registry = {}
    nodes = load_all_nodes()
    for node in nodes:
        iri = node["iri"]
        # Register canonical title
        title = node.get("title", "")
        if title:
            registry[title.lower()] = iri
        # Register slug
        registry[node["slug"].lower()] = iri
        # Register all aliases
        for alias in node.get("aliases", []):
            registry[alias.lower()] = iri
    return registry


def build_graph() -> nx.DiGraph:
    """Build NetworkX graph from wiki wikilinks and typed edges."""
    G = nx.DiGraph()
    nodes = load_all_nodes()

    for node in nodes:
        G.add_node(node["iri"], **{
            "slug": node["slug"],
            "title": node["title"],
            "node_type": node["node_type"],
            "domain": node["domain"],
            "coverage": node["coverage"],
        })

    # Parse wikilinks from content to build edges
    wikilink_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
    for node in nodes:
        content = node.get("content", "")
        # Also check frontmatter for typed relationships
        fm = node.get("frontmatter", {})

        # Extract edges from typed relationship fields
        for edge_type in EDGE_WEIGHTS.keys():
            targets = fm.get(edge_type.replace("-", "_"), []) or \
                      fm.get(edge_type, [])
            if isinstance(targets, str):
                targets = [targets]
            for target in targets:
                target_slug = target.strip("[]").split("|")[0]
                target_path = find_node_path(target_slug)
                if target_path:
                    target_node = load_node(target_path)
                    if target_node:
                        G.add_edge(
                            node["iri"],
                            target_node["iri"],
                            edge_type=edge_type,
                            weight=EDGE_WEIGHTS[edge_type]
                        )

        # Extract edges from raw wikilinks
        for match in wikilink_pattern.finditer(content):
            target_slug = match.group(1).strip()
            target_path = find_node_path(target_slug)
            if target_path:
                target_node = load_node(target_path)
                if target_node and target_node["iri"] != node["iri"]:
                    if not G.has_edge(node["iri"], target_node["iri"]):
                        G.add_edge(
                            node["iri"],
                            target_node["iri"],
                            edge_type="related",
                            weight=0.3
                        )

    return G


def build_bm25_index():
    """Build BM25 keyword index over all node content."""
    global _bm25_index, _bm25_corpus, _bm25_slugs
    nodes = load_all_nodes()
    corpus = []
    slugs = []
    for node in nodes:
        text = f"{node['title']} {node.get('content', '')} {' '.join(node.get('aliases', []))}"
        tokens = text.lower().split()
        corpus.append(tokens)
        slugs.append(node["iri"])
    _bm25_index = BM25Okapi(corpus)
    _bm25_corpus = corpus
    _bm25_slugs = slugs


def refresh_caches():
    """Invalidate and rebuild all caches."""
    global _alias_registry, _node_cache, _graph, _bm25_index
    _node_cache = {}
    _alias_registry = build_alias_registry()
    _graph = build_graph()
    build_bm25_index()
    logger.info(f"Caches refreshed: {len(_alias_registry)} aliases, "
                f"{_graph.number_of_nodes()} nodes, "
                f"{_graph.number_of_edges()} edges")


def get_alias_registry() -> dict:
    global _alias_registry
    if not _alias_registry:
        _alias_registry = build_alias_registry()
    return _alias_registry


def get_graph() -> nx.DiGraph:
    global _graph
    if _graph is None:
        _graph = build_graph()
    return _graph


def structural_candidates(seed_iri: str, edge_types=None, max_hops=2) -> list:
    """Return structurally connected nodes with weighted scores."""
    G = get_graph()
    if seed_iri not in G:
        return []

    candidates = []
    visited = {seed_iri}

    def traverse(node_iri, depth):
        if depth > max_hops:
            return
        for neighbor in G.successors(node_iri):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            edge_data = G.get_edge_data(node_iri, neighbor) or {}
            etype = edge_data.get("edge_type", "related")
            if edge_types and etype not in edge_types:
                continue
            weight = EDGE_WEIGHTS.get(etype, 0.3)
            # Decay weight by depth
            effective_weight = weight * (0.7 ** (depth - 1))
            candidates.append({
                "iri": neighbor,
                "edge_type": etype,
                "weight": effective_weight,
                "hop_count": depth
            })
            traverse(neighbor, depth + 1)

    traverse(seed_iri, 1)
    return sorted(candidates, key=lambda x: x["weight"], reverse=True)


def rrf_score(rank: int, k: int = 60) -> float:
    return 1.0 / (k + rank)


def hybrid_search(query: str, domains=None, node_types=None, max_results=10) -> list:
    """Hybrid BM25 + structural search with RRF fusion."""
    global _bm25_index, _bm25_slugs

    if _bm25_index is None:
        build_bm25_index()

    # BM25 semantic ranking
    tokens = query.lower().split()
    bm25_scores = _bm25_index.get_scores(tokens)
    bm25_ranked = sorted(
        enumerate(bm25_scores),
        key=lambda x: x[1],
        reverse=True
    )[:max_results * 3]

    # Build RRF score map
    rrf_scores = {}
    for rank, (idx, score) in enumerate(bm25_ranked):
        iri = _bm25_slugs[idx]
        rrf_scores[iri] = rrf_scores.get(iri, 0) + rrf_score(rank)

    # Apply filters
    all_nodes = load_all_nodes()
    node_map = {n["iri"]: n for n in all_nodes}

    results = []
    seen = set()
    for iri, score in sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True):
        if iri in seen:
            continue
        seen.add(iri)
        node = node_map.get(iri)
        if not node:
            continue
        if domains and not any(d in node.get("domain", []) for d in domains):
            continue
        if node_types and node.get("node_type") not in node_types:
            continue
        # Anatomy assessment counts for component_scores
        # node["node_type"] is the folder name; map to singular for COMPONENT_SCORES_BY_TYPE
        node_type_key = FOLDER_TO_TYPE.get(node["node_type"], node["node_type"])
        components = COMPONENT_SCORES_BY_TYPE.get(node_type_key)
        anatomy_total = len(components) if components else 0
        anatomy_assessed = 0
        if components:
            cs = node.get("frontmatter", {}).get("component_scores") or {}
            anatomy_assessed = sum(1 for c in components if cs.get(c) is not None)

        results.append({
            "iri": iri,
            "canonical_title": node["title"],
            # singular knowledge type (folder name is plural) — keeps the viewer's
            # type filtering + colored badges consistent across search/index/frontier.
            "node_type": FOLDER_TO_TYPE.get(node["node_type"], node["node_type"]),
            "domain": node["domain"],
            "score": score,
            "excerpt": node["content"][:300] if node.get("content") else "",
            "coverage": node["coverage"],
            "understanding": node["understanding"],
            "anatomy_assessed": anatomy_assessed,
            "anatomy_total": anatomy_total,
        })
        if len(results) >= max_results:
            break

    return results


def _bearer(req) -> str:
    a = req.headers.get("Authorization", "")
    return a[7:].strip() if a.startswith("Bearer ") else ""


def _has_static_key(req) -> bool:
    tok = _bearer(req)
    return bool((WRITE_KEY and tok == WRITE_KEY) or (TRUSTED_TOKEN and tok == TRUSTED_TOKEN))


def _get_jwk_client():
    global _jwk_client
    if _jwk_client is None:
        from jwt import PyJWKClient  # lazy: app imports fine without PyJWT installed
        _jwk_client = PyJWKClient(OAUTH_JWKS_URL)
    return _jwk_client


def verify_jwt(token: str) -> dict:
    """Validate an IdP JWT (signature via cached JWKS; iss/aud/exp). Raises on failure."""
    import jwt
    signing_key = _get_jwk_client().get_signing_key_from_jwt(token)
    return jwt.decode(
        token, signing_key.key, algorithms=OAUTH_ALGS,
        audience=OAUTH_AUDIENCE, issuer=OAUTH_ISSUER,
        options={"require": ["exp", "iss", "aud"]},
    )


def _load_roles() -> dict:
    """{email: role} allowlist from PKIS_ROLES_PATH, reloaded on mtime change."""
    if not ROLES_PATH:
        return {}
    try:
        m = os.path.getmtime(ROLES_PATH)
        if m != _roles_cache["mtime"]:
            with open(ROLES_PATH) as f:
                # Keep keys verbatim: WorkOS `sub`s are case-sensitive. Email keys
                # should be stored lowercase (the email claim is lowercased at lookup).
                _roles_cache["data"] = dict(json.load(f))
            _roles_cache["mtime"] = m
    except Exception as e:  # noqa: BLE001
        logger.warning("OAuth roles load failed (%s): %s", ROLES_PATH, e)
    return _roles_cache["data"]


def _role_for_email(email: str) -> str:
    return _load_roles().get((email or "").lower(), "reader")


def oauth_identity(req):
    """Return (email, role) for a valid OAuth JWT, else None. No-op when OAuth off
    or when the bearer is the static key (handled by the static-key path)."""
    if not OAUTH_ENABLED:
        return None
    tok = _bearer(req)
    if not tok or tok == WRITE_KEY or tok == TRUSTED_TOKEN:
        return None
    try:
        claims = verify_jwt(tok)
    except Exception as e:  # noqa: BLE001
        logger.info("OAuth JWT rejected: %s", e)
        return None
    email = (claims.get("email") or "").lower()
    sub = (claims.get("sub") or "").strip()
    roles = _load_roles()
    # Map by email OR WorkOS sub (user id) — allowlist file may key on either.
    role = roles.get(email) or roles.get(sub) or "reader"
    logger.info("OAuth identity: email=%r sub=%r role=%r claim_keys=%s",
                email, sub, role, sorted(claims.keys()))
    return ((email or sub), role)


def is_trusted(req) -> bool:
    """Trusted tier: static TRUSTED_TOKEN, or an OAuth 'owner'."""
    if TRUSTED_TOKEN and _bearer(req) == TRUSTED_TOKEN:
        return True
    ident = oauth_identity(req)
    return bool(ident and ident[1] == "owner")


def is_write_authorized(req) -> bool:
    """Write tier: static WRITE_KEY, or an OAuth 'owner'/'writer'."""
    if WRITE_KEY and _bearer(req) == WRITE_KEY:
        return True
    ident = oauth_identity(req)
    return bool(ident and ident[1] in ("owner", "writer"))


def gate_error(req, tier: str) -> PermissionError:
    """Pick the right error for an unauthorized gated tool: a 401 OAuthChallenge
    when OAuth is on and the caller is anonymous (so the connector starts the
    flow), else a plain 403 PermissionError (OAuth off, or authed-but-insufficient)."""
    msg = f"Tool requires {tier} authorization"
    if OAUTH_ENABLED and not _has_static_key(req) and oauth_identity(req) is None:
        return OAuthChallenge(msg)
    return PermissionError(msg)


# ============================================================
# MCP Tool implementations
# ============================================================

def tool_resolve_concept(surface_form: str) -> dict:
    registry = get_alias_registry()
    normalized = surface_form.lower().strip()
    iri = registry.get(normalized)

    if iri:
        path = find_node_path_by_iri(iri)
        node = load_node(path) if path else {}
        return {
            "status": "found",
            "iri": iri,
            "canonical_title": node.get("title", ""),
            "confidence": 1.0,
            "aliases": node.get("aliases", [])
        }

    # Fuzzy fallback — find closest alias
    candidates = []
    for alias, candidate_iri in registry.items():
        if normalized in alias or alias in normalized:
            candidates.append({"iri": candidate_iri, "alias": alias})

    if candidates:
        return {
            "status": "ambiguous",
            "candidates": candidates[:5],
            "message": f"No exact match for '{surface_form}', found {len(candidates)} partial matches"
        }

    return {"status": "not_found", "surface_form": surface_form}


def tool_detect_concepts(text: str, threshold: float = 0.7) -> list:
    """Detect PKIS concepts in arbitrary text using BM25 + LLM judgment."""
    if _bm25_index is None:
        build_bm25_index()

    # BM25 pass to get candidates
    candidates = hybrid_search(text, max_results=10)
    if not candidates:
        return []

    # Use LLM to judge which candidates are genuinely instantiated
    candidate_descriptions = "\n".join([
        f"- {c['iri']}: {c['canonical_title']} (score: {c['score']:.3f})"
        for c in candidates
    ])

    prompt = f"""You are analyzing text to detect which PKIS knowledge concepts are instantiated in it.

Text to analyze:
{text[:2000]}

Candidate concepts (from keyword search):
{candidate_descriptions}

For each candidate, determine:
1. Is this concept genuinely present in the text (explicitly named, implicitly described, or structurally implied)?
2. What is your confidence (0.0-1.0)?
3. What type of reference is it: "explicit" (named directly), "semantic" (described without naming), or "structural" (implied by dependency)?

Return JSON array only, no other text:
[{{"iri": "...", "confidence": 0.0, "reference_type": "explicit|semantic|structural"}}]

Only include candidates with confidence >= {threshold}."""

    try:
        response = anthropic_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        result_text = response.content[0].text.strip()
        # Strip markdown fences if present
        result_text = re.sub(r'^```json\s*|\s*```$', '', result_text, flags=re.MULTILINE)
        results = json.loads(result_text)

        # Enrich with canonical titles
        all_nodes = {n["iri"]: n for n in load_all_nodes()}
        for r in results:
            node = all_nodes.get(r["iri"], {})
            r["canonical_title"] = node.get("title", r["iri"])

        return sorted(results, key=lambda x: x["confidence"], reverse=True)
    except Exception as e:
        logger.error(f"detect_concepts LLM call failed: {e}")
        # Fall back to BM25 results above threshold
        return [
            {
                "iri": c["iri"],
                "canonical_title": c["canonical_title"],
                "confidence": min(c["score"], 1.0),
                "reference_type": "semantic"
            }
            for c in candidates
            if c["score"] >= threshold
        ]


def tool_get_node(iri: str) -> dict:
    path = find_node_path_by_iri(iri)
    if not path:
        return {"error": f"Node not found: {iri}"}

    node = load_node(path)
    G = get_graph()

    # Get related nodes
    related = []
    if iri in G:
        for neighbor in list(G.successors(iri))[:10]:
            edge_data = G.get_edge_data(iri, neighbor) or {}
            neighbor_path = find_node_path_by_iri(neighbor)
            if neighbor_path:
                n = load_node(neighbor_path)
                related.append({
                    "iri": neighbor,
                    "title": n.get("title", neighbor),
                    "edge_type": edge_data.get("edge_type", "related"),
                    "direction": "outbound"
                })
        for predecessor in list(G.predecessors(iri))[:10]:
            edge_data = G.get_edge_data(predecessor, iri) or {}
            pred_path = find_node_path_by_iri(predecessor)
            if pred_path:
                n = load_node(pred_path)
                related.append({
                    "iri": predecessor,
                    "title": n.get("title", predecessor),
                    "edge_type": edge_data.get("edge_type", "related"),
                    "direction": "inbound"
                })

    # Build component_scores: return from frontmatter if present, else null-dict for known types
    # node["node_type"] is the folder name (e.g. "techniques"); map to singular for COMPONENT_SCORES_BY_TYPE
    node_type_key = FOLDER_TO_TYPE.get(node["node_type"], node["node_type"])
    fm_component_scores = node["frontmatter"].get("component_scores")
    components = COMPONENT_SCORES_BY_TYPE.get(node_type_key)
    if fm_component_scores is not None:
        component_scores = fm_component_scores
    elif components:
        component_scores = {c: None for c in components}
    else:
        component_scores = None

    return {
        "iri": iri,
        "frontmatter": node["frontmatter"],
        "content": node["content"],
        "related_nodes": related,
        "reading_path": node["frontmatter"].get("reading_path", []),
        "component_scores": component_scores,
    }


def tool_get_node_stub(iri: str) -> dict:
    path = find_node_path_by_iri(iri)
    if not path:
        return {"error": f"Node not found: {iri}"}
    node = load_node(path)
    content = node.get("content", "")
    first_line = content.split("\n")[0].strip() if content else ""
    return {
        "iri": iri,
        "canonical_title": node["title"],
        "node_type": node["node_type"],
        "domain": node["domain"],
        "coverage": node["coverage"],
        "understanding": node["understanding"],
        "confidence": node["confidence"],
        "one_line_summary": first_line[:200]
    }


def tool_search_wiki(query: str, domains=None, node_types=None, max_results=10) -> list:
    return hybrid_search(query, domains=domains, node_types=node_types, max_results=max_results)


def tool_search_wiki_index(query: str) -> list:
    """Fast keyword-only index scan, no LLM involvement."""
    if _bm25_index is None:
        build_bm25_index()
    tokens = query.lower().split()
    scores = _bm25_index.get_scores(tokens)
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:20]
    all_nodes = {n["iri"]: n for n in load_all_nodes()}
    results = []
    for idx, score in ranked:
        if score <= 0:
            continue
        iri = _bm25_slugs[idx]
        node = all_nodes.get(iri, {})
        content = node.get("content", "")
        first_line = content.split("\n")[0].strip() if content else ""
        results.append({
            "iri": iri,
            "canonical_title": node.get("title", iri),
            "domain": node.get("domain", []),
            "node_type": node.get("node_type", ""),
            "coverage": node.get("coverage", 0),
            "understanding": node.get("understanding", 0),
            "one_line_summary": first_line[:200],
            "score": score
        })
    return results


def tool_get_related(iri: str, edge_types=None, direction="both", max_hops=2) -> list:
    G = get_graph()
    if iri not in G:
        return []

    results = []
    visited = {iri}

    def traverse_out(node_iri, depth):
        if depth > max_hops:
            return
        for neighbor in G.successors(node_iri):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            edge_data = G.get_edge_data(node_iri, neighbor) or {}
            etype = edge_data.get("edge_type", "related")
            if edge_types and etype not in edge_types:
                continue
            path = find_node_path_by_iri(neighbor)
            title = load_node(path).get("title", neighbor) if path else neighbor
            results.append({
                "iri": neighbor,
                "canonical_title": title,
                "edge_type": etype,
                "direction": "outbound",
                "hop_count": depth
            })
            traverse_out(neighbor, depth + 1)

    def traverse_in(node_iri, depth):
        if depth > max_hops:
            return
        for predecessor in G.predecessors(node_iri):
            if predecessor in visited:
                continue
            visited.add(predecessor)
            edge_data = G.get_edge_data(predecessor, node_iri) or {}
            etype = edge_data.get("edge_type", "related")
            if edge_types and etype not in edge_types:
                continue
            path = find_node_path_by_iri(predecessor)
            title = load_node(path).get("title", predecessor) if path else predecessor
            results.append({
                "iri": predecessor,
                "canonical_title": title,
                "edge_type": etype,
                "direction": "inbound",
                "hop_count": depth
            })
            traverse_in(predecessor, depth + 1)

    if direction in ("both", "outbound"):
        traverse_out(iri, 1)
    if direction in ("both", "inbound"):
        traverse_in(iri, 1)

    return results


def tool_get_dependency_chain(iri: str) -> list:
    """Follow prerequisite-of edges with no hop limit."""
    G = get_graph()
    if iri not in G:
        return []

    chain = []
    visited = {iri}
    queue = [(iri, 0)]

    while queue:
        current_iri, depth = queue.pop(0)
        for neighbor in G.successors(current_iri):
            if neighbor in visited:
                continue
            edge_data = G.get_edge_data(current_iri, neighbor) or {}
            if edge_data.get("edge_type") != "prerequisite-of":
                continue
            visited.add(neighbor)
            path = find_node_path_by_iri(neighbor)
            title = load_node(path).get("title", neighbor) if path else neighbor
            chain.append({"iri": neighbor, "canonical_title": title, "depth": depth + 1})
            queue.append((neighbor, depth + 1))

    return sorted(chain, key=lambda x: x["depth"])


def tool_get_reading_queue(priority=None) -> list:
    queue_path = WIKI_DIR / "queue.md"
    if not queue_path.exists():
        return []

    content = queue_path.read_text()
    items = []
    current_priority = "normal"

    for line in content.split("\n"):
        if line.startswith("### High"):
            current_priority = "high"
        elif line.startswith("### Normal"):
            current_priority = "normal"
        elif line.startswith("- [ ]"):
            if priority and current_priority != priority.lower():
                continue
            # Parse: - [ ] [[slug]] — reason
            match = re.match(r'- \[ \] \[\[([^\]]+)\]\](?:\s*—\s*(.+))?', line)
            if match:
                slug = match.group(1)
                reason = match.group(2) or ""
                items.append({
                    "slug": slug,
                    "priority": current_priority,
                    "reason": reason.strip()
                })

    return items


def tool_add_to_queue(source_iri=None, reference=None, reason="", priority="normal") -> dict:
    queue_path = WIKI_DIR / "queue.md"
    if not queue_path.exists():
        queue_path.write_text("# Reading Queue\n\n### High\n\n### Normal\n")

    content = queue_path.read_text()

    if source_iri:
        _, _, slug = parse_iri(source_iri)
        entry = f"- [ ] [[{slug}]] — {reason}"
    else:
        entry = f"- [ ] {reference} — {reason}"

    section = "### High" if priority.lower() == "high" else "### Normal"

    if section in content:
        content = content.replace(section, f"{section}\n{entry}")
    else:
        content += f"\n{section}\n{entry}\n"

    queue_path.write_text(content)
    return {"success": True, "entry": entry, "priority": priority}


# How strongly proximity to an active research-cluster frontier boosts reading priority.
# A node directly used by a frontier hypothesis (1 hop, proximity 0.5) gains ~1.0 — about
# two extra inbound refs' worth; a frontier hypothesis itself (proximity 1.0) gains the full weight.
# This is the BUILT-IN default; the live default can be overridden per-call (get_concept_frontier
# cluster_proximity_weight=...) or globally via set_priority_config (persisted to a config file
# so it survives restarts and is shared across gunicorn workers, which don't share module globals).
DEFAULT_CLUSTER_PROXIMITY_WEIGHT = 2.0
PRIORITY_CONFIG_PATH = Path(os.environ.get("PRIORITY_CONFIG", str(REPO_DIR / "priority_config.json")))


def _priority_config() -> dict:
    """Read the persisted priority config (worker-safe: read per call rather than cached in a
    module global, since gunicorn workers don't share memory). Empty dict if unset/unreadable."""
    try:
        if PRIORITY_CONFIG_PATH.exists():
            import json as _json
            return _json.loads(PRIORITY_CONFIG_PATH.read_text()) or {}
    except Exception as ex:
        logger.warning(f"priority config read failed: {ex}")
    return {}


def _effective_proximity_weight(override=None):
    """Resolve the cluster-proximity weight to use and report where it came from.
    Returns (weight: float, source: str)."""
    if override is not None:
        return float(override), "call-override"
    cfg = _priority_config()
    w = cfg.get("cluster_proximity_weight")
    if isinstance(w, (int, float)):
        return float(w), "config-default"
    return DEFAULT_CLUSTER_PROXIMITY_WEIGHT, "built-in-default"


def _active_frontier_anchors(nodes) -> set:
    """IRIs of the hypotheses on the frontier of *active* research-clusters — the targets
    reading should gravitate toward. Resolves each cluster's frontier_hypotheses slugs to IRIs."""
    anchors = set()
    for node in nodes:
        fm = node.get("frontmatter", {})
        # node_type is the folder name ("clusters"); knowledge_type is the authoritative type.
        if fm.get("knowledge_type") != "research-cluster":
            continue
        if fm.get("status") != "active":
            continue
        for h_slug in fm.get("frontier_hypotheses", []) or []:
            hp = find_node_path(h_slug)
            if hp:
                hn = load_node(hp)
                if hn:
                    anchors.add(hn["iri"])
    return anchors


def _cluster_proximity_map(G, anchors) -> dict:
    """Map {iri: 1/(1+hops)} where hops is the undirected distance to the nearest frontier
    anchor over DELIBERATE typed edges only (raw `related` wikilinks excluded, so the signal
    reflects cluster/hypothesis/concept structure rather than incidental co-mention).
    Nodes unreachable from any anchor are absent (treated as proximity 0)."""
    if not anchors:
        return {}
    UG = nx.Graph()
    UG.add_nodes_from(G.nodes())
    for u, v, d in G.edges(data=True):
        if d.get("edge_type") != "related":
            UG.add_edge(u, v)
    present = [a for a in anchors if a in UG]
    if not present:
        return {}
    # Virtual super-source linked to every anchor → one BFS gives multi-source distance.
    SUPER = "__frontier_super__"
    UG.add_node(SUPER)
    for a in present:
        UG.add_edge(SUPER, a)
    lengths = nx.single_source_shortest_path_length(UG, SUPER)
    # distance from SUPER is 1 + hops-to-nearest-anchor; an anchor sits at distance 1.
    return {iri: 1.0 / (1.0 + (d - 1)) for iri, d in lengths.items() if iri != SUPER}


def tool_get_concept_frontier(cluster_proximity_weight: float = None) -> dict:
    """Return concepts that need attention most urgently. Priority blends centrality
    (inbound refs), coverage/understanding gaps, and proximity to the frontier hypotheses of
    active research-clusters — so reading is driven by the research agenda, not just citation
    count. The cluster-proximity term is 0 until a cluster's frontier_hypotheses are set and its
    membership edges are materialized (see add_connections).

    cluster_proximity_weight overrides the proximity weight for THIS call only; if omitted, the
    persisted default (set_priority_config) or the built-in default is used. The returned object
    reports the effective weight and its source under `params`."""
    eff_weight, weight_source = _effective_proximity_weight(cluster_proximity_weight)

    nodes = load_all_nodes()
    G = get_graph()

    anchors = _active_frontier_anchors(nodes)
    proximity = _cluster_proximity_map(G, anchors)

    results = []
    for node in nodes:
        iri = node["iri"]
        coverage = node.get("coverage", 0)
        understanding = node.get("understanding", 0)

        # Count inbound edges as proxy for centrality
        inbound_count = G.in_degree(iri) if iri in G else 0
        cluster_proximity = proximity.get(iri, 0.0)

        # Priority: centrality + coverage/understanding gaps + cluster-frontier proximity
        priority_score = (
            (inbound_count * 0.5)
            + ((5 - coverage) * 0.3)
            + ((5 - understanding) * 0.2)
            + (cluster_proximity * eff_weight)
        )

        results.append({
            "iri": iri,
            "canonical_title": node["title"],
            "coverage": coverage,
            "understanding": understanding,
            "inbound_refs": inbound_count,
            "cluster_proximity": round(cluster_proximity, 3),
            "priority_score": round(priority_score, 3),
            # node_type: singular knowledge type (frontmatter), falling back to folder→type.
            # Needed so the viewer can filter the frontier by type (folder name would be plural).
            "node_type": node.get("frontmatter", {}).get("knowledge_type")
                         or FOLDER_TO_TYPE.get(node.get("node_type", ""), node.get("node_type", "")),
            "domain": node.get("domain", []),
        })

    ranked = sorted(results, key=lambda x: x["priority_score"], reverse=True)[:20]
    return {
        "params": {
            "cluster_proximity_weight": eff_weight,
            "weight_source": weight_source,
            "built_in_default": DEFAULT_CLUSTER_PROXIMITY_WEIGHT,
            "frontier_anchors": len(anchors),
        },
        "results": ranked,
    }


def tool_set_priority_config(cluster_proximity_weight: float = None, reset: bool = False) -> dict:
    """Set, reset, or report the DEFAULT cluster-proximity weight used by get_concept_frontier for
    every call that does not pass an explicit override.
    - reset=True restores the built-in default (removes the persisted config).
    - cluster_proximity_weight=<n> persists <n> as the new default for all calls.
    - neither: report the current effective default without changing it.
    Persisted to a config file so it survives restarts and is shared across gunicorn workers."""
    import json as _json
    if reset:
        try:
            if PRIORITY_CONFIG_PATH.exists():
                PRIORITY_CONFIG_PATH.unlink()
        except Exception as ex:
            logger.warning(f"priority config reset failed: {ex}")
        return {
            "status": "reset",
            "cluster_proximity_weight": DEFAULT_CLUSTER_PROXIMITY_WEIGHT,
            "weight_source": "built-in-default",
            "built_in_default": DEFAULT_CLUSTER_PROXIMITY_WEIGHT,
        }
    if cluster_proximity_weight is None:
        w, src = _effective_proximity_weight(None)
        return {"status": "unchanged", "cluster_proximity_weight": w, "weight_source": src,
                "built_in_default": DEFAULT_CLUSTER_PROXIMITY_WEIGHT}
    w = float(cluster_proximity_weight)
    PRIORITY_CONFIG_PATH.write_text(_json.dumps({"cluster_proximity_weight": w}))
    return {"status": "set", "cluster_proximity_weight": w, "weight_source": "config-default",
            "built_in_default": DEFAULT_CLUSTER_PROXIMITY_WEIGHT}


def _extract_section(content: str, section_title: str) -> str:
    """Return the body text under a `## section_title` heading (up to the next `## ` or EOF), or ''."""
    m = re.search(
        r'^##\s+' + re.escape(section_title) + r'\s*\n(.*?)(?=^##\s|\Z)',
        content, re.DOTALL | re.MULTILINE,
    )
    return m.group(1).strip() if m else ""


def tool_get_clusters() -> list:
    """List all research-clusters with their thesis, constituent hypotheses (resolved titles +
    frontier flag), current-frontier prose, and the concept/technique nodes each cluster depends on.
    Powers the viewer's Clusters tab."""
    nodes = load_all_nodes()
    G = get_graph()
    by_iri = {n["iri"]: n for n in nodes}
    clusters = [n for n in nodes if n.get("frontmatter", {}).get("knowledge_type") == "research-cluster"]
    out = []
    for c in clusters:
        fm = c["frontmatter"]
        frontier = fm.get("frontier_hypotheses") or []
        hyps = []
        for h_slug in fm.get("hypotheses", []) or []:
            hp = find_node_path(h_slug)
            if hp:
                hn = load_node(hp); hfm = hn.get("frontmatter", {})
                hyps.append({"slug": h_slug, "iri": hn["iri"], "title": hfm.get("title", h_slug),
                             "status": hfm.get("status", "open"), "role": hfm.get("research_program_role", ""),
                             "is_frontier": h_slug in frontier})
            else:
                hyps.append({"slug": h_slug, "iri": None, "title": h_slug,
                             "status": "missing", "role": "", "is_frontier": h_slug in frontier})
        deps = []
        for _u, v, d in G.edges(c["iri"], data=True):
            if d.get("edge_type") == "related":
                continue
            tn = by_iri.get(v)
            deps.append({
                "iri": v,
                "title": tn["title"] if tn else v.split(":")[-1],
                "type": (tn.get("frontmatter", {}).get("knowledge_type") if tn else v.split(":")[1]),
                "predicate": d.get("edge_type"),
                "coverage": tn.get("coverage", 0) if tn else 0,
            })
        out.append({
            "iri": c["iri"], "slug": c["slug"], "title": fm.get("title", c["slug"]),
            "domain": fm.get("domain", []), "status": fm.get("status", "active"),
            "thesis": _extract_section(c.get("content", ""), "Thesis"),
            "current_frontier": _extract_section(c.get("content", ""), "Current Frontier"),
            "hypotheses": hyps, "frontier_hypotheses": frontier, "deps": deps,
        })
    return sorted(out, key=lambda x: x["slug"])


def tool_get_cluster_priorities() -> dict:
    """Concept-centric reading priority: for each ACTIVE cluster, the concept/technique/result
    nodes its frontier hypotheses depend on (coverage gaps surface first), plus the source reading
    queue. Powers the viewer's Priority tab. Reports the effective cluster-proximity weight."""
    nodes = load_all_nodes()
    G = get_graph()
    by_iri = {n["iri"]: n for n in nodes}
    eff_w, src = _effective_proximity_weight(None)
    clusters = [n for n in nodes
                if n.get("frontmatter", {}).get("knowledge_type") == "research-cluster"
                and n.get("frontmatter", {}).get("status") == "active"]
    groups = []
    for c in clusters:
        fm = c["frontmatter"]
        frontier = fm.get("frontier_hypotheses") or []
        if not frontier:
            continue
        gapset = {}
        for h_slug in frontier:
            hp = find_node_path(h_slug)
            if not hp:
                continue
            hn = load_node(hp)
            for _u, v, d in G.edges(hn["iri"], data=True):
                if d.get("edge_type") == "related":
                    continue
                tn = by_iri.get(v)
                if not tn:
                    continue
                kt = tn.get("frontmatter", {}).get("knowledge_type", "")
                if kt in ("research-cluster", "hypothesis"):
                    continue
                gapset[v] = {
                    "iri": v, "title": tn["title"],
                    "type": kt or FOLDER_TO_TYPE.get(tn.get("node_type", ""), tn.get("node_type", "")),
                    "coverage": tn.get("coverage", 0), "understanding": tn.get("understanding", 0),
                }
        gaps = sorted(gapset.values(), key=lambda x: (x["coverage"], x["understanding"]))
        groups.append({
            "cluster_slug": c["slug"], "cluster_iri": c["iri"],
            "cluster_title": fm.get("title", c["slug"]),
            "lead_hypothesis": frontier[0] if frontier else None,
            "frontier_hypotheses": frontier, "gaps": gaps,
        })
    return {
        "params": {"cluster_proximity_weight": eff_w, "weight_source": src},
        "clusters": sorted(groups, key=lambda x: x["cluster_slug"]),
        "reading_queue": tool_get_reading_queue(),
    }


def tool_get_reading_graph(
    scope: str = "all_unread",
    focus_concept: str = None,
    focus_domain: str = None,
    min_edge_weight: int = 2,
    max_nodes: int = 100,
) -> dict:
    """
    Return the source dependency graph.

    scope:
      "queue_only"  — only the 70 actively-tracked sources
      "all_unread"  — all unread sources (default)
      "full"        — all sources including already-read

    focus_concept / focus_domain: return the subgraph reachable from
    sources that cover the given concept slug or domain tag.

    Returns nodes, edges, clusters, gateway_nodes, suggested_sequence.
    """
    graph_path = WIKI_DIR / "source_graph.json"

    # Auto-build if missing
    if not graph_path.exists():
        try:
            import subprocess as _sp
            script = Path(__file__).parent.parent / "scripts" / "build_source_graph.py"
            if script.exists():
                _sp.run([sys.executable, str(script)], check=True, capture_output=True)
        except Exception as e:
            logger.warning(f"Could not auto-build source graph: {e}")
            return {"error": "source_graph.json not found — run scripts/build_source_graph.py"}

    try:
        graph = json.loads(graph_path.read_text())
    except Exception as e:
        return {"error": f"Could not read source_graph.json: {e}"}

    nodes: dict = graph.get("nodes", {})
    edges: list = graph.get("edges", [])

    # ── apply scope filter ────────────────────────────────────────────────
    if scope == "queue_only":
        keep = {s for s, n in nodes.items() if n.get("in_queue")}
    elif scope == "all_unread":
        keep = {s for s, n in nodes.items() if n.get("status") == "unread"}
    else:  # "full"
        keep = set(nodes.keys())

    # ── apply concept / domain focus ─────────────────────────────────────
    # Focus starts from the *full* nodes dict so 1-hop expansion can surface
    # out-of-scope sources worth adding.  We annotate those with out_of_scope=True.
    if focus_concept:
        seed = {s for s in nodes if focus_concept in nodes[s].get("concepts", [])}
        neighbours = set()
        for e in edges:
            if e["from"] in seed: neighbours.add(e["to"])
            if e["to"]   in seed: neighbours.add(e["from"])
        focus_set = seed | neighbours
        # Annotate nodes outside the original scope
        for s in focus_set - keep:
            nodes[s]["out_of_scope"] = True
        keep = focus_set  # replace keep with focused set

    if focus_domain:
        seed = {s for s in nodes
                if focus_domain in (nodes[s].get("domain") or [])}
        neighbours = set()
        for e in edges:
            if e["from"] in seed: neighbours.add(e["to"])
            if e["to"]   in seed: neighbours.add(e["from"])
        focus_set = seed | neighbours
        for s in focus_set - keep:
            nodes[s]["out_of_scope"] = True
        keep = focus_set

    # ── filter edges ─────────────────────────────────────────────────────
    filtered_edges = [
        e for e in edges
        if e["from"] in keep and e["to"] in keep
        and e["weight"] >= min_edge_weight
    ]

    # ── trim to max_nodes (highest lb_score first) ────────────────────────
    if len(keep) > max_nodes:
        keep = set(sorted(keep, key=lambda s: nodes[s].get("lb_score", 0), reverse=True)[:max_nodes])
        filtered_edges = [e for e in filtered_edges if e["from"] in keep and e["to"] in keep]

    filtered_nodes = {s: nodes[s] for s in keep}

    # ── recalculate gateway nodes for this subgraph ──────────────────────
    has_prereq_inbound = {e["to"] for e in filtered_edges if e["direction"] == "prerequisite"}
    lb_vals = sorted([n.get("lb_score", 0) for n in filtered_nodes.values() if n.get("lb_score", 0) > 0])
    q3 = lb_vals[int(len(lb_vals) * 0.75)] if lb_vals else 0
    gateway_nodes = sorted(
        [s for s, n in filtered_nodes.items()
         if n.get("lb_score", 0) >= q3 and s not in has_prereq_inbound],
        key=lambda s: -filtered_nodes[s].get("lb_score", 0)
    )[:20]

    # ── cluster info for retained nodes ──────────────────────────────────
    cluster_ids_in_view = {n.get("cluster_id") for n in filtered_nodes.values()}
    clusters = {
        str(cid): graph["clusters"].get(str(cid), {})
        for cid in cluster_ids_in_view
        if str(cid) in graph.get("clusters", {})
    }

    # ── suggested sequence (queue items in topological order) ─────────────
    sequence = [s for s in graph.get("suggested_sequence", []) if s in keep]

    return {
        "meta": {
            **graph.get("meta", {}),
            "scope":          scope,
            "nodes_returned": len(filtered_nodes),
            "edges_returned": len(filtered_edges),
            "min_edge_weight": min_edge_weight,
        },
        "nodes":              filtered_nodes,
        "edges":              filtered_edges,
        "clusters":           clusters,
        "gateway_nodes":      gateway_nodes,
        "suggested_sequence": sequence[:30],
    }


def tool_rebuild_source_graph() -> dict:
    """Rebuild wiki/source_graph.json from current wiki state. Run after ingest."""
    try:
        import subprocess as _sp
        script = Path(__file__).parent.parent / "scripts" / "build_source_graph.py"
        result = _sp.run(
            [sys.executable, str(script)],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0:
            return {"status": "error", "detail": result.stderr[:500]}
        graph_path = WIKI_DIR / "source_graph.json"
        meta = json.loads(graph_path.read_text()).get("meta", {})
        return {"status": "rebuilt", **meta}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


def tool_get_index(domain=None, node_type=None) -> list:
    nodes = load_all_nodes()
    results = []
    for node in nodes:
        singular = FOLDER_TO_TYPE.get(node["node_type"], node["node_type"])
        if domain and domain not in node.get("domain", []):
            continue
        # accept singular type ("concept") or the raw folder name ("concepts")
        if node_type and singular != node_type and node["node_type"] != node_type:
            continue
        results.append({
            "iri": node["iri"],
            "canonical_title": node["title"],
            "domain": node["domain"],
            "node_type": singular,
            "coverage": node["coverage"],
            "understanding": node["understanding"],
            "date_updated": node.get("date_updated", "")
        })
    return sorted(results, key=lambda x: x["canonical_title"])


def tool_get_domains() -> list:
    """Aggregate the domains across all nodes with counts — powers the viewer's domain facet."""
    from collections import Counter
    c = Counter()
    for n in load_all_nodes():
        for d in (n.get("domain") or []):
            if d:
                c[d] += 1
    return [{"domain": k, "count": v} for k, v in sorted(c.items(), key=lambda x: (-x[1], x[0]))]


def tool_get_health_metrics() -> dict:
    nodes = load_all_nodes()
    G = get_graph()

    total = len(nodes)
    sources = [n for n in nodes if n["node_type"] == "sources"]
    concepts = [n for n in nodes if n["node_type"] != "sources"]

    coverages = [n.get("coverage", 0) for n in nodes]
    understandings = [n.get("understanding", 0) for n in nodes]

    cross_domain_edges = sum(
        1 for u, v, d in G.edges(data=True)
        if G.nodes[u].get("domain") != G.nodes[v].get("domain")
    )

    stubs = [n for n in nodes if n.get("coverage", 0) <= 1]
    missing_source = [n for n in nodes if n.get("frontmatter", {}).get("needs_canonical_source")]
    queue_items = tool_get_reading_queue()

    return {
        "total_nodes": total,
        "total_sources": len(sources),
        "total_concepts": len(concepts),
        "avg_coverage": round(sum(coverages) / total, 2) if total else 0,
        "avg_understanding": round(sum(understandings) / total, 2) if total else 0,
        "cross_domain_connections": cross_domain_edges,
        "queue_depth": len(queue_items),
        "stubs_awaiting_deepening": len(stubs),
        "stubs_missing_source": len(missing_source),
        "total_edges": G.number_of_edges()
    }


def tool_get_sourceless_stubs() -> list:
    """List live knowledge nodes flagged needs_canonical_source: true.

    These are nodes that were stubbed before a canonical source was attached.
    Each entry carries any reference suggestions captured at creation time so a
    source can be found and attached."""
    out = []
    for n in load_all_nodes():
        fm = n.get("frontmatter", {})
        if not fm.get("needs_canonical_source"):
            continue
        out.append({
            "iri": n.get("iri"),
            "title": n.get("title", ""),
            "knowledge_type": fm.get("knowledge_type") or n.get("node_type"),
            "domain": n.get("domain", []),
            "date_created": fm.get("date_created", ""),
            "suggested_sources": fm.get("suggested_sources", {}),
        })
    return sorted(out, key=lambda x: x.get("date_created", ""), reverse=True)


def tool_check_alias_collision(surface_form: str) -> dict:
    registry = get_alias_registry()
    normalized = surface_form.lower()
    results = []

    for alias, iri in registry.items():
        if normalized in alias or alias in normalized:
            path = find_node_path_by_iri(iri)
            node = load_node(path) if path else {}
            similarity = len(set(normalized.split()) & set(alias.split())) / \
                        max(len(normalized.split()), len(alias.split()), 1)
            results.append({
                "iri": iri,
                "canonical_title": node.get("title", iri),
                "existing_aliases": node.get("aliases", []),
                "similarity_score": similarity
            })

    return {
        "surface_form": surface_form,
        "collision_candidates": sorted(results, key=lambda x: x["similarity_score"], reverse=True)[:5]
    }


def tool_log_operation(operation_type: str, affected_iris: list, summary: str, agent: str) -> dict:
    log_path = WIKI_DIR / "log.md"
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    iris_str = ", ".join(affected_iris)
    entry = f"\n## [{timestamp}] {operation_type} | {agent}\n- {summary}\n- Affected: {iris_str}\n"

    with open(log_path, "a") as f:
        f.write(entry)

    return {"success": True, "timestamp": timestamp}


def tool_register_operational_reference(
    operational_node_id: str,
    iri: str,
    confidence_class: str,
    source_system: str = "mnemon"
) -> dict:
    """Store operational → PKIS bridge reference."""
    bridge_path = WIKI_DIR / "bridge_references.jsonl"
    record = {
        "operational_node_id": operational_node_id,
        "iri": iri,
        "confidence_class": confidence_class,
        "source_system": source_system,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "reference_id": str(uuid.uuid4())[:8]
    }
    with open(bridge_path, "a") as f:
        f.write(json.dumps(record) + "\n")

    return {"success": True, "reference_id": record["reference_id"]}


def tool_get_operational_references(iri: str) -> list:
    bridge_path = WIKI_DIR / "bridge_references.jsonl"
    if not bridge_path.exists():
        return []

    results = []
    with open(bridge_path) as f:
        for line in f:
            try:
                record = json.loads(line)
                if record.get("iri") == iri:
                    results.append(record)
            except json.JSONDecodeError:
                continue

    return results


def tool_get_concept_operational_load(iri: str) -> dict:
    refs = tool_get_operational_references(iri)
    confirmed = [r for r in refs if r.get("confidence_class") == "confirmed"]
    inferred = [r for r in refs if r.get("confidence_class") != "confirmed"]
    systems = list(set(r.get("source_system") for r in refs))
    timestamps = [r.get("timestamp") for r in refs if r.get("timestamp")]

    return {
        "iri": iri,
        "confirmed_refs": len(confirmed),
        "inferred_refs": len(inferred),
        "source_systems": systems,
        "earliest_ref": min(timestamps) if timestamps else None,
        "latest_ref": max(timestamps) if timestamps else None
    }


# ============================================================
# Write tool helpers — metadata enrichment
# ============================================================

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


# ============================================================
# Write tool implementations
# ============================================================

def tool_create_bridge_note(
    rationale: str,
    source_context: str = "",
    linked_node_refs: list = None,
    proposed_edge_type: str = "",
    origin: str = "conversation",
    title: str = ""
) -> dict:
    """Create a bridge note in the staging area."""
    if not rationale:
        raise ValueError("rationale is required")

    staged_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y%m%d")
    ts_str = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Generate a descriptor from the rationale (first 5 meaningful words)
    descriptor_words = re.sub(r'[^a-z0-9\s]', '', rationale.lower()).split()[:5]
    descriptor = "-".join(descriptor_words)
    slug = f"bn-{date_str}-{descriptor}"[:60]

    # Resolve fuzzy references
    # linked_nodes stores plain slugs/refs (no wikilink brackets) for clean YAML frontmatter.
    # The body section wraps them in [[...]] for Obsidian wikilink rendering.
    resolution_candidates = {}
    linked_nodes = []
    if linked_node_refs:
        for ref in (linked_node_refs or []):
            path = find_node_path_by_iri(ref)
            if path:
                node = load_node(path)
                linked_nodes.append(node["slug"])
            else:
                results = hybrid_search(ref, max_results=3)
                if results:
                    resolution_candidates[ref] = [r["iri"] for r in results]
                linked_nodes.append(ref)

    fm = {
        "staged_at": ts_str,
        "staged_by": "mcp-create-bridge-note",
        "staged_id": staged_id,
        "review_status": "pending",
        "proposed_edges": [],
        "title": title or (", ".join(linked_nodes[:3]) + " connection" if linked_nodes else rationale[:80]),
        "knowledge_type": "bridge-note",
        "date_created": now.strftime("%Y-%m-%d"),
        "status": "unreviewed",
        "origin": origin,
        "source_context": source_context,
        "linked_nodes": linked_nodes,
        "proposed_edge_type": proposed_edge_type or "",
        "rationale": rationale,
        "integration_target": "",
    }
    if resolution_candidates:
        fm["resolution_candidates"] = resolution_candidates

    body = f"""## Connection
{rationale}

## Nodes Involved
{chr(10).join(f'- [[{n}]]' for n in linked_nodes) if linked_nodes else '_To be determined_'}

## Integration Notes
Pending review.
"""

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    staged_path = STAGING_DIR / f"{slug}.md"
    counter = 1
    while staged_path.exists():
        staged_path = STAGING_DIR / f"{slug}-{counter}.md"
        counter += 1

    staged_path.write_text(f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n{body}")

    log_path = WIKI_DIR / "log.md"
    with open(log_path, "a") as lf:
        lf.write(f"\n## [{now.strftime('%Y-%m-%d')}] staged | bridge-note\n- Staged: {staged_path.stem} (id: {staged_id})\n- Rationale: {rationale[:100]}\n")

    return {
        "staged_id": staged_id,
        "staged_at": ts_str,
        "slug": staged_path.stem,
        "resolution_candidates": resolution_candidates,
        "review_url": f"https://github.com/choct155/pkis/blob/main/wiki/staging/{staged_path.name}",
    }


def tool_create_source_stub(
    title: str = "",
    url: str = "",
    doi: str = "",
    authors: str = "",
    year: int = None,
    notes: str = "",
    priority: str = "normal"
) -> dict:
    """Create a source stub in staging with automated metadata enrichment."""
    if not any([title, url, doi]):
        raise ValueError("At least one of title, url, or doi must be provided")

    # ---- Enrichment ----
    metadata = {}
    enrichment_status = "minimal"

    # Detect arXiv
    arxiv_id = None
    if url and "arxiv.org" in url:
        m = re.search(r'arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]+v?[0-9]*)', url)
        if m:
            arxiv_id = m.group(1)
    if arxiv_id:
        metadata = _fetch_arxiv_metadata(arxiv_id)
        if metadata.get("title"):
            enrichment_status = "full" if metadata.get("abstract") else "partial"

    # CrossRef fallback
    if not metadata.get("title") and doi:
        metadata = _fetch_crossref_metadata(doi)
        if metadata.get("title"):
            enrichment_status = "full" if metadata.get("abstract") else "partial"

    # Merge caller-provided fields (override enriched values)
    if title:
        metadata["title"] = title
    if authors:
        metadata["authors"] = authors
    if year:
        metadata["year"] = year

    # ---- Slug generation ----
    final_title = metadata.get("title") or title or doi or url or "unknown"
    final_authors = metadata.get("authors") or authors or ""
    final_year = metadata.get("year") or year

    first_author_last = ""
    if final_authors:
        first_author = final_authors.split(",")[0].strip()
        first_author_last = re.sub(r'[^a-z0-9]', '', first_author.split()[-1].lower()) if first_author else ""

    title_words = re.sub(r'[^a-z0-9\s]', '', final_title.lower()).split()
    key_word = title_words[0] if title_words else "source"
    year_str = str(final_year) if final_year else ""

    slug_parts = [p for p in [first_author_last, key_word, year_str] if p]
    base_slug = "-".join(slug_parts)[:55] if slug_parts else "source-stub"
    slug = base_slug
    counter = 1
    while (STAGING_DIR / f"{slug}.md").exists() or find_node_path(slug):
        slug = f"{base_slug}-{counter}"
        counter += 1

    # ---- Connection candidates ----
    search_text = f"{final_title} {metadata.get('abstract', '')[:400]}"
    connection_candidates = []
    try:
        results = hybrid_search(search_text, max_results=8)
        connection_candidates = [r["iri"] for r in results if r["node_type"] != "sources"]
    except Exception:
        pass

    # ---- Build staged file ----
    staged_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc)
    ts_str = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    fields_populated = [k for k, v in {
        "title": metadata.get("title"),
        "authors": metadata.get("authors") or authors,
        "year": metadata.get("year") or year,
        "abstract": metadata.get("abstract"),
        "venue": metadata.get("venue"),
    }.items() if v]

    fm = {
        "staged_at": ts_str,
        "staged_by": "mcp-create-source-stub",
        "staged_id": staged_id,
        "review_status": "pending",
        "proposed_edges": [],
        "id": f"pkis:source:{slug}",
        "aliases": [],
        "title": metadata.get("title") or title or "",
        "authors": metadata.get("authors") or authors or "",
        "year": final_year,
        "type": metadata.get("source_type", "paper"),
        "domain": [],
        "tags": [],
        "source_url": url or "",
        "doi": doi or "",
        "drive_id": "",
        "drive_path": "",
        "status": "unread",
        "date_added": now.strftime("%Y-%m-%d"),
        "concepts": [],
        "connection_candidates": connection_candidates[:8],
        "priority": priority,
    }

    abstract = metadata.get("abstract", "")
    body = f"""## Summary
{abstract[:500] if abstract else '[To be filled during ingest]'}

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
{chr(10).join(f'- {iri}' for iri in connection_candidates[:5]) if connection_candidates else '[None identified]'}
{f'{chr(10)}## Notes{chr(10)}{notes}' if notes else ''}
"""

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    staged_path = STAGING_DIR / f"{slug}.md"
    staged_path.write_text(f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n{body}")

    log_path = WIKI_DIR / "log.md"
    with open(log_path, "a") as lf:
        lf.write(
            f"\n## [{now.strftime('%Y-%m-%d')}] staged | source-stub\n"
            f"- Staged: {slug} (id: {staged_id})\n"
            f"- Title: {metadata.get('title') or title or '(unknown)'}\n"
            f"- Enrichment: {enrichment_status}\n"
        )

    return {
        "staged_id": staged_id,
        "staged_at": ts_str,
        "slug": slug,
        "enrichment_status": enrichment_status,
        "fields_populated": fields_populated,
        "connection_candidates": connection_candidates[:5],
        "review_url": f"https://github.com/choct155/pkis/blob/main/wiki/staging/{staged_path.name}",
    }


# component_scores schema per knowledge node type (SCHEMA.md v3.0)
NODE_COMPONENT_SCORES = {
    "concept":   ["definition", "prerequisites", "boundary", "scope", "application", "formal_statement", "dependents", "transfer"],
    "technique": ["operational_mechanism", "principled_mechanism", "conditions", "implementation", "diagnostics", "alternatives", "failure_modes"],
    "framework": ["structure", "purpose", "primitives", "scope", "application", "limits"],
    "result":    ["statement", "proof_sketch", "conditions", "implications", "limitations"],
    "problem":   ["formulation", "why_hard", "solution_landscape", "instances"],
    "principle": ["statement", "justification", "implications", "violations"],
}


def tool_create_node_stub(
    knowledge_type: str,
    title: str,
    definition: str = "",
    domain: list = None,
    tags: list = None,
    aliases: list = None,
    also_type: list = None,
    sources: list = None,
    slug: str = "",
    suggest_sources: bool = True,
) -> dict:
    """Create a knowledge-node stub of any of the six knowledge types in staging,
    BEFORE a canonical source exists. If no source is supplied, flags the node with
    needs_canonical_source and (optionally) suggests references from the corpus and
    Semantic Scholar so the gap can be closed."""
    if knowledge_type not in NODE_COMPONENT_SCORES:
        raise ValueError(
            f"knowledge_type must be one of {sorted(NODE_COMPONENT_SCORES)}; got '{knowledge_type}'"
        )
    if not title:
        raise ValueError("title is required")

    domain = domain or []
    tags = tags or []
    aliases = aliases or []
    also_type = also_type or []
    sources = sources or []

    # ---- Slug generation ----
    base = slug or title
    base_slug = re.sub(r'[^a-z0-9]+', '-', base.lower()).strip('-')[:55] or "node-stub"
    slug = base_slug
    counter = 1
    while (STAGING_DIR / f"{slug}.md").exists() or find_node_path(slug):
        slug = f"{base_slug}-{counter}"
        counter += 1

    # ---- Normalize source refs to plain slugs ----
    norm_sources = []
    for s in sources:
        if isinstance(s, str) and s.startswith("pkis:"):
            _, _nt, sp = parse_iri(s)
            norm_sources.append(sp or s)
        else:
            norm_sources.append(str(s).strip("[]"))

    needs_source = len(norm_sources) == 0

    # ---- Reference suggestions for sourceless stubs ----
    internal_suggestions, external_suggestions = [], []
    if needs_source and suggest_sources:
        try:
            results = hybrid_search(f"{title} {definition}".strip(), max_results=6)
            internal_suggestions = [
                {"iri": r["iri"], "title": r.get("canonical_title", r["iri"])}
                for r in results if r.get("node_type") == "sources"
            ][:5]
        except Exception as e:
            logger.error(f"internal suggestion search failed: {e}")
        try:
            external_suggestions = _search_semantic_scholar(title, limit=5)
        except Exception as e:
            logger.error(f"external suggestion search failed: {e}")

    # ---- Frontmatter ----
    staged_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc)
    ts_str = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    date_str = now.strftime("%Y-%m-%d")

    fm = {
        "staged_at": ts_str,
        "staged_by": "mcp-create-node-stub",
        "staged_id": staged_id,
        "review_status": "pending",
        "proposed_edges": [],
        "id": f"pkis:{knowledge_type}:{slug}",
        "aliases": aliases,
        "title": title,
        "knowledge_type": knowledge_type,
        "also_type": also_type,
        "domain": domain,
        "tags": tags,
        "related_concepts": [],
        "sources": norm_sources,
        "date_created": date_str,
        "date_updated": date_str,
        "coverage": 1 if norm_sources else 0,
        "understanding": 0,
        "maturity": "evolving",
        "component_scores": {k: None for k in NODE_COMPONENT_SCORES[knowledge_type]},
        "needs_canonical_source": needs_source,
    }
    if needs_source and (internal_suggestions or external_suggestions):
        fm["suggested_sources"] = {
            "internal": internal_suggestions,
            "external": external_suggestions,
        }

    body = f"""## Definition
{definition if definition else '[To be filled during deepening]'}

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]
"""
    if needs_source:
        int_lines = "\n".join(f"- {s['iri']} — {s['title']}" for s in internal_suggestions) or "[none in corpus]"
        ext_lines = "\n".join(
            f"- {s['title']} ({s.get('year') or '?'}) — {s.get('url') or ''}".rstrip(" —")
            for s in external_suggestions
        ) or "[none found]"
        body += (
            "\n## Needs Canonical Source\n"
            "This stub was created without a source. Suggested references:\n\n"
            f"**Already in corpus:**\n{int_lines}\n\n"
            f"**External candidates (Semantic Scholar):**\n{ext_lines}\n"
        )

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    staged_path = STAGING_DIR / f"{slug}.md"
    staged_path.write_text(f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n{body}")

    log_path = WIKI_DIR / "log.md"
    with open(log_path, "a") as lf:
        lf.write(
            f"\n## [{date_str}] staged | node-stub ({knowledge_type})\n"
            f"- Staged: {slug} (id: {staged_id})\n"
            f"- Title: {title}\n"
            f"- needs_canonical_source: {needs_source}\n"
        )

    return {
        "staged_id": staged_id,
        "staged_at": ts_str,
        "slug": slug,
        "iri": f"pkis:{knowledge_type}:{slug}",
        "knowledge_type": knowledge_type,
        "needs_canonical_source": needs_source,
        "sources": norm_sources,
        "suggested_sources": {
            "internal": internal_suggestions,
            "external": external_suggestions,
        } if needs_source else {},
        "review_url": f"https://github.com/choct155/pkis/blob/main/wiki/staging/{staged_path.name}",
    }


def tool_create_hypothesis(
    title: str,
    cluster: str = "",
    role: str = "direct-test",
    domain: list = None,
    tags: list = None,
    formal_statement: str = "",
    motivation: str = "",
    current_evidence: str = "",
    open_questions: str = "",
    dependent_nodes: list = None,
    aliases: list = None,
    slug: str = "",
) -> dict:
    """Stage a hypothesis node — the one knowledge type create_node_stub does not cover.
    Hypotheses are research-program artifacts that belong to a research-cluster; this stages
    one with the standard hypothesis frontmatter + body sections (Formal Statement, Motivation,
    Current Evidence, Open Questions, Connections). Promote to the live graph via
    commit_staged_node (lands in wiki/hypotheses/)."""
    if not title:
        raise ValueError("title is required")

    domain = domain or []
    tags = tags or []
    aliases = aliases or []
    dependent_nodes = dependent_nodes or []

    # ---- Slug generation (same convention as create_node_stub) ----
    base = slug or title
    base_slug = re.sub(r'[^a-z0-9]+', '-', base.lower()).strip('-')[:55] or "hypothesis-stub"
    slug = base_slug
    counter = 1
    while (STAGING_DIR / f"{slug}.md").exists() or find_node_path(slug):
        slug = f"{base_slug}-{counter}"
        counter += 1

    # ---- Normalize cluster ref to a plain slug ----
    cluster_slug = ""
    if cluster:
        if cluster.startswith("pkis:"):
            _, _nt, cluster_slug = parse_iri(cluster)
        else:
            cluster_slug = cluster.strip("[]")

    staged_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc)
    ts_str = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    date_str = now.strftime("%Y-%m-%d")

    fm = {
        "staged_at": ts_str,
        "staged_by": "mcp-create-hypothesis",
        "staged_id": staged_id,
        "review_status": "pending",
        "proposed_edges": [],
        "id": f"pkis:hypothesis:{slug}",
        "aliases": aliases,
        "title": title,
        "knowledge_type": "hypothesis",
        "domain": domain,
        "tags": tags,
        "status": "open",
        "origin": "research-program",
        "research_program_cluster": cluster_slug or None,
        "research_program_role": role,
        "iks_link": None,
        "cluster_membership": [cluster_slug] if cluster_slug else [],
        "dependent_nodes": dependent_nodes,
        "evidence_nodes": [],
        "date_created": date_str,
        "date_updated": date_str,
    }

    conn_line = (
        f"- [[{cluster_slug}]] — belongs-to: constituent hypothesis of the {cluster_slug} cluster"
        if cluster_slug else "[To be populated during integration]"
    )
    body = f"""## Formal Statement
{formal_statement or '[To be filled]'}

## Motivation
{motivation or '[To be filled]'}

## Current Evidence
{current_evidence or '[To be filled]'}

## Open Questions
{open_questions or '[To be filled]'}

## Connections
{conn_line}
"""

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    staged_path = STAGING_DIR / f"{slug}.md"
    staged_path.write_text(f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n{body}")

    log_path = WIKI_DIR / "log.md"
    with open(log_path, "a") as lf:
        lf.write(
            f"\n## [{date_str}] staged | hypothesis\n"
            f"- Staged: {slug} (id: {staged_id})\n"
            f"- Title: {title}\n"
            f"- Cluster: {cluster_slug or '(none)'}\n"
        )

    return {
        "staged_id": staged_id,
        "staged_at": ts_str,
        "slug": slug,
        "iri": f"pkis:hypothesis:{slug}",
        "knowledge_type": "hypothesis",
        "cluster": cluster_slug,
        "review_url": f"https://github.com/choct155/pkis/blob/main/wiki/staging/{staged_path.name}",
    }


def _replace_section(content: str, section_title: str, new_body: str) -> str:
    """Replace the body under a `## section_title` heading (up to the next `## ` or EOF).
    Append the section if it does not already exist."""
    pattern = re.compile(
        r'(^##\s+' + re.escape(section_title) + r'\s*\n)(.*?)(?=^##\s|\Z)',
        re.DOTALL | re.MULTILINE,
    )
    new_content, n = pattern.subn(
        lambda m: m.group(1) + new_body.rstrip() + "\n\n", content
    )
    if n == 0:
        new_content = content.rstrip() + f"\n\n## {section_title}\n{new_body.rstrip()}\n"
    return new_content


def tool_edit_node(
    iri: str = "",
    slug: str = "",
    frontmatter_updates: dict = None,
    section_updates: dict = None,
    commit_message: str = "",
) -> dict:
    """Edit a LIVE node's frontmatter fields and/or named body sections, then commit + push.
    - frontmatter_updates: {field: value} merged into frontmatter (a null value deletes the field).
    - section_updates: {"Section Title": "new markdown body"} — replaces the body under that
      `## Section Title` heading, or appends the section if absent.
    Covers what add_connections cannot (e.g. a cluster's frontier_hypotheses + Current Frontier).
    date_updated is bumped automatically."""
    frontmatter_updates = frontmatter_updates or {}
    section_updates = section_updates or {}
    if not frontmatter_updates and not section_updates:
        raise ValueError("nothing to edit: provide frontmatter_updates and/or section_updates")

    path = None
    if iri:
        path = find_node_path_by_iri(iri)
    if not path and slug:
        path = find_node_path(slug)
    if not path:
        raise ValueError(f"node not found: {iri or slug}")

    post = frontmatter.load(str(path))
    fm = dict(post.metadata)
    content = post.content

    for k, v in frontmatter_updates.items():
        if v is None:
            fm.pop(k, None)
        else:
            fm[k] = v

    for title, body_text in section_updates.items():
        content = _replace_section(content, title, body_text)

    fm["date_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    new_post = frontmatter.Post(content, **fm)
    path.write_text(frontmatter.dumps(new_post))

    # Invalidate caches so the next read/graph reflects the edit
    global _node_cache, _graph
    _node_cache = {}
    _graph = None

    iri_final = fm.get("id") or iri or iri_from_slug(path.parent.name, path.stem)
    rel = path.relative_to(WIKI_DIR)

    log_path = WIKI_DIR / "log.md"
    try:
        with open(log_path, "a") as lf:
            lf.write(
                f"\n## [{datetime.now(timezone.utc).strftime('%Y-%m-%d')}] edit | edit_node\n"
                f"- {iri_final}: fields={list(frontmatter_updates)} sections={list(section_updates)}\n"
            )
    except Exception:
        pass

    git_sha, git_pushed = "", False
    try:
        repo_dir = str(REPO_DIR)
        subprocess.run(["git", "-C", repo_dir, "add", str(path), str(log_path)],
                       check=True, capture_output=True)
        msg = commit_message or f"[mcp-edit] {iri_final}"
        result = subprocess.run(["git", "-C", repo_dir, "commit", "-m", msg],
                                check=True, capture_output=True, text=True)
        m = re.search(r'\[.+? ([a-f0-9]{7,})\]', result.stdout)
        git_sha = m.group(1) if m else result.stdout.strip()[:12]
        try:
            subprocess.run(["git", "-C", repo_dir, "push"], check=True,
                           capture_output=True, timeout=30)
            git_pushed = True
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as pe:
            logger.warning(f"edit_node push failed (local commit retained): {pe}")
    except subprocess.CalledProcessError as e:
        logger.error(f"edit_node commit failed: {e.stderr}")

    return {
        "status": "edited",
        "iri": iri_final,
        "path": str(rel),
        "frontmatter_updated": list(frontmatter_updates),
        "sections_updated": list(section_updates),
        "git_commit": git_sha,
        "git_pushed": git_pushed,
        "url": f"https://github.com/choct155/pkis/blob/main/wiki/{rel}",
    }


def tool_add_connections(edges: list, commit_message: str = "") -> dict:
    """Add typed, graph-visible edges between existing live nodes, in one batch + a single
    git commit. Each edge is a dict {subject, target, predicate, note}. The predicate is
    written into the SUBJECT node's frontmatter (so build_graph emits a weighted typed edge,
    subject -> target) and a readable line is appended to its ## Connections section.

    Idempotent per (subject, predicate, target). Targets must already be live. Invalid edges
    are reported in the results, not fatal to the batch."""
    if not edges:
        raise ValueError("edges must be a non-empty list")

    results = []
    modified_paths = set()

    for e in edges:
        subject = (e.get("subject") or "").strip()
        target = (e.get("target") or "").strip()
        predicate = (e.get("predicate") or "").strip()
        note = e.get("note", "") or ""
        try:
            if predicate not in EDGE_WEIGHTS:
                raise ValueError(f"invalid predicate '{predicate}'; must be one of {sorted(EDGE_WEIGHTS)}")
            subj_path = (find_node_path_by_iri(subject) if subject.startswith("pkis:")
                         else find_node_path(subject))
            if not subj_path:
                raise ValueError(f"subject not found: {subject}")
            if target.startswith("pkis:"):
                _, _nt, tslug = parse_iri(target)
            else:
                tslug = target.strip("[]").split("|")[0]
            if not find_node_path(tslug):
                raise ValueError(f"target not found (must be live): {target}")

            post = frontmatter.load(str(subj_path))
            fm = dict(post.metadata)
            body = post.content

            existing = fm.get(predicate, [])
            if isinstance(existing, str):
                existing = [existing]
            norm_existing = [str(x).strip("[]").split("|")[0] for x in existing]
            if tslug in norm_existing:
                results.append({"subject": subject, "target": tslug,
                                "predicate": predicate, "status": "already-present"})
                continue
            existing.append(tslug)
            fm[predicate] = existing

            line = f"- [[{tslug}]] — {predicate}: {note}".rstrip().rstrip(":").rstrip()
            if "## Connections" in body:
                body = body.replace("## Connections\n", f"## Connections\n{line}\n", 1)
            else:
                body = body.rstrip() + f"\n\n## Connections\n{line}\n"

            subj_path.write_text(frontmatter.dumps(frontmatter.Post(body, **fm)))
            modified_paths.add(str(subj_path))
            results.append({"subject": subject, "target": tslug, "predicate": predicate,
                            "weight": EDGE_WEIGHTS[predicate], "status": "added"})
        except Exception as ex:
            results.append({"subject": subject, "target": target,
                            "predicate": predicate, "status": "error", "error": str(ex)})

    # Invalidate caches so the next graph read reflects the new edges
    global _node_cache, _graph
    _node_cache = {}
    _graph = None

    added = [r for r in results if r["status"] == "added"]
    git_sha, git_pushed = "", False
    if modified_paths:
        try:
            repo_dir = str(REPO_DIR)
            subprocess.run(["git", "-C", repo_dir, "add"] + list(modified_paths),
                           check=True, capture_output=True)
            msg = commit_message or f"[mcp-edge] add {len(added)} connection(s)"
            result = subprocess.run(["git", "-C", repo_dir, "commit", "-m", msg],
                                    check=True, capture_output=True, text=True)
            m = re.search(r'\[.+? ([a-f0-9]{7,})\]', result.stdout)
            git_sha = m.group(1) if m else result.stdout.strip()[:12]
            try:
                subprocess.run(["git", "-C", repo_dir, "push"], check=True,
                               capture_output=True, timeout=30)
                git_pushed = True
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as pe:
                logger.warning(f"edge push failed (local commit retained): {pe}")
        except subprocess.CalledProcessError as e:
            logger.error(f"edge commit failed: {e.stderr}")

    try:
        with open(WIKI_DIR / "log.md", "a") as lf:
            lf.write(f"\n## [{datetime.now(timezone.utc).strftime('%Y-%m-%d')}] edges | add_connections\n")
            for r in added:
                lf.write(f"- {r['subject']} —{r['predicate']}→ {r['target']}\n")
    except Exception:
        pass

    return {
        "added": len(added),
        "skipped": len([r for r in results if r["status"] == "already-present"]),
        "errors": len([r for r in results if r["status"] == "error"]),
        "git_commit": git_sha,
        "git_pushed": git_pushed,
        "results": results,
    }


def tool_commit_staged_node(
    staged_id: str,
    edits: dict = None,
    confirmed_links: dict = None,
    action: str = "commit"
) -> dict:
    """Promote a reviewed staged node from staging to the live graph."""
    STAGING_DIR.mkdir(parents=True, exist_ok=True)

    # Find staged file by staged_id
    staged_file = None
    for f in STAGING_DIR.glob("*.md"):
        try:
            post = frontmatter.load(str(f))
            if post.metadata.get("staged_id") == staged_id:
                staged_file = f
                break
        except Exception:
            continue

    if not staged_file:
        raise ValueError(f"No staged node found with staged_id: {staged_id}")

    post = frontmatter.load(str(staged_file))
    fm = dict(post.metadata)
    body_content = post.content

    if action == "discard":
        staged_file.unlink()
        log_path = WIKI_DIR / "log.md"
        with open(log_path, "a") as lf:
            lf.write(
                f"\n## [{datetime.now(timezone.utc).strftime('%Y-%m-%d')}] discarded | {fm.get('knowledge_type', 'unknown')}\n"
                f"- Discarded: {staged_file.stem} (id: {staged_id})\n"
            )
        return {"status": "discarded", "staged_id": staged_id}

    # Apply field-level edits
    if edits:
        for key, value in edits.items():
            fm[key] = value

    # Apply confirmed_links: replace fuzzy refs with canonical slug.
    # linked_nodes stores plain refs (no brackets); body has [[ref]] wikilinks.
    if confirmed_links:
        for fuzzy_ref, confirmed_iri in confirmed_links.items():
            _, _nt, slug_part = parse_iri(confirmed_iri)
            if slug_part:
                linked = fm.get("linked_nodes", [])
                # Update frontmatter list: plain ref → plain confirmed slug
                fm["linked_nodes"] = [slug_part if ref == fuzzy_ref else ref for ref in linked]
                # Update body: [[fuzzy_ref]] → [[confirmed-slug]]
                body_content = body_content.replace(f"[[{fuzzy_ref}]]", f"[[{slug_part}]]")

    # Remove staging-only fields
    for field in ["staged_at", "staged_by", "staged_id", "review_status", "proposed_edges",
                  "resolution_candidates", "connection_candidates", "suggested_sources", "priority"]:
        fm.pop(field, None)

    # Determine knowledge type and target folder
    knowledge_type = fm.get("knowledge_type") or fm.get("type") or "source"
    # Map paper/book/article/talk/video → source
    if knowledge_type in ("paper", "book", "article", "talk", "video"):
        fm["type"] = knowledge_type
        fm.pop("knowledge_type", None)
        knowledge_type = "source"

    folder = TYPE_TO_FOLDER.get(knowledge_type, "sources")
    target_dir = WIKI_DIR / folder
    target_dir.mkdir(parents=True, exist_ok=True)

    slug = staged_file.stem
    target_path = target_dir / f"{slug}.md"

    # Ensure IRI is set
    if "id" not in fm:
        fm["id"] = f"pkis:{knowledge_type}:{slug}"

    # Write promoted file
    new_post = frontmatter.Post(body_content, **fm)
    target_path.write_text(frontmatter.dumps(new_post))
    staged_file.unlink()

    # Invalidate node cache
    global _node_cache
    _node_cache = {}

    # Update index.md
    section_map = {
        "concept": "## Concepts", "technique": "## Techniques",
        "result": "## Results", "framework": "## Frameworks",
        "problem": "## Problems", "principle": "## Principles",
        "source": "## Sources", "hypothesis": "## Hypotheses",
        "research-cluster": "## Research Clusters", "asset": "## Assets",
        "bridge-note": "## Bridge Notes",
    }
    index_path = WIKI_DIR / "index.md"
    if index_path.exists():
        idx_content = index_path.read_text()
        node_domain = fm.get("domain", [])
        domain_str = ", ".join(node_domain) if isinstance(node_domain, list) else str(node_domain)
        now_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        new_entry = f"- [[{slug}]] — {fm.get('title', slug)} ({domain_str}) ({now_date})\n"
        section = section_map.get(knowledge_type, "## Sources")
        if section in idx_content:
            idx_content = idx_content.replace(section + "\n", section + "\n" + new_entry)
        else:
            idx_content += f"\n{section}\n{new_entry}"
        index_path.write_text(idx_content)

    # Append to log.md
    iri = fm.get("id", f"pkis:{knowledge_type}:{slug}")
    log_path = WIKI_DIR / "log.md"
    with open(log_path, "a") as lf:
        lf.write(
            f"\n## [{datetime.now(timezone.utc).strftime('%Y-%m-%d')}] committed | {knowledge_type}\n"
            f"- Committed: {slug} → {folder}/{slug}.md\n"
            f"- IRI: {iri}\n"
        )

    # Git commit and push
    git_sha = ""
    git_pushed = False
    try:
        repo_dir = str(REPO_DIR)
        files_to_add = [str(target_path), str(index_path), str(log_path)]
        subprocess.run(["git", "-C", repo_dir, "add"] + files_to_add, check=True, capture_output=True)
        result = subprocess.run(
            ["git", "-C", repo_dir, "commit", "-m",
             f"[mcp-commit] {knowledge_type}: {fm.get('title', slug)[:60]}"],
            check=True, capture_output=True, text=True
        )
        sha_match = re.search(r'\[.+? ([a-f0-9]{7,})\]', result.stdout)
        git_sha = sha_match.group(1) if sha_match else result.stdout.strip()[:12]
        logger.info(f"Git committed locally: {git_sha}")
        try:
            subprocess.run(["git", "-C", repo_dir, "push"], check=True, capture_output=True, timeout=30)
            git_pushed = True
            logger.info(f"Git pushed: {git_sha}")
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as push_err:
            logger.warning(f"Git push failed (local commit retained): {push_err}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Git commit failed: {e.stderr.decode() if isinstance(e.stderr, bytes) else e.stderr}")

    return {
        "status": "committed",
        "iri": iri,
        "git_commit": git_sha,
        "git_pushed": git_pushed,
        "url": f"https://github.com/choct155/pkis/blob/main/wiki/{folder}/{slug}.md",
    }


def tool_get_staged_nodes(
    node_type: str = None,
    staged_by: str = None,
    limit: int = 200
) -> list:
    """List all pending staged nodes awaiting review (all types — bridge notes, node stubs,
    source stubs). Default limit raised so source stubs aren't truncated behind newer bridge notes."""
    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    staged_files = sorted(STAGING_DIR.glob("*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
    for staged_file in staged_files:
        try:
            post = frontmatter.load(str(staged_file))
            fm = post.metadata
            if fm.get("staged_id") is None:
                continue
            effective_type = fm.get("knowledge_type") or fm.get("type") or "unknown"
            if node_type and effective_type != node_type:
                continue
            if staged_by and fm.get("staged_by") != staged_by:
                continue
            first_line = post.content.strip().split("\n")[0].lstrip("#").strip()[:200] if post.content.strip() else ""
            results.append({
                "staged_id": fm.get("staged_id"),
                "slug": staged_file.stem,
                "node_type": fm.get("knowledge_type") or fm.get("type") or "unknown",
                "staged_at": fm.get("staged_at", ""),
                "staged_by": fm.get("staged_by", ""),
                "title": fm.get("title", staged_file.stem),
                "review_status": fm.get("review_status", "pending"),
                "description": first_line,
                "review_url": f"https://github.com/choct155/pkis/blob/main/wiki/staging/{staged_file.name}",
            })
        except Exception as e:
            logger.error(f"Error reading staged file {staged_file}: {e}")
        if len(results) >= limit:
            break
    return results


# ============================================================
# Document store helpers
# ============================================================

ALLOWED_DOC_EXTENSIONS = {".pdf", ".epub", ".md", ".html", ".txt", ".docx"}


def _require_docs_auth(f):
    """
    Flask decorator: HTTP Basic Auth gated on DOCS_USERNAME / DOCS_PASSWORD env vars.
    If neither is set, the route is unprotected (dev/local mode).
    Applied to /docs/upload, /docs/list, and /docs/sources/<path>.
    /readwise/webhook is intentionally NOT wrapped — Readwise needs public access.
    """
    @wraps(f)
    def _decorated(*args, **kwargs):
        if not DOCS_USERNAME:
            return f(*args, **kwargs)   # no credentials configured — open
        import base64 as _b64
        auth = request.headers.get("Authorization", "")
        if auth.startswith("Basic "):
            try:
                decoded = _b64.b64decode(auth[6:]).decode("utf-8", errors="replace")
                username, _, password = decoded.partition(":")
                if username == DOCS_USERNAME and password == DOCS_PASSWORD:
                    return f(*args, **kwargs)
            except Exception:
                pass
        return Response(
            "Authentication required",
            401,
            {"WWW-Authenticate": 'Basic realm="PKIS Docs"'},
        )
    return _decorated


_SLUG_STOP_WORDS = {
    'a', 'an', 'the', 'to', 'of', 'in', 'on', 'at', 'for', 'with',
    'and', 'or', 'but', 'is', 'are', 'was', 'be', 'as', 'by', 'from',
    'into', 'via', 'its', 'this', 'that', 'some', 'how', 'why', 'when',
    'using', 'toward', 'towards', 'about', 'beyond', 'through',
}


def _compute_slug(title: str, authors: str, year) -> str:
    """
    Derive a slug from paper metadata: {last_name}-{key_title_word}-{year}.
    Skips stop-words and short words when picking the key title word so
    'A Conceptual Introduction…' → 'conceptual', not 'a'.
    Returns a collision-free slug (appends -2, -3, … if needed).
    """
    first_author = (authors or "").split(",")[0].strip()
    last_name = ""
    if first_author:
        last_name = re.sub(r"[^a-z0-9]", "", first_author.split()[-1].lower())

    words = re.sub(r"[^a-z0-9\s]", "", (title or "").lower()).split()
    key_words = [w for w in words if w not in _SLUG_STOP_WORDS and len(w) > 2]
    key_word  = key_words[0] if key_words else (words[0] if words else "source")

    year_str  = str(year) if year else ""
    parts     = [p for p in [last_name, key_word, year_str] if p]
    base      = "-".join(parts)[:55] or "source"

    slug, n = base, 1
    while find_node_path(slug) or (STAGING_DIR / f"{slug}.md").exists():
        slug = f"{base}-{n}"
        n   += 1
    return slug


def _arxiv_url_to_pdf_url(url_or_id: str) -> tuple[str, str]:
    """
    Given an arXiv URL (abs, pdf, html) or bare ID like '1701.02434',
    return (arxiv_id, pdf_fetch_url).
    Returns ('', '') if not recognised as arXiv.
    """
    # Bare ID pattern
    m = re.match(r'^(\d{4}\.\d{4,5})(v\d+)?$', url_or_id.strip())
    if m:
        return m.group(1), f"https://arxiv.org/pdf/{m.group(1)}"
    # URL pattern
    m = re.search(r'arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]+)(v\d+)?', url_or_id)
    if m:
        return m.group(1), f"https://arxiv.org/pdf/{m.group(1)}"
    return "", ""


def _is_file_url(url: str) -> bool:
    """True when the URL path ends with a storable file extension."""
    path = urllib.parse.urlparse(url).path.lower()
    return any(path.endswith(ext) for ext in ALLOWED_DOC_EXTENSIONS)


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


def _find_source_by_readwise_id(readwise_id: str) -> Optional[str]:
    """Find a source node's slug given its Readwise document ID."""
    if not readwise_id:
        return None
    for node in load_all_nodes():
        if node.get("node_type") == "sources":
            if node.get("frontmatter", {}).get("readwise_id") == readwise_id:
                return node["slug"]
    return None


def _update_source_frontmatter(slug: str, updates: dict) -> bool:
    """Apply field-level updates to a source node's frontmatter in place."""
    path = find_node_path(slug)
    if not path:
        return False
    try:
        post = frontmatter.load(str(path))
        for key, value in updates.items():
            post.metadata[key] = value
        path.write_text(frontmatter.dumps(post))
        global _node_cache
        _node_cache = {}
        return True
    except Exception as e:
        logger.error(f"Frontmatter update failed for {slug}: {e}")
        return False


def _git_commit_files(files: list, message: str) -> str:
    """Stage, commit, and push a list of file paths. Returns SHA or ''."""
    git_sha = ""
    try:
        subprocess.run(
            ["git", "-C", str(REPO_DIR), "add"] + [str(f) for f in files],
            check=True, capture_output=True
        )
        result = subprocess.run(
            ["git", "-C", str(REPO_DIR), "commit", "-m", message],
            check=True, capture_output=True, text=True
        )
        m = re.search(r'\[.+? ([a-f0-9]{7,})\]', result.stdout)
        git_sha = m.group(1) if m else result.stdout.strip()[:12]
        subprocess.run(
            ["git", "-C", str(REPO_DIR), "push"],
            check=True, capture_output=True, timeout=30
        )
    except Exception as e:
        logger.error(f"Git commit failed: {e}")
    return git_sha


def _append_reading_notes(source_slug: str, text: str, note: str,
                           highlight_id: str) -> Path:
    """
    Append an untagged highlight to a per-source reading-notes staging file.
    Creates the file if it doesn't exist.
    """
    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    notes_path = STAGING_DIR / f"{source_slug}-reading-notes.md"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if not notes_path.exists():
        fm = {
            "knowledge_type":  "reading-notes",
            "source":          source_slug,
            "staged_at":       ts,
            "staged_by":       "readwise-webhook",
            "review_status":   "pending",
        }
        notes_path.write_text(
            f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n"
            f"# Reading Notes — {source_slug}\n\n"
        )

    with open(notes_path, "a", encoding="utf-8") as f:
        f.write(f"\n## Highlight `{highlight_id[:8]}`\n")
        f.write(f"> {text}\n")
        if note:
            f.write(f"\n**Note:** {note}\n")
        f.write(f"\n*{ts}*\n")

    return notes_path


def _route_highlight(payload: dict, source_slug: str) -> dict:
    """
    Route a Readwise highlight based on its tags:
      #bridge      → staged bridge note
      #stub        → append to reading-notes with stub flag
      #concept:X   → append to reading-notes with concept tag
      (none)       → append to reading-notes for Librarian review
    """
    text         = (payload.get("text") or payload.get("content") or "").strip()
    note         = (payload.get("note") or "").strip()
    highlight_id = str(payload.get("id", ""))
    raw_tags     = payload.get("tags") or []
    tags         = [t["name"] if isinstance(t, dict) else str(t) for t in raw_tags]

    if not text:
        return {"action": "skipped", "reason": "empty highlight"}

    # ── #bridge → staged bridge note ─────────────────────────────────────
    if "bridge" in tags:
        rationale = note if note else text
        result = tool_create_bridge_note(
            rationale=rationale,
            title=text[:80] if note else "",
            source_context=source_slug,
            origin="reading",
        )
        return {"action": "bridge_note", "staged_id": result.get("staged_id")}

    # ── #stub → reading-notes with stub flag ─────────────────────────────
    if "stub" in tags:
        path = _append_reading_notes(source_slug, text, f"[STUB CANDIDATE] {note}", highlight_id)
        return {"action": "stub_candidate", "notes_file": path.name}

    # ── #concept:X → reading-notes with concept annotation ───────────────
    concept_tags = [t[len("concept:"):] for t in tags if t.startswith("concept:")]
    if concept_tags:
        path = _append_reading_notes(
            source_slug, text,
            f"[CONCEPT: {', '.join(concept_tags)}] {note}",
            highlight_id
        )
        return {"action": "concept_enrichment",
                "concepts": concept_tags, "notes_file": path.name}

    # ── default → reading-notes ───────────────────────────────────────────
    path = _append_reading_notes(source_slug, text, note, highlight_id)
    return {"action": "reading_note", "notes_file": path.name}


# ── Auto source node creation on upload ──────────────────────────────────────

def _arxiv_id_from_filename(filename: str) -> str:
    """
    Extract an arXiv ID from a filename like '1701.02434v2.pdf' or
    '2301.07041.pdf'.  Returns '' if no arXiv ID pattern is found.
    """
    stem = Path(filename).stem          # e.g. '1701.02434v2'
    m = re.match(r'^(\d{4}\.\d{4,5})(v\d+)?$', stem)
    return m.group(1) if m else ""


def _auto_create_source_node(slug: str, filename: str,
                              fetch_url: str = "") -> dict:
    """
    Create a live wiki/sources/{slug}.md entry automatically when a document
    is uploaded for an unknown slug.  Tries arXiv enrichment first (from the
    filename pattern); falls back to a bare stub.

    Returns the frontmatter dict of the newly created node so the caller can
    proceed with a Readwise push without reloading from disk.
    """
    now  = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")

    # ── Try metadata enrichment ───────────────────────────────────────────
    metadata: dict = {}
    source_url = ""

    arxiv_id = _arxiv_id_from_filename(filename)
    if not arxiv_id and fetch_url and "arxiv.org" in fetch_url:
        m = re.search(r'arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]+)', fetch_url)
        if m:
            arxiv_id = m.group(1)

    if arxiv_id:
        metadata   = _fetch_arxiv_metadata(arxiv_id)
        source_url = f"https://arxiv.org/abs/{arxiv_id}"

    title   = metadata.get("title")   or slug.replace("-", " ").title()
    authors = metadata.get("authors") or ""
    year    = metadata.get("year")
    abstract = metadata.get("abstract", "")

    doc_path = f"sources/{slug}/{filename}"

    # ── Build source file ─────────────────────────────────────────────────
    fm = {
        "id":          f"pkis:source:{slug}",
        "aliases":     [],
        "title":       title,
        "authors":     authors,
        "year":        year,
        "type":        metadata.get("source_type", "paper"),
        "domain":      [],
        "tags":        [],
        "source_url":  source_url,
        "drive_id":    "",
        "drive_path":  "",
        "doc_path":    doc_path,
        "readwise_id": "",
        "isbn":        "",
        "toc_source":  "",
        "parent_book": "",
        "chapter":     None,
        "status":      "unread",
        "date_added":  today,
        "date_read":   "",
        "concepts":    [],
    }
    body_summary = (abstract[:600] + "…") if len(abstract) > 600 else abstract
    body = (
        f"## Summary\n"
        f"{body_summary if body_summary else '[To be filled by Librarian ingest]'}\n\n"
        f"## Key Knowledge Objects\n[To be identified during Librarian ingest]\n\n"
        f"## Key Extractions\n[To be identified during Librarian ingest]\n\n"
        f"## Connection Candidates\n[To be identified during Librarian ingest]\n"
    )

    dest = WIKI_DIR / "sources" / f"{slug}.md"
    dest.write_text(
        f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n{body}"
    )

    # Invalidate node cache so subsequent lookups see the new node
    global _node_cache
    _node_cache = {}

    enrichment = "arxiv" if arxiv_id and metadata.get("title") else "minimal"
    logger.info(f"Auto-created source node {slug} (enrichment={enrichment})")
    return {**fm, "_enrichment": enrichment,
            "_arxiv_id": arxiv_id, "_abstract": abstract}


# ── Cross-store duplicate detection ──────────────────────────────────────────

def _find_duplicate_doc(file_bytes: bytes,
                        exclude_path: Path = None) -> Optional[tuple[str, str]]:
    """
    Scan every file in DOCS_DIR/sources/ for content identical to file_bytes.
    Uses file-size as a pre-filter so only same-size files are hashed.
    exclude_path: skip this exact path (allows same-slug/same-name overwrites
                  with different content — the annotated replacement workflow).
    Returns (slug, filename) of the first match, or None.
    """
    incoming_size = len(file_bytes)
    incoming_hash: str = ""           # computed lazily on first size match

    sources_dir = DOCS_DIR / "sources"
    if not sources_dir.exists():
        return None

    for slug_dir in sources_dir.iterdir():
        if not slug_dir.is_dir():
            continue
        for f in slug_dir.iterdir():
            if f.suffix.lower() not in ALLOWED_DOC_EXTENSIONS:
                continue
            if exclude_path and f.resolve() == exclude_path.resolve():
                continue
            try:
                if f.stat().st_size != incoming_size:
                    continue
                if not incoming_hash:
                    incoming_hash = hashlib.sha256(file_bytes).hexdigest()
                if hashlib.sha256(f.read_bytes()).hexdigest() == incoming_hash:
                    return (slug_dir.name, f.name)
            except OSError:
                continue
    return None


# ── MCP tool functions ────────────────────────────────────────────────────────

def tool_upload_document(
    slug: str,
    filename: str,
    fetch_url: str = "",
    content_b64: str = "",
    push_to_readwise: bool = True,
) -> dict:
    """
    Store a document in the doc store for a given source slug.
    Provide either fetch_url (VPS fetches the file) or content_b64 (base64 payload).
    Optionally pushes the served URL to Readwise Reader.

    Duplicate detection (content-hash):
    - Same content + different filename → rejected with name of existing file
    - Same filename + same content     → rejected as already uploaded (no-op)
    - Same filename + different content → allowed (annotated replacement workflow)
    """
    import base64 as _b64

    if not slug:
        raise ValueError("slug is required")
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_DOC_EXTENSIONS:
        raise ValueError(f"Extension {ext} not allowed. Permitted: {ALLOWED_DOC_EXTENSIONS}")

    # ── Fetch bytes into memory first (needed for hash check) ────────────────
    if fetch_url:
        req = urllib.request.Request(fetch_url, headers={"User-Agent": "PKIS/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            file_bytes = resp.read()
    elif content_b64:
        file_bytes = _b64.b64decode(content_b64)
    else:
        raise ValueError("Either fetch_url or content_b64 must be provided")

    # ── Cross-store duplicate check ───────────────────────────────────────────
    dest_dir  = DOCS_DIR / "sources" / slug
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / filename

    # exclude_path = dest_path so same-slug/same-name with NEW content is allowed
    # (annotated PDF replacing pristine copy)
    dup = _find_duplicate_doc(file_bytes, exclude_path=dest_path)
    if dup:
        dup_slug, dup_file = dup
        if dup_slug == slug:
            raise ValueError(
                f"Duplicate: identical content already stored as "
                f"'{dup_file}' under source '{slug}'. Upload rejected."
            )
        else:
            raise ValueError(
                f"Duplicate: identical content already stored as "
                f"'{dup_file}' under source '{dup_slug}'. Upload rejected."
            )

    # ── Write ────────────────────────────────────────────────────────────────
    dest_path.write_bytes(file_bytes)

    doc_url  = f"{DOCS_BASE_URL}/sources/{slug}/{filename}"
    doc_path = f"sources/{slug}/{filename}"

    # ── Ensure a wiki source node exists ────────────────────────────────────
    node_path = find_node_path(slug)
    auto_created = False
    if not node_path:
        auto_fm = _auto_create_source_node(slug, filename, fetch_url=fetch_url)
        node_path = find_node_path(slug)
        auto_created = True

    node    = load_node(node_path) if node_path else None
    title   = node["title"]                          if node else ""
    authors = node["frontmatter"].get("authors", "") if node else ""
    year    = node["frontmatter"].get("year")        if node else None

    # ── Resolve arXiv ID + abstract for enriched Readwise push ──────────────
    if auto_created:
        arxiv_id = auto_fm.get("_arxiv_id", "")
        abstract = auto_fm.get("_abstract", "")
    else:
        # Existing node — try to extract arXiv ID from source_url or filename
        arxiv_id = _arxiv_id_from_filename(filename)
        if not arxiv_id and node:
            src_url = node["frontmatter"].get("source_url", "")
            m = re.search(r'arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]+)', src_url)
            if m:
                arxiv_id = m.group(1)
        abstract = ""
        if arxiv_id:
            meta = _fetch_arxiv_metadata(arxiv_id)
            abstract = meta.get("abstract", "")

    # ── Readwise push ────────────────────────────────────────────────────────
    readwise_result = {}
    fm_updates: dict = {"doc_path": doc_path}
    if push_to_readwise and READWISE_TOKEN:
        readwise_result = _readwise_save(
            doc_url, title=title, author=authors, slug=slug,
            abstract=abstract, year=year, arxiv_id=arxiv_id,
        )
        if readwise_result.get("id"):
            fm_updates["readwise_id"] = readwise_result["id"]

    # ── Persist frontmatter + commit ─────────────────────────────────────────
    if node_path:
        _update_source_frontmatter(slug, fm_updates)
        _git_commit_files(
            [node_path],
            f"[doc-store] {'auto-create + ' if auto_created else ''}add doc: {slug}/{filename}"
        )

    # ── Auto-build reader (uploaded paper PDF) ───────────────────────────────
    _maybe_autobuild_reader(slug)

    return {
        "slug":              slug,
        "filename":          filename,
        "doc_url":           doc_url,
        "source_auto_created": auto_created,
        "readwise_pushed":   bool(readwise_result.get("id")),
        "readwise_url":      readwise_result.get("url", ""),
        "readwise_id":       readwise_result.get("id", ""),
    }


def tool_save_url_source(
    url: str,
    slug: str = "",
    push_to_readwise: bool = True,
) -> dict:
    """
    Save a URL-only source (article, blog, video, tweet, newsletter, etc.)
    to the wiki. No file is stored on the VPS — the URL is the canonical ref.

    Workflow:
      1. Detect Readwise category from URL pattern
      2. Fetch title / author via oEmbed (YouTube) or HTML meta tags
      3. Auto-compute slug from metadata if not provided
      4. Write wiki/sources/{slug}.md
      5. Push to Readwise Reader with the correct category
    """
    if not url:
        raise ValueError("url is required")

    category    = _detect_readwise_category(url)
    metadata    = _fetch_url_metadata(url)
    title       = metadata.get("title", "") or url
    author      = metadata.get("author", "")
    wiki_type   = _CATEGORY_TO_WIKI_TYPE.get(category, "article")

    # ── Slug ─────────────────────────────────────────────────────────────────
    if not slug:
        if title and title != url and author:
            slug = _compute_slug(title, author, None)
        elif title and title != url:
            # no author — use domain + key title word
            domain = re.sub(r'^www\.', '', urllib.parse.urlparse(url).netloc).split(".")[0]
            words  = re.sub(r"[^a-z0-9\s]", "", title.lower()).split()
            key    = next((w for w in words if w not in _SLUG_STOP_WORDS and len(w) > 2), words[0] if words else "source")
            base   = f"{domain}-{key}"[:55]
            slug   = base
            n = 1
            while find_node_path(slug) or (STAGING_DIR / f"{slug}.md").exists():
                slug = f"{base}-{n}"; n += 1
        else:
            # fall back to domain + path fragment
            parsed    = urllib.parse.urlparse(url)
            domain    = re.sub(r'^www\.', '', parsed.netloc).split(".")[0]
            path_frag = re.sub(r'[^a-z0-9]+', '-', parsed.path.lower()).strip('-')[:30]
            base      = f"{domain}-{path_frag}".strip('-')[:55] or "url-source"
            slug      = base
            n = 1
            while find_node_path(slug) or (STAGING_DIR / f"{slug}.md").exists():
                slug = f"{base}-{n}"; n += 1

    # ── Wiki node ─────────────────────────────────────────────────────────────
    now   = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")
    fm = {
        "id":          f"pkis:source:{slug}",
        "aliases":     [],
        "title":       title,
        "authors":     author,
        "year":        None,
        "type":        wiki_type,
        "domain":      [],
        "tags":        [],
        "source_url":  url,
        "drive_id":    "",
        "drive_path":  "",
        "doc_path":    "",          # URL-only: no local file
        "readwise_id": "",
        "isbn":        "",
        "toc_source":  "",
        "parent_book": "",
        "chapter":     None,
        "status":      "unread",
        "date_added":  today,
        "date_read":   "",
        "concepts":    [],
    }
    body = (
        "## Summary\n[To be filled by Librarian ingest]\n\n"
        "## Key Knowledge Objects\n[To be identified during Librarian ingest]\n\n"
        "## Key Extractions\n[To be identified during Librarian ingest]\n\n"
        "## Connection Candidates\n[To be identified during Librarian ingest]\n"
    )
    dest = WIKI_DIR / "sources" / f"{slug}.md"
    dest.write_text(
        f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n{body}"
    )
    global _node_cache
    _node_cache = {}

    # ── Readwise push ─────────────────────────────────────────────────────────
    readwise_result: dict = {}
    if push_to_readwise and READWISE_TOKEN:
        readwise_result = _readwise_save(
            doc_url=url, title=title, author=author,
            slug=slug, category=category,
        )
        if readwise_result.get("id"):
            _update_source_frontmatter(slug, {"readwise_id": readwise_result["id"]})

    # ── Git commit ────────────────────────────────────────────────────────────
    _git_commit_files([dest], f"[doc-store] save url source: {slug}")

    # ── Auto-build reader for papers (arXiv / PDF) ───────────────────────────
    _maybe_autobuild_reader(slug)

    return {
        "slug":            slug,
        "type":            wiki_type,
        "category":        category,
        "title":           title,
        "source_url":      url,
        "readwise_pushed": bool(readwise_result.get("id")),
        "readwise_url":    readwise_result.get("url", ""),
        "readwise_id":     readwise_result.get("id", ""),
    }


# ── Podcast transcript lookup pipeline ───────────────────────────────────────

_PODCAST_URL_PATTERNS = (
    "open.spotify.com/episode", "open.spotify.com/show",
    "podcasts.apple.com", "anchor.fm", "podcastaddict.com",
    "overcast.fm", "pocketcasts.com", "castro.fm", "castbox.fm",
    "stitcher.com", "iheart.com/podcast", "buzzsprout.com",
    "simplecast.com", "transistor.fm", "podbean.com", "spreaker.com",
    "acast.com", "blubrry.com", "libsyn.com",
)

# Podcast Index RSS namespace
_PI_NS = "https://podcastindex.org/namespace/1.0"


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


def _append_transcript_queue(entry: dict) -> None:
    """Append a podcast episode to wiki/transcript-queue.md for Whisper processing."""
    queue_path = WIKI_DIR / "transcript-queue.md"
    if not queue_path.exists():
        queue_path.write_text(
            "# Transcript Queue\n\n"
            "Episodes awaiting transcription. "
            "Run Whisper locally and save output to "
            "`raw/clippings/{slug}-transcript.md`.\n\n"
            "## Pending\n"
        )
    slug        = entry.get("slug", "")
    title       = entry.get("title", "")
    show        = entry.get("show", "")
    url         = entry.get("url", "")
    youtube_url = entry.get("youtube_url", "")
    ts          = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    lines = [f"\n### {slug} | pending"]
    if title:       lines.append(f"- **Episode**: {title}")
    if show:        lines.append(f"- **Show**: {show}")
    if url:         lines.append(f"- **URL**: {url}")
    if youtube_url: lines.append(f"- **YouTube**: {youtube_url}")
    lines.append(f"- **Added**: {ts}")

    with open(queue_path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def tool_get_transcript_queue() -> list:
    """List pending entries in the podcast transcript queue."""
    queue_path = WIKI_DIR / "transcript-queue.md"
    if not queue_path.exists():
        return []
    entries, current = [], {}
    for line in queue_path.read_text().split("\n"):
        m = re.match(r'^### (.+?) \| (.+)$', line)
        if m:
            if current.get("slug"):
                entries.append(current)
            current = {"slug": m.group(1).strip(), "status": m.group(2).strip()}
        elif line.startswith("- **Episode**: "):
            current["title"] = line[len("- **Episode**: "):].strip()
        elif line.startswith("- **Show**: "):
            current["show"] = line[len("- **Show**: "):].strip()
        elif line.startswith("- **URL**: "):
            current["url"] = line[len("- **URL**: "):].strip()
        elif line.startswith("- **YouTube**: "):
            current["youtube_url"] = line[len("- **YouTube**: "):].strip()
        elif line.startswith("- **Added**: "):
            current["added"] = line[len("- **Added**: "):].strip()
    if current.get("slug"):
        entries.append(current)
    return entries


def tool_save_podcast_source(
    url: str,
    push_to_readwise: bool = True,
) -> dict:
    """
    Save a podcast episode as a PKIS source with automatic transcript lookup.

    Resolution order:
      1. YouTube (if URL is YouTube)  → youtube-transcript-api
      2. Podcast Index API            → podcast:transcript in RSS feed
      3. Apple Podcasts RSS           → podcast:transcript in feed
    Falls back to Listen Notes + Podchaser for metadata enrichment, then
    adds episode to wiki/transcript-queue.md for Whisper processing.

    Env vars:
      PODCAST_INDEX_KEY / PODCAST_INDEX_SECRET  (api.podcastindex.org — free)
      LISTEN_NOTES_KEY                          (listennotes.com — free tier)
      PODCHASER_KEY                             (podchaser.com — free tier)
    """
    if not url:
        raise ValueError("url is required")

    now   = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")

    transcript_segments: list = []
    transcript_source:   str  = ""
    episode_meta:        dict = {}

    # ── Page metadata ────────────────────────────────────────────────────────
    page_meta   = _fetch_podcast_page_metadata(url)
    title       = page_meta.get("title", "")
    show        = page_meta.get("show", "")
    description = page_meta.get("description", "")

    is_youtube  = bool(_extract_youtube_id(url))
    youtube_url = url if is_youtube else ""

    # ── 1. YouTube ───────────────────────────────────────────────────────────
    if is_youtube:
        segs = _youtube_get_transcript(url)
        if segs:
            transcript_segments = segs
            transcript_source   = "youtube"
            episode_meta        = {"title": title, "show": show,
                                   "episode_url": url, "youtube_url": url}

    # ── 2. Podcast Index ─────────────────────────────────────────────────────
    if not transcript_segments:
        segs, pi_meta = _podcast_index_get_transcript(
            show_name=show, episode_title=title
        )
        if segs:
            transcript_segments = segs
            transcript_source   = "podcast-index"
            episode_meta        = pi_meta
        elif pi_meta.get("title") or pi_meta.get("show"):
            episode_meta = pi_meta
            if not title: title = pi_meta.get("title", "")
            if not show:  show  = pi_meta.get("show", "")

    # ── 3. Apple Podcasts RSS ─────────────────────────────────────────────────
    if not transcript_segments and (show or title):
        segs, ap_meta = _apple_podcasts_get_transcript(
            show_name=show, episode_title=title
        )
        if segs:
            transcript_segments = segs
            transcript_source   = "apple"
            episode_meta        = ap_meta

    # ── Metadata fallback (Listen Notes + Podchaser) ──────────────────────────
    if not transcript_segments:
        for fb in (_listen_notes_get_metadata(show, title),
                   _podchaser_get_metadata(show, title)):
            for k in ("title", "show", "description", "pub_date"):
                if fb.get(k) and not episode_meta.get(k):
                    episode_meta[k] = fb[k]

    # Final field resolution
    if not title:       title       = episode_meta.get("title", "") or url
    if not show:        show        = episode_meta.get("show", "")
    if not description: description = episode_meta.get("description", "")

    # ── Slug ──────────────────────────────────────────────────────────────────
    if show:
        slug = _compute_slug(title, show, None)
    elif title and title != url:
        words = re.sub(r"[^a-z0-9\s]", "", title.lower()).split()
        key   = next((w for w in words if w not in _SLUG_STOP_WORDS and len(w) > 2),
                     words[0] if words else "podcast")
        dom   = re.sub(r'^www\.', '', urllib.parse.urlparse(url).netloc).split(".")[0]
        base  = f"{dom}-{key}"[:55]
        slug, n = base, 1
        while find_node_path(slug) or (STAGING_DIR / f"{slug}.md").exists():
            slug = f"{base}-{n}"; n += 1
    else:
        parsed = urllib.parse.urlparse(url)
        dom    = re.sub(r'^www\.', '', parsed.netloc).split(".")[0]
        frag   = re.sub(r'[^a-z0-9]+', '-', parsed.path.lower()).strip('-')[:30]
        base   = f"{dom}-{frag}".strip('-')[:55] or "podcast"
        slug, n = base, 1
        while find_node_path(slug) or (STAGING_DIR / f"{slug}.md").exists():
            slug = f"{base}-{n}"; n += 1

    # ── Store transcript ──────────────────────────────────────────────────────
    doc_path_fm     = ""
    transcript_path = ""
    if transcript_segments:
        md = _segments_to_markdown(
            transcript_segments, title=title, show=show,
            source=transcript_source, episode_url=url,
        )
        clips_dir = RAW_DIR / "clippings"
        clips_dir.mkdir(parents=True, exist_ok=True)
        t_file = clips_dir / f"{slug}-transcript.md"
        t_file.write_text(md, encoding="utf-8")
        transcript_path = str(t_file)
        doc_path_fm     = f"clippings/{slug}-transcript.md"

    # ── Wiki source node ──────────────────────────────────────────────────────
    pub_date = episode_meta.get("pub_date", "")
    year     = None
    if pub_date:
        ym = re.search(r'\b(19|20)\d{2}\b', str(pub_date))
        if ym: year = int(ym.group(0))

    fm: dict = {
        "id":                f"pkis:source:{slug}",
        "aliases":           [],
        "title":             title,
        "authors":           show,
        "year":              year,
        "type":              "talk",
        "domain":            [],
        "tags":              [],
        "source_url":        url,
        "drive_id":          "",
        "drive_path":        "",
        "doc_path":          doc_path_fm,
        "readwise_id":       "",
        "isbn":              "",
        "toc_source":        "",
        "parent_book":       "",
        "chapter":           None,
        "status":            "unread",
        "date_added":        today,
        "date_read":         "",
        "concepts":          [],
        "transcript_status": "found" if transcript_segments else "queued",
        "transcript_source": transcript_source,
    }
    if youtube_url and youtube_url != url:
        fm["youtube_url"] = youtube_url

    body = (
        f"## Summary\n{description[:500] if description else '[To be filled by Librarian ingest]'}\n\n"
        "## Key Knowledge Objects\n[To be identified during Librarian ingest]\n\n"
        "## Key Extractions\n[To be identified during Librarian ingest]\n\n"
        "## Connection Candidates\n[To be identified during Librarian ingest]\n"
    )
    dest = WIKI_DIR / "sources" / f"{slug}.md"
    dest.write_text(
        f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True)}---\n\n{body}"
    )
    global _node_cache
    _node_cache = {}

    # ── Whisper queue if no transcript ────────────────────────────────────────
    if not transcript_segments:
        _append_transcript_queue({
            "slug":        slug,
            "title":       title,
            "show":        show,
            "url":         url,
            "youtube_url": youtube_url,
        })

    # ── Readwise push ─────────────────────────────────────────────────────────
    readwise_result: dict = {}
    if push_to_readwise and READWISE_TOKEN:
        html_content = (
            _segments_to_html(transcript_segments, title=title)
            if transcript_segments else ""
        )
        readwise_result = _readwise_save(
            doc_url=url, title=title, author=show, slug=slug,
            category="article",
            abstract=description[:600] if description else "",
            year=year,
            html=html_content,
        )
        if readwise_result.get("id"):
            _update_source_frontmatter(slug, {"readwise_id": readwise_result["id"]})

    # ── Git commit ────────────────────────────────────────────────────────────
    files_to_commit = [dest]
    if transcript_path:
        files_to_commit.append(Path(transcript_path))
    q_path = WIKI_DIR / "transcript-queue.md"
    if not transcript_segments and q_path.exists():
        files_to_commit.append(q_path)
    _git_commit_files(files_to_commit, f"[podcast] save episode: {slug}")

    return {
        "slug":                slug,
        "type":                "talk",
        "title":               title,
        "show":                show,
        "source_url":          url,
        "transcript_found":    bool(transcript_segments),
        "transcript_source":   transcript_source,
        "transcript_segments": len(transcript_segments),
        "transcript_queued":   not bool(transcript_segments),
        "readwise_pushed":     bool(readwise_result.get("id")),
        "readwise_url":        readwise_result.get("url", ""),
        "readwise_id":         readwise_result.get("id", ""),
    }


def tool_list_documents(slug: str = None) -> list:
    """List stored documents, optionally filtered to a single source slug."""
    sources_dir = DOCS_DIR / "sources"
    if not sources_dir.exists():
        return []
    results = []
    search_dirs = [sources_dir / slug] if slug else sorted(sources_dir.iterdir())
    for d in search_dirs:
        if not d.is_dir():
            continue
        for f in sorted(d.iterdir()):
            if f.suffix.lower() in ALLOWED_DOC_EXTENSIONS:
                results.append({
                    "slug":     d.name,
                    "filename": f.name,
                    "url":      f"{DOCS_BASE_URL}/sources/{d.name}/{f.name}",
                    "size_kb":  round(f.stat().st_size / 1024, 1),
                    "modified": datetime.fromtimestamp(
                        f.stat().st_mtime, tz=timezone.utc
                    ).strftime("%Y-%m-%dT%H:%M:%SZ"),
                })
    return results


# ============================================================
# Flask routes — Document store + Readwise webhook
# ============================================================

_UPLOAD_FORM = """<!DOCTYPE html>
<html><head>
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>PKIS Upload</title>
<style>
  body {{ font-family: system-ui, sans-serif; max-width: 520px;
          margin: 40px auto; padding: 0 16px; }}
  label {{ display: block; margin: 12px 0 4px; font-weight: 600; }}
  input {{ width: 100%; padding: 8px; box-sizing: border-box;
           font-size: 16px; border: 1px solid #ccc; border-radius: 4px; }}
  .hint {{ font-size: 13px; color: #666; margin: 2px 0 0; }}
  .divider {{ text-align: center; color: #999; margin: 16px 0 4px;
              font-size: 13px; font-style: italic; }}
  button {{ margin-top: 16px; width: 100%; padding: 12px;
            background: #1a56db; color: white; border: none;
            border-radius: 4px; font-size: 16px; cursor: pointer; }}
  .msg {{ margin-top: 16px; padding: 12px; border-radius: 4px; }}
  .ok  {{ background: #d1fae5; color: #065f46; }}
  .err {{ background: #fee2e2; color: #991b1b; }}
</style></head><body>
<h2>PKIS Doc Upload</h2>
{msg}
<form method="POST" enctype="multipart/form-data">
  <label>URL <span style="font-weight:400">(arXiv, article, podcast, video, etc. — optional)</span></label>
  <input name="source_url" placeholder="https://arxiv.org/abs/1701.02434  ·  Spotify/Apple episode  ·  blog post"
         value="{source_url}" autocomplete="off">
  <p class="hint">arXiv → PDF fetched + HTML in Reader. Podcast platforms (Spotify, Apple, etc.) → transcript lookup + Whisper queue if needed. Articles/videos → URL saved.</p>

  <div class="divider">— or attach a file —</div>

  <label>File <span style="font-weight:400">(optional when URL given)</span></label>
  <input type="file" name="file" accept=".pdf,.epub,.md,.html,.txt,.docx">

  <label>Slug <span style="font-weight:400">(leave blank to auto-compute)</span></label>
  <input name="slug" placeholder="auto-computed from metadata" value="{slug}"
         autocomplete="off">
  <p class="hint">Override only if you want a specific identifier, e.g. betancourt-hmc.</p>

  <label style="margin-top:14px">
    <input type="checkbox" name="push_readwise" value="1" {rw_checked}>
    Push to Readwise Reader
  </label>
  <button type="submit" id="submitBtn">Upload</button>
</form>
<script>
document.getElementById('submitBtn').addEventListener('click', function() {{
  var f = this.form;
  var hasInput = f.source_url.value.trim() || f.file.files.length > 0;
  if (hasInput) {{
    var btn = this;
    // defer so the click event + form submit fire before the button is disabled
    setTimeout(function() {{ btn.disabled = true; btn.textContent = 'Uploading…'; }}, 0);
  }}
}});
</script>
</body></html>"""


@app.route("/docs/upload", methods=["GET", "POST"])
@_require_docs_auth
def docs_upload():
    """HTML upload form — protected by HTTP Basic Auth (DOCS_USERNAME/DOCS_PASSWORD)."""
    msg        = ""
    slug_val   = ""
    src_url_val = ""
    rw_checked = "checked" if READWISE_TOKEN else ""

    if request.method == "POST":
        slug_val    = request.form.get("slug", "").strip()
        src_url_val = request.form.get("source_url", "").strip()
        push_rw     = bool(request.form.get("push_readwise"))
        file        = request.files.get("file")
        has_file    = bool(file and file.filename)

        if not src_url_val and not has_file:
            msg = '<div class="msg err">Provide a URL or a file (or both).</div>'
        else:
            try:
                # ── Resolve fetch_url and filename ───────────────────────────
                fetch_url = ""
                filename  = ""

                if src_url_val:
                    arxiv_id, pdf_url = _arxiv_url_to_pdf_url(src_url_val)
                    if pdf_url:
                        # arXiv → fetch PDF from arXiv
                        fetch_url = pdf_url
                        filename  = f"{arxiv_id}.pdf"
                    elif _is_file_url(src_url_val):
                        # Direct file URL (PDF, EPUB, …)
                        fetch_url = src_url_val
                        filename  = Path(urllib.parse.urlparse(src_url_val).path).name
                    elif not has_file:
                        # Podcast episode → transcript lookup pipeline
                        if _is_podcast_url(src_url_val):
                            result = tool_save_podcast_source(
                                url=src_url_val,
                                push_to_readwise=push_rw and bool(READWISE_TOKEN),
                            )
                            t_note = (" · transcript found"
                                      if result.get("transcript_found")
                                      else " · queued for Whisper")
                            rw_note = (f" · <a href='{result['readwise_url']}'>Open in Reader</a>"
                                       if result.get("readwise_url") else "")
                            msg = (f'<div class="msg ok">Podcast saved as '
                                   f'<strong>{result["slug"]}</strong>: '
                                   f'{result.get("title","")[:60] or src_url_val[:60]}'
                                   f'{t_note}{rw_note}</div>')
                            slug_val = src_url_val = ""
                            return _UPLOAD_FORM.format(
                                msg=msg, slug=slug_val,
                                source_url=src_url_val, rw_checked=rw_checked
                            )
                        # URL-only source — article, video, tweet, etc.
                        result = tool_save_url_source(
                            url=src_url_val,
                            slug=slug_val or "",
                            push_to_readwise=push_rw and bool(READWISE_TOKEN),
                        )
                        cat_label = result["category"].capitalize()
                        rw_note   = (f" · <a href='{result['readwise_url']}'>Open in Reader</a>"
                                     if result.get("readwise_url") else "")
                        msg = (f'<div class="msg ok">{cat_label} saved as '
                               f'<strong>{result["slug"]}</strong>: '
                               f'{result.get("title","")[:60] or src_url_val[:60]}'
                               f'{rw_note}</div>')
                        slug_val = src_url_val = ""
                        return _UPLOAD_FORM.format(
                            msg=msg, slug=slug_val,
                            source_url=src_url_val, rw_checked=rw_checked
                        )

                # File takes priority over URL-derived filename if both given
                content_b64 = ""
                if has_file:
                    import base64 as _b64
                    content_b64 = _b64.b64encode(file.read()).decode()
                    filename    = Path(file.filename).name
                    fetch_url   = ""   # don't double-fetch

                if not filename:
                    raise ValueError("Could not determine filename.")

                # ── Auto-compute slug if not provided ────────────────────────
                if not slug_val:
                    # Try arXiv metadata first
                    arxiv_id_for_slug, _ = _arxiv_url_to_pdf_url(src_url_val) if src_url_val else ("", "")
                    if not arxiv_id_for_slug:
                        arxiv_id_for_slug = _arxiv_id_from_filename(filename)
                    if arxiv_id_for_slug:
                        meta = _fetch_arxiv_metadata(arxiv_id_for_slug)
                        slug_val = _compute_slug(
                            meta.get("title", ""), meta.get("authors", ""), meta.get("year")
                        )
                    else:
                        # Fallback: clean filename stem
                        stem = re.sub(r'[^a-z0-9]+', '-', Path(filename).stem.lower()).strip('-')
                        slug_val = stem[:55] or "source"

                result = tool_upload_document(
                    slug=slug_val,
                    filename=filename,
                    fetch_url=fetch_url,
                    content_b64=content_b64,
                    push_to_readwise=push_rw and bool(READWISE_TOKEN),
                )
                rw_note  = (f" · <a href='{result['readwise_url']}'>Open in Reader</a>"
                            if result.get("readwise_url") else "")
                new_node = " · wiki node created" if result.get("source_auto_created") else ""
                msg = (f'<div class="msg ok">Stored as <strong>{result["slug"]}</strong>: '
                       f'<a href="{result["doc_url"]}">{filename}</a>{rw_note}{new_node}</div>')
                slug_val = src_url_val = ""
            except Exception as e:
                msg = f'<div class="msg err">Error: {e}</div>'

    return _UPLOAD_FORM.format(
        msg=msg, slug=slug_val, source_url=src_url_val, rw_checked=rw_checked
    )


@app.route("/docs/list", methods=["GET"])
@_require_docs_auth
def docs_list():
    """JSON listing of stored documents — protected by Basic Auth."""
    slug = request.args.get("slug")
    return jsonify(tool_list_documents(slug))


@app.route("/docs/sources/<path:filepath>")
def docs_serve(filepath: str):
    """
    Serve files from the document store (NO auth — Readwise must be able to fetch).
    URL pattern: /docs/sources/<slug>/<filename>
    Maps to DOCS_DIR/sources/<slug>/<filename> on disk.

    The management endpoints (/docs/upload, /docs/list) are auth-protected;
    the file URLs themselves are public-but-opaque (slug + filename required).
    If we ever need stronger file security, replace with a signed-token scheme.

    send_from_directory handles path-traversal protection automatically.
    """
    sources_dir = DOCS_DIR / "sources"
    return send_from_directory(str(sources_dir), filepath)


# ── Readwise webhook ──────────────────────────────────────────────────────────

@app.route("/readwise/webhook", methods=["POST"])
def readwise_webhook():
    """
    Receive Readwise webhook events and route them:

    reader.document.finished / .archived
      → update source status: read + date_read + git commit

    readwise.highlight.created
      → route by highlight tags (#bridge / #stub / #concept:X / default)
    """
    # force=True: parse regardless of Content-Type header
    # silent=True: return None instead of raising on bad/empty body
    payload = request.get_json(force=True, silent=True) or {}

    # Verify shared secret (Readwise includes it in the payload body)
    if READWISE_WEBHOOK_SECRET:
        if payload.get("secret") != READWISE_WEBHOOK_SECRET:
            logger.warning("Readwise webhook: invalid secret")
            return jsonify({"error": "invalid secret"}), 401

    event_type = payload.get("event_type", "")
    logger.info(f"Readwise webhook: {event_type}")

    # ── document finished / archived → mark read ─────────────────────────
    if event_type in ("reader.document.finished", "reader.document.archived"):
        doc_id   = payload.get("id", "")
        # Try readwise_id lookup first, fall back to pkis tag in document tags
        slug = _find_source_by_readwise_id(doc_id)
        if not slug:
            for tag in (payload.get("tags") or []):
                name = tag["name"] if isinstance(tag, dict) else str(tag)
                if name.startswith("pkis:source:"):
                    slug = name[len("pkis:source:"):]
                    break

        if slug:
            date_read = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            if _update_source_frontmatter(slug, {"status": "read", "date_read": date_read}):
                source_path = find_node_path(slug)
                if source_path:
                    sha = _git_commit_files(
                        [source_path],
                        f"[readwise] mark read: {slug}"
                    )
                    logger.info(f"Marked {slug} read (commit {sha})")
                return jsonify({"status": "marked_read", "slug": slug})
        else:
            logger.warning(f"Readwise webhook: no PKIS source found for id={doc_id}")
        return jsonify({"status": "no_match"})

    # ── highlight created → route by tags ────────────────────────────────
    if event_type == "readwise.highlight.created":
        book_id = payload.get("book_id", "")
        slug    = _find_source_by_readwise_id(book_id)
        if not slug:
            # Fall back: check if source slug is in the document URL
            logger.warning(f"Readwise webhook: no source for book_id={book_id}")
            return jsonify({"status": "no_source_match"})

        result = _route_highlight(payload, slug)
        logger.info(f"Highlight routed: {result.get('action')} for {slug}")
        return jsonify({"status": "ok", "route": result})

    # ── other events — log and acknowledge ───────────────────────────────
    logger.info(f"Readwise webhook: unhandled event {event_type!r}")
    return jsonify({"status": "acknowledged", "event_type": event_type})


# ============================================================
# Flask routes — MCP HTTP transport
# ============================================================

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "wiki_dir": str(WIKI_DIR)})


@app.route("/refresh", methods=["POST"])
def refresh():
    """Called by git webhook or cron to invalidate caches."""
    refresh_caches()
    return jsonify({"status": "refreshed"})


def _jsonrpc_error(req_id, code: int, message: str):
    """Build a JSON-RPC 2.0 error response body."""
    return jsonify({
        "jsonrpc": JSONRPC_VERSION,
        "id": req_id,
        "error": {"code": code, "message": message}
    })


def _jsonrpc_result(req_id, result):
    """Build a JSON-RPC 2.0 success response body."""
    return jsonify({
        "jsonrpc": JSONRPC_VERSION,
        "id": req_id,
        "result": result
    })


def tool_get_write_schema() -> dict:
    """Describe the writable structure of the wiki so clients can compose valid
    writes without guessing: knowledge types, edge predicates (+ definitions),
    node frontmatter fields, and the parameter spec for each write tool."""
    return {
        "knowledge_types": {
            "concept": "An idea/object of study (definition-bearing).",
            "technique": "A method or algorithm.",
            "result": "A theorem, empirical finding, or established result.",
            "framework": "An organizing structure spanning techniques/concepts.",
            "problem": "An open or canonical problem.",
            "principle": "A guiding rule or invariant.",
        },
        "special_node_types": {
            "source": "Paper/book/chapter — create_source_stub (auto-enriched, staged).",
            "hypothesis": "Research-program hypothesis — create_hypothesis.",
            "bridge-note": "Cross-node insight linking >=2 nodes — create_bridge_note.",
        },
        "edge_predicates": dict(EDGE_WEIGHTS),
        "edge_predicate_definitions": {
            "prerequisite-of": "subject must be understood before target",
            "uses": "subject employs target as a component/tool",
            "specializes": "subject is a special case of target",
            "generalizes": "subject is a generalization of target",
            "extends": "subject builds on / extends target",
            "applies": "subject applies target to a domain",
            "instantiates": "subject is a concrete instance of target",
            "contrasts-with": "subject is meaningfully opposed/compared to target",
            "analogous-to": "subject is structurally analogous to target (same structure, different mechanism/domain)",
        },
        "node_frontmatter_fields": {
            "title": "str (required)",
            "knowledge_type": "one of knowledge_types",
            "aliases": "list[str]",
            "also_type": "list[str] secondary knowledge types",
            "domain": "list[str] domain tags",
            "tags": "list[str] free tags",
            "sources": "list[str] source IRIs/slugs backing the node",
            "related_concepts": "list of [[wikilinks]]",
            "maturity": "stub | evolving | settled",
            "coverage": "int curation metric",
            "understanding": "int self-assessed",
            "component_scores": "anatomy dict: operational_mechanism, principled_mechanism, conditions, implementation, diagnostics, alternatives, failure_modes",
            "needs_canonical_source": "bool (set when sourceless)",
        },
        "write_tools": {
            "create_node_stub": {
                "creates": "staged knowledge node",
                "required": ["knowledge_type", "title"],
                "optional": ["slug", "definition", "domain", "tags", "aliases", "also_type", "sources", "suggest_sources"],
                "notes": "No edges param — use add_connections after commit. Stages; promote with commit_staged_node.",
            },
            "create_source_stub": {
                "creates": "staged source node, metadata auto-enriched (CrossRef/arXiv/Semantic Scholar)",
                "optional": ["title", "authors", "url", "year", "doi", "notes", "priority"],
                "notes": "Slug auto-derived. domain/tags/summary are NOT params — set via edit_node after commit.",
            },
            "create_hypothesis": {
                "creates": "staged hypothesis node",
                "required": ["title"],
                "optional": ["slug", "domain", "tags", "formal_statement", "motivation", "current_evidence", "open_questions", "aliases", "cluster", "role", "dependent_nodes"],
                "notes": "No connections param — use add_connections after commit.",
            },
            "create_bridge_note": {
                "creates": "staged bridge note linking >=2 nodes",
                "required": ["rationale"],
                "optional": ["title", "linked_node_refs", "origin", "proposed_edge_type", "source_context"],
                "notes": "Takes linked_node_refs (IRIs or fuzzy refs); NOT domain/tags.",
            },
            "edit_node": {
                "edits": "a LIVE node's frontmatter and/or body sections (commits+pushes)",
                "optional": ["iri", "slug", "frontmatter_updates", "section_updates", "commit_message"],
                "notes": "frontmatter_updates merges {field:value} (null deletes). section_updates replaces a '## Section' body (appends if absent).",
            },
            "add_connections": {
                "adds": "typed graph edges between LIVE nodes (batch)",
                "required": ["edges"],
                "edge_shape": {"subject": "IRI/slug", "target": "IRI/slug (must be live)", "predicate": "one of edge_predicates", "note": "optional rationale"},
                "notes": "Idempotent per (subject,predicate,target).",
            },
            "add_to_queue": {
                "adds": "a source/reference to the reading queue",
                "optional": ["source_iri", "reference", "priority", "reason"],
                "notes": "priority is 'high' or 'normal'.",
            },
        },
        "two_phase_write": "create_* tools STAGE (review via get_staged_nodes, promote via commit_staged_node). edit_node and add_connections write LIVE immediately.",
    }


def _get_tools_list():
    """Return the canonical tools list used by both tools/list and the manifest."""
    return [
        {
            "name": "get_write_schema",
            "description": "Describe the writable structure of the wiki — knowledge types, edge predicates (with definitions), node frontmatter fields, and the parameter spec for every write tool. Call this BEFORE composing writes so node/edge structure is correct by construction.",
            "inputSchema": {"type": "object", "properties": {}},
        },
        {
            "name": "search_wiki",
            "description": "Search the PKIS wiki using hybrid keyword and structural search. Call this FIRST for any question touching the user's learning domains. Returns ranked concept and source nodes.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "domains": {"type": "array", "items": {"type": "string"}},
                    "node_types": {"type": "array", "items": {"type": "string"}},
                    "max_results": {"type": "integer", "default": 10}
                },
                "required": ["query"]
            }
        },
        {
            "name": "get_node",
            "description": "Retrieve full content of a specific PKIS wiki node by IRI. Use after search_wiki or resolve_concept to get full detail.",
            "inputSchema": {
                "type": "object",
                "properties": {"iri": {"type": "string"}},
                "required": ["iri"]
            }
        },
        {
            "name": "resolve_concept",
            "description": "Resolve a concept name, abbreviation, or alias to its canonical PKIS IRI. Use when the user mentions a concept by name.",
            "inputSchema": {
                "type": "object",
                "properties": {"surface_form": {"type": "string"}},
                "required": ["surface_form"]
            }
        },
        {
            "name": "detect_concepts",
            "description": "Detect which PKIS concepts are present in arbitrary text, even when not explicitly named. Use for implicit concept instantiation.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"},
                    "threshold": {"type": "number", "default": 0.7}
                },
                "required": ["text"]
            }
        },
        {
            "name": "get_related",
            "description": "Get structurally connected nodes via typed relationship edges. Use to explore concept dependencies and connections.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "iri": {"type": "string"},
                    "edge_types": {"type": "array", "items": {"type": "string"}},
                    "direction": {"type": "string", "enum": ["inbound", "outbound", "both"]},
                    "max_hops": {"type": "integer", "default": 2}
                },
                "required": ["iri"]
            }
        },
        {
            "name": "add_to_queue",
            "description": "Add a source or reference to the reading queue. Use when the user wants to note something for later ingestion.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "source_iri": {"type": "string"},
                    "reference": {"type": "string"},
                    "reason": {"type": "string"},
                    "priority": {"type": "string", "enum": ["high", "normal"]}
                }
            }
        },
        {
            "name": "get_reading_queue",
            "description": "Get the current reading queue contents.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "priority": {"type": "string", "enum": ["high", "normal"]}
                }
            }
        },
        {
            "name": "get_concept_frontier",
            "description": "Get the concepts that most need attention. Priority blends centrality (inbound refs), coverage/understanding gaps, and proximity to active research-cluster frontier hypotheses (so reading follows the research agenda). Returns {params, results}: params reports the effective cluster_proximity_weight and its source (call-override / config-default / built-in-default). Pass cluster_proximity_weight to override the weight for THIS call only.",
            "inputSchema": {"type": "object", "properties": {
                "cluster_proximity_weight": {"type": "number", "description": "Override the cluster-proximity weight for THIS call only; if omitted, the persisted default or built-in 2.0 is used"}
            }}
        },
        {
            "name": "set_priority_config",
            "description": "Set, reset, or report the DEFAULT cluster-proximity weight used by get_concept_frontier for every call without an explicit override. reset=true restores the built-in default (2.0); cluster_proximity_weight=<n> persists <n> as the new default for all calls; passing neither reports the current default. Persisted to a config file (survives restarts, shared across workers). Returns the resulting weight and its source.",
            "inputSchema": {"type": "object", "properties": {
                "cluster_proximity_weight": {"type": "number", "description": "New default weight to persist for all calls"},
                "reset": {"type": "boolean", "default": False, "description": "Restore the built-in default (2.0) by removing the persisted config"}
            }}
        },
        {
            "name": "get_health_metrics",
            "description": "Get summary health statistics for the wiki.",
            "inputSchema": {"type": "object", "properties": {}}
        },
        {
            "name": "get_sourceless_stubs",
            "description": "List live knowledge nodes flagged needs_canonical_source — stubs created before a canonical source was attached. Each carries any reference suggestions captured at creation so a source can be found and attached.",
            "inputSchema": {"type": "object", "properties": {}}
        },
        {
            "name": "get_reading_graph",
            "description": "Return the source dependency graph — nodes are sources, edges encode conceptual overlap and inferred prerequisite order. Use to answer: what should I read first? what is load-bearing? what does reading X unlock? Supports scoping to queue items, all unread, or the full corpus; can focus on a concept or domain.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "scope": {
                        "type": "string",
                        "enum": ["queue_only", "all_unread", "full"],
                        "default": "all_unread",
                        "description": "queue_only: 70 actively tracked sources; all_unread: full unread corpus; full: everything"
                    },
                    "focus_concept": {
                        "type": "string",
                        "description": "Concept slug — return subgraph of sources covering this concept plus 1-hop neighbours"
                    },
                    "focus_domain": {
                        "type": "string",
                        "description": "Domain tag (e.g. 'knowledge-representation') — restrict to sources in that domain"
                    },
                    "min_edge_weight": {
                        "type": "integer",
                        "default": 2,
                        "description": "Minimum shared concepts to show an edge. Higher = sparser, more confident connections"
                    },
                    "max_nodes": {
                        "type": "integer",
                        "default": 100,
                        "description": "Cap on nodes returned (highest load-bearing first)"
                    }
                }
            }
        },
        {
            "name": "get_staged_nodes",
            "description": "List all staged nodes awaiting review. Use to check what's pending in the two-phase write queue.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "node_type": {"type": "string"},
                    "staged_by": {"type": "string"},
                    "limit": {"type": "integer", "default": 20}
                }
            }
        },
        {
            "name": "create_bridge_note",
            "description": "Capture an epiphany or cross-domain connection. Creates a staged bridge note for later review. Accepts fuzzy node references — they are resolved to candidates automatically.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "rationale": {"type": "string", "description": "The insight or connection being captured"},
                    "title": {"type": "string", "description": "Short title for the bridge note (auto-generated from linked nodes if omitted)"},
                    "source_context": {"type": "string", "description": "Fuzzy reference to what prompted this"},
                    "linked_node_refs": {"type": "array", "items": {"type": "string"}, "description": "Node IRIs or fuzzy text references"},
                    "proposed_edge_type": {"type": "string", "description": "One of the 8 relationship predicates"},
                    "origin": {"type": "string", "enum": ["voice-capture", "conversation", "reading", "spontaneous"], "default": "conversation"}
                },
                "required": ["rationale"]
            }
        },
        {
            "name": "create_source_stub",
            "description": "Register a new source from any identifying fragment. Enriches metadata from arXiv, CrossRef, or Semantic Scholar. Creates a staged stub for Librarian review.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "url": {"type": "string", "description": "arXiv URL, DOI URL, blog URL, etc."},
                    "doi": {"type": "string"},
                    "authors": {"type": "string"},
                    "year": {"type": "integer"},
                    "notes": {"type": "string"},
                    "priority": {"type": "string", "enum": ["high", "normal"], "default": "normal"}
                }
            }
        },
        {
            "name": "create_node_stub",
            "description": "Create a knowledge-node stub (concept, technique, result, framework, problem, or principle) BEFORE a canonical source exists. If no source is supplied, the node is flagged needs_canonical_source and reference suggestions are gathered from the corpus and Semantic Scholar. Creates a staged stub for review.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "knowledge_type": {"type": "string", "enum": ["concept", "technique", "result", "framework", "problem", "principle"]},
                    "title": {"type": "string"},
                    "definition": {"type": "string", "description": "Body text for the node's Definition section"},
                    "domain": {"type": "array", "items": {"type": "string"}},
                    "tags": {"type": "array", "items": {"type": "string"}},
                    "aliases": {"type": "array", "items": {"type": "string"}},
                    "also_type": {"type": "array", "items": {"type": "string"}, "description": "Secondary knowledge types"},
                    "sources": {"type": "array", "items": {"type": "string"}, "description": "Source slugs or IRIs backing this node; omit to flag needs_canonical_source"},
                    "slug": {"type": "string", "description": "Optional explicit slug; derived from title if omitted"},
                    "suggest_sources": {"type": "boolean", "default": True, "description": "When sourceless, gather reference suggestions from corpus + Semantic Scholar"}
                },
                "required": ["knowledge_type", "title"]
            }
        },
        {
            "name": "create_hypothesis",
            "description": "Stage a hypothesis node — the research-program knowledge type create_node_stub does not cover. Creates standard hypothesis frontmatter (status, research_program_cluster/role, cluster_membership, dependent_nodes) plus body sections (Formal Statement, Motivation, Current Evidence, Open Questions, Connections). Promote with commit_staged_node; lands in wiki/hypotheses/.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "cluster": {"type": "string", "description": "Research-cluster slug or IRI this hypothesis belongs to (e.g. intensional-grounding)"},
                    "role": {"type": "string", "description": "research_program_role, e.g. direct-test, boundary-condition, generalization-test, scaling-foil", "default": "direct-test"},
                    "domain": {"type": "array", "items": {"type": "string"}},
                    "tags": {"type": "array", "items": {"type": "string"}},
                    "formal_statement": {"type": "string", "description": "Body for the Formal Statement section"},
                    "motivation": {"type": "string"},
                    "current_evidence": {"type": "string"},
                    "open_questions": {"type": "string"},
                    "dependent_nodes": {"type": "array", "items": {"type": "object"}, "description": "List of {node, node_type, rationale} dependency descriptors"},
                    "aliases": {"type": "array", "items": {"type": "string"}},
                    "slug": {"type": "string", "description": "Optional explicit slug; derived from title if omitted"}
                },
                "required": ["title"]
            }
        },
        {
            "name": "edit_node",
            "description": "Edit a LIVE node's frontmatter fields and/or named body sections, then commit + push. frontmatter_updates merges {field: value} into frontmatter (null value deletes a field); section_updates replaces the body under each `## Section Title` (or appends the section if absent). Covers what add_connections cannot — e.g. setting a cluster's frontier_hypotheses and rewriting its Current Frontier. date_updated is bumped automatically.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "iri": {"type": "string", "description": "IRI of the node to edit (preferred)"},
                    "slug": {"type": "string", "description": "Slug of the node to edit (used if iri omitted)"},
                    "frontmatter_updates": {"type": "object", "description": "{field: value} merged into frontmatter; a null value deletes the field"},
                    "section_updates": {"type": "object", "description": "{\"Section Title\": \"new markdown body\"} replacing that section's body (appended if absent)"},
                    "commit_message": {"type": "string", "description": "Optional git commit message"}
                }
            }
        },
        {
            "name": "add_connections",
            "description": "Add typed, graph-visible edges between existing live nodes in one batch + a single git commit. Each edge {subject, target, predicate, note}: the predicate is written into the SUBJECT node's frontmatter (build_graph emits a weighted typed edge subject->target) and a line is appended to its ## Connections. Idempotent per (subject, predicate, target). Predicate must be one of: prerequisite-of, uses, specializes, generalizes, extends, applies, instantiates, contrasts-with, analogous-to.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "edges": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "subject": {"type": "string", "description": "IRI or slug of the node the edge originates from"},
                                "target": {"type": "string", "description": "IRI or slug of the node the edge points to (must be live)"},
                                "predicate": {"type": "string", "enum": ["prerequisite-of", "uses", "specializes", "generalizes", "extends", "applies", "instantiates", "contrasts-with", "analogous-to"]},
                                "note": {"type": "string", "description": "One-sentence rationale for the connection"}
                            },
                            "required": ["subject", "target", "predicate"]
                        }
                    },
                    "commit_message": {"type": "string", "description": "Optional git commit message for the batch"}
                },
                "required": ["edges"]
            }
        },
        {
            "name": "commit_staged_node",
            "description": "Promote a reviewed staged node to the live wiki graph. Commits and pushes to git. Use after reviewing a staged node via get_staged_nodes.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "staged_id": {"type": "string", "description": "UUID from create_bridge_note or create_source_stub"},
                    "edits": {"type": "object", "description": "Field-level edits to apply before committing"},
                    "confirmed_links": {"type": "object", "description": "Resolution of fuzzy refs: {fuzzy_ref: confirmed_iri}"},
                    "action": {"type": "string", "enum": ["commit", "discard"], "default": "commit"}
                },
                "required": ["staged_id"]
            }
        },
        {
            "name": "rebuild_source_graph",
            "description": "Rebuild wiki/source_graph.json from current wiki state. Call after ingesting new sources or marking sources as read. Returns updated graph metadata.",
            "inputSchema": {"type": "object", "properties": {}}
        },
        {
            "name": "upload_document",
            "description": "Store a source document in the PKIS doc store and optionally push it to Readwise Reader. Provide either fetch_url (VPS fetches the file) or content_b64 (base64-encoded bytes).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "slug":             {"type": "string", "description": "Source slug, e.g. hastie-esl-ch08"},
                    "filename":         {"type": "string", "description": "Filename to store as, e.g. hastie-esl-ch08.pdf"},
                    "fetch_url":        {"type": "string", "description": "URL the VPS should fetch the file from"},
                    "content_b64":      {"type": "string", "description": "Base64-encoded file content"},
                    "push_to_readwise": {"type": "boolean", "default": True,
                                        "description": "Push the doc URL to Readwise Reader after storing"}
                },
                "required": ["slug", "filename"]
            }
        },
        {
            "name": "list_documents",
            "description": "List documents stored in the PKIS doc store, optionally filtered to a single source slug.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "slug": {"type": "string", "description": "Filter to a specific source slug"}
                }
            }
        },
        {
            "name": "save_url_source",
            "description": "Save a URL-only source (article, blog post, video, tweet, newsletter, etc.) to the wiki. No file stored on VPS — the URL is the canonical reference. Auto-detects Readwise category (article/video/tweet/email) and fetches title/author from the page.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "url":             {"type": "string", "description": "Full URL of the source"},
                    "slug":            {"type": "string", "description": "Source slug (auto-computed from metadata if omitted)"},
                    "push_to_readwise":{"type": "boolean", "default": True,
                                       "description": "Push to Readwise Reader after saving"}
                },
                "required": ["url"]
            }
        },
        {
            "name": "save_podcast_source",
            "description": "Save a podcast episode as a PKIS source with automatic transcript lookup. Tries YouTube → Podcast Index → Apple Podcasts RSS (in that order). Falls back to Listen Notes + Podchaser for metadata and queues the episode for Whisper transcription if no transcript is found. Stores transcript in raw/clippings/ and pushes full text to Readwise for highlighting.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "url":             {"type": "string", "description": "Podcast episode URL (Spotify, Apple Podcasts, YouTube, RSS, etc.)"},
                    "push_to_readwise":{"type": "boolean", "default": True,
                                       "description": "Push to Readwise Reader after saving"}
                },
                "required": ["url"]
            }
        },
        {
            "name": "get_transcript_queue",
            "description": "List podcast episodes queued for Whisper transcription — no transcript was automatically found when they were saved.",
            "inputSchema": {"type": "object", "properties": {}}
        }
    ]


def handle_jsonrpc(body):
    """
    Handle a JSON-RPC 2.0 MCP Streamable HTTP request.

    Supported methods:
      initialize            — handshake; returns protocol version + capabilities
      notifications/initialized — client ready notification; return 202
      tools/list            — enumerate available tools
      tools/call            — invoke a tool by name
      ping                  — liveness check
    """
    req_id = body.get("id")
    method = body.get("method", "")
    params = body.get("params") or {}

    if method == "initialize":
        # Negotiate: honor the client's requested version if we support it, else
        # offer our newest. Echoing the client's version keeps modern clients
        # (claude.ai connector) on single-endpoint Streamable HTTP instead of the
        # legacy SSE transport (which 404'd against our single /mcp route).
        requested = params.get("protocolVersion")
        negotiated = requested if requested in MCP_SUPPORTED_PROTOCOL_VERSIONS else MCP_PROTOCOL_VERSION
        return _jsonrpc_result(req_id, {
            "protocolVersion": negotiated,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "PKIS Wiki", "version": "1.0.0"}
        })

    elif method.startswith("notifications/"):
        # Client-to-server notifications — no response body required
        return Response(status=202)

    elif method == "tools/list":
        return _jsonrpc_result(req_id, {"tools": _get_tools_list()})

    elif method == "tools/call":
        tool_name = params.get("name")
        tool_args = params.get("arguments") or {}
        if not tool_name:
            return _jsonrpc_error(req_id, -32602, "Missing 'name' in params"), 422
        try:
            result = dispatch_tool(tool_name, tool_args, request)
            return _jsonrpc_result(req_id, {
                "content": [{"type": "text", "text": json.dumps(result, default=str)}]
            })
        except OAuthChallenge as e:
            resp = _jsonrpc_error(req_id, -32001, str(e))
            resp.status_code = 401
            resp.headers["WWW-Authenticate"] = (
                f'Bearer resource_metadata="{PUBLIC_BASE}/.well-known/oauth-protected-resource"'
            )
            return resp
        except PermissionError as e:
            return _jsonrpc_error(req_id, -32001, str(e)), 403
        except ValueError as e:
            return _jsonrpc_error(req_id, -32601, str(e))
        except Exception as e:
            logger.error(f"tools/call error [{tool_name}]: {e}", exc_info=True)
            return _jsonrpc_error(req_id, -32603, str(e)), 500

    elif method == "ping":
        return _jsonrpc_result(req_id, {})

    else:
        return _jsonrpc_error(req_id, -32601, f"Method not found: {method}"), 404


@app.route("/mcp", methods=["GET", "POST"])
@app.route("/mcp/<path:session>", methods=["GET", "POST"])
def mcp_endpoint(session=None):
    """
    MCP Streamable HTTP transport endpoint.

    Routes BOTH the canonical `/mcp` and any session-suffixed `/mcp/<session>`.
    claude.ai's connector persists a per-connector session id and POSTs its
    sub-channel traffic to `/mcp/<session>`; before this catch-all those
    requests 404'd (≈86% of connector traffic), which is what made the connector
    intermittently "unable to read" the wiki. The session segment is accepted
    and ignored — this server is stateless (no per-session state to look up).

    GET  → 405 (SSE server-push not implemented; reads return inline over POST)
    POST → JSON-RPC 2.0 if body has {"jsonrpc": "2.0", ...}
           Legacy format {"tool": "...", "params": {...}} still accepted for
           backward compatibility.
    """
    if session is not None:
        # Visibility into the session-suffixed sub-channel without needing a
        # redeploy to diagnose; confirms the catch-all is doing its job.
        logger.info(
            "MCP session-suffixed request: %s /mcp/%s ua=%r",
            request.method, session, request.headers.get("User-Agent", "")
        )

    if request.method == "GET":
        return Response("Server-Sent Events not supported", status=405)

    try:
        body = request.get_json(silent=True)
        if not body:
            return jsonify({"error": "Empty or non-JSON request body"}), 400

        # JSON-RPC 2.0 path
        if body.get("jsonrpc") == JSONRPC_VERSION:
            return handle_jsonrpc(body)

        # Legacy path: {"tool": "...", "params": {...}}
        tool_name = body.get("tool")
        params = body.get("params", {})
        if not tool_name:
            return jsonify({"error": "Missing 'tool' or 'jsonrpc' field"}), 400

        result = dispatch_tool(tool_name, params, request)
        return jsonify({"result": result, "error": None})

    except Exception as e:
        logger.error(f"MCP endpoint error: {e}", exc_info=True)
        return jsonify({"result": None, "error": str(e)}), 500


def dispatch_tool(tool_name: str, params: dict, req) -> any:
    """Dispatch tool call to implementation."""

    # Rebuild caches if another worker committed a write since this one last built,
    # so search/discovery reflects new content without a service restart.
    ensure_fresh()

    # Read-only tools — available to all clients
    read_tools = {
        "get_write_schema": lambda p: tool_get_write_schema(),
        "resolve_concept": lambda p: tool_resolve_concept(p["surface_form"]),
        "resolve_or_detect": lambda p: {
            "registry": tool_resolve_concept(p["text"]),
            "detected": tool_detect_concepts(p["text"], p.get("threshold", 0.7))
        },
        "detect_concepts": lambda p: tool_detect_concepts(
            p["text"], p.get("threshold", 0.7)
        ),
        "get_node": lambda p: tool_get_node(p["iri"]),
        "get_node_stub": lambda p: tool_get_node_stub(p["iri"]),
        "search_wiki": lambda p: tool_search_wiki(
            p["query"],
            domains=p.get("domains"),
            node_types=p.get("node_types"),
            max_results=p.get("max_results", 10)
        ),
        "search_wiki_index": lambda p: tool_search_wiki_index(p["query"]),
        "get_related": lambda p: tool_get_related(
            p["iri"],
            edge_types=p.get("edge_types"),
            direction=p.get("direction", "both"),
            max_hops=p.get("max_hops", 2)
        ),
        "get_dependency_chain": lambda p: tool_get_dependency_chain(p["iri"]),
        "get_reading_queue": lambda p: tool_get_reading_queue(p.get("priority")),
        "add_to_queue": lambda p: tool_add_to_queue(
            source_iri=p.get("source_iri"),
            reference=p.get("reference"),
            reason=p.get("reason", ""),
            priority=p.get("priority", "normal")
        ),
        "get_concept_frontier": lambda p: tool_get_concept_frontier(
            cluster_proximity_weight=p.get("cluster_proximity_weight")),
        "get_clusters": lambda p: tool_get_clusters(),
        "get_cluster_priorities": lambda p: tool_get_cluster_priorities(),
        "get_reading_graph": lambda p: tool_get_reading_graph(
            scope=p.get("scope", "all_unread"),
            focus_concept=p.get("focus_concept"),
            focus_domain=p.get("focus_domain"),
            min_edge_weight=p.get("min_edge_weight", 2),
            max_nodes=p.get("max_nodes", 100),
        ),
        "get_index": lambda p: tool_get_index(
            domain=p.get("domain"),
            node_type=p.get("node_type")
        ),
        "get_health_metrics": lambda p: tool_get_health_metrics(),
        "get_sourceless_stubs": lambda p: tool_get_sourceless_stubs(),
        # Read-only: lists pending staged nodes (no mutation). In READ tier so it
        # works from the claude.ai connector (anonymous reads).
        "get_staged_nodes": lambda p: tool_get_staged_nodes(
            node_type=p.get("node_type"),
            staged_by=p.get("staged_by"),
            limit=p.get("limit", 20),
        ),
        "list_documents": lambda p: tool_list_documents(p.get("slug")),
        "get_transcript_queue": lambda p: tool_get_transcript_queue(),
        "check_alias_collision": lambda p: tool_check_alias_collision(p["surface_form"]),
        "get_operational_references": lambda p: tool_get_operational_references(p["iri"]),
        "get_concept_operational_load": lambda p: tool_get_concept_operational_load(p["iri"]),
    }

    # Trusted-only tools — require PKIS_TRUSTED_TOKEN
    trusted_tools = {
        "register_operational_reference": lambda p: tool_register_operational_reference(
            p["operational_node_id"],
            p["iri"],
            p["confidence_class"],
            p.get("source_system", "mnemon")
        ),
        "log_operation": lambda p: tool_log_operation(
            p["operation_type"],
            p.get("affected_iris", []),
            p.get("summary", ""),
            p.get("agent", "unknown")
        ),
    }

    # Write tools — require PKIS_MCP_WRITE_KEY
    write_tools = {
        "create_bridge_note": lambda p: tool_create_bridge_note(
            rationale=p["rationale"],
            title=p.get("title", ""),
            source_context=p.get("source_context", ""),
            linked_node_refs=p.get("linked_node_refs"),
            proposed_edge_type=p.get("proposed_edge_type", ""),
            origin=p.get("origin", "conversation"),
        ),
        "create_source_stub": lambda p: tool_create_source_stub(
            title=p.get("title", ""),
            url=p.get("url", ""),
            doi=p.get("doi", ""),
            authors=p.get("authors", ""),
            year=p.get("year"),
            notes=p.get("notes", ""),
            priority=p.get("priority", "normal"),
        ),
        "create_node_stub": lambda p: tool_create_node_stub(
            knowledge_type=p["knowledge_type"],
            title=p["title"],
            definition=p.get("definition", ""),
            domain=p.get("domain"),
            tags=p.get("tags"),
            aliases=p.get("aliases"),
            also_type=p.get("also_type"),
            sources=p.get("sources"),
            slug=p.get("slug", ""),
            suggest_sources=p.get("suggest_sources", True),
        ),
        "create_hypothesis": lambda p: tool_create_hypothesis(
            title=p["title"],
            cluster=p.get("cluster", ""),
            role=p.get("role", "direct-test"),
            domain=p.get("domain"),
            tags=p.get("tags"),
            formal_statement=p.get("formal_statement", ""),
            motivation=p.get("motivation", ""),
            current_evidence=p.get("current_evidence", ""),
            open_questions=p.get("open_questions", ""),
            dependent_nodes=p.get("dependent_nodes"),
            aliases=p.get("aliases"),
            slug=p.get("slug", ""),
        ),
        "edit_node": lambda p: tool_edit_node(
            iri=p.get("iri", ""),
            slug=p.get("slug", ""),
            frontmatter_updates=p.get("frontmatter_updates"),
            section_updates=p.get("section_updates"),
            commit_message=p.get("commit_message", ""),
        ),
        "set_priority_config": lambda p: tool_set_priority_config(
            cluster_proximity_weight=p.get("cluster_proximity_weight"),
            reset=p.get("reset", False),
        ),
        "build_reader": lambda p: tool_build_reader(slug=p["slug"], arxiv_id=p.get("arxiv_id")),
        "add_connections": lambda p: tool_add_connections(
            edges=p["edges"],
            commit_message=p.get("commit_message", ""),
        ),
        "commit_staged_node": lambda p: tool_commit_staged_node(
            staged_id=p["staged_id"],
            edits=p.get("edits"),
            confirmed_links=p.get("confirmed_links"),
            action=p.get("action", "commit"),
        ),
        "rebuild_source_graph": lambda p: tool_rebuild_source_graph(),
        "upload_document": lambda p: tool_upload_document(
            slug=p["slug"],
            filename=p["filename"],
            fetch_url=p.get("fetch_url", ""),
            content_b64=p.get("content_b64", ""),
            push_to_readwise=p.get("push_to_readwise", True),
        ),
        "save_url_source": lambda p: tool_save_url_source(
            url=p["url"],
            slug=p.get("slug", ""),
            push_to_readwise=p.get("push_to_readwise", True),
        ),
        "save_podcast_source": lambda p: tool_save_podcast_source(
            url=p["url"],
            push_to_readwise=p.get("push_to_readwise", True),
        ),
    }

    if tool_name in read_tools:
        return read_tools[tool_name](params)
    elif tool_name in trusted_tools:
        if not is_trusted(req):
            raise gate_error(req, "trusted")
        return trusted_tools[tool_name](params)
    elif tool_name in write_tools:
        if not is_write_authorized(req):
            raise gate_error(req, "write")
        return write_tools[tool_name](params)
    else:
        raise ValueError(f"Unknown tool: {tool_name}")


# ============================================================
# MCP manifest — tells Claude what tools are available
# ============================================================

@app.route("/.well-known/mcp", methods=["GET"])
def mcp_manifest():
    """MCP server manifest for Claude connector registration."""
    return jsonify({
        "name": "PKIS Wiki",
        "description": "Personal Knowledge Integration System — semantic wiki covering Bayesian statistics, deep learning, reinforcement learning, causal analysis, knowledge representation, and symbolic/sub-symbolic AI",
        "version": "1.0.0",
        "tools": _get_tools_list()
    })


@app.route("/.well-known/oauth-protected-resource", methods=["GET"])
@app.route("/.well-known/oauth-protected-resource/mcp", methods=["GET"])
def oauth_protected_resource():
    """RFC 9728 Protected Resource Metadata — points the connector at the IdP.
    404 while OAuth is dormant (PKIS_OAUTH_ISSUER unset) so behavior is unchanged
    until activation; the 401 challenge that references this only fires when enabled."""
    if not OAUTH_ENABLED:
        return jsonify({"error": "OAuth not enabled"}), 404
    return jsonify({
        "resource": OAUTH_AUDIENCE,
        "authorization_servers": [OAUTH_ISSUER],
        "bearer_methods_supported": ["header"],
    })


# ============================================================
# Flask routes — Viewer REST API  (/pkis-api/*)
# Called directly by the React PWA in viewer/.
# No separate proxy process needed — these call tool functions in-process.
# ============================================================

def _api_json():
    """Parse request JSON body, return empty dict on failure."""
    return request.get_json(force=True, silent=True) or {}


def _api_ok(result):
    """Wrap a tool result in a JSON response."""
    return jsonify(result)


def _api_err(e, code=400):
    return jsonify({"error": str(e)}), code


@app.route("/pkis-api/search", methods=["POST"])
def pkis_api_search():
    b = _api_json()
    try:
        return _api_ok(tool_search_wiki(
            query=b.get("query", ""),
            domains=b.get("domains"),
            node_types=b.get("node_types"),
            max_results=b.get("max_results", 10),
        ))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/node", methods=["POST"])
def pkis_api_node():
    b = _api_json()
    iri = b.get("iri", "")
    if not iri:
        return _api_err("iri is required")
    try:
        return _api_ok(tool_get_node(iri))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/related", methods=["POST"])
def pkis_api_related():
    b = _api_json()
    iri = b.get("iri", "")
    if not iri:
        return _api_err("iri is required")
    try:
        return _api_ok(tool_get_related(
            iri=iri,
            edge_types=b.get("edge_types"),
            direction=b.get("direction", "both"),
            max_hops=b.get("max_hops", 2),
        ))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/health", methods=["POST"])
def pkis_api_health():
    try:
        return _api_ok(tool_get_health_metrics())
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/frontier", methods=["POST"])
def pkis_api_frontier():
    b = _api_json()
    try:
        # Viewer expects a list; return just the ranked results (params are MCP-only).
        return _api_ok(tool_get_concept_frontier(
            cluster_proximity_weight=b.get("cluster_proximity_weight"))["results"])
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/clusters", methods=["POST"])
def pkis_api_clusters():
    try:
        return _api_ok(tool_get_clusters())
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/index", methods=["POST"])
def pkis_api_index():
    b = _api_json()
    try:
        return _api_ok(tool_get_index(domain=b.get("domain"), node_type=b.get("node_type")))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/domains", methods=["POST"])
def pkis_api_domains():
    try:
        return _api_ok(tool_get_domains())
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/cluster-priorities", methods=["POST"])
def pkis_api_cluster_priorities():
    try:
        return _api_ok(tool_get_cluster_priorities())
    except Exception as e:
        return _api_err(e, 500)


# ── Read+listen reader (slice 1) ──────────────────────────────────────────
READER_DIR = Path(os.environ.get("READER_DIR", str(WIKI_DIR / "reader")))


@app.route("/pkis-api/reader/<slug>", methods=["GET", "POST"])
def pkis_api_reader(slug):
    p = READER_DIR / slug / "payload.json"
    if not p.exists():
        return _api_err(f"no reader payload for {slug}", 404)
    try:
        return _api_ok(json.loads(p.read_text()))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/reader/<slug>/<audiofile>", methods=["GET"])
def pkis_api_reader_audio(slug, audiofile):
    if audiofile not in ("audio.mp3", "audio.wav"):
        return _api_err("not found", 404)
    d = READER_DIR / slug
    if not (d / audiofile).exists():
        return _api_err("no audio", 404)
    return send_from_directory(str(d), audiofile)


@app.route("/pkis-api/reader/<slug>/status", methods=["GET"])
def pkis_api_reader_status(slug):
    d = READER_DIR / slug
    sp = d / "status.json"
    # An in-progress/failed build takes precedence over a (possibly stale) existing payload.
    if sp.exists():
        try:
            st = json.loads(sp.read_text())
            if st.get("state") in ("building", "error"):
                return _api_ok(st)
        except Exception:
            pass
    if (d / "payload.json").exists():
        return _api_ok({"state": "ready"})
    return _api_ok({"state": "none"})


def _maybe_autobuild_reader(slug: str) -> None:
    """Auto-build a reader when a *paper* lands in the source directory (frontier-driven intent).
    Papers process immediately; books are on-demand. Gate: arXiv URL or an uploaded doc-store PDF
    only — random saved URLs (video/tweet/paywall) and book-chapter splits (-chNN) are skipped.
    Best-effort: never let a reader build break ingestion."""
    if os.environ.get("READER_AUTOBUILD", "1") != "1":
        return
    if re.search(r"-ch\d+$", slug):          # book chapters are built on demand, not on ingest
        return
    if (READER_DIR / slug / "payload.json").exists():
        return
    try:
        p = find_node_path_by_iri(f"pkis:source:{slug}")
        fm = load_node(p).get("frontmatter", {}) if p else {}
        url = str(fm.get("source_url", "") or "")
        has_arxiv = bool(re.search(r'arxiv\.org/(?:abs|pdf)/[0-9]+\.[0-9]+', url))
        sdir = DOCS_DIR / "sources" / slug
        has_pdf = sdir.is_dir() and any(sdir.glob("*.pdf"))
        if has_arxiv or has_pdf:
            tool_build_reader(slug)
    except Exception:
        pass


def tool_build_reader(slug: str, arxiv_id: str = None) -> dict:
    """Kick off a background build of the read+listen payload for a source. The builder is
    slug-driven and routes by available input: arXiv id in source_url → ar5iv; else a doc-store
    PDF → Claude PDF extraction; else an http source_url → web extraction. Returns immediately;
    poll /pkis-api/reader/<slug>/status (or get the payload) for completion."""
    p = find_node_path_by_iri(f"pkis:source:{slug}")
    if not p:
        raise ValueError(f"no source node for slug '{slug}'")
    fm = load_node(p).get("frontmatter", {})
    url = str(fm.get("source_url", "") or fm.get("url", ""))
    # detect route for status reporting + early validation (the builder re-routes the same way)
    m = re.search(r'arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+)', url)
    if not arxiv_id and m:
        arxiv_id = m.group(1)
    pdf_glob = sorted((DOCS_DIR / "sources" / slug).glob("*.pdf")) if (DOCS_DIR / "sources" / slug).is_dir() else []
    if arxiv_id:
        route = "arxiv"
    elif pdf_glob:
        route = "pdf"
    elif url.startswith("http"):
        route = "html"
    else:
        raise ValueError(f"no narratable input for '{slug}' (no arXiv id, no doc-store PDF, no http source_url)")
    d = READER_DIR / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / "status.json").write_text(json.dumps({"state": "building", "route": route, "arxiv_id": arxiv_id}))
    script = str(REPO_DIR / "tools" / "reader_build.py")
    py = os.environ.get("READER_PYTHON", "/home/pkis/venv/bin/python")
    env = dict(os.environ)
    env["PYTHONPATH"] = str(REPO_DIR) + ":" + env.get("PYTHONPATH", "")
    env.setdefault("PIPER", "/home/pkis/piper_dist/piper/piper")
    env.setdefault("PIPER_MODEL", "/home/pkis/piper_dist/voices/en_GB-cori-high.onnx")
    env["LD_LIBRARY_PATH"] = "/home/pkis/piper_dist/piper:" + env.get("LD_LIBRARY_PATH", "")
    env["OUTDIR"] = str(d)
    # slug-driven: the builder loads the source node and routes internally
    cmd = (f'{py} {script} {slug} full > {d}/build.log 2>&1 '
           f'&& echo \'{{"state":"ready"}}\' > {d}/status.json '
           f'|| echo \'{{"state":"error"}}\' > {d}/status.json')
    subprocess.Popen(["bash", "-c", cmd], env=env, start_new_session=True,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return {"status": "building", "slug": slug, "route": route, "arxiv_id": arxiv_id}


@app.route("/pkis-api/reader-build", methods=["POST"])
def pkis_api_reader_build():
    b = _api_json()
    slug = b.get("slug")
    if not slug:
        return _api_err("slug required")
    try:
        return _api_ok(tool_build_reader(slug, b.get("arxiv_id")))
    except Exception as e:
        return _api_err(e, 400)


@app.route("/pkis-api/reader/<slug>/annotations", methods=["GET"])
def pkis_api_reader_annotations(slug):
    p = READER_DIR / slug / "annotations.jsonl"
    if not p.exists():
        return _api_ok([])
    items = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
    return _api_ok(items)


@app.route("/pkis-api/reader-annotate", methods=["POST"])
def pkis_api_reader_annotate():
    """Save a position-anchored annotation from the reader; optionally drop a bridge note
    into the graph when the user flags it (kind='bridge')."""
    b = _api_json()
    slug = b.get("slug")
    if not slug:
        return _api_err("slug required")
    d = READER_DIR / slug
    d.mkdir(parents=True, exist_ok=True)
    rec = {
        "id": str(uuid.uuid4()),
        "slug": slug,
        "section_id": b.get("section_id", ""),
        "text": b.get("text", ""),
        "note": b.get("note", ""),
        "kind": b.get("kind", "note"),
        "created": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    with open(d / "annotations.jsonl", "a") as f:
        f.write(json.dumps(rec) + "\n")
    result = {"status": "saved", "annotation": rec}
    if rec["kind"] == "bridge":
        try:
            note = (rec["note"] or rec["text"] or "")[:300]
            br = tool_create_bridge_note(
                rationale=f"[reading {slug} · {rec['section_id']}] {note}",
                linked_node_refs=[f"pkis:source:{slug}"],
                proposed_edge_type="related",
                origin="reading",
            )
            result["bridge_staged_id"] = br.get("staged_id")
        except Exception as e:
            result["bridge_error"] = str(e)
    return _api_ok(result)


@app.route("/pkis-api/reading-graph", methods=["POST"])
def pkis_api_reading_graph():
    b = _api_json()
    try:
        return _api_ok(tool_get_reading_graph(
            scope=b.get("scope", "all_unread"),
            focus_concept=b.get("focus_concept"),
            focus_domain=b.get("focus_domain"),
            min_edge_weight=b.get("min_edge_weight", 2),
            max_nodes=b.get("max_nodes", 100),
        ))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/staged", methods=["POST"])
def pkis_api_staged():
    b = _api_json()
    try:
        return _api_ok(tool_get_staged_nodes(
            node_type=b.get("node_type"),
            limit=b.get("limit", 20),
        ))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/staged/commit", methods=["POST"])
def pkis_api_staged_commit():
    b = _api_json()
    staged_id = b.get("staged_id", "")
    if not staged_id:
        return _api_err("staged_id is required")
    try:
        return _api_ok(tool_commit_staged_node(
            staged_id=staged_id,
            action=b.get("action", "commit"),
            edits=b.get("edits"),
            confirmed_links=b.get("confirmed_links"),
        ))
    except ValueError as e:
        return _api_err(e, 404)
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/bridge-note", methods=["POST"])
def pkis_api_bridge_note():
    b = _api_json()
    try:
        return _api_ok(tool_create_bridge_note(
            rationale=b.get("rationale", ""),
            linked_node_refs=b.get("linked_node_refs", []),
            proposed_edge_type=b.get("proposed_edge_type", ""),
            origin=b.get("origin", "viewer"),
            title=b.get("title", ""),
        ))
    except ValueError as e:
        return _api_err(e)
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/source-stub", methods=["POST"])
def pkis_api_source_stub():
    b = _api_json()
    try:
        return _api_ok(tool_create_source_stub(
            title=b.get("title", ""),
            url=b.get("url", ""),
            doi=b.get("doi", ""),
            authors=b.get("authors", ""),
            year=b.get("year"),
            notes=b.get("notes", ""),
            priority=b.get("priority", "normal"),
        ))
    except ValueError as e:
        return _api_err(e)
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/queue", methods=["POST"])
def pkis_api_queue_get():
    b = _api_json()
    try:
        return _api_ok(tool_get_reading_queue(priority=b.get("priority")))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/queue/add", methods=["POST"])
def pkis_api_queue_add():
    b = _api_json()
    try:
        return _api_ok(tool_add_to_queue(
            source_iri=b.get("source_iri"),
            reference=b.get("reference"),
            reason=b.get("reason", ""),
            priority=b.get("priority", "normal"),
        ))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/save-url", methods=["POST"])
def pkis_api_save_url():
    b = _api_json()
    url = b.get("url", "")
    if not url:
        return _api_err("url is required")
    try:
        return _api_ok(tool_save_url_source(
            url=url,
            slug=b.get("slug"),
            push_to_readwise=b.get("push_to_readwise", True),
        ))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/rebuild-graph", methods=["POST"])
def pkis_api_rebuild_graph():
    try:
        return _api_ok(tool_rebuild_source_graph())
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/detect-concepts", methods=["POST"])
def pkis_api_detect_concepts():
    b = _api_json()
    text = b.get("text", "")
    if not text:
        return _api_err("text is required")
    try:
        return _api_ok(tool_detect_concepts(
            text=text,
            threshold=b.get("threshold", 0.7),
        ))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/viz/<path:filename>")
def pkis_api_viz(filename):
    """Serve standalone HTML viz assets from wiki/assets/viz/."""
    if ".." in filename:
        return _api_err("Invalid path"), 400
    viz_dir = WIKI_DIR / "assets" / "viz"
    return send_from_directory(str(viz_dir), filename)


# ============================================================
# Entry point
# ============================================================

if __name__ == "__main__":
    # Build caches on startup
    logger.info("Building caches on startup...")
    refresh_caches()
    logger.info("PKIS MCP server ready")
    app.run(host="127.0.0.1", port=5000, debug=False)
