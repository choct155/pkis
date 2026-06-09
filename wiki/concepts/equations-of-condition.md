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
- bayesian-stats
- statistical-learning
id: pkis:concept:equations-of-condition
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch19
tags:
- jaynes
- measurement-error
- linear-inverse-problem
- parameter-estimation
- laplace
- least-squares
title: Equations of Condition (Overdetermined Linear Observation Model)
understanding: 0
---

## Definition
A system y = Ax + delta relating N imperfect observations y_i to n unknown parameters x_j through a known (N x n) design matrix A, where delta is the vector of (typically zero-mean) observation errors. Each row y_i = sum_j a_ij x_j + delta_i is an 'equation of condition' contributed by one measurement. The classical case is *overdetermined* (N > n): A is not square and has no inverse, so the equations cannot be solved exactly and generally disagree. The historical 'reduction of equations of condition' (Laplace, Essai Philosophique 1812) sought an (n x N) matrix B forming n linear combinations By = BAx + B*delta, then x_hat = (BA)^{-1} By; least squares is one criterion for choosing B. This is the framing in which Euler (1749) failed (N=75, n=8) for lack of the right principles, and in which Laplace later succeeded. The model also covers the well-posed (N = n) and underdetermined (N < n) cases. A parameter x_k is *irrelevant* if a nonzero q makes sum_j a_ij q_j vanish for all i (columns of A linearly dependent): then x and x + cq give identical data and x_k can be dropped. An observation is *useless* if its error weight w_i = 0. With at least as many cogent observations as relevant parameters, the system is identifiable. The model is the linear backbone of physical measurement, regression, and linear inverse problems.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]