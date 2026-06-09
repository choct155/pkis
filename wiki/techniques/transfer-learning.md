---
aliases: []
also_type: []
applies:
- data-hunger
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- deep-learning
id: pkis:technique:transfer-learning
knowledge_type: technique
maturity: evolving
related_concepts:
- '[[inductive-bias]]'
- '[[compositionality]]'
- '[[data-hunger]]'
sources:
- '[[marcus-dl-critical-appraisal-2018]]'
tags:
- generalization
- fine-tuning
- domain-adaptation
- representation-learning
- few-shot
title: Transfer Learning
understanding: 0
uses:
- gradient-descent
---

A learning paradigm in which a model trained on one task or domain is adapted (fine-tuned or directly applied) to a related but different task or domain, with the expectation that representations learned in the source task are useful for the target. Marcus (2018) argues that current deep learning's transfer is severely limited — systems that learn Atari games fail on minor perturbations, and models trained on SQuAD drop precipitously when distractor sentences are inserted — reflecting that learned correlations are brittle interpolations within training space rather than generalizable abstractions.

## Reading Path
- [[marcus-dl-critical-appraisal-2018]] (unread) — §3.2 documents concrete transfer failures in deep RL (Atari game perturbations) and NLP (SQuAD distractor attacks); primary treatment in this corpus

## Connections
- [[data-hunger]] — applies
- [[gradient-descent]] — uses: pretrained weights are copied then fine-tuned by gradient descent on the target task