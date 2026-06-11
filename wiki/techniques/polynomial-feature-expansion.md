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
- statistics
extends:
- linear-regression
id: pkis:technique:polynomial-feature-expansion
instantiates:
- overfitting-and-underfitting
- bias-variance-tradeoff
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch01
specializes:
- basis-function-models
- feature-engineering
tags:
- feature-engineering
- basis-functions
- nonlinear-regression
- overfitting
title: Polynomial Feature Expansion
understanding: 0
---

## Definition
A feature preprocessing technique that augments an input $x \in \mathbb{R}$ (or $\mathbb{R}^D$) with its powers up to degree $D$:
$$\phi(x) = [1,\, x,\, x^2,\, \ldots,\, x^D] \in \mathbb{R}^{D+1}$$
allowing a linear model $f(x;w) = w^\top \phi(x)$ to represent polynomial functions of the original input while remaining linear in parameters $w$.

### Why it matters
Polynomial expansion is the simplest instance of the basis-function / kernel trick idea: by manually lifting inputs to a richer feature space, a linear model gains nonlinear expressive power with a unique, analytically tractable optimum (via least squares). It also serves as the canonical illustration of the bias-variance tradeoff and overfitting.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[feature-engineering]] — specializes
- [[bias-variance-tradeoff]] — instantiates
- [[overfitting-and-underfitting]] — instantiates
- [[linear-regression]] — extends
- [[basis-function-models]] — specializes
[To be populated during integration]