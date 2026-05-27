---
id: "pkis:framework:structural-time-series"
aliases: []
title: "Structural Time Series Models"
knowledge_type: framework
also_type: []
domain: [time-series, state-space-models, bayesian-stats]
tags: [state-space-models, harvey, basic-structural-model, local-linear-trend, trend-decomposition, seasonal]
related_concepts: ["[[kalman-filter]]", "[[state-space-models]]", "[[var-models]]"]
sources: ["[[duncan-mskf-seemingly-unrelated-1993]]", "[[scott-varian-nowcasting-2013a]]", "[[scott-varian-bsts-2014]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

A framework (Harvey 1989) for modeling time series by explicitly decomposing them into interpretable structural components — trend (level + slope), seasonal, cycle, and irregular terms — each expressed as a latent state variable evolving according to a stochastic transition equation. The full model is in state-space form and estimated via the Kalman filter. Unlike ARIMA, which fits a black-box polynomial filter, structural time series gives each component a direct economic interpretation and allows them to be estimated separately.

The canonical "basic structural model" (BSM) has: a local linear trend (μ_t = μ_{t-1} + δ_{t-1} + η_t, where δ_t = δ_{t-1} + ζ_t), a seasonal component constrained to sum to zero over a full cycle, and an observation error ε_t. Adding a regression component β^T x_t yields BSTS.

## Reading Path
- [[scott-varian-nowcasting-2013a]] (unread) — introduces the BSTS framework, presents the local linear trend model with stochastic level and slope, and integrates spike-and-slab regression
- [[scott-varian-bsts-2014]] (unread) — full technical exposition: state-space form equations, modular composition of components, Kalman filter/smoother details, and empirical decompositions
- [[duncan-mskf-seemingly-unrelated-1993]] (unread) — presents the DLM (dynamic linear model) as the state-space basis for the MSKF; comparable framework but in a multi-state mixture context
