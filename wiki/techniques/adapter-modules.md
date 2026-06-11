---
aliases: []
also_type: []
applies:
- transformer-attention-mechanisms
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
- deep-learning
- nlp
- computer-vision
id: pkis:technique:adapter-modules
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
specializes:
- transfer-learning-fine-tuning
tags:
- parameter-efficient
- fine-tuning
- transformer
- resnet
- low-rank
title: Adapter Modules
understanding: 0
uses:
- low-rank-approximation
---

## Definition
Adapters are small trainable parameter blocks inserted into a frozen pretrained model to specialise it for a new task without updating the backbone. For a transformer layer with feature dimension $D$ and bottleneck size $M$, an adapter MLP introduces $O(DM)$ new parameters per layer with a residual (skip) connection so that initialisation to zero implements the identity map. For a ResNet, a $1\times1$ convolution $\alpha \in \mathbb{R}^{C\times D}$ yields either a *series* perturbation
$$\mathbf{y} = (\text{diag}_1(\mathbf{I}+\alpha)\circledast\mathbf{f})\circledast\mathbf{x}$$
or a *parallel* (additive) perturbation
$$\mathbf{y} = (\mathbf{f}+\text{diag}_L(\alpha))\circledast\mathbf{x}$$
both interpretable as low-rank perturbations to the original filter $\mathbf{f}$.

### Why it matters
Adapters enable **parameter-efficient fine-tuning**: only ~1–10% of original parameters are trained per task, the backbone is reused across tasks without storage overhead, and empirically adapters match or exceed full fine-tuning on NLP benchmarks. They are a precursor to modern PEFT methods such as LoRA.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[transformer-attention-mechanisms]] — applies
- [[low-rank-approximation]] — uses: Series and parallel adapter perturbations are low-rank modifications to convolutional filters.
- [[transfer-learning-fine-tuning]] — specializes: Adapters are parameter-efficient fine-tuning: backbone frozen, only small bottleneck modules trained.
[To be populated during integration]