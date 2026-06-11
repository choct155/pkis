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
- probabilistic-modeling
id: pkis:technique:sliced-score-matching
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch24
tags:
- Fisher-divergence
- random-projection
- Hutchinson-estimator
- EBM-training
title: Sliced Score Matching (SSM)
understanding: 0
---

## Definition
$$J_{\mathrm{SSM}}(\theta) = E_{p_D(x)}E_{p(v)}\!\left[\frac{1}{2}(v^T s_\theta(x))^2 + v^T (\mathbf{J}_x s_\theta(x))\,v\right]$$

SSM (Song et al. 2019) reduces the $O(d^2)$ Jacobian trace in basic score matching to $O(d)$ by projecting the score onto random directions $v \sim p(v)$. The key insight is that $\sum_{i,j}(\partial^2 E/\partial x_i \partial x_j)v_i v_j$ can be computed as a single Jacobian-vector product $v^T \mathbf{J}_x s_\theta v$, requiring only two forward/backward passes via automatic differentiation.

### Why it matters
SSM is a consistent estimator of the data distribution (unlike DSM) and computationally efficient for high-dimensional data. When $p(v)=\mathcal{N}(0,I)$, the first term collapses to the squared-norm term of basic SM, recoverable via the Hutchinson trace estimator. SSM bridges NCE and SM: the NCE objective with small perturbation vectors equals SSM up to $o(\|v\|^2)$ terms.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]