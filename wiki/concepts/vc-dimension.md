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
- statistical-learning
id: pkis:concept:vc-dimension
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch07
tags:
- model-complexity
- generalization-bounds
- shattering
- vc-theory
title: Vapnik–Chervonenkis (VC) Dimension
understanding: 0
---

## Definition
A general, parameter-count-free measure of the complexity (capacity) of a class of functions, defined as the largest number of points that can be shattered by members of the class. A set of points is shattered if, for every one of the 2^n binary labelings of those points, some member of the class realizes that labeling exactly. The VC dimension answers the limitation of “number of parameters” as a complexity measure: the single-parameter family I(sin(αx) > 0) has infinite VC dimension (it can shatter arbitrarily many points by choosing the frequency α), whereas a linear indicator in p dimensions has VC dimension p+1 — exactly its free-parameter count. The definition extends from indicator functions to real-valued functions g via the indicator class {I(g(x,α) − β > 0)}. The practical payoff is distribution-free generalization bounds: fitting N points with a class of VC dimension h gives, with probability ≥ 1−η over training sets, an upper bound on Err_T of the form err + ε-correction, where ε ∝ h[log(a₂N/h)+1]/N. These bounds hold simultaneously over the entire class (hence permit searching over it), grow with h and shrink with N — qualitatively matching the AIC d/N correction but stronger. The chief practical obstacle is that the VC dimension of a class is usually hard to compute, and only crude upper bounds are typically obtainable.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]