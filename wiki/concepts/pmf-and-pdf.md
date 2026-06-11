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
- probability-theory
- statistics
id: pkis:concept:pmf-and-pdf
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch02
tags:
- pmf
- pdf
- cdf
- random-variable
- probability-distribution
title: Probability Mass Function and Probability Density Function
understanding: 0
---

## Definition
For a discrete random variable $X$ with state space $\mathcal{X}$, the **probability mass function (PMF)** is
$$p_X(a) = \mathbb{P}[X = a], \quad a \in \mathcal{X}.$$
For a continuous random variable $X$ on $\mathbb{R}$, the **probability density function (PDF)** $p_X(x) \geq 0$ satisfies
$$\mathbb{P}([a,b]) = \int_a^b p_X(x)\,dx, \qquad \int_{-\infty}^{\infty} p_X(x)\,dx = 1.$$
The **cumulative distribution function (CDF)** unifies both cases: $P_X(x) = \mathbb{P}[X \leq x]$.

### Why it matters
The PMF/PDF is the primary computational object for evaluating likelihoods, computing expectations, and specifying generative models; choosing the right functional form for a PMF or PDF is the central modeling decision in probabilistic machine learning.

### Connections
For continuous $X$, the PDF is the Radon–Nikodym derivative of the probability measure with respect to Lebesgue measure, linking measure theory to the calculus-based formulas used in practice.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]