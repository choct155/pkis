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
- meta-learning
id: pkis:concept:hypernetwork
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch16
tags:
- hypernetwork
- parameter-generation
- multiplicative-interaction
- meta-learning
title: Hypernetwork
understanding: 0
---

## Definition
$$f(x; g(z; \phi))$$

A hypernetwork is a neural network $g(z;\phi)$ whose output serves as the parameters $\theta = g(z;\phi)$ of a primary ("target") network $f(x;\theta)$. When both networks are affine, the hypernetwork is equivalent to a bilinear multiplicative layer: $y = (z^T\mathbf{W} + \mathbf{V})x + \mathbf{U}z + b$.

### Why it matters
Hypernetworks allow rapid, input-conditioned parameter generation, enabling a single meta-network to produce customized weights for diverse tasks or input contexts. They are closely related to FiLM layers, attention (a three-way hypernetwork), and meta-learning methods that adapt at test time. The multiplicative-interaction framing reveals hypernetworks as a generalization of gating and linear modulation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]