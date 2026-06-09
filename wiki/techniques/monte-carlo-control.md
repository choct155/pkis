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
id: pkis:technique:monte-carlo-control
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch05
tags:
- reinforcement-learning
- monte-carlo
- generalized-policy-iteration
- control
- policy-improvement
- exploring-starts
title: Monte Carlo Control (RL)
understanding: 0
---

## Definition
Monte Carlo control approximates an *optimal* policy from sampled experience by embedding Monte Carlo policy evaluation inside generalized policy iteration (GPI): alternate between evaluating the current policy's action-value function from returns and improving the policy greedily with respect to that function,
$$\pi_0 \xrightarrow{E} q_{\pi_0} \xrightarrow{I} \pi_1 \xrightarrow{E} q_{\pi_1} \xrightarrow{I} \cdots \xrightarrow{I} \pi_* \xrightarrow{E} q_*.$$
Greedy improvement, $\pi(s) \doteq \arg\max_a q(s,a)$, requires *action* values (not state values) precisely because no model is available to look ahead. The policy improvement theorem guarantees each greedy step is no worse than the last, so $q_{\pi_k}(s,\pi_{k+1}(s)) = \max_a q_{\pi_k}(s,a) \ge v_{\pi_k}(s)$. In practice the algorithm does not run evaluation to convergence; like value iteration it intermixes evaluation and improvement on an *episode-by-episode* basis. The canonical instance is **Monte Carlo ES (Exploring Starts)**, which after each episode updates $Q(S_t,A_t)$ toward the observed return and sets $\pi(S_t)$ greedy.

### Why it matters
Monte Carlo control is the first method in the book that finds optimal behavior with *no* knowledge of environment dynamics — only sampled episodes. It demonstrates that the GPI machinery developed for dynamic programming carries over to model-free learning, establishing the template (sampled evaluation + greedy improvement) that every later tabular and approximate control algorithm follows. Its central practical difficulty — maintaining exploration so that all actions get evaluated — motivates the on-policy/off-policy distinction and the use of soft policies. (Notably, formal convergence of Monte Carlo ES remains one of RL's open theoretical questions.)

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]