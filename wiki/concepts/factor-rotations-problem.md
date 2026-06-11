---
aliases: []
also_type: []
analogous-to:
- identifiability-of-mixtures
- label-switching
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- independent-component-analysis
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:concept:factor-rotations-problem
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch28
tags:
- identifiability
- factor-loading
- rotational-invariance
- latent-variables
title: Factor Rotations Problem
understanding: 0
---

## Definition
$$\text{Cov}[x] = W R R^T W^T + \Psi = W W^T + \Psi \quad \forall\, R \in O(L)$$

The factor rotations problem is the unidentifiability of a factor analysis model with respect to orthogonal transformations of the latent space: any rotation $\tilde{W} = WR$ of the factor loading matrix yields identical marginal likelihood. Because $p(z) = \mathcal{N}(0,I)$ is rotation-invariant, neither $W$ nor the latent factors $z$ can be uniquely recovered without additional constraints.

### Why it matters
This fundamental ambiguity means MLE or MAP estimates of $W$ are not interpretable without explicit regularization. Standard resolutions include (a) lower-triangular constraints on $W$ with positive diagonal, (b) orthogonality constraints as in PCA, (c) sparsity-promoting priors (ARD, spike-and-slab), or (d) non-Gaussian priors on $z$ (as in ICA). Understanding this problem is essential before using factor loadings for scientific interpretation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[label-switching]] — analogous-to
- [[independent-component-analysis]] — contrasts-with: Non-Gaussian priors in ICA resolve the rotation ambiguity
- [[identifiability-of-mixtures]] — analogous-to
[To be populated during integration]