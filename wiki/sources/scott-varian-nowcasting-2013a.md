---
title: "Bayesian Variable Selection for Nowcasting Economic Time Series"
authors: ["Steven L. Scott", "Hal R. Varian"]
year: 2013
type: paper
domain: [time-series, forecasting, bayesian-stats]
tags: [nowcasting, google-trends, spike-and-slab, state-space-models, variable-selection, fat-regression]
source_url: ""
drive_id: "1mDuFfFZoUxh7wUxTPeCSGYuM17BlQ1wy"
drive_path: "PKIS/sources/papers/scott-varian-nowcasting-2013a.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[structural-time-series]]", "[[kalman-filter]]", "[[spike-and-slab]]", "[[bayesian-model-averaging]]", "[[nowcasting]]"]
---

## Summary

This paper presents BSTS (Bayesian Structural Time Series), a system for nowcasting economic time series when predictors outnumber observations — the "fat regression" problem. BSTS integrates three Bayesian methods: (1) a structural time series model (local linear trend with optional seasonality) estimated via the Kalman filter; (2) spike-and-slab regression for variable selection, which places a mixture prior with a point mass at zero on each regression coefficient; and (3) Bayesian model averaging across the posterior, so forecasts automatically account for predictor uncertainty.

The paper motivates the problem using Google Trends data: with 151 query categories for ~100 months of consumer sentiment data, conventional regression is infeasible. The BSTS system decomposes this into a Gibbs sampler that alternates between sampling the latent state vector α (via the Kalman smoother), sampling the spike-and-slab regression parameters (γ, β, σ²), and updating the state variances. Applied to consumer sentiment and gun sales (NICS background check data), BSTS achieves ~14% improvement in one-step-ahead MAE over a naive AR(1) model. The key innovation is the modular integration: the Kalman filter handles temporal dynamics while spike-and-slab handles high-dimensional predictor selection, and the two cooperate naturally because conditional on the latent state α, the regression is a standard linear problem.

## Key Knowledge Objects

- [[structural-time-series]] (framework, high) — the "basic structural model" (BSM): local linear trend + seasonal + regression in state-space form; the time-series backbone of BSTS
- [[kalman-filter]] (technique, high) — used for state estimation, smoothing, and sampling in the Gibbs algorithm; described via the DLM observation and transition equations
- [[spike-and-slab]] (technique, high) — spike-and-slab prior for variable selection: point mass at zero (spike) plus continuous slab; enables probabilistic variable selection and posterior inclusion probabilities
- [[bayesian-model-averaging]] (technique, high) — automatic ensemble averaging over predictor subsets as a by-product of MCMC over γ; each draw from posterior is a different model
- [[nowcasting]] (problem, high) — the challenge of estimating a current-period economic value before official data are released, using contemporaneous signals

## Key Extractions

1. **Local linear trend model**: y_t = μ_t + z_t + v_t; μ_t = μ_{t-1} + b_{t-1} + w_{1t}; b_t = b_{t-1} + w_{2t}; z_t = βx_t. The random-walk level and slope allow the model to track structural changes without assuming stationarity.
2. **Spike-and-slab prior**: γ_i ~ Bernoulli(π_i); if γ_i = 1, β_γ|γ,σ² ~ N(b_γ, σ²Ω_γ⁻¹) with Zellner g-prior Ω⁻¹ ∝ X^TX. The prior inclusion probability π can be set by specifying expected model size k/K.
3. **Gibbs sampler structure**: Alternate (1) sample α|θ,β,γ,y via Durbin-Koopman simulation smoother; (2) sample γ|α,y via SSVS; (3) sample β,σ²|γ,α,y in closed form; (4) sample state variances|α,y via conjugate Gamma.
4. **Consumer sentiment result**: Top predictor by inclusion probability is "Financial Planning" (included in ~100% of models). BSTS achieves MAE ~4.5% vs. AR(1) MAE ~5.2% — 14% improvement.
5. **Gun sales result**: BSTS identifies "gun stores" as by far the best predictor (from 585 Trends verticals), cutting in-sample MAE from 0.34 to 0.15 — a 56% reduction.

## Connection Candidates

- [[structural-time-series]] — uses: BSTS is an implementation of structural time series with added spike-and-slab regression component
- [[kalman-filter]] — uses: BSTS uses the Kalman filter/smoother at each Gibbs iteration to sample the latent state vector
- [[spike-and-slab]] — uses: BSTS uses spike-and-slab as the variable selection mechanism within the regression component
- [[bayesian-model-averaging]] — uses: BMA emerges automatically from the MCMC by averaging over posterior draws of γ
- [[nowcasting]] — addresses: BSTS was designed specifically for the nowcasting problem with many contemporaneous predictors
