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
- machine-learning
- statistics
id: pkis:result:ebm-log-likelihood-gradient
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch24
tags:
- MLE
- EBM
- partition-function
- Monte-Carlo-gradient
title: EBM Log-Likelihood Gradient Decomposition
understanding: 0
---

## Definition
$$\nabla_\theta \log p_\theta(x) = -\nabla_\theta E_\theta(x) - \nabla_\theta \log Z_\theta$$

where the partition-function gradient equals a model expectation:
$$\nabla_\theta \log Z_\theta = E_{x' \sim p_\theta(x')}[-\nabla_\theta E_\theta(x')]$$

This decomposition, derived by differentiating $\log Z_\theta = \log \int e^{-E_\theta(x)}dx$ under the integral sign, shows that the gradient of the log-likelihood decomposes into a **data term** (pushes energy down at observed $x$) minus an **expectation term** (pushes energy up at model samples).

### Why it matters
This result is the foundation of all MCMC-based MLE training of EBMs: if one can draw approximate samples from $p_\theta$, the intractable partition function gradient can be estimated via Monte Carlo. It also gives the Hebbian (clamped) vs. anti-Hebbian (unclamped) interpretation used in RBM and Boltzmann machine training.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]