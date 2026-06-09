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
- robotics
- optimization
- systems-theory
id: pkis:result:linear-quadratic-regulator-lqr
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
tags:
- robotics
- optimal-control
- riccati-equation
- control
title: Linear Quadratic Regulator (LQR)
understanding: 0
---

## Definition
The closed-form solution of the continuous optimal-control problem when the cost is quadratic (∫ xᵀQx + uᵀRu dt, with Q, R positive definite) and the dynamics are linear (ẋ = Ax + Bu). Over an infinite horizon, the optimal cost-to-go (value function) is quadratic and the optimal policy is the linear state feedback u = −Kx, where K is obtained by solving an algebraic Riccati equation—no value iteration, policy iteration, or local optimization required. Because exact LQR is so cheap, real nonlinear problems are tackled with iterative LQR (ILQR): repeatedly linearize the dynamics and take a second-order (quadratic) approximation of the cost about the current trajectory, solve the resulting LQR, and iterate. LQR/ILQR unify motion planning and trajectory tracking by optimizing directly over controls.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]