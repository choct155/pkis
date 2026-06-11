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
- machine-learning
- deep-learning
- nlp
generalizes:
- self-attention
id: pkis:concept:multi-headed-attention
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- transformer-architecture
related_concepts: []
sources:
- murphy-pml1-intro-ch15
tags:
- transformer
- attention
- parallel
- representation-learning
title: Multi-Headed Attention (MHA)
understanding: 0
uses:
- scaled-dot-product-attention
---

## Definition
Multi-headed attention runs $h$ independent attention functions (heads) in parallel, each with its own learned projection matrices:

$$\mathbf{h}_i = \text{Attn}(\mathbf{W}^{(q)}_i \mathbf{q},\ \{\mathbf{W}^{(k)}_i \mathbf{k}_j,\ \mathbf{W}^{(v)}_i \mathbf{v}_j\}) \in \mathbb{R}^{p_v}$$

$$\text{MHA}(\mathbf{q}, \{\mathbf{k}_j, \mathbf{v}_j\}) = \mathbf{W}^o [\mathbf{h}_1^\top; \ldots; \mathbf{h}_h^\top]^\top \in \mathbb{R}^{p_o}$$

Setting $p_q h = p_k h = p_v h = p_o$ allows all heads to be computed in a single batched operation.

### Why it matters
Different heads specialise in capturing different notions of token similarity (syntactic, semantic, positional), analogously to multiple kernels in a kernel method. MHA is the key component in Transformer encoders and decoders, responsible for computing contextualised representations over the full sequence.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[self-attention]] — generalizes
- [[transformer-architecture]] — prerequisite-of
- [[scaled-dot-product-attention]] — uses
[To be populated during integration]