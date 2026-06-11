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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- decision theory
generalizes:
- maximum-a-posteriori-estimation-map
- bayesian-point-estimation
id: pkis:concept:posterior-risk
instantiates:
- statistical-decision-theory
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch34
specializes:
- expected-loss
tags:
- posterior
- loss function
- Bayes estimator
- risk
title: Posterior Risk (Posterior Expected Loss)
understanding: 0
uses:
- bayesian-inference
---

## Definition
$$\rho_\pi(a|x) \triangleq \mathbb{E}_{p_\pi(h|x)}[\ell(h, a)] = \int \ell(h, a)\, p_\pi(h|x)\, dh$$

The posterior risk is the expected loss of taking action $a$ averaged over the posterior distribution of the state of nature given the observed data $x$. The Bayesian optimal action minimises this quantity pointwise for each $x$.

### Why it matters
Provides a constructive recipe for any decision problem: compute the posterior, then minimise expected loss. It is the building block linking Bayesian inference to action selection, and it subsumes MAP estimation (0-1 loss) and MMSE estimation (squared-error loss) as special cases.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-point-estimation]] — generalizes
- [[maximum-a-posteriori-estimation-map]] — generalizes
- [[expected-loss]] — specializes
- [[bayesian-inference]] — uses
- [[statistical-decision-theory]] — instantiates
[To be populated during integration]