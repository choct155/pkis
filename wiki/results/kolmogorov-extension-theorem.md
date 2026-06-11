---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability
- mathematics
id: pkis:result:kolmogorov-extension-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- stochastic-process-as-prior
- gaussian-process
related_concepts: []
sources:
- murphy-pml2-advanced-ch31
tags:
- stochastic-process
- consistency
- infinite-dimensional
- measure-theory
- bayesian-nonparametric
title: Kolmogorov Extension Theorem
understanding: 0
uses:
- probability-theory
---

## Definition
Let $\{(\Omega_t, \mathcal{F}_t)\}_{t\in\mathcal{T}}$ be a family of measurable spaces. For each finite $I\subset\mathcal{T}$ suppose $\mu_I$ is a probability measure on $\prod_{t\in I}\Omega_t$ such that the family is **consistent** (projective): for $I\subset J$, $\mu_I$ equals the marginal of $\mu_J$ on the $I$-coordinates. Then there exists a unique probability measure $\mu$ on the product space $(\prod_{t\in\mathcal{T}}\Omega_t,\,\bigotimes_{t}\mathcal{F}_t)$ whose marginals are the $\mu_I$.

This is the mathematical guarantee that a coherent stochastic process can be specified by its finite-dimensional distributions.

### Why it matters
The theorem justifies the entire programme of Bayesian nonparametrics: one only needs to specify consistent finite-dimensional distributions (as Gaussian processes and Dirichlet processes do) and the full infinite-dimensional process is automatically well-defined.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gaussian-process]] — prerequisite-of
- [[stochastic-process-as-prior]] — prerequisite-of
- [[probability-theory]] — uses
[To be populated during integration]