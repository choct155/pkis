---
title: "Predicting the Present with Bayesian Structural Time Series"
authors: ["Steven L. Scott", "Hal Varian"]
year: 2014
type: paper
domain: [time-series, forecasting, bayesian-stats]
tags: [nowcasting, google-trends, spike-and-slab, state-space-models, bayesian-model-averaging, mcmc, structural-time-series]
source_url: ""
drive_id: "1pYOurRcHiX_jpU5Ea8w9PzTb0AyyOaCn"
drive_path: "PKIS/sources/papers/scott-varian-bsts-2014.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[structural-time-series]]", "[[kalman-filter]]", "[[spike-and-slab]]", "[[bayesian-model-averaging]]", "[[nowcasting]]"]
---

## Summary

The full publication of the BSTS (Bayesian Structural Time Series) system, extending the earlier 2013 conference paper. The paper provides a complete technical treatment of the state-space model, spike-and-slab prior, MCMC algorithm, and Bayesian model averaging machinery, with two worked examples: weekly initial unemployment claims and monthly retail sales.

The model combines (1) a structural time series component — the Harvey (1989) "basic structural model" with local linear trend (level μ_t, slope δ_t, both random walks) and optional seasonal component τ_t — with (2) a regression component β^T x_t capturing contemporaneous Google search signals. The spike-and-slab prior on β induces sparsity: γ_k ∈ {0,1} indicates inclusion with Bernoulli(π_k) prior, and conditional on inclusion, β_γ ~ N(b_γ, σ² Ω_γ^{-1}) (slab, using Zellner g-prior). Because all components are Gaussian, the MCMC alternates between: sampling the state via the Durbin-Koopman simulation smoother; sampling model parameters (variance components) via conjugate Gamma; and sampling (β, σ², γ) via stochastic search variable selection (SSVS / George-McCulloch 1997).

Key results: for initial claims, adding Google Trends data prevents the large error spike during the 2008–09 financial crisis that the pure time-series model experiences — demonstrating that search query data captures turning-point signals that past time series behavior misses. For retail sales, the full Trends dataset and an economically-relevant subset both outperform Google Correlate alone.

## Key Knowledge Objects

- [[structural-time-series]] (framework, high) — full exposition of the basic structural model in state-space form: observation equation y_t = Z_t^T α_t + ε_t; transition equation α_{t+1} = T_t α_t + R_t η_t; modular composition of trend, seasonal, regression components
- [[kalman-filter]] (technique, high) — primary tool for filtering (forward pass), smoothing (backward pass), and simulation (Durbin-Koopman 2002 simulation smoother) of the latent state; described in full algorithmic detail
- [[spike-and-slab]] (technique, high) — spike-and-slab prior with Zellner g-prior slab; full posterior derivation for γ and β conditional on α; SSVS Gibbs sampler for sampling γ element-wise
- [[bayesian-model-averaging]] (technique, high) — BMA over predictor subsets emerges from MCMC: posterior predictive distribution averages over draws of γ, β, σ², α, θ
- [[nowcasting]] (problem, high) — the nowcasting framing: many economic series are released with a lag; goal is to estimate current value using contemporaneous signals before official release

## Key Extractions

1. **State-space modularity**: State components (trend, seasonal, regression) are combined by concatenating observation vectors Z_t and arranging model matrices block-diagonally. This means any combination of components can be added without redesigning the algorithm — a powerful engineering property of state-space models.
2. **Regression via state augmentation**: Adding the regression component β^T x_t by appending a constant "1" state and updating the observation equation (not the state transition) keeps the state dimension small (Kalman complexity is O(d²) in state dimension d), regardless of the number of regressors.
3. **Spike-and-slab posterior**: The marginal posterior of γ has closed form (after integrating out β and σ²): p(γ|y*) ∝ |Ω_γ^{-1}|^{1/2} / |V_γ^{-1}|^{1/2} × p(γ) × SS_γ^{−N/2}. This is inexpensive to evaluate for sparse models.
4. **Financial crisis turning point**: For initial claims, the model using Google Trends data avoids the large cumulative error jump during the 2008-09 recession that the pure time series model experiences. The recession-related search terms (file for unemployment, state unemployment queries) signal the structural shift contemporaneously.
5. **Retail sales decomposition**: The regression component captures the sharp, sudden drop at the onset of the financial crisis, allowing the local linear trend to remain smooth. This decomposition of "structural change into regression vs. trend" is a key interpretive feature of BSTS.

## Connection Candidates

- [[structural-time-series]] — is: BSTS is the flagship implementation of structural time series with BMA-based predictor selection
- [[kalman-filter]] — uses: BSTS uses the Durbin-Koopman simulation smoother at every MCMC iteration
- [[spike-and-slab]] — uses: spike-and-slab is the variable selection mechanism; this paper gives the most complete technical derivation in the cluster
- [[bayesian-model-averaging]] — uses: BMA emerges from MCMC averaging over γ draws; paper shows this produces sparse, interpretable predictor inclusion probabilities
- [[scott-varian-nowcasting-2013a]] — extends: this is the full journal paper; the 2013 conference version covers the same model with different examples
