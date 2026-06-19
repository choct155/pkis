# PKIS Inbox

The single surface where everything needing human attention is collected. **All
agents append; only the human removes** (check an item off with `- [x]` or delete
the line). The PWA inbox view renders each swim lane as a section. (Agent Roster
v2, Build Order Phase 1.)

> Empty lanes below are the skeleton — agents append real items under the matching
> heading. Checked-off items older than 30 days are pruned by the Auditor.

## Discovery
Items parked for potential future ingest. Review when a primary concept becomes active.
<!-- - [ ] [[slug]] — rationale (primary concept) (date parked) [Librarian] -->

## Proposals
Synthesizer proposals ready for review and approval.
<!-- - [ ] Synthesizer proposal pass YYYY-MM-DD — N proposals (wiki/proposals/synthesizer-YYYY-MM-DD.md) -->

## Staged
Bridge notes and staged nodes awaiting commit or discard.
<!-- - [ ] [[staged-id]] — title (date staged) [MCP] -->

## Structural Gaps
Auditor-flagged gaps for Synthesizer attention.
<!-- - [ ] Problem without techniques: [[problem-slug]] (date flagged) [Auditor] -->
<!-- - [ ] Isolated domain: domain-name — N cross-domain edges (date flagged) [Auditor] -->
- [x] Frontmatter wikilink-quoting bug (sources): unquoted `[[wikilink]]` in YAML list fields misparses as a NESTED LIST (`[[x]]` → `[['x']]`), breaking source rendering. FIXED the `sources` field for 15 causal-inference nodes (selection-bias, ATE, LATE, DiD, RDD, IV, matching, synthetic-control, fixed-effects, propensity-score, collider-bias, omitted-variable-bias, identification-strategy, parallel-trends, potential-outcomes-framework) → now block-style quoted strings (2026-06-19). NB: the cited sources (cunningham-causal-inference-mixtape, malkiel-emh-critics-2003) DO exist — encoding was the only problem.
- [ ] Frontmatter wikilink-quoting bug (other fields): the SAME misparse affects ~11 nodes' `related_concepts` / other list fields — hygiene pass to quote `[[wikilinks]]` in all frontmatter list values; ideally fix the writing path so agents emit quoted wikilinks (2026-06-19) [Hygienist]
- [ ] Broken node: `wiki/sources/jaynes-probability-ch10.md` has malformed YAML frontmatter (won't parse → won't load into the graph) — needs a manual fix (2026-06-19) [Hygienist]
- [ ] Source-capture sweep: prose in many nodes cites readable ingested books (MacKay, BDA3, …) that never made it into the structured `sources`/Reading Path — Synthesizer pass to capture cited readable sources corpus-wide. Exemplar done: [[bayesian-inference]] enriched 2026-06-19 with readable [[mackay-itila-ch02]] + [[gelman-bda3-ch01]] (its prior sole source, the kroese ch.8 stub, has no readable text) (2026-06-19) [Auditor]

## Awaiting Classification
Sources with low-confidence knowledge-object classifications pending human decision.
<!-- - [ ] [[source-slug]] § object-name — candidate types: technique or principle (date flagged) [Librarian] -->

## Conformance
Schema violations and convention issues.
<!-- - [ ] [[node-slug]] — missing IRI (date flagged) [Hygienist] -->
<!-- - [ ] Architect report YYYY-MM-DD — N violations (date) -->

## Budget
Cost alerts from the Comptroller.
<!-- - [ ] Weekly variable cost $XX.XX — exceeds threshold (date) -->
