"""
Seam A — MCP dispatch ↔ tool_* implementations (ARCHITECTURE_AUDIT.md §7 Seam A).

The MCP tool surface is the de-facto API every Claude agent depends on. These are
the regression guards the review plan calls "Priority 1": call each tool with
canonical input over the real JSON-RPC endpoint and assert the *observable
contract* (shape + required fields), never internal behavior.

Status: the harness-level guards (F-1 invariant, JSON-RPC envelope, tools/list
well-formedness, two representative read tools) are IMPLEMENTED and should pass.
The per-tool input/output contract tests are STUBS with docstrings — to be filled
in during the review of this scaffold.
"""

import base64
import json
import subprocess

import pytest


# --------------------------------------------------------------------------- #
# Surface extraction. Advertised tools come from _get_tools_list(); dispatchable
# tools come from the module-level registry (READ_TOOLS / TRUSTED_TOOLS /
# WRITE_TOOLS, combined as DISPATCHABLE_TOOLS) introduced when dispatch was made
# introspectable. No source parsing needed.
# --------------------------------------------------------------------------- #

def _advertised_names(appmod) -> set:
    return {t["name"] for t in appmod._get_tools_list()}


def _dispatchable_names(appmod) -> set:
    return set(appmod.DISPATCHABLE_TOOLS)


# The 14 tools that are dispatchable but deliberately NOT advertised, as of the
# Phase-1 audit (§2.2). Freezing this set turns any NEW accidental hidden tool
# into a test failure. Per decision D-2, the two "mnemon" trusted-tier tools are
# slated to become advertised in Phase 3 — see test_mnemon_tools_should_be_advertised.
# After B5 only two tools stay reachable-but-unadvertised (decision pending —
# possible external callers we can't confirm; not removed). The other 12 former
# hidden tools were advertised.
KNOWN_HIDDEN = {"search_wiki_index", "get_node_stub"}


# --------------------------------------------------------------------------- #
# F-1 — the cheapest high-value guard in the whole plan (§2.2, §9 step 1).
# --------------------------------------------------------------------------- #

@pytest.mark.contract
def test_every_advertised_tool_is_dispatchable(appmod):
    """No tool may be advertised in tools/list without a dispatch handler — that
    would be a phantom tool that 404s when called."""
    missing = _advertised_names(appmod) - _dispatchable_names(appmod)
    assert not missing, f"advertised but not dispatchable (phantom tools): {sorted(missing)}"


@pytest.mark.contract
def test_hidden_tool_set_is_frozen(appmod):
    """Dispatchable-but-unadvertised tools must match the known set. A new entry
    here means a tool was wired into dispatch without being advertised — either
    advertise it or remove it; don't let it drift silently (§2.2)."""
    hidden = _dispatchable_names(appmod) - _advertised_names(appmod)
    assert hidden == KNOWN_HIDDEN, (
        f"hidden-tool drift.\n  newly hidden: {sorted(hidden - KNOWN_HIDDEN)}"
        f"\n  no longer hidden: {sorted(KNOWN_HIDDEN - hidden)}"
    )


@pytest.mark.contract
def test_mnemon_tools_are_advertised(appmod):
    """Decision D-2: the mnemon trusted tier is kept and advertised (done in B5)."""
    advertised = _advertised_names(appmod)
    assert {"register_operational_reference", "log_operation"} <= advertised


# --------------------------------------------------------------------------- #
# JSON-RPC transport envelope (§2.4).
# --------------------------------------------------------------------------- #

def _rpc(client, method, params=None, rid=1):
    body = {"jsonrpc": "2.0", "id": rid, "method": method}
    if params is not None:
        body["params"] = params
    return client.post("/mcp", json=body)


@pytest.mark.contract
def test_initialize_negotiates_protocol(client, appmod):
    r = _rpc(client, "initialize", {"protocolVersion": "2025-06-18"})
    assert r.status_code == 200
    result = r.get_json()["result"]
    assert result["protocolVersion"] in appmod.MCP_SUPPORTED_PROTOCOL_VERSIONS
    assert "tools" in result["capabilities"]
    assert result["serverInfo"]["name"]


@pytest.mark.contract
def test_tools_list_is_well_formed(client):
    """Every advertised tool must carry name, description, and a valid inputSchema
    object — the schema is what MCP clients build their call UIs from."""
    result = _rpc(client, "tools/list").get_json()["result"]
    tools = result["tools"]
    assert len(tools) == 43, "advertised tool count changed — update the contract baseline intentionally"
    for t in tools:
        assert t["name"]
        assert t["description"]
        assert t["inputSchema"]["type"] == "object"
        assert "properties" in t["inputSchema"]


@pytest.mark.contract
def test_unknown_method_returns_jsonrpc_error(client):
    r = _rpc(client, "no/such/method")
    assert r.get_json()["error"]["code"] == -32601


@pytest.mark.contract
def test_unknown_tool_returns_error(client):
    r = _rpc(client, "tools/call", {"name": "no_such_tool", "arguments": {}})
    assert r.get_json().get("error") is not None


# --------------------------------------------------------------------------- #
# Representative read-tool contracts (IMPLEMENTED — prove the harness works).
# --------------------------------------------------------------------------- #

def _call_tool(client, name, arguments=None):
    r = _rpc(client, "tools/call", {"name": name, "arguments": arguments or {}})
    payload = r.get_json()
    assert "result" in payload, f"{name} errored: {payload.get('error')}"
    # tools/call wraps the result as content[0].text containing JSON.
    return json.loads(payload["result"]["content"][0]["text"])


@pytest.mark.contract
def test_get_health_metrics_shape(client):
    m = _call_tool(client, "get_health_metrics")
    for key in ("total_nodes", "total_sources", "total_concepts", "avg_coverage",
                "avg_understanding", "cross_domain_connections", "queue_depth",
                "stubs_awaiting_deepening", "stubs_missing_source", "total_edges"):
        assert key in m, f"get_health_metrics missing {key}"
    assert m["total_nodes"] >= 4  # the seeded fixture nodes
    assert isinstance(m["total_edges"], int)


@pytest.mark.contract
def test_get_write_schema_shape(client):
    s = _call_tool(client, "get_write_schema")
    assert isinstance(s, dict) and s, "get_write_schema must return a non-empty object"


@pytest.mark.contract
def test_resolve_concept_finds_seeded_node(client):
    out = _call_tool(client, "resolve_concept", {"surface_form": "Bayesian Inference"})
    assert out, "expected a resolution for a seeded concept"


@pytest.mark.contract
def test_get_sourceless_stubs_returns_flagged_node(client):
    out = _call_tool(client, "get_sourceless_stubs")
    iris = {n.get("iri") for n in out}
    assert "pkis:concept:sourceless-example" in iris


# --------------------------------------------------------------------------- #
# Per-tool input/output contracts — STUBS to complete during scaffold review.
# One test per advertised read + write tool, asserting canonical input → shape.
# --------------------------------------------------------------------------- #

# ── Read-tool contracts: canonical input → documented shape (IMPLEMENTED) ──

def _has(d, *keys):
    return isinstance(d, dict) and all(k in d for k in keys)


# (tool, arguments, validator) against the session fixture wiki (4 seeded nodes).
READ_CONTRACT_CASES = [
    ("search_wiki", {"query": "entropy"},
     lambda r: isinstance(r, list) and (not r or _has(r[0], "iri", "canonical_title", "score"))),
    ("get_node", {"iri": "pkis:concept:entropy"},
     lambda r: _has(r, "iri") and r["iri"] == "pkis:concept:entropy"),
    ("detect_concepts", {"text": "Bayesian inference updates beliefs with evidence."},
     lambda r: isinstance(r, list)),
    ("get_related", {"iri": "pkis:concept:entropy"},
     lambda r: isinstance(r, list)),
    ("get_reading_queue", {},
     lambda r: isinstance(r, list)),
    ("get_concept_frontier", {},
     lambda r: _has(r, "params", "results") and isinstance(r["results"], list)),
    ("get_reading_graph", {},
     lambda r: isinstance(r, dict)),
    ("get_staged_nodes", {},
     lambda r: isinstance(r, list)),
    ("get_transcript_queue", {},
     lambda r: isinstance(r, list)),
    ("list_documents", {},
     lambda r: isinstance(r, list)),
]


@pytest.mark.contract
@pytest.mark.parametrize("tool,args,check", READ_CONTRACT_CASES, ids=[c[0] for c in READ_CONTRACT_CASES])
def test_read_tool_contract(client, tool, args, check):
    """Each advertised read tool: canonical valid input → documented response
    shape. Read tools need no auth; they run against the session fixture wiki."""
    result = _call_tool(client, tool, args)
    assert check(result), f"{tool} returned unexpected shape: {result!r}"


# ── Write-tool contracts (IMPLEMENTED) ──
# Each tool is called DIRECTLY (auth is Seam E, not this test) against an isolated
# wiki + git repo. The 3 network tools mock their boundary functions; tools that
# would touch real on-disk stores (DOCS_DIR, RAW_DIR, the priority config, the
# source-graph subprocess) have those redirected/stubbed so the suite stays hermetic.

def _hk(r, *keys):
    return isinstance(r, dict) and all(k in r for k in keys)


def _su_bridge(env, app, mp):
    return {"rationale": "Entropy and surprise are the same quantity seen two ways."}

def _su_source_stub(env, app, mp):
    return {"title": "A Test Paper", "url": ""}

def _su_node_stub(env, app, mp):
    return {"knowledge_type": "concept", "title": "Test Concept", "suggest_sources": False}

def _su_hypothesis(env, app, mp):
    return {"title": "A Testable Hypothesis"}

def _su_edit(env, app, mp):
    return {"slug": "entropy", "section_updates": {"Definition": "Edited for the write contract."}}

def _su_add_conn(env, app, mp):
    return {"edges": [{"subject": "pkis:concept:entropy",
                       "target": "pkis:concept:bayesian-inference", "predicate": "uses"}]}

def _su_commit_staged(env, app, mp):
    # commit_staged_node git-adds index.md + log.md alongside the promoted node,
    # so they must exist in the fixture before the add.
    (env.wiki / "index.md").write_text("# Index\n")
    (env.wiki / "log.md").write_text("# Log\n")
    staged = app.tool_create_node_stub(knowledge_type="concept", title="Promote Me",
                                       suggest_sources=False)
    return {"staged_id": staged["staged_id"]}

def _su_rebuild(env, app, mp):
    (env.wiki / "source_graph.json").write_text(json.dumps({"meta": {"nodes": 0, "edges": 0}}))
    class _R:
        returncode, stderr, stdout = 0, "", ""
    mp.setattr(subprocess, "run", lambda *a, **k: _R())
    return {}

def _su_log_idea(env, app, mp):
    (env.repo / "docs").mkdir(parents=True, exist_ok=True)
    (env.repo / "docs" / "IDEAS.md").write_text("# Ideas\n\n---\n\n## existing\nbody\n")
    return {"title": "A logged idea", "idea": "Some idea body."}

def _su_set_priority(env, app, mp):
    mp.setattr(app, "PRIORITY_CONFIG_PATH", env.repo / ".priority_config.json")
    return {"reset": True}

def _su_save_url(env, app, mp):
    mp.setattr(app, "_fetch_url_metadata", lambda u: {"title": "Test Article", "author": "Jane Doe"})
    mp.setattr(app, "_maybe_autobuild_reader", lambda slug: None)
    return {"url": "https://example.com/some-post"}

def _su_upload_doc(env, app, mp):
    mp.setattr(app, "DOCS_DIR", env.repo / "docstore")
    mp.setattr(app, "_maybe_autobuild_reader", lambda slug: None)
    env.write_node("sources", "test-doc", id="pkis:source:test-doc", title="Test Doc")
    app._node_cache = {}
    return {"slug": "test-doc", "filename": "test-doc.pdf",
            "content_b64": base64.b64encode(b"%PDF-1.4 fake pdf bytes").decode()}

def _su_save_podcast(env, app, mp):
    mp.setattr(app, "RAW_DIR", env.repo / "raw")
    mp.setattr(app, "_fetch_podcast_page_metadata", lambda u: {"title": "Ep 1", "show": "Test Show", "description": "d"})
    mp.setattr(app, "_podcast_index_get_transcript", lambda **k: ([], {}))
    mp.setattr(app, "_apple_podcasts_get_transcript", lambda **k: ([], {}))
    mp.setattr(app, "_listen_notes_get_metadata", lambda *a, **k: {})
    mp.setattr(app, "_podchaser_get_metadata", lambda *a, **k: {})
    mp.setattr(app, "_maybe_autobuild_reader", lambda slug: None)
    return {"url": "https://example.com/podcast/ep1"}


WRITE_CONTRACT_CASES = [
    ("create_bridge_note", _su_bridge, lambda r: _hk(r, "staged_id")),
    ("create_source_stub", _su_source_stub, lambda r: _hk(r, "staged_id")),
    ("create_node_stub", _su_node_stub, lambda r: _hk(r, "staged_id", "iri")),
    ("create_hypothesis", _su_hypothesis, lambda r: _hk(r, "staged_id")),
    ("edit_node", _su_edit, lambda r: r.get("status") == "edited" and r.get("git_pushed") is True),
    ("add_connections", _su_add_conn, lambda r: _hk(r, "added") and r.get("git_pushed") is True),
    ("commit_staged_node", _su_commit_staged, lambda r: r.get("status") == "committed"),
    ("rebuild_source_graph", _su_rebuild, lambda r: _hk(r, "status")),
    ("log_idea", _su_log_idea, lambda r: _hk(r, "logged")),
    ("set_priority_config", _su_set_priority, lambda r: r.get("status") == "reset"),
    ("save_url_source", _su_save_url, lambda r: _hk(r, "slug", "type")),
    ("upload_document", _su_upload_doc, lambda r: r.get("slug") == "test-doc"),
    ("save_podcast_source", _su_save_podcast, lambda r: _hk(r, "slug") and r.get("transcript_queued") is True),
]


@pytest.mark.contract
@pytest.mark.parametrize("tool,setup,check", WRITE_CONTRACT_CASES, ids=[c[0] for c in WRITE_CONTRACT_CASES])
def test_write_tool_contract(appmod, isolated_wiki, monkeypatch, tool, setup, check):
    """Each advertised write tool: canonical input → documented response shape,
    against the isolated wiki/git fixture (called directly; auth is Seam E)."""
    kwargs = setup(isolated_wiki, appmod, monkeypatch)
    result = getattr(appmod, "tool_" + tool)(**kwargs)
    assert check(result), f"{tool} returned unexpected shape: {result!r}"
