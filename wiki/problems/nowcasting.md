---
title: "Nowcasting"
knowledge_type: problem
also_type: []
domain: [time-series, forecasting]
tags: [contemporaneous-forecasting, leading-indicators, google-trends, central-banking, fat-regression]
related_concepts: ["[[structural-time-series]]", "[[kalman-filter]]", "[[spike-and-slab]]", "[[bayesian-model-averaging]]"]
sources: ["[[scott-varian-nowcasting-2013a]]", "[[scott-varian-bsts-2014]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: evolving
---

The problem of estimating the current value of an economic (or other) variable before it is officially released or finalized. Many economic time series are reported infrequently (monthly, quarterly) despite being theoretically observable on finer time scales, and are often revised after first release. Nowcasting exploits contemporaneous signals — such as Google search query data, financial prices, or other high-frequency series — to form an estimate of the current-period value of the target series as soon as possible.

The nowcasting problem differs from standard forecasting in that the signal arrives contemporaneously with (or after) the period being estimated, not in advance. This creates a "fat regression" problem when there are many potential predictors: the number of predictors may exceed the number of observations, requiring a sparse modeling approach (such as spike-and-slab priors or LASSO) to extract signal from noise.

## Reading Path
- [[scott-varian-nowcasting-2013a]] (unread) — introduces BSTS as a nowcasting system combining Kalman filtering, spike-and-slab regression, and BMA; illustrates with consumer sentiment and gun sales applications
- [[scott-varian-bsts-2014]] (unread) — full BSTS paper with nowcasting applications to initial unemployment claims and retail sales; demonstrates that Google Trends data helps predict turning points
