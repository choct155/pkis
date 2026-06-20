---
aliases: []
also_type: []
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- bayesian-stats
- forecasting
id: pkis:technique:bayesian-model-averaging
knowledge_type: technique
maturity: settled
related_concepts:
- '[[model-selection-problem]]'
- '[[conjugate-prior]]'
- '[[spike-and-slab]]'
- '[[ensemble-learning]]'
sources:
- '[[steel-bma-forecasting-2011]]'
- '[[scott-varian-nowcasting-2013a]]'
- '[[scott-varian-bsts-2014]]'
- gelman-bda3
tags:
- model-uncertainty
- variable-selection
- marginal-likelihood
- g-prior
- ensemble-methods
title: Bayesian Model Averaging
understanding: 0
---

The principled Bayesian approach to model uncertainty: rather than selecting a single best model, compute a posterior-weighted mixture over all models in the model space M. For any quantity of interest Δ (such as a forecast), P(Δ|y) = Σ_j P(Δ|y, M_j) P(M_j|y), where P(M_j|y) ∝ L_y(M_j) P(M_j) is the posterior model probability proportional to marginal likelihood times prior. BMA is optimal under squared error loss (Min-Zellner 1993) and log predictive score (Raftery et al. 1997) when the true model is in M.

In practice, BMA over 2^k models for large k requires MCMC over model space (sampling only models with non-negligible posterior probability), or spike-and-slab priors that naturally induce sparsity and enable BMA as a by-product of posterior simulation.

## Reading Path
- [[steel-bma-forecasting-2011]] (unread) — the primary tutorial on BMA in economics: covers the g-prior structure, hierarchical priors on θ and g, and sensitivity of posterior model probabilities to prior choices; applications to growth regressions
- [[scott-varian-nowcasting-2013a]] (unread) — BMA as by-product of spike-and-slab MCMC for nowcasting; posterior predictive distribution automatically averages over predictor subsets
- [[scott-varian-bsts-2014]] (unread) — BMA in the BSTS system: marginal posterior inclusion probabilities as summaries, model-averaged forecasts from posterior predictive distribution

## Prediction under discrete model uncertainty (MacKay)
MacKay (ITILA Ch. 3) presents BMA as a virtue of the Bayesian approach: rather than 'test' a default model and then use it exclusively, carry forward model uncertainty when predicting any quantity $t$ via the sum rule $P(t\mid D,I)=\sum_H P(t\mid D,H,I)\,P(H\mid D,I)$, where the model weights $P(H\mid D,I)$ come from Bayesian model comparison (posterior model probabilities $\propto$ evidence $\times$ prior).