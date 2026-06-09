---
aliases: []
also_type: []
applies:
- datalog
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- backward-chaining-fol
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:technique:forward-chaining-fol
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch09
tags:
- first-order-logic
- logical-inference
- datalog
- russell-norvig-aima
title: Forward Chaining (First-Order)
understanding: 0
uses:
- generalized-modus-ponens
---

## Definition
A data-driven inference algorithm over first-order definite clauses: starting from known facts, it repeatedly fires every rule whose premises are satisfied (via Generalized Modus Ponens), adding conclusions until the query is answered or a fixed point is reached. Sound and complete for definite clauses; for Datalog it runs in polynomial data complexity, but with function symbols it can generate infinitely many facts (entailment is only semidecidable).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[datalog]] — applies
- [[backward-chaining-fol]] — contrasts-with
- [[generalized-modus-ponens]] — uses
[To be populated during integration]