---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
contrasts-with:
- maximum-likelihood-estimation
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:result:laplaces-rule-of-succession
instantiates:
- bayesian-inference
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch03
tags:
- posterior-predictive
- uniform-prior
- add-one-smoothing
- beta-binomial
- prediction
title: Laplace's Rule of Succession
understanding: 0
---

## Definition
Having observed $F_a$ successes and $F_b$ failures in $F=F_a+F_b$ Bernoulli trials with a uniform prior on the success probability $p_a$, the predictive probability that the next trial succeeds is
$$P(a\mid s,F) = \int_0^1 p_a\, P(p_a\mid s,F)\, dp_a = \frac{F_a+1}{F_a+F_b+2}.$$
This is the posterior predictive obtained by integrating the per-outcome probability over the full posterior on $p_a$, not by plugging in a point estimate.

### Why it matters
It is the canonical posterior-predictive computation: prediction is done by *averaging over* parameter uncertainty. The '+1 / +2' shifts naive frequencies toward 1/2, so even after zero successes the next-trial probability is $1/(F+2)>0$ rather than 0 — the basis of add-one (Laplace) smoothing in language and compression models.

### Note
The predictive mean $\frac{F_a+1}{F_a+F_b+2}$ differs from the posterior mode (the MAP/MLE-style estimate $F_a/F$), illustrating that the Bayesian prediction is not the same as the most probable parameter value.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[maximum-likelihood-estimation]] — contrasts-with: predictive mean differs from MLE; averages over vs. maximizes the posterior
- [[bayesian-inference]] — instantiates: posterior-predictive integration is a worked instance of full Bayesian inference
[To be populated during integration]