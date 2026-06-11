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
- probabilistic-graphical-models
id: pkis:concept:markov-blanket-dpgm
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- gibbs-sampler
- mean-field-approximation
related_concepts: []
sources:
- murphy-pml2-advanced-ch04
specializes:
- markov-blanket
tags:
- Gibbs-sampling
- mean-field
- conditional-independence
- local-computation
title: Markov Blanket in Directed Graphical Models
understanding: 0
uses:
- d-separation
---

## Definition
$$\text{mb}(i) \triangleq \text{ch}(i) \cup \text{pa}(i) \cup \text{copa}(i)$$

The Markov blanket of node $i$ in a DPGM consists of its parents, children, and co-parents (other parents of its children); conditioning on $\text{mb}(i)$ renders $x_i$ independent of all other nodes.

### Why it matters
The full conditional distribution needed for Gibbs sampling and mean-field variational inference is
$$p(x_i \mid x_{-i}) = p(x_i \mid x_{\text{mb}(i)}) \propto p(x_i \mid x_{\text{pa}(i)}) \prod_{k \in \text{ch}(i)} p(x_k \mid x_{\text{pa}(k)})$$
making the Markov blanket the minimal sufficient neighborhood for local computations in large graphical models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[d-separation]] — uses
- [[mean-field-approximation]] — prerequisite-of
- [[gibbs-sampler]] — prerequisite-of
- [[markov-blanket]] — specializes
[To be populated during integration]