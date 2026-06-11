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
- numerical-methods
- debugging
id: pkis:technique:gradient-checking
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch11
tags:
- debugging
- automatic-differentiation
- finite-differences
- backpropagation
title: Gradient Checking (Finite-Difference Derivative Verification)
understanding: 0
---

## Definition
**Gradient checking** verifies analytic gradient implementations by comparing them to numerical finite-difference estimates. The centered-difference approximation gives

$$f'(x) \approx \frac{f(x + \tfrac{1}{2}\epsilon) - f(x - \tfrac{1}{2}\epsilon)}{\epsilon} + O(\epsilon^2).$$

For vector-valued functions $g:\mathbb{R}^m\to\mathbb{R}^n$, random projections reduce the cost: test $f(x) = \mathbf{u}^\top g(\mathbf{v}x)$ for random vectors $\mathbf{u}, \mathbf{v}$, converting a potentially $mn$-dimensional check into a scalar one.

### Why it matters
Backpropagation bugs are silent — incorrect gradients still reduce training loss via weight adaptation in unaffected parameters. Gradient checking provides a gold-standard unit test for any new differentiable operation, catching sign errors, missing factors, and incorrect chain-rule applications before they silently corrupt training.

### Complex-step variant
Using complex perturbation $f(x + i\epsilon)$ avoids cancellation error and permits $\epsilon\approx 10^{-150}$, achieving machine-precision accuracy.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]