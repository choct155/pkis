---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:concept:unification
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- generalized-modus-ponens
- resolution-first-order
- backward-chaining-fol
- forward-chaining-fol
related_concepts: []
sources:
- russell-norvig-aima-ch09
tags:
- first-order-logic
- logical-inference
- russell-norvig-aima
title: Unification
understanding: 0
---

## Definition
Unification is the process of finding a substitution (a unifier) that makes two logical expressions syntactically identical: UNIFY(p,q) returns theta such that SUBST(theta,p) = SUBST(theta,q), or failure if none exists. It is the engine of all first-order inference, since lifted inference rules require making different expressions look identical.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[forward-chaining-fol]] — prerequisite-of
- [[backward-chaining-fol]] — prerequisite-of
- [[resolution-first-order]] — prerequisite-of
- [[generalized-modus-ponens]] — prerequisite-of
[To be populated during integration]