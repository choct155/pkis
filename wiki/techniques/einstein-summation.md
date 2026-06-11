---
aliases: []
also_type: []
applies:
- linear-algebra
- transformer-attention-mechanisms
- graph-neural-networks
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
- linear-algebra
- machine-learning
- deep-learning
id: pkis:technique:einstein-summation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch07
tags:
- tensor-contraction
- index-notation
- NumPy
- PyTorch
- optimisation
- batched-operations
title: Einstein Summation Notation (Einsum)
understanding: 0
---

## Definition
**Einstein summation** (einsum) is a compact index-based notation for tensor contractions: any index appearing exactly twice on the right-hand side is implicitly summed over, and any index absent from the left-hand side is also summed. For example, matrix multiplication $C_{ij} = \sum_k A_{ik}B_{kj}$ is written $C_{ij} = A_{ik}B_{kj}$.

More generally, for a batched sequence embedding:
$$L_{nc} = S_{ntk}W_{kd}V_{dc}$$
sums over $k$, $d$, and $t$ automatically.

### Why it matters
Einsum is implemented in NumPy, PyTorch, TensorFlow, and JAX. It (i) makes complex tensor operations readable and bug-resistant, (ii) allows libraries to automatically choose an optimal contraction order (minimising treewidth of the computation graph), and (iii) avoids materialising large intermediate tensors. It is indispensable for attention mechanisms, graph neural networks, and any operation involving batched multi-dimensional data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[graph-neural-networks]] — applies
- [[transformer-attention-mechanisms]] — applies
- [[linear-algebra]] — applies
[To be populated during integration]