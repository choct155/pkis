---
aliases: []
authors: Shakir Mohamed, Mihaela Rosca, Michael Figurnov, Andriy Mnih
concepts: []
date_added: '2026-06-07'
date_updated: '2026-06-07'
doi: ''
domain:
- bayesian-stats
- optimization
- deep-learning
drive_id: ''
drive_path: ''
id: pkis:source:mohamed-monte-2020
source_url: https://jmlr.org/papers/v21/19-346.html
status: unread
tags:
- score-function-estimator
- log-derivative-trick
- REINFORCE
- reparameterization-trick
- gradient-estimation
- variational-inference
- policy-gradient
title: Monte Carlo Gradient Estimation in Machine Learning
type: paper
year: 2020
---

## Summary
Mohamed et al. (2020), Journal of Machine Learning Research. The definitive unified treatment of gradient estimation for stochastic computation graphs. Covers the score function estimator (log derivative trick), the reparameterization trick, and their relationship. Makes explicit that REINFORCE in RL and the score function gradient estimator in VI are the same mathematical object applied in different contexts. Essential reading for understanding why variational inference and policy gradient RL converge mathematically. This is the missing bridge between the VI cluster and the RL cluster in the research program.

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:technique:kernel-density-estimation
- pkis:technique:reparameterization-trick
- pkis:source:betancourt-hmcgeometric
- pkis:concept:privacy-in-ml
- pkis:source:sjolund-parametric-vi

## Reading Notes
READ BEFORE Sutton-Barto Ch13. Provides the unifying mathematical framework that makes Ch13 feel like a special case rather than a new concept. The score function estimator section directly resolves the log derivative trick gap identified in session 2026-06-07. Position in reading graph: bridges VI cluster 9 (blei-vi-review, sjolund) to new RL cluster. Prerequisite: ELBO mechanics (solid after today's session). Unlocks: Sutton-Barto Ch13, yellapragada-variational-bayes RL sections.