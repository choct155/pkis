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
- reinforcement-learning
- optimization
id: pkis:technique:expected-sarsa
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch06
tags:
- expected-sarsa
- td-control
- action-value
- variance-reduction
- off-policy
- on-policy
title: Expected Sarsa
understanding: 0
---

## Definition
Expected Sarsa is a temporal-difference control algorithm that replaces the sampled next-action value in the Sarsa target with its expectation under the policy, eliminating the variance contributed by the random selection of the next action.

## Definition
$$Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha\,\Big[\,R_{t+1} + \gamma \sum_a \pi(a\mid S_{t+1})\,Q(S_{t+1}, a) - Q(S_t, A_t)\,\Big].$$
(Eq. 6.9) Given the next state, the update moves deterministically in the same direction that Sarsa moves *in expectation*, hence the name.

## Why it helps
Expected Sarsa is more expensive per step than Sarsa but removes the variance due to the random choice of $A_{t+1}$. Empirically it performs slightly to significantly better than Sarsa across a wide range of step sizes. When all transition randomness comes from the policy (e.g. deterministic dynamics, as in Cliff-Walking), Expected Sarsa can safely set $\alpha = 1$ with no loss of asymptotic performance, whereas Sarsa needs a small $\alpha$. The authors note it may completely dominate both Sarsa and Q-learning apart from the small extra computation.

## Relationship to Q-learning
Expected Sarsa generalizes Q-learning: if the target policy $\pi$ is greedy while behavior is exploratory, the expectation collapses to the max and Expected Sarsa becomes exactly Q-learning. In general it can use a target policy different from behavior, making it an off-policy method that subsumes Q-learning while reliably improving over Sarsa.

## History
Introduced by George John (1994, who called it "Q-learning"); presented as an exercise in the first edition of Sutton & Barto; convergence and conditions for outperforming Sarsa/Q-learning established by van Seijen et al. (2009). The general off-policy view was noted by van Hasselt (2011) as "General Q-learning."

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]