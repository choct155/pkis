---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:posterior-predictive-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch01
- gelman-bda3-ch03
- gelman-bda3-ch06
tags:
- bayesian
- prediction
- posterior
- marginalization
- model-checking
title: Posterior Predictive Distribution
understanding: 0
---

## Definition
$$p(\tilde{y}\mid y) = \int p(\tilde{y}\mid\theta)\,p(\theta\mid y)\,d\theta.$$
The distribution of a new observable $\tilde{y}$ after seeing data $y$ — an average of the data model over the posterior of $\theta$, so predictive uncertainty folds in parameter uncertainty rather than plugging in a single estimate.

The name is descriptive: *posterior* because it conditions on the observed $y$, *predictive* because it concerns a quantity that is itself observable. The final equality $p(\tilde{y}\mid\theta,y)=p(\tilde{y}\mid\theta)$ uses the conditional independence of $y$ and $\tilde{y}$ given $\theta$.

### Contrast with plug-in prediction
A frequentist plug-in predictor uses $p(\tilde{y}\mid\hat\theta)$ at a point estimate $\hat\theta$, understating uncertainty. The posterior predictive integrates over the whole posterior, so it is wider and properly calibrated when the model holds. In simulation it is trivial: for each posterior draw $\theta^s$, draw $\tilde{y}^s\sim p(\tilde{y}\mid\theta^s)$; the collection $\{\tilde{y}^s\}$ is a sample from $p(\tilde{y}\mid y)$.

### Role in model checking
Replicated data drawn from the posterior predictive can be compared with the observed data: systematic discrepancies between simulated and real data signal model misfit. This makes the posterior predictive the workhorse of Bayesian model checking, not merely forecasting.

### Why it matters
Prediction is frequently the actual goal of an analysis, and the posterior predictive is the only fully Bayesian answer — it propagates every source of uncertainty into statements about future observables, and it doubles as the engine for checking whether a fitted model could plausibly have generated the data at hand.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]