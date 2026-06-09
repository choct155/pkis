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
id: pkis:concept:brownian-bridge
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch06
tags:
- stochastic-processes
- gaussian-process
- empirical-process
- goodness-of-fit
title: Brownian Bridge
understanding: 0
---

## Definition
The Brownian bridge $\{B^{(0)}(t), 0 \le t \le 1\}$ is the Gaussian process obtained by tying down a standard Brownian motion at both endpoints: $B^{(0)}(t) = B(t) - t B(1)$. It satisfies $B^{(0)}(0) = B^{(0)}(1) = 0$, has zero mean, and covariance function
$$\mathrm{Cov}(B^{(0)}(s), B^{(0)}(t)) = s(1-t), \quad 0 \le s \le t \le 1.$$
Equivalently, the bridge is Brownian motion conditioned to be zero at time 1: the conditioned process $B^{(\epsilon)}$ (BM given $0 \le B(1) \le \epsilon$) converges to $B^{(0)}$ as $\epsilon \to 0$. A useful structural fact is that $B(1)$ is independent of the entire bridge process.

The Brownian bridge is the weak limit of the normalized empirical process: for iid samples with continuous CDF $F$ and empirical CDF $\hat F_n$, $\sqrt{n}(\hat F_n(x) - F(x)) \Rightarrow B^{(0)}(F(x))$. This is why the Kolmogorov-Smirnov statistic $\sqrt{n}D_n$ converges to $\sup_{0\le t\le1}|B^{(0)}(t)|$, whose distribution $P[D \le v] = 1 + 2\sum_{k\ge1}(-1)^k e^{-2k^2 v^2}$ supplies large-sample critical values.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]