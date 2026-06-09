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
- reinforcement-learning
- optimization
generalizes:
- state-value-function
id: pkis:concept:action-value-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch03
tags: []
title: Action-Value Function (Q)
understanding: 0
uses:
- bellman-equation
---

## Definition
$$q_\pi(s, a) \doteq \mathbb{E}_\pi\!\left[G_t \mid S_t = s, A_t = a\right] = \mathbb{E}_\pi\!\left[\sum_{k=0}^{\infty}\gamma^k R_{t+k+1} \,\Big|\, S_t = s, A_t = a\right]$$

The **action-value function** $q_\pi(s,a)$ is the expected return from taking action $a$ in state $s$ and following policy $\pi$ afterward — how good a specific action is in a specific state.

### Intuition
Whereas $v_\pi$ scores states, $q_\pi$ scores state–action pairs. It answers "if I commit to $a$ now and then act as usual, what return do I expect?" Often called the **Q-function**, after Watkins's Q-learning.

### Relation to state values
$v_\pi(s) = \sum_a \pi(a\mid s)\, q_\pi(s,a)$ and $q_\pi(s,a) = \sum_{s',r} p(s',r\mid s,a)[r + \gamma v_\pi(s')]$. The two value functions are thus interderivable given the policy and dynamics.

### Why Q is convenient
With $q_*$ in hand, optimal action selection requires no one-step lookahead and no knowledge of the environment's dynamics: the agent simply picks $\arg\max_a q_*(s,a)$. The action-value function effectively caches the results of all one-step searches.

### Why it matters
$q_\pi$ is the object learned by value-based control methods (Q-learning, Sarsa); it makes action selection model-free, which is central to practical RL.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[state-value-function]] — generalizes: v_pi(s) = sum_a pi(a|s) q_pi(s,a); state value is the policy-average of action values.
- [[bellman-equation]] — uses: q_pi obeys an analogous Bellman recursion.
[To be populated during integration]