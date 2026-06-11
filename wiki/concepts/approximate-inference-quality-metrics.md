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
- bayesian-inference
- approximate-inference
- model-evaluation
id: pkis:concept:approximate-inference-quality-metrics
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch07
tags:
- KL-divergence
- posterior-quality
- evaluation
- Wasserstein
- Bayesian-risk
title: Approximate Inference Quality Metrics
understanding: 0
---

## Definition
$$\text{KL divergence: } D_{\text{KL}}(p(\theta|D)\| q_t(\theta)), \quad \text{Bayesian risk: } R = \mathbb{E}_{p^*(x,y)}[\ell(y, q(y|x,D))]$$

where $q(y|x,D) = \int p(y|x,\theta)q(\theta|D)\,d\theta$ is the predictive distribution under the approximate posterior $q$.

Metrics for comparing approximate inference algorithms include: (1) reverse KL to the true posterior (hard to compute but theoretically clean); (2) Wasserstein distance; (3) held-out predictive performance; (4) Bayesian risk under a task loss; (5) performance on downstream tasks such as active or continual learning.

### Why it matters
Because the "ground truth" posterior is usually unavailable, practitioners must rely on indirect proxies. Held-out log-likelihood and downstream task performance are most commonly used in practice. The choice of metric matters: VI minimises forward KL which tends to under-disperse, while MCMC targets the full posterior but is slower, and the "best" method depends on the downstream use case.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]