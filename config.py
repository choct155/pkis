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
# Generated OpenWiki code map — lives at <repo>/openwiki (same checkout as app.py +
# docs/, so it hangs off DOCS_REPO_DIR). Exposed read-only over MCP via get_openwiki.
OPENWIKI_DIR = Path(os.environ.get("OPENWIKI_DIR", str(DOCS_REPO_DIR / "openwiki")))
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
    "hypotheses", "clusters", "assets", "bridge-notes", "discovery",
    "findings", "resources",
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
    "findings":    "finding",
    "resources":   "resource",
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
    "evidence-for": 0.5,  # a Finding node is empirical evidence bearing on a Hypothesis (Finding -> Hypothesis)
    "implemented-by": 0.6,  # a concept/technique is concretely realized by a Resource (subject -> resource)
    "superseded-by": 0.5,  # a Resource has been replaced/made obsolete by another Resource (resource -> resource)
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

# ============================================================
# Native-app auth (Capacitor APK). After a WorkOS login completes at the existing
# web callback, PKIS mints its OWN opaque bearer tokens and hands them to the app
# over a one-time code on the `com.pkis.app://` deep link (the WebView is served
# from https://localhost, so the cookie/redirect web flow can't reach it). The app
# stores the refresh token in the Android Keystore behind biometric unlock. These
# tokens are PKIS-owned (not WorkOS JWTs), so validation needs no IdP round-trip.
# DORMANT unless WorkOS web auth is configured (login depends on it).
# ============================================================
NATIVE_APP_SCHEME   = os.environ.get("PKIS_NATIVE_APP_SCHEME", "com.pkis.app")
NATIVE_TOKEN_DB     = Path(os.environ.get(
    "PKIS_NATIVE_TOKEN_DB", "/home/pkis/conversations/native_tokens.sqlite"))
NATIVE_ACCESS_TTL   = int(os.environ.get("PKIS_NATIVE_ACCESS_TTL", str(3600)))            # 1 hour
NATIVE_REFRESH_TTL  = int(os.environ.get("PKIS_NATIVE_REFRESH_TTL", str(60 * 24 * 3600))) # 60 days
NATIVE_CODE_TTL     = int(os.environ.get("PKIS_NATIVE_CODE_TTL", str(300)))               # one-time code / pending state: 5 min
NATIVE_AUTH_ENABLED = WEB_AUTH_ENABLED

# Built viewer SPA (Vite `npm run build`, base '/app/'). On the VPS nginx served this
# at /app/; on the workstation gunicorn serves it directly (see serve_app in app.py).
# Override with PKIS_VIEWER_DIST if the build lives elsewhere.
VIEWER_DIST = Path(os.environ.get(
    "PKIS_VIEWER_DIST", str(Path(__file__).resolve().parent / "viewer" / "app" / "dist")))

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

# Repo web base for review_url / url fields in write-tool return payloads (B6).
# One value so a fork / repo move doesn't break the returned links.
REPO_WEB_BASE = os.environ.get("PKIS_REPO_WEB_BASE", "https://github.com/choct155/pkis").rstrip("/")

# Model IDs (B6 centralization — were scattered as literals across app.py + tools/).
# Env-overridable; the tools import these so there is one place to bump a model.
CONCEPT_DETECT_MODEL = os.environ.get("PKIS_CONCEPT_DETECT_MODEL", "claude-sonnet-4-20250514")
NARRATION_MODEL      = os.environ.get("PKIS_NARRATION_MODEL", "claude-sonnet-4-6")
EXTRACT_MODEL        = os.environ.get("PKIS_EXTRACT_MODEL", "claude-haiku-4-5")
RATIONALE_MODEL      = os.environ.get("PKIS_RATIONALE_MODEL", "claude-sonnet-4-6")
PROPOSAL_MODEL       = os.environ.get("PKIS_PROPOSAL_MODEL", "claude-sonnet-4-6")

# Comptroller usage store (Roster Phase 4). SQLite under /home/pkis (pkis owns it —
# avoids the /var/pkis sudo the roster's spec assumed; passwordless sudo is
# systemctl-only here). log_usage writes here best-effort; tools/comptroller.py reads it.
USAGE_DB_PATH = Path(os.environ.get("PKIS_USAGE_DB", "/home/pkis/usage/usage.sqlite"))

# Retrieval lab (C-1e). Named search profiles persist as JSON (mirrors
# priority_config.json; the `_config.json` suffix is gitignored). Experiment runs
# log to an append-only SQLite store (gitignored; runtime data, not committed).
SEARCH_PROFILES_PATH = Path(os.environ.get(
    "PKIS_SEARCH_PROFILES", str(REPO_DIR / "search_profile_config.json")))
# Cross-encoder reranker model (lazy-loaded). MiniLM is small (~80MB) and fast on
# CPU; BAAI/bge-reranker-base is a heavier, higher-quality option. Per-profile
# override via reranker_params.cross_encoder.model.
CROSS_ENCODER_MODEL = os.environ.get("PKIS_CROSS_ENCODER", "cross-encoder/ms-marco-MiniLM-L-6-v2")
EXPERIMENT_DB_PATH = Path(os.environ.get(
    "PKIS_EXPERIMENT_DB", str(REPO_DIR / ".experiments.sqlite")))

# MCP JSON-RPC 2.0 Streamable HTTP transport constants
JSONRPC_VERSION = "2.0"
MCP_SUPPORTED_PROTOCOL_VERSIONS = ["2025-06-18", "2025-03-26", "2024-11-05"]
MCP_PROTOCOL_VERSION = MCP_SUPPORTED_PROTOCOL_VERSIONS[0]
