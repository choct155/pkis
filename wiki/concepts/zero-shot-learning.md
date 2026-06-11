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
- representation-learning
- computer-vision
- nlp
id: pkis:concept:zero-shot-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch15
specializes:
- transfer-learning-domain-adaptation
tags:
- zero-shot
- few-shot
- one-shot
- semantic-embedding
- generalization
- multimodal
title: Zero-Shot Learning
understanding: 0
uses:
- word-embeddings
- distributed-representation
- disentangled-representation
- contextual-word-embeddings
---

## Definition
A form of transfer learning in which the model must classify or predict for target classes that had **no labeled training examples**, by exploiting a side-channel description of the class (e.g., a learned word embedding or attribute vector). The model is trained to estimate
$$p(\mathbf{y} \mid \mathbf{x}, T)$$
where $T$ encodes a distributed representation of the task / class description. At test time, $T$ refers to a novel class whose embedding was never seen paired with labeled images.

### Why it matters
Zero-shot learning demonstrates that distributed representations can bind perceptual and semantic spaces: an image encoder and a language encoder are jointly aligned so that $f_x(\mathbf{x}_{\text{test}})$ is matched to $f_y(\mathbf{y}_{\text{test}})$ via the learned cross-modal map, even for unseen pairings. It underlies CLIP-style contrastive multimodal models and is a key benchmark of genuine compositional generalisation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[contextual-word-embeddings]] — uses
- [[disentangled-representation]] — uses
- [[distributed-representation]] — uses
- [[word-embeddings]] — uses
- [[transfer-learning-domain-adaptation]] — specializes
[To be populated during integration]