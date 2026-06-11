---
aliases: []
also_type: []
analogous-to:
- monte-carlo-estimator
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
- optimization
- machine-learning
extends:
- stochastic-gradient-descent
id: pkis:technique:svrg
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch08
tags:
- variance-reduction
- control-variate
- finite-sum
- linear-convergence
- SGD
title: Stochastic Variance Reduced Gradient (SVRG)
understanding: 0
uses:
- strong-convexity
---

## Definition
**SVRG** (Johnson & Zhang 2013) reduces the variance of SGD gradient estimates using a control-variate construction. Periodically (e.g., each epoch) a snapshot $\tilde{\theta}$ is taken and the full-batch gradient $\nabla L(\tilde{\theta})$ is computed. At step $t$, the corrected gradient estimate is:

$$g_t = \nabla L_n(\theta_t) - \nabla L_n(\tilde{\theta}) + \nabla L(\tilde{\theta})$$

This estimate is unbiased ($\mathbb{E}[g_t] = \nabla L(\theta_t)$) and has variance that decreases as $\theta_t \to \tilde{\theta}$. SVRG achieves **linear convergence** (the same rate as full-batch gradient descent) on strongly-convex finite-sum objectives, while requiring only two stochastic gradient evaluations per step.

### Why it matters
SVRG (and related SAGA) bridge the gap between the per-step cheapness of SGD and the fast convergence of full-batch GD, and are the theoretical workhorses behind variance reduction in ML. They are less used in deep learning due to incompatibility with batch-norm and dropout.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[monte-carlo-estimator]] — analogous-to
- [[strong-convexity]] — uses
- [[stochastic-gradient-descent]] — extends
[To be populated during integration]