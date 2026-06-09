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
id: pkis:result:td-fixed-point
instantiates:
- linear-function-approximation-rl
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
tags:
- convergence
- linear-methods
- temporal-difference
- error-bound
title: TD Fixed Point
understanding: 0
uses:
- on-policy-distribution
---

## Definition
The weight vector w_TD = A⁻¹ b to which linear semi-gradient TD(0) converges, where A = E[x_t (x_t − γ x_{t+1})ᵀ] and b = E[R_{t+1} x_t]. In expected steady state E[w_{t+1}|w_t] = w_t + α(b − A w_t), so any fixed point satisfies b = A w_TD. Convergence and the existence of A⁻¹ follow from A being positive definite; for the continuing case A = Xᵀ D (I − γP) X, and the key matrix D(I − γP) has column sums (1−γ)μᵀ > 0 because μ is the stationary distribution—so on-policy TD(0) is stable (Sutton 1988; Tsitsiklis & Van Roy 1997). At the fixed point the asymptotic error is bounded: VE(w_TD) ≤ (1/(1−γ)) min_w VE(w). The expansion factor 1/(1−γ) can be large when γ is near one, so TD trades some asymptotic accuracy (vs. Monte Carlo) for much lower variance and faster learning. The bound and stability hold only under on-policy updating; off-policy bootstrapping with function approximation can diverge.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[on-policy-distribution]] — uses: positive definiteness of A, and hence stability, relies on updating under the on-policy distribution
- [[linear-function-approximation-rl]] — instantiates: the TD fixed point is the convergence point of linear semi-gradient TD(0)
[To be populated during integration]