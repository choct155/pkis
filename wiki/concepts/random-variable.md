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
id: pkis:concept:random-variable
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- deisenroth-mml-ch06
tags: []
title: Random Variable
understanding: 0
---

## Definition
$$X : \Omega \to \mathcal{T}, \qquad P_X(S) = P(X^{-1}(S)) = P(\{\omega \in \Omega : X(\omega) \in S\})$$

A random variable is a function mapping outcomes of a random experiment to a target (often numerical) space, transporting the probability defined on the abstract sample space onto quantities we actually care about.

### Intuition
Kolmogorov's probability space $(\Omega, \mathcal{A}, P)$ — sample space, event space, probability measure — is rigorous but cumbersome to compute with. A random variable $X$ relocates the probability to a more convenient target space $\mathcal{T}$ (the *states*). For two coin tosses counting heads, $X(hh)=2$, $X(ht)=X(th)=1$, $X(tt)=0$, so $\mathcal{T}=\{0,1,2\}$. We say $X$ is *distributed according to* $P_X$ (its law), defined by pushing probability through the pre-image $X^{-1}$.

### Discrete vs. continuous
When $\mathcal{T}$ is finite or countable, $X$ is a **discrete** random variable described by a probability mass function $P(X=x)$. When $\mathcal{T}=\mathbb{R}$ or $\mathbb{R}^D$, $X$ is **continuous**, described by a density $f$ with $P(a\le X\le b)=\int_a^b f(x)\,dx$ and $P(X=x)=0$ for any single point.

### Why it matters
Virtually all of probabilistic ML is phrased over random variables rather than raw outcomes: features, labels, parameters, and latent states are all random variables, and inference is computation of their joint, marginal, and conditional laws. The pushforward construction is what licenses the everyday abuse $P(X=0)=P((\pounds,\pounds))$ that hides the underlying sample space.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]