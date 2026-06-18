"""
Comptroller instrumentation seam (Roster Phase 4).

Proves the one app.py Anthropic call site (tool_detect_concepts) records a usage
event via usage.log_usage on a SUCCESSFUL call — and that the contract is
best-effort (a broken store never breaks the tool). The default hermetic suite
forces detect_concepts down its no-network fallback (create() raises), so this test
installs a fake client that returns a real-shaped response with .usage.
"""

import json

import pytest

import usage


class _FakeUsage:
    input_tokens = 1200
    output_tokens = 340
    cache_read_input_tokens = 0
    cache_creation_input_tokens = 0


class _FakeBlock:
    def __init__(self, text):
        self.text = text


class _FakeResponse:
    model = "claude-sonnet-4-20250514"
    usage = _FakeUsage()

    def __init__(self, text):
        self.content = [_FakeBlock(text)]


class _FakeClient:
    """Returns a fixed, valid detect_concepts JSON payload."""
    class messages:
        @staticmethod
        def create(*_a, **_k):
            return _FakeResponse(json.dumps([
                {"iri": "pkis:concept:bayesian-inference",
                 "confidence": 0.9, "reference_type": "explicit"}
            ]))


@pytest.mark.integration
def test_detect_concepts_logs_a_usage_event(appmod, monkeypatch, tmp_path):
    db = tmp_path / "usage.sqlite"
    usage.seed_pricing(db)
    monkeypatch.setattr(appmod, "USAGE_DB_PATH", db)
    monkeypatch.setattr(appmod, "anthropic_client", _FakeClient())
    appmod.STORE.invalidate_search()  # rebuild BM25 over the fixture wiki

    out = appmod.tool_detect_concepts("Bayesian inference updates beliefs with evidence.")
    assert any(r["iri"] == "pkis:concept:bayesian-inference" for r in out)

    events = usage.events_between(db, "1970-01-01", "2999-01-01")
    assert len(events) == 1
    e = events[0]
    assert e["origin"] == "pkis-mcp" and e["project"] == "pkis"
    assert e["model"] == "claude-sonnet-4-20250514"
    assert json.loads(e["attributes"]) == {"tool": "detect_concepts"}
    assert e["computed_cost_usd"] > 0


@pytest.mark.integration
def test_logging_failure_does_not_break_the_tool(appmod, monkeypatch):
    # Point the store at an impossible path: log_usage must swallow the error and
    # the tool must still return its result.
    monkeypatch.setattr(appmod, "USAGE_DB_PATH", "/proc/nonexistent/usage.sqlite\0bad")
    monkeypatch.setattr(appmod, "anthropic_client", _FakeClient())
    appmod.STORE.invalidate_search()
    out = appmod.tool_detect_concepts("Bayesian inference updates beliefs with evidence.")
    assert any(r["iri"] == "pkis:concept:bayesian-inference" for r in out)
