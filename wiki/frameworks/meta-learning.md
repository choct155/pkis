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
contrasts-with:
- pretraining-and-fine-tuning
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
extends:
- domain-generalization
id: pkis:framework:meta-learning
instantiates:
- hierarchical-bayesian-models
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
specializes:
- transfer-learning
tags:
- few-shot-learning
- transfer-learning
- hierarchical-bayes
- adaptation
title: Meta-Learning
understanding: 0
---

## Definition
Meta-learning ("learning to learn") trains a meta-learner on a distribution of tasks $\{\mathcal{T}^j\}$ so that, given a small support set $D^{\text{tr}}$ from a new task $\mathcal{T}^{J+1}$, it can quickly adapt and generalize to the task's query set $D^{\text{te}}$:

$$\min_\theta \mathbb{E}_{\mathcal{T}}\left[\mathcal{L}^{\text{te}}\!\left(\mathcal{A}_\theta(D^{\text{tr}}),\, D^{\text{te}}\right)\right]$$

where $\mathcal{A}_\theta$ is a parameterized adaptation algorithm.

### Why it matters
Meta-learning enables few-shot learning: after training on many tasks, a model can learn a new task from only a handful of labeled examples. The framework unifies gradient-based inner-loop adaptation (MAML), metric-based methods (prototypical networks), and amortized/Bayesian approaches under a hierarchical Bayesian interpretation.

### Relation to domain generalization
Meta-learning and DG both involve training across multiple distributions, but meta-learning explicitly simulates the train/test split for each task during meta-training, enabling learning of an adaptation procedure.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[pretraining-and-fine-tuning]] — contrasts-with
- [[transfer-learning]] — specializes
- [[hierarchical-bayesian-models]] — instantiates
- [[domain-generalization]] — extends
[To be populated during integration]