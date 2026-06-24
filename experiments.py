"""PKIS retrieval-experiment store.

Append-only SQLite log of search/ask runs for the retrieval lab. One row per
(query, profile) execution; a comparison run shares a `comparison_id` so the lab
can render columns side by side and the owner can revisit experiments over time.

Each row captures everything needed to interpret and reproduce a run: the query,
the resolved profile, the corpus state (`corpus_head` = git HEAD), the computed
metrics, the per-stage trace, separated retrieval/eval cost, and a compact
payload (result IRIs+titles, or the answer text for ask).

Pure stdlib (sqlite3/json/datetime), mirroring usage.py — trivially unit-testable
against a tmp DB, importable in any context. Store path: config.EXPERIMENT_DB_PATH.
"""

import json
import logging
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger("pkis.experiments")

_SCHEMA = """
CREATE TABLE IF NOT EXISTS experiments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emitted_at TIMESTAMP NOT NULL,
    comparison_id TEXT,
    paradigm TEXT NOT NULL,
    query TEXT NOT NULL,
    profile_name TEXT,
    profile TEXT,
    corpus_head TEXT,
    n_results INTEGER,
    retrieval_ms REAL,
    eval_ms REAL,
    eval_cost_usd REAL,
    total_cost_usd REAL,
    metrics TEXT,
    trace TEXT,
    payload TEXT
);
CREATE INDEX IF NOT EXISTS idx_exp_emitted ON experiments(emitted_at);
CREATE INDEX IF NOT EXISTS idx_exp_comparison ON experiments(comparison_id);

-- Standing-eval loop (C-1f). Every deliberate owner query becomes a test case;
-- the nightly runner replays the whole set through the profile suite.
CREATE TABLE IF NOT EXISTS query_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query_norm TEXT UNIQUE NOT NULL,
    query TEXT NOT NULL,
    paradigm TEXT,
    source TEXT,
    count INTEGER DEFAULT 1,
    first_seen TIMESTAMP,
    last_seen TIMESTAMP
);

-- Feedback tap — the supervised target. Winner verdicts are held until feedback
-- exists, so nightly metrics stay descriptive until these rows accumulate.
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emitted_at TIMESTAMP NOT NULL,
    query TEXT,
    comparison_id TEXT,
    paradigm TEXT,
    chosen_profile TEXT,
    chosen_iri TEXT,
    rating TEXT,
    notes TEXT
);
"""

_JSON_FIELDS = ("profile", "metrics", "trace", "payload")


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


def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def log_experiment(db_path, record: dict):
    """Insert one experiment row. BEST-EFFORT: returns the new row id, or None on
    failure (logging must never break the serving path). JSON fields are encoded
    here so callers pass plain dicts/lists."""
    try:
        init_store(db_path)
        r = dict(record)
        r.setdefault("emitted_at", _utcnow_iso())
        for f in _JSON_FIELDS:
            if not isinstance(r.get(f), str):
                r[f] = json.dumps(r.get(f))
        cols = ("emitted_at", "comparison_id", "paradigm", "query", "profile_name",
                "profile", "corpus_head", "n_results", "retrieval_ms", "eval_ms",
                "eval_cost_usd", "total_cost_usd", "metrics", "trace", "payload")
        conn = _connect(db_path)
        try:
            cur = conn.execute(
                f"INSERT INTO experiments ({','.join(cols)}) "
                f"VALUES ({','.join('?' for _ in cols)})",
                tuple(r.get(c) for c in cols),
            )
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()
    except Exception as e:  # noqa: BLE001 — best-effort by design
        logger.warning("log_experiment failed (non-fatal): %s", e)
        return None


def _row_to_dict(row) -> dict:
    d = dict(row)
    for f in _JSON_FIELDS:
        if d.get(f):
            try:
                d[f] = json.loads(d[f])
            except Exception:
                pass
    return d


def _normalize_query(q: str) -> str:
    return " ".join((q or "").lower().split())


def log_query(db_path, query, paradigm="search", source="owner"):
    """Upsert a deliberate query into the standing test set (deduped on normalized
    text; increments count + last_seen on repeat). BEST-EFFORT. Returns True on a
    write. Short/empty queries are ignored."""
    norm = _normalize_query(query)
    if len(norm) < 2:
        return False
    try:
        init_store(db_path)
        now = _utcnow_iso()
        conn = _connect(db_path)
        try:
            conn.execute(
                """INSERT INTO query_log (query_norm, query, paradigm, source, count, first_seen, last_seen)
                   VALUES (?, ?, ?, ?, 1, ?, ?)
                   ON CONFLICT(query_norm) DO UPDATE SET
                       count = count + 1, last_seen = excluded.last_seen,
                       paradigm = excluded.paradigm""",
                (norm, query.strip(), paradigm, source, now, now),
            )
            conn.commit()
            return True
        finally:
            conn.close()
    except Exception as e:  # noqa: BLE001
        logger.warning("log_query failed (non-fatal): %s", e)
        return False


def list_queries(db_path, limit=1000, paradigm=None) -> list:
    """The standing test set — distinct queries, most-used / most-recent first."""
    init_store(db_path)
    where, params = "", []
    if paradigm:
        where = " WHERE paradigm = ?"
        params.append(paradigm)
    conn = _connect(db_path)
    try:
        rows = conn.execute(
            f"SELECT * FROM query_log{where} ORDER BY count DESC, last_seen DESC LIMIT ?",
            (*params, int(limit)),
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def log_feedback(db_path, record: dict):
    """Record one feedback signal (owner verdict on a query/comparison). BEST-EFFORT."""
    try:
        init_store(db_path)
        r = dict(record)
        r.setdefault("emitted_at", _utcnow_iso())
        cols = ("emitted_at", "query", "comparison_id", "paradigm",
                "chosen_profile", "chosen_iri", "rating", "notes")
        conn = _connect(db_path)
        try:
            cur = conn.execute(
                f"INSERT INTO feedback ({','.join(cols)}) VALUES ({','.join('?' for _ in cols)})",
                tuple(r.get(c) for c in cols),
            )
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()
    except Exception as e:  # noqa: BLE001
        logger.warning("log_feedback failed (non-fatal): %s", e)
        return None


def list_feedback(db_path, limit=200) -> list:
    init_store(db_path)
    conn = _connect(db_path)
    try:
        rows = conn.execute(
            "SELECT * FROM feedback ORDER BY id DESC LIMIT ?", (int(limit),)
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def list_experiments(db_path, limit=50, comparison_id=None, paradigm=None) -> list:
    """Most-recent experiments first, optionally filtered by comparison or paradigm."""
    init_store(db_path)
    clauses, params = [], []
    if comparison_id:
        clauses.append("comparison_id = ?")
        params.append(comparison_id)
    if paradigm:
        clauses.append("paradigm = ?")
        params.append(paradigm)
    where = (" WHERE " + " AND ".join(clauses)) if clauses else ""
    conn = _connect(db_path)
    try:
        rows = conn.execute(
            f"SELECT * FROM experiments{where} ORDER BY id DESC LIMIT ?",
            (*params, int(limit)),
        ).fetchall()
        return [_row_to_dict(r) for r in rows]
    finally:
        conn.close()
