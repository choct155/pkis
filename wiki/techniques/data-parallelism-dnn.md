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
- distributed-computing
id: pkis:technique:data-parallelism-dnn
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch13
tags:
- distributed-training
- GPU
- scalability
- all-reduce
title: Data Parallelism for DNN Training
understanding: 0
---

## Definition
Data parallelism distributes a minibatch across $K$ devices, each holding a complete copy of the model. At each step $t$:
1. Partition minibatch: $\mathcal{D} = \bigcup_k \mathcal{D}_k^t$.
2. Each device $k$ computes local gradient $g_k^t = \nabla_\theta L(\theta;\mathcal{D}_k^t)$.
3. **All-reduce** (sum) gradients: $g_t = \sum_k g_k^t$.
4. Broadcast $g_t$ and update: $\theta \leftarrow \theta - \eta_t g_t$.

**Synchronous** training waits for all devices before updating; **asynchronous / hogwild** training allows independent updates, which can be proved to converge when updates are sparse.

### Why it matters
Data parallelism is the dominant strategy for large-scale DNN training because it is embarrassingly parallel and yields linear speedups in gradient computation. It is the basis of distributed training in all major frameworks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]