"""
usage.py — Comptroller usage-accounting module (Roster Phase 4).

Pure-stdlib module, so these tests import it directly and run against a tmp SQLite
store — no app import, no network. They lock the cost model, the best-effort
log_usage contract (a logging failure must never raise), and the report aggregation
helpers that tools/comptroller.py builds on.
"""

import sqlite3

import pytest

import usage


class _FakeUsage:
    def __init__(self, **kw):
        self.input_tokens = kw.get("input_tokens", 0)
        self.output_tokens = kw.get("output_tokens", 0)
        self.cache_read_input_tokens = kw.get("cache_read_input_tokens", 0)
        self.cache_creation_input_tokens = kw.get("cache_creation_input_tokens", 0)


class _FakeResponse:
    def __init__(self, model, **usage_kw):
        self.model = model
        self.usage = _FakeUsage(**usage_kw)


# --------------------------------------------------------------------------- #
# Cost model
# --------------------------------------------------------------------------- #

@pytest.mark.unit
def test_compute_cost_sonnet_default_rates():
    # 1M input @ $3, 1M output @ $15 => $18 exactly with default seed rates.
    cost = usage.compute_cost("claude-sonnet-4-20250514", 1_000_000, 1_000_000)
    assert cost == pytest.approx(18.0)


@pytest.mark.unit
def test_compute_cost_includes_cache_tokens():
    # 1M cache-read @ $0.30 + 1M cache-write @ $3.75 = $4.05 (sonnet defaults).
    cost = usage.compute_cost("claude-sonnet-4-6", 0, 0,
                              cache_read_tokens=1_000_000,
                              cache_write_tokens=1_000_000)
    assert cost == pytest.approx(4.05)


@pytest.mark.unit
def test_compute_cost_model_family_routing():
    # Opus output rate ($75/mtok) is 5x sonnet ($15/mtok) for the same tokens.
    sonnet = usage.compute_cost("claude-sonnet-4-6", 0, 1_000_000)
    opus = usage.compute_cost("claude-opus-4-8", 0, 1_000_000)
    assert opus == pytest.approx(5 * sonnet)


@pytest.mark.unit
def test_compute_cost_unknown_model_falls_back_to_sonnet():
    known = usage.compute_cost("claude-sonnet-4-6", 1_000_000, 0)
    unknown = usage.compute_cost("some-future-model", 1_000_000, 0)
    assert unknown == pytest.approx(known)


# --------------------------------------------------------------------------- #
# Store init / seed
# --------------------------------------------------------------------------- #

@pytest.mark.unit
def test_seed_pricing_is_idempotent_and_preserves_edits(tmp_path):
    db = tmp_path / "usage.sqlite"
    usage.seed_pricing(db)
    # Simulate a manual rate edit.
    conn = sqlite3.connect(str(db))
    conn.execute("UPDATE config SET value='9.99' WHERE key='claude_sonnet_input_per_mtok'")
    conn.commit()
    conn.close()
    # Re-seeding must not clobber the edited value.
    usage.seed_pricing(db)
    cfg = usage.get_config(db)
    assert cfg["claude_sonnet_input_per_mtok"] == "9.99"


# --------------------------------------------------------------------------- #
# log_usage — happy path + best-effort contract
# --------------------------------------------------------------------------- #

@pytest.mark.unit
def test_log_usage_writes_event_and_computes_cost(tmp_path):
    db = tmp_path / "usage.sqlite"
    usage.seed_pricing(db)
    resp = _FakeResponse("claude-sonnet-4-20250514",
                         input_tokens=1000, output_tokens=500)
    assert usage.log_usage(db, resp, origin="pkis-mcp", project="pkis",
                           attributes={"tool": "detect_concepts"}) is True

    events = usage.events_between(db, "1970-01-01", "2999-01-01")
    assert len(events) == 1
    e = events[0]
    assert e["origin"] == "pkis-mcp"
    assert e["model"] == "claude-sonnet-4-20250514"
    assert e["input_tokens"] == 1000 and e["output_tokens"] == 500
    # 1000 in @ $3/mtok + 500 out @ $15/mtok = 0.003 + 0.0075 = 0.0105
    assert e["computed_cost_usd"] == pytest.approx(0.0105)


@pytest.mark.unit
def test_log_usage_is_best_effort_never_raises():
    # An undirected/garbage db path + a response missing .usage must NOT raise;
    # it returns False. This is the serving-path safety contract.
    class _Bad:
        model = "claude-sonnet-4-6"
        # no .usage attribute
    ok = usage.log_usage("/this/path/does/not/exist/and/cannot/be/made\0/x.sqlite", _Bad())
    assert ok is False


# --------------------------------------------------------------------------- #
# Aggregation helpers
# --------------------------------------------------------------------------- #

@pytest.mark.unit
def test_insert_event_explicit_timestamp_and_dedup_keys(tmp_path):
    db = tmp_path / "usage.sqlite"
    usage.seed_pricing(db)
    usage.insert_event(db, emitted_at="2026-06-14T10:00:00Z", origin="claude-code",
                       project="proj", model="claude-sonnet-4-6",
                       input_tokens=1000, output_tokens=500,
                       attributes={"dedup_key": "req-1"})
    events = usage.events_between(db, "1970-01-01", "2999-01-01")
    assert len(events) == 1 and events[0]["emitted_at"] == "2026-06-14T10:00:00Z"
    assert events[0]["computed_cost_usd"] == pytest.approx(0.0105)
    assert usage.existing_dedup_keys(db, "claude-code") == {"req-1"}
    assert usage.existing_dedup_keys(db, "pkis-mcp") == set()


@pytest.mark.unit
def test_aggregate_and_total(tmp_path):
    db = tmp_path / "usage.sqlite"
    usage.seed_pricing(db)
    usage.log_usage(db, _FakeResponse("claude-sonnet-4-6", input_tokens=1000, output_tokens=1000),
                    origin="pkis-mcp")
    usage.log_usage(db, _FakeResponse("claude-opus-4-8", input_tokens=1000, output_tokens=1000),
                    origin="claude-code")
    events = usage.events_between(db, "1970-01-01", "2999-01-01")
    by_origin = usage.aggregate(events, "origin")
    assert set(by_origin) == {"pkis-mcp", "claude-code"}
    assert by_origin["pkis-mcp"]["calls"] == 1
    # Opus costs more, so it sorts first (dict insertion order = cost desc).
    assert list(by_origin)[0] == "claude-code"
    assert usage.total_cost(events) == pytest.approx(
        sum(e["computed_cost_usd"] for e in events))
