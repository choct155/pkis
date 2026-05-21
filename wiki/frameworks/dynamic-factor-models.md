---
title: "Dynamic Factor Models"
knowledge_type: framework
also_type: []
domain: [time-series, forecasting]
tags: [factor-analysis, latent-variables, dimensionality-reduction, macroeconometrics, state-space-models]
related_concepts: ["[[var-models]]", "[[state-space-models]]", "[[kalman-filter]]", "[[principal-component-analysis]]"]
sources: ["[[sargent-sims-business-cycle-1977]]", "[[stock-watson-leading-indicators-1992]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

A framework for modeling high-dimensional time series by positing that all observed comovements arise from k << n common latent factors (indexes), plus idiosyncratic components: y_t = Λ f_t + u_t, where f_t is the k×1 factor vector, Λ is the n×k loading matrix, and u_t is an idiosyncratic vector with diagonal (or nearly diagonal) cross-series covariance. The "dynamic" aspect means the factors f_t follow their own stochastic process (often a VAR), so the model captures temporal dynamics as well as cross-sectional comovements.

Sargent-Sims (1977) introduced the "unobservable index model" in the frequency domain as the time series counterpart of classical factor analysis. Stock-Watson (1989, 1992) implemented a state-space version estimated via the Kalman filter — the single-index model in which Δc_t is the latent common factor for U.S. coincident economic indicators. Dynamic factor models are closely related to principal components (which extract static factors) and to structural VARs (which impose explicit economic identification on the factors).

## Reading Path
- [[sargent-sims-business-cycle-1977]] (unread) — introduces the unobservable index model as a frequency-domain factor analysis; foundational theoretical treatment motivating the approach as an alternative to over-identified structural models
- [[stock-watson-leading-indicators-1992]] (unread) — single-index dynamic factor model implemented in state-space form via Kalman filter; used to construct XCI/XLI/XRI experimental recession indexes
