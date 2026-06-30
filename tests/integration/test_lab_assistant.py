"""
PKIS Lab Assistant (Part A) — descriptive monitoring, drift flags, transformations.
Hermetic: the monitor reads a tmp wiki directly; the report tool runs against the
fixture wiki. No external system, no live-wiki writes.
"""
import json
import os
import sys
from datetime import datetime, timezone

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools"))
import lab_monitor       # noqa: E402
import lab_transform     # noqa: E402

NOW = datetime(2026, 6, 30, tzinfo=timezone.utc)


def _node(wiki, folder, slug, **fm):
    d = wiki / folder
    d.mkdir(parents=True, exist_ok=True)
    body = "---\n" + "".join(f"{k}: {json.dumps(v)}\n" for k, v in fm.items()) + "---\n\n# " + slug + "\n"
    (d / f"{slug}.md").write_text(body)


def _build_wiki(tmp_path):
    w = tmp_path / "wiki"
    _node(w, "hypotheses", "h-open-1", id="pkis:hypothesis:h-open-1", knowledge_type="hypothesis",
          status="open", cluster_membership=["c1"], research_program_role="direct-test")
    _node(w, "hypotheses", "h-open-2", id="pkis:hypothesis:h-open-2", knowledge_type="hypothesis",
          status="open", cluster_membership=["c1"], research_program_role="boundary-condition")
    _node(w, "hypotheses", "h-conf", id="pkis:hypothesis:h-conf", knowledge_type="hypothesis",
          status="confirmed", cluster_membership=["c1"], research_program_role="direct-test")
    _node(w, "clusters", "c1", id="pkis:research-cluster:c1", knowledge_type="research-cluster",
          status="active", frontier_hypotheses=["h-open-1"], date_updated="2026-05-01")  # 60d stale
    _node(w, "concepts", "k1", id="pkis:concept:k1", knowledge_type="concept",
          coverage=4, understanding=3)
    return w


@pytest.mark.integration
def test_snapshot_status_distribution(tmp_path):
    snap = lab_monitor.compute_snapshot(_build_wiki(tmp_path), tmp_path, now=NOW)
    assert snap["hypothesis_status"] == {"open": 2, "confirmed": 1}
    assert snap["hypothesis_role"] == {"direct-test": 2, "boundary-condition": 1}
    assert snap["hypotheses_by_cluster"] == {"c1": 3}
    assert snap["node_counts"]["hypothesis"] == 3 and snap["node_counts"]["concept"] == 1
    assert snap["clusters"]["c1"]["frontier_count"] == 1
    assert snap["clusters"]["c1"]["staleness_days"] == 60
    assert snap["avg_coverage"] == 4.0 and snap["avg_understanding"] == 3.0


@pytest.mark.integration
def test_drift_flags_idle_cluster(tmp_path):
    snap = lab_monitor.compute_snapshot(_build_wiki(tmp_path), tmp_path, now=NOW)
    flags = lab_monitor.detect_drift(None, snap)
    assert any("c1" in f and "idle" in f for f in flags)


@pytest.mark.integration
def test_drift_flags_status_delta():
    prev = {"hypothesis_status": {"open": 3}}
    curr = {"hypothesis_status": {"open": 2, "confirmed": 1}, "clusters": {}, "oldest_staged_hours": None}
    flags = lab_monitor.detect_drift(prev, curr)
    assert any("open" in f and "-1" in f for f in flags)
    assert any("confirmed" in f and "+1" in f for f in flags)


@pytest.mark.integration
def test_snapshot_roundtrip_and_inbox(tmp_path):
    w = _build_wiki(tmp_path)
    lab_dir = tmp_path / "lab"
    snap = lab_monitor.compute_snapshot(w, tmp_path, now=NOW)
    lab_monitor.write_snapshot(snap, lab_dir, NOW)
    prev = lab_monitor.load_previous(lab_dir)
    assert prev["generated_at"] == snap["generated_at"]

    lab_monitor.append_inbox_flags(["Cluster `c1` idle 60d."], w, NOW)
    inbox = (w / "inbox.md").read_text()
    assert "## Lab" in inbox and "c1" in inbox


@pytest.mark.integration
def test_transform_apply_named_is_pure(tmp_path):
    snap = lab_monitor.compute_snapshot(_build_wiki(tmp_path), tmp_path, now=NOW)
    out = lab_transform.apply_named("cluster_staleness", [snap])
    assert out[0]["max_staleness_days"] == 60 and out[0]["cluster_count"] == 1
    assert "staleness_days_by_cluster" not in snap  # input untouched


@pytest.mark.integration
def test_get_lab_report_tool(appmod, isolated_wiki, monkeypatch, tmp_path):
    monkeypatch.setenv("PKIS_LAB_DIR", str(tmp_path / "lab"))
    rep = appmod.tool_get_lab_report()
    assert set(rep) >= {"snapshot", "drift_flags", "previous_snapshot_at"}
    assert "node_counts" in rep["snapshot"]
    assert isinstance(rep["drift_flags"], list)
