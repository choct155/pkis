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
contrasts-with:
- maximum-likelihood-estimation
- credible-interval
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:bayesian-point-estimation
instantiates:
- bayesian-inference
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- credible-interval
related_concepts: []
sources:
- jaynes-probability-ch06
tags:
- point-estimate
- posterior-mean
- posterior-median
- posterior-mode
- loss-function
- decision-theory
title: Bayesian Point Estimation (Mean, Median, Mode)
understanding: 0
uses:
- expected-loss
---

## Definition
Given a posterior pdf $p(\alpha\mid D I)$, a **point estimate** is a single number $\alpha^*(D,I)$ summarizing it. Jaynes (Ch. 6, §6.4) stresses that there is no unique "right" estimate — the choice is a decision-theory question (which loss function to minimize) layered on top of inference — and the three standard summaries correspond to three loss functions:

- **Posterior mean** $\alpha^*=\langle\alpha\rangle=\int \alpha\,p(\alpha\mid DI)\,d\alpha$ minimizes the *expected squared error*; the achieved minimum equals the posterior variance. This is Gauss/Legendre least squares read over the posterior.
- **Posterior median** $\alpha^+$ (where $P(\alpha>\alpha^+\mid DI)=1/2$) minimizes the *expected absolute error* — Laplace's "most advantageous" estimate.
- **Posterior mode** $\hat\alpha$ (the peak) corresponds to a 0–1 loss; with a locally flat prior it coincides with the **maximum-likelihood estimate**.

### Selection criteria
Jaynes argues the mean is easy to compute and good for sharp symmetric posteriors, but it is *sensitive to the tails* ("one very rich man in a poor village pulls the average far from anything representative") and is *not invariant under reparameterization*: in general $\lambda(\langle\alpha\rangle)\ne\langle\lambda(\alpha)\rangle$, so changing the parameter silently changes what counts as a good estimate. The median and all percentiles *are* reparameterization-invariant and *robust* to tail variations (an error twice as large is twice, not four times, as serious). Computers make the median/quartiles as cheap as moments, so the historical preference for least squares is now only "the force of long habit."

### Worked contrast (particle counter)
The same posterior gives strikingly different point estimates depending on rule and prior: with counter efficiency $\phi=0.1$, source strength $s=100$ and $c=15$ counts observed, the MLE/mode is $\hat n=c/\phi=150$ but the posterior-mean estimate is only $\langle n\rangle=c+s(1-\phi)=105$ — because the prior $p(n\mid s)$ pulls the estimate back. "If you see $k$ more counts than you should have, that is evidence for only $k$ more particles, not $10k$."

## Reading Path
- [[jaynes-probability-ch06]] — §6.4: mean/median/mode, loss functions, invariance and robustness; particle-counter Bayes-vs-MLE contrast

## Connections
- [[credible-interval]] — prerequisite-of
- [[credible-interval]] — contrasts-with
- [[bayesian-inference]] — instantiates
- [[maximum-likelihood-estimation]] — contrasts-with
- [[expected-loss]] — uses
- [[expected-loss]] — uses: the choice of point estimate is the minimizer of an expected loss (squared, absolute, or 0–1) over the posterior.
- [[maximum-likelihood-estimation]] — contrasts-with: the posterior mode equals the MLE only under a locally flat prior; the mean and median generally differ from it.
- [[bayesian-inference]] — instantiates: extracting a point estimate is a downstream summary of the full posterior.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]