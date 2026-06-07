---
aliases: []
authors: Richard S. Sutton, Andrew G. Barto
concepts: []
date_added: '2026-06-07'
date_updated: '2026-06-07'
doi: ''
domain:
- optimization
- deep-learning
- bayesian-stats
drive_id: ''
drive_path: ''
id: pkis:source:sutton-policy-2018
parent_book: pkis:source:sutton-reinforcement-2018
source_url: ''
status: unread
tags:
- reinforcement-learning
- policy-gradient
- REINFORCE
- score-function
- log-derivative-trick
- entropy-regularization
- actor-critic
- variance-reduction
- baseline
title: Policy Gradient Methods (Sutton & Barto Ch. 13)
type: paper
year: 2018
---

## Summary
Canonical treatment of policy gradient methods in RL. Derives the policy gradient theorem from first principles. Introduces REINFORCE as the baseline Monte Carlo policy gradient algorithm. Develops the log derivative trick (score function estimator) as the mechanism for computing gradients of expectations over stochastic policies. Covers baselines for variance reduction and the actor-critic architecture.

## Key Knowledge Objects
[To be identified during ingest]

## Key Extractions
[To be identified during ingest]

## Connection Candidates
- pkis:source:hastie-esl
- pkis:technique:reparameterization-trick
- pkis:source:hastie-esl-ch10
- pkis:source:yellapragada-variational-bayes
- pkis:source:deisenroth-mml-ch07

## Reading Notes
READ AFTER Mohamed et al. (2020) which provides the unifying framework. Key connections to existing wiki clusters: (1) Log derivative trick = score function estimator in VI — same math, different notation. Resolves identified RL foundations gap from 2026-06-07 session. (2) REINFORCE update rule is structurally identical to ELBO gradient estimator under reparameterization trick. (3) Entropy regularization in policy gradient = entropy term in ELBO — maximum entropy RL and VI are the same objective in different notation. (4) Baseline subtraction = control variates in VI gradient estimation. Position in reading graph: prerequisite for variational-graph-traversal hypothesis RL formalization. Unlocks: actor-critic methods, SAC, the RL side of the premature-concentration bridge note.