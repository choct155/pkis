---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:technique:mixture-of-factor-analyzers
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch20
- murphy-pml2-advanced-ch28
tags:
- mixture-models
- factor-analysis
- dimensionality-reduction
- em-algorithm
- manifold-learning
title: Mixture of Factor Analyzers (MFA)
understanding: 0
---

## Definition
$$p(x|\theta) = \sum_{k=1}^{K} \pi_k \mathcal{N}(x|\mu_k,\; W_k W_k^T + \Psi_k)$$

A mixture of factor analyzers assigns each observation to one of $K$ local linear FA models; it can be seen as a low-rank mixture of Gaussians requiring $O(KLD)$ instead of $O(KD^2)$ parameters, fitted via EM with an additional discrete latent indicator.

### Why it matters
MFA approximates a globally nonlinear manifold by a union of local linear subspaces, trading off expressiveness and parameter efficiency. It reduces overfitting compared with full-covariance Gaussian mixtures, and generalises naturally to mixtures of PPCA models. It motivates the nonlinear extension provided by VAEs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]