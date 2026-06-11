---
aliases: []
also_type: []
analogous-to:
- probability-mass-function
applies:
- random-variable
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
- probability-theory
- machine-learning
id: pkis:concept:probability-density-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- change-of-variables-density
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
specializes:
- probability-theory
tags:
- continuous
- distribution
- density
- fundamentals
title: Probability Density Function (PDF)
understanding: 0
---

## Definition
A **probability density function** $p$ for a continuous random variable $\mathbf{x}$ satisfies:
$$p(x) \geq 0, \quad \int_{-\infty}^{\infty} p(x)\,dx = 1.$$
The probability that $x$ lies in a set $S$ is $\int_S p(x)\,dx$; the density $p(x)$ itself need not be $\leq 1$. Uncertainty is spread continuously, so individual point probabilities are zero.

### Why it matters
PDFs underpin nearly all continuous probabilistic models in deep learning, from Gaussian likelihoods to normalizing flows. The distinction from PMFs — particularly that density values can exceed 1 — is a common source of confusion.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[change-of-variables-density]] — prerequisite-of
- [[probability-mass-function]] — analogous-to
- [[probability-theory]] — specializes
- [[random-variable]] — applies
[To be populated during integration]