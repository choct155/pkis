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
- machine learning
- reinforcement learning
- statistics
id: pkis:concept:cumulative-regret
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch34
specializes:
- performance-measure
tags:
- regret
- exploration-exploitation
- bandit
- online learning
- performance measure
title: Cumulative Regret
understanding: 0
uses:
- exploration-exploitation-tradeoff
- multi-armed-bandit
---

## Definition
$$L_T \triangleq \mathbb{E}\left[\sum_{t=1}^{T} \ell_t\right], \quad \ell_t = \mathbb{E}_{p(s_t)}[R(s_t, \pi^*(s_t))] - \mathbb{E}_{\pi_t(a_t|s_t)p(s_t)}[R(s_t, a_t)]$$

Cumulative regret $L_T$ measures the total expected reward foregone relative to an oracle policy $\pi^*$ that knows the true reward function, accumulated over $T$ steps. It can be decomposed as $L_T = \sum_a \mathbb{E}[N_{T+1}(a)]\Delta_a$, where $\Delta_a$ is the reward gap and $N_{T+1}(a)$ the number of pulls of arm $a$.

### Why it matters
Regret is the canonical metric for evaluating exploration-exploitation algorithms: sublinear regret ($L_T = o(T)$) implies the policy converges to optimal, while the growth rate (logarithmic vs. polynomial vs. linear) quantifies how quickly. It connects bandit learning to classical statistical estimation via sample-size/accuracy tradeoffs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[performance-measure]] — specializes
- [[multi-armed-bandit]] — uses
- [[exploration-exploitation-tradeoff]] — uses
[To be populated during integration]