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
- machine-learning
- probability
generalizes:
- dirichlet-distribution
id: pkis:concept:dirichlet-process
instantiates:
- bayesian-nonparametric-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch31
tags:
- dirichlet-process
- nonparametric-bayes
- clustering
- stick-breaking
- chinese-restaurant-process
title: Dirichlet Process
understanding: 0
uses:
- exchangeability
- stick-breaking-construction
- chinese-restaurant-process
---

## Definition
The Dirichlet process $\mathrm{DP}(\alpha, H)$ with concentration parameter $\alpha > 0$ and base measure $H$ is a distribution over probability measures $G$ on a measurable space $\Theta$ such that, for any finite measurable partition $(A_1,\ldots,A_k)$ of $\Theta$,
$$
(G(A_1),\ldots,G(A_k)) \sim \mathrm{Dir}(\alpha H(A_1),\ldots,\alpha H(A_k)).
$$
Almost surely, draws $G\sim\mathrm{DP}(\alpha,H)$ are discrete (atomic) probability measures, expressible via the stick-breaking construction $G = \sum_{k=1}^{\infty} \pi_k \delta_{\theta_k}$ where $\theta_k\overset{\text{iid}}{\sim}H$ and weights $\pi_k$ arise from sequential Beta-distributed breaks.

The DP is the canonical prior over probability distributions and is the building block for the Dirichlet Process Mixture Model.

### Why it matters
The DP allows clustering with an unbounded number of components: the posterior automatically determines how many clusters are supported by the data, avoiding the need to pre-specify $K$. The Chinese Restaurant Process and stick-breaking representations make posterior inference via MCMC and variational methods tractable.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-nonparametric-models]] — instantiates
- [[chinese-restaurant-process]] — uses
- [[stick-breaking-construction]] — uses
- [[exchangeability]] — uses
- [[dirichlet-distribution]] — generalizes
[To be populated during integration]