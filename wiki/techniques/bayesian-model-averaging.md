---
id: "pkis:technique:bayesian-model-averaging"
aliases: []
title: "Bayesian Model Averaging"
knowledge_type: technique
also_type: []
domain: [bayesian-stats, forecasting]
tags: [model-uncertainty, variable-selection, marginal-likelihood, g-prior, ensemble-methods]
related_concepts: ["[[model-selection-problem]]", "[[conjugate-prior]]", "[[spike-and-slab]]", "[[ensemble-learning]]"]
sources: ["[[steel-bma-forecasting-2011]]", "[[scott-varian-nowcasting-2013a]]", "[[scott-varian-bsts-2014]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

The principled Bayesian approach to model uncertainty: rather than selecting a single best model, compute a posterior-weighted mixture over all models in the model space M. For any quantity of interest Δ (such as a forecast), P(Δ|y) = Σ_j P(Δ|y, M_j) P(M_j|y), where P(M_j|y) ∝ L_y(M_j) P(M_j) is the posterior model probability proportional to marginal likelihood times prior. BMA is optimal under squared error loss (Min-Zellner 1993) and log predictive score (Raftery et al. 1997) when the true model is in M.

In practice, BMA over 2^k models for large k requires MCMC over model space (sampling only models with non-negligible posterior probability), or spike-and-slab priors that naturally induce sparsity and enable BMA as a by-product of posterior simulation.

## Reading Path
- [[steel-bma-forecasting-2011]] (unread) — the primary tutorial on BMA in economics: covers the g-prior structure, hierarchical priors on θ and g, and sensitivity of posterior model probabilities to prior choices; applications to growth regressions
- [[scott-varian-nowcasting-2013a]] (unread) — BMA as by-product of spike-and-slab MCMC for nowcasting; posterior predictive distribution automatically averages over predictor subsets
- [[scott-varian-bsts-2014]] (unread) — BMA in the BSTS system: marginal posterior inclusion probabilities as summaries, model-averaged forecasts from posterior predictive distribution
