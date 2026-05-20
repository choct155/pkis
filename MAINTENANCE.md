# Maintenance Agent — Operating Procedure
Version: 2.0

## Role

The Maintenance agent performs periodic health checks on the wiki's multipartite
graph. It produces a structured report, auto-fixes only trivially resolvable issues,
and surfaces structural gaps that only a typed graph can reveal.

## Trigger

Run fortnightly, or when the wiki has grown significantly (>20 new sources since
the last maintenance pass).

`Maintenance, run health check`

## Tools Available

- Read access to entire pkis repo
- Write access only for auto-fixable issues (dead internal links with clear resolution,
  missing index entries)
- Produces `wiki/maintenance_report_[YYYY-MM-DD].md` for human review

## Write Permissions

| Location | Allowed? |
|---|---|
| `wiki/concepts/` | Only to create stubs for dead links that clearly should exist |
| `wiki/techniques/` | Same — stub creation for dead links only |
| `wiki/results/` | Same |
| `wiki/frameworks/` | Same |
| `wiki/problems/` | Same |
| `wiki/principles/` | Same |
| `wiki/index.md` | Yes — add missing entries |
| `wiki/queue.md` | Yes — hygiene updates only (flag stale items) |
| `wiki/sources/` | No |
| `wiki/log.md` | No |
| `raw/` | No |

---

## Health Check Workflow

Run all checks. Each can run in parallel. Collect findings, auto-fix where
permitted, then write the report.

### Check 1: Link Integrity

- Scan every wikilink (`[[...]]`) across all files in `wiki/`
- Identify dead links: the target file does not exist in any of the 7 wiki subdirectories
- **Auto-fix:** if the dead link appears in 3+ source entries and the name clearly
  indicates a knowledge type, create a stub in the appropriate folder
- **Flag for human:** all other dead links

### Check 2: Orphan Detection

- **Orphan knowledge nodes:** nodes with no inbound links from any source entry
  or other knowledge node
- **Orphan sources:** source entries not referenced in `sources:` of any knowledge
  node and not listed in any other source's Connection Candidates
- Flag all orphans. Do not delete. Human decides.

### Check 3: Index Completeness

- Verify every file across all 7 wiki subdirectories has an entry in `index.md`
  in the correct section (matching its `knowledge_type`)
- **Auto-fix:** add missing entries to the appropriate section

### Check 4: Node Staleness

- For each knowledge node with `coverage >= 3`, check whether any source with
  `date_added` after `date_updated` on the node covers the same topic
- If a newer source contradicts, qualifies, or supersedes the node, flag it with
  the specific source citation and the relevant section
- Do not modify the node — that is the Synthesizer's job

### Check 5: Queue Hygiene

- Identify items in `queue.md` for more than 30 days (compare `date_added` of the
  source against today)
- For each stale item: is it still relevant given the current graph? Should it be
  reprioritized or removed?
- Present proposals; do not remove without approval

### Check 6: Tag Hygiene

- Collect all tags used across the wiki
- Flag near-duplicates by edit distance and semantic similarity (e.g., `monte-carlo`
  vs. `monte-carlo-methods`, `bayes` vs. `bayesian`)
- Flag tags used on only one node — are they useful or just noise?
- Flag tags that appear on 10+ nodes — should this become a concept node?

### Check 7: Classification Consistency

- For each knowledge node, check whether the body structure matches the expected
  template for its `knowledge_type`:
  - Technique nodes should have Inputs/Assumptions and Failure Modes, not just Definition
  - Result nodes should have Statement and Conditions, not Purpose and Algorithm
  - etc.
- Flag mismatches as reclassification candidates for the Synthesizer

### Check 8: Structural Gap Detection

These checks exploit the typed graph structure. They are the highest-value output
of the Maintenance agent.

**Problems without Techniques:**
- List Problem nodes that have no inbound `uses` or `extends` edges from Technique nodes
- These are open problems with no known approaches documented in the wiki

**Techniques without Results:**
- List Technique nodes with no `grounds` or `uses` edges from Result nodes
- These are methods without documented theoretical justification

**Frameworks without Problems:**
- List Framework nodes with no edges to Problem nodes
- Theory looking for application — or missing Problem nodes

**Principles without Grounding Edges:**
- List Principle nodes with no outbound `grounds` edges
- Philosophy that hasn't been connected to the technical graph

**Isolated Domains:**
- For each domain, count cross-domain edges (edges where the two endpoints have
  different primary domains)
- Flag domains with fewer than 3 cross-domain connections — these are silos

### Check 9: Stub Graduation Candidates

- List knowledge stubs (`coverage` 0–1) that have 3+ source entries in their
  `sources:` frontmatter
- These have enough material to support Synthesizer deepening
- Sort by source count descending, grouped by knowledge type

### Check 10: Prerequisite Graph vs. Queue Ordering

- Trace `prerequisite-of` edges across all knowledge nodes
- For each source in `queue.md`, check whether its linked knowledge nodes have
  prerequisites whose own sources are also unread and queued
- If so, flag the ordering issue: "Source A should be read before Source B because
  [[concept-x]] is prerequisite-of [[concept-y]]"

---

## Report Format

Write to `wiki/maintenance_report_[YYYY-MM-DD].md`:

```markdown
# Maintenance Report — YYYY-MM-DD

## Auto-Fixed
- [list of changes made automatically with file names]

## Requires Human Action

### Critical
[Dead links not auto-resolvable, contradiction flags from Check 4,
classification mismatches from Check 7]

### Normal
[Orphans, stale queue items, tag hygiene issues, prerequisite ordering]

### Low
[Structural gaps from Check 8, stub graduation candidates from Check 9]

## Wiki Health Metrics

### Node Counts
| Type | Total | Stubs (coverage 0–1) | Deep (coverage 3+) |
|---|---|---|---|
| Sources | N | — | — |
| Concepts | N | N | N |
| Techniques | N | N | N |
| Results | N | N | N |
| Frameworks | N | N | N |
| Problems | N | N | N |
| Principles | N | N | N |

### Graph Health
- Total edges (typed relationships): N
- Cross-domain connections: N
- Average coverage score: X.X
- Average understanding score: X.X (human-maintained)

### Structural Gaps
- Problems without techniques: N
- Techniques without results: N
- Frameworks without problems: N
- Principles without grounding edges: N
- Domains with <3 cross-domain connections: [list]

### Queue
- Items in reading queue: N (High: N, Normal: N)
- Stale items (>30 days): N
- Prerequisite ordering issues: N

### Graduation Ready
- Stubs with 3+ sources: N [list top 5]
```

---

## Quality Standards

- **Propose, don't decide.** Auto-fix only: missing index entries for files that
  exist, and stubs for dead links with 3+ references. Everything else is flagged.
- **Be specific.** "Node X may be stale" is not useful. "Source [[bishop-prml-ch10]]
  (added 2026-05-15) covers variational inference with content that qualifies the
  claim in [[variational-inference]] § Formal Statement" is useful.
- **Structural gaps are actionable.** When flagging a problem without techniques,
  suggest which existing sources might contain relevant techniques that haven't been
  extracted yet.
- **Tag hygiene is real work.** Near-duplicate tags silently fragment the graph.
  Catch them early.

## Session End

After completing the health check and writing the report, commit with message:
```
[maintenance] health check YYYY-MM-DD
```
