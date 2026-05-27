---
id: "pkis:technique:spike-and-slab"
aliases: []
title: "Spike-and-Slab Priors"
knowledge_type: technique
also_type: []
domain: [bayesian-stats, time-series]
tags: [variable-selection, sparsity, bernoulli-prior, g-prior, stochastic-search-variable-selection]
related_concepts: ["[[bayesian-model-averaging]]", "[[bayesian-linear-regression]]", "[[conjugate-prior]]", "[[regularization]]"]
sources: ["[[scott-varian-nowcasting-2013a]]", "[[scott-varian-bsts-2014]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

A class of prior distributions for regression coefficients that enables probabilistic variable selection by placing positive probability mass exactly at zero. The joint prior factors as p(β, γ, σ⁻²) = p(β_γ|γ, σ²) p(σ⁻²|γ) p(γ), where γ_i ∈ {0,1} is the inclusion indicator. The "spike" is the Bernoulli prior p(γ): p(γ_i = 1) = π_i, placing mass at β_i = 0. The "slab" is the continuous prior p(β_γ|γ, σ²): typically a diffuse Gaussian (Zellner g-prior) conditional on inclusion. This differs from L1/lasso regularization, which gives a mode at zero but no positive probability mass.

Posterior inference via MCMC: the SSVS (stochastic search variable selection, George-McCulloch 1997) algorithm uses Gibbs sampling, sampling each γ_i from its binary full conditional — which has a closed form because the marginal likelihood for each sub-model is available analytically under the conjugate Gaussian-inverse-Gamma prior. Marginal posterior inclusion probabilities for each predictor are estimated as the proportion of MCMC draws with γ_i = 1.

## Reading Path
- [[scott-varian-nowcasting-2013a]] (unread) — introduces spike-and-slab in the context of nowcasting with Google Trends; describes the Bernoulli spike and g-prior slab, and the SSVS Gibbs sampler
- [[scott-varian-bsts-2014]] (unread) — complete technical derivation: closed-form marginal posterior of γ, SSVS algorithm, default prior elicitation via expected model size and expected R²; most thorough treatment in the cluster
