---
aliases: []
also_type: []
applies:
- support-vector-machine
- svm-dual-formulation
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- optimization
id: pkis:technique:sequential-minimal-optimisation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch07
tags:
- svm
- training-algorithm
- quadratic-programming
- optimisation
title: Sequential Minimal Optimisation (SMO)
understanding: 0
---

## Definition
SMO (Platt, 1999) solves the SVM quadratic programme by iteratively selecting pairs of Lagrange multipliers $(a_i, a_j)$ and optimising the dual objective analytically with respect to these two variables while keeping all others fixed. The two-variable subproblem always admits a closed-form solution. Heuristics select which pair to update at each step. The algorithm terminates when all KKT conditions are satisfied to within a tolerance.

SMO reduces SVM training to a sequence of trivial two-variable QPs, entirely avoiding numerical QP solvers.

### Why it matters
Direct solution of the SVM QP over $N$ variables is $O(N^3)$ and requires $O(N^2)$ memory; SMO scales between $O(N)$ and $O(N^2)$ in practice. It is the most widely used SVM training algorithm and underlies popular libraries such as LIBSVM.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[svm-dual-formulation]] — applies
- [[support-vector-machine]] — applies
[To be populated during integration]