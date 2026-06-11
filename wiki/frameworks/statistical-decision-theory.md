---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- decision theory
- machine learning
extends:
- wald-decision-theory
id: pkis:framework:statistical-decision-theory
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch34
tags:
- decision theory
- loss function
- Bayesian
- frequentist
- risk
- admissibility
title: Statistical Decision Theory (Bayesian & Frequentist)
understanding: 0
uses:
- bayesian-inference
- expected-loss
- admissibility
- maximum-expected-utility-principle
- minimax-criterion
---

## Definition
$$\delta^*(\cdot) = \operatorname*{arg\,min}_{\delta} R(\delta), \quad R(\delta) = \mathbb{E}[\ell(h, \delta(X))]$$

An agent chooses an action $a \in \mathcal{A}$ given data $x$, a state of nature $h \in \mathcal{H}$, and a loss function $\ell(h,a)$; the optimal *policy* $\delta^*(x)$ minimises expected loss. The frequentist approach fixes $h$ and averages over data (frequentist risk); the Bayesian approach fixes the data and averages the posterior over $h$ (posterior risk). The Bayesian decision $\delta^*(x) = \arg\min_{a}\mathbb{E}_{p(h|x)}[\ell(h,a)]$ is constructive and simultaneously minimises the Bayes (integrated) risk.

### Why it matters
Unifies estimation, classification, regression, and sequential decisions under a single framework; shows that Bayesian estimators are admissible and that every admissible estimator is Bayes with respect to some prior (Wald's theorem).

### Key loss–estimator correspondences
| Loss | Optimal estimator |
|---|---|
| 0-1 | MAP (posterior mode) |
| Squared error | Posterior mean (MMSE) |
| Hamming | Max posterior marginals (MPM) |

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[minimax-criterion]] — uses
- [[maximum-expected-utility-principle]] — uses
- [[wald-decision-theory]] — extends
- [[admissibility]] — uses
- [[expected-loss]] — uses
- [[bayesian-inference]] — uses
[To be populated during integration]