---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:result:walds-identity
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch01
tags:
- probability-theory
- stochastic-processes
- stopping-times
- random-sums
- martingales
title: Wald's Identity
understanding: 0
---

## Definition
$$E\!\left(\sum_{i=1}^{\alpha} X_i\right) = E(X_1)\, E(\alpha)$$

Wald's identity gives the expectation of a sum of i.i.d. terms stopped at a random (stopping) time $\alpha$: the expected total equals the expected number of terms times the per-term mean — exactly as if $\alpha$ were a fixed constant.

### Hypotheses
The $X_n$ are i.i.d. with $E|X_1| < \infty$, and $\alpha$ is a stopping time with respect to $\{X_n\}$ satisfying $E\alpha < \infty$. The proof writes $\sum_{i=1}^{\alpha} X_i = \sum_{i\ge 1} X_i \mathbf 1_{[i \le \alpha]}$ and uses the *key independence*: $[i \le \alpha] = [\alpha \le i-1]^c$ depends only on $X_1,\ldots,X_{i-1}$, so $X_i$ is independent of the indicator. A Fubini/dominated-convergence argument justifies the interchange of sum and expectation.

### A diagnostic example
For the simple random walk with $N = \inf\{n : S_n = 1\}$, Wald gives $1 = ES_N = (p-q)EN$. In the symmetric case $p=q$ this forces $EN = \infty$; for $p<q$ it produces a contradiction unless $EN=\infty$, recovering known facts. For $p>q$ it yields $EN = (p-q)^{-1}$ — though it does not by itself establish finiteness.

### Why it matters
Wald's identity is the workhorse for the mean of randomly stopped sums in sequential analysis, gambling and ruin problems, renewal theory, and queueing. It is the simplest of the optional-stopping (martingale) theorems and shares the multiplicative $E(N)E(X_1)$ form already met in compound distributions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]