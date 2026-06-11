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
- robotics
- computer-vision
- machine-learning
id: pkis:concept:perceptual-aliasing
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch27
tags:
- inverse-problems
- ill-posed
- sensor-limitations
- ambiguity
title: Perceptual Aliasing
understanding: 0
---

## Definition
Perceptual aliasing occurs when distinct world states $z \neq z'$ produce identical (or indistinguishable) observations $x$, i.e., $p(x|z) = p(x|z')$. Formally, the observation mapping is not injective: $|\{z : p(x|z) > 0\}| > 1$ for some $x$.

### Why it matters
Perceptual aliasing is the core difficulty of inverse modeling: the observation alone does not uniquely identify the latent state. It arises in robotics (two corridors look the same), computer vision (different 3-D scenes project to the same 2-D image), and any sensor with limited resolution or information. Resolving aliasing requires a prior $p(z)$, history, or additional observations. It directly motivates belief-state representations and POMDP formulations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]