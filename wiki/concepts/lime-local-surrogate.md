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
- interpretability
id: pkis:concept:lime-local-surrogate
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch33
tags:
- LIME
- local-explanation
- surrogate
- model-agnostic
- interpretability
title: Local Interpretable Model-Agnostic Explanations (LIME)
understanding: 0
---

## Definition
**LIME** (Local Interpretable Model-Agnostic Explanations) explains the prediction of any black-box model $f$ at input $x_0$ by fitting a locally-weighted sparse linear model $g \in \mathcal{G}$:
$$\xi(x_0) = \arg\min_{g \in \mathcal{G}} \mathcal{L}(f, g, \pi_{x_0}) + \Omega(g)$$
where $\pi_{x_0}(x) = \exp(-D(x, x_0)^2/\sigma^2)$ is a proximity kernel, $\mathcal{L}$ measures how well $g$ approximates $f$ on samples drawn near $x_0$, and $\Omega(g)$ penalizes complexity (e.g., number of nonzero coefficients).

The explanation is the coefficient vector of the locally-fitted $g$, interpreted as "feature importances in the neighborhood of $x_0$".

### Why it matters
LIME is model-agnostic and applies to any differentiable or black-box predictor, making it one of the most widely deployed post-hoc explanation methods. Its key limitation is locality: the fidelity of $g$ to $f$ degrades outside the neighborhood defined by $\pi_{x_0}$, and users may over-generalize the local explanation. The choice of neighborhood kernel, sampling strategy, and feature representation (e.g., superpixels for images) strongly influences explanation quality.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]