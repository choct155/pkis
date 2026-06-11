---
aliases: []
also_type: []
applies:
- bayesian-inference
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
- statistics
- machine-learning
extends:
- gaussian-distribution
id: pkis:result:partitioned-gaussian-conditionals-marginals
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- kalman-filter
related_concepts: []
sources:
- bishop-prml-ch02
tags:
- gaussian-distribution
- conditional-distribution
- marginal-distribution
- bayesian-inference
title: Partitioned Gaussian Conditionals and Marginals
understanding: 0
uses:
- precision-matrix
---

## Definition
Given a joint Gaussian $\mathcal{N}(\mathbf{x}|\boldsymbol{\mu},\boldsymbol{\Sigma})$ with $\boldsymbol{\Lambda}=\boldsymbol{\Sigma}^{-1}$ and partition $\mathbf{x}=(\mathbf{x}_a,\mathbf{x}_b)^T$:

$$p(\mathbf{x}_a|\mathbf{x}_b) = \mathcal{N}(\mathbf{x}_a|\boldsymbol{\mu}_{a|b}, \Lambda_{aa}^{-1})$$
$$\boldsymbol{\mu}_{a|b} = \boldsymbol{\mu}_a - \Lambda_{aa}^{-1}\Lambda_{ab}(\mathbf{x}_b-\boldsymbol{\mu}_b) = \boldsymbol{\mu}_a + \Sigma_{ab}\Sigma_{bb}^{-1}(\mathbf{x}_b-\boldsymbol{\mu}_b)$$
$$\Sigma_{a|b} = \Sigma_{aa} - \Sigma_{ab}\Sigma_{bb}^{-1}\Sigma_{ba}$$
$$p(\mathbf{x}_a) = \mathcal{N}(\mathbf{x}_a|\boldsymbol{\mu}_a, \Sigma_{aa})$$

Conditional covariance is the Schur complement; marginal parameters are simply the corresponding sub-blocks of the joint parameters.

### Why it matters
These identities underlie Kalman filtering, Gaussian process regression, linear dynamical systems, and any Bayesian update in a linear-Gaussian model. The completing-the-square technique used to derive them is a workhorse for analytically tractable probabilistic inference.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kalman-filter]] — prerequisite-of
- [[bayesian-inference]] — applies
- [[precision-matrix]] — uses: Conditional covariance = Lambda_aa^{-1}
- [[gaussian-distribution]] — extends
[To be populated during integration]