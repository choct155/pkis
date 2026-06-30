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


# --------------------------------------------------------------------------- #
# Native-app bearer tokens (Capacitor APK). Fully hermetic: the token store is
# PKIS-owned (no WorkOS/JWT), so tests mint tokens directly and assert the gates.
# --------------------------------------------------------------------------- #

@pytest.fixture()
def native_env(appmod, monkeypatch, tmp_path):
    """Enable native auth against a throwaway token DB, with a fixed role allowlist."""
    monkeypatch.setattr(appmod, "NATIVE_AUTH_ENABLED", True)
    monkeypatch.setattr(appmod, "NATIVE_TOKEN_DB", tmp_path / "native_tokens.sqlite")
    monkeypatch.setattr(appmod, "_load_roles",
                        lambda: {"owner@x.io": "owner", "writer@x.io": "writer"})
    return appmod


def _mint(appmod, email):
    """Mint an access+refresh pair for `email` directly (bypasses the WorkOS hop)."""
    conn = appmod._native_db()
    try:
        access, refresh, _ = appmod._native_mint(conn, email)
        conn.commit()
        return access, refresh
    finally:
        conn.close()


@pytest.mark.integration
def test_native_pkce_roundtrip_mints_usable_token(native_env):
    """register challenge → consume → issue code → redeem w/ verifier → usable token.
    The one-time code cannot be redeemed twice."""
    appmod = native_env
    verifier = "a-sufficiently-long-pkce-code-verifier-1234567890"
    challenge = appmod._pkce_challenge(verifier)
    nonce = appmod._native_register_challenge(challenge)
    assert appmod._native_consume_challenge(nonce) == challenge
    code = appmod._native_issue_code("owner@x.io", challenge)
    out = appmod._native_redeem_code(code, verifier)
    assert out is not None
    access, _refresh, _exp = out
    assert appmod._native_resolve(access) == "owner@x.io"
    assert appmod._native_redeem_code(code, verifier) is None  # one-time


@pytest.mark.integration
def test_native_pkce_mismatch_rejected(native_env):
    """A code redeemed with the wrong PKCE verifier fails closed."""
    appmod = native_env
    code = appmod._native_issue_code("owner@x.io", appmod._pkce_challenge("right-verifier-aaaaaaaaaa"))
    assert appmod._native_redeem_code(code, "wrong-verifier-bbbbbbbbbb") is None


@pytest.mark.integration
def test_native_consume_challenge_is_one_time(native_env):
    appmod = native_env
    nonce = appmod._native_register_challenge("chal")
    assert appmod._native_consume_challenge(nonce) == "chal"
    assert appmod._native_consume_challenge(nonce) is None


@pytest.mark.integration
def test_native_token_gates_honor_role(native_env):
    """Native owner/writer/reader map onto the same gates as web identities — and a
    native owner is NOT in the trusted (M2M) tier (mirrors web_identity)."""
    from flask import request as req
    appmod = native_env
    owner_access, _ = _mint(appmod, "owner@x.io")
    writer_access, _ = _mint(appmod, "writer@x.io")
    reader_access, _ = _mint(appmod, "nobody@x.io")  # absent from allowlist → reader

    def ctx(tok):
        return appmod.app.test_request_context(headers={"Authorization": f"Bearer {tok}"})

    with ctx(owner_access):
        assert appmod.is_write_authorized(req) is True
        assert appmod.is_owner(req) is True
        assert appmod.is_trusted(req) is False
    with ctx(writer_access):
        assert appmod.is_write_authorized(req) is True
        assert appmod.is_owner(req) is False
    with ctx(reader_access):
        assert appmod.is_write_authorized(req) is False
        assert appmod.is_owner(req) is False
    with ctx("garbage-not-a-token"):
        assert appmod.native_identity(req) is None


@pytest.mark.integration
def test_native_token_revoked_and_expired_rejected(native_env, monkeypatch):
    appmod = native_env
    access, _ = _mint(appmod, "owner@x.io")
    assert appmod._native_resolve(access) == "owner@x.io"
    appmod._native_revoke(access)
    assert appmod._native_resolve(access) is None
    # already-expired at mint time
    monkeypatch.setattr(appmod, "NATIVE_ACCESS_TTL", -1)
    stale, _ = _mint(appmod, "owner@x.io")
    assert appmod._native_resolve(stale) is None


@pytest.mark.integration
def test_native_refresh_rotates_and_revokes_old(native_env):
    appmod = native_env
    _access, refresh = _mint(appmod, "owner@x.io")
    out = appmod._native_rotate(refresh)
    assert out is not None
    new_access, new_refresh, _ = out
    assert appmod._native_resolve(new_access) == "owner@x.io"
    assert new_refresh != refresh
    assert appmod._native_rotate(refresh) is None  # old refresh now revoked


@pytest.mark.integration
def test_native_identity_dormant_when_disabled(native_env, monkeypatch):
    """With a valid token minted, flipping NATIVE_AUTH_ENABLED off makes the bearer
    inert — a misconfig can't silently keep the gate open."""
    from flask import request as req
    appmod = native_env
    access, _ = _mint(appmod, "owner@x.io")
    monkeypatch.setattr(appmod, "NATIVE_AUTH_ENABLED", False)
    with appmod.app.test_request_context(headers={"Authorization": f"Bearer {access}"}):
        assert appmod.native_identity(req) is None


@pytest.mark.integration
def test_native_token_endpoint_happy_path_and_me(native_env, client):
    """The /auth/native/token route redeems a code, and /auth/me reflects the bearer."""
    appmod = native_env
    verifier = "another-long-pkce-verifier-09876543210"
    code = appmod._native_issue_code("owner@x.io", appmod._pkce_challenge(verifier))
    r = client.post("/pkis-api/auth/native/token", json={"code": code, "verifier": verifier})
    assert r.status_code == 200
    tok = r.get_json()["access_token"]
    me = client.get("/pkis-api/auth/me", headers={"Authorization": f"Bearer {tok}"}).get_json()
    assert me["authenticated"] is True and me["role"] == "owner"


@pytest.mark.integration
def test_native_token_endpoint_rejects_bad_code(native_env, client):
    r = client.post("/pkis-api/auth/native/token", json={"code": "nope", "verifier": "nope"})
    assert r.status_code == 401
