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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- deep-learning
id: pkis:technique:residual-network
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch21
tags:
- very-deep-networks
- skip-connections
- vanishing-gradient
- identity-mapping
title: Residual Network (Skip Connections)
understanding: 0
---

## Definition
An architectural device (He et al., 2016) for building very deep networks that avoid the vanishing-gradient failure of information propagation. The key idea is that a layer should perturb the representation from the previous layer rather than replace it entirely: z^(i) = g_r(z^(i-1) + f(z^(i-1))), where the residual f (typically one nonlinear plus one linear layer, f(z) = V g(Wz)) is added to a pass-through of the previous layer. If the learned perturbation is small, the layer is close to a copy of its predecessor. Critically, with ReLU activations a layer with zero residual weights (V = 0) reduces to an identity mapping, since ReLU(ReLU(x)) = ReLU(x), so the layer simply passes its inputs through and the network functions as if the layer never existed. Whereas traditional networks must learn to propagate information and can fail catastrophically for bad parameters, residual networks propagate information by default. They are a general-purpose tool (often combined with convolutional layers) enabling reliable training of networks with hundreds of layers.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]