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
- numerical-computation
- machine-learning
id: pkis:concept:numerical-underflow-overflow
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- numerically-stable-softmax
related_concepts: []
sources:
- goodfellow-deeplearning-ch04
tags:
- floating-point
- numerical-stability
- softmax
- rounding-error
title: Numerical Underflow and Overflow
understanding: 0
---

## Definition
**Underflow** occurs when numbers near zero are rounded to zero by finite-precision arithmetic; **overflow** occurs when numbers of large magnitude are approximated as $\pm\infty$. Both are forms of rounding error that can cause otherwise-correct algorithms to return undefined results (NaN or division-by-zero).

They are the primary numerical instability hazards in floating-point computation and must be explicitly designed around in production ML code.

### Why it matters
Softmax, log-softmax, and many probabilistic computations involve exponentials whose arguments span a wide range; naive implementations overflow or underflow silently. Numerically stable re-implementations (e.g., subtracting $\max_i x_i$ before computing softmax) are standard engineering practice in deep learning frameworks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[numerically-stable-softmax]] — prerequisite-of
[To be populated during integration]