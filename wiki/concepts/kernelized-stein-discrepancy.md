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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- functional-analysis
id: pkis:concept:kernelized-stein-discrepancy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch24
tags:
- Stein-operator
- RKHS
- EBM-training
- goodness-of-fit
title: Kernelized Stein Discrepancy (KSD)
understanding: 0
---

## Definition
$$D_{\mathrm{KSD}}(p_D \| p_\theta) = \sup_{\|f\|_{\mathcal{H}} \leq 1}\; E_{p_D(x)}\!\left[\nabla_x \log p_\theta(x)^T f(x) + \operatorname{tr}(\nabla_x f(x))\right]$$

where $f$ ranges over the unit ball of a reproducing kernel Hilbert space (RKHS) with kernel $k$. The supremum has a closed-form solution involving the Stein operator applied to $k$, making the trace term a constant that does not affect EBM training.

### Why it matters
KSD provides a partition-function-free divergence for training EBMs that avoids the expensive $O(d^2)$ trace computation of general Stein discrepancy. It generalises score matching and is used for goodness-of-fit testing and variational inference. The RKHS formulation enables kernel-based hypothesis testing without samples from the model.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]