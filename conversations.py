"""conversations.py — persistence for signed-in ask conversations.

Auto-saved, per-user (keyed by WorkOS `sub`), soft-deletable. A conversation is
just the rich turn list the viewer renders (role / content / citations / meta),
stored as its latest state — chats are append-only, so they don't need version
history.

Versioning/rollback lives on the *document* a conversation may be authoring (the
coming "studio" companion), NOT on chat turns — see `document_versions`, added
when the studio lands. The `artifact` / `anchor_*` columns are reserved now so
that slots in without a migration.

Pure stdlib (sqlite3/json/uuid/datetime) — no Flask/Anthropic import, so it stays
unit-testable in isolation and mirrors usage.py's store style.
"""

import json
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

_SCHEMA = """
CREATE TABLE IF NOT EXISTS conversations (
    id            TEXT PRIMARY KEY,
    user_sub      TEXT NOT NULL,
    title         TEXT NOT NULL DEFAULT '',
    messages      TEXT NOT NULL DEFAULT '[]',   -- JSON: the rich turn[] (latest state)
    created_at    TEXT NOT NULL,
    updated_at    TEXT NOT NULL,
    deleted_at    TEXT,                          -- soft delete (recoverable)
    anchor_type   TEXT,                          -- forward-compat: 'source'|'node'|'doc'
    anchor_ref    TEXT,                          -- forward-compat: an iri/slug
    artifact      TEXT                           -- forward-compat: companion doc (current)
);
CREATE INDEX IF NOT EXISTS idx_conv_user ON conversations(user_sub, updated_at DESC);
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
    """Create tables (idempotent)."""
    conn = _connect(db_path)
    try:
        conn.executescript(_SCHEMA)
        conn.commit()
    finally:
        conn.close()


_initialized = set()


def _ensure(db_path):
    """Lazily create the schema once per path. Lets `import app` stay filesystem-
    free until an endpoint is actually hit (the default DB path only exists on the
    server), while keeping every public call self-sufficient."""
    key = str(db_path)
    if key not in _initialized:
        init_store(db_path)
        _initialized.add(key)


def _derive_title(messages) -> str:
    """First user message, trimmed to a one-line title."""
    for m in messages or []:
        if isinstance(m, dict) and m.get("role") == "user":
            t = " ".join(str(m.get("content", "")).split())
            return (t[:70] + "…") if len(t) > 70 else (t or "Untitled")
    return "Untitled"


def _turn_count(messages) -> int:
    return sum(1 for m in (messages or []) if isinstance(m, dict) and m.get("role") == "user")


def save(db_path, user_sub, *, conv_id=None, messages, title=None,
         anchor=None, artifact=None) -> dict:
    """Create or update (upsert) a conversation's latest state.

    New conversation when conv_id is None/unknown → a fresh id and an auto title.
    Otherwise the caller must own it (user_sub match) — a mismatch raises
    PermissionError. Returns {id, title, created}.
    """
    if not user_sub:
        raise PermissionError("sign in required")
    _ensure(db_path)
    snapshot = json.dumps(messages or [], default=str)
    now = _utcnow_iso()
    conn = _connect(db_path)
    try:
        row = None
        if conv_id:
            row = conn.execute("SELECT user_sub, title FROM conversations WHERE id=?",
                               (conv_id,)).fetchone()
            if row and row["user_sub"] != user_sub:
                raise PermissionError("not your conversation")
        if not row:  # create
            cid = conv_id or uuid.uuid4().hex
            ttl = title or _derive_title(messages)
            conn.execute(
                "INSERT INTO conversations (id,user_sub,title,messages,created_at,updated_at,"
                "anchor_type,anchor_ref,artifact) VALUES (?,?,?,?,?,?,?,?,?)",
                (cid, user_sub, ttl, snapshot, now, now,
                 (anchor or {}).get("type"), (anchor or {}).get("ref"), artifact))
            conn.commit()
            return {"id": cid, "title": ttl, "created": True}
        ttl = title if title is not None else row["title"]
        conn.execute(
            "UPDATE conversations SET messages=?,title=?,artifact=?,updated_at=?,deleted_at=NULL"
            " WHERE id=?", (snapshot, ttl, artifact, now, conv_id))
        conn.commit()
        return {"id": conv_id, "title": ttl, "created": False}
    finally:
        conn.close()


def list_for_user(db_path, user_sub, include_deleted=False) -> list:
    """Conversation summaries for a user, newest-updated first."""
    _ensure(db_path)
    conn = _connect(db_path)
    try:
        q = "SELECT * FROM conversations WHERE user_sub=?"
        if not include_deleted:
            q += " AND deleted_at IS NULL"
        q += " ORDER BY updated_at DESC"
        out = []
        for r in conn.execute(q, (user_sub,)).fetchall():
            try:
                msgs = json.loads(r["messages"] or "[]")
            except Exception:
                msgs = []
            out.append({
                "id": r["id"], "title": r["title"],
                "created_at": r["created_at"], "updated_at": r["updated_at"],
                "turn_count": _turn_count(msgs),
                "anchor": ({"type": r["anchor_type"], "ref": r["anchor_ref"]}
                           if r["anchor_type"] else None),
                "deleted": bool(r["deleted_at"]),
            })
        return out
    finally:
        conn.close()


def get(db_path, user_sub, conv_id) -> dict:
    """Full conversation, or None if missing / not owned by this user."""
    _ensure(db_path)
    conn = _connect(db_path)
    try:
        r = conn.execute("SELECT * FROM conversations WHERE id=?", (conv_id,)).fetchone()
        if not r or r["user_sub"] != user_sub:
            return None
        try:
            messages = json.loads(r["messages"] or "[]")
        except Exception:
            messages = []
        return {
            "id": r["id"], "title": r["title"], "messages": messages,
            "created_at": r["created_at"], "updated_at": r["updated_at"],
            "deleted": bool(r["deleted_at"]),
            "anchor": ({"type": r["anchor_type"], "ref": r["anchor_ref"]}
                       if r["anchor_type"] else None),
            "artifact": r["artifact"],
        }
    finally:
        conn.close()


def _owned(conn, user_sub, conv_id):
    r = conn.execute("SELECT user_sub FROM conversations WHERE id=?", (conv_id,)).fetchone()
    return bool(r and r["user_sub"] == user_sub)


def rename(db_path, user_sub, conv_id, title) -> bool:
    _ensure(db_path)
    conn = _connect(db_path)
    try:
        if not _owned(conn, user_sub, conv_id):
            return False
        conn.execute("UPDATE conversations SET title=?,updated_at=? WHERE id=?",
                     (title or "Untitled", _utcnow_iso(), conv_id))
        conn.commit()
        return True
    finally:
        conn.close()


def set_deleted(db_path, user_sub, conv_id, deleted=True) -> bool:
    """Soft delete / undelete — recoverable; the row is kept."""
    _ensure(db_path)
    conn = _connect(db_path)
    try:
        if not _owned(conn, user_sub, conv_id):
            return False
        conn.execute("UPDATE conversations SET deleted_at=? WHERE id=?",
                     (_utcnow_iso() if deleted else None, conv_id))
        conn.commit()
        return True
    finally:
        conn.close()
