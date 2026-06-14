"""
Seam E — auth gating (ARCHITECTURE_AUDIT.md §7 Seam E).

Three credential sources (static key, OAuth JWT, WorkOS web session) collapse into
two tiers (trusted, write). The contract that must never break: a bad/absent
credential yields a well-formed 401/403 — never a silent success, never a hang.
The OAuth/WorkOS paths are DORMANT unless env is set; the default suite runs in
that dormant state (conftest unsets the relevant vars).

One implemented guard (static-key gate works in the dormant default state); the
OAuth/web-session paths are stubs requiring a mocked IdP.
"""

import pytest


@pytest.mark.integration
def test_write_tool_rejected_without_credentials(client):
    """STUB: with no auth configured and no credential presented, a write tool
    over /mcp must return a well-formed JSON-RPC error (403 PermissionError tier),
    not execute. Assert the error envelope + that no node was written."""
    pytest.skip("Phase-2 stub — assert write-tier dispatch raises gate_error → JSON-RPC -32001")


@pytest.mark.integration
def test_static_write_key_authorizes(appmod, monkeypatch, client):
    """STUB: with PKIS_MCP_WRITE_KEY set and presented as a Bearer token, a write
    tool is authorized (the machine-to-machine escape hatch for desktop Claude
    Code). Monkeypatch appmod.WRITE_KEY, send Authorization: Bearer <key>."""
    pytest.skip("Phase-2 stub — assert is_write_authorized True path end-to-end")


@pytest.mark.integration
def test_bad_bearer_token_is_well_formed_error(client):
    """STUB: a malformed/garbage Bearer token must produce a clean 401/403, never
    a 500 or a hang (the JWKS path must fail closed)."""
    pytest.skip("Phase-2 stub — assert garbage token → well-formed rejection, no traceback")


@pytest.mark.integration
def test_oauth_dormant_falls_back_to_static_key(appmod):
    """STUB: with no OAuth env, OAUTH_ENABLED is False and is_write_authorized
    depends solely on the static key — confirm the dormant fallback, so a
    misconfiguration can't silently open or close the gate."""
    assert appmod.OAUTH_ENABLED is False  # dormant in the default test env
    pytest.skip("Phase-2 stub — extend with explicit static-key-only authorization matrix")
