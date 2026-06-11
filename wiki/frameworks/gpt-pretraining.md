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
- natural-language-processing
- deep-learning
- generative-models
id: pkis:framework:gpt-pretraining
instantiates:
- autoregressive-model-arm
- language-model
- foundation-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch22
tags:
- GPT
- LLM
- decoder-only-transformer
- pre-training
- causal-attention
- in-context-learning
title: GPT / Large Language Model Pre-training
understanding: 0
uses:
- transformer-attention-mechanisms
- maximum-likelihood-estimation
- in-context-learning
- neural-scaling-laws
---

## Definition
GPT (Generative Pre-trained Transformer) is a decoder-only transformer trained with maximum-likelihood on the autoregressive objective:
$$\mathcal{L} = -\sum_{t} \log p(y_t \mid y_{1:t-1};\theta).$$
The architecture uses causal (masked) self-attention so that position $t$ attends only to positions $\leq t$. Models are first pre-trained on large text corpora and then optionally fine-tuned on downstream tasks. GPT-2 (1.5B params), GPT-3 (175B params), and ChatGPT (RLHF-aligned GPT-3) represent successive scale-ups.

### Why it matters
GPT demonstrated that a single large-scale autoregressive language model, trained purely with next-token prediction, acquires broad competence across NLP tasks via few-shot and zero-shot prompting (in-context learning). It established the paradigm of *foundation models*: pre-train once at scale, adapt cheaply.

### Scaling and emergent capabilities
Empirical scaling laws (Kaplan et al.) show loss decreases predictably with model size, data, and compute. At sufficient scale, qualitatively new capabilities emerge (chain-of-thought reasoning, code generation, etc.), motivating the continued pursuit of larger models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[neural-scaling-laws]] — uses: GPT scaling follows empirical neural scaling laws
- [[foundation-model]] — instantiates
- [[language-model]] — instantiates
- [[in-context-learning]] — uses: GPT-style models exhibit few-shot in-context learning
- [[maximum-likelihood-estimation]] — uses
- [[autoregressive-model-arm]] — instantiates
- [[transformer-attention-mechanisms]] — uses: GPT uses causal (masked) self-attention in a decoder-only transformer
[To be populated during integration]