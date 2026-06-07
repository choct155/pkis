# PKIS MCP — Access & Connection Guide

How to connect to the PKIS knowledge wiki from Claude, what you can do once
connected, and how access is controlled.

> **Server:** `https://pkis.dev/mcp` (Streamable HTTP MCP transport)
> **Reads are open. Writes require authorization.**
>
> This guide documents both the **current** auth model and the **planned** OAuth
> model. The OAuth section is marked PLANNED until [`OAUTH_PLAN.md`](./OAUTH_PLAN.md)
> is implemented.

---

## 1. What the server exposes

The wiki is a set of MCP tools, split into three access tiers:

| Tier | Examples | Who can call them |
|---|---|---|
| **Read** | `search_wiki`, `get_node`, `get_related`, `get_concept_frontier`, `get_reading_queue`, `get_health_metrics`, `list_documents` | Anyone connected |
| **Write** | `create_bridge_note`, `create_node_stub`, `create_source_stub`, `edit_node`, `commit_staged_node`, `add_to_queue`, `save_url_source`, `upload_document` | Authorized writers only |
| **Trusted** (owner) | `register_operational_reference`, server-management tools | Owner only |

If you call a write tool without authorization you get:
`-32001 / "Tool '<name>' requires write authorization key"`.

---

## 2. Connecting

### A. Claude Code (desktop) — works today

Claude Code reads MCP servers from `~/.claude.json`. The PKIS server is
configured per-project with a static Bearer token (this is the **service /
machine-to-machine** credential and is intentionally kept even after OAuth
lands — see the plan):

```jsonc
// ~/.claude.json  →  projects → <pkis project path> → mcpServers
"pkis-wiki": {
  "type": "http",
  "url": "https://pkis.dev/mcp",
  "headers": { "Authorization": "Bearer <PKIS_MCP_WRITE_KEY>" }
}
```

- **Reads** work with or without the header.
- **Writes** work because the header matches the server's `PKIS_MCP_WRITE_KEY`.
- To get the key, ask the owner. Treat it like a password — it is, today, the
  whole of write access.

### B. claude.ai (mobile app / web) — read today, write after OAuth

In the Claude app, add a **custom connector**:

1. Settings → **Connectors** → **Add custom connector**
2. Name: `pkis-wiki`
3. URL: `https://pkis.dev/mcp`
4. Save, then enable it in a chat's tools.

Add the bare URL `https://pkis.dev/mcp`. This works for **reads** on mobile and
is safe to share with colleagues — it carries no secret and write tools stay
gated.

**Mobile writes are not possible without OAuth.** The claude.ai connector UI has
no custom-header field, so the `Authorization: Bearer` token that Claude Code
uses can't be supplied. We tried carrying the write key in the connector URL —
both as a query string (`?wk=<key>`) and as a path segment (`/mcp/<key>`) — and
**both fail**: claude.ai rebuilds the endpoint URL internally and will not carry
an ad-hoc credential, so the session dies ("Session terminated") on any tool
call. The bare URL (no credential) is the only form claude.ai accepts. Therefore
authenticated mobile writes require the real OAuth flow — see
[`OAUTH_PLAN.md`](./OAUTH_PLAN.md).

> **Tested & rejected (2026-06-05):** `?wk=` and `/mcp/<key>` URL-embedded
> credentials. The server itself speaks the MCP protocol correctly over the bare
> URL; the blocker is purely claude.ai's refusal to carry credentials in a custom
> connector URL. Do not re-attempt the URL-credential shortcut.

### C. Other MCP clients

Any Streamable-HTTP MCP client works for reads by pointing at
`https://pkis.dev/mcp`. For writes it must send either the static Bearer token
(if you have it) or, post-OAuth, a valid OAuth access token.

---

## 3. Write access after OAuth (PLANNED)

Once [`OAUTH_PLAN.md`](./OAUTH_PLAN.md) is implemented, connecting from claude.ai
(mobile or web) will be:

1. Add the connector exactly as in §2B.
2. On first use, Claude opens a **login** page (Google sign-in or email code).
3. Approve the consent screen.
4. You're connected **as yourself**. What you can do depends on your role:

| Your role | Reads | Writes | Notes |
|---|---|---|---|
| **Owner** | ✅ | ✅ + owner tools | The maintainer (`choct155@gmail.com`) |
| **Writer** | ✅ | ✅ | Colleagues on the allowlist |
| **Reader** | ✅ | ❌ | Signed in but not on the allowlist |
| **Anonymous** | ✅ | ❌ | Connected without signing in |

No tokens to copy, no headers to set — the login *is* the access. Write access
is granted by the owner adding your email to the allowlist; revoking is removing
it. The desktop Claude Code static-key path (§2A) keeps working unchanged.

---

## 4. Roles & how to get write access

- **Reading:** nothing required — just connect.
- **Writing (today):** ask the owner for the `PKIS_MCP_WRITE_KEY` and use Claude
  Code as in §2A. There is no per-person write on mobile yet.
- **Writing (after OAuth):** ask the owner to add your email to the writer
  allowlist (`PKIS_ROLES_PATH`). Then sign in via the connector — done.

---

## 5. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Write tool → `requires write authorization key` | No/invalid credential | Desktop: check the `Authorization` header in `~/.claude.json`. Mobile: writes need OAuth (not yet live) or you're a reader. |
| Mobile connector connects but only reads | Expected pre-OAuth, or you're a `reader` post-OAuth | Get added to the allowlist (post-OAuth) or use Claude Code (today). |
| Reads work, can't even see write tools | Some clients hide tools you can't call | Cosmetic; verify with a known read tool like `get_health_metrics`. |
| `405` on `GET /mcp` | Server-Sent Events not supported on GET | Expected — MCP uses POST. Not an error. |
| (Post-OAuth) login loops / stays unauthenticated | Malformed `WWW-Authenticate` or redirect-URI mismatch | Owner: test with MCP Inspector; see `OAUTH_PLAN.md` §9. |

---

## 6. Security notes

- **Today:** write access is a *single shared secret*. Anyone who has it can
  write as "the wiki," with no attribution. Rotate it (`PKIS_MCP_WRITE_KEY` on
  the host + every client) if it may have leaked. This is the limitation OAuth
  removes.
- **After OAuth:** writes are tied to a real, revocable identity; the static key
  is demoted to a documented machine-to-machine service credential for desktop
  Claude Code only.
- Reads are intentionally open. If that changes, it's a one-line default flip
  (see `OAUTH_PLAN.md` §4).

---

*Maintainer: `choct155@gmail.com`. Implementation details for the auth model
live in [`OAUTH_PLAN.md`](./OAUTH_PLAN.md).*
