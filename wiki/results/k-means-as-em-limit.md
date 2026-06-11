---
aliases: []
also_type: []
applies:
- k-means-algorithm
- gaussian-mixture-models
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
- machine-learning
- statistics
id: pkis:result:k-means-as-em-limit
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch09
tags:
- K-means
- Gaussian-mixtures
- EM
- hard-assignment
- temperature-limit
title: K-Means as a Limit of Gaussian Mixture EM
understanding: 0
uses:
- em-monotone-likelihood-increase
- responsibilities-mixture-models
---

## Definition
Consider a Gaussian mixture with isotropic components $p(\mathbf{x}\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)=\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}_k,\epsilon\mathbf{I})$, $\epsilon$ fixed. The responsibilities are
$$\gamma(z_{nk})=\frac{\pi_k\exp\{-\|\mathbf{x}_n-\boldsymbol{\mu}_k\|^2/2\epsilon\}}{\sum_j\pi_j\exp\{-\|\mathbf{x}_n-\boldsymbol{\mu}_j\|^2/2\epsilon\}}.$$
In the limit $\epsilon\to 0$, the term with the smallest $\|\mathbf{x}_n-\boldsymbol{\mu}_j\|^2$ dominates, so $\gamma(z_{nk})\to r_{nk}$ (hard 0/1 assignment). The M-step mean update $\boldsymbol{\mu}_k=\frac{1}{N_k}\sum_n\gamma(z_{nk})\mathbf{x}_n$ reduces to the K-means centroid formula, and the expected complete-data log likelihood becomes $-\tfrac{1}{2}J + \text{const}$.

Therefore maximising the EM lower bound in this limit is equivalent to minimising the K-means distortion $J$.

### Why it matters
This derivation places K-means inside the probabilistic EM framework, clarifying that hard assignment is an extreme (zero-temperature) version of soft assignment. It justifies using K-means to initialise Gaussian mixture EM, and shows that K-means inherits EM's monotone convergence property.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[responsibilities-mixture-models]] — uses
- [[em-monotone-likelihood-increase]] — uses
- [[gaussian-mixture-models]] — applies
- [[k-means-algorithm]] — applies
[To be populated during integration]