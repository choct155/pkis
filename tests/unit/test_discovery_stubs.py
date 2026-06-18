"""
tools/discovery_stubs_from_inbox.py — Phase-1c migration (discovery_inbox.json →
discovery-stub nodes). Locks the conformance the Hygienist's Check 7 enforces (≤2
primary_concepts, no Reading Path, no Key Extractions) and idempotency.
"""

import importlib.util
import json
from pathlib import Path

import frontmatter
import pytest

_ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location(
    "discovery_stubs", _ROOT / "tools" / "discovery_stubs_from_inbox.py")
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def _cand(**over):
    c = {
        "title": "Variational Message Passing in Factor Graphs",
        "authors": "A. Author, B. Writer", "year": "2021",
        "field": "Computer Science", "subfield": "Artificial Intelligence",
        "url": "https://doi.org/10.x", "doi": "10.x",
        "reason": "fills frontier gap Variational Inference; sim 0.85",
        "status": "pending", "discovered_at": "2026-06-15T07:05:17Z",
        "nearest_frontier": {"iri": "pkis:technique:variational-inference"},
        "links": [
            {"iri": "pkis:concept:variational-free-energy-vfe", "score": 0.033},
            {"iri": "pkis:framework:variational-inference-framework", "score": 0.032},
            {"iri": "pkis:concept:entropy", "score": 0.01},
        ],
    }
    c.update(over)
    return c


@pytest.mark.unit
def test_primary_concepts_frontier_first_max_two():
    pc = mod.pick_primary_concepts(_cand())
    assert pc[0] == "variational-inference"          # frontier gap first
    assert len(pc) == 2 and len(set(pc)) == 2         # capped, distinct


@pytest.mark.unit
def test_stub_is_conformant(tmp_path):
    slug, md = mod.stub_markdown(_cand())
    post = frontmatter.loads(md)
    assert post["id"] == f"pkis:discovery-stub:{slug}"
    assert post["knowledge_type"] == "discovery-stub"
    assert post["status"] == "parked"
    assert post["promoted"] is False
    assert len(post["primary_concepts"]) <= 2
    # Check 7 constraints: no Reading Path, no Key Extractions sections.
    assert "## Reading Path" not in md and "## Key Extractions" not in md


@pytest.mark.unit
def test_generate_is_idempotent_and_skips_decided(tmp_path):
    inbox = tmp_path / "inbox.json"
    out = tmp_path / "discovery"
    inbox.write_text(json.dumps({"candidates": [
        _cand(),
        _cand(title="Dismissed Paper", status="dismissed"),
    ]}))
    written, skipped = mod.generate(str(inbox), str(out), wiki_root=str(tmp_path))
    assert len(written) == 1                                   # dismissed skipped
    assert any("status=dismissed" in why for _, why in skipped)
    # Second run writes nothing (stub already on disk).
    written2, _ = mod.generate(str(inbox), str(out), wiki_root=str(tmp_path))
    assert written2 == []
