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
- deep-learning
- probabilistic-graphical-models
id: pkis:concept:fast-pcd
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch18
tags:
- RBM
- undirected-models
- MCMC-training
- Markov-chain-mixing
title: Fast PCD (FPCD)
understanding: 0
---

## Definition
**Fast PCD** (FPCD; Tieleman & Hinton, 2009) accelerates Markov chain mixing during PCD training by splitting model parameters into slow and fast copies:
$$\theta = \theta^{(\text{slow})} + \theta^{(\text{fast})}.$$
The fast parameters are updated with a much larger learning rate and penalized by strong weight decay, so they transiently take large values to push the Markov chain to new territory (forcing rapid mode-hopping) and then decay back to zero. Only the slow parameters are used at test time.

### Why it matters
FPCD addresses the chain-lag problem of SML/PCD: if the model changes faster than the chains mix, the negative phase samples become stale. By temporarily exaggerating parameter values, FPCD forces the chain to explore the model's distribution more aggressively during training. The fast weights incur no lasting model change (due to decay) but act as a transient annealing mechanism, bridging different modes without requiring parallel tempering or increased $k$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]