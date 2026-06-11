---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- optimization
generalizes:
- deterministic-policy-gradient
id: pkis:result:policy-gradient-theorem
instantiates:
- policy-gradient-methods
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- reinforce
- policy-gradient-methods
- actor-critic
- trust-region-policy-optimization
- proximal-policy-optimization
related_concepts: []
sources:
- sutton-policy-2018
tags:
- policy-gradient
- gradient-estimation
- on-policy-distribution
- theorem
title: Policy Gradient Theorem
understanding: 0
uses:
- return-and-discounting
- action-value-function
- markov-decision-processes
---

## Definition
An analytic expression for the gradient of policy performance with respect to the policy parameter that crucially does NOT involve the derivative of the state distribution (which depends on the unknown environment dynamics). For the episodic case:
$$\nabla J(\theta)\;\propto\;\sum_s \mu(s)\sum_a q_\pi(s,a)\,\nabla\pi(a\mid s,\theta),$$
where $\mu$ is the on-policy state distribution under $\pi$ and the constant of proportionality is the average episode length (it is exactly 1, an equality, in the continuing case).

## Why It Is Needed
Performance depends on both action selections and the distribution of states visited; both are affected by $\theta$. The effect on actions is computable from the parameterization, but the effect of policy changes on the state distribution is a function of the environment and is typically unknown. The theorem shows the performance gradient can be written without the troublesome $\nabla\mu$ term, making stochastic-gradient estimation feasible.

## Proof Sketch (episodic)
Starting from $\nabla v_\pi(s)=\nabla[\sum_a \pi(a\mid s)q_\pi(s,a)]$, apply the product rule and the Bellman recursion for $q_\pi$, then repeatedly unroll one step. The bootstrapped $\nabla v_\pi(s')$ terms accumulate into $\sum_{x}\sum_{k=0}^{\infty}\Pr(s\to x,k,\pi)\sum_a \nabla\pi(a\mid x)q_\pi(x,a)$, where $\Pr(s\to x,k,\pi)$ is the $k$-step transition probability under $\pi$. Evaluating at $s_0$ and normalizing the accumulated visitation counts $\eta(s)$ to the on-policy distribution $\mu(s)=\eta(s)/\sum_{s'}\eta(s')$ yields the proportionality. The continuing-case proof rearranges the average-reward Bellman gradient and exploits $\sum_s\mu(s)=1$ and the steady-state invariance of $\mu$.

## Significance
This is the theoretical foundation for ALL policy-gradient algorithms (REINFORCE, actor-critic, and successors). First obtained by Marbach and Tsitsiklis (1998, 2001) and independently by Sutton, McAllester, Singh, and Mansour (2000), who coined 'policy gradient methods'.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-decision-processes]] — uses
- [[action-value-function]] — uses
- [[return-and-discounting]] — uses
- [[deterministic-policy-gradient]] — generalizes
- [[proximal-policy-optimization]] — prerequisite-of
- [[trust-region-policy-optimization]] — prerequisite-of
- [[actor-critic]] — prerequisite-of
- [[policy-gradient-methods]] — instantiates
- [[policy-gradient-methods]] — prerequisite-of: The theorem is the theoretical foundation underpinning every member algorithm of the framework.
- [[reinforce]] — prerequisite-of: REINFORCE is derived directly from the policy gradient theorem by converting the action sum to an expectation and sampling.
[To be populated during integration]