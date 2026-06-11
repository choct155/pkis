---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- philosophy-of-science
id: pkis:principle:prediction-generation-subroutines-discovery
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch27
tags:
- interpretability
- discovery
- scientific-modeling
- latent-variables
title: Prediction and Generation as Subroutines of Discovery
understanding: 0
---

## Definition
The principle that supervised prediction (conditional likelihood maximisation) and unsupervised generation (unconditional likelihood maximisation) are necessary but not sufficient for scientific discovery. Discovery additionally requires that learned representations be interpretable, stable across training protocols, and actionable by domain experts.

### Why it matters
Neural networks trained purely for prediction or generation may implicitly encode useful structure but expose it in an opaque, unstable form (sensitive to learning rates, random seeds, etc.). Framing discovery as a distinct goal motivates the design of latent variable models with explicit, constrained, and semantically grounded latent factors rather than uninterpretable distributed representations.

### Implications for model design
Models aimed at discovery must balance expressiveness (to capture true structure) against interpretability (so that $z$ is meaningful to end users), often accepting a trade-off in raw predictive performance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]