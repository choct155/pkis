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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- optimization
- numerical-methods
id: pkis:technique:conjugate-gradient-method
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch08
tags:
- second-order-methods
- conjugate-directions
- deep-learning
- quadratic-optimization
title: Conjugate Gradient Method
understanding: 0
---

## Definition
Conjugate gradient (CG) avoids computing or inverting the Hessian by constructing search directions $\mathbf{d}_t$ that are mutually $\mathbf{H}$-conjugate ($\mathbf{d}_t^\top\mathbf{H}\mathbf{d}_{t-1}=0$):
$$\mathbf{d}_t = -\mathbf{g}_t + \beta_t \mathbf{d}_{t-1},$$
with $\beta_t$ computed via Fletcher-Reeves ($\beta_t = \mathbf{g}_t^\top\mathbf{g}_t / \mathbf{g}_{t-1}^\top\mathbf{g}_{t-1}$) or Polak-Ribière ($\beta_t = (\mathbf{g}_t-\mathbf{g}_{t-1})^\top\mathbf{g}_t / \mathbf{g}_{t-1}^\top\mathbf{g}_{t-1}$). For a strictly quadratic objective in $k$ dimensions, CG converges in at most $k$ line searches.

Intuition: steepest descent wastes effort by oscillating in a zig-zag; CG retains progress along previous directions by ensuring the new search direction does not undo it.

### Why it matters
CG achieves super-linear convergence on quadratic objectives without forming or inverting the Hessian ($O(k^2)$ storage vs $O(k^3)$ for Newton). Nonlinear CG (periodic resets of $\beta_t$) generalises to non-quadratic objectives. CG is used in Hessian-free optimisation for deep networks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]