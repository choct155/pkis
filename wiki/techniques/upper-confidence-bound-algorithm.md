---
aliases: []
also_type: []
applies:
- contextual-bandit
- exploration-exploitation-tradeoff
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
- machine learning
- reinforcement learning
- statistics
id: pkis:technique:upper-confidence-bound-algorithm
instantiates:
- upper-confidence-bound
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch34
tags:
- bandit
- optimism
- regret
- exploration
- concentration inequality
title: Upper Confidence Bound (UCB) Algorithm
understanding: 0
uses:
- cumulative-regret
---

## Definition
$$a_t = \operatorname*{arg\,max}_{a}\, \tilde{R}_t(s_t, a), \quad \tilde{R}_t(s_t, a) = \hat{R}_t(s_t, a) + \delta_t(s_t, a)$$

UCB maintains an optimistic reward estimate $\tilde{R}_t$ that upper-bounds the true reward with high probability, and acts greedily with respect to this estimate. For the Bernoulli bandit, the Chernoff-Hoeffding bound gives $\delta_t(a) = c/\sqrt{N_t(a)}$, yielding:
$$\tilde{R}_t(a) = \hat{\mu}_t(a) + \frac{c}{\sqrt{N_t(a)}}$$

Optimism decreases as an arm is sampled more, naturally balancing exploration and exploitation.

### Why it matters
UCB achieves near-optimal (logarithmic) cumulative regret in many bandit variants and matches the Lai-Robbins lower bound asymptotically. It is deterministic, interpretable, and can be extended to contextual bandits via Bayesian posterior standard deviations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[cumulative-regret]] — uses
- [[exploration-exploitation-tradeoff]] — applies
- [[contextual-bandit]] — applies
- [[upper-confidence-bound]] — instantiates
[To be populated during integration]