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
- deep-learning
id: pkis:concept:zero-padding-cnn
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch09
tags:
- padding
- valid convolution
- same convolution
- full convolution
- spatial dimensions
title: Zero Padding
understanding: 0
---

## Definition
**Zero padding** implicitly extends the input by appending zeros around its border before applying a convolution, allowing independent control of output spatial size.

Three standard regimes:
- **Valid**: no padding; output shrinks by $k-1$ per layer.
- **Same**: pad by $\lfloor k/2\rfloor$ each side; output size equals input size.
- **Full**: pad by $k-1$; output size is $m+k-1$.

### Why it matters
Without padding, repeated convolutions rapidly erode spatial dimensions, limiting network depth. Choosing the padding regime trades off spatial fidelity at boundaries against architectural flexibility; 'same' padding is standard in deep stacks while 'valid' is preferred when boundary artifacts matter.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]