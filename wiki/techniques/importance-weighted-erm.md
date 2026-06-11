---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:technique:importance-weighted-erm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
tags:
- covariate-shift
- density-ratio
- domain-adaptation
- robust-learning
title: Importance-Weighted Empirical Risk Minimization
understanding: 0
---

## Definition
$$\hat{R}_w(f, D^s) = \frac{1}{N}\sum_{n=1}^N w(x_n)\,\ell(f(x_n), y_n), \quad w(x) = \frac{q(x)}{p(x)}$$

Importance-weighted ERM reweights each source training loss by the density ratio $w(x)=q(x)/p(x)$ so that the weighted empirical risk is an unbiased estimator of the target risk $R(f, q)$ under the covariate shift assumption.

### Why it matters
It is the principled, consistent estimator for the target risk given only labeled source data and (unlabeled) target data, provided $\operatorname{supp}(q) \subseteq \operatorname{supp}(p)$. The density ratio can be estimated without explicitly fitting two density models by training a binary classifier to distinguish source from target samples; the log-odds of that classifier equal $\log w(x)$.

### Practical estimation of weights
If a logistic classifier is trained with $c=-1$ for source and $c=+1$ for target, then $w(x_n) = \exp(h(x_n))$ where $h$ is the logit output. Weights are plugged directly into the mini-batch gradient computation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]