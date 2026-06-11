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
- regularization
id: pkis:technique:label-smoothing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch07
- murphy-pml2-advanced-ch14
tags:
- label-smoothing
- softmax
- cross-entropy
- regularization
- output-noise
title: Label Smoothing
understanding: 0
---

## Definition
Replace one-hot targets $y \in \{0,1\}$ with soft targets:
$$\tilde{y}_k = \begin{cases} 1 - \epsilon & \text{if } k = \text{true class} \\ \dfrac{\epsilon}{K-1} & \text{otherwise} \end{cases}$$

where $\epsilon$ is a small smoothing coefficient and $K$ is the number of classes. The standard cross-entropy loss is then applied to $\tilde{y}$.

Label smoothing prevents the model from driving softmax outputs toward hard 0/1 probabilities, which would require unbounded weights.

### Why it matters
A softmax classifier trained with hard targets and maximum likelihood can never assign probability exactly 0 or 1, so it continues increasing weight magnitudes indefinitely. Label smoothing resolves this divergence, acts as output-noise regularization, and has been a standard component in state-of-the-art image classifiers (e.g., Inception) since the 1980s.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]