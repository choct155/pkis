---
aliases: []
also_type: []
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
- bayesian-stats
- knowledge-representation
id: pkis:framework:relational-probability-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch15
tags:
- first-order-probability
- database-semantics
- directed-models
- context-specific-independence
- relational-uncertainty
title: Relational Probability Model
understanding: 0
---

## Definition
A first-order probability model built on the database semantics of first-order logic: it adopts the unique-names assumption and domain closure (no objects beyond those named) so the set of possible worlds stays finite, but unlike pure database semantics it does NOT make the closed-world assumption. An RPM has constant, function, and predicate symbols with a type signature for each function; instantiating every function over every combination of typed objects yields the basic random variables. One dependency statement per function (with logical-variable arguments) specifies a shared conditional distribution, so a complex domain with astronomically many possible worlds can be captured in a few hundred parameters. RPMs support context-specific independence via if-then-else dependencies and relational uncertainty (an unknown function value, e.g. Author(b), acts as a multiplexer selecting which parents influence a child). The semantics are obtained by grounding the dependencies into an equivalent Bayesian network. Used in the book-recommendation example and in Bayesian skill-rating systems such as Microsoft's TrueSkill.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]