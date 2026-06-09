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
id: pkis:technique:residual-gradient-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch11
tags:
- bellman-error
- sgd
- double-sampling
- off-policy
- baird
title: Residual-Gradient Algorithm
understanding: 0
---

## Definition
A true SGD method (Baird, 1995) that performs gradient descent on the mean square Bellman error (a.k.a. Bellman residual). The 'naive' version simply completes the semi-gradient TD update with the missing gradient term: w_{t+1} = w_t + alpha rho_t delta_t [grad v(S_t) - grad v(S_{t+1})], converging robustly but to undesirable values that minimize the mean square TD error (TDE) rather than producing accurate predictions — as shown by the A-split example, where it learns B=3/4, C=1/4 instead of the true B=1, C=0. The correct (non-naive) residual-gradient update has the next state appear in two multiplied expectations, requiring two independent next-state samples ('double sampling') for an unbiased product; this is only possible in deterministic environments (where the samples coincide) or in simulators (roll back and re-sample). It then provably converges to the unique BE minimizer for linear or nonlinear approximators. Sutton & Barto identify three deficiencies: it is empirically slow, it converges to the wrong values under genuine function approximation (A-presplit example), and — most damning — the BE objective it targets is not learnable from observable data. It thus serves as the chapter's cautionary case against pursuing the Bellman error directly.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]