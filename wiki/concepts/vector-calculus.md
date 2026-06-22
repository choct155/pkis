---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-22'
domain:
- statistical-learning
- optimization
- deep-learning
id: pkis:concept:vector-calculus
knowledge_type: concept
maturity: settled
prerequisite-of:
- continuous-optimization
related_concepts:
- '[[linear-algebra]]'
- '[[continuous-optimization]]'
- '[[automatic-differentiation]]'
- '[[backpropagation]]'
sources:
- '[[deisenroth-mml]]'
- betancourt-a-2018
tags:
- mathematical-foundations
- calculus
title: Vector Calculus
understanding: 0
---

Differentiation extended to vector- and matrix-valued functions: gradients (scalar → vector output), Jacobians (vector → vector), and Hessians (scalar → matrix), providing the mathematical foundation for all gradient-based optimization and for backpropagation as reverse-mode automatic differentiation.

## Connections
- [[continuous-optimization]] — prerequisite-of: MML Ch.1: vector calculus (Ch.5, gradients) supplies the direction information that gradient-based continuous optimization (Ch.7) uses to find maxima/minima of objective functions.