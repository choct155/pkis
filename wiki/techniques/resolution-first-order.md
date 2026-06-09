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
generalizes:
- backward-chaining-fol
id: pkis:technique:resolution-first-order
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch09
tags:
- first-order-logic
- logical-inference
- theorem-proving
- russell-norvig-aima
title: First-Order Resolution
understanding: 0
uses:
- unification
- skolemization
- herbrands-theorem
---

## Definition
The lifted version of propositional resolution and the only inference family complete for any first-order KB (not just definite clauses). Two CNF clauses with no shared variables are resolved on complementary literals — one unifying with the negation of the other under MGU theta — producing a resolvent with theta applied. Resolution is refutation-complete: it proves KB entails alpha by deriving the empty clause from KB and not-alpha.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[herbrands-theorem]] — uses
- [[backward-chaining-fol]] — generalizes
- [[skolemization]] — uses
- [[unification]] — uses
[To be populated during integration]