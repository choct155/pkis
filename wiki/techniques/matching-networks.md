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
- few-shot-learning
- meta-learning
id: pkis:technique:matching-networks
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
tags:
- few-shot
- attention
- episodic-training
- metric-learning
- in-context
title: Matching Networks
understanding: 0
---

## Definition
Matching networks define a semi-parametric few-shot classifier by attending over a labeled support set $S=\{(x_n,y_n)\}$:
$$p_\theta(y|x,S) = \sum_{n\in S} a_\theta(x,x_n;S)\,y_n$$
where the attention kernel uses cosine similarity in a learned embedding space:
$$a(x,x_n;S) = \frac{\exp(c(f(x),g(x_n)))}{\sum_{n'}\exp(c(f(x),g(x_{n'})))}$$
The embedding functions $f$ and $g$ are trained episodically: sample a task (support set $S$, query set $T$ from disjoint classes), then maximise $\sum_{(x,y)\in T}\log p_\theta(y|x,S)$.

### Why it matters
Matching networks pioneer the *episodic training* paradigm that aligns training and test conditions in few-shot learning. By conditioning predictions on the support set rather than fixed class centroids, the model implicitly learns which features discriminate the current set of classes — a form of in-context learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]