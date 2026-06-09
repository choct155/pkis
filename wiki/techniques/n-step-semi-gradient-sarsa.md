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
id: pkis:technique:n-step-semi-gradient-sarsa
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch10
tags:
- n-step-bootstrapping
- sarsa
- function-approximation
- n-step-return
- bias-variance
- mountain-car
title: n-step Semi-Gradient Sarsa
understanding: 0
---

## Definition
$n$-step semi-gradient Sarsa generalizes one-step semi-gradient Sarsa by replacing the one-step bootstrapped target with an $n$-step return, balancing the bias of heavy bootstrapping against the variance of long Monte Carlo backups. The episodic $n$-step return for action values is

$$G_{t:t+n} \doteq R_{t+1} + \gamma R_{t+2} + \cdots + \gamma^{n-1}R_{t+n} + \gamma^n\hat{q}(S_{t+n},A_{t+n},\mathbf{w}_{t+n-1}), \quad t+n<T,$$

with $G_{t:t+n}\doteq G_t$ when $t+n\ge T$. The update applied at time $t+n$ is

$$\mathbf{w}_{t+n} \doteq \mathbf{w}_{t+n-1} + \alpha\left[G_{t:t+n} - \hat{q}(S_t,A_t,\mathbf{w}_{t+n-1})\right]\nabla\hat{q}(S_t,A_t,\mathbf{w}_{t+n-1}).$$

The intuition: $n=1$ is fully bootstrapped (low variance, high bias from a possibly wrong estimate), while large $n$ approaches Monte Carlo (low bias, high variance). An intermediate $n$ usually wins. On Mountain Car, $n=8$ learns faster and reaches better asymptotic performance than $n=1$, with a detailed study showing $n=4$ best for early performance.

### Why it matters
$n$-step methods are the standard way to tune the bias-variance trade-off in TD control, and this algorithm is the bridge to eligibility-trace methods (forward Sarsa($\lambda$)). A differential (average-reward) $n$-step version follows directly by replacing $R_i$ with $R_i - \bar{R}$ and dropping $\gamma$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]