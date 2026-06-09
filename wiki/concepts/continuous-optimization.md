---
aliases: []
also_type:
- framework
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- optimization
- statistical-learning
id: pkis:concept:continuous-optimization
knowledge_type: concept
maturity: settled
prerequisite-of:
- empirical-risk-minimization
related_concepts:
- '[[vector-calculus]]'
- '[[gradient-descent]]'
- '[[convex-optimization]]'
- '[[lagrange-multipliers]]'
sources:
- '[[deisenroth-mml]]'
tags:
- mathematical-foundations
- calculus
title: Continuous Optimization
understanding: 0
---

The theory and practice of minimizing (or maximizing) differentiable functions over continuous domains, encompassing unconstrained methods (gradient descent, Newton's method), constrained methods (Lagrange multipliers, KKT conditions), and the special case of convex problems where local optima are global.

## Connections
- [[empirical-risk-minimization]] — prerequisite-of: MML Ch.1: training = numerically optimizing model parameters w.r.t. a utility function; continuous optimization (Ch.7) is the machinery that carries out ERM-style parameter estimation.