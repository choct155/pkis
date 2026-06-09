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
id: pkis:technique:n-step-sarsa
instantiates:
- n-step-bootstrapping
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch07
tags:
- reinforcement-learning
- control
- on-policy
- bootstrapping
title: n-step Sarsa
understanding: 0
uses:
- n-step-return
---

## Definition
n-step Sarsa is the on-policy TD control method that extends one-step Sarsa (Sarsa(0)) to n-step bootstrapping by switching from state values to action values. The n-step return is redefined over state-action pairs, G_{t:t+n} = R_{t+1} + ... + gamma^{n-1}*R_{t+n} + gamma^n * Q_{t+n-1}(S_{t+n}, A_{t+n}), and the update is Q_{t+n}(S_t, A_t) <- Q_{t+n-1}(S_t, A_t) + alpha[G_{t:t+n} - Q_{t+n-1}(S_t, A_t)], with the policy kept epsilon-greedy with respect to Q. Like all n-step methods, the update for (S_t, A_t) is delayed until time t+n. The benefit over one-step Sarsa is faster propagation of credit: in a gridworld where only the goal is rewarded, one-step Sarsa strengthens only the final action of a successful episode, whereas n-step Sarsa strengthens the last n actions, so much more is learned from a single episode. n-step Expected Sarsa is the variant whose n-step return replaces the final sampled action value with its expectation under the target policy, Vbar_{t+n-1}(S_{t+n}) = sum_a pi(a|s) Q(s,a).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[n-step-bootstrapping]] — instantiates: n-step Sarsa is the on-policy control instance of n-step bootstrapping
- [[n-step-return]] — uses: n-step Sarsa uses the action-value form of the n-step return
[To be populated during integration]