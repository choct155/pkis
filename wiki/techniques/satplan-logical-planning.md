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
- optimization
- symbolic-subsymbolic
id: pkis:technique:satplan-logical-planning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch07
tags:
- satplan
- planning
- sat
- successor-state-axiom
- precondition-axiom
- action-exclusion
title: 'SATPLAN: Planning as Satisfiability'
understanding: 0
uses:
- satisfiability-sat
- frame-problem
- dpll-algorithm
---

## Definition
An approach (Kautz & Selman, 1992) that solves planning by reduction to Boolean satisfiability: build a single propositional sentence asserting the initial state Init₀, the successor-state (transition) axioms Transition₁…Transition_t for all actions up to horizon t, and the goal achieved at time t; hand it to a SAT solver; if a satisfying model is found, the action variables assigned true form a plan. Because the plan length is unknown, SATPLAN tries increasing horizons t up to T_max, guaranteeing the shortest plan. Crucially, satisfiability has different requirements than entailment-based querying (ASK): unknown variables can be set to whatever makes the goal true, so a correct encoding must also include precondition axioms (an action requires its preconditions, e.g. Shoot^t ⇒ HaveArrow^t), exactly-one-location/orientation constraints, and action-exclusion axioms (¬A_i^t ∨ ¬A_j^t for interfering action pairs) to rule out spurious plans.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[dpll-algorithm]] — uses: A DPLL-style solver finds the plan model.
- [[frame-problem]] — uses: Transition axioms in SATPLAN are successor-state axioms, the frame-problem solution.
- [[satisfiability-sat]] — uses: Reduces planning to finding a satisfying model.
[To be populated during integration]