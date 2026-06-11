---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- representation-learning
id: pkis:framework:transfer-learning-domain-adaptation
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch15
tags:
- transfer
- domain-adaptation
- few-shot
- zero-shot
- fine-tuning
- multi-task
title: Transfer Learning and Domain Adaptation
understanding: 0
---

## Definition
A learning paradigm in which knowledge acquired from a source distribution $P_1$ (or task $T_1$) is exploited to improve generalisation on a target distribution $P_2$ (or task $T_2$). Formally, a model trained on $(\mathbf{x}, y) \sim P_1$ provides an initialisation, a feature extractor, or a prior that accelerates learning under $P_2$:

- **Transfer learning**: $P_1 \neq P_2$, tasks may differ; shared lower-layer representations are reused.
- **Domain adaptation**: task is identical but $p_1(\mathbf{x}) \neq p_2(\mathbf{x})$; the input-to-output mapping is constant.
- **Concept drift**: gradual temporal shift of $P$, treated as sequential transfer.
- **One-shot / zero-shot learning**: transfer so efficient that 1 or 0 target labels suffice.

### Why it matters
Transfer learning is the dominant paradigm for modern deep learning practice (ImageNet-pretrained convnets, pretrained language models). It is theoretically justified whenever the source and target share underlying causal factors, allowing a shared representation to carry statistical strength across tasks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]