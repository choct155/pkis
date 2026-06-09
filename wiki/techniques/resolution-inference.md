---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:technique:resolution-inference
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch07
tags:
- resolution
- theorem-proving
- refutation
- completeness
- clauses
title: Resolution Inference
understanding: 0
uses:
- conjunctive-normal-form
- satisfiability-sat
---

## Definition
A single inference rule that, applied to clauses in CNF, yields a refutation-complete inference algorithm for propositional logic. The full resolution rule takes two clauses containing a complementary pair of literals (ℓᵢ and ¬ℓᵢ) and produces the resolvent: the disjunction of all the remaining literals from both clauses, with duplicate literals removed (factoring). Soundness follows from case analysis on the complementary literal. A resolution theorem prover decides whether KB ⊨ α by proof by contradiction: convert (KB ∧ ¬α) to CNF and repeatedly resolve clause pairs; if the empty clause (a contradiction, equivalent to False) is ever derived, KB ⊨ α; if no new clauses can be produced first, KB does not entail α.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[satisfiability-sat]] — uses: Refutation: prove KB |= a by showing (KB ^ ~a) unsatisfiable.
- [[conjunctive-normal-form]] — uses: Resolution applies only to clauses; every sentence is converted to CNF first.
[To be populated during integration]