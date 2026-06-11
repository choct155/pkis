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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- optimisation
id: pkis:technique:robbins-monro-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch02
tags:
- sequential-learning
- stochastic-approximation
- online-learning
- convergence
title: Robbins-Monro Algorithm
understanding: 0
---

## Definition
A general sequential root-finding procedure: given a regression function $f(\theta)=\mathbb{E}[z|\theta]$, construct successive estimates
$$\theta^{(N)} = \theta^{(N-1)} + a_{N-1}\,z(\theta^{(N-1)})$$
where the step-size sequence $\{a_N\}$ satisfies $a_N\to 0$, $\sum_N a_N=\infty$, and $\sum_N a_N^2<\infty$. Under these conditions the sequence converges to the root $\theta^*$ where $f(\theta^*)=0$ with probability one.

### Why it matters
Applied to maximum likelihood, the algorithm processes one data point at a time: $\theta^{(N)}=\theta^{(N-1)}+a_{N-1}\nabla_{\theta}\ln p(x_N|\theta^{(N-1)})$, yielding **online/stochastic gradient ascent**. The three conditions on $a_N$ are satisfied by $a_N=c/N$, recovering the sequential mean update for Gaussian MLE. The Robbins-Monro framework thus provides the theoretical foundation for stochastic gradient descent and online EM.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]