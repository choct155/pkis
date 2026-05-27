---
id: "pkis:source:duncan-mskf-seemingly-unrelated-1993"
aliases: []
title: "Bayesian Forecasting for Seemingly Unrelated Time Series: Application to Local Government Revenue Forecasting"
authors: ["George Duncan", "Wilpen Gorr", "Janusz Szczypula"]
year: 1993
type: paper
domain: [time-series, forecasting, bayesian-stats]
tags: [kalman-filter, state-space-models, hierarchical-models, local-government, cross-sectional-pooling]
source_url: "https://www.jstor.org/stable/2632644"
drive_id: "1vdVJ3jKwoB-773H01pZpjn1pttAp9wqX"
drive_path: "PKIS/sources/papers/duncan-mskf-seemingly-unrelated-1993.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[kalman-filter]]", "[[state-space-models]]", "[[structural-time-series]]"]
---

## Summary

This paper develops C-MSKF (Cross-Sectionally Adjusted Multi-State Kalman Filter), a Bayesian method for forecasting "seemingly unrelated time series" — multiple parallel time series that share no direct cause-and-effect relationship but are jointly subject to the same external forces such as business cycles. The authors integrate two established Bayesian methods: the Multi-State Kalman Filter (MSKF), which handles structural change in individual series via a mixture of four state models (no change, step change, slope change, transient), and the Conditionally Independent Hierarchical Model (CIHM), which borrows strength across cross-sectional units by treating unit-level parameters as draws from a common distribution.

The C-MSKF alternates at each time step between an MSKF update for each series individually and a CIHM cross-sectional adjustment that shrinks each unit's estimate toward the cross-sectional mean, with weights inversely proportional to variance. This "borrow strength from neighbors" mechanism is especially valuable for short and volatile time series. The paper demonstrates the method on income tax collection data for forty school districts in Allegheny County, Pennsylvania, over 1972–1986, comparing C-MSKF to univariate MSKF. Results show C-MSKF is more accurate in 62% of cases, with advantages growing as time series shorten, forecast horizon increases, and economic cycle sensitivity rises.

## Key Knowledge Objects

- [[kalman-filter]] (technique, high) — recursive Bayesian state updating for dynamic linear models; the computational engine of MSKF
- [[state-space-models]] (framework, high) — dynamic linear model (DLM) formulation as observation + system equations; the structural backbone
- [[structural-time-series]] (framework, high) — decomposition of time series into level, trend, and transient components using state-space methods

## Key Extractions

1. **C-MSKF architecture**: At each time t, MSKF updates each unit's state separately (using a mixture of J=4 state DLMs), then CIHM adjusts each unit's posterior mean as a weighted average of the unit's own time series estimate and the cross-sectional mean — weight inversely proportional to variance.
2. **MSKF states**: Harrison and Stevens (1971) four-state mixture: no change (π=0.9), step change (π=0.003), slope change (π=0.003), and transient (π=0.094). Each state has different variance inflation factors R_ε, R_γ, R_ρ calibrated to respond at the right rate to each change type.
3. **CIHM update formula**: The cross-sectionally adjusted posterior mean is μ̂ᵢₜ = (μ₀Vᵢₜ + Tᵢₜτ²)/(Vᵢₜ + τ²), where μ₀ and τ² are ML estimates of the cross-sectional hyperparameters — intuitively, a precision-weighted average of the global mean and the unit's time-series estimate.
4. **Empirical findings**: C-MSKF outperforms MSKF most strongly for the "high sensitivity" school districts (near steel mills) during the 1981–82 recession, where cross-sectional correlation of the shock is most useful. For stable periods (1978 origin), both methods perform similarly.
5. **VAR comparison context**: The authors note that full multivariate VAR models require min-sample sizes of at least twice the series length, making them impractical for the 15-year school district data; C-MSKF sidesteps this by using hierarchical pooling rather than explicit covariance estimation.

## Connection Candidates

- [[kalman-filter]] — uses: C-MSKF uses Kalman filter as the recursive update step within each MSKF state
- [[bayesian-linear-regression]] — prerequisite-of: the CIHM adjustment is a Bayesian hierarchical regression; understanding BLR illuminates why the weighted-average formula arises
- [[directed-graphical-models]] — equivalent-in-context: the DLM state-space structure is equivalent to a dynamic Bayes net; edges are the state transition and observation equations
- [[var-models]] — contrasts-with: VAR requires explicit cross-variable covariance estimation; C-MSKF avoids this by using hierarchical pooling of univariate models
