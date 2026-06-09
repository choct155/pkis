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
- statistical-learning
id: pkis:concept:ancillary-statistic
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch08
specializes:
- sampling-theory
tags:
- ancillarity
- conditioning
- likelihood
- configuration
- fisher
- sampling-theory
title: Ancillary Statistic
understanding: 0
uses:
- logical-vs-causal-independence
---

## Definition
An ancillary statistic z(x_1,...,x_n) is a function of the data whose sampling distribution is free of the parameter theta: p(z|theta I) = p(z|I). Fisher (1934) introduced ancillaries to repair an anomaly in orthodox estimation. Choosing an estimator theta*(x) collapses the data to a single number, so two data sets with the same estimate but very different configurations (range, clustering, higher moments) are treated as equally accurate when accuracy is judged by the width of the estimator's sampling distribution. Fisher's remedy was to report sampling distributions conditional on an ancillary z that captures the otherwise-discarded configuration; in general up to (n-1) ancillaries are needed, and they often fail to exist because of the required theta-independence.

## Jaynes' Bayesian dissolution
Jaynes shows the device accomplishes nothing for inference. Writing p(D|z theta I) = p(D|theta I) p(z|D theta I)/p(z|theta I), and noting that when z = z(D) is a function only of the data, p(z|D theta I) is a delta function delta[z - z(D)], the theta-independence p(z|theta I) = p(z|I) makes the conditioned sampling distribution carry exactly the same likelihood function as the unconditioned one. Conditioning on an ancillary that is part of the data is therefore redundant: the value of z is already known from D. This is once more the principle AA = A. The very fact that Fisher got different estimates with and without conditioning shows only that his unconditioned procedure violated the likelihood principle. For a Bayesian, the question of ancillarity never arises. Conversely, conditioning on a quantity Z that is NOT merely a function of the data injects genuine new information and will generally change inferences.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[logical-vs-causal-independence]] — uses: Jaynes dissolves data-function ancillarity via AA = A: a known function of the data is redundant information.
- [[sampling-theory]] — specializes: Ancillarity is a sampling-theory device (Fisher 1934) defined via parameter-free sampling distributions.
[To be populated during integration]