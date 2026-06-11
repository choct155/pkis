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
- information-theory
id: pkis:concept:self-information
instantiates:
- shannon-information-content
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- entropy
- kl-divergence
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
specializes:
- information-theory
tags:
- surprisal
- Shannon
- nats
- bits
title: Self-Information
understanding: 0
---

## Definition
The **self-information** (or surprisal) of an event $x$ with probability $P(x)$ is
$$I(x) = -\log P(x).$$
When the logarithm is natural, the unit is the **nat**; with base-2 logarithm the unit is the **bit** (shannon). Rare events yield high self-information; certain events yield zero.

### Why it matters
Self-information is the atomic building block of Shannon's information theory. Shannon entropy is its expectation, and KL divergence measures the average excess self-information when using the wrong distribution. These three quantities cascade logically and appear throughout modern ML in loss functions, model comparison, and compression.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[information-theory]] — specializes
- [[kl-divergence]] — prerequisite-of
- [[shannon-information-content]] — instantiates
- [[entropy]] — prerequisite-of
[To be populated during integration]