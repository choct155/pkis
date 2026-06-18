"""
PKIS usage accounting (Comptroller, Roster Phase 4).

A small, dependency-free module shared by two callers:

  * app.py   — calls log_usage() after each Claude API call (best-effort: a
               logging failure must NEVER break a tool call).
  * tools/comptroller.py — reads the same SQLite store to produce cost reports.

The store is SQLite at config.USAGE_DB_PATH (default /home/pkis/usage/usage.sqlite).
Schema + cost model are specified in COMPTROLLER.md. Pricing constants live in the
`config` table and are read at report time; each usage_events row keeps the cost
computed at emission time (no retro-pricing).

Pure stdlib (sqlite3/json/datetime). No Anthropic import, no Flask import — so it is
trivially unit-testable against a tmp DB and importable in any context.
"""

import json
import logging
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger("pkis.usage")

# --------------------------------------------------------------------------- #
# Schema
# --------------------------------------------------------------------------- #

_SCHEMA = """
CREATE TABLE IF NOT EXISTS config (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS usage_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emitted_at TIMESTAMP NOT NULL,
    origin TEXT NOT NULL,
    project TEXT,
    model TEXT NOT NULL,
    input_tokens INTEGER NOT NULL,
    output_tokens INTEGER NOT NULL,
    cache_read_tokens INTEGER DEFAULT 0,
    cache_write_tokens INTEGER DEFAULT 0,
    computed_cost_usd REAL NOT NULL,
    attributes TEXT
);

CREATE TABLE IF NOT EXISTS budget_periods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    fixed_cost_usd REAL NOT NULL,
    variable_cost_usd REAL NOT NULL,
    total_cost_usd REAL NOT NULL,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_usage_emitted_at ON usage_events(emitted_at);
CREATE INDEX IF NOT EXISTS idx_usage_origin ON usage_events(origin);
"""

# Default pricing seed (USD per million tokens). Example rates — confirm against
# current Anthropic pricing at deploy. Keyed by a model family prefix so several
# concrete model ids share one rate set; see _rate_prefix().
_DEFAULT_CONFIG = {
    "claude_sonnet_input_per_mtok": "3.00",
    "claude_sonnet_output_per_mtok": "15.00",
    "claude_sonnet_cache_read_per_mtok": "0.30",
    "claude_sonnet_cache_write_per_mtok": "3.75",
    "claude_opus_input_per_mtok": "15.00",
    "claude_opus_output_per_mtok": "75.00",
    "claude_opus_cache_read_per_mtok": "1.50",
    "claude_opus_cache_write_per_mtok": "18.75",
    "claude_haiku_input_per_mtok": "0.80",
    "claude_haiku_output_per_mtok": "4.00",
    "claude_haiku_cache_read_per_mtok": "0.08",
    "claude_haiku_cache_write_per_mtok": "1.00",
    "max_plan_monthly_usd": "100.00",
    "billing_cycle_start_day": "1",
}


# --------------------------------------------------------------------------- #
# Connection / init
# --------------------------------------------------------------------------- #

def _connect(db_path) -> sqlite3.Connection:
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    # Reduce 'database is locked' under the MCP server's concurrent workers.
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


def seed_pricing(db_path, overrides=None) -> None:
    """Insert default pricing/config rows if absent (idempotent — never clobbers
    an existing key, so manual rate edits survive re-seeding)."""
    init_store(db_path)
    values = dict(_DEFAULT_CONFIG)
    if overrides:
        values.update({k: str(v) for k, v in overrides.items()})
    conn = _connect(db_path)
    try:
        for k, v in values.items():
            conn.execute(
                "INSERT OR IGNORE INTO config(key, value) VALUES (?, ?)", (k, v)
            )
        conn.commit()
    finally:
        conn.close()


def get_config(db_path) -> dict:
    """Return the config table as a plain {key: value(str)} dict."""
    conn = _connect(db_path)
    try:
        return {r["key"]: r["value"] for r in conn.execute("SELECT key, value FROM config")}
    finally:
        conn.close()


# --------------------------------------------------------------------------- #
# Cost model
# --------------------------------------------------------------------------- #

def _rate_prefix(model: str) -> str:
    """Map a concrete model id to the config rate-key family prefix."""
    m = (model or "").lower()
    if "opus" in m:
        return "claude_opus"
    if "haiku" in m:
        return "claude_haiku"
    # Default family is sonnet (covers claude-sonnet-*, and unknown ids fall here).
    return "claude_sonnet"


def compute_cost(model, input_tokens, output_tokens,
                 cache_read_tokens=0, cache_write_tokens=0, rates=None) -> float:
    """Cost in USD for one call. `rates` is the config dict (from get_config); if
    None, the module defaults are used. Token counts are per-call totals."""
    rates = rates or _DEFAULT_CONFIG
    p = _rate_prefix(model)

    def rate(kind, default):
        try:
            return float(rates.get(f"{p}_{kind}_per_mtok", default))
        except (TypeError, ValueError):
            return float(default)

    in_r = rate("input", _DEFAULT_CONFIG[f"{p}_input_per_mtok"])
    out_r = rate("output", _DEFAULT_CONFIG[f"{p}_output_per_mtok"])
    cr_r = rate("cache_read", _DEFAULT_CONFIG[f"{p}_cache_read_per_mtok"])
    cw_r = rate("cache_write", _DEFAULT_CONFIG[f"{p}_cache_write_per_mtok"])

    cost = (
        (input_tokens or 0) * in_r
        + (output_tokens or 0) * out_r
        + (cache_read_tokens or 0) * cr_r
        + (cache_write_tokens or 0) * cw_r
    ) / 1_000_000.0
    return round(cost, 6)


# --------------------------------------------------------------------------- #
# Logging a usage event
# --------------------------------------------------------------------------- #

def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def log_usage(db_path, response, origin="pkis-mcp", project="pkis",
              attributes=None) -> bool:
    """Record one API call's usage. BEST-EFFORT: any failure is swallowed and
    logged, never raised — accounting must not break the serving path.

    `response` is an Anthropic Message (has .model and .usage). Returns True on a
    successful write, False otherwise.
    """
    try:
        usage = getattr(response, "usage", None)
        model = getattr(response, "model", "") or ""
        in_tok = int(getattr(usage, "input_tokens", 0) or 0)
        out_tok = int(getattr(usage, "output_tokens", 0) or 0)
        cache_read = int(getattr(usage, "cache_read_input_tokens", 0) or 0)
        cache_write = int(getattr(usage, "cache_creation_input_tokens", 0) or 0)

        rates = get_config(db_path)  # also ensures the store exists
        cost = compute_cost(model, in_tok, out_tok, cache_read, cache_write, rates)

        conn = _connect(db_path)
        try:
            conn.execute(
                """INSERT INTO usage_events
                   (emitted_at, origin, project, model, input_tokens, output_tokens,
                    cache_read_tokens, cache_write_tokens, computed_cost_usd, attributes)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (_utcnow_iso(), origin, project, model, in_tok, out_tok,
                 cache_read, cache_write, cost, json.dumps(attributes or {})),
            )
            conn.commit()
        finally:
            conn.close()
        return True
    except Exception as e:  # noqa: BLE001 — best-effort by design
        logger.warning("log_usage failed (non-fatal): %s", e)
        return False


# --------------------------------------------------------------------------- #
# Reporting queries (used by tools/comptroller.py)
# --------------------------------------------------------------------------- #

def events_between(db_path, start_iso, end_iso):
    """All usage_events with start_iso <= emitted_at < end_iso, as a list of dicts."""
    conn = _connect(db_path)
    try:
        rows = conn.execute(
            "SELECT * FROM usage_events WHERE emitted_at >= ? AND emitted_at < ? "
            "ORDER BY emitted_at",
            (start_iso, end_iso),
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def aggregate(events, key):
    """Group events by a column name; return {value: {calls, input_tokens,
    output_tokens, cost}} sorted by cost desc."""
    out = {}
    for e in events:
        k = e.get(key) or "(none)"
        bucket = out.setdefault(
            k, {"calls": 0, "input_tokens": 0, "output_tokens": 0, "cost": 0.0}
        )
        bucket["calls"] += 1
        bucket["input_tokens"] += e.get("input_tokens", 0) or 0
        bucket["output_tokens"] += e.get("output_tokens", 0) or 0
        bucket["cost"] += e.get("computed_cost_usd", 0.0) or 0.0
    return dict(sorted(out.items(), key=lambda kv: kv[1]["cost"], reverse=True))


def total_cost(events) -> float:
    return round(sum(e.get("computed_cost_usd", 0.0) or 0.0 for e in events), 6)
