# PKIS Ideas

Holding area for ideas that are worth preserving but **not yet decided**. Entries
graduate to [`DECISIONS.md`](DECISIONS.md) (if adopted), get dropped (with a note), or
stay here while still open. Newest first. Most entries are appended automatically by
the `log_idea` MCP tool from chat or code sessions.

Format:
```
## <short title>
**Date logged:** YYYY-MM-DD
**Source:** <chat session title or code session context>
**Idea:** description
**Relation to existing system:** what it extends or replaces
**Open questions:** what must be resolved before this can be decided
**Status:** open | adopted (→ DECISIONS [date]) | dropped (<reason>)
```

---

## Discovery inbox + feedback UI
**Date logged:** 2026-06-12
**Source:** docs-system bootstrap (migrated from project notes)
**Idea:** Build the viewer-side inbox where proactively discovered candidate sources
can be accepted/dismissed with a reason chip, feeding a relevance signal back into
discovery ranking.
**Relation to existing system:** Completes the proactive-discovery layer (currently a
validated MVP with no UI). The durable signal/noise fix.
**Open questions:** What feedback dimensions to capture; how aggressively accepted
items enter the reading queue.
**Status:** open
