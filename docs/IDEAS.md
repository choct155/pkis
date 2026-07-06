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

## Write path test
**Date logged:** 2026-07-06
**Source:** Claude chat: write path validation
**Idea:** MCP write connectivity test from Claude.ai chat. Discard.
**Relation to existing system:** —
**Open questions:** —
**Status:** open


## OpGraph Strategist — multi-agent strategic council
**Date logged:** 2026-06-29
**Source:** Claude chat: OpGraph agent roster design session
**Idea:** The Strategist agent role in OpGraph may eventually evolve beyond a single reasoning agent into a multi-agent "strategic council" — multiple agents or personas with different stances, frameworks, or priorities debating a question or decision. Different agents could represent different analytical lenses (risk-focused, opportunity-focused, stakeholder-focused) or even simulate the positions of key people in the portfolio. The user directs the council, observes the debate, and uses it to pressure-test a decision or surface blind spots before committing.
**Relation to existing system:** Extends the OpGraph Strategist agent role. Potentially draws on Person and Role nodes in OpGraph to ground personas in real stakeholder positions. Conceptually adjacent to multi-agent debate frameworks in the AI literature.
**Open questions:** What's the right number of council members? How do personas get defined — user-specified, graph-derived from real stakeholders, or archetype-based? How does the output get captured back into OpGraph as a Decision or Commitment? Does this require a multi-agent LangGraph architecture (separate subgraphs per persona) or can it be simulated with a single model and structured prompting?
**Status:** open


## Register new explainers as PKIS assets and create explainer roadmap
**Date logged:** 2026-06-21
**Source:** Claude Code: main
**Idea:** Three HTML explainers built in Claude.ai need registering in the PKIS asset system and deploying to the viz serving directory. Also create EXPLAINER_ROADMAP.md in pkis/docs/. Full task brief in conversation — pass to Claude Code.
**Relation to existing system:** —
**Open questions:** —
**Status:** open


## Register new explainers as PKIS assets and create explainer roadmap
**Date logged:** 2026-06-21
**Source:** Claude.ai session — session date June 21 2026
**Idea:** Three HTML explainers built in Claude.ai sessions need to be registered in the PKIS asset system and the HTML files deployed to the viz serving directory. Additionally create EXPLAINER_ROADMAP.md in pkis/docs/ tracking planned explainers. Full task brief and code prompt in conversation context — pass to Claude Code.
**Relation to existing system:** Asset registry, explainer infrastructure, position paper scaffolding
**Open questions:** Which directory does the viz serving happen from? Check existing HMC/Typical Sets asset frontmatter for canonical path structure before writing new ones.
**Status:** open


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
