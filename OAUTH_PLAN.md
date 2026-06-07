# OAuth for the PKIS MCP Server — Implementation Plan

> Status: **PLAN ONLY — not implemented.** This document scopes the work to
> replace the single shared `PKIS_MCP_WRITE_KEY` with real per-user
> authentication + authorization, so that the `https://pkis.dev/mcp` URL can be
> shared safely.
>
> Companion doc: [`MCP_ACCESS_GUIDE.md`](./MCP_ACCESS_GUIDE.md) — how users
> actually connect once this lands.

---

## 1. Why

The MCP URL has been shared with colleagues. Today, **write access is one static
shared secret** (`Authorization: Bearer <PKIS_MCP_WRITE_KEY>`, checked in
`app.py:is_write_authorized`, gate at `app.py:4916-4918`). That means:

- Anyone with the key can write; anyone who reads the key (it rides in
  `~/.claude.json` and, on mobile, would have to ride in the URL) has full write.
- No identity, no per-user revocation, no audit of *who* wrote.
- Mobile (claude.ai connectors) **can't send a custom header at all** — its
  connector flow only speaks OAuth. So today mobile is read-only by construction.

OAuth fixes all of these at once: claude.ai's connector is *built* to do the
OAuth handshake, identity comes from a real login, and we gate writes on a
per-user allowlist.

---

## 2. How MCP OAuth actually works (the handshake claude.ai performs)

This is the flow we must support. Numbers map to the MCP Authorization spec
(rev. 2025-06-18), which builds on OAuth 2.1.

```
claude.ai (client)                    pkis.dev (our server = Resource Server)        Authorization Server
   |                                       |                                              |
   |  1. POST /mcp  (no token)             |                                              |
   |-------------------------------------->|                                              |
   |  401 + WWW-Authenticate:              |                                              |
   |     resource_metadata=".../.well-known/oauth-protected-resource"                     |
   |<--------------------------------------|                                              |
   |  2. GET /.well-known/oauth-protected-resource                                        |
   |-------------------------------------->|  { resource, authorization_servers:[AS] }    |
   |<--------------------------------------|                                              |
   |  3. GET <AS>/.well-known/oauth-authorization-server ------------------------------->|
   |<------------------------------------------------ endpoints + jwks_uri --------------|
   |  4. POST <AS>/register  (Dynamic Client Registration, RFC 7591) ------------------->|
   |<------------------------------------------------ client_id -------------------------|
   |  5. GET <AS>/authorize  (PKCE S256) -> user LOGS IN + CONSENTS --------------------->|
   |<------------------------------------------------ redirect w/ auth code -------------|
   |  6. POST <AS>/token  (code + verifier) -------------------------------------------->|
   |<------------------------------------------------ access_token (JWT) + refresh ------|
   |  7. POST /mcp  Authorization: Bearer <JWT>                                           |
   |-------------------------------------->|  validate JWT (sig/iss/aud/exp/scope)        |
   |  result                               |  email -> role -> allowed tool set           |
   |<--------------------------------------|                                              |
```

The relevant RFCs (you don't implement them all — the IdP does most): OAuth 2.1,
RFC 9728 (Protected Resource Metadata), RFC 8414 (AS Metadata), RFC 7591
(Dynamic Client Registration), RFC 7636 (PKCE), RFC 8707 (Resource Indicators).

**The pivotal question** is *who plays the Authorization Server* in steps 3–6.
That's the architecture decision below, and it's where 80% of the effort
difference lives.

---

## 3. Architecture decision: delegate the AS, don't build one

| | **A. Delegate to a managed IdP** (recommended) | **B. Self-host the AS in Flask** |
|---|---|---|
| Who runs authorize/token/register/consent | The IdP (Stytch / WorkOS / Auth0 / Descope / Scalekit — any with **DCR** support) | You, in `app.py` |
| Who stores clients/codes/tokens | The IdP | You — and it must be a **shared store** (SQLite), because gunicorn workers don't share memory |
| Who handles the human login | The IdP (Google social login or email OTP — colleagues already have Google) | You build it (magic-link or Google sign-in or passwords) |
| Crypto you own | JWT **verification** only (well-trodden, low-risk) | JWT **signing + key rotation + JWKS**, PKCE, refresh rotation (security-critical) |
| New code in `app.py` | ~150–250 lines (token validation + metadata + authz) | ~600–1000 lines + a consent UI + SQLite schema |
| New dependency | `PyJWT[crypto]` (or `authlib`) | `authlib` (AS server pieces) + a DB |
| Ongoing burden | IdP patches the scary parts | You are now running a security-critical auth server |
| Effort | **~1–2 focused days** | **~4–7 focused days** + maintenance |
| Cost | Free tier covers a handful of users on every major IdP | $0 software, but your time |

**Recommendation: Architecture A.** You are a solo maintainer with a few
colleague users. Self-hosting an OAuth Authorization Server means owning token
signing, key rotation, a consent screen, refresh-token rotation, and a
cross-worker token database — all security-critical, all to let yourself and
three colleagues write notes from a phone. Delegating leaves your server
**stateless** (it only *verifies* tokens), which sidesteps the gunicorn
shared-state problem entirely.

The rest of this plan assumes **A**. Section 9 keeps B documented as the fallback.

### Picking an IdP

Hard requirement: the IdP must support **Dynamic Client Registration** (RFC
7591), because claude.ai registers itself dynamically (step 4) — you can't
pre-create a client for it. IdPs that advertise MCP/DCR support and have usable
free tiers: **Stytch**, **WorkOS AuthKit**, **Auth0** (DCR is a toggle),
**Descope**, **Scalekit**. Decision deferred to implementation; criteria:

1. DCR on the free tier (non-negotiable).
2. Google social login + email OTP (so colleagues need no new account).
3. Lets you set the token **audience** to `https://pkis.dev/mcp` (RFC 8707) so a
   token minted for some *other* app can't be replayed against us.
4. Exposes a JWKS URL for stateless signature verification.

> **Open question to resolve in Phase 0:** confirm the chosen IdP issues
> JWT (not opaque) access tokens with an `email` (or equivalent) claim. If it
> only issues opaque tokens, we add a token-introspection call (RFC 7662)
> instead of local JWT verification — a small change, but worth knowing up front.

### Cost (spoiler: ~$0 at this scale)

The recurring bill for the managed-IdP path is **almost certainly $0/month**.
A handful of users is orders of magnitude under every free tier. The "cost" is
only that these IdPs *have* paid tiers — not that you'd reach them.

Free-tier ceilings (monthly active users), as of Jan 2026 — **verify before
committing; auth pricing churns:**

| IdP | Free tier (MAU) | Notes |
|---|---|---|
| **WorkOS AuthKit** | ~1,000,000 | Effectively free forever at this scale |
| **Clerk** | ~10,000 | |
| **Stytch** | ~10,000 (B2C) / ~1,000 orgs (B2B) | Explicit MCP-auth support |
| **Descope** | ~7,500 | |
| **Auth0** | ~7,500 | Free tier changes most often; watch DCR availability |

**The real pricing question is not user count — it's whether _Dynamic Client
Registration_ is free.** claude.ai *requires* DCR (it can't use a pre-created
client). A couple of IdPs keep advanced OAuth features (DCR, custom domains,
token customization) on paid plans even when MAU is free. If DCR is gated, that
IdP's free tier doesn't help us — so confirming "DCR on the free tier" is a
Phase-0 gate, not an afterthought.

Other cost notes:
- **No new infrastructure** — OAuth adds no servers; we already run pkis.dev.
- **Self-hosting the AS (Architecture B) is also $0 in software** — its cost is
  entirely the 4–7 days of build + indefinite maintenance. That's the whole
  reason the managed path wins: same $0, minus the days.
- **Growth** only matters if PKIS ever serves thousands of MAU; even then WorkOS
  stays free to ~1M.

> ⚠️ **Prerequisite discovered in research:** claude.ai **custom connectors
> require a paid Claude plan** (Pro / Max / Team / Enterprise). Free Claude
> accounts can't add custom connectors at all. Confirm the account doing the
> connecting is on a paid plan before any of this matters.

### IdP comparison — Phase 0 research (2026-06-05)

Researched DCR-on-free-tier, token format, audience binding, MCP support, and
claude.ai compatibility across the candidates. Hard requirement = **DCR on the
free tier** (claude.ai registers itself dynamically; we can't pre-create a client).

| IdP | DCR on free tier? | JWT + email? | Audience binding | Free MAU | claude.ai-proven? |
|---|---|---|---|---|---|
| **WorkOS (AuthKit)** | Yes (dashboard toggle)¹ | JWT via JWKS; email-in-token TBV | **Explicit** (`aud` = requested `resource`) | **1,000,000** | Partial — 1 community token-exchange report to re-test |
| **Stytch** | Yes (opt-in toggle) | JWT; email-in-token TBV | Implied (introspection) | 10,000 | **Yes** — docs name Claude connectors directly |
| **Descope** | **Yes — confirmed Free Forever** | Not documented (TBV) | Not documented (TBV) | 7,500 | Lists Claude as example; no e2e proof |
| **Clerk** | Yes (toggle) | JWT-native; email TBV | TBV | ~10,000 | Not specifically confirmed |
| **Scalekit** | Yes (toggle) | TBV | **Explicit** (resource validation) | 5,000 tool-calls/mo + 25 accts² | Desktop/Cursor/VS Code; no claude.ai-web |
| **Auth0** | **UNCONFIRMED** (off by default; Enterprise-marketed) | JWT *only if* default audience set, else **opaque** | Yes, with config | 25,000 | Friction (opaque-by-default footgun) |

¹ Not gated on the pricing page, but the "not gated" claim isn't stated verbatim — confirm the toggle exists on a fresh free account.
² Scalekit's free tier is metered by tool-calls/connected-accounts, not MAU — a tighter, different failure mode for an MCP server.
TBV = to-be-verified in-console (token format / email claim / audience couldn't be confirmed from docs alone).

**Recommendation: WorkOS (AuthKit), with Stytch as the close runner-up.**
- **WorkOS** — DCR is a toggle, free to **1M MAU** (you'll use ~5), and it's the
  only one with a written guarantee that the token `aud` equals the requested
  `resource` (RFC 8707) over JWKS-verifiable JWTs. One community report of a
  claude.ai-side `/token` hiccup — re-test the full handshake in Phase 0.
- **Stytch** — the most explicit *claude.ai/Claude* MCP positioning (docs name
  Claude connectors; DCR a documented opt-in), free to 10k MAU. Pick this if the
  WorkOS handshake misbehaves.
- **Avoid Auth0** for this: DCR-on-free-tier is unconfirmed and it issues opaque
  tokens by default — the worst fit for a stateless verify-only server.

**Two facts to verify in-console before committing (true for all candidates):**
the access token is a **JWT (not opaque)** and **carries `email` in the access
token** (not only the ID token / userinfo). Mint a real token and inspect it —
this is the single most important Phase 0 check after confirming DCR.

---

## 4. Target design (Architecture A)

Our server stays a **Resource Server**. Three additions:

1. **Protected Resource Metadata endpoint** — `GET /.well-known/oauth-protected-resource`
   returns a tiny static JSON pointing at the IdP:
   ```json
   {
     "resource": "https://pkis.dev/mcp",
     "authorization_servers": ["https://<your-idp-issuer>"],
     "bearer_methods_supported": ["header"]
   }
   ```

2. **401 challenge** — when `/mcp` is called for a write tool without a valid
   token, respond `401` with:
   ```
   WWW-Authenticate: Bearer resource_metadata="https://pkis.dev/.well-known/oauth-protected-resource"
   ```
   (This is the trigger that makes claude.ai start the flow. Getting the header
   byte-exact matters — a malformed challenge means the connector silently stays
   unauthenticated.)

3. **Token validation + authorization** — a helper that replaces/extends
   `is_write_authorized`:
   ```python
   # sketch — not final
   def authorize_request(req, required: str) -> Identity:
       token = bearer(req)
       # legacy/service path stays for machine-to-machine (see §6)
       if token == WRITE_KEY:        return Identity(email="service", role="writer")
       if token == TRUSTED_TOKEN:    return Identity(email="owner",   role="owner")
       claims = verify_jwt(token)    # PyJWT + cached JWKS; checks sig/iss/aud/exp
       role = ROLE_FOR.get(claims["email"], "reader")  # allowlist file
       return Identity(email=claims["email"], role=role)
   ```
   `verify_jwt` fetches the IdP's JWKS once and caches it (per-worker, TTL'd — no
   shared store needed; this is the payoff of going stateless).

### Authorization model

Reuse the existing three-tier tool split (`read_tools` / `write_tools` /
`trusted_tools` in `dispatch_tool`, `app.py:4746-4919`). Map roles → tiers:

| Role | Source of truth | Read tools | Write tools | Trusted tools |
|---|---|---|---|---|
| `owner` (you) | allowlist / `TRUSTED_TOKEN` | ✅ | ✅ | ✅ |
| `writer` (colleagues you list) | allowlist file | ✅ | ✅ | ❌ |
| `reader` (authenticated, not listed) | default | ✅ | ❌ | ❌ |
| anonymous (no token) | default | ✅ | ❌ | ❌ |

Allowlist is a small JSON file following your existing config-file pattern
(`PKIS_ROLES_PATH`), e.g. `{ "choct155@gmail.com": "owner", "boss@…": "writer" }`.
Editing it + a refresh is how you grant/revoke — no redeploy.

> **Decision to confirm:** keep reads anonymous (current behavior — you shared
> the URL for reading) vs. require login for everything. Plan assumes reads stay
> open; flip one default if you want them gated.

---

## 5. Implementation phases & effort

Estimates are **focused engineering hours** for one person who knows this
codebase. Calendar time is longer (IdP signup, claude.ai round-trips).

| Phase | Work | Est. |
|---|---|---|
| **0. IdP selection & spike** | Create IdP account; enable DCR + Google/email login; confirm JWT access tokens with an email claim and settable audience; register a throwaway client and pull one token by hand. *De-risks everything below.* | **2–4 h** |
| **1. Protected Resource Metadata + 401 challenge** | Add `/.well-known/oauth-protected-resource` route; emit correct `WWW-Authenticate` on unauthorized writes. Verify with `curl`. | **2–3 h** |
| **2. Token validation** | Add `PyJWT[crypto]`; implement `verify_jwt` (JWKS fetch + cache + TTL, verify sig/iss/aud/exp); unit tests for valid / expired / wrong-aud / wrong-iss / bad-sig. | **4–6 h** |
| **3. Authz wiring** | `authorize_request` helper; role allowlist file + loader (config-file pattern); thread identity into `dispatch_tool`; map roles → read/write/trusted tiers; keep static-key fallback (§6). | **3–5 h** |
| **4. End-to-end with MCP Inspector** | Run `@modelcontextprotocol/inspector` against `pkis.dev/mcp`, complete the real OAuth flow, confirm read-as-reader / write-as-writer / 403-as-reader. | **2–4 h** |
| **5. claude.ai mobile + desktop** | Add the connector on the phone, log in, confirm a real bridge-note write. Confirm desktop Claude Code still writes via the legacy key. | **1–2 h** |
| **6. Deploy & docs** | nginx check that `/.well-known/*` reaches Flask; new env vars (`PKIS_OAUTH_ISSUER`, `PKIS_OAUTH_AUDIENCE`, `PKIS_ROLES_PATH`); `pip install` in the venv; restart; finalize `MCP_ACCESS_GUIDE.md`. | **2–3 h** |
| | **Total (Architecture A)** | **~16–27 h → 2–4 focused days** |

> Architecture **B** (self-hosted AS) replaces phases 1–3 with building DCR, an
> authorize+consent UI, token issuance, RSA signing + JWKS rotation, PKCE
> verification, refresh rotation, and a **SQLite store shared across gunicorn
> workers**. Realistic total **~4–7 days plus indefinite maintenance**. Not
> recommended.

---

## 6. Backward compatibility (don't break what works)

- **Desktop Claude Code is machine-to-machine** — it can't do an interactive
  browser login. Keep the static `PKIS_MCP_WRITE_KEY` / `PKIS_TRUSTED_TOKEN`
  Bearer path alive as a **service-account credential** (the first two lines of
  the `authorize_request` sketch). Your `~/.claude.json` setup keeps working
  unchanged. Document it clearly as the M2M escape hatch.
- This makes the rollout **additive and reversible**: OAuth is a new accepted
  credential type alongside the existing one. If anything misbehaves, the static
  key still writes while you debug.
- (Optional, later) migrate desktop to an OAuth **client-credentials** token to
  retire the static key entirely. Not needed for v1.

---

## 7. Testing plan

- **Unit** (Phase 2/3): token valid / expired / wrong audience / wrong issuer /
  tampered signature / missing email claim; role mapping incl. unknown-email →
  `reader`; static-key fallback still authorizes.
- **Integration** (Phase 4): full handshake via MCP Inspector (it implements the
  OAuth client side) — confirms our metadata + 401 challenge are spec-correct
  without burning claude.ai cycles.
- **Manual** (Phase 5): mobile connector add → Google login → read OK, write OK
  as writer, write 403 as reader; desktop regression.
- **Negative**: revoke a user in the allowlist → next write is 403 after refresh.

---

## 8. Deployment & rollback

- **Prereqs already met:** TLS at nginx (OAuth needs HTTPS ✅), public hostname ✅.
- **nginx:** confirm `location /.well-known/` proxies to Flask (not served as
  static / intercepted). One-line check during Phase 6.
- **New env** on the host service unit: `PKIS_OAUTH_ISSUER`,
  `PKIS_OAUTH_AUDIENCE` (= `https://pkis.dev/mcp`), `PKIS_ROLES_PATH`.
- **Dep:** `pip install "PyJWT[crypto]"` into `/home/pkis/venv`.
- **Ship:** scp `app.py` through the symlink, `sudo systemctl restart pkis-mcp.service`.
- **Rollback:** revert `app.py`, restart. Because the static key path is
  untouched, write access never depends on the new code being correct.

---

## 9. Risks & open questions

1. **DCR is mandatory** for claude.ai — verify on the IdP's *free* tier (Phase 0).
2. **Opaque vs JWT tokens** — if the IdP issues opaque tokens, swap local JWT
   verify for introspection (RFC 7662). Small, but confirm in Phase 0.
3. **Audience binding** — set the resource/audience so a token for another app
   can't be replayed against `pkis.dev/mcp` (RFC 8707).
4. **`WWW-Authenticate` exactness** — a malformed challenge = connector silently
   stays read-only. Test with Inspector before blaming claude.ai.
5. **Redirect URI allowlist** — the IdP must allow claude.ai's connector
   callback URL(s); capture them in Phase 0.
6. **JWKS caching across workers** — cache per-worker with a TTL; on key
   rotation, stale cache causes transient 401s until TTL expires. Keep TTL modest
   (e.g. 1 h) and re-fetch on unknown `kid`.
7. **Free-tier limits** — monthly active users / token volume; a handful of users
   is comfortably within every major IdP's free tier, but note the ceiling.

---

## 10. TL;DR for the "how much is this" question

- **Recommended path (delegate to a managed IdP): ~2–4 focused days**, mostly
  glue code (metadata endpoint, JWT verification, role allowlist) — your server
  stays stateless, which dodges the gunicorn shared-state problem.
- **Self-hosting the OAuth server: ~4–7 days + ongoing security maintenance.**
  Not worth it at this scale.
- **Nothing breaks meanwhile:** the change is additive; the existing static key
  remains a valid service credential for desktop Claude Code, so rollout and
  rollback are low-risk.
