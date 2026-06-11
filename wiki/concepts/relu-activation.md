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
- deep-learning
id: pkis:concept:relu-activation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch13
tags:
- activation-function
- ReLU
- GELU
- dead-relu
- non-saturating
title: ReLU and Non-Saturating Activation Functions
understanding: 0
---

## Definition
The **Rectified Linear Unit (ReLU)** is:
$$\text{ReLU}(a) = \max(a, 0) = a\,\mathbb{I}(a > 0), \qquad \text{ReLU}'(a) = \mathbb{I}(a > 0)$$
Unlike sigmoid/tanh, it does not saturate for positive inputs, preventing gradient vanishing. A family of non-saturating variants address the **dead ReLU** problem (units permanently off when pre-activations are large-negative):

| Variant | Definition |
|---------|------------|
| Leaky ReLU | $\max(\alpha a, a)$, $\alpha \in (0,1)$ |
| Parametric ReLU | Leaky ReLU with learned $\alpha$ |
| ELU | $\alpha(e^a-1)$ for $a\le 0$; $a$ for $a>0$ |
| SELU | $\lambda\,\text{ELU}(a;\alpha)$ with fixed $\alpha,\lambda$ guaranteeing self-normalizing property |
| Swish / SiLU | $a\,\sigma(\beta a)$ |
| GELU | $a\,\Phi(a)$ where $\Phi$ is the Gaussian CDF |

### Why it matters
The choice of activation function is one of the most impactful architectural decisions in deep learning. ReLU enabled training of very deep networks and remains the default; GELU is now dominant in Transformer architectures.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]