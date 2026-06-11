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
- computer-vision
- machine-learning
- cognitive-science
id: pkis:concept:vision-as-inverse-graphics
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch27
tags:
- inverse-problems
- generative-models
- scene-understanding
- MAP-inference
- perception
title: Vision as Inverse Graphics (Analysis by Synthesis)
understanding: 0
---

## Definition
$$\hat{z} = \arg\max_z \left[\log p(z) + \log p(x|z)\right]$$

An approach to computer vision in which perception is cast as Bayesian inversion of a generative (graphics) model: given an observed image $x$, infer the latent 3-D scene description $z$ (objects, surfaces, lighting) that most plausibly produced it. The name reflects the duality with computer graphics, which maps $z \to x$.

### Why it matters
Inverse graphics provides a principled probabilistic account of how a visual system can recover rich scene structure from impoverished retinal data. It motivates analysis-by-synthesis architectures—e.g., rendering-based differentiable simulators and generative scene models—used in robotics, AR/VR, and neuroscience models of visual cortex.

### Perceptual aliasing
Because the forward rendering map is many-to-one (different scenes can produce the same image), the inverse problem is ill-posed without a prior over scenes. MAP or full Bayesian inference over $z$ resolves this ambiguity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]