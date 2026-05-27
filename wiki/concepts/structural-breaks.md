---
id: "pkis:concept:structural-breaks"
aliases: []
title: "Structural Breaks"
knowledge_type: concept
also_type: []
domain: [time-series, forecasting]
tags: [parameter-instability, regime-change, chow-test, quandt-andrews, cusum, nonstationarity]
related_concepts: ["[[var-models]]", "[[state-space-models]]", "[[structural-time-series]]"]
sources: ["[[lee-structural-breaks-2007]]", "[[stock-watson-leading-indicators-1992]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

A structural break is a change in the parameters (intercepts, slopes, variance terms) of a forecasting or statistical model at some point in time, typically due to a change in the economic environment, policy regime, institutions, or data-generating process. Structural breaks violate the parameter constancy assumption of classical regression and time series models, potentially causing systematic forecast failure.

Detection methods include: the Chow test (requires known break date), the Quandt-Andrews (QLR) test (unknown break date; takes the maximum Chow statistic over trimmed sample), the Andrews-Ploberger weighted average tests, and CUSUM analysis (cumulative sum of recursive residuals for continuous parameter stability monitoring). Remedies include differencing (which converts intercept breaks into blips), using state-space models with stochastic parameters, or explicitly modeling the break with a time-varying parameter specification.

## Reading Path
- [[lee-structural-breaks-2007]] (unread) — primary applied treatment: tests 10 DC withholding tax models for structural breaks using QLR and CUSUM; concludes that misspecified models are more likely to show breaks, and that models robust to breaks do not always forecast better
- [[stock-watson-leading-indicators-1992]] (unread) — the 1990 recession post-mortem illustrates the impact of structural breaks on leading indicator systems: the financial crisis changed the leading indicators' relationship to recessions, causing the XRI to fail
