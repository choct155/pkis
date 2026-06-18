# Comptroller — Operating Procedure
Version: 1.1

> **Status: LIVE (Phase 4 deployed 2026-06-18).** Built and deployed:
> `usage.py` (the store + cost model + best-effort `log_usage`), `tools/comptroller.py`
> (the reporting CLI), `log_usage` wired into the MCP server's one Anthropic call
> site (`tool_detect_concepts`), the SQLite store seeded on the VPS, and the
> daily/weekly/monthly report crons.
>
> **Two deviations from the original spec, by deployment constraint:**
> 1. **Store path is `/home/pkis/usage/usage.sqlite`, not `/var/pkis/usage/…`** —
>    passwordless sudo on the VPS is `systemctl`-only, and the `pkis` user owns
>    `/home/pkis`, so the store lives there (no `/var` sudo needed). The schema and
>    behavior are otherwise exactly as specified.
> 2. **The scheduled threshold→inbox alert is deferred.** The report crons run
>    **report-only**, writing to `/home/pkis/usage/` (outside the wiki git repo).
>    They do **not** pass `--inbox`, because the 15-minute deploy cron does a plain
>    `git pull` that a dirty working tree would break. Enabling the inbox alert on a
>    schedule needs a safe commit/push path (a flock'd add+commit+push, or routing
>    the alert through the MCP write surface). Until then, the alert fires only on a
>    **manual** `Comptroller, report weekly --inbox …` run, where a human owns the
>    commit. The CLI fully supports it (`maybe_alert_inbox`, tested).

## Role

Track the total budgetary cost of all Claude API usage across every call site.
Produce breakdowns by origin, model, project, and time window; flag threshold
crossings. The Comptroller **owns the usage store and all budget reporting**.

The Comptroller is the one roster member that is **not a Claude agent** — it is a
plain Python script that reads the SQLite usage store and writes reports without any
LLM call. (The single exception: the on-demand `Comptroller, report …` invocation
can be triggered from a Claude Code session, which just shells out to the script and
returns its output.)

## Cost Model

Two categories:

**Fixed** — the Claude.ai Max Plan subscription. Stored as config constants
(`max_plan_monthly_usd`, `billing_cycle_start_day`). Included as a line item in
monthly rollups; not tracked dynamically.

**Variable** — API calls from all instrumented call sites. Cost per call is computed
from published Anthropic pricing **at the time of the call**:

```
cost = input_tokens       × input_rate
     + output_tokens      × output_rate
     + cache_read_tokens  × cache_read_rate
     + cache_write_tokens × cache_write_rate
```

Rates live in the `config` table and are updated manually when Anthropic changes
pricing. **Historical events are never retro-priced** — each `usage_events` row keeps
the cost computed at emission time.

## Data Architecture

**Usage store:** SQLite at `/home/pkis/usage/usage.sqlite` on the Hetzner VPS
(config key `PKIS_USAGE_DB` / `config.USAGE_DB_PATH`).

Three tables:

```sql
-- Config: pricing constants and fixed costs
CREATE TABLE config (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Usage events: one row per API call
CREATE TABLE usage_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emitted_at TIMESTAMP NOT NULL,
    origin TEXT NOT NULL,        -- 'pkis-mcp', 'claude-code', 'iks-pipeline', 'manual'
    project TEXT,                -- 'pkis', 'iks', 'ars', null if unknown
    model TEXT NOT NULL,         -- 'claude-sonnet-4-6', etc.
    input_tokens INTEGER NOT NULL,
    output_tokens INTEGER NOT NULL,
    cache_read_tokens INTEGER DEFAULT 0,
    cache_write_tokens INTEGER DEFAULT 0,
    computed_cost_usd REAL NOT NULL,
    attributes TEXT              -- JSON blob for extensible fields; schema evolves here
);

-- Budget periods: monthly rollups
CREATE TABLE budget_periods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    fixed_cost_usd REAL NOT NULL,
    variable_cost_usd REAL NOT NULL,
    total_cost_usd REAL NOT NULL,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**The `attributes` JSON column is the schema-evolution surface.** When a new
attribution dimension is needed (agent name, hypothesis cluster, IKS job ID), add it
to `attributes` with no migration. The Comptroller reads known keys and ignores
unknown ones — fixed envelope, flexible payload (the open-attributes-bag pattern).

## Instrumentation Points

### PKIS MCP server (primary, highest priority — Phase 4)

The MCP server is the most tractable instrumentation point: every tool handler that
makes a Claude API call has the response's `usage` metadata in hand. Phase 4 adds a
`log_usage` helper called at the end of each such handler:

```python
def log_usage(response, origin="pkis-mcp", project="pkis", attributes=None):
    usage = response.usage
    cost = compute_cost(usage.input_tokens, usage.output_tokens,
                        getattr(usage, 'cache_read_input_tokens', 0),
                        getattr(usage, 'cache_creation_input_tokens', 0))
    db.execute("""
        INSERT INTO usage_events
        (emitted_at, origin, project, model, input_tokens, output_tokens,
         cache_read_tokens, cache_write_tokens, computed_cost_usd, attributes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (datetime.utcnow(), origin, project, response.model,
          usage.input_tokens, usage.output_tokens,
          getattr(usage, 'cache_read_input_tokens', 0),
          getattr(usage, 'cache_creation_input_tokens', 0),
          cost, json.dumps(attributes or {})))
```

**Reliability constraint:** `log_usage` must never break a tool call. Wrap the write
so that a failure to log (locked DB, disk full) is swallowed and logged to stderr,
not propagated to the MCP response. Accounting is best-effort; serving is not.

### Claude Code (secondary, partial)

Claude Code makes API calls through its own internals. On each run the Comptroller
checks for a local usage file (`~/.claude/usage.json` or equivalent) on the machine
where Claude Code runs; if present it ingests new entries, **deduplicating by session
ID**. If absent, Claude Code usage is carried only as an estimated line item based on
observed session patterns (and labelled `(estimated)` in reports).

### Future call sites (IKS pipeline, ARS)

When built, these wrap the Anthropic SDK client in the same `log_usage` pattern and
distinguish themselves via the `origin` field (`'iks-pipeline'`, `'ars-session'`,
…). No store change required — arbitrary origins are already accommodated.

## Pricing Config Initialization

On first run, seed the `config` table (example rates — confirm against current
Anthropic pricing at deploy time):

```sql
INSERT INTO config VALUES ('claude_sonnet_input_per_mtok', '3.00', CURRENT_TIMESTAMP);
INSERT INTO config VALUES ('claude_sonnet_output_per_mtok', '15.00', CURRENT_TIMESTAMP);
INSERT INTO config VALUES ('claude_sonnet_cache_read_per_mtok', '0.30', CURRENT_TIMESTAMP);
INSERT INTO config VALUES ('claude_sonnet_cache_write_per_mtok', '3.75', CURRENT_TIMESTAMP);
INSERT INTO config VALUES ('max_plan_monthly_usd', '100.00', CURRENT_TIMESTAMP);
INSERT INTO config VALUES ('billing_cycle_start_day', '1', CURRENT_TIMESTAMP);
```

Add per-model rate keys as more models are instrumented (Opus, Haiku). Update rates
manually on Anthropic price changes; the Comptroller reads them at report time only.

## Trigger Conditions

- **Daily** — summary of the previous day's variable API cost by origin.
- **Weekly** — full breakdown by origin, project, model, with week-over-week delta.
- **Monthly** — budget close: fixed + variable, written to `budget_periods`.
- **On demand** — `Comptroller, report [daily|weekly|monthly|ytd]`.
- **On threshold crossing** — when weekly variable cost exceeds a configurable
  threshold (default: 50% of monthly budget headroom), append an alert to
  `wiki/inbox.md` under `## Budget`, following the lane convention:
  `- [ ] Weekly variable cost $XX.XX — exceeds threshold (YYYY-MM-DD) [Comptroller]`

## Report Format

Write to `/home/pkis/usage/comptroller_report_YYYY-MM-DD.md`:

```markdown
# Comptroller Report — YYYY-MM-DD [daily|weekly|monthly]

## Budget Summary
Period: YYYY-MM-DD to YYYY-MM-DD
Fixed cost (Max Plan): $XX.XX
Variable cost (API): $XX.XX
Total: $XX.XX
Remaining headroom: $XX.XX

## Variable Cost Breakdown

### By Origin
| Origin | Calls | Input Tokens | Output Tokens | Cost |
|---|---|---|---|---|
| pkis-mcp | N | N | N | $X.XX |
| claude-code | N | N | N | $X.XX (estimated) |

### By Model
| Model | Calls | Cost |
|---|---|---|

### By Project
| Project | Cost | % of Variable |
|---|---|---|

### By Day (weekly/monthly reports)
[table]

## Alerts
[threshold crossings, anomalies]
```

## Execution Environment

Runs on the Hetzner VPS as a Python script (no LLM call). Schedulable via cron
alongside the discovery job. This `COMPTROLLER.md` describes the **script's behavior
and configuration**, not an LLM agent procedure. The on-demand `Comptroller, report`
invocation may be triggered from a Claude Code session, which calls the script and
relays its output.

### Phase 4 build checklist (delivered 2026-06-18)

1. ✅ `usage.py` — store schema, `compute_cost` (sonnet/opus/haiku families),
   idempotent `seed_pricing`, best-effort `log_usage`, and report query helpers
   (`events_between` / `aggregate` / `total_cost`). 8 unit tests.
2. ✅ `tools/comptroller.py` — `init` (seed) + `report {daily|weekly|monthly|ytd}`
   with window math, by-origin/model/project breakdowns, and the (manual-only for
   now) threshold→inbox alert. 7 tests.
3. ✅ `log_usage` wired into the MCP server's one Anthropic call site
   (`tool_detect_concepts`), best-effort and non-fatal — test-gated (2 integration
   tests), preflight-gated, deploy-verified (40 tools, health ok).
4. ✅ `/home/pkis/usage/` created on the VPS, store initialized + pricing seeded.
5. ✅ cron entries for the daily / weekly / monthly report passes (report-only;
   see the Status note for the deferred inbox alert).

**Not yet delivered (future):** the Claude Code usage-file ingest (secondary
origin, session-dedup), the scheduled inbox alert (needs a safe commit path), and
per-call-site instrumentation of the `tools/` scripts (`reader_build.py`,
`discovery_openalex.py`, `mine_proposals.py`) — each would log under its own
`origin`.
