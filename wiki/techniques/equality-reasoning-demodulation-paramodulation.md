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
id: pkis:technique:equality-reasoning-demodulation-paramodulation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch09
tags:
- first-order-logic
- theorem-proving
- russell-norvig-aima
title: 'Equality Reasoning: Demodulation and Paramodulation'
understanding: 0
---

## Definition
Techniques for handling the equality relation, which resolution cannot process directly. Three approaches: axiomatize equality (reflexive/symmetric/transitive plus substitution axioms); add inference rules — demodulation (directional rewriting using a unit equation x=y to replace x by y) and paramodulation (its extension to non-unit clauses, which is complete for FOL with equality); or build equality into the unifier via equational unification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]