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
- debugging
- deep-learning
id: pkis:technique:fit-tiny-dataset-debug
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch11
tags:
- debugging
- sanity-check
- overfitting
- unit-test
title: Fit-a-Tiny-Dataset Debugging Test
understanding: 0
---

## Definition
The **fit-a-tiny-dataset** test deliberately trains a model on a very small dataset (as few as one example) to verify that the optimisation pipeline can achieve near-zero training loss. If a model cannot memorise a single training example, the fault lies in the software rather than in generalisation capacity:

$$\text{if } \hat{\mathcal{L}}_{\text{train}}(\mathcal{D}_1) > \delta \text{ after } T \text{ steps, suspect a bug.}$$

### Why it matters
Many neural network bugs — wrong loss function, disabled gradients, mismatched label encoding — are invisible when inspecting outputs on a full dataset because other components compensate. Overfit a tiny dataset first: this is the fastest test that isolates optimisation correctness from generalisation capacity, and it is especially useful for detecting evaluation bugs (e.g., incorrect metric computation) that can mislead practitioners into believing a broken system is working.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]