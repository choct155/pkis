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
- deep-learning
id: pkis:technique:test-time-adaptation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
tags:
- domain-adaptation
- online-learning
- entropy-minimization
- self-supervised
title: Test-Time Adaptation (TTA)
understanding: 0
---

## Definition
Test-time adaptation (TTA) updates model parameters *at inference time* using only unlabeled test data, without access to the original source training set. Common objectives include entropy minimization on a batch of test examples,
$$\min_w \mathcal{H}\!\left(\bar{p}(y|x,w)\right), \quad \bar{p}(y|x,w) = \frac{1}{B}\sum_{b=1}^B p(y|\tilde{x}_b,w)$$
where $\tilde{x}_1,\ldots,\tilde{x}_B$ are augmented copies of $x$.

### Why it matters
TTA allows a deployed model to track distribution shift continuously without re-training from scratch or requiring any target labels. The TENT method minimizes predictive entropy; TTT uses a self-supervised proxy task (e.g., rotation prediction) trained simultaneously with the main task; MEMO minimizes marginal entropy over augmented views of a single test point.

### Contrast with UDA
Unlike unsupervised domain adaptation (UDA), TTA does not assume access to the source data distribution at adaptation time.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]