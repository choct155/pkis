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
- optimization
- machine-learning
generalizes:
- lasso
- elastic-net
id: pkis:concept:composite-objective
instantiates:
- regularization
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch08
tags:
- proximal
- regularization
- lasso
- non-smooth
- splitting
title: Composite Objective (Smooth + Non-smooth)
understanding: 0
uses:
- subgradient-subdifferential
---

## Definition
A **composite objective** decomposes the loss into a smooth part and a non-smooth part:

$$\mathcal{L}(\theta) = \mathcal{L}_s(\theta) + \mathcal{L}_r(\theta)$$

where $\mathcal{L}_s$ is continuously differentiable (e.g., negative log-likelihood) and $\mathcal{L}_r$ is non-smooth (e.g., $\ell_1$ norm, total-variation penalty). The structure enables specialized algorithms — notably **proximal gradient methods** — that handle each part differently rather than blending them.

### Why it matters
Most regularized ML objectives (LASSO, group-LASSO, elastic net) are composite. Recognizing this structure enables provably faster algorithms than treating the combined objective as generic non-smooth, and provides a principled interface between the optimization and statistical goals of regularization.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[elastic-net]] — generalizes
- [[lasso]] — generalizes
- [[regularization]] — instantiates
- [[subgradient-subdifferential]] — uses
[To be populated during integration]