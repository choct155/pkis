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
- [x] Frontmatter wikilink-quoting bug (other fields): FIXED 2026-06-19 — normalized all 28 affected nodes across every list field (`related_concepts` etc.; some were triple-nested). Still open: fix the *writing path* so agents emit quoted `[[wikilinks]]` and this can't recur. [Hygienist]
- [x] Broken node `wiki/sources/jaynes-probability-ch10.md`: FIXED 2026-06-19 — single-quoted title with inner apostrophes → re-quoted; parses + loads now.
- [ ] Source-capture sweep: prose in many nodes cites readable ingested books (MacKay, BDA3, …) that never made it into the structured `sources`/Reading Path — Synthesizer pass to capture cited readable sources corpus-wide. Exemplar done: [[bayesian-inference]] enriched 2026-06-19 with readable [[mackay-itila-ch02]] + [[gelman-bda3-ch01]] (its prior sole source, the kroese ch.8 stub, has no readable text) (2026-06-19) [Auditor]

- [ ] Reader narration audio gap: 215 of 311 reader chapters have NO narration audio (TTS only run for ~96 — mackay, betancourt, early bishop). Missing across bishop-prml, deisenroth-mml, gelman-bda3, goodfellow-deeplearning, jaynes, murphy-pml1/pml2, pearl-causality, resnick, russell-norvig-aima, sutton. The reader now shows a graceful "narration not generated" notice (2026-06-19) instead of a dead player. Building = reader_build TTS run (significant API/TTS cost via tools/reader_build.py) — decide which books to prioritize (2026-06-19) [owner decision]

- [ ] 89 concept stubs auto-created 2026-06-19 (UX review) from dangling references — all carry `needs_classification: true` + `maturity: stub`. Synthesizer: deepen; Hygienist: verify type (some are techniques/principles/results mis-defaulted to concept). They de-dangled ~100 dead internal links (finance/econ, behavioral-econ, causal). (2026-06-19) [Synthesizer]
- [ ] 2 malformed prose wikilinks (descriptive text inside `[[...]]`) in bridge notes bn-20260531-nedner-is-the-task-under and bn-20260531-the-umbrella-thesis-claims-ontological — fix the link form (2026-06-19) [Hygienist]

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

## Lab
Descriptive drift flags from the Lab Assistant (idle clusters, stuck staged nodes, hypothesis-status swings). Descriptive only — the human decides what they warrant.
<!-- - [ ] Cluster `x` idle 30d (date) -->
