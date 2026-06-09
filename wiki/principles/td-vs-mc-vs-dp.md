---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- optimization
id: pkis:principle:td-vs-mc-vs-dp
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch06
tags:
- sampling
- bootstrapping
- certainty-equivalence
- batch-updating
- prediction
- comparison
title: TD vs. Monte Carlo vs. Dynamic Programming
understanding: 0
uses:
- temporal-difference-learning
- maximum-likelihood-estimation
---

## Definition
A recurring organizing theme of reinforcement learning: temporal-difference, Monte Carlo, and dynamic-programming methods for the prediction problem differ along two independent axes — whether they *sample* the expectation and whether they *bootstrap* from other estimates — and TD occupies the cell that combines both.

## The two axes
The value function obeys $v_\pi(s) = \mathbb{E}_\pi[G_t \mid S_t=s] = \mathbb{E}_\pi[R_{t+1} + \gamma v_\pi(S_{t+1}) \mid S_t=s]$ (Eqs. 6.3–6.4). The three method families estimate it differently:
- **Monte Carlo** samples the expectation (uses a sample return $G_t$) but does *not* bootstrap (uses the full return as target).
- **Dynamic programming** bootstraps (target uses $V(S_{t+1})$) but does *not* sample — it takes an *expected update* over the complete distribution of successors, which requires a model.
- **TD** does both: it samples the expectation *and* bootstraps from the current estimate. Its target is an estimate for both reasons.
TD thus combines Monte Carlo's freedom from a model with DP's incremental bootstrapping.

## What each batch limit converges to
Under batch updating both TD(0) and constant-α MC converge deterministically, but to *different* answers:
- Batch **Monte Carlo** converges to the values minimizing mean-squared error on the training set (sample averages of observed returns).
- Batch **TD(0)** converges to the **certainty-equivalence estimate**: the value function that would be exactly correct for the **maximum-likelihood model** of the Markov process built from the data.
The "You are the Predictor" example (Ex. 6.4) makes the difference concrete: given the data, MC estimates $V(A)=0$ (zero training error) while TD estimates $V(A)=3/4$ (the Markov-model answer), and the TD answer generalizes better to future data because it exploits the Markov structure.

## Why TD tends to be faster
This explains TD's typical empirical speed advantage on stochastic tasks (e.g. the Random Walk MRP): batch TD computes the certainty-equivalence estimate, which is the more relevant optimum for predicting returns. Computing the certainty-equivalence estimate directly is usually infeasible (order $n^2$ memory and $n^3$ computation for $n$ states), yet TD approximates it with order-$n$ memory — often the only feasible route on large state spaces. No proof exists that either online method converges faster in general, but TD is usually found faster in practice.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[maximum-likelihood-estimation]] — uses: batch TD converges to the certainty-equivalence estimate of the maximum-likelihood Markov model
- [[temporal-difference-learning]] — uses: TD is one of the three method families compared along the sampling/bootstrapping axes
[To be populated during integration]