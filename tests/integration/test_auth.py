"""
Seam E — auth gating (ARCHITECTURE_AUDIT.md §7 Seam E).

Contract: a bad/absent credential yields a well-formed JSON-RPC error (403 tier),
never a silent success and never a 500. OAuth/WorkOS are DORMANT in the test env
(conftest unsets their config), so these exercise the static-key path and the
dormant fallback.
"""

import pytest

WRITE_CALL = {
    "jsonrpc": "2.0", "id": 1, "method": "tools/call",
    "params": {"name": "create_bridge_note", "arguments": {"rationale": "x"}},
}


@pytest.mark.integration
def test_write_tool_rejected_without_credentials(client):
    """No credential + a write tool → well-formed JSON-RPC error, tool not run."""
    body = client.post("/mcp", json=WRITE_CALL).get_json()
    assert body.get("result") is None
    assert body.get("error", {}).get("code") == -32001


@pytest.mark.integration
def test_bad_bearer_token_is_well_formed_error(client):
    """A garbage Bearer token must fail closed with a clean 401/403 — never a 500
    or a hang (the auth path must not leak an exception)."""
    r = client.post("/mcp", headers={"Authorization": "Bearer garbage-not-a-token"}, json=WRITE_CALL)
    assert r.status_code in (401, 403)
    body = r.get_json()
    assert body.get("error", {}).get("code") == -32001
    assert body.get("result") is None


@pytest.mark.integration
def test_static_write_key_authorizes(appmod, isolated_wiki, monkeypatch, client):
    """With PKIS_MCP_WRITE_KEY set and presented as a Bearer token, a write tool
    runs (the machine-to-machine escape hatch for desktop Claude Code)."""
    monkeypatch.setattr(appmod, "WRITE_KEY", "secret-test-key")
    body = client.post("/mcp", headers={"Authorization": "Bearer secret-test-key"},
                       json=WRITE_CALL).get_json()
    assert body.get("error") is None
    assert "result" in body


@pytest.mark.integration
def test_oauth_dormant_static_key_only_matrix(appmod, monkeypatch):
    """OAuth dormant → is_write_authorized depends solely on the static key. Confirm
    the matrix so a misconfiguration can't silently open or close the gate."""
    from flask import request as req
    assert appmod.OAUTH_ENABLED is False
    monkeypatch.setattr(appmod, "WRITE_KEY", "k")
    with appmod.app.test_request_context(headers={"Authorization": "Bearer k"}):
        assert appmod.is_write_authorized(req) is True
    with appmod.app.test_request_context(headers={"Authorization": "Bearer wrong"}):
        assert appmod.is_write_authorized(req) is False
    with appmod.app.test_request_context():
        assert appmod.is_write_authorized(req) is False
