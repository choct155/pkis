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

## Group viewer nav as it grows (8+ items crowd the mobile bottom-nav)
**Date logged:** 2026-06-12
**Source:** Claude Code: main
**Idea:** After adding the Docs view the bottom nav is 8 items, which is cramped on a phone. Consider keeping a primary set (browse, search, priority, graph) prominent and folding secondary views (staged, explainers, discover, docs) into a 'more' sheet or a second row.
**Relation to existing system:** Extends the viewer nav (lib/nav.ts shared by BottomNav + Sidebar) introduced with the docs system.
**Open questions:** Which views are primary vs secondary? Does a 'more' sheet hurt discoverability of discover/docs?
**Resolution:** Primary = browse/clusters/priority/graph; secondary (staged/explainers/discover/docs) folded into a "more" popover above the bottom bar. Desktop sidebar unchanged.
**Status:** adopted — implemented b0a00e27 ("more" menu)


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
