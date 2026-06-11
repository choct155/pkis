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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probabilistic-graphical-models
id: pkis:concept:context-specific-independence
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch16
tags:
- conditional-independence
- graphical-models
- limitations
- CSI
title: Context-Specific Independence
understanding: 0
---

## Definition
A **context-specific independence** (CSI) is a conditional independence that holds only for specific values (a *context*) of some conditioning variables, rather than for all values.

Formally: $X \perp Y \mid Z=z_0$ holds for a particular value $z_0$ but not for all values of $Z$. Equivalently, the conditional distribution $p(X \mid Y, Z=z_0) = p(X \mid Z=z_0)$ even though $X \not\perp Y \mid Z$ in general.

### Why it matters
Context-specific independences cannot be captured by standard graph topology (neither directed nor undirected), because adding an edge to encode the dependence for $z \neq z_0$ incorrectly implies dependence for $z = z_0$. This reveals a fundamental limitation of standard graphical model notation: graphs encode *structural* independences but not value-dependent ones. CSIs can be represented using alternative formalisms such as decision trees, rules, or algebraic decision diagrams for the conditional probability tables.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]