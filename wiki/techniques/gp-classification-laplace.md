---
aliases: []
also_type: []
analogous-to:
- bayesian-neural-networks
applies:
- gaussian-process-gp
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
- bayesian-statistics
- kernel-methods
extends:
- gaussian-process-regression
generalizes:
- logistic-regression
id: pkis:technique:gp-classification-laplace
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch06
- murphy-pml2-advanced-ch18
tags:
- Gaussian-process
- classification
- Laplace-approximation
- IRLS
- approximate-inference
title: Gaussian Process Classification via Laplace Approximation
understanding: 0
uses:
- laplace-approximation
- iteratively-reweighted-least-squares
---

## Definition
In GP classification the latent function $a(\mathbf{x})$ is given a GP prior and mapped through a sigmoid to produce class probabilities. The posterior $p(\mathbf{a}_N|\mathbf{t}_N)$ is non-Gaussian; the **Laplace approximation** finds its mode $\mathbf{a}_N^*$ by iterative reweighted least squares (IRLS):

$$\mathbf{a}_N^{\text{new}} = \mathbf{C}_N(I+W_N\mathbf{C}_N)^{-1}\{\mathbf{t}_N - \boldsymbol{\sigma}_N + W_N\mathbf{a}_N\}$$

where $W_N = \operatorname{diag}[\sigma(a_n)(1-\sigma(a_n))]$. At convergence the posterior is approximated as
$$q(\mathbf{a}_N) = \mathcal{N}(\mathbf{a}_N|\mathbf{a}_N^*, H^{-1}), \quad H = W_N + \mathbf{C}_N^{-1}.$$
The predictive distribution integrates the Gaussian-approximated posterior with the GP prior for the test latent value, yielding a Gaussian $p(a_{N+1}|\mathbf{t}_N)$ whose mean and variance are available in closed form; the final class probability is obtained by a probit-sigmoid integral.

### Why it matters
The Laplace approach extends GP regression to classification with only moderate additional cost (one Newton solve per hyperparameter update), and the resulting approximate log marginal likelihood admits analytic gradients for hyperparameter optimisation, making full Bayesian classification tractable.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-neural-networks]] — analogous-to
- [[gaussian-process-gp]] — applies
- [[logistic-regression]] — generalizes
- [[iteratively-reweighted-least-squares]] — uses
- [[laplace-approximation]] — uses
- [[gaussian-process-regression]] — extends
[To be populated during integration]