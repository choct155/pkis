"""shares.py — capability-link sharing for private artifacts.

A share is an unguessable token granting READ-ONLY public access to one owned
item — a conversation today; nodes / studio docs later (same mechanism). Anyone
with the link can view; no account needed; the owner can revoke (and links may
carry an optional expiry). Possession of the token IS the authorization, so
tokens are long and random (`secrets.token_urlsafe`).

This module only maps token → (kind, ref, owner). It deliberately knows nothing
about the items themselves: the endpoint resolves a token, then fetches the
content via the item's own store (scoped to the share's owner_sub). Pure stdlib,
mirrors conversations.py (lazy `_ensure`, WAL).
"""

import secrets
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

_SCHEMA = """
CREATE TABLE IF NOT EXISTS shares (
    token       TEXT PRIMARY KEY,
    kind        TEXT NOT NULL,        -- 'conversation' | 'node' | 'doc'
    ref         TEXT NOT NULL,        -- conversation id / node slug / doc id
    owner_sub   TEXT NOT NULL,
    created_at  TEXT NOT NULL,
    revoked_at  TEXT,                 -- set → link dead
    expires_at  TEXT                  -- optional ISO; past → link dead
);
CREATE INDEX IF NOT EXISTS idx_shares_owner ON shares(owner_sub);
CREATE INDEX IF NOT EXISTS idx_shares_ref ON shares(owner_sub, kind, ref);
"""


def _utcnow_iso():
    return datetime.now(timezone.utc).isoformat()


def _connect(db_path) -> sqlite3.Connection:
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA busy_timeout=3000;")
    return conn


def init_store(db_path) -> None:
    conn = _connect(db_path)
    try:
        conn.executescript(_SCHEMA)
        conn.commit()
    finally:
        conn.close()


_initialized = set()


def _ensure(db_path):
    key = str(db_path)
    if key not in _initialized:
        init_store(db_path)
        _initialized.add(key)


def _active(row) -> bool:
    if not row or row["revoked_at"]:
        return False
    exp = row["expires_at"]
    return not (exp and exp < _utcnow_iso())


def mint(db_path, owner_sub, kind, ref, expires_at=None) -> dict:
    """Create (or reuse) a share token for one owned item. Idempotent: if an
    active token already exists for (owner, kind, ref), return it rather than
    minting a duplicate — so re-sharing yields a stable link. Returns
    {token, created}."""
    if not owner_sub:
        raise PermissionError("sign in required")
    _ensure(db_path)
    conn = _connect(db_path)
    try:
        for r in conn.execute(
            "SELECT * FROM shares WHERE owner_sub=? AND kind=? AND ref=?",
            (owner_sub, kind, ref)).fetchall():
            if _active(r):
                return {"token": r["token"], "created": False}
        token = secrets.token_urlsafe(16)
        conn.execute(
            "INSERT INTO shares (token,kind,ref,owner_sub,created_at,expires_at)"
            " VALUES (?,?,?,?,?,?)", (token, kind, ref, owner_sub, _utcnow_iso(), expires_at))
        conn.commit()
        return {"token": token, "created": True}
    finally:
        conn.close()


def resolve(db_path, token) -> dict:
    """Public: token → {kind, ref, owner_sub} if the share is active, else None.
    The caller then fetches the actual content scoped to owner_sub."""
    if not token:
        return None
    _ensure(db_path)
    conn = _connect(db_path)
    try:
        r = conn.execute("SELECT * FROM shares WHERE token=?", (token,)).fetchone()
        if not _active(r):
            return None
        return {"kind": r["kind"], "ref": r["ref"], "owner_sub": r["owner_sub"]}
    finally:
        conn.close()


def revoke(db_path, owner_sub, token) -> bool:
    """Owner-only: kill a link. Returns False if not found / not owned."""
    _ensure(db_path)
    conn = _connect(db_path)
    try:
        r = conn.execute("SELECT owner_sub FROM shares WHERE token=?", (token,)).fetchone()
        if not r or r["owner_sub"] != owner_sub:
            return False
        conn.execute("UPDATE shares SET revoked_at=? WHERE token=?", (_utcnow_iso(), token))
        conn.commit()
        return True
    finally:
        conn.close()


def active_token_for(db_path, owner_sub, kind, ref) -> str:
    """The existing active share token for an item, or None — so the UI can show
    'shared' state and offer revoke without minting."""
    _ensure(db_path)
    conn = _connect(db_path)
    try:
        for r in conn.execute(
            "SELECT * FROM shares WHERE owner_sub=? AND kind=? AND ref=?",
            (owner_sub, kind, ref)).fetchall():
            if _active(r):
                return r["token"]
        return None
    finally:
        conn.close()
