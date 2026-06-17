"""
PKIS configuration constants (B2 split).

All environment-derived settings + static lookup tables, extracted verbatim from
app.py so other split modules can import them without a circular dependency on
app. app.py does `from config import *`, binding these as its own module globals
— so the rest of app.py is unchanged and tests still monkeypatch app.WIKI_DIR /
REPO_DIR / STAGING_DIR / DOCS_DIR / RAW_DIR (those names resolve as app-module
globals at call time).

Only PURE config lives here. Mutable runtime singletons (_jwk_client,
_roles_cache, _workos_client), the sentence-transformers probe, the Flask app,
the Anthropic client, and the in-memory caches stay in app.py.
"""

import os
from pathlib import Path

WIKI_DIR = Path(os.environ.get("WIKI_DIR", "/home/pkis/pkis-wiki/wiki"))
RAW_DIR = Path(os.environ.get("RAW_DIR", "/home/pkis/pkis-wiki/raw"))
REPO_DIR = Path(os.environ.get("REPO_DIR", "/home/pkis/pkis-wiki"))
# Repo root holding app.py + docs/ (today the SAME checkout as the wiki nodes — one
# repo, github.com/choct155/pkis). .resolve() follows a symlinked app.py (prod:
# /home/pkis/app.py -> /home/pkis/pkis-wiki/app.py) to the real repo root, so this
# equals REPO_DIR in prod. Override DOCS_REPO_DIR if docs ever split into their own repo.
DOCS_REPO_DIR = Path(os.environ.get("DOCS_REPO_DIR", str(Path(__file__).resolve().parent)))
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# Semantic (dense) search. BM25 stays the precision anchor; embeddings add recall
# for paraphrase / "approach the idea" queries. Fused via RRF (see hybrid_search).
# Degrades gracefully: if sentence-transformers isn't installed the app runs
# BM25-only, so local dev needs no heavy ML deps.
EMBED_MODEL_NAME = os.environ.get("PKIS_EMBED_MODEL", "BAAI/bge-small-en-v1.5")
# bge-* is trained for asymmetric retrieval: the QUERY (not the documents) gets
# this instruction prefix. Empty it via env for symmetric models (e.g. MiniLM).
EMBED_QUERY_PREFIX = os.environ.get(
    "PKIS_EMBED_QUERY_PREFIX",
    "Represent this sentence for searching relevant passages: ",
)
EMBED_CACHE_PATH = Path(os.environ.get("PKIS_EMBED_CACHE", str(REPO_DIR / ".embed_cache.npz")))
SEMANTIC_SEARCH = os.environ.get("PKIS_SEMANTIC_SEARCH", "1") != "0"

KNOWLEDGE_DIRS = [
    "concepts", "techniques", "results",
    "frameworks", "problems", "principles", "sources",
    "hypotheses", "clusters", "assets", "bridge-notes", "discovery"
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
    "discovery":   "discovery-stub",
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
    "illustrated-by": 0.3,  # subject is illustrated/explained by an asset (interactive explainer/viz)
}

# Trusted client token — set via env var in production
TRUSTED_TOKEN = os.environ.get("PKIS_TRUSTED_TOKEN", "")

# Write endpoint key — separate from read token; required for write operations
WRITE_KEY = os.environ.get("PKIS_MCP_WRITE_KEY", "")

# ============================================================
# OAuth (MCP Resource Server) — DORMANT until PKIS_OAUTH_ISSUER is set.
# ============================================================
OAUTH_ISSUER   = os.environ.get("PKIS_OAUTH_ISSUER", "").rstrip("/")
OAUTH_AUDIENCE = os.environ.get("PKIS_OAUTH_AUDIENCE", "https://pkis.dev/mcp")
OAUTH_JWKS_URL = os.environ.get("PKIS_OAUTH_JWKS_URL", "") or (
    OAUTH_ISSUER + "/.well-known/jwks.json" if OAUTH_ISSUER else "")
OAUTH_ALGS     = [a.strip() for a in os.environ.get("PKIS_OAUTH_ALGS", "RS256").split(",") if a.strip()]
ROLES_PATH     = os.environ.get("PKIS_ROLES_PATH", "")
PUBLIC_BASE    = os.environ.get("PKIS_PUBLIC_BASE", "https://pkis.dev").rstrip("/")
OAUTH_ENABLED  = bool(OAUTH_ISSUER and OAUTH_JWKS_URL)

# ============================================================
# Web sign-in (WorkOS AuthKit sealed session) — gates the VIEWER's write routes.
# DORMANT until WORKOS_API_KEY is set.
# ============================================================
WORKOS_API_KEY        = os.environ.get("WORKOS_API_KEY", "")
WORKOS_CLIENT_ID      = os.environ.get("WORKOS_CLIENT_ID", "")
WORKOS_COOKIE_PASSWORD = os.environ.get("WORKOS_COOKIE_PASSWORD", "")
WORKOS_REDIRECT_URI   = os.environ.get("WORKOS_REDIRECT_URI", "https://pkis.dev/pkis-api/auth/callback")
WEB_AUTH_ENABLED      = bool(WORKOS_API_KEY and WORKOS_CLIENT_ID and WORKOS_COOKIE_PASSWORD)
WEB_SESSION_COOKIE    = "wos_session"

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
MCP_SUPPORTED_PROTOCOL_VERSIONS = ["2025-06-18", "2025-03-26", "2024-11-05"]
MCP_PROTOCOL_VERSION = MCP_SUPPORTED_PROTOCOL_VERSIONS[0]
