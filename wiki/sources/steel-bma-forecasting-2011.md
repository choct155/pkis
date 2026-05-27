---
id: "pkis:source:steel-bma-forecasting-2011"
aliases: []
title: "Bayesian Model Averaging and Forecasting"
authors: ["Mark F.J. Steel"]
year: 2011
type: paper
domain: [bayesian-stats, forecasting]
tags: [model-uncertainty, variable-selection, g-prior, marginal-likelihood, economic-forecasting]
source_url: ""
drive_id: "14wr-jEyK9UTwcs3t38O8wjZtDuxYgqxU"
drive_path: "PKIS/sources/papers/steel-bma-forecasting-2011.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[bayesian-model-averaging]]", "[[spike-and-slab]]", "[[model-selection-problem]]"]
---

## Summary

A focused tutorial on Bayesian Model Averaging (BMA) for variable selection in linear regression, with emphasis on forecasting in economics. The paper motivates BMA as the principled Bayesian response to model uncertainty: rather than selecting the single best model, form a posterior-weighted mixture over all 2^k models (where k is the number of potential regressors), yielding predictions and inference that properly propagate model uncertainty.

The paper focuses on the normal linear regression model with Fernández-Ley-Steel prior structure: an improper prior on intercept and scale, and a g-prior (Zellner 1986) on regression coefficients, so that Bayes factors and marginal likelihoods have closed-form expressions. The key decisions are: (1) the choice of g controlling how much information the prior assigns to β, and (2) the prior on model space P(Mⱼ) controlling expected model size. Steel argues strongly for hierarchical priors on both g and on the model inclusion probability θ, showing that a fixed θ = 0.5 (equal model prior) creates unintended concentration of prior mass at intermediate model sizes, while a Beta(1,b) hyperprior on θ with chosen prior mean model size is more robust and data-adaptive. Empirical applications use cross-country growth regressions with k=67 potential regressors.

## Key Knowledge Objects

- [[bayesian-model-averaging]] (technique, high) — formal Bayesian treatment of model uncertainty via posterior-weighted mixture over 2^k models; the central subject of this paper
- [[model-selection-problem]] (problem, high) — the general challenge of choosing among competing models given finite data; BMA is offered as the principled solution

## Key Extractions

1. **BMA as optimal predictor**: Min and Zellner (1993) show that BMA minimizes expected predictive squared error loss if the true model is in the set M; Raftery et al. (1997) show it is optimal under log predictive score. BMA is thus not just philosophically correct but empirically competitive.
2. **g-prior structure**: Under the Fernández-Ley-Steel prior, the Bayes factor between models Mᵢ and Mⱼ is a function only of sample size n, the hyperparameter g, and the R² values of the two models. For equal fit, the larger model is penalized by g^{−1/2} per additional regressor.
3. **Prior sensitivity**: "The use of hierarchical priors on θ always leads to downweighting of models with kⱼ around k/2, counteracting the fact that there are many more models of intermediate size." Fixed θ is dangerously sensitive to the choice of mean model size m; random θ is much more robust.
4. **g choices**: Recommended choices for g are max(n, k²) (Fernández-Ley-Steel 2001) or hyper-g/n prior (Liang et al. 2008). The author recommends using a hierarchical Beta prior on g for robustness, sampling (g, Mⱼ) jointly via Gibbs.
5. **Practical recommendation**: Use hierarchical Beta(1, b) prior on θ with elicited prior mean model size m, and a hyperprior on g of hyper-g/n type. Free R packages: BAS (Clyde), BMA (Raftery), BMS (Feldkircher/Zeugner).

## Connection Candidates

- [[bayesian-model-averaging]] — creates: this paper is the primary tutorial source for BMA in economics
- [[model-selection-problem]] — addresses: BMA is the Bayesian approach to resolving model uncertainty
- [[lasso]] — contrasts-with: both do variable selection under p >> n but LASSO gives point estimate at mode; BMA gives posterior over all models with positive probability at exactly-zero coefficients
- [[bayesian-linear-regression]] — prerequisite-of: BMA over linear models requires understanding Bayesian updating of regression coefficients via conjugate g-prior
- [[em-algorithm]] — contrasts-with: EM is an alternative for model selection in latent variable models; BMA averages over models rather than selecting one
