---
id: "pkis:framework:var-models"
aliases: ["VAR"]
title: "Vector Autoregression (VAR) Models"
knowledge_type: framework
also_type: []
domain: [time-series, forecasting]
tags: [macroeconometrics, impulse-response, granger-causality, identification, reduced-form]
related_concepts: ["[[dynamic-factor-models]]", "[[structural-breaks]]", "[[state-space-models]]"]
sources: ["[[sargent-sims-business-cycle-1977]]", "[[lee-structural-breaks-2007]]", "[[stock-watson-leading-indicators-1992]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

A multivariate time series framework in which each variable in a system is modeled as a linear function of its own lags and the lags of all other variables, with no a priori zero restrictions on cross-variable effects. The reduced-form VAR: y_t = A_1 y_{t-1} + ... + A_p y_{t-p} + ε_t, where y_t is n×1, each A_i is n×n, and ε_t ~ N(0, Σ). The VAR treats all variables symmetrically — none is exogenous a priori — and avoids the contested identification assumptions of structural simultaneous-equations models.

VARs are the direct empirical counterpart of Sargent-Sims (1977)'s argument against over-identification: if one cannot defend the zero restrictions in structural models, the reduced form VAR is the honest starting point. Structural VARs (SVARs) add identifying restrictions post-estimation to recover structural shocks and impulse-response functions.

## Reading Path
- [[sargent-sims-business-cycle-1977]] (unread) — motivating argument: existing macro models impose unjustifiable restrictions; VAR-like symmetric modeling is the defensible alternative; this paper is VAR's intellectual origin
- [[stock-watson-leading-indicators-1992]] (unread) — uses a single-index model (close cousin of VAR) with leading indicators for recession probability; the Sargent-Sims framework applied for forecasting
- [[lee-structural-breaks-2007]] (unread) — tests a single-equation VAR specification (Model 10) for structural breaks alongside simpler models; provides empirical comparison in a forecasting context
