---
title: "A Procedure for Predicting Recessions with Leading Indicators: Econometric Issues and Recent Experience"
authors: ["James H. Stock", "Mark W. Watson"]
year: 1992
type: paper
domain: [time-series, forecasting]
tags: [leading-indicators, recession-forecasting, dynamic-factor-models, kalman-filter, business-cycles, recession-index]
source_url: ""
drive_id: "1MV7OHMvQYpZZMhaZm4QJTJgW_hQ-gdN4"
drive_path: "PKIS/sources/papers/stock-watson-leading-indicators-1992.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[dynamic-factor-models]]", "[[kalman-filter]]", "[[var-models]]"]
---

## Summary

This NBER working paper develops and evaluates a probabilistic recession forecasting system built on a dynamic single-index model (Sargent-Sims 1977 architecture). The paper constructs three experimental indexes: XCI (coincident), XLI (leading, 6-month growth forecast), and XRI (recession probability index). The XRI estimates P(economy in recession 6 months hence) using stochastic simulation: the Kalman filter generates a conditional distribution for the unobserved state variable Δc_t (growth in the composite coincident index), and Monte Carlo integration then computes the probability that the future path of Δc_t falls in one of two defined recessionary patterns.

A recession is defined as Δc_t falling below a threshold b_{r,t} for 6 consecutive months, or 7 of 9 consecutive months (including first and last). The threshold is itself treated as random — distributed N(μ_b, σ²_b) — reflecting uncertainty in what constitutes a recession under NBER committee-style judgment.

The paper's empirical focus is the 1990 recession. The XLI performed well through September 1990 (forecasting +0.4% vs. actual −0.8% decline in XCI), but failed to forecast the sharp October-November collapse. The authors examine 45 individual indicators and find almost all failed to forecast the 1990 downturn, attributing this partly to the unusual nature of the recession (not driven by tight monetary policy, so financial variables — typically the strongest leading indicators — gave weak signals).

## Key Knowledge Objects

- [[dynamic-factor-models]] (framework, high) — single-index dynamic factor model: unobserved state c_t drives comovements among coincident variables; leading indicators predict future c_t; fitted via Kalman filter
- [[kalman-filter]] (technique, high) — used to compute the conditional distribution of the latent state and to produce one-step-ahead forecasts; central computational engine for the XCI/XLI/XRI system
- [[var-models]] (framework, moderate — could be technique) — the leading-indicator system augments the single-index model with a VAR for Δx_t and y_t; used to form forecasts of future c_t for the recession probability computation

## Key Extractions

1. **Single-index model structure**: Δx_{it} = γ_i(L)Δc_t + d_i(L)u_{it}, where u_{it} is idiosyncratic and mutually uncorrelated. One element of γ_i(L) is set to a scalar to fix timing of c_t. This is Sargent-Sims 1977 implemented for coincident variable forecasting.
2. **Recession definition as pattern recognition**: Rather than using a Markov-switching model (Hamilton 1989) where recession is intrinsic to the process, Stock-Watson treat recession classification as a pattern applied to any realization of c_t. This makes the approach applicable even if the data-generating process is linear and Gaussian.
3. **Monte Carlo integration for P(recession)**: (i) Compute N(m_{r|t}, Ω_{r|t}) for c_{r}(-8,8) from Kalman filter; (ii) draw pseudo-random realizations; (iii) draw random thresholds b_r, b_e from their distribution; (iv) evaluate recessionary pattern; (v) compute probability as fraction of draws classified as recession.
4. **1990 recession post-mortem**: Financial variables (interest rate spreads, stock prices) are normally strong leading indicators but gave weak recession signals in 1990 because the recession was not associated with tight monetary policy. Housing permits, consumer expectations, and help-wanted advertising did signal the downturn, but these were not included in the experimental index.
5. **Lesson on indicator robustness**: No single indicator or composite reliably forecasts all recessions — the structural cause of each recession differs, so the relevant leading indicators differ too.

## Connection Candidates

- [[dynamic-factor-models]] — implements: the Stock-Watson XCI/XLI/XRI system is a specific implementation of the Sargent-Sims unobservable single-index model
- [[kalman-filter]] — uses: Kalman filter is the computational engine for state estimation and forecasting in the single-index model
- [[sargent-sims-business-cycle-1977]] — extends: Stock-Watson implement and empirically evaluate the unobservable index model proposed by Sargent-Sims
- [[structural-breaks]] — deepens: failure of the XRI in 1990 is attributed to structural change in the relationship between leading indicators and recessions during a non-monetary recession
