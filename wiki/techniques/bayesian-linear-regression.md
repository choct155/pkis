---
title: "Bayesian Linear Regression"
knowledge_type: technique
also_type: []
domain: [bayesian-stats, statistical-learning]
tags: [probability-theory, linear-algebra]
related_concepts: ["[[conjugate-prior]]", "[[gaussian-distribution]]", "[[probability-theory]]", "[[logistic-regression]]"]
sources: ["[[deisenroth-mml]]", "[[steel-bma-forecasting-2011]]", "[[scott-varian-bsts-2014]]", "[[kroese-statistical-modeling]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 4
understanding: 0
maturity: settled
---

Linear regression under a full Bayesian treatment: places a prior over weights, computes the posterior analytically (via Gaussian conjugacy), and produces a predictive distribution over outputs rather than a point estimate — naturally regularizing and quantifying predictive uncertainty.

## Reading Path
- [[deisenroth-mml]] (unread) — foundational treatment: Gaussian conjugacy, prior/posterior update equations, marginal likelihood, predictive distribution
- [[steel-bma-forecasting-2011]] (unread) — the g-prior (Zellner 1986) for BLR in the context of variable selection; covers how the marginal likelihood closes in closed form under Gaussian-inverse-Gamma conjugacy
- [[scott-varian-bsts-2014]] (unread) — the slab component of spike-and-slab is a Zellner g-prior BLR; shows closed-form posterior for β_γ and σ² conditional on γ and latent state α
- [[kroese-statistical-modeling-ch08]] (unread) — Bayesian normal linear model with full conjugate posterior derivation including marginal posterior for σ²
