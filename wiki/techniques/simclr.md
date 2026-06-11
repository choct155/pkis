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
- computer-vision
- deep-learning
id: pkis:technique:simclr
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
tags:
- contrastive-learning
- self-supervised
- representation-learning
- vision
- energy-based-model
title: SimCLR (Simple Contrastive Learning of Representations)
understanding: 0
---

## Definition
SimCLR trains a feature encoder $F:\mathbb{R}^D\to\mathbb{R}^E$ by maximising agreement between two augmented views $x_1=t_1(x)$, $x_2=t_2(x)$ of the same image relative to $n$ in-batch negatives:
$$J = F(t_1(x))^\top F(t_2(x)) - \log\sum_{x^-_i\in N(x)}\exp[F(x^-_i)^\top F(t_1(x))]$$
where $F$ outputs $\ell_2$-normalised embeddings (cosine similarity). The objective is equivalent to maximum-likelihood estimation of a conditional energy-based model $p(x_2|x_1) \propto \exp[F(x_2)^\top F(x_1)]$, with the denominator approximated by a Monte Carlo sum over negatives.

### Why it matters
SimCLR demonstrated that careful data augmentation (random cropping + colour jitter + flip) and a nonlinear projection head yield representations competitive with supervised ImageNet pre-training under linear evaluation. The momentum variant **MoCo** extends it to small-batch settings via an exponential-moving-average memory bank of past negatives.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]