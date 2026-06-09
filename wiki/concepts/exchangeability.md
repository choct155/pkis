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
id: pkis:concept:exchangeability
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch01
- gelman-bda3-ch05
tags:
- bayesian
- de-finetti
- iid
- foundations
- prior
title: Exchangeability
understanding: 0
---

## Definition
$$p(y_1,\ldots,y_n) = p(y_{\pi(1)},\ldots,y_{\pi(n)}) \quad \text{for every permutation } \pi.$$
A sequence is exchangeable when its joint distribution is invariant to reordering the indexes — the labels carry no information beyond the values themselves.

Exchangeability is the usual (often tacit) starting point of a statistical analysis. It is weaker than independence: exchangeable variables are generally dependent, but symmetrically so. It is the assumption that licenses pooling units into a common model.

### Relation to iid and de Finetti
Exchangeable data are commonly modeled as independent and identically distributed *given* an unknown parameter $\theta$ with its own distribution $p(\theta)$: $p(y_1,\ldots,y_n)=\int \prod_i p(y_i\mid\theta)\,p(\theta)\,d\theta$. De Finetti's theorem makes this precise: any infinitely exchangeable binary sequence can be represented as a mixture of iid sequences, which is exactly the prior-times-likelihood structure of Bayesian modeling. Thus exchangeability supplies a justification for the existence of a parameter and a prior rather than positing them by fiat.

### Extensions: covariates and hierarchy
When unit indexes do carry information, exchangeability can often be restored by conditioning on explanatory variables $x$, requiring the pairs $(x,y)_i$ to be exchangeable. In hierarchical (multilevel) models one assumes exchangeability *at each level* — e.g., patients within a city, and cities among themselves — which is the conceptual engine behind partial pooling.

### Why it matters
Exchangeability is what makes a parameter, a prior, and a likelihood meaningful at all, and it tells the analyst exactly when units may be combined and when a covariate must be added. It is the bridge between a symmetry judgment about data and the full probability model required for Bayesian inference.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]