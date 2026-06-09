---
aliases: []
also_type: []
applies:
- datalog
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:framework:logic-programming
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch09
tags:
- first-order-logic
- logic-programming
- russell-norvig-aima
title: Logic Programming
understanding: 0
uses:
- backward-chaining-fol
---

## Definition
A declarative programming paradigm embodying Kowalski's equation Algorithm = Logic + Control: knowledge is expressed as definite clauses and problems are solved by running inference (depth-first backward chaining) over them. Prolog is the canonical language; it trades full first-order semantics for efficiency by adopting database semantics (unique-names + closed-world + negation-as-failure), omitting the occur check, and offering no loop checks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[datalog]] — applies
- [[backward-chaining-fol]] — uses
[To be populated during integration]