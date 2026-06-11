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
- machine-learning
- probabilistic-inference
id: pkis:concept:structured-variational-inference
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch19
tags:
- graphical-models
- variational-inference
- posterior-approximation
- approximate-inference
title: Structured Variational Inference
understanding: 0
---

## Definition
Structured variational inference (Saul & Jordan, 1996) generalizes mean field by allowing $q(\mathbf{h}|\mathbf{v})$ to be any distribution that factorizes according to a chosen graphical model structure, rather than requiring full independence:

$$q(\mathbf{h}|\mathbf{v}) \text{ factorizes according to graph } \mathcal{G}_q \subsetneq \mathcal{G}_p$$

The ELBO is then maximized over distributions in this structured family, capturing more posterior correlations than mean field while remaining more tractable than the full posterior.

### Why it matters
Full mean field ($\mathcal{G}_q$ = empty graph) is the extreme tractable case; exact inference ($\mathcal{G}_q = \mathcal{G}_p$) is the extreme expressive case. Structured VI occupies the middle ground. For deep Boltzmann machines, choosing a layered bipartite $q$ graph enables closed-form block updates for alternating layers. The choice of $q$ structure is a model-design decision trading off approximation quality against computational cost.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]