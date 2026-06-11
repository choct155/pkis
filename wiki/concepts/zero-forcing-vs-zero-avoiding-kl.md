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
- information-theory
- approximate-inference
id: pkis:concept:zero-forcing-vs-zero-avoiding-kl
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch10
tags:
- KL-divergence
- mode-seeking
- mean-seeking
- variational-inference
- expectation-propagation
title: Zero-Forcing vs. Zero-Avoiding KL Divergence
understanding: 0
---

## Definition
$$\text{KL}(q\|p) = \int q(z)\ln\frac{q(z)}{p(z)}\,dz \quad \text{(zero-forcing / exclusive)}$$
$$\text{KL}(p\|q) = \int p(z)\ln\frac{p(z)}{q(z)}\,dz \quad \text{(zero-avoiding / inclusive)}$$

The two directions of KL divergence produce qualitatively different approximations: $\text{KL}(q\|p)$ penalizes $q>0$ where $p\approx 0$, so the approximation collapses onto one mode of a multimodal $p$; $\text{KL}(p\|q)$ penalizes $q\approx 0$ where $p>0$, so the approximation spreads to cover all mass of $p$, often over-estimating support.

### Why it matters
This asymmetry directly determines whether an approximate inference algorithm (VI uses $\text{KL}(q\|p)$; EP uses $\text{KL}(p\|q)$) will produce compact unimodal or broad diffuse approximations, with major practical consequences for predictive distributions and model comparison.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]