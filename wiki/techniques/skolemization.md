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
id: pkis:technique:skolemization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- resolution-first-order
related_concepts: []
sources:
- russell-norvig-aima-ch09
tags:
- first-order-logic
- logical-inference
- theorem-proving
- russell-norvig-aima
title: Skolemization and CNF Conversion
understanding: 0
---

## Definition
Skolemization removes existential quantifiers by replacing an existentially quantified variable with a fresh Skolem constant (when no universal quantifier is in scope) or a Skolem function of the enclosing universally quantified variables. It is the principal step distinguishing first-order CNF conversion from the propositional case; the Skolemized sentence is satisfiable exactly when the original is.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[resolution-first-order]] — prerequisite-of
[To be populated during integration]