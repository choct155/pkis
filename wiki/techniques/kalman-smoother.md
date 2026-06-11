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
- signal-processing
- machine-learning
- control-theory
id: pkis:technique:kalman-smoother
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch13
tags:
- Kalman
- smoothing
- RTS
- backward-pass
- LDS
- EM
title: Kalman Smoother (RTS Smoother)
understanding: 0
---

## Definition
The backward message-passing pass for an LDS that computes the full-data posterior $\gamma(\mathbf{z}_n)=p(\mathbf{z}_n|\mathbf{x}_1,\ldots,\mathbf{x}_N)=\mathcal{N}(\mathbf{z}_n|\hat{\mu}_n,\hat{V}_n)$ by combining Kalman filter outputs with a backward recursion (Rauch-Tung-Striebel equations):

$$J_{n-1} = V_{n-1}A^T P_{n-1}^{-1}$$
$$\hat{\mu}_{n-1} = \mu_{n-1} + J_{n-1}(\hat{\mu}_n - A\mu_{n-1})$$
$$\hat{V}_{n-1} = V_{n-1} + J_{n-1}(\hat{V}_n - P_{n-1})J_{n-1}^T$$

initialized at $\hat{\mu}_N=\mu_N$, $\hat{V}_N=V_N$ from the Kalman filter.

### Why it matters
Forms the E step of EM for LDS parameter learning, providing the posterior moments $E[z_n]$, $E[z_nz_n^T]$, $E[z_nz_{n-1}^T]$ needed by the M step. Analogous to the $\beta$-pass of the forward-backward algorithm for HMMs; subsumes the Kalman filter when no future observations are available.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]