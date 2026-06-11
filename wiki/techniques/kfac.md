---
aliases: []
also_type: []
applies:
- neural-networks
- multilayer-perceptron
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
- optimization
id: pkis:technique:kfac
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch06
specializes:
- natural-gradient-descent
tags:
- natural-gradient
- Kronecker-product
- second-order
- Fisher-information
- neural-networks
title: KFAC (Kronecker-Factored Approximate Curvature)
understanding: 0
uses:
- fisher-information
---

## Definition
KFAC approximates the Fisher information matrix of a deep neural network as a **block-diagonal** matrix where each block (one per layer) is expressed as a **Kronecker product** of two small matrices:
$$\mathbf{F}_\ell \approx \mathbf{A}_{\ell-1} \otimes \mathbf{G}_\ell$$
where $\mathbf{A}_{\ell-1} = \mathbb{E}[a_{\ell-1}a_{\ell-1}^\top]$ is the covariance of layer $\ell$'s input activations and $\mathbf{G}_\ell = \mathbb{E}[g_\ell g_\ell^\top]$ is the covariance of the loss gradients w.r.t. the pre-activations. Inversion exploits the identity $(A \otimes G)^{-1} = A^{-1} \otimes G^{-1}$.

### Why it matters
KFAC reduces the cost of approximate natural gradient descent from $O(p^2)$ storage and $O(p^3)$ inversion to storage and inversion of two small matrices per layer. It has demonstrated faster convergence than SGD on supervised learning and reinforcement learning tasks, and can be justified via a mean-field approximation to the true Fisher.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[multilayer-perceptron]] — applies
- [[neural-networks]] — applies
- [[fisher-information]] — uses
- [[natural-gradient-descent]] — specializes
[To be populated during integration]