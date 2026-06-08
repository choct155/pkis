---
aliases: []
also_type: []
applies:
- deconvolution
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- maximum-likelihood-estimation
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- bayesian-stats
id: pkis:technique:optimal-linear-filter
instantiates:
- bayesian-inference
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch46
tags:
- wiener-filter
- deconvolution
- regularization
- gaussian-prior
- minimum-mean-square-error
- pseudoinverse
title: Optimal Linear Filter (Wiener Filter)
understanding: 0
uses:
- regularization
- laplace-approximation
---

## Definition
The optimal linear filter is the best *linear* estimator $\hat{\mathbf{f}} = \mathbf{W}\mathbf{d}$ for recovering a signal from linearly-degraded, noisy data $d_n = \sum_k R_{nk} f_k + n_n$. With a Gaussian likelihood (noise variance $\sigma_\nu^2$) and a Gaussian prior on the image (scale $\sigma_f$, correlation matrix $\mathbf{C}$), the posterior is Gaussian and its mode equals its mean:
$$\mathbf{f}_{MP} = \left[ \mathbf{R}^T\mathbf{R} + \tfrac{\sigma_\nu^2}{\sigma_f^2}\mathbf{C} \right]^{-1}\mathbf{R}^T\mathbf{d}.$$
The added term $\tfrac{\sigma_\nu^2}{\sigma_f^2}\mathbf{C}$ regularizes the otherwise ill-conditioned pseudoinverse $[\mathbf{R}^T\mathbf{R}]^{-1}\mathbf{R}^T$. When noise vanishes it reduces to that pseudoinverse.

### Two derivations, one filter
It arises from two routes. The *Bayesian* route maximizes the Gaussian posterior. The *minimum-square-error* route assumes a linear estimator $\hat{\mathbf{f}}=\mathbf{W}\mathbf{d}$ and minimizes the expected squared error, giving $\mathbf{W}_{opt} = \mathbf{F}\mathbf{R}^T[\mathbf{R}\mathbf{F}\mathbf{R}^T + \sigma_\nu^2\mathbf{I}]^{-1}$ with $\mathbf{F}=\langle f_j f_{j'}\rangle$. Identifying $\mathbf{F}=\sigma_f^2\mathbf{C}^{-1}$ shows the two estimators coincide, even though the MSE derivation made no explicit Gaussian assumption.

### Why it matters
This equivalence reveals the implicit Gaussian assumptions buried in classical least-squares signal processing, and the Bayesian view exposes them as criticizable choices. It also yields *error bars* (the posterior covariance), not just a point estimate, enabling uncertainty visualization.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[laplace-approximation]] — uses: Posterior covariance is the inverse Hessian of the neg-log-posterior; for this Gaussian posterior the Laplace approximation is exact.
- [[maximum-likelihood-estimation]] — contrasts-with: Dropping the prior term reduces the filter to the ML pseudoinverse, which is ill-conditioned; the prior is what regularizes it.
- [[regularization]] — uses: The sigma_nu^2/sigma_f^2 C term regularizes the ill-conditioned pseudoinverse.
- [[bayesian-inference]] — instantiates: f_MP is the posterior mode of a linear-Gaussian Bayesian model; the filter is MAP estimation.
- [[deconvolution]] — applies: The optimal linear filter is the standard linear solution to the deconvolution / linear inverse problem.
[To be populated during integration]