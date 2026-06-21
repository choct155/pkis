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

## Register new explainers as PKIS assets + set up explainer roadmap
**Date logged:** 2026-06-21
**Source:** Claude.ai session — June 2026 research session
**Idea:** Three explainers built in Claude.ai sessions need to be registered in the PKIS asset system and their HTML files deployed to the viz serving directory so they appear in the PWA at pkis.dev/app/. A fourth task is creating an EXPLAINER_ROADMAP.md in pkis/docs/ tracking planned explainers not yet built. Full Claude Code brief with asset frontmatter, HTML file locations, and roadmap spec is in the Claude Code brief attached to this session.
**Relation to existing system:** Extends the asset registry. New explainers are: knowledge_infrastructure_bundle.html (covers amortization + hardening), mi_estimation_explainer.html (covers MI estimation families), accuracy_calibration_explainer.html (covers silver/gold calibration + NHPP revision model). Roadmap tracks four planned explainers: hardening trajectory, quality framework, passive instrumentation, retrieval comparison (blocked on intelligent layer results).
**Open questions:** Check existing HMC/Typical Sets asset frontmatter for canonical directory structure and viz serving path before writing new frontmatter files.
**Status:** open


## Reading queue vs. concept frontier — dedupe the priority signal
**Date logged:** 2026-06-14
**Source:** Claude Code: main (code-review engagement)
**Idea:** The flat reading queue (`queue.md`, coarse high/normal tags via add_to_queue / get_reading_queue) and `get_concept_frontier` are partly redundant — but only partly. They rank *different objects*: the queue ranks **sources you flagged to read**; the frontier ranks **concepts the graph says are under-developed** (a continuous priority_score). The frontier can only prioritize what's already modeled, so the queue is irreplaceable as the **pre-ingestion capture inbox** (add_to_queue even accepts a free-text reference that isn't a node). The genuinely redundant piece is the manual `high/normal` tag — a coarse, hand-maintained duplicate of the frontier's computed score. Proposal: keep the queue as a capture inbox; demote the priority tag to a capture-time hint that only matters *before* ingestion; once a queued source is ingested, derive its ordering from the frontier + reading graph (a queued paper floats up by how much it advances a high-priority frontier concept). One prioritizer (frontier), one capture surface (queue).
**Relation to existing system:** Touches the reading-priority surfaces — queue.md, tool_add_to_queue / tool_get_reading_queue, the viewer queue/priority views, tool_get_concept_frontier, tool_get_reading_graph (scope=queue_only), the Librarian's queue-drain and the Auditor's queue-hygiene check. A de-duplication in the spirit of consolidating the dual write surfaces and the copy-pasted git logic.
**Open questions:** Is the capture-time tag worth keeping at all, or fully derive from the frontier? How to order pre-ingestion captures with no graph signal yet? Does folding queue ordering into the frontier complicate the viewer's queue view?
**Status:** open


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
