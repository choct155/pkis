---
aliases: []
also_type: []
applies:
- elbo
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- score-function-estimator
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
extends:
- reparameterization-gradient
id: pkis:technique:stl-estimator
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch06
tags:
- variational-inference
- ELBO
- gradient-estimation
- variance-reduction
- stop-gradient
title: Sticking-the-Landing (STL) Estimator
understanding: 0
---

## Definition
For the reparameterized ELBO gradient, the STL estimator drops the score-function term to reduce variance. Given $z = g(\epsilon, \theta)$, $\epsilon \sim q_0$, and $\tilde{L}(\theta,z) = \log p(z,x) - \log q(z|\theta)$, the standard reparameterized gradient contains:
$$\nabla_\theta \tilde{L} = \underbrace{\nabla_z[\log p(z,x) - \log q(z|\theta)]\cdot J}_{\text{path derivative}} - \underbrace{\nabla_\theta \log q(z|\theta)}_{\text{score function (zero in expectation)}}$$
The STL estimator removes the score-function term by using a **stop-gradient** copy $\theta'$ of $\theta$ in the entropy term:
$$g_{\text{STL}} = \nabla_\theta[\log p(z,x) - \log q(z|\theta')]$$

### Why it matters
The score-function term vanishes in expectation but inflates variance for finite samples, especially when the approximate posterior is far from the true posterior. STL can substantially reduce gradient variance at convergence. However, it is not always superior: weighting STL and the standard estimator optimally (e.g., via the combination estimator of [GD20]) is an active research direction.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[score-function-estimator]] — contrasts-with
- [[elbo]] — applies
- [[reparameterization-gradient]] — extends
[To be populated during integration]