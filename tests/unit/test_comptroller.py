"""
tools/comptroller.py — usage cost reporting CLI (Roster Phase 4).

Tests the pure pieces (window math, report rendering against a seeded tmp store,
the threshold->inbox alert with its idempotent under-heading insert) by importing
the module from its file path, plus one end-to-end subprocess run of the CLI.
"""

import importlib.util
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

import usage

_ROOT = Path(__file__).resolve().parents[2]
_SCRIPT = _ROOT / "tools" / "comptroller.py"

_spec = importlib.util.spec_from_file_location("comptroller", _SCRIPT)
comptroller = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(comptroller)


class _FakeUsage:
    def __init__(self, i, o):
        self.input_tokens, self.output_tokens = i, o
        self.cache_read_input_tokens = 0
        self.cache_creation_input_tokens = 0


class _FakeResponse:
    def __init__(self, model, i, o):
        self.model, self.usage = model, _FakeUsage(i, o)


# --------------------------------------------------------------------------- #
# Window math
# --------------------------------------------------------------------------- #

@pytest.mark.unit
def test_daily_window_is_previous_full_day():
    now = datetime(2026, 6, 14, 9, 30, tzinfo=timezone.utc)
    start, end, label = comptroller.compute_window("daily", now)
    assert label == "daily"
    assert start == datetime(2026, 6, 13, 0, 0, tzinfo=timezone.utc)
    assert end == datetime(2026, 6, 14, 0, 0, tzinfo=timezone.utc)


@pytest.mark.unit
def test_weekly_window_is_trailing_7_days():
    now = datetime(2026, 6, 14, 9, 30, tzinfo=timezone.utc)
    start, end, _ = comptroller.compute_window("weekly", now)
    assert (end - start).days == 7
    assert end == now


@pytest.mark.unit
def test_monthly_window_respects_billing_start_day():
    now = datetime(2026, 6, 20, 12, 0, tzinfo=timezone.utc)
    start, _, _ = comptroller.compute_window("monthly", now, billing_start_day=1)
    assert start == datetime(2026, 6, 1, 0, 0, tzinfo=timezone.utc)


# --------------------------------------------------------------------------- #
# Report rendering
# --------------------------------------------------------------------------- #

@pytest.mark.unit
def test_render_report_aggregates_costs(tmp_path):
    db = tmp_path / "usage.sqlite"
    usage.seed_pricing(db)
    usage.log_usage(db, _FakeResponse("claude-sonnet-4-6", 1000, 1000), origin="pkis-mcp")
    usage.log_usage(db, _FakeResponse("claude-opus-4-8", 1000, 1000), origin="claude-code")
    now = datetime.now(timezone.utc)
    report, summary = comptroller.render_report(db, "ytd", now)
    assert "# Comptroller Report" in report
    assert "### By Origin" in report
    assert "pkis-mcp" in report and "claude-code" in report
    assert summary["events"] == 2
    assert summary["variable"] == pytest.approx(usage.total_cost(
        usage.events_between(db, "1970-01-01", "2999-01-01")))


# --------------------------------------------------------------------------- #
# Inbox alert
# --------------------------------------------------------------------------- #

def _inbox(tmp_path):
    p = tmp_path / "inbox.md"
    p.write_text("# PKIS Inbox\n\n## Conformance\nstuff\n\n## Budget\n"
                 "Cost alerts from the Comptroller.\n")
    return p


@pytest.mark.unit
def test_alert_appends_under_budget_when_over_threshold(tmp_path):
    inbox = _inbox(tmp_path)
    summary = {"kind": "weekly", "variable": 60.0, "fixed_monthly": 100.0,
               "report_date": "2026-06-14"}
    line = comptroller.maybe_alert_inbox(inbox, summary, threshold_frac=0.5)
    assert line is not None
    text = inbox.read_text()
    # Inserted inside the Budget section (after its heading, before EOF).
    assert "## Budget" in text and line in text
    assert text.index(line) > text.index("## Budget")


@pytest.mark.unit
def test_alert_is_idempotent_and_silent_under_threshold(tmp_path):
    inbox = _inbox(tmp_path)
    over = {"kind": "weekly", "variable": 60.0, "fixed_monthly": 100.0,
            "report_date": "2026-06-14"}
    comptroller.maybe_alert_inbox(inbox, over, 0.5)
    comptroller.maybe_alert_inbox(inbox, over, 0.5)  # second call: no dup
    assert inbox.read_text().count("Weekly variable cost") == 1

    under = {"kind": "weekly", "variable": 10.0, "fixed_monthly": 100.0,
             "report_date": "2026-06-15"}
    assert comptroller.maybe_alert_inbox(inbox, under, 0.5) is None


# --------------------------------------------------------------------------- #
# CLI end-to-end
# --------------------------------------------------------------------------- #

@pytest.mark.unit
def test_cli_init_then_report(tmp_path):
    db = tmp_path / "usage.sqlite"
    out = tmp_path / "out"
    r1 = subprocess.run([sys.executable, str(_SCRIPT), "init", "--db", str(db)],
                        capture_output=True, text=True)
    assert r1.returncode == 0 and db.exists()
    r2 = subprocess.run([sys.executable, str(_SCRIPT), "report", "ytd",
                         "--db", str(db), "--out", str(out)],
                        capture_output=True, text=True)
    assert r2.returncode == 0
    assert list(out.glob("comptroller_report_*.md")), r2.stdout + r2.stderr
