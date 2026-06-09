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
- optimization
- deep-learning
extends:
- n-step-sarsa
id: pkis:technique:n-step-off-policy
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch07
tags:
- reinforcement-learning
- off-policy
- importance-sampling
- control-variate
title: n-step Off-policy Learning
understanding: 0
uses:
- importance-sampling
---

## Definition
Off-policy n-step learning estimates the value function for a target policy pi while following a different behavior policy b, by weighting each n-step update with the importance sampling ratio rho_{t:h} = product_{k=t}^{min(h,T-1)} pi(A_k|S_k)/b(A_k|S_k), the relative probability of taking the observed actions under the two policies. For state-value prediction: V_{t+n}(S_t) <- V_{t+n-1}(S_t) + alpha*rho_{t:t+n-1}[G_{t:t+n} - V_{t+n-1}(S_t)]. For action values (off-policy n-step Sarsa) the ratio starts one step later, rho_{t+1:t+n}, because the first action is the one being learned and needs no correction. Setting pi = b (the on-policy case) makes every ratio 1, so these updates strictly generalize their on-policy counterparts. A drawback is high variance, which forces small step sizes and slow learning. A more refined per-decision form uses control variates: G_{t:h} = rho_t(R_{t+1} + gamma*G_{t+1:h}) + (1 - rho_t)*V_{h-1}(S_t), so that when rho_t = 0 the target equals the current estimate (no change) instead of collapsing to zero, reducing variance without changing the expected update.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[importance-sampling]] — uses: weights n-step updates by the product-of-policy-ratios importance sampling ratio
- [[n-step-sarsa]] — extends: off-policy n-step learning extends on-policy n-step Sarsa/TD via importance sampling
[To be populated during integration]