---
aliases: []
also_type: []
analogous-to:
- spike-and-slab
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
contrasts-with:
- l2-regularization-eigenspectrum-shrinkage
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- optimization
- statistics
- regularization
id: pkis:result:l1-sparsity-soft-thresholding
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch07
specializes:
- shrinkage-priors
tags:
- L1-regularization
- LASSO
- sparsity
- soft-thresholding
- feature-selection
title: L1 Regularization Induces Sparsity via Soft Thresholding
understanding: 0
uses:
- lasso
- maximum-a-posteriori-estimation-map
---

## Definition
For a quadratic objective with diagonal Hessian $\mathbf{H} = \text{diag}(H_{ii})$ and $L^1$ penalty $\alpha\|\mathbf{w}\|_1$, the optimal weight satisfies:
$$w_i = \operatorname{sign}(w_i^*)\max\left\{|w_i^*| - \frac{\alpha}{H_{ii}},\; 0\right\}$$

When $|w_i^*| \leq \alpha/H_{ii}$ the weight is set exactly to zero; otherwise it is shifted by $\alpha/H_{ii}$ toward zero.

Unlike $L^2$ regularization, $L^1$ regularization produces exact zeros, inducing a sparse parameter vector.

### Why it matters
The exact-zero property makes $L^1$ (LASSO) a natural feature-selection mechanism: features with insufficient signal-to-noise (small $|w_i^*|$ relative to $\alpha/H_{ii}$) are discarded entirely. This is qualitatively different from $L^2$ shrinkage, which only scales weights toward zero. The result also connects to the Bayesian MAP interpretation: $L^1$ corresponds to a Laplace prior, $L^2$ to a Gaussian prior.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[maximum-a-posteriori-estimation-map]] — uses
- [[shrinkage-priors]] — specializes
- [[spike-and-slab]] — analogous-to: Both achieve parameter sparsity via prior-induced shrinkage-to-zero
- [[l2-regularization-eigenspectrum-shrinkage]] — contrasts-with: L1 produces exact zeros; L2 only scales toward zero
- [[lasso]] — uses
[To be populated during integration]