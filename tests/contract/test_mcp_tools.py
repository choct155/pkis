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

import json

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
KNOWN_HIDDEN = {
    "build_reader", "check_alias_collision", "get_assets", "get_cluster_priorities",
    "get_clusters", "get_concept_operational_load", "get_dependency_chain",
    "get_index", "get_node_stub", "get_operational_references",
    "log_operation", "register_operational_reference", "resolve_or_detect",
    "search_wiki_index",
}


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
@pytest.mark.xfail(reason="D-2: mnemon trusted tier is to be advertised in Phase 3; "
                          "this guards that work and flips to pass once done.",
                   strict=True)
def test_mnemon_tools_should_be_advertised(appmod):
    """Decision D-2 keeps the mnemon trusted tier and promotes it to advertised.
    Until Phase 3 does that, this is an expected failure that documents the gap."""
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
    assert len(tools) == 28, "advertised tool count changed — update the contract baseline intentionally"
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


# ── Write-tool contracts: STILL STUBBED (next B1 increment; needs auth + mocks) ──

ADVERTISED_WRITE = [
    "create_bridge_note", "create_source_stub", "create_node_stub",
    "create_hypothesis", "edit_node", "add_connections", "commit_staged_node",
    "rebuild_source_graph", "log_idea", "set_priority_config",
    "upload_document", "save_url_source", "save_podcast_source",
]


@pytest.mark.contract
@pytest.mark.parametrize("tool", ADVERTISED_WRITE)
def test_write_tool_contract(client, isolated_wiki, tool):
    """STUB (B1 increment 2): with write auth granted and an isolated wiki, call
    `tool` with canonical input and assert the response shape. The 3 network write
    tools (save_url_source/upload_document/save_podcast_source) mock the boundary."""
    pytest.skip("B1 increment 2 — write-tool contracts pending")
