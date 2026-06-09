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
- reinforcement-learning
- statistical-learning
id: pkis:technique:kernel-regression-rl
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
specializes:
- memory-based-function-approximation
tags:
- kernel-function
- nonparametric
- memory-based
- kernel-trick
title: Kernel Regression for Value Estimation
understanding: 0
uses:
- the-kernel-trick
---

## Definition
A memory-based value approximator that returns a kernel-weighted average of all stored targets: v̂(s, D) = Σ_{s'∈D} k(s,s') g(s'), where the kernel k(s,s') measures the strength of generalization from s' to s (often a Gaussian RBF centered on stored states). Weighted-average methods are the special case where k is nonzero only for nearby states. Crucially, any linear parametric method with feature vectors x(s) can be recast as kernel regression with k(s,s') = x(s)ᵀ x(s'), yielding the identical approximation—so generalization in linear function approximation is always describable by a kernel (e.g. tile coding's offset patterns correspond to kernels even though it never computes one explicitly). When such an inner-product kernel has a compact closed form, one can work in a high-dimensional implicit feature space without ever computing in it—the kernel trick—making kernel regression less complex than the equivalent parametric method.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[the-kernel-trick]] — uses: inner-product kernels let one work in an implicit high-dimensional feature space without computing in it
- [[memory-based-function-approximation]] — specializes: kernel regression is a memory-based method using a kernel-weighted average of stored targets
[To be populated during integration]