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
- unbiasedness
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:concept:estimator-consistency
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch05
tags:
- consistency
- convergence-in-probability
- asymptotic-theory
- MLE
- unbiasedness
title: Statistical Estimator Consistency
understanding: 0
uses:
- maximum-likelihood-estimation
- cramer-rao-bound
- weak-law-of-large-numbers
---

## Definition
An estimator $\hat{\theta}_m$ is **consistent** (weakly) if it converges in probability to the true parameter value as the number of samples grows:

$$\operatorname{plim}_{m\to\infty}\hat{\theta}_m = \theta \quad\Leftrightarrow\quad \forall\,\epsilon>0,\; P(|\hat{\theta}_m-\theta|>\epsilon)\to 0.$$

**Strong consistency** requires almost sure convergence: $P(\lim_{m\to\infty}\hat{\theta}_m = \theta)=1$. Consistency implies that bias vanishes asymptotically, but the converse is false—an asymptotically unbiased estimator need not be consistent.

### Why it matters
Consistency is the minimal large-sample guarantee for an estimator. Maximum likelihood estimation is consistent under mild regularity conditions, which—combined with its statistical efficiency (achieving the Cramér–Rao lower bound asymptotically)—provides the principal theoretical justification for MLE as the default estimation strategy in machine learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[weak-law-of-large-numbers]] — uses
- [[cramer-rao-bound]] — uses
- [[unbiasedness]] — contrasts-with
- [[maximum-likelihood-estimation]] — uses
[To be populated during integration]