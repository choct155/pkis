---
aliases: []
also_type: []
analogous-to:
- dirichlet-distribution
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
- probability-theory
- statistics
- bayesian-inference
extends:
- wishart-distribution
id: pkis:concept:inverse-wishart-distribution
instantiates:
- conjugate-prior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch02
tags:
- inverse-wishart
- covariance-prior
- conjugate-prior
- multivariate
- inverse-gamma-generalization
title: Inverse Wishart Distribution
understanding: 0
uses:
- multivariate-normal-model
---

## Definition
The **inverse Wishart distribution** $\mathrm{IW}(\boldsymbol{\Sigma} \mid \mathbf{S}^{-1}, \nu)$ is the distribution of $\boldsymbol{\Sigma}$ when $\boldsymbol{\Sigma}^{-1} \sim \mathrm{Wi}(\mathbf{S}^{-1}, \nu)$:
$$\mathrm{IW}(\boldsymbol{\Sigma} \mid \mathbf{S}^{-1}, \nu) \propto |\boldsymbol{\Sigma}|^{-(\nu+D+1)/2} \exp\!\left(-\tfrac{1}{2}\mathrm{tr}(\mathbf{S}\boldsymbol{\Sigma}^{-1})\right),$$
for $\nu > D-1$ and $\mathbf{S} \succ 0$. Its mean is $\mathbf{S}/(\nu-D-1)$ (for $\nu > D+1$). For $D=1$ it reduces to the inverse gamma; for $s=1$ it reduces to the inverse chi-squared.

### Why it matters
The inverse Wishart is the standard conjugate prior for the covariance matrix $\boldsymbol{\Sigma}$ of a multivariate Gaussian (as opposed to the precision), and is used extensively in Bayesian multivariate analysis and hierarchical models for covariance structure.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[dirichlet-distribution]] — analogous-to
- [[multivariate-normal-model]] — uses
- [[conjugate-prior]] — instantiates
- [[wishart-distribution]] — extends
[To be populated during integration]