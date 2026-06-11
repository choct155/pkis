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
- machine-learning
- numerical-methods
id: pkis:concept:hmm-scaling-factors
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch13
tags:
- HMM
- numerical-stability
- scaling
- underflow
- forward-backward
title: HMM Scaling Factors and Numerical Stability
understanding: 0
---

## Definition
To prevent underflow in the forward-backward algorithm, the raw $\alpha(z_n)=p(x_1,\ldots,x_n,z_n)$ is replaced by the normalized quantity $\hat{\alpha}(z_n)=p(z_n|x_1,\ldots,x_n)$, related by
$$\alpha(z_n) = \left(\prod_{m=1}^n c_m\right)\hat{\alpha}(z_n), \quad c_n = p(x_n|x_1,\ldots,x_{n-1})$$

The scaled backward variable is $\hat{\beta}(z_n)=\left(\prod_{m=n+1}^N c_m\right)\beta(z_n)$. Marginals are recovered as $\gamma(z_n)=\hat{\alpha}(z_n)\hat{\beta}(z_n)$ and the marginal likelihood as $p(X)=\prod_{n=1}^N c_n$.

### Why it matters
Without scaling, $\alpha(z_n)$ decays exponentially in $n$ and underflows to zero in double precision for sequences of moderate length ($\sim 100$ steps). The scaling factors cancel in all EM ratio quantities (e.g. $\mu_k$) but their log-sum gives $\ln p(X)=\sum_n \ln c_n$, enabling likelihood monitoring during training.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]