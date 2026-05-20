---
title: "Kalman Filter"
knowledge_type: technique
also_type: []
domain: [time-series, state-space-models, bayesian-stats]
tags: [state-space-models, sequential-inference, linear-gaussian, recursive-estimation, filtering, smoothing]
related_concepts: ["[[state-space-models]]", "[[structural-time-series]]", "[[bayesian-linear-regression]]", "[[dynamic-factor-models]]"]
sources: ["[[duncan-mskf-seemingly-unrelated-1993]]", "[[scott-varian-nowcasting-2013a]]", "[[scott-varian-bsts-2014]]", "[[stock-watson-leading-indicators-1992]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 4
understanding: 0
maturity: settled
---

Recursive Bayesian estimation algorithm for linear Gaussian state-space models: given the current observation y_t, the Kalman filter produces the optimal (minimum mean-square-error) estimate of the latent state α_t by combining the prior prediction (from the transition equation) with the observation likelihood, yielding a Gaussian posterior that serves as the prior for the next step.

## Reading Path
- [[duncan-mskf-seemingly-unrelated-1993]] (unread) — introduces Kalman filter as the DLM update step within MSKF; presents the recursive equations for m_t and C_t explicitly
- [[scott-varian-nowcasting-2013a]] (unread) — uses Kalman filter within BSTS Gibbs sampler; describes the Durbin-Koopman simulation smoother for sampling the latent state
- [[scott-varian-bsts-2014]] (unread) — most complete technical description of Kalman filtering/smoothing/simulation in the context of structural time series with spike-and-slab regression
- [[stock-watson-leading-indicators-1992]] (unread) — uses Kalman filter to compute the conditional distribution of the unobserved economic state for recession probability computation
