---
title: "Business Cycle Modeling Without Pretending to Have Too Much A Priori Economic Theory"
authors: ["Thomas J. Sargent", "Christopher A. Sims"]
year: 1977
type: paper
domain: [time-series, forecasting]
tags: [macroeconometrics, var-models, factor-models, index-models, identification, business-cycles]
source_url: ""
drive_id: "1-G9Ig4PaNgYM7WS2c3jFSbd-70u5g2Ps"
drive_path: "PKIS/sources/papers/sargent-sims-business-cycle-1977.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[var-models]]", "[[dynamic-factor-models]]"]
---

## Summary

This foundational working paper (Federal Reserve Bank of Minneapolis, 1977) argues that standard large-scale macroeconometric models impose unjustifiable identifying restrictions — zero restrictions on coefficients, exogeneity assumptions, and uncorrelated residual assumptions — amounting to "measurement without theory" (Koopmans). The authors propose instead modeling macroeconomic variables as general vector stochastic processes, treating all variables symmetrically and imposing only restrictions that are empirically testable or theoretically minimal.

The paper develops and applies two related classes of "index models": (1) **unobservable index models**, where aggregate economic fluctuations are driven by k latent factors (analogous to factor analysis but in the frequency domain), and (2) **observable index models**, where the driving factors are observable combinations of macroeconomic variables. These are operationalized via spectral/frequency-domain factor analysis, with the "one-index" model capturing the NBER notion that business cycle fluctuations are "essentially one-dimensional." The paper presents empirical applications fitting a six-variable monthly U.S. macro model, estimating the degree to which a single index accounts for co-movement, and testing the validity of various identification schemes. This paper is the direct precursor to VAR analysis: by relaxing over-identification, it argues that reduced-form vector autoregressions provide a more defensible foundation for macroeconomic analysis than structural models with contested identifying restrictions.

## Key Knowledge Objects

- [[var-models]] (framework, high) — Vector AutoRegression: modeling n time series as functions of each other's lags with no a priori zero restrictions; the general form advocated here as alternative to structural models
- [[dynamic-factor-models]] (framework, high) — unobservable index model: k latent common factors driving comovements in n observed time series; frequency-domain implementation of factor analysis for time series

## Key Extractions

1. **Core critique**: Standard simultaneous-equations macro models impose identifying restrictions (zero coefficients, exogeneity classifications, uncorrelated residuals) that are "not deduced from an appeal to optimizing behavior or any other economic theory." The authors argue for symmetric, data-based restrictions instead.
2. **Index model specification**: y ≈ a*z + u where y is n×1 observed, z is k×1 (k<<n) common indexes, u is the idiosyncratic residual vector assumed to have small diagonal elements relative to the common component. The "good fit" criterion: each u_i has small variance relative to corresponding y_i at all frequencies.
3. **Observable vs. unobservable index**: When z is observable (a function of current/lagged x), orthogonality of z and u identifies the system. When z is latent, requiring mutual orthogonality of u components provides identification — equivalent to the factor analysis identification condition.
4. **Empirical application**: Using a 6-variable monthly U.S. macro data set, they test whether a single-index model fits well. The result supports a roughly one-dimensional description of business cycle comovements — consistent with the NBER reference cycle concept.
5. **Connection to VAR**: The paper shows that "if one wants to allow all the variables to interact dynamically with one another and their own lags, one needs a model with about ten equations and ten lags." The resulting near-unrestricted VAR is the logical conclusion of the argument.

## Connection Candidates

- [[var-models]] — introduces: this paper is one of the founding documents motivating VAR analysis in macroeconomics
- [[dynamic-factor-models]] — introduces: the unobservable index model is an early formulation of the dynamic factor model
- [[directed-graphical-models]] — contrasts-with: standard structural macroeconometric models are causal DAGs with contested zero restrictions; this paper argues for fewer such restrictions
- [[em-algorithm]] — uses: frequency-domain factor analysis (Geweke's algorithm referenced here) is analogous to EM for factor models in the frequency domain
