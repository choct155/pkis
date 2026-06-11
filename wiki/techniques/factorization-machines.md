---
aliases: []
also_type: []
applies:
- cold-start-problem
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- multilayer-perceptron
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- recommender-systems
extends:
- linear-regression
generalizes:
- matrix-factorization-recommender
id: pkis:technique:factorization-machines
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch22
tags:
- feature-interactions
- bilinear-model
- side-information
- embedding
title: Factorization Machines (FM)
understanding: 0
---

## Definition
$$f(\mathbf{x}) = \mu + \sum_{i=1}^{D} w_i x_i + \sum_{i=1}^{D}\sum_{j=i+1}^{D} (\mathbf{v}_i^\top \mathbf{v}_j)\, x_i x_j$$

where $\mathbf{x} \in \mathbb{R}^D$ is a feature vector (e.g. one-hot user $\oplus$ one-hot item $\oplus$ side information), $\mathbf{V} \in \mathbb{R}^{D \times K}$ parameterises pairwise feature interactions via inner products of $K$-dimensional embedding vectors. The double sum can be rewritten as

$$\frac{1}{2}\sum_{k=1}^{K}\!\left[\!\left(\sum_{i} v_{ik} x_i\right)^{\!2} - \sum_{i} v_{ik}^2 x_i^2\right]$$

reducing computation from $O(KD^2)$ to $O(KD)$ (or $O(K)$ for sparse one-hot inputs).

### Why it matters
FMs generalise matrix factorisation to arbitrary feature vectors, unifying CF and content-based approaches in one model. They naturally handle the cold-start problem by incorporating side information and are the linear core of deep FM and wide-and-deep architectures.

### Connections
- [[multilayer-perceptron]] — contrasts-with: FM is the linear bilinear core; deep FM adds an MLP branch
- [[linear-regression]] — extends
- [[cold-start-problem]] — applies
- [[matrix-factorization-recommender]] — generalizes
When $\mathbf{x}$ contains only one-hot user and item encodings, the FM reduces to standard matrix factorisation. Deep FMs add an MLP branch to capture higher-order feature interactions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]