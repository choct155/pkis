---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:kolmogorov-smirnov-statistic
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch06
tags:
- goodness-of-fit
- hypothesis-testing
- empirical-distribution
- nonparametric
title: Kolmogorov-Smirnov Statistic
understanding: 0
uses:
- brownian-bridge
- reflection-principle
- invariance-principle
---

## Definition
The Kolmogorov-Smirnov statistic $D_n = \sup_{x \in \mathbb{R}} |\hat F_n(x) - F(x)|$ measures the largest discrepancy between the empirical CDF $\hat F_n$ of an iid sample and a hypothesized continuous CDF $F$; it is the test statistic for the goodness-of-fit hypothesis $H_0$: the sample came from $F$, rejecting when $D_n$ is large. Its key feature is being **distribution-free**: for any continuous $F$, $D_n$ has the same distribution as under the uniform $F = U$ (proven by the probability-integral transform $F(X) \sim U$), so a single table of critical values serves all continuous nulls. In practice $D_n = \max_i \big(|i/n - F(X_{(i)})| \vee |F(X_{(i)}) - (i-1)/n|\big)$ over order statistics.

For large $n$, $\sqrt{n} D_n \Rightarrow D := \sup_{0\le t\le1} |B^{(0)}(t)|$, the supremum of the absolute Brownian bridge, with limit law $P[D > d] = 2\sum_{k\ge1}(-1)^{k-1} e^{-2k^2 d^2}$, computed via the reflection principle. This connects the empirical process to Brownian-motion theory and supplies asymptotic critical points.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[invariance-principle]] — uses: sqrt(n)(F_hat - F) converges to the bridge via the empirical-process invariance principle, justifying the sup-functional limit.
- [[reflection-principle]] — uses: The KS limit distribution is computed by iterated application of the reflection principle to the Brownian bridge / conditioned BM.
- [[brownian-bridge]] — uses: The large-sample law of sqrt(n) D_n is the distribution of the supremum of the absolute Brownian bridge.
[To be populated during integration]