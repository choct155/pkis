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
- computer-vision
- machine-learning
id: pkis:technique:classifier-cascade
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch12
tags:
- face-detection
- efficiency
- conditional-computation
- object-detection
- cascaded
title: Dynamic Cascade of Classifiers
understanding: 0
---

## Definition
A classifier cascade is a sequence of $K$ classifiers $f_1, \ldots, f_K$ arranged in order of increasing capacity and cost. Each classifier either accepts an input as a positive (passing it to the next stage) or rejects it. For rare-object detection the pipeline maximises recall at each early stage and precision at the final stage:
$$\text{decision}(\mathbf{x}) = \begin{cases} \text{reject} & \text{if any } f_k(\mathbf{x}) = \text{negative}\\ \text{accept} & \text{if all } f_k(\mathbf{x}) = \text{positive.}\end{cases}$$
Average inference cost is low because most inputs are rejected cheaply by early, simple classifiers.

### Why it matters
Enables real-time detection of rare objects (e.g., faces in images, Viola–Jones 2001) by spending computation only where necessary; also used in address-number transcription pipelines and as a form of hard attention. Exemplifies the principle of conditional/dynamic computation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]