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
id: pkis:technique:xavier-initialization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch13
tags:
- initialization
- training
- neural-networks
- variance
title: Xavier / Glorot Initialization
understanding: 0
---

## Definition
Xavier (Glorot) initialization sets the variance of the weight distribution for layer $l$ to:
$$\sigma^2 = \frac{2}{n_{\text{in}} + n_{\text{out}}}$$
where $n_{\text{in}}$ and $n_{\text{out}}$ are the fan-in and fan-out of the layer. For a uniform draw $w_{ij} \sim \text{Unif}(-a, a)$ this gives $a = \sqrt{\frac{6}{n_{\text{in}}+n_{\text{out}}}}$. The derivation requires that the variance of forward activations and backward gradients both remain $O(1)$ across layers.

### Why it matters
Poor initialization causes activations or gradients to explode or vanish before training even begins. Xavier initialization provides a theoretically grounded default that keeps signal magnitudes stable in the linear/tanh/sigmoid regime.

### Variants
| Name | Formula | Recommended for |
|------|---------|----------------|
| LeCun | $\sigma^2 = 1/n_{\text{in}}$ | SELU |
| Xavier/Glorot | $\sigma^2 = 2/(n_{\text{in}}+n_{\text{out}})$ | tanh, sigmoid, softmax |
| He (Kaiming) | $\sigma^2 = 2/n_{\text{in}}$ | ReLU and variants |

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]