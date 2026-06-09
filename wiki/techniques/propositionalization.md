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
id: pkis:technique:propositionalization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch09
tags:
- first-order-logic
- logical-inference
- russell-norvig-aima
title: Propositionalization
understanding: 0
---

## Definition
The reduction of first-order inference to propositional inference by replacing quantified sentences with their ground instances: Universal Instantiation substitutes ground terms for universally quantified variables (every instantiation) and Existential Instantiation substitutes a fresh Skolem constant once. Made complete by Herbrand's theorem, but typically slow because it generates many unnecessary ground instances, and it inherits the semidecidability of first-order entailment.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]