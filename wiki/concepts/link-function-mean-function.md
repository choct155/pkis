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
id: pkis:concept:link-function-mean-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch12
tags:
- link-function
- canonical-link
- GLM
- probit
- complementary-log-log
title: Link Function and Mean Function
understanding: 0
---

## Definition
In a GLM the **link function** $\ell$ maps the mean $\mu$ to the natural parameter $\eta$:
$$\eta = \ell(\mu), \qquad \mu = \ell^{-1}(\eta) \equiv f(\eta)$$
where $f = \ell^{-1}$ is called the **mean function** (or inverse-link).

The **canonical link** is defined by $\ell(\mu) = \theta(\mu)$, i.e. it maps the mean directly to the natural (canonical) parameter of the exponential family. Using the canonical link makes $\eta = \theta$, simplifying the log-normalizer algebra and guaranteeing a convex NLL.

### Why it matters
The choice of link function determines (a) the support and shape of predictions, (b) whether the NLL is convex, and (c) the model's scientific interpretability. Common choices beyond the canonical link include the **probit** $\ell(\mu)=\Phi^{-1}(\mu)$ and the **complementary log-log** $\ell(\mu)=\log(-\log(1-\mu))$, the latter arising naturally from a Poisson event-count interpretation of binary outcomes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]