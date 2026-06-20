---
aliases: []
also_type: []
applies:
- markov-decision-processes
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
date_updated: '2026-06-20'
domain:
- reinforcement-learning
- optimization
id: pkis:technique:policy-iteration
instantiates:
- generalized-policy-iteration
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch04
- cassandras-des-intro-ch09
tags:
- dynamic-programming
- optimal-policy
- value-function
title: Policy Iteration
understanding: 0
uses:
- policy-evaluation
- policy-improvement
---

## Definition
$$\pi_0 \xrightarrow{E} v_{\pi_0} \xrightarrow{I} \pi_1 \xrightarrow{E} v_{\pi_1} \xrightarrow{I} \cdots \xrightarrow{I} \pi_* \xrightarrow{E} v_*$$

Policy iteration alternates full policy evaluation ($E$) and policy improvement ($I$) to produce a sequence of monotonically improving policies that converges to an optimal policy and value function.

### Operational mechanism
Starting from an arbitrary $V$ and $\pi$: (1) run iterative policy evaluation to (near-)convergence to obtain $v_\pi$; (2) compute the greedy policy $\pi'$ with respect to $v_\pi$; (3) if the policy is unchanged (`policy-stable`), stop and return $V \approx v_*$, $\pi \approx \pi_*$; otherwise repeat. Warm-starting each evaluation from the previous policy's value function greatly speeds convergence, since values change little between successive policies.

### Conditions and convergence
A finite MDP has only finitely many deterministic policies, and each iteration yields a strict improvement unless already optimal, so policy iteration converges in a finite number of iterations — often surprisingly few. A subtle termination bug arises if two equally-good policies cycle; tie-breaking fixes it.

### Why it matters
Policy iteration is one of the two classical DP algorithms for solving finite MDPs exactly given a model, and it is the concrete archetype of the evaluation/improvement loop that generalizes to value iteration and generalized policy iteration.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-decision-processes]] — applies: Computes an optimal policy for a finite MDP.
- [[generalized-policy-iteration]] — instantiates: Policy iteration is the complete-step instance of GPI.
- [[policy-improvement]] — uses: Each iteration makes the policy greedy w.r.t. v_pi.
- [[policy-evaluation]] — uses: Each iteration runs full policy evaluation to obtain v_pi.
[To be populated during integration]