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
import base64
import secrets
import sqlite3
import sys
import time
import threading
# B2 split: make sibling split-modules (store.py, …) importable regardless of the
# process CWD. On the server app.py is a symlink (/home/pkis/app.py ->
# pkis-wiki/app.py) and gunicorn's WorkingDirectory is /home/pkis, so realpath
# resolves to the real package dir; locally this is a harmless no-op.
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

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
from flask import Flask, request, jsonify, Response, send_from_directory, g, redirect, make_response, stream_with_context
from anthropic import Anthropic

# B2 split (incremental): pure helpers carved out to store.py; re-imported so the
# rest of app.py and every `import app` consumer keep referencing them unchanged.
from store import slug_from_path, iri_from_slug, parse_iri, rrf_score, WikiStore
from store import merge_search_profile, DEFAULT_SEARCH_PROFILE
import experiments
import metrics
# The shared natural-language "ask brain" (retrieve → traverse → cited synthesis).
# ask.py imports `app` lazily inside its functions, so this top-level import is
# not circular. Reused by /pkis-api/ask and (later) the ask_pkis MCP tool.
import ask
# Per-user persistence for ask conversations (auto-saved, versioned). Pure stdlib,
# no back-reference to app.
import conversations
# Capability-link sharing (token → owned item, public read-only). Pure stdlib.
import shares
# Comptroller usage accounting (Roster Phase 4). log_usage is BEST-EFFORT — it never
# raises, so a logging failure cannot break a tool call. Writes to config.USAGE_DB_PATH.
from usage import log_usage, compute_cost, get_config
# External-API adapters carved out to adapters.py; `import *` (driven by adapters'
# __all__) binds the underscore-named fetchers as app globals, so callers resolve
# them and the contract-test monkeypatches still land.
from adapters import *  # noqa: F401,F403

# ============================================================
# Configuration — all constants extracted to config.py (B2 split); re-imported
# so app.py and every `import app` consumer reference them unchanged, and tests
# still monkeypatch app.WIKI_DIR / REPO_DIR / STAGING_DIR / DOCS_DIR / RAW_DIR
# (import * binds them as app-module globals the functions read at call time).
# ============================================================
from config import *  # noqa: F401,F403

# sentence-transformers capability probe (runtime capability, not config) — the
# app degrades to BM25-only when it isn't installed.
try:
    from sentence_transformers import SentenceTransformer  # noqa: F401
    _ST_AVAILABLE = True
except Exception:
    _ST_AVAILABLE = False

# Mutable runtime singletons — kept in app.py so their lazy-init `global` rebinding
# stays within this module.
_jwk_client = None
_roles_cache = {"mtime": 0.0, "data": {}}
_workos_client = None


class OAuthChallenge(PermissionError):
    """Unauthorized write while OAuth is enabled and caller is anonymous —
    triggers a 401 + WWW-Authenticate so the connector starts the OAuth flow."""


class GitPushError(RuntimeError):
    """A local commit succeeded but `git push` failed. Raised LOUDLY so a write
    is never silently left diverging from origin (the 'sneaky divergence' that
    swallowed push failures used to cause). The local commit is RETAINED — no
    work is lost — and `.diagnostics` carries the divergence snapshot plus a
    recommended remediation. Reconcile via tools/reconcile_push.py (a deliberate,
    confirmed step), never automatically inside a request."""

    def __init__(self, message: str, diagnostics: dict):
        super().__init__(message)
        self.diagnostics = diagnostics

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Fail loudly if web auth is on but the cookie key isn't a valid Fernet key. The
# WorkOS Python SDK seals sessions with Fernet, so WORKOS_COOKIE_PASSWORD must be a
# Fernet.generate_key() value (44-char base64) — NOT an arbitrary 32/64-char string
# (WorkOS's generic ">=32 chars" guidance is for the Node SDK's iron-session).
if WEB_AUTH_ENABLED:
    try:
        from cryptography.fernet import Fernet as _Fernet
        _Fernet(WORKOS_COOKIE_PASSWORD)
    except Exception as _e:  # noqa: BLE001
        logger.error("WORKOS_COOKIE_PASSWORD is not a valid Fernet key (%s); web sign-in "
                     "will silently fail. Generate one via Fernet.generate_key().", _e)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 200 * 1024 * 1024  # 200 MB — matches nginx client_max_body_size
anthropic_client = Anthropic(api_key=ANTHROPIC_API_KEY)

# ============================================================
# In-memory caches (invalidated on git pull via /refresh)
# ============================================================

# Node + alias caches now live on the injected WikiStore (option-C DI). The
# remaining caches (graph, BM25, embeddings) migrate in later C increments.
# The WikiStore now owns the node, alias, graph, BM25 and embedding caches
# (option-C DI). semantic_enabled = config flag AND the sentence-transformers probe.
STORE = WikiStore(WIKI_DIR, repo_dir=REPO_DIR, semantic_enabled=(SEMANTIC_SEARCH and _ST_AVAILABLE))


def _content_signature():
    return STORE.content_signature()


def ensure_fresh():
    return STORE.ensure_fresh()


# ============================================================
# Core helpers
# ============================================================



# Thin wrappers over the injected WikiStore (option-C DI) — these keep every
# existing call site unchanged while the node-loading logic + caches live on STORE.

def find_node_path(slug):
    return STORE.find_node_path(slug)


def find_node_path_by_iri(iri):
    return STORE.find_node_path_by_iri(iri)


def load_node(path):
    return STORE.load_node(path)


def load_all_nodes():
    return STORE.load_all_nodes()


def build_alias_registry():
    return STORE.build_alias_registry()


def build_graph():
    return STORE.build_graph()


# Search-layer wrappers over the injected WikiStore (option-C DI). The embedding
# internals (_get_embed_model/_embed_text/_load_/_save_embed_cache) are now private
# to WikiStore.

def build_bm25_index():
    return STORE.build_bm25_index()


def _semantic_enabled():
    return STORE._semantic_enabled()


def build_embedding_index():
    return STORE.build_embedding_index()


def vector_search(query, max_results=30):
    return STORE.vector_search(query, max_results=max_results)


def refresh_caches():
    """Invalidate and rebuild all caches."""
    return STORE.refresh()


def get_alias_registry():
    return STORE.get_alias_registry()


def get_graph():
    return STORE.get_graph()


def structural_candidates(seed_iri, edge_types=None, max_hops=2):
    return STORE.structural_candidates(seed_iri, edge_types=edge_types, max_hops=max_hops)


def hybrid_search(query, domains=None, node_types=None, max_results=10):
    return STORE.hybrid_search(query, domains=domains, node_types=node_types, max_results=max_results)


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


_userinfo_cache: dict = {}  # opaque access token -> (claims, expiry_ts)


def _userinfo_claims(tok: str) -> dict:
    """Resolve an opaque access token to OIDC claims via AuthKit's userinfo
    endpoint — the fallback when a bearer isn't a decodable JWT (WorkOS AuthKit
    can hand MCP clients opaque access tokens). Cached briefly to avoid a
    userinfo round-trip on every request."""
    import time

    import requests

    now = time.time()
    hit = _userinfo_cache.get(tok)
    if hit and hit[1] > now:
        return hit[0]
    r = requests.get(
        OAUTH_ISSUER + "/oauth2/userinfo",
        headers={"Authorization": f"Bearer {tok}"},
        timeout=6,
    )
    r.raise_for_status()
    claims = r.json()
    _userinfo_cache[tok] = (claims, now + 300)
    return claims


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
        # Not a decodable JWT (e.g. AuthKit issued an opaque access token) — fall
        # back to OIDC userinfo introspection so opaque bearers still resolve.
        try:
            claims = _userinfo_claims(tok)
            logger.info("OAuth identity via userinfo (opaque token)")
        except Exception as e2:  # noqa: BLE001
            logger.info("OAuth token rejected: jwt=%s userinfo=%s", e, e2)
            return None
    email = (claims.get("email") or "").lower()
    sub = (claims.get("sub") or "").strip()
    roles = _load_roles()
    # Map by email OR WorkOS sub (user id) — allowlist file may key on either.
    role = roles.get(email) or roles.get(sub) or "reader"
    logger.info("OAuth identity: email=%r sub=%r role=%r claim_keys=%s",
                email, sub, role, sorted(claims.keys()))
    return ((email or sub), role)


def _get_workos():
    global _workos_client
    if _workos_client is None:
        from workos import WorkOSClient  # lazy: app boots without the dep
        _workos_client = WorkOSClient(api_key=WORKOS_API_KEY, client_id=WORKOS_CLIENT_ID)
    return _workos_client


# Refresh coalescing (cross-process). WorkOS refresh tokens are SINGLE-USE
# (rotated on each refresh). When the access token expires, a burst of concurrent
# requests carrying the same cookie would each call session.refresh() with that
# one token — the first wins, the rest come back unauthenticated, silently logging
# the user out of those requests (e.g. an inbox 401 while /auth/me and a write
# succeeded). We serialize per cookie through a small SQLite cache (works across
# gunicorn workers): the first refresh writes the new sealed cookie + resolved
# identity; concurrent/closely-following requests with the same cookie reuse it
# instead of spending the already-rotated token again.
AUTH_REFRESH_DB = Path(os.environ.get(
    "PKIS_AUTH_REFRESH_DB", "/home/pkis/conversations/auth_refresh.sqlite"))
_REFRESH_TTL = 90.0  # seconds a shared refresh result stays reusable


def _refresh_db():
    AUTH_REFRESH_DB.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(AUTH_REFRESH_DB), timeout=6)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA busy_timeout=6000;")
    conn.execute("CREATE TABLE IF NOT EXISTS refresh_cache ("
                 "cookie_hash TEXT PRIMARY KEY, sealed TEXT, sub TEXT, role TEXT, ts REAL)")
    return conn


def _identity_from_user(user) -> Optional[tuple]:
    """(stable-id, role) from a WorkOS user object, role via the allowlist.

    The stable id is the EMAIL when present, falling back to the WorkOS sub. Email
    is the durable per-person anchor; the WorkOS `sub` (user id) is login-method
    specific, so the same person signing in via a different connection gets a
    different sub. Keying user-owned data (conversations, shares) on the sub
    therefore fragmented it across logins. Email-first matches oauth_identity() and
    keeps a user's history continuous regardless of how they signed in this time."""
    sub = email = ""
    if user is not None:
        sub = (getattr(user, "id", None)
               or (user.get("id") if isinstance(user, dict) else "") or "").strip()
        email = (getattr(user, "email", None)
                 or (user.get("email") if isinstance(user, dict) else "") or "").strip().lower()
    if not (sub or email):
        return None
    roles = _load_roles()
    return (email or sub, roles.get(email) or roles.get(sub) or "reader")


def _coalesced_refresh(cookie: str, session):
    """Refresh a sealed session, serialized per cookie across processes via SQLite
    so the single-use token is spent once. Returns (identity, new_sealed_cookie),
    or (None, None) on genuine failure (true sign-out)."""
    key = hashlib.sha256(cookie.encode()).hexdigest()
    now = time.time()
    conn = _refresh_db()
    try:
        conn.execute("BEGIN IMMEDIATE")  # serialize refreshers; only contends with other refreshers
        row = conn.execute(
            "SELECT sealed, sub, role, ts FROM refresh_cache WHERE cookie_hash=?",
            (key,)).fetchone()
        if row and (now - row[3]) < _REFRESH_TTL:
            conn.commit()
            return (row[1], row[2]), row[0]
        try:
            ref = session.refresh(cookie_password=WORKOS_COOKIE_PASSWORD)
        except Exception as e:  # noqa: BLE001
            conn.rollback()
            logger.info("web session refresh failed: %s", e)
            return None, None
        if not getattr(ref, "authenticated", False):
            conn.rollback()
            return None, None
        sealed = getattr(ref, "sealed_session", None)
        identity = _identity_from_user(getattr(ref, "user", None))
        if identity is None:
            conn.rollback()
            return None, None
        conn.execute(
            "INSERT OR REPLACE INTO refresh_cache (cookie_hash, sealed, sub, role, ts) "
            "VALUES (?,?,?,?,?)", (key, sealed, identity[0], identity[1], now))
        conn.execute("DELETE FROM refresh_cache WHERE ts < ?", (now - _REFRESH_TTL,))
        conn.commit()
        return identity, sealed
    finally:
        conn.close()


# ============================================================
# Native-app bearer tokens (Capacitor APK). PKIS mints these AFTER a WorkOS login
# (the web callback hands the app a one-time code over the com.pkis.app:// deep
# link; the app exchanges it here for an access+refresh pair, binding the exchange
# with PKCE so only the app instance that started the flow can redeem it). Tokens
# are opaque random strings, persisted only as SHA-256 hashes — the plaintext is
# never stored. Role is resolved LIVE from the allowlist at validation time, so
# allowlist edits and revocation take effect immediately. Mirrors the _refresh_db
# SQLite pattern. DORMANT unless NATIVE_AUTH_ENABLED (WorkOS web auth configured).
# ============================================================

def _hash_token(tok: str) -> str:
    return hashlib.sha256(tok.encode()).hexdigest()


def _pkce_challenge(verifier: str) -> str:
    """S256 PKCE: base64url(sha256(verifier)) without padding (RFC 7636)."""
    digest = hashlib.sha256(verifier.encode()).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode()


def _native_db():
    NATIVE_TOKEN_DB.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(NATIVE_TOKEN_DB), timeout=6)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA busy_timeout=6000;")
    conn.execute("CREATE TABLE IF NOT EXISTS native_pending ("
                 "state TEXT PRIMARY KEY, challenge TEXT, ts REAL)")
    conn.execute("CREATE TABLE IF NOT EXISTS native_codes ("
                 "code_hash TEXT PRIMARY KEY, email TEXT, challenge TEXT, ts REAL)")
    conn.execute("CREATE TABLE IF NOT EXISTS native_tokens ("
                 "access_hash TEXT PRIMARY KEY, refresh_hash TEXT UNIQUE, email TEXT, "
                 "issued REAL, access_exp REAL, refresh_exp REAL, revoked INTEGER DEFAULT 0)")
    return conn


def _native_register_challenge(challenge: str) -> str:
    """Store a PKCE challenge under a fresh state nonce (carried through WorkOS as
    `native:<nonce>`); return the nonce. Garbage-collects stale pending rows."""
    nonce = secrets.token_urlsafe(24)
    now = time.time()
    conn = _native_db()
    try:
        conn.execute("INSERT INTO native_pending (state, challenge, ts) VALUES (?,?,?)",
                     (nonce, challenge, now))
        conn.execute("DELETE FROM native_pending WHERE ts < ?", (now - NATIVE_CODE_TTL,))
        conn.commit()
    finally:
        conn.close()
    return nonce


def _native_consume_challenge(nonce: str) -> Optional[str]:
    """Pop (one-time) the PKCE challenge for a pending nonce, or None if missing/expired."""
    now = time.time()
    conn = _native_db()
    try:
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute("SELECT challenge, ts FROM native_pending WHERE state=?",
                           (nonce,)).fetchone()
        conn.execute("DELETE FROM native_pending WHERE state=?", (nonce,))
        conn.commit()
        if not row or (now - row[1]) > NATIVE_CODE_TTL:
            return None
        return row[0]
    finally:
        conn.close()


def _native_issue_code(email: str, challenge: str) -> str:
    """Mint a one-time auth code bound to (email, PKCE challenge); return the plaintext."""
    code = secrets.token_urlsafe(32)
    now = time.time()
    conn = _native_db()
    try:
        conn.execute("INSERT INTO native_codes (code_hash, email, challenge, ts) VALUES (?,?,?,?)",
                     (_hash_token(code), email, challenge, now))
        conn.execute("DELETE FROM native_codes WHERE ts < ?", (now - NATIVE_CODE_TTL,))
        conn.commit()
    finally:
        conn.close()
    return code


def _native_mint(conn, email: str) -> tuple:
    """Insert a fresh access+refresh pair for `email` on an open connection; return
    (access_plaintext, refresh_plaintext, access_exp)."""
    now = time.time()
    access = secrets.token_urlsafe(32)
    refresh = secrets.token_urlsafe(32)
    a_exp = now + NATIVE_ACCESS_TTL
    conn.execute(
        "INSERT INTO native_tokens (access_hash, refresh_hash, email, issued, "
        "access_exp, refresh_exp, revoked) VALUES (?,?,?,?,?,?,0)",
        (_hash_token(access), _hash_token(refresh), email, now, a_exp, now + NATIVE_REFRESH_TTL))
    return access, refresh, a_exp


def _native_redeem_code(code: str, verifier: str) -> Optional[tuple]:
    """Validate a one-time code + PKCE verifier; on success mint a token pair and
    return (access, refresh, access_exp). One-time: the code is consumed either way."""
    now = time.time()
    expected = _pkce_challenge(verifier)
    conn = _native_db()
    try:
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute("SELECT email, challenge, ts FROM native_codes WHERE code_hash=?",
                           (_hash_token(code),)).fetchone()
        conn.execute("DELETE FROM native_codes WHERE code_hash=?", (_hash_token(code),))
        if not row or (now - row[2]) > NATIVE_CODE_TTL or not secrets.compare_digest(row[1], expected):
            conn.commit()
            return None
        out = _native_mint(conn, row[0])
        conn.commit()
        return out
    finally:
        conn.close()


def _native_rotate(refresh: str) -> Optional[tuple]:
    """Rotate a valid (unexpired, not revoked) refresh token: revoke the old row and
    mint a new pair for the same email. Returns (access, refresh, access_exp) or None."""
    now = time.time()
    conn = _native_db()
    try:
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute(
            "SELECT email, refresh_exp, revoked FROM native_tokens WHERE refresh_hash=?",
            (_hash_token(refresh),)).fetchone()
        if not row or row[2] or row[1] < now:
            conn.commit()
            return None
        conn.execute("UPDATE native_tokens SET revoked=1 WHERE refresh_hash=?",
                     (_hash_token(refresh),))
        out = _native_mint(conn, row[0])
        # prune fully-dead rows (refresh expired, or revoked + access also expired)
        conn.execute("DELETE FROM native_tokens WHERE refresh_exp < ? OR (revoked=1 AND access_exp < ?)",
                     (now, now))
        conn.commit()
        return out
    finally:
        conn.close()


def _native_resolve(access: str) -> Optional[str]:
    """Email for a valid (unexpired, not revoked) native access token, else None."""
    now = time.time()
    conn = _native_db()
    try:
        row = conn.execute(
            "SELECT email, access_exp, revoked FROM native_tokens WHERE access_hash=?",
            (_hash_token(access),)).fetchone()
        if not row or row[2] or row[1] < now:
            return None
        return row[0]
    finally:
        conn.close()


def _native_revoke(access: str) -> None:
    """Revoke the token row for an access token (logout). Idempotent."""
    conn = _native_db()
    try:
        conn.execute("UPDATE native_tokens SET revoked=1 WHERE access_hash=?",
                     (_hash_token(access),))
        conn.commit()
    finally:
        conn.close()


@app.before_request
def _load_web_session():
    """Populate g.web_identity = (sub, role) from the sealed-session cookie, with
    TRANSPARENT REFRESH: an expired access token is healed via the session's
    refresh token (g.refreshed_session is re-cookied in after_request), so a
    signed-in user is never re-prompted. No-op without a cookie or when web auth
    is unconfigured — so reads and the MCP path are unaffected."""
    g.web_identity = None
    g.refreshed_session = None
    if not WEB_AUTH_ENABLED:
        return
    cookie = request.cookies.get(WEB_SESSION_COOKIE)
    if not cookie:
        return
    try:
        session = _get_workos().user_management.load_sealed_session(
            session_data=cookie, cookie_password=WORKOS_COOKIE_PASSWORD)
        res = session.authenticate()
        if getattr(res, "authenticated", False):
            # Match by email OR sub (web sealed session has the email claim that the
            # MCP access token lacks) → an allowlisted email works regardless of which
            # login method's sub the web flow produces.
            g.web_identity = _identity_from_user(getattr(res, "user", None))
        else:
            # access token expired → refresh transparently, coalescing concurrent
            # refreshes of this cookie so the single-use token is spent exactly once
            identity, sealed = _coalesced_refresh(cookie, session)
            if identity is None:
                return
            g.web_identity = identity
            if sealed:
                g.refreshed_session = sealed
    except Exception as e:  # noqa: BLE001 — any failure = treat as signed out
        logger.info("web session auth failed: %s", e)


@app.after_request
def _persist_refreshed_session(resp):
    sealed = getattr(g, "refreshed_session", None)
    if sealed:
        resp.set_cookie(WEB_SESSION_COOKIE, sealed, max_age=30 * 24 * 3600,
                        httponly=True, secure=True, samesite="Lax")
    return resp


def web_identity(req=None) -> Optional[tuple]:
    """(sub, role) for a valid web sealed session, else None. Computed by the
    before_request hook (with refresh); the arg is ignored, kept for symmetry."""
    return getattr(g, "web_identity", None)


def native_identity(req):
    """(email, role) for a valid native-app bearer access token, else None. No-op
    when native auth is off or the bearer is a static key. Role is resolved LIVE
    from the allowlist, so revocation + role edits apply immediately. This is the
    native-client analogue of web_identity (an interactive user session), so it is
    wired into the same gates web_identity is — NOT into is_trusted (the M2M tier)."""
    if not NATIVE_AUTH_ENABLED:
        return None
    tok = _bearer(req)
    if not tok or tok == WRITE_KEY or tok == TRUSTED_TOKEN:
        return None
    email = _native_resolve(tok)
    if not email:
        return None
    return (email, _role_for_email(email))


def require_write(fn):
    """Gate a REST write route: 401 if not signed in, 403 if signed in but lacking
    write role. The MCP dispatch path gates itself and is unaffected. The static
    WRITE_KEY Bearer still authorizes (desktop Claude Code M2M)."""
    @wraps(fn)
    def _wrap(*args, **kwargs):
        if is_write_authorized(request):
            return fn(*args, **kwargs)
        anon = (web_identity(request) is None
                and oauth_identity(request) is None
                and native_identity(request) is None
                and not _has_static_key(request))
        if anon:
            return jsonify({"error": "sign in required"}), 401
        return jsonify({"error": "insufficient role — write access required"}), 403
    return _wrap


def is_trusted(req) -> bool:
    """Trusted tier: static TRUSTED_TOKEN, or an OAuth 'owner'."""
    if TRUSTED_TOKEN and _bearer(req) == TRUSTED_TOKEN:
        return True
    ident = oauth_identity(req)
    return bool(ident and ident[1] == "owner")


def is_write_authorized(req) -> bool:
    """Write tier: static WRITE_KEY, an OAuth 'owner'/'writer' (Bearer JWT, MCP),
    a signed-in web 'owner'/'writer' (sealed session), or a native-app
    'owner'/'writer' (bearer access token)."""
    if WRITE_KEY and _bearer(req) == WRITE_KEY:
        return True
    ident = oauth_identity(req)
    if ident and ident[1] in ("owner", "writer"):
        return True
    wident = web_identity(req)
    if wident and wident[1] in ("owner", "writer"):
        return True
    nident = native_identity(req)
    return bool(nident and nident[1] in ("owner", "writer"))


def is_owner(req) -> bool:
    """Owner tier — gates ADMINISTRATIVE surfaces (the inbox). Static TRUSTED_TOKEN,
    an OAuth 'owner', a web sealed session with the 'owner' role, or a native-app
    'owner'. Note: 'writer' does NOT qualify — the inbox is owner-only."""
    if TRUSTED_TOKEN and _bearer(req) == TRUSTED_TOKEN:
        return True
    ident = oauth_identity(req)
    if ident and ident[1] == "owner":
        return True
    wident = web_identity(req)
    if wident and wident[1] == "owner":
        return True
    nident = native_identity(req)
    return bool(nident and nident[1] == "owner")


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
    if STORE._bm25_index is None:
        STORE.build_bm25_index()

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
            model=CONCEPT_DETECT_MODEL,
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        # Comptroller accounting (best-effort; never raises). USAGE_DB_PATH is bound
        # from config via import *; resolved as an app global at call time.
        log_usage(USAGE_DB_PATH, response, origin="pkis-mcp", project="pkis",
                  attributes={"tool": "detect_concepts"})
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
                nfm = n.get("frontmatter", {})
                related.append({
                    "iri": neighbor,
                    "title": n.get("title", neighbor),
                    "edge_type": edge_data.get("edge_type", "related"),
                    "direction": "outbound",
                    "viz": nfm.get("viz"),
                    "kind": nfm.get("kind"),
                })
        for predecessor in list(G.predecessors(iri))[:10]:
            edge_data = G.get_edge_data(predecessor, iri) or {}
            pred_path = find_node_path_by_iri(predecessor)
            if pred_path:
                n = load_node(pred_path)
                nfm = n.get("frontmatter", {})
                related.append({
                    "iri": predecessor,
                    "title": n.get("title", predecessor),
                    "edge_type": edge_data.get("edge_type", "related"),
                    "direction": "inbound",
                    "viz": nfm.get("viz"),
                    "kind": nfm.get("kind"),
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


# ── Retrieval lab: search profiles + instrumented runs (C-1e) ──
# A SearchProfile is a (possibly partial) toggle bundle; STORE.search merges it
# over DEFAULT_SEARCH_PROFILE. Named profiles persist to SEARCH_PROFILES_PATH
# (mirrors priority_config: read-per-call, worker-safe), overlaid on builtins.

BUILTIN_SEARCH_PROFILES = {
    "default":       {"name": "default"},
    "lexical_only":  {"name": "lexical_only", "retrievers": {"lexical": True, "dense": False}},
    "dense_only":    {"name": "dense_only",   "retrievers": {"lexical": False, "dense": True}},
    "rerank":        {"name": "rerank",       "rerankers": ["cross_encoder"]},
    "graph_rerank":  {"name": "graph_rerank", "rerankers": ["graph"]},
}


def _persisted_search_profiles() -> dict:
    try:
        if SEARCH_PROFILES_PATH.exists():
            return json.loads(SEARCH_PROFILES_PATH.read_text()) or {}
    except Exception as ex:
        logger.warning(f"search profiles read failed: {ex}")
    return {}


def search_profiles() -> dict:
    """All known named profiles — builtins overlaid with persisted ones."""
    out = dict(BUILTIN_SEARCH_PROFILES)
    out.update(_persisted_search_profiles())
    return out


def resolve_search_profile(profile):
    """profile: None | name(str) | inline(dict) -> (raw_profile_dict, source).
    The raw dict is merged over DEFAULT_SEARCH_PROFILE inside STORE.search."""
    if profile is None:
        return BUILTIN_SEARCH_PROFILES["default"], "default"
    if isinstance(profile, str):
        profs = search_profiles()
        if profile in profs:
            return profs[profile], f"named:{profile}"
        logger.warning(f"unknown search profile '{profile}'; using default")
        return BUILTIN_SEARCH_PROFILES["default"], "default"
    if isinstance(profile, dict):
        return profile, "inline"
    return BUILTIN_SEARCH_PROFILES["default"], "default"


def tool_search_wiki(query: str, domains=None, node_types=None, max_results=10,
                     profile=None, trace=None) -> list:
    prof, _src = resolve_search_profile(profile)
    return STORE.search(query, profile=prof, trace=trace, domains=domains,
                        node_types=node_types, max_results=max_results)


def _result_vectors(result_iris):
    """Stack dense vectors for result IRIs from the embedding index, or None when
    semantic search is off (so redundancy/diversity is simply skipped)."""
    if STORE._embed_matrix is None or not STORE._embed_slugs:
        return None
    idx = {iri: i for i, iri in enumerate(STORE._embed_slugs)}
    rows = [STORE._embed_matrix[idx[i]] for i in result_iris if i in idx]
    return np.vstack(rows) if rows else None


def _estimate_cq(query):
    """C(q) estimation (the coverage-driven-traversal technique's 'Mode 1'): an
    LLM decomposes the query into the concept set a complete answer must cover,
    each resolved to a graph node IRI. The one LLM call gates the deep metrics, so
    it's computed ONCE per comparison and reused across profiles. Returns cq IRIs."""
    prompt = ("List the core concepts a complete answer to this query must cover. "
              "Return ONLY a JSON array of 3-7 short concept names, no prose.\n\n"
              f"Query: {query}")
    try:
        resp = anthropic_client.messages.create(
            model=EXTRACT_MODEL, max_tokens=200,
            messages=[{"role": "user", "content": prompt}])
        log_usage(USAGE_DB_PATH, resp, origin="pkis-mcp", project="pkis",
                  attributes={"surface": "deep-metrics"})
        txt = resp.content[0].text
        names = json.loads(txt[txt.find("["):txt.rfind("]") + 1])
    except Exception as e:  # deep metrics simply absent if C(q) can't be formed
        logger.warning(f"C(q) estimation failed: {e}")
        return []
    cq = []
    for nm in (names or [])[:8]:
        res = tool_search_wiki(str(nm), max_results=1)
        if res:
            cq.append(res[0]["iri"])
    return list(dict.fromkeys(cq))


def run_search(query, profile=None, max_results=10, comparison_id=None,
               with_metrics=True, log=True, deep_cq=None):
    """One instrumented search run: execute the profile, time retrieval vs. metric
    evaluation separately, compute the cheap reference-free metrics, and (best-
    effort) persist an experiment row. Returns the lab column dict."""
    prof, source = resolve_search_profile(profile)
    trace = {}
    t0 = time.perf_counter()
    results = STORE.search(query, profile=prof, trace=trace, max_results=max_results)
    retrieval_ms = round((time.perf_counter() - t0) * 1000, 3)

    metrics_out, eval_ms = {}, 0.0
    if with_metrics:
        te = time.perf_counter()
        iris = [r["iri"] for r in results]
        try:
            metrics_out = metrics.cheap_metrics(iris, _result_vectors(iris), STORE.get_graph())
            if deep_cq:  # C(q)-dependent dims (precomputed C(q) reused across profiles)
                toks = sum(len(r.get("excerpt") or "") for r in results) / 4.0
                metrics_out.update(metrics.deep_metrics(deep_cq, iris, STORE.get_graph(), toks))
        except Exception as ex:  # metrics must never break a search
            logger.warning(f"search metric computation failed: {ex}")
        eval_ms = round((time.perf_counter() - te) * 1000, 3)

    profile_name = (prof.get("name") if isinstance(prof, dict) else None) or source
    column = {
        "profile_name": profile_name,
        "results": results,
        "trace": trace,
        "metrics": metrics_out,
        "retrieval_ms": retrieval_ms,
        "eval_ms": eval_ms,
    }
    if log:
        experiments.log_experiment(EXPERIMENT_DB_PATH, {
            "comparison_id": comparison_id,
            "paradigm": "search",
            "query": query,
            "profile_name": profile_name,
            "profile": merge_search_profile(prof),
            "corpus_head": _content_signature(),
            "n_results": len(results),
            "retrieval_ms": retrieval_ms,
            "eval_ms": eval_ms,
            "eval_cost_usd": 0.0,
            "total_cost_usd": 0.0,
            "metrics": metrics_out,
            "trace": trace.get("stages", []),
            "payload": {"results": [
                {"iri": r["iri"], "title": r["canonical_title"], "score": r["score"]}
                for r in results
            ]},
        })
    return column


def tool_set_search_profile(name: str, profile: dict = None, reset: bool = False) -> dict:
    """WRITE-authorized: persist (or remove) a NAMED search profile to a config
    file shared across workers. reset=true deletes it; profile=<dict> saves it;
    neither reports the current resolved profile. Mirrors set_priority_config."""
    profs = _persisted_search_profiles()
    if reset:
        profs.pop(name, None)
        SEARCH_PROFILES_PATH.write_text(json.dumps(profs, indent=2))
        return {"ok": True, "removed": name, "profiles": sorted(search_profiles().keys())}
    if profile is None:
        return {"name": name, "profile": search_profiles().get(name),
                "known": sorted(search_profiles().keys())}
    prof = dict(profile)
    prof["name"] = name
    profs[name] = prof
    SEARCH_PROFILES_PATH.write_text(json.dumps(profs, indent=2))
    return {"ok": True, "saved": name, "profile": prof}


def _maybe_capture_query(query, paradigm):
    """Owner-only, best-effort: append a deliberate query to the standing test set
    (the nightly eval replays it against every profile). Never breaks the request."""
    try:
        if query and is_owner(request):
            experiments.log_query(EXPERIMENT_DB_PATH, query, paradigm=paradigm, source="owner")
    except Exception:  # noqa: BLE001
        pass


def _ask_groundedness(answer, surfaced):
    """Embedding-alignment proxy for groundedness: for each answer sentence, the
    max cosine to any surfaced node's vector, averaged. None when semantic search
    is off or there's nothing to compare."""
    ev = _result_vectors(list(surfaced or []))
    if ev is None or not answer:
        return {"groundedness": None}
    try:
        model = STORE._get_embed_model()
    except Exception:
        return {"groundedness": None}
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", answer) if len(s.strip()) > 15]
    if not sents:
        return {"groundedness": None}
    av = np.asarray(model.encode(sents, normalize_embeddings=True), dtype=np.float32)
    return metrics.groundedness(av, ev)


def _ask_cost(model_name, usage):
    rates = None
    try:
        rates = get_config(USAGE_DB_PATH)
    except Exception:
        pass  # fall back to compute_cost's built-in default rates
    try:
        return compute_cost(model_name, usage.get("input_tokens", 0),
                           usage.get("output_tokens", 0), rates=rates)
    except Exception:
        return None


def run_ask_experiment(messages, profile=None, comparison_id=None, query=None, log=True):
    """One instrumented ask run under a retrieval profile: synthesize the answer,
    score its groundedness against the surfaced nodes, tally token cost + latency,
    and (best-effort) log an ask-paradigm experiment row. Returns the lab column."""
    prof, source = resolve_search_profile(profile)
    profile_name = (prof.get("name") if isinstance(prof, dict) else None) or source
    t0 = time.perf_counter()
    result = ask.run_ask(messages, tier="owner", profile=prof)
    latency_ms = round((time.perf_counter() - t0) * 1000, 3)
    te = time.perf_counter()
    gmetrics = _ask_groundedness(result.get("answer", ""), result.get("surfaced", []))
    eval_ms = round((time.perf_counter() - te) * 1000, 3)
    usage = result.get("usage", {}) or {}
    cost = _ask_cost(result.get("model"), usage)
    column = {
        "profile_name": profile_name,
        "answer": result.get("answer", ""),
        "citations": result.get("citations", []),
        "surfaced": result.get("surfaced", []),
        "metrics": gmetrics,
        "latency_ms": latency_ms,
        "eval_ms": eval_ms,
        "cost_usd": cost,
        "usage": usage,
        "turns": result.get("turns"),
        "model": result.get("model"),
    }
    if log:
        experiments.log_experiment(EXPERIMENT_DB_PATH, {
            "comparison_id": comparison_id, "paradigm": "ask",
            "query": query or "", "profile_name": profile_name,
            "profile": merge_search_profile(prof), "corpus_head": _content_signature(),
            "n_results": len(result.get("surfaced", []) or []),
            "retrieval_ms": latency_ms, "eval_ms": eval_ms,
            "eval_cost_usd": 0.0, "total_cost_usd": cost or 0.0,
            "metrics": gmetrics, "trace": [],
            "payload": {"answer": result.get("answer", ""),
                        "citations": result.get("citations", []),
                        "surfaced": result.get("surfaced", [])},
        })
    return column


def tool_search_wiki_index(query: str) -> list:
    """Fast keyword-only index scan, no LLM involvement."""
    if STORE._bm25_index is None:
        STORE.build_bm25_index()
    tokens = query.lower().split()
    scores = STORE._bm25_index.get_scores(tokens)
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:20]
    all_nodes = {n["iri"]: n for n in load_all_nodes()}
    results = []
    for idx, score in ranked:
        if score <= 0:
            continue
        iri = STORE._bm25_slugs[idx]
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
    """Reading queue as a pre-ingestion CAPTURE inbox (B10). Ordering is derived from
    the concept frontier — a queued item's priority is its subject's frontier
    priority_score — NOT the old manual high/normal tag, which is now only a
    capture-time `hint`. Items whose subject the frontier can't see (un-ingested, the
    common case) carry frontier_score=None and sort after scored items, by capture
    order. `priority` arg still filters by the recorded hint for back-compat.

    Parses BOTH the new flat format and the legacy `### High`/`### Normal` sections
    (the section becomes the item's hint), so old queue.md files keep working."""
    queue_path = WIKI_DIR / "queue.md"
    if not queue_path.exists():
        return []

    scores = _frontier_score_by_slug()
    items = []
    section_hint = None  # legacy section → hint
    for line in queue_path.read_text().split("\n"):
        s = line.strip()
        if s.startswith("### High"):
            section_hint = "high"; continue
        if s.startswith("### Normal"):
            section_hint = "normal"; continue
        if s.startswith("## "):
            section_hint = None; continue
        if not s.startswith("- [ ]"):
            continue
        m = re.match(r'- \[ \] (?:\[\[([^\]]+)\]\]|([^—]+?))(?:\s*—\s*(.+))?$', s)
        if not m:
            continue
        slug = (m.group(1) or m.group(2) or "").strip()
        tail = (m.group(3) or "").strip()
        # Pull an inline `(hint: high)` and `(captured: YYYY-MM-DD)` out of the tail.
        hint = section_hint
        hm = re.search(r'\(hint:\s*(high|normal)\)', tail)
        if hm:
            hint = hm.group(1)
        cm = re.search(r'\(captured:\s*([0-9-]+)\)', tail)
        captured = cm.group(1) if cm else None
        reason = re.sub(r'\s*\((?:hint|captured):[^)]*\)', '', tail).strip()
        if priority and (hint or "normal") != priority.lower():
            continue
        items.append({
            "slug": slug,
            "reason": reason,
            "hint": hint,                       # demoted manual tag (informational)
            "captured": captured,
            "frontier_score": scores.get(slug),  # primary ordering signal; None if unseen
            "capture_order": len(items),
        })

    # Collapse duplicate captures of the same slug (the queue is an append log, so the
    # same source can be recorded more than once). Keep the richest entry: prefer a
    # 'high' hint, then the longest reason, then the earliest capture; always carry the
    # earliest capture_order forward so unscored items keep a stable order.
    by_slug = {}
    for it in items:
        if not it["slug"]:
            continue
        prev = by_slug.get(it["slug"])
        if prev is None:
            by_slug[it["slug"]] = it
            continue
        earliest = min(prev["capture_order"], it["capture_order"])
        better = (((it.get("hint") == "high") - (prev.get("hint") == "high"))
                  or (len(it.get("reason") or "") - len(prev.get("reason") or ""))
                  or (prev["capture_order"] - it["capture_order"]))
        winner = it if better > 0 else prev
        winner["capture_order"] = earliest
        by_slug[it["slug"]] = winner
    items = list(by_slug.values())

    # Frontier score drives ordering; un-ingested (None) fall to the back in capture order.
    items.sort(key=lambda it: (it["frontier_score"] is not None,
                               it["frontier_score"] or 0.0,
                               -it["capture_order"]),
               reverse=True)
    for it in items:
        it.pop("capture_order", None)
    return items


def tool_add_to_queue(source_iri=None, reference=None, reason="", priority="normal") -> dict:
    """Capture a source into the reading queue (a flat, pre-ingestion inbox — B10).
    Ordering is the frontier's job (see get_reading_queue); `priority` is recorded
    only as a capture-time `hint`, no longer a High/Normal section."""
    queue_path = WIKI_DIR / "queue.md"
    if not queue_path.exists():
        queue_path.write_text("# Reading Queue\n\nCapture inbox — ordering is derived "
                              "from the concept frontier (see get_reading_queue).\n\n## Queue\n")

    content = queue_path.read_text()
    if "## Queue" not in content:  # legacy file (### High/### Normal) → add a flat section
        content += "\n## Queue\n"

    target = source_iri and f"[[{parse_iri(source_iri)[2]}]]" or reference
    # Idempotent capture: if this source is already queued, don't append a duplicate
    # (the queue is an append log; re-capturing the same source used to compound it).
    slug_check = source_iri and parse_iri(source_iri)[2] or (reference or "")
    if slug_check and re.search(r'- \[ \].*' + re.escape(slug_check), content):
        return {"success": True, "entry": None, "skipped": "already queued",
                "priority": priority, "hint": priority}
    captured = datetime.now(timezone.utc).date().isoformat()
    annot = f" (captured: {captured})"
    if priority and priority.lower() == "high":
        annot += " (hint: high)"
    entry = f"- [ ] {target} — {reason}{annot}"

    # Append under the flat ## Queue section.
    content = content.replace("## Queue", f"## Queue\n{entry}", 1)
    queue_path.write_text(content)
    return {"success": True, "entry": entry, "priority": priority, "hint": priority}


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
    results, anchors = _compute_frontier(eff_weight)
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


def _compute_frontier(eff_weight: float):
    """Score every node for reading priority (centrality + coverage/understanding
    gaps + cluster-frontier proximity). Returns (results_list, anchors). Shared by
    get_concept_frontier (top-20) and the reading queue (B10: queued items are
    ordered by their subject's frontier score)."""
    nodes = load_all_nodes()
    G = get_graph()
    anchors = _active_frontier_anchors(nodes)
    proximity = _cluster_proximity_map(G, anchors)

    results = []
    for node in nodes:
        iri = node["iri"]
        coverage = node.get("coverage", 0)
        understanding = node.get("understanding", 0)
        inbound_count = G.in_degree(iri) if iri in G else 0
        cluster_proximity = proximity.get(iri, 0.0)
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
            "node_type": node.get("frontmatter", {}).get("knowledge_type")
                         or FOLDER_TO_TYPE.get(node.get("node_type", ""), node.get("node_type", "")),
            "domain": node.get("domain", []),
        })
    return results, anchors


def _frontier_score_by_slug() -> dict:
    """{slug: priority_score} over all nodes, for ordering queued items by their
    subject's frontier priority. Empty scores degrade to capture-order in the queue."""
    eff_weight, _ = _effective_proximity_weight(None)
    results, _ = _compute_frontier(eff_weight)
    out = {}
    for r in results:
        _, _, slug = parse_iri(r["iri"])
        if slug:
            out[slug] = r["priority_score"]
    return out


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


def _norm_source_ref(ref) -> str:
    """A concept's `sources` entry may be a bare slug, a [[wikilink]], or an IRI —
    normalise to the source slug."""
    s = str(ref or "").strip()
    if s.startswith("[[") and s.endswith("]]"):
        s = s[2:-2]
    s = s.split("|")[0].strip()
    if ":" in s:
        s = s.split(":")[-1]
    return s.strip().lstrip("/")


def _active_cluster_gaps(nodes, G, by_iri) -> dict:
    """{concept_iri: cluster_title} for the coverage-gap concepts of ACTIVE clusters
    (frontier-hypothesis dependencies). Used to flag which concepts are load-bearing
    for live research."""
    gaps = {}
    clusters = [n for n in nodes
                if n.get("frontmatter", {}).get("knowledge_type") == "research-cluster"
                and n.get("frontmatter", {}).get("status") == "active"]
    for c in clusters:
        fm = c["frontmatter"]
        ctitle = fm.get("title", c["slug"])
        for h_slug in (fm.get("frontier_hypotheses") or []):
            hp = find_node_path(h_slug)
            if not hp:
                continue
            for _u, v, d in G.edges(load_node(hp)["iri"], data=True):
                if d.get("edge_type") == "related":
                    continue
                tn = by_iri.get(v)
                if tn and tn.get("frontmatter", {}).get("knowledge_type", "") not in ("research-cluster", "hypothesis"):
                    gaps.setdefault(v, ctitle)
    return gaps


_CONCEPT_KINDS = ("concept", "technique", "result", "principle", "framework", "problem")


def _source_concept_map(nodes, G, by_iri) -> dict:
    """{source_slug: [{concept, concept_iri, coverage, is_gap, cluster}]} — every
    concept that cites a source via its `sources`, i.e. what reading it informs.
    Concepts that are active-cluster frontier gaps are flagged is_gap (+cluster) and
    sorted first (the load-bearing ones). This drives the Priority 'why read it' and
    the source research-relevance panel."""
    gaps = _active_cluster_gaps(nodes, G, by_iri)
    out = {}
    for cn in nodes:
        if cn.get("frontmatter", {}).get("knowledge_type", "") not in _CONCEPT_KINDS:
            continue
        for sref in (cn.get("frontmatter", {}).get("sources") or []):
            sslug = _norm_source_ref(sref)
            if not sslug:
                continue
            out.setdefault(sslug, []).append({
                "concept": cn["title"], "concept_iri": cn["iri"],
                "coverage": cn.get("coverage", 0),
                "is_gap": cn["iri"] in gaps, "cluster": gaps.get(cn["iri"]),
            })
    for k, lst in out.items():        # dedupe; gaps first, then lowest-coverage
        seen, uniq = set(), []
        for it in sorted(lst, key=lambda x: (not x["is_gap"], x["coverage"])):
            if it["concept_iri"] not in seen:
                seen.add(it["concept_iri"])
                uniq.append(it)
        out[k] = uniq
    return out


def _source_relevance(slug: str) -> dict:
    """Standalone (loads nodes/graph) — the research-relevance of one source for the
    detail panel: the concepts it informs (gaps flagged) + its frontier score."""
    nodes = load_all_nodes()
    G = get_graph()
    by_iri = {n["iri"]: n for n in nodes}
    serves = _source_concept_map(nodes, G, by_iri).get(slug, [])
    return {"slug": slug, "serves": serves, "frontier_score": _frontier_score_by_slug().get(slug)}


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
    # Enrich the reading queue with the "why read it" linkage (reuse the nodes/graph
    # already loaded above) + the real source title.
    serves_map = _source_concept_map(nodes, G, by_iri)
    rq = tool_get_reading_queue()
    for item in rq:
        sp = find_node_path(item["slug"])
        item["title_full"] = (load_node(sp) or {}).get("title") if sp else None
        item["serves"] = serves_map.get(item["slug"], [])[:3]
    return {
        "params": {"cluster_proximity_weight": eff_w, "weight_source": src},
        "clusters": sorted(groups, key=lambda x: x["cluster_slug"]),
        "reading_queue": rq,
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


def _cluster_member_iris(cluster_slug: str) -> set:
    """Member nodes of a research cluster: its typed-edge dep targets plus its
    hypotheses — mirrors the membership shown by tool_get_clusters so the browse
    facet matches the Clusters view exactly."""
    cpath = find_node_path(cluster_slug)
    if not cpath:
        return set()
    cnode = load_node(cpath)
    G = get_graph()
    members = set()
    for _u, v, d in G.edges(cnode["iri"], data=True):
        if d.get("edge_type") == "related":
            continue
        members.add(v)
    for h_slug in cnode.get("frontmatter", {}).get("hypotheses", []) or []:
        hp = find_node_path(h_slug)
        if hp:
            members.add(load_node(hp)["iri"])
    return members


def tool_get_index(domain=None, node_type=None, cluster=None) -> list:
    nodes = load_all_nodes()
    member_iris = _cluster_member_iris(cluster) if cluster else None
    results = []
    for node in nodes:
        singular = FOLDER_TO_TYPE.get(node["node_type"], node["node_type"])
        if member_iris is not None and node["iri"] not in member_iris:
            continue
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


def _viz_title(slug: str) -> str:
    """The explainer's own <title>, for the gallery (falls back to the slug)."""
    p = WIKI_DIR / "assets" / "viz" / f"{slug}.html"
    try:
        m = re.search(r"<title>(.*?)</title>", p.read_text(errors="ignore"), re.I | re.S)
        return m.group(1).strip() if m else slug
    except Exception:
        return slug


def tool_get_assets(kind: str = None) -> list:
    """Asset nodes — anything the owner authors. `format` is how it renders:
    'interactive' (an HTML `viz:` — explainers/visualizations) or 'writing' (the
    node's markdown body — e.g. a position-paper). `kind` is the open genre
    (controlled by wiki/asset_kinds.json), optionally used to filter. Powers the
    viewer's Assets gallery; the full node (incl. prose body) is in get_node.
    `illustrates` = how many nodes link here via `illustrated-by`."""
    G = get_graph()
    out = []
    for n in load_all_nodes():
        if n.get("node_type") != "assets":
            continue
        fm = n.get("frontmatter", {})
        viz = fm.get("viz")
        k = fm.get("kind") or ("explainer" if viz else "writing")
        if kind and k != kind:
            continue
        # `format` is explicit when set; otherwise inferred (a viz ⇒ interactive).
        fmt = fm.get("format") or ("interactive" if viz else "writing")
        iri = n["iri"]
        illustrates = 0
        if iri in G:
            illustrates = sum(
                1 for p in G.predecessors(iri)
                if (G.get_edge_data(p, iri) or {}).get("edge_type") == "illustrated-by"
            )
        title = n.get("title", n["slug"])
        out.append({
            "iri": iri,
            "title": title,
            "kind": k,
            "format": fmt,
            "viz": viz or "",
            "viz_title": _viz_title(viz) if viz else title,
            # An explicit `viz_url` in frontmatter promotes a Tier-2 dynamic
            # explainer (Flask-backed, e.g. /pkis-api/x/<name>/); otherwise derive
            # the static-file URL from `viz`. Writing assets have no viz_url.
            "viz_url": n.get("viz_url") or (f"/pkis-api/viz/{viz}.html" if viz else None),
            "domain": n.get("domain", []),
            "illustrates": illustrates,
            "excerpt": (n.get("content") or "").strip()[:200],
        })
    out.sort(key=lambda x: x["title"].lower())
    return out


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


def _lab_monitor_mod():
    """Lazy-load tools/lab_monitor.py (kept decoupled from app for cheap scheduling)."""
    tools_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tools")
    if tools_dir not in sys.path:
        sys.path.insert(0, tools_dir)
    import lab_monitor
    return lab_monitor


def tool_get_lab_report() -> dict:
    """The PKIS Lab Assistant's known analytical access point: a DESCRIPTIVE snapshot
    of the wiki's research-data health (node counts, coverage, hypothesis-status
    distribution, cluster staleness, staged-node throughput) computed live, plus drift
    flags vs the most recent stored monitoring snapshot. Read-only and descriptive — it
    never evaluates hypotheses, changes research state, or asserts causality."""
    lm = _lab_monitor_mod()
    snapshot = lm.compute_snapshot(WIKI_DIR, REPO_DIR)
    lab_dir = Path(os.environ.get("PKIS_LAB_DIR", "/home/pkis/lab"))
    prev = lm.load_previous(lab_dir)
    return {
        "snapshot": snapshot,
        "drift_flags": lm.detect_drift(prev, snapshot),
        "previous_snapshot_at": (prev or {}).get("generated_at"),
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
        "review_url": f"{REPO_WEB_BASE}/blob/main/wiki/staging/{staged_path.name}",
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
        "review_url": f"{REPO_WEB_BASE}/blob/main/wiki/staging/{staged_path.name}",
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
        "review_url": f"{REPO_WEB_BASE}/blob/main/wiki/staging/{staged_path.name}",
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
        "review_url": f"{REPO_WEB_BASE}/blob/main/wiki/staging/{staged_path.name}",
    }


def tool_create_finding_stub(
    finding_id: str = "",
    generated_at: str = "",
    hypothesis_ref: str = "",
    summary: str = "",
    statistics: dict = None,
    stratification: dict = None,
    source_pointer: dict = None,
    slug: str = "",
) -> dict:
    """Accept a SCRUBBED, AGGREGATE finding object produced by an external experimental
    system (initially OpGraph) and stage it as a `finding` node attached to a live PKIS
    hypothesis via an `evidence-for` edge. This is a narrow, content-restricted inbound
    gate — PKIS stays unaware of the producing system beyond "accept an object matching
    this schema."

    Trust boundary (deliberate): PKIS validates ONLY (a) schema conformance and (b) that
    `hypothesis_ref` resolves to an existing LIVE hypothesis. It does NOT recompute or
    verify the statistics, and does NOT scrub for identifying content — the producer is
    responsible for scrubbing (it alone holds the entity registry), and the human staging
    review is the actual content gate. Promote via commit_staged_node (lands in
    wiki/findings/)."""
    statistics = statistics or {}
    stratification = stratification or {}
    source_pointer = source_pointer or {}

    # ---- (a) schema conformance ----
    missing = [f for f, v in (
        ("finding_id", finding_id), ("generated_at", generated_at),
        ("hypothesis_ref", hypothesis_ref), ("summary", summary),
    ) if not v]
    if missing:
        raise ValueError(f"finding object missing required field(s): {', '.join(missing)}")
    if not isinstance(statistics, dict) or not statistics:
        raise ValueError("statistics must be a non-empty object")
    if not isinstance(stratification, dict):
        raise ValueError("stratification must be an object")
    if not isinstance(source_pointer, dict) or not source_pointer.get("system"):
        raise ValueError("source_pointer must be an object with at least a 'system' field")

    # ---- (b) hypothesis_ref must resolve to a LIVE hypothesis ----
    try:
        _ns, _ntype, hyp_slug = parse_iri(hypothesis_ref)
    except Exception:
        raise ValueError(f"hypothesis_ref is not a valid IRI: {hypothesis_ref!r}")
    if _ntype != "hypothesis":
        raise ValueError(f"hypothesis_ref must be a hypothesis IRI (pkis:hypothesis:...); got {hypothesis_ref!r}")
    hyp_path = find_node_path_by_iri(hypothesis_ref)
    if not hyp_path:
        raise ValueError(f"hypothesis_ref does not resolve to a live node: {hypothesis_ref}")
    # inherit domain from the target hypothesis so the finding shares its facets
    try:
        hyp_domain = frontmatter.load(str(hyp_path)).metadata.get("domain", []) or []
    except Exception:
        hyp_domain = []

    # ---- slug: deterministic + collision-safe ----
    strategy = str(statistics.get("strategy", "")).strip()
    metric = str(statistics.get("metric", "")).strip()
    gen_date = (generated_at or "")[:10]
    base = "-".join(p for p in ["finding", hyp_slug, strategy, metric, gen_date] if p)
    base_slug = re.sub(r'[^a-z0-9]+', '-', base.lower()).strip('-')[:70] or "finding-stub"
    slug = slug or base_slug
    counter = 1
    while (STAGING_DIR / f"{slug}.md").exists() or find_node_path(slug):
        slug = f"{base_slug}-{counter}"
        counter += 1

    staged_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc)
    ts_str = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    date_str = now.strftime("%Y-%m-%d")

    comparison = str(statistics.get("comparison_strategy", "")).strip()
    title_core = f"{strategy} vs {comparison}" if (strategy and comparison) else (strategy or "result")
    title = f"Finding: {title_core}{f' — {metric}' if metric else ''}"
    source_system = source_pointer.get("system", "")
    tags = [t for t in [source_system, strategy] if t]

    fm = {
        "staged_at": ts_str,
        "staged_by": "mcp-create-finding-stub",
        "staged_id": staged_id,
        "review_status": "pending",
        "proposed_edges": [],
        "id": f"pkis:finding:{slug}",
        "aliases": [],
        "title": title,
        "knowledge_type": "finding",
        "domain": hyp_domain,
        "tags": tags,
        "date_created": date_str,
        "date_updated": date_str,
        "maturity": "evolving",
        "finding_id": finding_id,
        "generated_at": generated_at,
        "summary": summary,
        "statistics": statistics,
        "stratification": stratification,
        "source_system": source_system,
        "source_run_id": source_pointer.get("run_id", ""),
        "source_log_date_range": source_pointer.get("log_date_range", []),
        "evidence-for": [hyp_slug],
    }

    stats_lines = "\n".join(f"- **{k}**: {v}" for k, v in statistics.items()) or "[none]"
    strat_lines = "\n".join(f"- **{k}**: {v}" for k, v in stratification.items()) or "[none]"
    body = f"""## Summary
{summary}

## Statistics
{stats_lines}

**Stratification:**
{strat_lines}

## Provenance
- **Source system:** {source_system or '[unknown]'}
- **Run ID:** {source_pointer.get('run_id', '') or '[none]'}
- **Log date range:** {source_pointer.get('log_date_range', []) or '[none]'}
- **Generated at:** {generated_at}
- **Finding ID:** {finding_id}

PKIS validated only the schema and that the target hypothesis is live; it did not
recompute or verify these statistics. Trust is established at human staging review.

## Connections
- [[{hyp_slug}]] — evidence-for: empirical evidence bearing on this hypothesis
"""

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    staged_path = STAGING_DIR / f"{slug}.md"
    staged_path.write_text(f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)}---\n\n{body}")

    log_path = WIKI_DIR / "log.md"
    with open(log_path, "a") as lf:
        lf.write(
            f"\n## [{date_str}] staged | finding\n"
            f"- Staged: {slug} (id: {staged_id})\n"
            f"- Evidence for: {hyp_slug}\n"
            f"- Source: {source_system or '(unknown)'} run {source_pointer.get('run_id', '') or '(none)'}\n"
        )

    return {
        "staged_id": staged_id,
        "staged_at": ts_str,
        "slug": slug,
        "iri": f"pkis:finding:{slug}",
        "knowledge_type": "finding",
        "hypothesis_ref": hypothesis_ref,
        "review_url": f"{REPO_WEB_BASE}/blob/main/wiki/staging/{staged_path.name}",
    }


RESOURCE_TYPE_VOCAB = ["library", "tool", "platform", "dataset", "documentation", "service"]
RESOURCE_STATUS_VOCAB = ["active", "unmaintained", "deprecated", "archived"]


def tool_create_resource_stub(
    title: str = "",
    resource_url: str = "",
    resource_type: str = "",
    status: str = "active",
    last_evaluated: str = "",
    technological_scope: list = None,
    domain: list = None,
    tags: list = None,
    definition: str = "",
    summary: str = "",
    relationship_candidates: str = "",
    aliases: list = None,
    slug: str = "",
) -> dict:
    """Stage a `resource` node — an external tool, library, platform, dataset,
    documentation site, or service with a development/maintenance lifecycle. A resource
    is epistemically distinct from a `source`: it backs "this exists and does X", not
    "this claim is established". The URL is taken AS-IS — no CrossRef/arXiv/Semantic
    Scholar enrichment. Operational deployment lives in OpGraph, not here. Body carries
    ## Summary + ## Relationship Candidates (never ## Key Concepts). Promote via
    commit_staged_node (lands in wiki/resources/)."""
    if not title:
        raise ValueError("title is required")
    if not resource_url:
        raise ValueError("resource_url is required for a resource")
    resource_type = (resource_type or "").strip()
    if resource_type and resource_type not in RESOURCE_TYPE_VOCAB:
        raise ValueError(f"resource_type must be one of {RESOURCE_TYPE_VOCAB}; got {resource_type!r}")
    status = (status or "active").strip()
    if status not in RESOURCE_STATUS_VOCAB:
        raise ValueError(f"status must be one of {RESOURCE_STATUS_VOCAB}; got {status!r}")

    domain = domain or []
    tags = tags or []
    aliases = aliases or []
    technological_scope = technological_scope or []

    now = datetime.now(timezone.utc)
    ts_str = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    date_str = now.strftime("%Y-%m-%d")
    last_evaluated = last_evaluated or date_str

    base = slug or title
    base_slug = re.sub(r'[^a-z0-9]+', '-', base.lower()).strip('-')[:60] or "resource-stub"
    slug = base_slug
    counter = 1
    while (STAGING_DIR / f"{slug}.md").exists() or find_node_path(slug):
        slug = f"{base_slug}-{counter}"
        counter += 1

    staged_id = str(uuid.uuid4())
    fm = {
        "staged_at": ts_str,
        "staged_by": "mcp-create-resource-stub",
        "staged_id": staged_id,
        "review_status": "pending",
        "proposed_edges": [],
        "id": f"pkis:resource:{slug}",
        "aliases": aliases,
        "title": title,
        "knowledge_type": "resource",
        "domain": domain,
        "tags": tags,
        "date_created": date_str,
        "date_updated": date_str,
        "maturity": "evolving",
        "resource_url": resource_url,
        "resource_type": resource_type or None,
        "status": status,
        "last_evaluated": last_evaluated,
        "technological_scope": technological_scope,
        "understanding": 0,
    }

    body = f"""## Summary
{summary or definition or '[To be filled — what it does, the problem it solves, dependencies, caveats]'}

## Relationship Candidates
{relationship_candidates or '[To be populated — which concepts/techniques this implements or applies; resources it depends on or competes with]'}
"""

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    staged_path = STAGING_DIR / f"{slug}.md"
    staged_path.write_text(f"---\n{yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)}---\n\n{body}")

    log_path = WIKI_DIR / "log.md"
    with open(log_path, "a") as lf:
        lf.write(
            f"\n## [{date_str}] staged | resource\n"
            f"- Staged: {slug} (id: {staged_id})\n"
            f"- URL: {resource_url}\n"
            f"- Type: {resource_type or '(unset)'} | status: {status}\n"
        )

    return {
        "staged_id": staged_id,
        "staged_at": ts_str,
        "slug": slug,
        "iri": f"pkis:resource:{slug}",
        "knowledge_type": "resource",
        "resource_url": resource_url,
        "review_url": f"{REPO_WEB_BASE}/blob/main/wiki/staging/{staged_path.name}",
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
    content: str = None,
    commit_message: str = "",
) -> dict:
    """Edit a LIVE node's frontmatter fields and/or body, then commit + push.
    - frontmatter_updates: {field: value} merged into frontmatter (a null value deletes the field).
    - section_updates: {"Section Title": "new markdown body"} — replaces the body under that
      `## Section Title` heading, or appends the section if absent.
    - content: if provided, REPLACES the entire body (used by the viewer's edit sheet, which
      edits the whole markdown). Mutually exclusive in spirit with section_updates.
    Covers what add_connections cannot (e.g. a cluster's frontier_hypotheses + Current Frontier).
    date_updated is bumped automatically."""
    frontmatter_updates = frontmatter_updates or {}
    section_updates = section_updates or {}
    if not frontmatter_updates and not section_updates and content is None:
        raise ValueError("nothing to edit: provide frontmatter_updates, section_updates, and/or content")

    path = None
    if iri:
        path = find_node_path_by_iri(iri)
    if not path and slug:
        path = find_node_path(slug)
    if not path:
        raise ValueError(f"node not found: {iri or slug}")

    post = frontmatter.load(str(path))
    fm = dict(post.metadata)
    body = post.content if content is None else content   # full-body replace when content given

    for k, v in frontmatter_updates.items():
        if v is None:
            fm.pop(k, None)
        else:
            fm[k] = v

    for title, body_text in section_updates.items():
        body = _replace_section(body, title, body_text)

    fm["date_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    new_post = frontmatter.Post(body, **fm)
    path.write_text(frontmatter.dumps(new_post))

    # Invalidate caches so the next read/graph reflects the edit
    STORE.invalidate_nodes()
    STORE.invalidate_graph()

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

    msg = commit_message or f"[mcp-edit] {iri_final}"
    git = _git_commit_and_push([path, log_path], msg)

    return {
        "status": "edited",
        "iri": iri_final,
        "path": str(rel),
        "frontmatter_updated": list(frontmatter_updates),
        "sections_updated": list(section_updates),
        "git_commit": git["sha"],
        "git_pushed": git["pushed"],
        "url": f"{REPO_WEB_BASE}/blob/main/wiki/{rel}",
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
    STORE.invalidate_nodes()
    STORE.invalidate_graph()

    added = [r for r in results if r["status"] == "added"]
    git = {"sha": "", "pushed": False}
    if modified_paths:
        msg = commit_message or f"[mcp-edge] add {len(added)} connection(s)"
        git = _git_commit_and_push(list(modified_paths), msg)

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
        "git_commit": git["sha"],
        "git_pushed": git["pushed"],
        "results": results,
    }


# ============================================================
# Documentation system — docs/ lives in the MAIN repo (DOCS_REPO_DIR), which on the
# server is DISTINCT from the wiki REPO_DIR the other write tools commit to. Reads are
# surfaced in the viewer's Docs view; log_idea appends to docs/IDEAS.md.
# ============================================================

def _docs_manifest() -> list:
    """Load docs/manifest.json — a list of {key, title, category, path} entries."""
    try:
        data = json.loads((DOCS_REPO_DIR / "docs" / "manifest.json").read_text())
        return [d for d in data.get("docs", []) if d.get("key") and d.get("path")]
    except Exception as e:
        logger.warning(f"docs manifest unreadable: {e}")
        return []


def tool_list_docs() -> list:
    """Return the docs manifest (key, title, category, path) for the viewer Docs nav.
    `path` lets the viewer resolve relative cross-links (e.g. [..](USAGE.md)) to keys."""
    return [{"key": d["key"], "title": d["title"],
             "category": d.get("category", ""), "path": d["path"]}
            for d in _docs_manifest()]


def tool_get_doc(key: str) -> dict:
    """Return one doc's markdown by manifest key. Manifest-gated: only files listed in
    the manifest are readable, and the resolved path must stay within DOCS_REPO_DIR."""
    entry = next((d for d in _docs_manifest() if d["key"] == key), None)
    if not entry:
        raise ValueError(f"unknown doc key: {key}")
    base = DOCS_REPO_DIR.resolve()
    path = (base / entry["path"]).resolve()
    if base not in path.parents and path != base or not path.is_file():
        raise ValueError(f"doc not found: {key}")
    return {"key": key, "title": entry["title"],
            "category": entry.get("category", ""), "markdown": path.read_text()}


def _openwiki_pages() -> list:
    """All markdown page paths under OPENWIKI_DIR, as sorted repo-relative-to-openwiki
    strings (e.g. 'architecture/server.md', 'testing.md'). Dotfiles are skipped."""
    base = OPENWIKI_DIR.resolve()
    if not base.is_dir():
        return []
    return sorted(
        str(p.relative_to(base))
        for p in base.rglob("*.md")
        if p.is_file() and not any(part.startswith(".") for part in p.relative_to(base).parts)
    )


def tool_get_openwiki(page: str = None) -> dict:
    """Read the generated OpenWiki code map (read-only). With no `page`, return
    quickstart.md plus the list of all available page paths under openwiki/. With a
    `page`, return that page's markdown. Path-restricted to OPENWIKI_DIR: the resolved
    path must stay inside it (no '..', no absolute escapes)."""
    base = OPENWIKI_DIR.resolve()
    page = (page or "").strip()

    if not page:
        quickstart = base / "quickstart.md"
        markdown = quickstart.read_text() if quickstart.is_file() else ""
        return {"page": "quickstart.md", "markdown": markdown, "pages": _openwiki_pages()}

    # Reject absolute paths outright; resolve the rest under the openwiki base and
    # confirm containment so traversal ('../', symlink escapes) can't read outside it.
    if Path(page).is_absolute():
        raise ValueError(f"invalid openwiki page: {page}")
    path = (base / page).resolve()
    if not (path == base or base in path.parents) or not path.is_file():
        raise ValueError(f"openwiki page not found: {page}")
    return {"page": str(path.relative_to(base)), "markdown": path.read_text(),
            "pages": _openwiki_pages()}


def _docs_repo_branch() -> str:
    try:
        r = subprocess.run(["git", "-C", str(DOCS_REPO_DIR), "rev-parse", "--abbrev-ref", "HEAD"],
                           capture_output=True, text=True, timeout=10)
        return r.stdout.strip() or "main"
    except Exception:
        return "main"


def _commit_docs(paths, message) -> tuple:
    """git add/commit/push the given paths in DOCS_REPO_DIR. Returns (sha, pushed).
    Routes through the single _git_commit_and_push path, so a push failure raises
    GitPushError (loud) rather than silently retaining a diverging local commit."""
    git = _git_commit_and_push(paths, message, repo_dir=DOCS_REPO_DIR)
    return git["sha"], git["pushed"]


def tool_log_idea(title: str, idea: str, source: str = "",
                  relation_to_system: str = "", open_questions: str = "") -> dict:
    """Append an idea to docs/IDEAS.md (newest-first) in the MAIN repo and commit+push.
    Does NOT promote to DECISIONS.md — that stays a deliberate human action."""
    title = (title or "").strip()
    idea = (idea or "").strip()
    if not title or not idea:
        raise ValueError("title and idea are required")
    source = (source or "").strip() or f"Claude Code: {_docs_repo_branch()}"
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    entry = (
        f"## {title}\n"
        f"**Date logged:** {today}\n"
        f"**Source:** {source}\n"
        f"**Idea:** {idea}\n"
        f"**Relation to existing system:** {(relation_to_system or '').strip() or '—'}\n"
        f"**Open questions:** {(open_questions or '').strip() or '—'}\n"
        f"**Status:** open\n"
    )

    ideas_path = DOCS_REPO_DIR / "docs" / "IDEAS.md"
    if not ideas_path.is_file():
        raise ValueError("docs/IDEAS.md not found")
    content = ideas_path.read_text()

    # Prepend under the preamble: insert just after the '---' separator that closes
    # the format block, so new entries land at the top of the list (newest-first).
    marker = "\n---\n"
    idx = content.find(marker)
    if idx != -1:
        cut = idx + len(marker)
        new_content = content[:cut] + "\n" + entry + "\n" + content[cut:]
    else:
        new_content = content.rstrip() + "\n\n---\n\n" + entry
    ideas_path.write_text(new_content)

    git_sha, git_pushed = _commit_docs([ideas_path], f"[ideas] log: {title}")
    return {"logged": title, "date": today, "entry": entry,
            "git_commit": git_sha, "git_pushed": git_pushed}


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
    STORE.invalidate_nodes()

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

    # Git commit and push — single consolidated path; loud (GitPushError) on push failure.
    git = _git_commit_and_push(
        [target_path, index_path, log_path],
        f"[mcp-commit] {knowledge_type}: {fm.get('title', slug)[:60]}",
    )

    return {
        "status": "committed",
        "iri": iri,
        "git_commit": git["sha"],
        "git_pushed": git["pushed"],
        "url": f"{REPO_WEB_BASE}/blob/main/wiki/{folder}/{slug}.md",
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
            # Bridge-note review context: resolve each referenced node so the inbox
            # can show why the note exists AND which links exist vs. need resolving
            # (the "node shows as not existing" confusion). Cheap — staged sets are
            # small and this is just a path lookup per ref, no search.
            links = []
            for ref in (fm.get("linked_nodes") or []):
                p = find_node_path(ref)
                iri = (load_node(p) or {}).get("iri") if p else None
                links.append({"ref": ref, "iri": iri, "exists": bool(iri)})
            results.append({
                "staged_id": fm.get("staged_id"),
                "slug": staged_file.stem,
                "node_type": fm.get("knowledge_type") or fm.get("type") or "unknown",
                "staged_at": fm.get("staged_at", ""),
                "staged_by": fm.get("staged_by", ""),
                "title": fm.get("title", staged_file.stem),
                "review_status": fm.get("review_status", "pending"),
                "description": first_line,
                "rationale": fm.get("rationale", ""),
                "proposed_edge_type": fm.get("proposed_edge_type") or fm.get("edge_type") or "related",
                "links": links,
                "review_url": f"{REPO_WEB_BASE}/blob/main/wiki/staging/{staged_file.name}",
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


def _current_branch(repo: str) -> str:
    r = subprocess.run(["git", "-C", repo, "rev-parse", "--abbrev-ref", "HEAD"],
                       capture_output=True, text=True)
    return r.stdout.strip() or "main"


def _git_push_diagnostics(repo: str, branch: str, sha: str, message: str) -> dict:
    """Read-only divergence snapshot after a failed push: ahead/behind counts,
    the diverging commits each way, a --stat diff, and a recommended remediation.
    Never mutates the repo (a fetch is read-only)."""
    def _run(args):
        return subprocess.run(["git", "-C", repo] + args, capture_output=True, text=True)

    remote_ref = f"origin/{branch}"
    fetch = _run(["fetch", "origin", branch])
    behind = ahead = None
    counts = _run(["rev-list", "--left-right", "--count", f"{remote_ref}...HEAD"])
    if counts.returncode == 0 and len(counts.stdout.split()) == 2:
        behind, ahead = (int(x) for x in counts.stdout.split())
    local_unpushed = _run(["log", "--oneline", f"{remote_ref}..HEAD"]).stdout.strip()
    remote_only = _run(["log", "--oneline", f"HEAD..{remote_ref}"]).stdout.strip()
    diffstat = _run(["diff", "--stat", f"{remote_ref}...HEAD"]).stdout.strip()

    if fetch.returncode != 0:
        rec = ("remote unreachable (fetch failed) — the commit is retained locally; "
               "retry the push when connectivity returns. Inspect with "
               "`tools/reconcile_push.py`.")
    elif behind and ahead:
        rec = (f"history diverged (local +{ahead}, origin +{behind}) — review the "
               f"origin-only commits, then `tools/reconcile_push.py --confirm` to "
               f"rebase local onto origin and re-push.")
    elif ahead and not behind:
        rec = ("origin is not ahead — push likely failed on network / lock / hook. "
               "Retry with `tools/reconcile_push.py` (inspect first; --confirm to push).")
    else:
        rec = "push failed — run `tools/reconcile_push.py` to inspect and reconcile."

    return {
        "repo": repo, "branch": branch, "sha": sha, "commit_message": message,
        "fetch_ok": fetch.returncode == 0, "behind": behind, "ahead": ahead,
        "local_unpushed": local_unpushed, "remote_only": remote_only,
        "diffstat": diffstat, "push_error": "", "recommendation": rec,
    }


def _git_commit_and_push(files: list, message: str, repo_dir=None) -> dict:
    """THE single git-write path for every write tool (Seam C consolidation).

    Stages `files`, commits, and pushes in `repo_dir` (default REPO_DIR). Returns
    {"committed": bool, "sha": str, "pushed": True}; an idempotent write with no
    changes returns committed=False, pushed=True (nothing to send).

    Raises GitPushError if the commit succeeds but the push fails: the local
    commit is RETAINED and the error carries divergence diagnostics + a
    recommendation. No write path swallows a push failure anymore."""
    repo = str(repo_dir or REPO_DIR)
    subprocess.run(["git", "-C", repo, "add"] + [str(f) for f in files],
                   check=True, capture_output=True)

    commit = subprocess.run(["git", "-C", repo, "commit", "-m", message],
                            capture_output=True, text=True)
    if commit.returncode != 0:
        blob = (commit.stdout + commit.stderr).lower()
        if "nothing to commit" in blob or "no changes added" in blob:
            return {"committed": False, "sha": "", "pushed": True}
        raise RuntimeError(f"git commit failed: {commit.stderr.strip() or commit.stdout.strip()}")

    m = re.search(r'\[.+? ([a-f0-9]{7,})\]', commit.stdout)
    sha = m.group(1) if m else commit.stdout.strip()[:12]
    branch = _current_branch(repo)

    def _push():
        try:
            p = subprocess.run(["git", "-C", repo, "push"],
                               capture_output=True, text=True, timeout=60)
            return p.returncode == 0, p.stderr.strip()
        except subprocess.TimeoutExpired:
            return False, "push timed out after 60s"

    push_ok, push_err = _push()

    # B11 — auto-reconcile the benign race. The server pulls origin/main on a 15-min
    # cron; an external push (me, CI) moves the remote, so a production write commits
    # on a stale HEAD and the first push is rejected (non-fast-forward). When the
    # changes are disjoint (the common case — wiki nodes vs docs), a `pull --rebase`
    # replays our one commit cleanly and the retry succeeds. Only a GENUINE conflict
    # (or repeated failure) still raises GitPushError, preserving the loud-divergence
    # guarantee. This is the happy-path version of tools/reconcile_push.py --confirm.
    if not push_ok and ("fetch first" in push_err.lower()
                        or "non-fast-forward" in push_err.lower()
                        or "rejected" in push_err.lower()):
        rebased = subprocess.run(["git", "-C", repo, "pull", "--rebase", "origin", branch],
                                 capture_output=True, text=True, timeout=120)
        if rebased.returncode == 0:
            logger.info("git push race auto-reconciled via pull --rebase in %s", repo)
            push_ok, push_err = _push()
        else:
            # Conflict or no-upstream: abort the half-done rebase so the local commit
            # is left clean + retained for tools/reconcile_push.py, then fall through to raise.
            subprocess.run(["git", "-C", repo, "rebase", "--abort"],
                           capture_output=True, text=True)
            push_err = f"pull --rebase failed (genuine divergence): {rebased.stderr.strip() or rebased.stdout.strip()}"

    if not push_ok:
        diag = _git_push_diagnostics(repo, branch, sha, message)
        diag["push_error"] = push_err
        logger.error("git push failed in %s (sha=%s): %s | %s",
                     repo, sha, push_err, diag["recommendation"])
        raise GitPushError(
            f"commit {sha} retained locally but push failed: {diag['recommendation']}",
            diag)
    # A rebase rewrites the commit hash; report the post-push HEAD.
    head = subprocess.run(["git", "-C", repo, "rev-parse", "--short", "HEAD"],
                          capture_output=True, text=True)
    if head.returncode == 0 and head.stdout.strip():
        sha = head.stdout.strip()
    return {"committed": True, "sha": sha, "pushed": True}


def _git_commit_files(files: list, message: str) -> str:
    """Back-compat wrapper over _git_commit_and_push: returns the commit SHA
    ('' if nothing to commit). A push failure now raises GitPushError (loud)
    instead of silently returning ''."""
    return _git_commit_and_push(files, message)["sha"]


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
    STORE.invalidate_nodes()

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
    STORE.invalidate_nodes()

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
    STORE.invalidate_nodes()

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


@app.route("/app", methods=["GET"])
def app_redirect():
    """Redirect the no-trailing-slash form to /app/."""
    return redirect("/app/", code=301)


@app.route("/app/", defaults={"path": ""}, methods=["GET"])
@app.route("/app/<path:path>", methods=["GET"])
def serve_app(path):
    """Serve the built viewer SPA at /app/. On the VPS this was nginx's job; on the
    workstation gunicorn serves it directly from VIEWER_DIST. Real asset files are
    served as-is; unknown paths fall back to index.html so client-side routing works."""
    dist = VIEWER_DIST
    if path and (dist / path).is_file():
        return send_from_directory(str(dist), path)
    return send_from_directory(str(dist), "index.html")


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
            "finding": "Scrubbed external aggregate result — create_finding_stub (evidence-for a hypothesis).",
            "resource": "External tool/library/platform/docs/dataset/service with a lifecycle — create_resource_stub.",
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
            "illustrated-by": "subject is illustrated/explained by target (an interactive asset: explainer or visualization)",
            "evidence-for": "subject (a finding) is empirical evidence bearing on target (a hypothesis)",
            "implemented-by": "subject (a concept/technique) is concretely realized by target (a resource)",
            "superseded-by": "subject (a resource) has been replaced or made obsolete by target (a resource)",
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
            "create_finding_stub": {
                "creates": "staged finding node (evidence-for a live hypothesis), from a scrubbed external aggregate result",
                "required": ["finding_id", "generated_at", "hypothesis_ref", "summary", "statistics", "source_pointer"],
                "optional": ["stratification", "slug"],
                "notes": "Inbound gate. Validates schema + that hypothesis_ref resolves to a live hypothesis ONLY; never recomputes stats, never scrubs content (producer scrubs; human review is the gate). domain inherited from the hypothesis.",
            },
            "create_resource_stub": {
                "creates": "staged resource node (external tool/library/platform/docs/dataset/service with a lifecycle)",
                "required": ["title", "resource_url"],
                "optional": ["resource_type", "status", "last_evaluated", "technological_scope", "domain", "tags", "summary", "relationship_candidates", "aliases", "slug"],
                "notes": "URL taken as-is, no enrichment. resource_type ∈ {library,tool,platform,dataset,documentation,service}; status ∈ {active,unmaintained,deprecated,archived}. Body: ## Summary + ## Relationship Candidates (no ## Key Concepts). Deployment lives in OpGraph, not PKIS.",
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
            "log_idea": {
                "appends": "a status:open entry to docs/IDEAS.md in the MAIN pkis repo (not the wiki)",
                "required": ["title", "idea"],
                "optional": ["source", "relation_to_system", "open_questions"],
                "notes": "Newest-first. Does NOT promote to DECISIONS.md. source defaults to 'Claude Code: <branch>'.",
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
            "description": "WRITE-authorized config tool. Sets or resets the DEFAULT cluster-proximity weight used by get_concept_frontier for every call without an explicit override (it persists to a config file shared across workers, hence write-tier even when only reporting). reset=true restores the built-in default (2.0); cluster_proximity_weight=<n> persists <n> as the new default for all calls; passing neither reports the current default. Returns the resulting weight and its source.",
            "inputSchema": {"type": "object", "properties": {
                "cluster_proximity_weight": {"type": "number", "description": "New default weight to persist for all calls"},
                "reset": {"type": "boolean", "default": False, "description": "Restore the built-in default (2.0) by removing the persisted config"}
            }}
        },
        {
            "name": "set_search_profile",
            "description": "WRITE-authorized config tool for the retrieval lab. Persists or removes a NAMED search profile (a toggle bundle: retrievers, fusion, rerankers, filters) to a config file shared across workers. profile=<object> saves it under <name>; reset=true deletes it; passing only <name> reports the resolved profile and lists known profiles. Profiles are then selectable by name in /pkis-api/search and /search/compare.",
            "inputSchema": {"type": "object", "properties": {
                "name": {"type": "string", "description": "Profile name to save/remove/report"},
                "profile": {"type": "object", "description": "Partial profile to persist (merged over the default at search time); omit to report"},
                "reset": {"type": "boolean", "default": False, "description": "Remove the named persisted profile"}
            }, "required": ["name"]}
        },
        {
            "name": "get_health_metrics",
            "description": "Get summary health statistics for the wiki.",
            "inputSchema": {"type": "object", "properties": {}}
        },
        {
            "name": "get_lab_report",
            "description": "PKIS Lab Assistant descriptive report: a live snapshot of research-data health (node counts, coverage, hypothesis-status distribution, cluster staleness, staged-node throughput) plus drift flags vs the last stored monitoring snapshot. Descriptive only — never evaluates hypotheses or changes research state.",
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
            "name": "log_idea",
            "description": "Log a not-yet-decided idea to the project's docs/IDEAS.md from any chat or code session. Prepends a dated, status:open entry and commits to the main pkis repo (NOT the wiki). Does not promote to DECISIONS.md — that stays a deliberate human action. Use for ideas worth preserving but not yet committed to.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "Short descriptive title"},
                    "idea": {"type": "string", "description": "Description of the idea"},
                    "source": {"type": "string", "description": "Session context, e.g. 'Claude chat: discovery layer'. Defaults to 'Claude Code: <branch>'."},
                    "relation_to_system": {"type": "string", "description": "What it extends or replaces (optional)"},
                    "open_questions": {"type": "string", "description": "What must be resolved before this can be decided (optional)"}
                },
                "required": ["title", "idea"]
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
            "name": "create_finding_stub",
            "description": "Accept a SCRUBBED, AGGREGATE finding object from an external experimental system (initially OpGraph) and stage it as a `finding` node attached to a live PKIS hypothesis via an `evidence-for` edge. Narrow inbound gate: PKIS validates only schema conformance and that hypothesis_ref resolves to a live hypothesis — it never recomputes/verifies the statistics and never scrubs for identifying content (the producer scrubs; human staging review is the content gate). Promote with commit_staged_node; lands in wiki/findings/.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "finding_id": {"type": "string", "description": "UUID of the finding in the producing system"},
                    "generated_at": {"type": "string", "description": "ISO 8601 timestamp when the producer computed the finding"},
                    "hypothesis_ref": {"type": "string", "description": "IRI of the live PKIS hypothesis this is evidence for, e.g. pkis:hypothesis:intensional-grounding-ned-accuracy"},
                    "summary": {"type": "string", "description": "Plain-language, already-scrubbed summary"},
                    "statistics": {"type": "object", "description": "Aggregate statistics only (e.g. strategy, comparison_strategy, metric, value, comparison_value, n, confidence_interval)"},
                    "stratification": {"type": "object", "description": "Structural/methodological strata only (e.g. mention_type) — never content-identifying"},
                    "source_pointer": {"type": "object", "description": "{system, run_id, log_date_range} — a citation back to the producer, not a reproduction of its data"},
                    "slug": {"type": "string", "description": "Optional explicit slug; derived otherwise"}
                },
                "required": ["finding_id", "generated_at", "hypothesis_ref", "summary", "statistics", "source_pointer"]
            }
        },
        {
            "name": "create_resource_stub",
            "description": "Stage a `resource` node — an external tool, library, platform, dataset, documentation site, or service with a development/maintenance lifecycle. Epistemically distinct from a source: a resource backs 'this exists and does X', not 'this claim is established'. The URL is taken AS-IS (no CrossRef/arXiv/Semantic Scholar enrichment). Body carries ## Summary + ## Relationship Candidates (never ## Key Concepts). Operational deployment lives in OpGraph, not PKIS. Promote with commit_staged_node; lands in wiki/resources/.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "resource_url": {"type": "string", "description": "Canonical URL — required; taken as-is"},
                    "resource_type": {"type": "string", "enum": ["library", "tool", "platform", "dataset", "documentation", "service"]},
                    "status": {"type": "string", "enum": ["active", "unmaintained", "deprecated", "archived"], "default": "active"},
                    "last_evaluated": {"type": "string", "description": "ISO date you last assessed it; defaults to ingest date"},
                    "technological_scope": {"type": "array", "items": {"type": "string"}, "description": "Free tags: language, framework, stack"},
                    "domain": {"type": "array", "items": {"type": "string"}},
                    "tags": {"type": "array", "items": {"type": "string"}},
                    "summary": {"type": "string", "description": "Body for ## Summary (what it does, problem solved, dependencies, caveats)"},
                    "relationship_candidates": {"type": "string", "description": "Body for ## Relationship Candidates"},
                    "definition": {"type": "string", "description": "Short description; seeds ## Summary if summary omitted"},
                    "aliases": {"type": "array", "items": {"type": "string"}},
                    "slug": {"type": "string", "description": "Optional explicit slug; derived from title otherwise"}
                },
                "required": ["title", "resource_url"]
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
                                "predicate": {"type": "string", "enum": ["prerequisite-of", "uses", "specializes", "generalizes", "extends", "applies", "instantiates", "contrasts-with", "analogous-to", "illustrated-by", "evidence-for", "implemented-by", "superseded-by"]},
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
        },
        # ── Promoted hidden→advertised (B5, 2026-06-15). `search_wiki_index` and
        # `get_node_stub` remain reachable-but-unadvertised pending a decision. ──
        {
            "name": "resolve_or_detect",
            "description": "Resolve a phrase to a canonical IRI AND detect implicitly-present concepts in one call. Returns {registry, detected}.",
            "inputSchema": {"type": "object", "properties": {
                "text": {"type": "string"}, "threshold": {"type": "number", "default": 0.7}
            }, "required": ["text"]}
        },
        {
            "name": "get_clusters",
            "description": "List research-program clusters with their hypotheses, status, and dependencies.",
            "inputSchema": {"type": "object", "properties": {}}
        },
        {
            "name": "get_cluster_priorities",
            "description": "Frontier coverage gaps grouped by research cluster, with the effective cluster-proximity weight params.",
            "inputSchema": {"type": "object", "properties": {}}
        },
        {
            "name": "get_index",
            "description": "Browse the wiki catalog, optionally filtered by domain, node_type, and/or cluster.",
            "inputSchema": {"type": "object", "properties": {
                "domain": {"type": "string"}, "node_type": {"type": "string"}, "cluster": {"type": "string"}
            }}
        },
        {
            "name": "get_openwiki",
            "description": "Read the generated OpenWiki code map (read-only). Omit `page` to get quickstart.md plus the list of all available page paths (e.g. 'architecture/server.md', 'testing.md'); pass a `page` path to fetch that page's markdown. Path-restricted to openwiki/.",
            "inputSchema": {"type": "object", "properties": {"page": {"type": "string"}}}
        },
        {
            "name": "get_dependency_chain",
            "description": "Return the transitive prerequisite chain for a node (what must be understood first), ordered by depth.",
            "inputSchema": {"type": "object", "properties": {"iri": {"type": "string"}}, "required": ["iri"]}
        },
        {
            "name": "get_assets",
            "description": "List interactive explainer / visualization assets, optionally filtered by kind.",
            "inputSchema": {"type": "object", "properties": {"kind": {"type": "string"}}}
        },
        {
            "name": "check_alias_collision",
            "description": "Check whether a surface form collides with existing aliases across the wiki before coining a new one.",
            "inputSchema": {"type": "object", "properties": {"surface_form": {"type": "string"}}, "required": ["surface_form"]}
        },
        {
            "name": "get_operational_references",
            "description": "List external operational-system references registered against a wiki node IRI.",
            "inputSchema": {"type": "object", "properties": {"iri": {"type": "string"}}, "required": ["iri"]}
        },
        {
            "name": "get_concept_operational_load",
            "description": "Report how heavily a concept is referenced by external operational systems (operational load).",
            "inputSchema": {"type": "object", "properties": {"iri": {"type": "string"}}, "required": ["iri"]}
        },
        {
            "name": "build_reader",
            "description": "Build the read+listen reader payload (narrated sections + audio + sync map) for a source slug. Write-tier.",
            "inputSchema": {"type": "object", "properties": {
                "slug": {"type": "string"}, "arxiv_id": {"type": "string"}
            }, "required": ["slug"]}
        },
        {
            "name": "register_operational_reference",
            "description": "Register an external operational-system node as referencing a PKIS IRI (trusted tier; mnemon operational layer).",
            "inputSchema": {"type": "object", "properties": {
                "operational_node_id": {"type": "string"}, "iri": {"type": "string"},
                "confidence_class": {"type": "string"}, "source_system": {"type": "string", "default": "mnemon"}
            }, "required": ["operational_node_id", "iri", "confidence_class"]}
        },
        {
            "name": "log_operation",
            "description": "Log an operational event against affected PKIS IRIs (trusted tier; mnemon operational layer).",
            "inputSchema": {"type": "object", "properties": {
                "operation_type": {"type": "string"},
                "affected_iris": {"type": "array", "items": {"type": "string"}},
                "summary": {"type": "string"}, "agent": {"type": "string"}
            }, "required": ["operation_type"]}
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


# ============================================================
# Tool registry — the single source of truth for MCP dispatch.
# Lifted out of dispatch_tool() so the surface is introspectable (contract
# tests, manifest cross-checks) and ready for the planned app.py split into a
# dedicated mcp module. Tiers: READ = open to all; TRUSTED = is_trusted;
# WRITE = is_write_authorized. Each value is `lambda params: tool_*(...)`.
# ============================================================

# Read-only tools — available to all clients
READ_TOOLS = {
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
        "get_assets": lambda p: tool_get_assets(kind=p.get("kind")),
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
            node_type=p.get("node_type"),
            cluster=p.get("cluster")
        ),
        "get_health_metrics": lambda p: tool_get_health_metrics(),
        "get_openwiki": lambda p: tool_get_openwiki(page=p.get("page")),
        "get_lab_report": lambda p: tool_get_lab_report(),
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
TRUSTED_TOOLS = {
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
WRITE_TOOLS = {
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
        "create_finding_stub": lambda p: tool_create_finding_stub(
            finding_id=p.get("finding_id", ""),
            generated_at=p.get("generated_at", ""),
            hypothesis_ref=p.get("hypothesis_ref", ""),
            summary=p.get("summary", ""),
            statistics=p.get("statistics"),
            stratification=p.get("stratification"),
            source_pointer=p.get("source_pointer"),
            slug=p.get("slug", ""),
        ),
        "create_resource_stub": lambda p: tool_create_resource_stub(
            title=p.get("title", ""),
            resource_url=p.get("resource_url", ""),
            resource_type=p.get("resource_type", ""),
            status=p.get("status", "active"),
            last_evaluated=p.get("last_evaluated", ""),
            technological_scope=p.get("technological_scope"),
            domain=p.get("domain"),
            tags=p.get("tags"),
            definition=p.get("definition", ""),
            summary=p.get("summary", ""),
            relationship_candidates=p.get("relationship_candidates", ""),
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
        "set_search_profile": lambda p: tool_set_search_profile(
            name=p["name"],
            profile=p.get("profile"),
            reset=p.get("reset", False),
        ),
        "build_reader": lambda p: tool_build_reader(slug=p["slug"], arxiv_id=p.get("arxiv_id")),
        "add_connections": lambda p: tool_add_connections(
            edges=p["edges"],
            commit_message=p.get("commit_message", ""),
        ),
        "log_idea": lambda p: tool_log_idea(
            title=p["title"],
            idea=p["idea"],
            source=p.get("source", ""),
            relation_to_system=p.get("relation_to_system", ""),
            open_questions=p.get("open_questions", ""),
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

# Combined views for introspection (contract tests + manifest cross-checks).
DISPATCHABLE_TOOLS = {**READ_TOOLS, **TRUSTED_TOOLS, **WRITE_TOOLS}
TOOL_TIERS = {
    **{n: "read" for n in READ_TOOLS},
    **{n: "trusted" for n in TRUSTED_TOOLS},
    **{n: "write" for n in WRITE_TOOLS},
}


def dispatch_tool(tool_name: str, params: dict, req) -> any:
    """Dispatch an MCP tool call to its implementation, gating by tier. The tool
    tables live at module scope (READ_TOOLS / TRUSTED_TOOLS / WRITE_TOOLS) so the
    surface is introspectable and ready for the app.py split."""
    # Rebuild caches if another worker committed a write since this one last
    # built, so search/discovery reflects new content without a service restart.
    ensure_fresh()

    if tool_name in READ_TOOLS:
        return READ_TOOLS[tool_name](params)
    elif tool_name in TRUSTED_TOOLS:
        if not is_trusted(req):
            raise gate_error(req, "trusted")
        return TRUSTED_TOOLS[tool_name](params)
    elif tool_name in WRITE_TOOLS:
        if not is_write_authorized(req):
            raise gate_error(req, "write")
        return WRITE_TOOLS[tool_name](params)
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
        # Response stays a plain SearchResult[] (back-compat with the Browse box).
        # An optional `profile` (named or inline) selects a non-default pipeline.
        # `capture: true` marks this as a deliberate query for the standing test
        # set — the as-you-type Browse box omits it, so prefixes aren't logged.
        if b.get("capture"):
            _maybe_capture_query(b.get("query", ""), "search")
        return _api_ok(tool_search_wiki(
            query=b.get("query", ""),
            domains=b.get("domains"),
            node_types=b.get("node_types"),
            max_results=b.get("max_results", 10),
            profile=b.get("profile"),
        ))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/search/compare", methods=["POST"])
def pkis_api_search_compare():
    """Run one query through N profiles for the lab. Returns a column per profile
    (results + per-stage trace + metrics + retrieval/eval latency) and logs each
    to the experiment store under a shared comparison_id."""
    b = _api_json()
    query = b.get("query", "")
    profiles = b.get("profiles") or ["default"]
    max_results = b.get("max_results", 10)
    log = b.get("log", True)
    try:
        _maybe_capture_query(query, "search")  # a compare is always a deliberate query
        # C(q) for the deep metrics is query-dependent only — compute it ONCE here
        # (one LLM call) and reuse across every profile column.
        deep_cq = _estimate_cq(query) if b.get("deep") else None
        cid = uuid.uuid4().hex[:12]
        columns = [run_search(query, profile=p, max_results=max_results,
                              comparison_id=cid, log=log, deep_cq=deep_cq) for p in profiles]
        return _api_ok({"comparison_id": cid, "query": query, "columns": columns})
    except Exception as e:
        return _api_err(e, 500)


def _resolve_anchor(ref):
    """Resolve a path-query endpoint (IRI, slug, or free text) to a graph node IRI:
    exact IRI → slug lookup → top search hit."""
    if not ref:
        return None
    G = get_graph()
    if G.has_node(ref):
        return ref
    path = find_node_path(str(ref).strip().lower().replace(" ", "-"))
    if path:
        iri = (load_node(path) or {}).get("iri")
        if iri and G.has_node(iri):
            return iri
    res = tool_search_wiki(ref, max_results=1)
    return res[0]["iri"] if res else None


def tool_path_between(a, b, max_paths=3):
    """Relationship query: the shortest typed-edge path(s) between two nodes and
    their common neighbours. Endpoints are resolved from IRI/slug/free text."""
    G = get_graph()
    ia, ib = _resolve_anchor(a), _resolve_anchor(b)
    title = lambda i: G.nodes.get(i, {}).get("title", i)  # noqa: E731
    if not ia or not ib:
        return {"error": "could not resolve both endpoints", "a": a, "b": b}
    out = {"a": {"ref": a, "iri": ia, "title": title(ia)},
           "b": {"ref": b, "iri": ib, "title": title(ib)},
           "connected": False, "paths": [], "common": []}
    if ia == ib:
        out["connected"] = True
        out["paths"] = [[{"iri": ia, "title": title(ia)}]]
        return out
    UG = G.to_undirected()
    if UG.has_node(ia) and UG.has_node(ib) and nx.has_path(UG, ia, ib):
        out["connected"] = True
        for p in nx.all_shortest_paths(UG, ia, ib):
            out["paths"].append([{"iri": n, "title": title(n)} for n in p])
            if len(out["paths"]) >= max_paths:
                break
        common = set(UG.neighbors(ia)) & set(UG.neighbors(ib))
        out["common"] = [{"iri": n, "title": title(n)} for n in list(common)[:12]]
    return out


@app.route("/pkis-api/path", methods=["POST"])
def pkis_api_path():
    """Relationship/path query between two nodes (read-open, like get_related)."""
    b = _api_json()
    try:
        return _api_ok(tool_path_between(b.get("a", ""), b.get("b", "")))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/experiments", methods=["GET"])
def pkis_api_experiments():
    """List recent logged experiments (most recent first). Filter by comparison_id
    or paradigm; ?limit=N caps the count."""
    try:
        return _api_ok(experiments.list_experiments(
            EXPERIMENT_DB_PATH,
            limit=int(request.args.get("limit", 50)),
            comparison_id=request.args.get("comparison_id"),
            paradigm=request.args.get("paradigm"),
        ))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/queries", methods=["GET"])
def pkis_api_queries():
    """Owner-only: the standing test set (deliberate queries captured from use)."""
    if not is_owner(request):
        return _api_err("owner only", 403)
    try:
        return _api_ok(experiments.list_queries(
            EXPERIMENT_DB_PATH, limit=int(request.args.get("limit", 1000))))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/feedback", methods=["POST"])
def pkis_api_feedback():
    """Owner-only feedback tap — the supervised target for winner determination.
    Body: {query, comparison_id?, paradigm?, chosen_profile?, chosen_iri?, rating?, notes?}."""
    if not is_owner(request):
        return _api_err("owner only", 403)
    b = _api_json()
    try:
        fid = experiments.log_feedback(EXPERIMENT_DB_PATH, {
            "query": b.get("query"),
            "comparison_id": b.get("comparison_id"),
            "paradigm": b.get("paradigm", "search"),
            "chosen_profile": b.get("chosen_profile"),
            "chosen_iri": b.get("chosen_iri"),
            "rating": b.get("rating"),
            "notes": b.get("notes"),
        })
        return _api_ok({"ok": fid is not None, "id": fid})
    except Exception as e:
        return _api_err(e, 500)


# Bounds on the public ask endpoint: reads are open, so this route reaches the
# paid model API anonymously. Per-request caps keep a single ask cheap; the
# per-IP throttle below caps how fast one caller can spend.
_ASK_MAX_MESSAGES = 40
_ASK_MAX_CHARS = 8000

# Per-IP rate limit — three nested windows: burst (min), session (hour), and a
# daily cap. Env-tunable so it can be loosened/tightened without a code change.
# This is a COST SAFETY NET, not security: it's in-process, so with N gunicorn
# workers the effective ceiling is ~N× these numbers (each worker keeps its own
# window). The service runs 2 workers, so these per-worker defaults give an
# effective ceiling of ≈16/min, 50/hr, 100/day per IP. A hard guarantee would
# need a shared store (or the sign-in gate).
_ASK_RATE_PER_MIN = int(os.environ.get("PKIS_ASK_RATE_PER_MIN", "8"))
_ASK_RATE_PER_HOUR = int(os.environ.get("PKIS_ASK_RATE_PER_HOUR", "25"))
_ASK_RATE_PER_DAY = int(os.environ.get("PKIS_ASK_RATE_PER_DAY", "50"))
_ask_hits = {}                 # ip -> list[monotonic timestamps] within the last day
_ask_hits_lock = threading.Lock()


def _client_ip(req):
    """Real client IP behind nginx: first hop of X-Forwarded-For, else remote_addr.
    (Gunicorn sees 127.0.0.1, so remote_addr alone would lump everyone together.)"""
    xff = req.headers.get("X-Forwarded-For", "")
    if xff:
        return xff.split(",")[0].strip()
    return req.remote_addr or "unknown"


def _ask_rate_check(ip):
    """Sliding-window throttle over min / hour / day windows. Returns
    (ok, retry_after_seconds). Prunes the caller's window to the last day and
    opportunistically sweeps idle IPs so the map can't grow without bound."""
    now = time.monotonic()
    day_ago, hour_ago, min_ago = now - 86400, now - 3600, now - 60
    with _ask_hits_lock:
        if len(_ask_hits) > 4096:  # cheap stale-IP sweep
            for k in [k for k, v in _ask_hits.items() if not v or v[-1] < day_ago]:
                _ask_hits.pop(k, None)
        hits = [t for t in _ask_hits.get(ip, ()) if t > day_ago]
        _ask_hits[ip] = hits
        # Check coarsest-first so Retry-After reflects the binding limit.
        for window, span, cap in (
            (day_ago, 86400, _ASK_RATE_PER_DAY),
            (hour_ago, 3600, _ASK_RATE_PER_HOUR),
            (min_ago, 60, _ASK_RATE_PER_MIN),
        ):
            in_window = [t for t in hits if t > window]
            if len(in_window) >= cap:
                return False, int(min(in_window) + span - now) + 1
        hits.append(now)
        return True, 0


def _ask_prepare():
    """Shared validation + throttle for the ask endpoints. Returns
    (clean_messages, tier, None) on success, or (None, None, response) where
    `response` is the error/429 to return immediately."""
    b = _api_json()
    messages = b.get("messages") or []
    question = (b.get("question") or "").strip()
    if question:
        messages = list(messages) + [{"role": "user", "content": question}]

    if not isinstance(messages, list) or not messages:
        return None, None, _api_err("messages (or question) is required")
    if len(messages) > _ASK_MAX_MESSAGES:
        messages = messages[-_ASK_MAX_MESSAGES:]
    clean = []
    for m in messages:
        if not isinstance(m, dict):
            continue
        role, content = m.get("role"), m.get("content")
        if role not in ("user", "assistant") or not isinstance(content, str):
            continue
        clean.append({"role": role, "content": content[:_ASK_MAX_CHARS]})
    if not clean or clean[-1]["role"] != "user":
        return None, None, _api_err("conversation must end with a user message")

    tier = "owner" if is_owner(request) else "reader"
    # Throttle anonymous/reader callers; signed-in writers and the owner are
    # trusted and bypass it (they bear the cost knowingly).
    if not is_write_authorized(request):
        ok, retry_after = _ask_rate_check(_client_ip(request))
        if not ok:
            resp = jsonify({"error": "rate limit — too many questions, try again shortly"})
            resp.headers["Retry-After"] = str(retry_after)
            return None, None, (resp, 429)
    return clean, tier, None


@app.route("/pkis-api/ask", methods=["POST"])
def pkis_api_ask():
    """Natural-language ask over the graph (non-streaming JSON). Stateless +
    multi-turn: the client sends the full conversation each call.

    Body: {"messages": [{"role":"user"|"assistant","content": str}, …]}
          — or {"question": str, "messages": [...prior...]} as a convenience.
    Returns: {answer, citations:[{slug,iri,title}], surfaced, tier, model,
              turns, usage}. The viewer uses /pkis-api/ask/stream; this JSON form
              backs the future MCP ask_pkis tool and non-streaming clients."""
    clean, tier, err = _ask_prepare()
    if err is not None:
        return err
    _maybe_capture_query(clean[-1]["content"], "ask")  # owner asks → standing test set
    try:
        result = ask.run_ask(clean, tier=tier)
        result["tier"] = tier
        return _api_ok(result)
    except Exception as e:
        logger.error(f"ask error: {e}", exc_info=True)
        return _api_err(e, 500)


@app.route("/pkis-api/ask/stream", methods=["POST"])
def pkis_api_ask_stream():
    """Streaming (SSE) ask — the engine's events forwarded as `data:` frames so
    the viewer can render the answer token-by-token. Event shapes match
    ask._ask_events: {type:status|delta|done|error, …}. `tier` is folded into the
    done frame."""
    clean, tier, err = _ask_prepare()
    if err is not None:
        return err
    _maybe_capture_query(clean[-1]["content"], "ask")  # owner asks → standing test set

    def gen():
        try:
            for ev in ask._ask_events(clean, tier=tier):
                if ev.get("type") == "done":
                    ev["tier"] = tier
                yield f"data: {json.dumps(ev)}\n\n"
        except Exception as e:
            logger.error(f"ask stream error: {e}", exc_info=True)
            yield f"data: {json.dumps({'type': 'error', 'error': str(e)})}\n\n"

    return Response(stream_with_context(gen()), mimetype="text/event-stream",
                    headers={"Cache-Control": "no-cache",
                             "X-Accel-Buffering": "no"})  # tell nginx not to buffer SSE


@app.route("/pkis-api/ask/compare", methods=["POST"])
def pkis_api_ask_compare():
    """Owner-only lab endpoint: answer one question under N retrieval profiles
    (capped — each is a full LLM call) and return a column per profile with the
    answer, citations, groundedness, latency, and token cost. Logs ask-paradigm
    experiments under a shared comparison_id; the query joins the test set."""
    if not is_owner(request):
        return _api_err("owner only", 403)
    clean, _tier, err = _ask_prepare()
    if err is not None:
        return err
    b = _api_json()
    profiles = (b.get("profiles") or ["default"])[:3]   # hard cap — LLM cost
    query = clean[-1]["content"]
    _maybe_capture_query(query, "ask")
    try:
        cid = uuid.uuid4().hex[:12]
        columns = [run_ask_experiment(clean, profile=p, comparison_id=cid, query=query)
                   for p in profiles]
        return _api_ok({"comparison_id": cid, "query": query, "columns": columns})
    except Exception as e:
        logger.error(f"ask compare error: {e}", exc_info=True)
        return _api_err(e, 500)


# ── Conversation persistence (signed-in, per-user) ─────────────────────────
# Auto-saved latest state; the store self-inits lazily on first use (the default
# path only exists on the server). Document versioning will live on the studio
# artifact, not on chat turns.
CONVERSATIONS_DB = Path(os.environ.get(
    "PKIS_CONVERSATIONS_DB", "/home/pkis/conversations/conversations.sqlite"))
_CONV_MAX_TURNS = 500  # generous guard on a single stored conversation


def _conv_sub(req):
    """The signed-in user's id (WorkOS sub) from a web sealed session or an OAuth
    bearer, else None. Conversations are private to this sub."""
    ident = web_identity(req) or oauth_identity(req)
    return ident[0] if ident else None


@app.route("/pkis-api/conversations", methods=["GET"])
def pkis_api_conversations_list():
    sub = _conv_sub(request)
    if not sub:
        return jsonify({"error": "sign in required"}), 401
    try:
        convs = conversations.list_for_user(CONVERSATIONS_DB, sub)
        # Annotate share state in one query so the history view can show a "shared"
        # badge + offer revoke without a lookup per row.
        shared = shares.active_map_for_owner(SHARES_DB, sub, "conversation")
        for c in convs:
            c["share_token"] = shared.get(c["id"])
            c["shared"] = bool(c["share_token"])
        return _api_ok({"conversations": convs})
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/conversations", methods=["POST"])
def pkis_api_conversations_save():
    """Auto-save (create or update) the signed-in user's conversation, appending a
    version snapshot. Body: {id?, messages, title?, anchor?, artifact?}."""
    sub = _conv_sub(request)
    if not sub:
        return jsonify({"error": "sign in required"}), 401
    b = _api_json()
    messages = b.get("messages")
    if not isinstance(messages, list) or not messages:
        return _api_err("messages is required")
    if len(messages) > _CONV_MAX_TURNS:
        messages = messages[-_CONV_MAX_TURNS:]
    try:
        return _api_ok(conversations.save(
            CONVERSATIONS_DB, sub, conv_id=b.get("id"), messages=messages,
            title=b.get("title"), anchor=b.get("anchor"), artifact=b.get("artifact")))
    except PermissionError as e:
        return jsonify({"error": str(e)}), 403
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/conversation/<cid>", methods=["GET"])
def pkis_api_conversation_get(cid):
    sub = _conv_sub(request)
    if not sub:
        return jsonify({"error": "sign in required"}), 401
    c = conversations.get(CONVERSATIONS_DB, sub, cid)
    if not c:
        return _api_err("conversation not found", 404)
    return _api_ok(c)


@app.route("/pkis-api/conversation/<cid>/rename", methods=["POST"])
def pkis_api_conversation_rename(cid):
    sub = _conv_sub(request)
    if not sub:
        return jsonify({"error": "sign in required"}), 401
    title = (_api_json().get("title") or "").strip()
    if not conversations.rename(CONVERSATIONS_DB, sub, cid, title):
        return _api_err("conversation not found", 404)
    return _api_ok({"ok": True, "title": title or "Untitled"})


@app.route("/pkis-api/conversation/<cid>/delete", methods=["POST"])
def pkis_api_conversation_delete(cid):
    """Soft delete (recoverable). Body {deleted: false} undeletes."""
    sub = _conv_sub(request)
    if not sub:
        return jsonify({"error": "sign in required"}), 401
    deleted = _api_json().get("deleted", True)
    if not conversations.set_deleted(CONVERSATIONS_DB, sub, cid, bool(deleted)):
        return _api_err("conversation not found", 404)
    return _api_ok({"ok": True, "deleted": bool(deleted)})


# ── Capability-link sharing (mint owner-only; resolve public, read-only) ────
SHARES_DB = Path(os.environ.get("PKIS_SHARES_DB", "/home/pkis/conversations/shares.sqlite"))


def _share_owns(sub, kind, ref):
    """Does this signed-in user own the item they're trying to share?"""
    if kind == "conversation":
        c = conversations.get(CONVERSATIONS_DB, sub, ref)
        return bool(c and not c.get("deleted"))
    return False


@app.route("/pkis-api/share", methods=["POST"])
def pkis_api_share_create():
    """Owner mints (or reuses) a read-only capability link for an owned item.
    Body: {kind, ref}. Returns {token, url, created}."""
    sub = _conv_sub(request)
    if not sub:
        return jsonify({"error": "sign in required"}), 401
    b = _api_json()
    kind, ref = b.get("kind"), b.get("ref")
    if kind not in ("conversation",):           # nodes/docs reuse this later
        return _api_err("unsupported share kind")
    if not ref or not _share_owns(sub, kind, ref):
        return _api_err("item not found or not yours", 404)
    res = shares.mint(SHARES_DB, sub, kind, ref)
    res["url"] = f"/app/?s={res['token']}"
    return _api_ok(res)


@app.route("/pkis-api/share/<token>/revoke", methods=["POST"])
def pkis_api_share_revoke(token):
    sub = _conv_sub(request)
    if not sub:
        return jsonify({"error": "sign in required"}), 401
    if not shares.revoke(SHARES_DB, sub, token):
        return _api_err("share not found", 404)
    return _api_ok({"ok": True})


@app.route("/pkis-api/share/<token>", methods=["GET"])
def pkis_api_share_resolve(token):
    """PUBLIC, no auth: a valid token returns the shared item's read-only content.
    Returns only the content (title + messages) — never the owner's identity."""
    sh = shares.resolve(SHARES_DB, token)
    if not sh:
        return _api_err("share not found or revoked", 404)
    if sh["kind"] == "conversation":
        c = conversations.get(CONVERSATIONS_DB, sh["owner_sub"], sh["ref"])
        if not c or c.get("deleted"):
            return _api_err("shared item is no longer available", 404)
        return _api_ok({"kind": "conversation", "title": c["title"],
                        "messages": c["messages"], "updated_at": c["updated_at"]})
    return _api_err("unsupported share kind", 400)


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


def _resolve_one(slug):
    s = (slug or "").strip().lstrip("/")
    if not s:
        return None
    path = find_node_path(s)
    if not path:
        return None
    node = load_node(path)
    return (node or {}).get("iri")


@app.route("/pkis-api/resolve", methods=["POST"])
def pkis_api_resolve():
    """Resolve bare node slug(s) (from body [[wikilinks]]) to canonical IRIs so the
    viewer can navigate and dim danglers. Single: {"slug": s} → {"iri": iri|null}.
    Batch: {"slugs": [...]} → {"map": {slug: iri|null}}. null = no such node."""
    b = _api_json()
    slugs = b.get("slugs")
    try:
        if isinstance(slugs, list):
            return _api_ok({"map": {s: _resolve_one(s) for s in slugs if (s or "").strip()}})
        slug = (b.get("slug", "") or "").strip()
        if not slug:
            return _api_err("slug or slugs is required")
        return _api_ok({"iri": _resolve_one(slug)})
    except Exception as e:
        return _api_err(e, 500)


def _source_status(slug):
    """For a cited source slug: does its node exist, is it readable, and where.
    read_url priority: external source_url → derived split PDF → doc_path PDF.
    (A reader payload also counts as readable via the in-app reader: has_reader.)"""
    s = (slug or "").strip().lstrip("/")
    st = {"iri": None, "readable": False, "read_url": None, "has_reader": False}
    if not s:
        return st
    path = find_node_path(s)
    if not path:
        return st                      # dangling — not ingested
    node = load_node(path) or {}
    st["iri"] = node.get("iri")
    fm = node.get("frontmatter", {}) or {}
    su = (fm.get("source_url") or "").strip()
    dp = (fm.get("doc_path") or "").strip()
    if su:
        st.update(readable=True, read_url=su)
    elif (DOCS_DIR / "sources" / s / f"{s}.pdf").exists():
        st.update(readable=True, read_url=f"/docs/sources/{s}/{s}.pdf")
    elif dp:
        st.update(readable=True, read_url="/docs/" + dp.lstrip("/"))
    st["has_reader"] = (WIKI_DIR / "reader" / s).exists()
    if st["has_reader"]:
        st["readable"] = True
    return st


@app.route("/pkis-api/source-status", methods=["POST"])
def pkis_api_source_status():
    """Readability of cited sources, so the viewer can offer a 'read' affordance and
    dim un-ingested ones. {"slugs": [...]} → {"map": {slug: {iri, readable, read_url, has_reader}}}."""
    slugs = _api_json().get("slugs") or []
    try:
        return _api_ok({"map": {s: _source_status(s) for s in slugs if (s or "").strip()}})
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
        return _api_ok(tool_get_index(domain=b.get("domain"), node_type=b.get("node_type"), cluster=b.get("cluster")))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/domains", methods=["POST"])
def pkis_api_domains():
    try:
        return _api_ok(tool_get_domains())
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/assets", methods=["POST"])
def pkis_api_assets():
    b = _api_json()
    try:
        return _api_ok(tool_get_assets(kind=b.get("kind")))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/explainers", methods=["POST"])
def pkis_api_explainers():
    # back-compat alias — explainer-kind assets only
    try:
        return _api_ok(tool_get_assets(kind="explainer"))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/docs", methods=["POST"])
def pkis_api_docs():
    # Manifest for the viewer Docs nav (keys, titles, categories).
    try:
        return _api_ok(tool_list_docs())
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/doc", methods=["POST"])
def pkis_api_doc():
    b = _api_json()
    key = b.get("key", "")
    if not key:
        return _api_err("key is required")
    try:
        return _api_ok(tool_get_doc(key))
    except ValueError as e:
        return _api_err(str(e), 404)
    except Exception as e:
        return _api_err(e, 500)


# ── Web sign-in (WorkOS AuthKit sealed session) ───────────────────────────────
@app.route("/pkis-api/auth/login", methods=["GET"])
def pkis_api_auth_login():
    if not WEB_AUTH_ENABLED:
        return jsonify({"error": "web auth not configured"}), 503
    return_to = request.args.get("return", "/app/")
    try:
        url = _get_workos().user_management.get_authorization_url(
            provider="authkit",
            redirect_uri=WORKOS_REDIRECT_URI,
            state=return_to,
        )
        return redirect(url)
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/auth/callback", methods=["GET"])
def pkis_api_auth_callback():
    if not WEB_AUTH_ENABLED:
        return jsonify({"error": "web auth not configured"}), 503
    code = request.args.get("code", "")
    if not code:
        return jsonify({"error": "missing code"}), 400
    state = request.args.get("state") or "/app/"
    # Native (Capacitor) sign-in carries `state = "native:<nonce>"`. Instead of
    # sealing a cookie (the APK's WebView can't receive one), we hand the app a
    # one-time code over the com.pkis.app:// deep link, which it redeems at
    # /auth/native/token for a PKIS bearer pair. Falls back to the web flow.
    native_nonce = state[len("native:"):] if state.startswith("native:") else None
    dest = state if state.startswith("/app") else "/app/"
    try:
        res = _get_workos().user_management.authenticate_with_code(code=code)
        if native_nonce is not None:
            cb = f"{NATIVE_APP_SCHEME}://auth-callback"
            challenge = _native_consume_challenge(native_nonce)
            identity = _identity_from_user(getattr(res, "user", None))
            if not challenge or not identity:
                logger.warning("native sign-in: %s", "expired/unknown state" if not challenge else "no identity")
                return redirect(f"{cb}?error={'expired' if not challenge else 'identity'}")
            auth_code = _native_issue_code(identity[0], challenge)
            logger.info("native sign-in OK: user=%s", getattr(res.user, "email", "?"))
            return redirect(f"{cb}?code={urllib.parse.quote(auth_code)}")
        # workos 8.x: authenticate_with_code returns the tokens; we seal the session
        # CLIENT-SIDE with the SDK's own helper (Fernet, keyed by WORKOS_COOKIE_PASSWORD)
        # so it round-trips exactly with load_sealed_session/unseal_data on every read.
        # (The earlier request_raw seal_session approach never produced a usable cookie.)
        from workos.session import seal_session_from_auth_response
        sealed = seal_session_from_auth_response(
            access_token=res.access_token,
            refresh_token=res.refresh_token,
            user=res.user.to_dict(),
            impersonator=res.impersonator.to_dict() if res.impersonator is not None else None,
            cookie_password=WORKOS_COOKIE_PASSWORD,
        )
        resp = make_response(redirect(dest))
        resp.set_cookie(WEB_SESSION_COOKIE, sealed, max_age=30 * 24 * 3600,
                        httponly=True, secure=True, samesite="Lax")
        logger.info("web sign-in OK: user=%s", getattr(res.user, "email", "?"))
        return resp
    except Exception as e:  # noqa: BLE001
        logger.warning("auth callback failed: %s", e, exc_info=True)
        return redirect("/app/?auth_error=1")


@app.route("/pkis-api/inbox", methods=["GET"])
def pkis_api_inbox():
    """OWNER-ONLY administrative inbox (wiki/inbox.md) — the unified review surface.
    401 if anonymous, 403 if signed in without the owner role (e.g. a 'writer' or
    another user). Returns the raw markdown; the viewer parses swim lanes."""
    if not is_owner(request):
        anon = (web_identity(request) is None
                and oauth_identity(request) is None
                and native_identity(request) is None
                and not _has_static_key(request))
        return (jsonify({"error": "sign in required"}), 401) if anon \
            else (jsonify({"error": "owner only — this surface is administrative"}), 403)
    path = WIKI_DIR / "inbox.md"
    return _api_ok({"markdown": path.read_text(encoding="utf-8") if path.exists() else ""})


@app.route("/pkis-api/auth/me", methods=["GET"])
def pkis_api_auth_me():
    # Web sealed-session OR native bearer token — both resolve to (id, role).
    ident = web_identity(request) or native_identity(request)
    if not ident:
        return jsonify({"authenticated": False, "role": "reader"})
    sub, role = ident
    return jsonify({"authenticated": True, "user_id": sub, "role": role})


@app.route("/pkis-api/auth/logout", methods=["POST"])
def pkis_api_auth_logout():
    resp = make_response(jsonify({"ok": True}))
    resp.delete_cookie(WEB_SESSION_COOKIE)
    return resp


# ── Native-app sign-in (Capacitor APK; PKIS-minted bearer tokens) ─────────────
@app.route("/pkis-api/auth/native/start", methods=["GET"])
def pkis_api_auth_native_start():
    """Begin native sign-in. The app passes a PKCE `challenge` (S256); we stash it
    under a nonce carried through WorkOS as `state=native:<nonce>`, then redirect to
    the WorkOS hosted login. After login, /auth/callback hands the app a one-time
    code on the com.pkis.app:// deep link."""
    if not NATIVE_AUTH_ENABLED:
        return jsonify({"error": "native auth not configured"}), 503
    challenge = request.args.get("challenge", "")
    if not challenge:
        return jsonify({"error": "missing challenge"}), 400
    try:
        nonce = _native_register_challenge(challenge)
        url = _get_workos().user_management.get_authorization_url(
            provider="authkit",
            redirect_uri=WORKOS_REDIRECT_URI,
            state=f"native:{nonce}",
        )
        return redirect(url)
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/auth/native/token", methods=["POST"])
def pkis_api_auth_native_token():
    """Exchange a one-time auth code + PKCE verifier for a PKIS bearer pair."""
    if not NATIVE_AUTH_ENABLED:
        return jsonify({"error": "native auth not configured"}), 503
    b = request.get_json(silent=True) or {}
    code, verifier = b.get("code", ""), b.get("verifier", "")
    if not code or not verifier:
        return jsonify({"error": "missing code or verifier"}), 400
    out = _native_redeem_code(code, verifier)
    if not out:
        return jsonify({"error": "invalid or expired code"}), 401
    access, refresh, access_exp = out
    return jsonify({"access_token": access, "refresh_token": refresh,
                    "expires_in": int(access_exp - time.time())})


@app.route("/pkis-api/auth/native/refresh", methods=["POST"])
def pkis_api_auth_native_refresh():
    """Rotate a refresh token for a fresh access+refresh pair (old refresh revoked)."""
    if not NATIVE_AUTH_ENABLED:
        return jsonify({"error": "native auth not configured"}), 503
    b = request.get_json(silent=True) or {}
    refresh = b.get("refresh_token", "")
    if not refresh:
        return jsonify({"error": "missing refresh_token"}), 400
    out = _native_rotate(refresh)
    if not out:
        return jsonify({"error": "invalid or expired refresh_token"}), 401
    access, new_refresh, access_exp = out
    return jsonify({"access_token": access, "refresh_token": new_refresh,
                    "expires_in": int(access_exp - time.time())})


@app.route("/pkis-api/auth/native/logout", methods=["POST"])
def pkis_api_auth_native_logout():
    """Revoke the presented native access token (best-effort; idempotent)."""
    tok = _bearer(request)
    if tok:
        _native_revoke(tok)
    return jsonify({"ok": True})


@app.route("/pkis-api/cluster-priorities", methods=["POST"])
def pkis_api_cluster_priorities():
    try:
        return _api_ok(tool_get_cluster_priorities())
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/source-relevance", methods=["POST"])
def pkis_api_source_relevance():
    """Why a source is worth reading: the frontier-gap concepts it serves + its
    priority score. Powers the 'research relevance' panel on a source's detail."""
    slug = (_api_json().get("slug") or "").strip().lstrip("/")
    if not slug:
        return _api_err("slug is required")
    try:
        return _api_ok(_source_relevance(slug))
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
@require_write
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
@require_write
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
@require_write
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


@app.route("/pkis-api/edit", methods=["POST"])
@require_write
def pkis_api_edit():
    """Edit a LIVE node from the viewer's edit sheet — frontmatter fields and/or the
    full body — then commit + push. (The old viewer path mis-routed to staged/commit
    with an empty staged_id and always 400'd.)"""
    b = _api_json()
    iri = b.get("iri", "")
    if not iri:
        return _api_err("iri is required")
    try:
        return _api_ok(tool_edit_node(
            iri=iri,
            frontmatter_updates=b.get("frontmatter_updates") or {},
            section_updates=b.get("section_updates") or {},
            content=b.get("content"),
            commit_message=b.get("commit_message", "viewer: edit node"),
        ))
    except ValueError as e:
        return _api_err(e, 404)
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/bridge-note", methods=["POST"])
@require_write
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
@require_write
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


@app.route("/pkis-api/resource-stub", methods=["POST"])
@require_write
def pkis_api_resource_stub():
    """Stage a resource node from the viewer (e.g. the share-target review card)."""
    b = _api_json()
    try:
        return _api_ok(tool_create_resource_stub(
            title=b.get("title", ""),
            resource_url=b.get("resource_url", ""),
            resource_type=b.get("resource_type", ""),
            status=b.get("status", "active"),
            last_evaluated=b.get("last_evaluated", ""),
            technological_scope=b.get("technological_scope"),
            domain=b.get("domain"),
            tags=b.get("tags"),
            definition=b.get("definition", ""),
            summary=b.get("summary", ""),
            relationship_candidates=b.get("relationship_candidates", ""),
            aliases=b.get("aliases"),
            slug=b.get("slug", ""),
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
@require_write
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


# ============================================================
# PROACTIVE DISCOVERY — inbox + feedback loop
# The generator (tools/discovery_openalex.py, cron'd) writes ranked, frontier-gated
# candidates into discovery_inbox.json. The viewer's Discover tab reads them and the
# user accepts (→ source stub + reading queue) or dismisses. Every decision is logged
# and folds into a per-signal learned prior that re-weights the next run — the durable
# fix for the residual taste-dependent noise the a-priori gates can't catch.
# ============================================================
DISCOVERY_DIR = Path(os.environ.get("PKIS_DISCOVERY_DIR", "/home/pkis"))
DISCOVERY_INBOX = DISCOVERY_DIR / "discovery_inbox.json"
DISCOVERY_FEEDBACK = DISCOVERY_DIR / "discovery_feedback.jsonl"
DISCOVERY_PRIOR = DISCOVERY_DIR / "discovery_prior.json"


def _discovery_load():
    if DISCOVERY_INBOX.exists():
        try:
            return json.loads(DISCOVERY_INBOX.read_text())
        except Exception:
            pass
    return {"candidates": []}


def _discovery_save(data):
    DISCOVERY_INBOX.write_text(json.dumps(data, ensure_ascii=False, indent=1))


def _discovery_counts(data):
    from collections import Counter
    return dict(Counter(c.get("status", "pending") for c in data.get("candidates", [])))


def _discovery_recompute_prior():
    """From the feedback log, build a per-signal accept/reject multiplier. Each signal
    value gets (accepts+1)/(rejects+1) clamped to [0.1, 3.0] — neutral 1.0 with no data,
    >1 when you tend to accept it, <1 when you tend to dismiss it. The generator applies
    the geometric mean of a candidate's signal multipliers to its score."""
    from collections import defaultdict
    stats = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    if DISCOVERY_FEEDBACK.exists():
        for line in DISCOVERY_FEEDBACK.read_text().splitlines():
            if not line.strip():
                continue
            try:
                fb = json.loads(line)
            except Exception:
                continue
            acc = 1 if fb.get("action") == "accept" else 0
            rej = 1 if fb.get("action") == "dismiss" else 0
            for dim, val in (fb.get("signals") or {}).items():
                if not val:
                    continue
                s = stats[dim][str(val)]
                s[0] += acc
                s[1] += rej
    prior = {}
    for dim, vals in stats.items():
        prior[dim] = {v: max(0.1, min(3.0, (a + 1) / (r + 1))) for v, (a, r) in vals.items()}
    DISCOVERY_PRIOR.write_text(json.dumps(prior, ensure_ascii=False, indent=1))
    return prior


def tool_get_discovery(status: str = "pending", limit: int = 50) -> dict:
    """List discovery candidates (default: pending), ranked by score."""
    data = _discovery_load()
    cands = data.get("candidates", [])
    if status:
        cands = [c for c in cands if c.get("status", "pending") == status]
    cands = sorted(cands, key=lambda c: -c.get("score", 0))[:limit]
    return {
        "generated_at": data.get("generated_at"),
        "channel": data.get("channel"),
        "counts": _discovery_counts(data),
        "candidates": cands,
    }


def tool_discovery_act(cand_id: str, action: str, note: str = "", reason_chip: str = "") -> dict:
    """Accept (→ source stub + reading queue) or dismiss a candidate; log feedback and
    refresh the learned prior."""
    if action not in ("accept", "dismiss"):
        raise ValueError("action must be 'accept' or 'dismiss'")
    data = _discovery_load()
    cand = next((c for c in data.get("candidates", []) if c.get("id") == cand_id), None)
    if not cand:
        raise ValueError(f"candidate not found: {cand_id}")
    result = {"action": action, "id": cand_id}
    if action == "accept":
        stub = tool_create_source_stub(
            title=cand.get("title", ""), url=cand.get("url", ""), doi=cand.get("doi", ""),
            authors=cand.get("authors", ""), year=cand.get("year"),
            notes=f"Discovered (frontier): {cand.get('reason', '')}", priority="normal")
        result["source_slug"] = stub.get("slug")
        result["staged_id"] = stub.get("staged_id")
        try:
            tool_add_to_queue(reference=stub.get("slug"),
                              reason=cand.get("reason", "discovery pick"), priority="normal")
            result["queued"] = True
        except Exception as e:
            logger.error(f"discovery queue-add failed: {e}")
    fb = {
        "id": cand_id, "action": action,
        "ts": datetime.now(timezone.utc).isoformat(),
        "signals": cand.get("signals") or {},
        "reason_chip": reason_chip, "note": note, "title": cand.get("title"),
    }
    with open(DISCOVERY_FEEDBACK, "a") as f:
        f.write(json.dumps(fb, ensure_ascii=False) + "\n")
    cand["status"] = "accepted" if action == "accept" else "dismissed"
    cand["decided_at"] = fb["ts"]
    if reason_chip:
        cand["reason_chip"] = reason_chip
    _discovery_save(data)
    _discovery_recompute_prior()
    result["prior_updated"] = True
    return result


@app.route("/pkis-api/discovery", methods=["POST"])
def pkis_api_discovery():
    b = _api_json()
    try:
        return _api_ok(tool_get_discovery(status=b.get("status", "pending"),
                                          limit=b.get("limit", 50)))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/discovery/act", methods=["POST"])
@require_write
def pkis_api_discovery_act():
    b = _api_json()
    try:
        return _api_ok(tool_discovery_act(
            cand_id=b.get("id"), action=b.get("action", ""),
            note=b.get("note", ""), reason_chip=b.get("reason_chip", "")))
    except ValueError as e:
        return _api_err(e)
    except Exception as e:
        return _api_err(e, 500)


# ── Architect doc-drift review (owner-only) — atomic, individually-acceptable items.
# The fortnightly audit (tools/architect_audit.py) writes drift items here; each is a
# single anchor→replacement edit to a living doc. Accept applies just that one edit
# and commits it; dismiss records the decision so it won't resurface.
DRIFT_INBOX = Path(os.environ.get("PKIS_DRIFT_PATH", "/home/pkis/architect_drift.json"))
_DRIFT_DOCS = ("docs/ARCHITECTURE.md", "docs/ABOUT.md", "docs/USAGE.md")


def _drift_load():
    if DRIFT_INBOX.exists():
        try:
            return json.loads(DRIFT_INBOX.read_text())
        except Exception:
            pass
    return {"items": []}


def _drift_save(data):
    DRIFT_INBOX.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def tool_docs_drift_list(status="pending"):
    data = _drift_load()
    all_items = data.get("items", [])
    counts = {}
    for x in all_items:
        s = x.get("status", "pending"); counts[s] = counts.get(s, 0) + 1
    items = [x for x in all_items if x.get("status", "pending") == status] if status else all_items
    return {"generated_at": data.get("generated_at"), "counts": counts, "items": items}


def tool_docs_drift_act(item_id, action):
    if action not in ("accept", "dismiss"):
        raise ValueError("action must be 'accept' or 'dismiss'")
    data = _drift_load()
    it = next((x for x in data.get("items", []) if x.get("id") == item_id), None)
    if not it:
        raise ValueError(f"drift item not found: {item_id}")
    if it.get("status") in ("accepted", "dismissed"):
        return {"action": action, "id": item_id, "already": it["status"]}
    result = {"action": action, "id": item_id}
    if action == "accept":
        doc_rel = it.get("doc", "")
        if doc_rel not in _DRIFT_DOCS:
            raise ValueError("doc not in the auditable set")
        path = REPO_DIR / doc_rel
        text = path.read_text()
        anchor = it.get("anchor", "")
        if not anchor or text.count(anchor) != 1:
            it["status"] = "stale"
            it["decided_at"] = datetime.now(timezone.utc).isoformat()
            _drift_save(data)
            raise ValueError("anchor no longer uniquely present - doc changed; item marked stale")
        path.write_text(text.replace(anchor, it.get("replacement", ""), 1))
        gp = _git_commit_and_push([str(path)], f"docs(architect): {it.get('title', 'apply drift fix')}")
        result["sha"] = gp.get("sha"); result["committed"] = gp.get("committed")
    it["status"] = "accepted" if action == "accept" else "dismissed"
    it["decided_at"] = datetime.now(timezone.utc).isoformat()
    _drift_save(data)
    return result


def _owner_gate(req):
    """None if the requester is the owner, else a (json, code) error response."""
    if is_owner(req):
        return None
    anon = (web_identity(req) is None and oauth_identity(req) is None and not _has_static_key(req))
    return (jsonify({"error": "sign in required"}), 401) if anon \
        else (jsonify({"error": "owner only - this surface is administrative"}), 403)


@app.route("/pkis-api/docs-drift", methods=["POST"])
def pkis_api_docs_drift():
    gate = _owner_gate(request)
    if gate:
        return gate
    b = _api_json()
    try:
        return _api_ok(tool_docs_drift_list(status=b.get("status", "pending")))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/docs-drift/act", methods=["POST"])
def pkis_api_docs_drift_act():
    gate = _owner_gate(request)
    if gate:
        return gate
    b = _api_json()
    try:
        return _api_ok(tool_docs_drift_act(b.get("id"), b.get("action", "")))
    except ValueError as e:
        return _api_err(e)
    except Exception as e:
        return _api_err(e, 500)


# ── Graph-gaps review (owner-only) — orphaned concept-side nodes + SUGGESTED typed
# edges. The fortnightly audit (tools/graph_audit.py) writes editable suggestions here;
# the inbox lets the owner edit the {target, predicate} edges then approve (applies via
# add_connections) or dismiss. Mirrors docs-drift, but the suggestions are editable.
GRAPH_GAPS = Path(os.environ.get("PKIS_GRAPH_GAPS_PATH", "/home/pkis/graph_gaps.json"))


def _gaps_load():
    if GRAPH_GAPS.exists():
        try:
            return json.loads(GRAPH_GAPS.read_text())
        except Exception:
            pass
    return {"items": []}


def _gaps_save(data):
    GRAPH_GAPS.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def tool_graph_gaps_list(status="pending"):
    data = _gaps_load()
    alli = data.get("items", [])
    counts = {}
    for x in alli:
        s = x.get("status", "pending"); counts[s] = counts.get(s, 0) + 1
    items = [x for x in alli if x.get("status", "pending") == status] if status else alli
    # surface the valid predicate vocabulary so the editor can offer a dropdown
    return {"counts": counts, "items": items, "predicates": list(EDGE_WEIGHTS.keys())}


def tool_graph_gaps_act(item_id, action, edges=None):
    if action not in ("accept", "dismiss"):
        raise ValueError("action must be 'accept' or 'dismiss'")
    data = _gaps_load()
    it = next((x for x in data.get("items", []) if x.get("id") == item_id), None)
    if not it:
        raise ValueError(f"gap item not found: {item_id}")
    if it.get("status") in ("accepted", "dismissed"):
        return {"action": action, "id": item_id, "already": it["status"]}
    result = {"action": action, "id": item_id}
    if action == "accept":
        # use the owner's (possibly edited) edges if provided, else the suggestions
        use = edges if edges else it.get("suggestions", [])
        use = [e for e in use if e.get("target") and e.get("predicate")]
        if not use:
            raise ValueError("no edges to apply — add at least one (target + predicate)")
        ec = [{"subject": it["iri"], "target": e["target"], "predicate": e["predicate"],
               "note": "graph-gaps: wire orphan"} for e in use]
        r = tool_add_connections(ec, commit_message=f"graph: wire orphan {it.get('slug','')} ({len(ec)} edge(s))")
        result["added"] = [x for x in r.get("results", []) if x.get("status") == "added"]
        result["errors"] = [x for x in r.get("results", []) if x.get("status") == "error"]
    it["status"] = "accepted" if action == "accept" else "dismissed"
    it["decided_at"] = datetime.now(timezone.utc).isoformat()
    _gaps_save(data)
    return result


@app.route("/pkis-api/graph-gaps", methods=["POST"])
def pkis_api_graph_gaps():
    gate = _owner_gate(request)
    if gate:
        return gate
    b = _api_json()
    try:
        return _api_ok(tool_graph_gaps_list(status=b.get("status", "pending")))
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/graph-gaps/act", methods=["POST"])
def pkis_api_graph_gaps_act():
    gate = _owner_gate(request)
    if gate:
        return gate
    b = _api_json()
    try:
        return _api_ok(tool_graph_gaps_act(b.get("id"), b.get("action", ""), edges=b.get("edges")))
    except ValueError as e:
        return _api_err(e)
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/upload-document", methods=["POST"])
@require_write
def pkis_api_upload_document():
    """Upload a document (base64) from the viewer. Stores it in the doc store and
    auto-creates the source node + reader if the slug is new. Mirrors the
    /docs/upload form's slug fallback (clean filename stem)."""
    b = _api_json()
    try:
        filename = (b.get("filename") or "").strip()
        if not filename:
            return _api_err("filename is required")
        slug = (b.get("slug") or "").strip()
        if not slug:
            slug = re.sub(r'[^a-z0-9]+', '-', Path(filename).stem.lower()).strip('-')[:55] or "source"
        return _api_ok(tool_upload_document(
            slug=slug,
            filename=filename,
            content_b64=b.get("content_b64", ""),
            push_to_readwise=bool(b.get("push_to_readwise", False)) and bool(READWISE_TOKEN),
        ))
    except ValueError as e:
        return _api_err(e)
    except Exception as e:
        return _api_err(e, 500)


@app.route("/pkis-api/save-url", methods=["POST"])
@require_write
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
@require_write
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


# Tier-2 dynamic explainers (Flask-backed, /pkis-api/x/<name>/). Optional + best
# effort: a load failure must never take down the main app.
try:
    import explainer_x
    explainer_x.register(
        app,
        is_write_authorized=globals().get("is_write_authorized"),
        log_usage=globals().get("log_usage"),
    )
    logger.info("dynamic-explainer blueprint mounted at /pkis-api/x")
except Exception as _ex:
    logger.warning(f"dynamic-explainer blueprint not loaded: {_ex}")


# ============================================================
# Entry point
# ============================================================

if __name__ == "__main__":
    import sys
    # Offline embedding build: `python app.py build-embeddings`. Run once at deploy
    # so the initial full encode (~minutes) happens out of band, not inside a
    # request that would trip gunicorn's worker timeout. Persists EMBED_CACHE_PATH;
    # the live workers then load vectors instantly and only re-encode on change.
    if len(sys.argv) > 1 and sys.argv[1] == "build-embeddings":
        if not _semantic_enabled():
            print(f"Semantic search disabled "
                  f"(SEMANTIC_SEARCH={SEMANTIC_SEARCH}, st_available={_ST_AVAILABLE}); nothing to build.")
            sys.exit(1)
        logger.info("Building embedding index offline...")
        build_embedding_index()
        print(f"Embedding index built: {len(STORE._embed_slugs)} nodes -> {EMBED_CACHE_PATH}")
        sys.exit(0)

    # Build caches on startup
    logger.info("Building caches on startup...")
    refresh_caches()
    logger.info("PKIS MCP server ready")
    app.run(host="127.0.0.1", port=5000, debug=False)
