---
title: "State-Space Models"
knowledge_type: framework
also_type: []
domain: [time-series, state-space-models, bayesian-stats]
tags: [latent-variables, dynamic-linear-models, hidden-markov-models, linear-gaussian, sequential-inference]
related_concepts: ["[[kalman-filter]]", "[[structural-time-series]]", "[[dynamic-factor-models]]", "[[directed-graphical-models]]"]
sources: ["[[duncan-mskf-seemingly-unrelated-1993]]", "[[scott-varian-nowcasting-2013a]]", "[[scott-varian-bsts-2014]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 3
understanding: 0
maturity: settled
---

A general framework for models of sequential data where observed outputs y_t are generated from unobserved latent states α_t, which evolve through time according to a Markovian transition distribution. In the linear-Gaussian special case (Dynamic Linear Model), both the observation equation y_t = Z_t^T α_t + ε_t and the transition equation α_{t+1} = T_t α_t + R_t η_t are linear with Gaussian noise, making the Kalman filter the optimal exact inference algorithm. A very large class of time series models — including all ARIMA and VARMA models — can be expressed in state-space form.

State-space models can be viewed as dynamic Bayesian networks: the latent state sequence (α_1, α_2, ...) forms a Markov chain, and observations y_t are conditionally independent given the states. This equivalence connects time series analysis to the broader graphical models literature.

## Reading Path
- [[duncan-mskf-seemingly-unrelated-1993]] (unread) — presents the DLM as the formal backbone of the MSKF; gives explicit recursive Kalman filter equations for the linear-Gaussian case
- [[scott-varian-bsts-2014]] (unread) — shows state-space modularity: any combination of components (trend, seasonal, regression) can be composed by concatenating observation vectors and arranging model matrices block-diagonally
- [[scott-varian-nowcasting-2013a]] (unread) — introduces state-space form for the BSTS nowcasting model; motivates the framework as encompassing ARIMA, structural decompositions, and regression components
