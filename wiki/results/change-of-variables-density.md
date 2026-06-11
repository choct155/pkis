---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability-theory
- statistics
- machine-learning
extends:
- probability-density-function
id: pkis:result:change-of-variables-density
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- normalizing-flows
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
tags:
- Jacobian
- normalizing-flows
- variable-transformation
- density
title: Change-of-Variables Formula for Probability Densities
understanding: 0
uses:
- gradient-and-jacobian
- determinant
---

## Definition
Let $\mathbf{y} = g(\mathbf{x})$ where $g$ is an invertible, differentiable mapping. Then the density of $\mathbf{y}$ is
$$p_y(\mathbf{y}) = p_x(g^{-1}(\mathbf{y}))\left|\det\!\left(\frac{\partial g^{-1}(\mathbf{y})}{\partial \mathbf{y}}\right)\right|.$$
Equivalently, $p_x(\mathbf{x}) = p_y(g(\mathbf{x}))\left|\det\!\left(\frac{\partial g(\mathbf{x})}{\partial \mathbf{x}}\right)\right|$. The absolute Jacobian determinant corrects for how $g$ stretches or compresses volume.

### Why it matters
This formula is the foundation of **normalizing flows**: a sequence of invertible transformations with tractable Jacobians can convert a simple base density into an arbitrarily complex target density. Ignoring the Jacobian is a common mistake that produces unnormalized densities.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[determinant]] — uses
- [[gradient-and-jacobian]] — uses
- [[normalizing-flows]] — prerequisite-of
- [[probability-density-function]] — extends
[To be populated during integration]