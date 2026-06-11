---
aliases: []
also_type: []
applies:
- neural-networks
- convolutional-neural-networks
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
- interpretability
- computer-vision
id: pkis:concept:saliency-map
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch33
specializes:
- post-hoc-explanation
tags:
- saliency
- attribution
- gradients
- integrated-gradients
- interpretability
- local-explanation
title: Saliency Map (Attribution Map)
understanding: 0
uses:
- explanation-fidelity
- gradient-and-jacobian
---

## Definition
A **saliency map** (attribution map) is a function $s: \mathcal{X} \to \mathbb{R}^d$ that assigns an importance score to each input dimension $i$ for a given model prediction $f(x)$.

The gradient-based variant computes:
$$s_i(x) = \left|\frac{\partial f(x)}{\partial x_i}\right|$$
or integrated variants such as Integrated Gradients:
$$s_i(x) = (x_i - x_i^\text{ref}) \int_0^1 \frac{\partial f(x^\text{ref} + \alpha(x-x^\text{ref}))}{\partial x_i} d\alpha$$

Saliency maps provide a **local** post-hoc explanation identifying which input dimensions most influenced a specific prediction.

### Why it matters
Saliency maps are the dominant interpretability method for image, audio, and text models where individual input dimensions (pixels, amplitudes, tokens) carry semantic meaning in aggregate. However, they are vulnerable to several failure modes: (1) gradient saturation in piece-wise-constant models gives misleading zero gradients; (2) adversarial perturbations can produce similar saliency maps for inputs with opposite predictions; (3) visualization artifacts (masking, percentile clipping) can misrepresent importance to human viewers.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gradient-and-jacobian]] — uses: Gradient-based saliency maps are computed as the Jacobian of the output w.r.t. input.
- [[explanation-fidelity]] — uses
- [[convolutional-neural-networks]] — applies
- [[neural-networks]] — applies: Gradient-based saliency maps are computed with respect to a neural network's input.
- [[post-hoc-explanation]] — specializes
[To be populated during integration]