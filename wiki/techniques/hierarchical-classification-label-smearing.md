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
id: pkis:technique:hierarchical-classification-label-smearing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch10
tags:
- hierarchical-classification
- label-smearing
- taxonomy
- multi-label
- fine-grained-recognition
title: Hierarchical Classification with Label Smearing
understanding: 0
---

## Definition
A method for classification over a label taxonomy in which training labels are **propagated upward** (smeared) to all ancestor nodes before training. A multi-label classifier trained on smeared data naturally predicts at multiple levels of the hierarchy. Sibling-exclusion constraints enforce consistency:
$$p(\text{dog}|x)+p(\text{cat}|x) = p(\text{mammal}|x)$$
Generalisations allow soft constraints and arbitrary graphical structure.

### Why it matters
Hierarchical label structures arise in fine-grained recognition (species, products, medical codes). Label smearing is a simple, model-agnostic strategy that converts any multi-label classifier into a hierarchically consistent predictor without requiring custom architectures.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]