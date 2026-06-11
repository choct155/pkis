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
- machine-learning
- weakly-supervised-learning
id: pkis:concept:multi-instance-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
tags:
- weak-supervision
- bags
- medical-imaging
- label-noise
- partial-labels
title: Multi-Instance Learning
understanding: 0
---

## Definition
In multi-instance learning (MIL) the training data consists of *bags* $x_n=\{x_{n,1},\ldots,x_{n,B}\}$, each with a single bag-level label $y_n$ but no instance-level labels. Under the standard assumption:
$$y_n = \bigvee_{b=1}^B y_{nb}$$
a bag is positive iff at least one instance is positive, and negative only when all instances are negative. The learning task is to infer instance-level predictions and/or a bag-level classifier without observing which instance caused each positive label.

### Why it matters
MIL naturally models weakly supervised problems in medical imaging (a scan is positive if any patch contains a lesion), document classification (a document is positive if any sentence supports the claim), and drug activity prediction. It is a special case of weakly supervised learning that lies between fully supervised and unsupervised settings.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]