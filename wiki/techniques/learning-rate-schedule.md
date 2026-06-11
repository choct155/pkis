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
- optimization
- deep-learning
id: pkis:technique:learning-rate-schedule
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch08
- murphy-pml2-advanced-ch06
tags:
- SGD
- warmup
- cosine-decay
- cyclical
- hyperparameter
title: Learning Rate Schedule and Warmup
understanding: 0
---

## Definition
A **learning rate schedule** specifies $\{\eta_t\}$ as a function of iteration $t$. Common forms include:

- **Step decay**: $\eta_t = \eta_0 \gamma^i$ at milestone $i$  
- **Exponential decay**: $\eta_t = \eta_0 e^{-\lambda t}$  
- **Square-root / polynomial decay**: $\eta_t = \eta_0 (\beta t+1)^{-\alpha}$  
- **One-cycle / warmup-then-cosine-decay**: learning rate increases linearly then decreases via cosine annealing  
- **Cyclical learning rate**: periodic triangular oscillation between $\eta_{\min}$ and $\eta_{\max}$

Convergence of SGD requires the **Robbins-Monro conditions**: $\sum_t \eta_t = \infty$ and $\sum_t \eta_t^2 < \infty$.

### Why it matters
The learning rate schedule is often the most impactful hyper-parameter in deep learning training. Warmup avoids instability in poorly conditioned early-training landscapes; cosine decay and cyclical schedules can find flatter minima that generalize better, motivating the SWA technique.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]