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
- decision-theory
- statistics
- machine-learning
id: pkis:concept:loss-function-posterior-expected-loss
instantiates:
- expected-utility-theory
- decision-theory-foundations
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch05
specializes:
- expected-loss
tags:
- loss
- risk
- posterior
- decision-theory
- bayesian
title: Loss Function and Posterior Expected Loss
understanding: 0
uses:
- bayesian-inference
- maximum-expected-utility-principle
---

## Definition
$$\rho(a|x) \triangleq \mathbb{E}_{p(h|x)}[\ell(h,a)] = \sum_{h \in \mathcal{H}} \ell(h,a)\, p(h|x)$$

The loss function $\ell(h,a)$ encodes the cost incurred when action $a$ is taken and the true state of nature is $h$; the **posterior expected loss** (also called the **Bayes risk**) averages that cost over the posterior distribution of hidden states given observed evidence.

### Why it matters
It is the fundamental quantity minimized by the Bayes-optimal decision rule: any coherent decision procedure must minimize this quantity rather than, say, the maximum possible loss or the loss at a point estimate. The construction makes explicit that good decisions require both a probabilistic model of the world *and* a specification of preferences over outcomes — two separable concerns.

### Connection to utility
An equivalent formulation uses a utility function $U(h,a) = -\ell(h,a)$; the optimal policy then maximizes expected utility (see `maximum-expected-utility-principle`). The loss matrix (a table of $\ell(h,a)$ values) is the practitioner's primary design artifact in Bayesian decision analysis.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[expected-loss]] — specializes
- [[decision-theory-foundations]] — instantiates
- [[maximum-expected-utility-principle]] — uses
- [[expected-utility-theory]] — instantiates
- [[bayesian-inference]] — uses
[To be populated during integration]