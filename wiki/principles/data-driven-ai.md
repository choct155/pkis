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
- artificial-intelligence
- machine-learning
id: pkis:principle:data-driven-ai
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch01
tags:
- empirical-risk
- machine-learning
- knowledge-bottleneck
- big-data
title: Data-Driven AI (Learning from Experience)
understanding: 0
---

## Definition
The data-driven AI principle holds that **AI systems should acquire knowledge by extracting statistical patterns from raw data** rather than by having knowledge hand-coded as explicit rules by human experts.

Formally: rather than specifying a mapping $f: \mathcal{X} \to \mathcal{Y}$ symbolically, allow an algorithm $\mathcal{A}$ to approximate $f$ by minimizing empirical risk $\hat{R}(f) = \frac{1}{n}\sum_{i=1}^n L(f(x_i), y_i)$ over a dataset $\{(x_i, y_i)\}_{i=1}^n$.

### Why it matters
The difficulty of formally specifying informal human knowledge (the *knowledge acquisition bottleneck*) makes rule-based AI brittle. A data-driven approach scales gracefully: more data generally means better performance, and the system automatically adapts to the complexity of the domain.

### Scale threshold (empirical)
As of ~2016, supervised deep learning typically achieves acceptable performance with ~5,000 labeled examples per class, and matches or exceeds human performance with ≥10 million labeled examples.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]