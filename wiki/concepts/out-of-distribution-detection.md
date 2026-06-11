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
- statistics
id: pkis:concept:out-of-distribution-detection
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
tags:
- anomaly-detection
- novelty-detection
- uncertainty
- safety
- selective-prediction
title: Out-of-Distribution Detection
understanding: 0
---

## Definition
Out-of-distribution (OOD) detection is the problem of deciding, given a single test point $x \sim q$, whether $x$ is **in-distribution** (ID, drawn from the training source $p$) or **out-of-distribution** (drawn from a different distribution $q \neq p$), typically by thresholding a scalar score $s(x)$.

### Why it matters
High-performing discriminative models can be confidently wrong on OOD inputs. Detecting OOD samples allows a system to abstain, route to a human, or trigger a retraining cycle, improving safety in deployed systems. Methods include max-class probability, energy scores, likelihood ratios $\log p(x)/q_0(x)$, reconstruction error, and conformal prediction.

### Key failure mode
For deep generative models, raw log-likelihood $\log p(x)$ is an unreliable OOD score because OOD data can receive *higher* likelihood than in-distribution data (the typicality gap). Using a log-likelihood ratio against a background model mitigates this.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]