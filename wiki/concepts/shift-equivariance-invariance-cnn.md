---
aliases: []
also_type: []
applies:
- convolutional-neural-networks
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
- computer-vision
id: pkis:concept:shift-equivariance-invariance-cnn
instantiates:
- inductive-bias
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch16
tags:
- convolution
- equivariance
- invariance
- CNN
- symmetry
- inductive-bias
title: Shift Equivariance and Shift Invariance in CNNs
understanding: 0
uses:
- symmetry-groups
- pooling-layer
---

## Definition
A function $f$ is **shift-equivariant** if translating the input by $\delta$ translates the output by $\delta$: $f(T_\delta x) = T_\delta f(x)$. It is **shift-invariant** if $f(T_\delta x) = f(x)$ for all $\delta$.

Convolutional layers with shared weights are shift-equivariant by construction; pooling layers (max or average over local patches) convert equivariance to invariance by discarding spatial position information.

### Why it matters
Shift equivariance is why CNNs transfer a learned feature detector across all spatial locations of an image without extra parameters, yielding dramatic parameter efficiency compared to fully connected networks. Pooling then provides the invariance needed for classification (where the absolute position of an object does not matter). This geometric inductive bias is the key reason CNNs dominated vision benchmarks before transformers with positional encodings became competitive.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[pooling-layer]] — uses
- [[symmetry-groups]] — uses
- [[inductive-bias]] — instantiates
- [[convolutional-neural-networks]] — applies
[To be populated during integration]