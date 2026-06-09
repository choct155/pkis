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
id: pkis:technique:sarsa
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch06
specializes:
- temporal-difference-learning
tags:
- sarsa
- on-policy
- td-control
- action-value
- epsilon-greedy
- generalized-policy-iteration
title: Sarsa
understanding: 0
uses:
- td-error
---

## Definition
Sarsa is the on-policy temporal-difference control algorithm: it applies TD prediction to the action-value function $q_\pi(s,a)$ and folds it into generalized policy iteration, continually estimating $q_\pi$ for the current (e.g. ε-greedy) behavior policy while making that policy greedier with respect to the estimate.

## Definition
After every transition from a nonterminal state, Sarsa updates the action-value of the visited state–action pair:
$$Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha\,[\,R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}) - Q(S_t, A_t)\,].$$
(Eq. 6.7) If $S_{t+1}$ is terminal, $Q(S_{t+1},A_{t+1})$ is defined as 0. The update uses the full quintuple $(S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1})$ — *State, Action, Reward, State, Action* — which gives the algorithm its name. Crucially, the next action $A_{t+1}$ is the action actually selected by the behavior policy, which is what makes Sarsa **on-policy**.

## Convergence
Sarsa converges with probability 1 to an optimal policy and action-value function under the usual stochastic-approximation step-size conditions, provided all state–action pairs are visited infinitely often and the policy converges in the limit to the greedy policy (e.g. ε-greedy with $\epsilon = 1/t$).

## On-policy character
Because Sarsa learns the value of the policy it is actually following (including its exploratory actions), it accounts for the cost of exploration. In the Cliff-Walking example it learns the safe, roundabout path rather than the risky optimal edge path that Q-learning learns, giving better *online* performance under persistent ε-greedy exploration. Online methods such as Sarsa also handle tasks where termination is not guaranteed for all policies (e.g. Windy Gridworld), unlike Monte Carlo control.

## History
Introduced by Rummery and Niranjan (1994) as "Modified Connectionist Q-learning"; named "Sarsa" by Sutton (1996). One-step tabular Sarsa's convergence was proved by Singh, Jaakkola, Littman & Szepesvári (2000). Holland's bucket-brigade idea evolved into a closely related algorithm.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[td-error]] — uses: Sarsa update uses the action-value TD error
- [[temporal-difference-learning]] — specializes: on-policy TD control: TD applied to q_pi with policy improvement
[To be populated during integration]