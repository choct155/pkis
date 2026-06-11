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
- machine-learning
extends:
- exponential-family
id: pkis:concept:exponential-family-distributions
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- generalized-linear-models
- conjugate-prior
related_concepts: []
sources:
- murphy-pml1-intro-ch03
tags:
- sufficient-statistics
- natural-parameters
- log-partition-function
- generalized-linear-models
title: Exponential Family
understanding: 0
uses:
- sufficient-statistics
- maximum-entropy-principle
- partition-function
---

## Definition
A family of distributions parameterised by $\boldsymbol{\eta} \in \mathbb{R}^K$ is an **exponential family** if its density can be written as:
$$p(\mathbf{y}|\boldsymbol{\eta}) = h(\mathbf{y}) \exp\left[\boldsymbol{\eta}^T T(\mathbf{y}) - A(\boldsymbol{\eta})\right]$$
where $h(\mathbf{y})$ is the base measure, $T(\mathbf{y})$ are sufficient statistics, $\boldsymbol{\eta}$ are natural (canonical) parameters, and $A(\boldsymbol{\eta}) = \log Z(\boldsymbol{\eta})$ is the log partition function.

The exponential family includes the Gaussian, Bernoulli, Poisson, Gamma, Dirichlet, and many other standard distributions; it unifies them into a single analytical framework.

### Why it matters
$A(\boldsymbol{\eta})$ is convex, and its gradient and Hessian yield the mean and covariance of $T(\mathbf{y})$. The log-likelihood is concave in $\boldsymbol{\eta}$, guaranteeing a unique MLE. Exponential families arise naturally as maximum-entropy distributions under moment constraints, and they are the foundation for generalised linear models.

### Key variants
- **Natural exponential family (NEF)**: $T(\mathbf{y}) = \mathbf{y}$, $\boldsymbol{\eta} = \boldsymbol{\phi}$.
- **Curved exponential family**: the map $\boldsymbol{\phi} \mapsto \boldsymbol{\eta}$ is nonlinear.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[partition-function]] — uses
- [[conjugate-prior]] — prerequisite-of
- [[generalized-linear-models]] — prerequisite-of
- [[maximum-entropy-principle]] — uses
- [[exponential-family]] — extends
- [[sufficient-statistics]] — uses
[To be populated during integration]