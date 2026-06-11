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
- deep-learning
- bayesian-inference
- optimisation
extends:
- laplace-approximation
id: pkis:technique:swa-swag
instantiates:
- bayesian-deep-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- SGD-trajectory
- flat-minima
- posterior-approximation
- ensembles
- Polyak-Ruppert
title: Stochastic Weight Averaging (SWA) and SWAG
understanding: 0
uses:
- stochastic-gradient-descent
- mode-connectivity
- effective-dimensionality-bnn
---

## Definition
**SWA** computes $\bar{\theta} = \frac{1}{S}\sum_{s=1}^{S} \theta_s$, where $\theta_s$ are SGD iterates collected at a *fixed* (non-decaying) learning rate. **SWAG** extends SWA by fitting a Gaussian posterior:
$$p(\theta|D) \approx \mathcal{N}(\bar{\theta},\, \Sigma), \quad \Sigma = \frac{\Sigma_{\text{diag}} + \Sigma_{\text{lr}}}{2}$$
where $\Sigma_{\text{diag}}$ is estimated from running second-moment statistics of iterates and $\Sigma_{\text{lr}}$ is a low-rank empirical covariance of recent deviation vectors.

### Why it matters
SGD at a fixed learning rate implicitly samples from a Gaussian approximation to the posterior centred at a local mode. SWA finds a *flat* basin centre—a broader minimum that generalises better than any single SGD point. SWAG converts these samples into a proper posterior distribution, enabling calibrated uncertainty estimates at negligible additional training cost, scaling to ResNet/ImageNet-scale models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[effective-dimensionality-bnn]] — uses
- [[mode-connectivity]] — uses: SWA finds a flat-basin centre along mode-connecting loss surface
- [[laplace-approximation]] — extends: SWAG fits a Gaussian to the mode found by SWA, similar to Laplace but using SGD trajectory
- [[stochastic-gradient-descent]] — uses: Collects iterates from SGD at fixed learning rate as posterior samples
- [[bayesian-deep-learning]] — instantiates
[To be populated during integration]