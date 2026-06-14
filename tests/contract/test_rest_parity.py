"""
Seam B — REST /pkis-api/* ↔ the same tool_* functions (ARCHITECTURE_AUDIT.md §7 Seam B).

The viewer REST API is a SECOND copy of the call surface, gated by a different
mechanism (@require_write decorator) than the MCP path (in-dispatch
is_write_authorized). The risk is drift: a write route added without the
decorator, or REST/MCP diverging in argument defaults. These tests freeze the
auth-coverage invariant statically (no server needed) and stub the behavioral
parity check.
"""

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


@pytest.mark.contract
@pytest.mark.parametrize("rest_path,mcp_tool", [
    ("/pkis-api/search", "search_wiki"),
    ("/pkis-api/node", "get_node"),
    ("/pkis-api/related", "get_related"),
    ("/pkis-api/frontier", "get_concept_frontier"),
])
def test_rest_and_mcp_return_same_shape(client, rest_path, mcp_tool):
    """STUB: for a logically identical call, the REST route and the MCP tool must
    return the same result shape (they call the same tool_* function; this guards
    against the two surfaces diverging in argument handling or wrapping)."""
    pytest.skip("Phase-2 stub — implement REST vs MCP shape-equality assertions")
