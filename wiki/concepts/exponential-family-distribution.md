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
- probability
- statistics
- information-theory
id: pkis:concept:exponential-family-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch02
tags:
- sufficient-statistics
- conjugate-prior
- natural-parameters
- maximum-entropy
title: Exponential Family
understanding: 0
---

## Definition
$$p(\mathbf{x}|\boldsymbol{\eta}) = h(\mathbf{x})\,g(\boldsymbol{\eta})\exp\{\boldsymbol{\eta}^T\mathbf{u}(\mathbf{x})\}$$

where $\boldsymbol{\eta}$ are the **natural parameters**, $\mathbf{u}(\mathbf{x})$ the **sufficient statistic vector**, $h(\mathbf{x})$ a base measure, and $g(\boldsymbol{\eta})$ ensures normalisation. The Bernoulli, binomial, Poisson, Gaussian, Beta, Dirichlet, and Gamma distributions are all members.

### Why it matters
The exponential family unifies seemingly disparate distributions under a single framework with shared properties: (1) moments are given by derivatives of $\ln g(\boldsymbol{\eta})$; (2) the MLE depends on data only through $\sum_n\mathbf{u}(\mathbf{x}_n)$—the sufficient statistic; (3) a conjugate prior of the form $g(\boldsymbol{\eta})^\nu\exp(\nu\boldsymbol{\eta}^T\boldsymbol{\chi})$ always exists; (4) the maximum-entropy distribution with fixed sufficient-statistic expectations is an exponential family member (exponential-family ML-MaxEnt duality).

### Natural parameterisation examples
Bernoulli: $\eta=\ln(\mu/(1-\mu))$ (logit), $u(x)=x$. Gaussian: $\boldsymbol{\eta}=(\mu/\sigma^2,\,-1/(2\sigma^2))^T$, $\mathbf{u}(x)=(x,x^2)^T$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]