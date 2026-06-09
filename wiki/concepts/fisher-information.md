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
id: pkis:concept:fisher-information
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch04
tags:
- likelihood
- curvature
- asymptotics
- observed-information
- jeffreys-prior
title: Fisher Information
understanding: 0
---

## Definition
A measure of the curvature of the log-likelihood that quantifies how much information a single observation carries about a parameter. The (expected) Fisher information J(omega) is the expectation, under the sampling distribution p(y|omega), of the negative second derivative of the log-likelihood with respect to omega; for vector omega it is a matrix. It is distinguished from the observed information I(omega) = -d^2/domega^2 log p(omega|y), which is the actual curvature of the log-posterior (or log-likelihood) evaluated at the data in hand; in large samples the observed information at the mode approaches n*J(omega_0). Fisher information governs large-sample Bayesian inference in two ways: it sets the asymptotic posterior precision (the posterior covariance approaches (n*J(omega_0))^{-1}, the Cramer-Rao-style optimal scale), and through its square root it defines Jeffreys' invariant noninformative prior. Higher Fisher information means a sharper likelihood, a more concentrated posterior, and more precisely estimable parameters; a flat or singular information matrix signals weak or absent identification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]