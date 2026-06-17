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
