---
aliases: []
also_type: []
applies:
- generative-vs-discriminative-models
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
- kernel-methods
- probabilistic-modeling
generalizes:
- fisher-kernel
id: pkis:technique:generative-model-kernels
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch06
tags:
- generative-kernel
- HMM-kernel
- mixture-kernel
- Fisher-kernel
- generative-discriminative
title: Generative-Model Kernels
understanding: 0
uses:
- kernel-construction-rules
- hidden-markov-model
- mixture-models
---

## Definition
Given a probabilistic generative model $p(\mathbf{x})$, kernels can be constructed that inherit the model's structure:

1. **Product kernel:** $k(\mathbf{x},\mathbf{x}') = p(\mathbf{x})p(\mathbf{x}')$ (similarity iff both inputs are probable).
2. **Mixture kernel:** $k(\mathbf{x},\mathbf{x}') = \sum_i p(\mathbf{x}|i)p(\mathbf{x}'|i)p(i)$ (inner product in the mixture component space).
3. **Continuous latent kernel:** $k(\mathbf{x},\mathbf{x}') = \int p(\mathbf{x}|z)p(\mathbf{x}'|z)p(z)\,dz$.
4. **HMM kernel (for sequences):** $k(\mathbf{X},\mathbf{X}') = \sum_{\mathbf{Z}} p(\mathbf{X}|\mathbf{Z})p(\mathbf{X}'|\mathbf{Z})p(\mathbf{Z})$, tying two sequences through a shared hidden-state path.

### Why it matters
Generative models handle variable-length inputs, missing data, and structured domains (sequences, graphs) naturally. By converting them into kernels, all the machinery of discriminative methods (SVMs, GP classifiers) can be applied while retaining these representational advantages — a direct realisation of the generative-discriminative trade-off.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generative-vs-discriminative-models]] — applies
- [[fisher-kernel]] — generalizes
- [[mixture-models]] — uses
- [[hidden-markov-model]] — uses
- [[kernel-construction-rules]] — uses
[To be populated during integration]