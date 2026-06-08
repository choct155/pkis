---
aliases: []
also_type: []
applies:
- bayesian-model-averaging
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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:concept:marginal-likelihood
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- bayesian-model-comparison
related_concepts: []
sources:
- mackay-itila-ch03
specializes:
- bayesian-inference
tags:
- evidence
- model-comparison
- normalizing-constant
- bayes-theorem
- occams-razor
title: Marginal Likelihood (Model Evidence)
understanding: 0
uses:
- conjugate-prior
- occam-factor
---

## Definition
The probability of the observed data under a model $H$, with all parameters integrated out:
$$P(D \mid H) = \int P(D \mid \theta, H)\, P(\theta \mid H)\, d\theta.$$
It is the denominator (normalizing constant) of parameter-level Bayesian inference and simultaneously the *evidence* the data lend to the model as a whole. MacKay's key observation: 'the evidence for a model is usually the normalizing constant of an earlier Bayesian inference' — the same integral that normalized $P(\theta\mid D,H)$ scores $H$.

### Automatic Occam's razor
Because the integral averages the likelihood over the *whole* prior — not just its peak — a model that spreads probability over many parameter values pays a cost in evidence for the regions the data rule out. A flexible model can never win by much, but the simpler model can lose by a large margin.

### Computing it
For the bent coin with a uniform prior, the evidence is the Beta integral $P(s\mid F,H_1)=\frac{F_a!\,F_b!}{(F_a+F_b+1)!}$. It is closed-form here but generally intractable, motivating Laplace approximation and Monte Carlo methods.

### Why it matters
Evidence is what makes Bayesian model comparison automatic: it requires no ad hoc estimators or significance tests, only the probability of the data under each hypothesis.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[occam-factor]] — uses: Under Laplace's method the marginal likelihood decomposes into best-fit likelihood times the Occam factor.
- [[conjugate-prior]] — uses: conjugacy (Beta-Binomial) yields the closed-form Beta-integral evidence in the bent-coin example
- [[bayesian-inference]] — specializes: the evidence is the normalizing constant of the parameter-level posterior
- [[bayesian-model-averaging]] — applies: model evidence supplies the posterior model weights P(H|D) used in BMA
- [[bayesian-model-comparison]] — prerequisite-of: evidence must be computable to compare models
[To be populated during integration]