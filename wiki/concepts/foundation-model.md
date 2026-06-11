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
- natural-language-processing
- deep-learning
id: pkis:concept:foundation-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch22
tags:
- foundation-model
- pre-training
- transfer-learning
- LLM
- scaling
- emergent-capabilities
title: Foundation Model
understanding: 0
uses:
- transfer-learning
- neural-scaling-laws
- pretraining-and-fine-tuning
- llm-hallucination
---

## Definition
A **foundation model** is a large-scale model trained on broad data (typically via self-supervised or autoregressive objectives) that can be adapted to a wide range of downstream tasks with minimal task-specific training:
$$\theta^* = \arg\max_\theta \sum_{t} \log p(x_t \mid x_{1:t-1}; \theta), \quad \text{on a large heterogeneous corpus}.$$
The term was coined by the Stanford Center for Research on Foundation Models (2021).

### Why it matters
Foundation models shift the AI development paradigm from training specialist models per task to *pre-train-once, adapt-many*. LLMs (GPT-3, PaLM), vision-language models (CLIP, DALL-E), and protein models (ESMFold) are all instances. Their scale enables emergent capabilities not present in smaller models, but raises concerns about bias, hallucination, resource consumption, and alignment.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[llm-hallucination]] — uses: LLM hallucination is a key failure mode of foundation models
- [[pretraining-and-fine-tuning]] — uses
- [[neural-scaling-laws]] — uses
- [[transfer-learning]] — uses
[To be populated during integration]