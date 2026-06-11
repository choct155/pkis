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
- computer-vision
- nlp
- multimodal
extends:
- simclr
id: pkis:technique:clip
instantiates:
- self-supervised-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
tags:
- contrastive-learning
- zero-shot
- multimodal
- representation-learning
- prompt-engineering
title: CLIP (Contrastive Language–Image Pre-training)
understanding: 0
uses:
- cross-entropy-loss
- in-context-learning
---

## Definition
CLIP jointly trains an image encoder $f_I$ and a text encoder $f_T$ on 400M web-scraped (image, text) pairs by maximising the cosine similarity of matched pairs and minimising it for mismatched pairs within each minibatch of size $N$:
$$J = \frac{1}{2}\left[\sum_{i=1}^N \text{CE}(L_{i,:},\mathbf{1}_i)+\sum_{j=1}^N \text{CE}(L_{:,j},\mathbf{1}_j)\right], \quad L_{ij}=\mathbf{I}_i^\top\mathbf{T}_j$$
where $\mathbf{I}_i=f_I(x_i)/\|f_I(x_i)\|_2$ and $\mathbf{T}_j=f_T(y_j)/\|f_T(y_j)\|_2$. At inference, zero-shot classification converts class names to text prompts and picks $\arg\max_k p(y=k|x)=\text{softmax}([\mathbf{I}^\top\mathbf{T}_1,\ldots])_k$.

### Why it matters
CLIP achieves competitive zero-shot performance on ImageNet without task-specific fine-tuning and exhibits strong robustness to distribution shift. It introduced **prompt engineering** as a key deployment skill: the textual form of class labels significantly affects accuracy, currently requiring per-dataset manual tuning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[in-context-learning]] — uses: Zero-shot classification via prompt engineering is a form of in-context specification.
- [[simclr]] — extends: CLIP extends contrastive SSL to cross-modal (image-text) pairs.
- [[cross-entropy-loss]] — uses
- [[self-supervised-learning]] — instantiates
[To be populated during integration]