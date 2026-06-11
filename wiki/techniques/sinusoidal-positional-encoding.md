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
- machine-learning
- deep-learning
- nlp
id: pkis:technique:sinusoidal-positional-encoding
instantiates:
- inductive-bias
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- transformer-architecture
related_concepts: []
sources:
- murphy-pml1-intro-ch15
tags:
- transformer
- position
- inductive-bias
- embedding
title: Positional Encoding (Sinusoidal)
understanding: 0
uses:
- self-attention
---

## Definition
To inject order information into a permutation-invariant self-attention model, position $i$ is encoded as a $d$-dimensional vector:

$$p_{i,2j} = \sin\!\left(\frac{i}{C^{2j/d}}\right), \quad p_{i,2j+1} = \cos\!\left(\frac{i}{C^{2j/d}}\right)$$

where $C = 10{,}000$. The positional embedding $\mathbf{P}$ is added elementwise to the word embedding matrix: $\text{POS}(\text{Embed}(\mathbf{X})) = \mathbf{X} + \mathbf{P}$.

### Why it matters
The sinusoidal basis ensures (1) extrapolation to sequence lengths unseen during training, and (2) a linearly predictable relationship $\mathbf{p}_{t+\phi} = R(\phi)\,\mathbf{p}_t$ where $R(\phi)$ is a rotation matrix, giving the model an inductive bias about relative distances. It is a key ingredient in the original Transformer and remains widely used alongside learned positional embeddings.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[inductive-bias]] — instantiates
- [[self-attention]] — uses: Positional encoding compensates for self-attention's permutation invariance
- [[transformer-architecture]] — prerequisite-of
[To be populated during integration]