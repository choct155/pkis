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
- machine-learning
id: pkis:technique:polyak-ruppert-averaging
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch08
tags:
- iterate-averaging
- variance-reduction
- SWA
- SGD
- generalization
title: Polyak-Ruppert Iterate Averaging
understanding: 0
---

## Definition
**Polyak-Ruppert averaging** (also called iterate averaging) maintains a running mean of SGD iterates:

$$\bar{\theta}_t = \frac{1}{t}\sum_{i=1}^t \theta_i = \frac{1}{t}\theta_t + \frac{t-1}{t}\bar{\theta}_{t-1}$$

Polyak (1990) and Ruppert (1988) proved that $\bar{\theta}_t$ achieves the optimal asymptotic convergence rate among all SGD variants, matching the rate of second-order methods. For linear regression, iterate averaging is statistically equivalent to $\ell_2$ (ridge) regularization.

**Stochastic Weight Averaging (SWA)** uses an equal-weight average with a modified schedule to exploit flat minima in deep networks and improve generalization beyond what faster convergence alone would achieve.

### Why it matters
Iterate averaging is a free, post-hoc variance reduction technique for SGD. SWA shows it also yields better generalization, not merely faster convergence, making it standard practice for large deep-learning models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]