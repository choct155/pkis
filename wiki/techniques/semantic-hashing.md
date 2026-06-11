---
aliases: []
also_type: []
applies:
- manifold-hypothesis
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
- information-retrieval
- deep-learning
- representation-learning
id: pkis:technique:semantic-hashing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch14
tags:
- binary-code
- hash-table
- Hamming-distance
- information-retrieval
- deep-autoencoder
title: Semantic Hashing
understanding: 0
uses:
- autoencoder
- hash-function
---

## Definition
Semantic hashing (Salakhutdinov & Hinton, 2007) is an information-retrieval technique that encodes database items into short binary codes using a deep autoencoder trained to produce saturated sigmoid outputs, then retrieves similar items via hash-table lookup:
$$\text{binary code}(x) = \text{round}(f_\sigma(x)) \in \{0,1\}^k$$
where $f_\sigma$ is a sigmoid-output encoder and $k \ll d$.

Retrieval reduces to exact or Hamming-distance search over bit strings, which is $O(1)$ or $O(k)$ per query.

### Why it matters
Semantic hashing brings learned representation to the scalability requirements of large-scale search: binary codes can be stored in hash tables and compared with bitwise operations. It demonstrates that autoencoders can directly optimise application-level structure (binary code similarity $\approx$ semantic similarity), and has been successfully applied to text and image retrieval.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[manifold-hypothesis]] — applies
- [[hash-function]] — uses
- [[autoencoder]] — uses
[To be populated during integration]