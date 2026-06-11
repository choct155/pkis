---
aliases: []
also_type: []
applies:
- curse-of-dimensionality
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- generative-adversarial-network
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
extends:
- factor-analysis
generalizes:
- probabilistic-pca
id: pkis:technique:mixture-of-factor-analyzers
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch20
- murphy-pml2-advanced-ch28
specializes:
- gaussian-mixture-models
tags:
- mixture-models
- factor-analysis
- dimensionality-reduction
- em-algorithm
- manifold-learning
title: Mixture of Factor Analyzers (MFA)
understanding: 0
uses:
- em-algorithm
- variational-inference
- automatic-relevance-determination
---

## Definition
$$p(x|\theta) = \sum_{k=1}^{K} \pi_k \mathcal{N}(x|\mu_k,\; W_k W_k^T + \Psi_k)$$

A mixture of factor analyzers assigns each observation to one of $K$ local linear FA models; it can be seen as a low-rank mixture of Gaussians requiring $O(KLD)$ instead of $O(KD^2)$ parameters, fitted via EM with an additional discrete latent indicator.

### Why it matters
MFA approximates a globally nonlinear manifold by a union of local linear subspaces, trading off expressiveness and parameter efficiency. It reduces overfitting compared with full-covariance Gaussian mixtures, and generalises naturally to mixtures of PPCA models. It motivates the nonlinear extension provided by VAEs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generative-adversarial-network]] — contrasts-with: MFA achieves competitive image generation while admitting exact likelihoods
- [[automatic-relevance-determination]] — uses: ARD used to prune irrelevant latent dimensions automatically
- [[variational-inference]] — uses
- [[curse-of-dimensionality]] — applies
- [[probabilistic-pca]] — generalizes
- [[em-algorithm]] — uses
- [[gaussian-mixture-models]] — specializes
- [[factor-analysis]] — extends
[To be populated during integration]