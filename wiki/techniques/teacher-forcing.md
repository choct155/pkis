---
aliases: []
also_type: []
applies:
- recurrent-neural-network
- language-model
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- backpropagation-through-time
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- deep-learning
- sequence-modeling
id: pkis:technique:teacher-forcing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch10
- murphy-pml1-intro-ch15
tags:
- RNN
- training
- autoregressive
- exposure-bias
- maximum-likelihood
title: Teacher Forcing
understanding: 0
uses:
- maximum-likelihood-estimation
- encoder-decoder-seq2seq
- backpropagation-through-time
- distribution-shift
---

## Definition
During training of an autoregressive/recurrent model, **teacher forcing** feeds the *ground-truth* target $y^{(t)}$ as the input at the next time step $t+1$, rather than the model's own prediction. It arises directly from the conditional maximum-likelihood objective:
$$\log p(y^{(1)},\ldots,y^{(\tau)}\mid x) = \sum_t \log p\!\left(y^{(t)} \mid y^{(1)},\ldots,y^{(t-1)}, x\right).$$
Maximizing this sum means conditioning on observed $y^{(t-1)}$ during training, which decouples time steps and enables parallelism.

### Why it matters
Teacher forcing dramatically accelerates training for output-recurrent networks by removing the dependency on previous hidden states, but it creates an *exposure bias*: the model sees only ground-truth history during training and its own (potentially erroneous) outputs at test time (open-loop mode). Mitigation strategies include scheduled sampling and mixing teacher-forced and free-running inputs.

### Limitations
Exposure bias can hurt generation quality; scheduled sampling (Bengio et al., 2015) gradually replaces ground-truth inputs with sampled outputs to bridge the gap.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[distribution-shift]] — uses: Exposure bias is a train-test distribution mismatch caused by teacher forcing
- [[language-model]] — applies
- [[backpropagation-through-time]] — uses
- [[encoder-decoder-seq2seq]] — uses
- [[maximum-likelihood-estimation]] — uses
- [[recurrent-neural-network]] — applies
- [[backpropagation-through-time]] — contrasts-with: Teacher forcing avoids BPTT in output-recurrent models by decoupling time steps
[To be populated during integration]