"""
Seam B — REST /pkis-api/* ↔ the same tool_* functions (ARCHITECTURE_AUDIT.md §7 Seam B).

The viewer REST API is a SECOND copy of the call surface, gated by a different
mechanism (@require_write decorator) than the MCP path (in-dispatch
is_write_authorized). The risk is drift: a write route added without the
decorator, or REST/MCP diverging in argument defaults. These tests freeze the
auth-coverage invariant statically (no server needed) and stub the behavioral
parity check.
"""

import json
import re

import pytest


def _route_table(appmod):
    """Parse app.py into {func_name: {"routes": [...], "methods": set, "require_write": bool}}
    by walking decorator stacks above each `def`."""
    src = open(appmod.__file__).read().splitlines()
    table, pending_routes, pending_methods, has_rw = {}, [], set(), False
    for line in src:
        m = re.match(r'@app\.route\("([^"]+)"(?:,\s*methods=\[([^\]]*)\])?\)', line.strip())
        if m:
            pending_routes.append(m.group(1))
            if m.group(2):
                pending_methods |= set(re.findall(r'"(\w+)"', m.group(2)))
            continue
        if line.strip() == "@require_write":
            has_rw = True
            continue
        d = re.match(r'def (\w+)\(', line)
        if d and pending_routes:
            table[d.group(1)] = {
                "routes": pending_routes, "methods": pending_methods or {"GET"},
                "require_write": has_rw,
            }
            pending_routes, pending_methods, has_rw = [], set(), False
        elif d:
            pending_routes, pending_methods, has_rw = [], set(), False
    return table


# Write-bearing REST routes per the Phase-1 audit (§7 Seam B). Every one of these
# MUST carry @require_write, or an unauthenticated caller could mutate the wiki.
EXPECTED_WRITE_ROUTES = {
    "/pkis-api/reader-build", "/pkis-api/reader-annotate", "/pkis-api/staged/commit",
    "/pkis-api/bridge-note", "/pkis-api/source-stub", "/pkis-api/queue/add",
    "/pkis-api/discovery/act", "/pkis-api/upload-document", "/pkis-api/save-url",
    "/pkis-api/rebuild-graph",
}

# Read routes that must stay open (no write gate) — a regression to gated here
# would break anonymous reads from the claude.ai connector / public viewer.
EXPECTED_OPEN_READ_ROUTES = {
    "/pkis-api/search", "/pkis-api/node", "/pkis-api/related", "/pkis-api/health",
    "/pkis-api/frontier", "/pkis-api/clusters", "/pkis-api/index", "/pkis-api/domains",
}


@pytest.mark.contract
def test_all_expected_write_routes_are_gated(appmod):
    table = _route_table(appmod)
    gated = {r for info in table.values() if info["require_write"] for r in info["routes"]}
    missing = EXPECTED_WRITE_ROUTES - gated
    assert not missing, f"write routes missing @require_write (unauthenticated mutation risk): {sorted(missing)}"


@pytest.mark.contract
def test_no_unexpected_write_gate_on_reads(appmod):
    table = _route_table(appmod)
    gated = {r for info in table.values() if info["require_write"] for r in info["routes"]}
    wrongly_gated = EXPECTED_OPEN_READ_ROUTES & gated
    assert not wrongly_gated, f"read routes wrongly write-gated (breaks anon reads): {sorted(wrongly_gated)}"


@pytest.mark.contract
def test_write_gate_inventory_is_frozen(appmod):
    """The full set of write-gated routes must match expectation — catches a NEW
    gated route nobody told us about (could be intended; force a conscious update)."""
    table = _route_table(appmod)
    gated = {r for info in table.values() if info["require_write"]
             for r in info["routes"] if r.startswith("/pkis-api/")}
    assert gated == EXPECTED_WRITE_ROUTES, (
        f"write-gate inventory drift.\n  new: {sorted(gated - EXPECTED_WRITE_ROUTES)}"
        f"\n  removed: {sorted(EXPECTED_WRITE_ROUTES - gated)}"
    )


def _shape(v):
    """Structural fingerprint: type + (for dicts) sorted keys + (for lists) the
    shape of the first element. Enough to catch REST/MCP surface divergence
    without asserting exact values."""
    if isinstance(v, list):
        return ("list", _shape(v[0]) if v else None)
    if isinstance(v, dict):
        return ("dict", tuple(sorted(v.keys())))
    return type(v).__name__


@pytest.mark.contract
@pytest.mark.parametrize("rest_path,mcp_tool,payload,mcp_extract", [
    ("/pkis-api/search", "search_wiki", {"query": "entropy"}, lambda m: m),
    ("/pkis-api/node", "get_node", {"iri": "pkis:concept:entropy"}, lambda m: m),
    ("/pkis-api/related", "get_related", {"iri": "pkis:concept:entropy"}, lambda m: m),
    # frontier: the REST route INTENTIONALLY unwraps to just the results list
    # (params are MCP-only — app.py:5839). Encode that asymmetry explicitly so the
    # guard still catches *unintended* drift while allowing the documented one.
    ("/pkis-api/frontier", "get_concept_frontier", {}, lambda m: m["results"]),
])
def test_rest_and_mcp_return_same_shape(client, rest_path, mcp_tool, payload, mcp_extract):
    """REST routes and their MCP twins call the same tool_* function. For most the
    response is identical; where a REST route deliberately reshapes for the viewer,
    the extractor encodes that documented relationship so the guard still catches
    unintended divergence."""
    rest = client.post(rest_path, json=payload).get_json()
    mcp_raw = client.post("/mcp", json={
        "jsonrpc": "2.0", "id": 1, "method": "tools/call",
        "params": {"name": mcp_tool, "arguments": payload},
    }).get_json()
    mcp = mcp_extract(json.loads(mcp_raw["result"]["content"][0]["text"]))
    assert _shape(rest) == _shape(mcp), f"{rest_path} vs {mcp_tool}: {_shape(rest)} != {_shape(mcp)}"


@pytest.mark.contract
def test_app_bare_redirects_to_trailing_slash(client):
    """/app (no slash) must 301 to /app/ — nginx only serves the /app/ alias, so a
    bare /app would otherwise fall through to a Flask 404."""
    r = client.get("/app")
    assert r.status_code == 301
    assert r.headers["Location"].endswith("/app/")


@pytest.mark.contract
def test_resolve_slug_to_iri(client):
    """/pkis-api/resolve turns a bare slug (from a body [[wikilink]]) into its IRI,
    and returns iri=None for a dangling link."""
    r = client.post("/pkis-api/resolve", json={"slug": "entropy"}).get_json()
    assert r["iri"] == "pkis:concept:entropy"
    miss = client.post("/pkis-api/resolve", json={"slug": "no-such-node-xyz"}).get_json()
    assert miss["iri"] is None
    # Batch form: a map of slug -> iri|null (used to dim dangling wikilinks).
    batch = client.post("/pkis-api/resolve",
                        json={"slugs": ["entropy", "no-such-node-xyz"]}).get_json()
    assert batch["map"] == {"entropy": "pkis:concept:entropy", "no-such-node-xyz": None}


@pytest.mark.contract
def test_source_status(client):
    """/pkis-api/source-status reports readability so the viewer can offer a 'read'
    affordance and dim un-ingested sources. The fixture source mackay-itila has a
    source_url; a dangling slug resolves to iri=None / not readable."""
    r = client.post("/pkis-api/source-status",
                    json={"slugs": ["mackay-itila", "no-such-source"]}).get_json()["map"]
    assert r["mackay-itila"]["iri"] == "pkis:source:mackay-itila"
    assert r["no-such-source"] == {"iri": None, "readable": False, "read_url": None, "has_reader": False}
