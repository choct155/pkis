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
- machine learning
- natural language processing
id: pkis:technique:minimum-bayes-risk-decoding
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch34
tags:
- structured prediction
- decoding
- loss function
- NLP
- posterior sampling
title: Minimum Bayes Risk (MBR) Decoding
understanding: 0
---

## Definition
$$\hat{y} = \operatorname*{arg\,min}_{\hat{y}' \in \mathcal{Y}} \sum_{y \in \mathcal{Y}} p(y|x)\, \ell(y, \hat{y}')$$

MBR decoding selects the output that minimises expected loss under the model posterior, rather than the single most probable output. In practice the expectation is approximated with $M$ samples from the posterior:
$$\hat{y} \approx \operatorname*{arg\,min}_{y^i} \sum_{j=1}^{M} p(y^j|x)\, \ell(y^j, y^i)$$
This is called *empirical MBR*.

### Why it matters
MAP/greedy decoding optimises for the single most probable output, which can be misleading in structured prediction (NLP, vision) when the posterior is multi-modal. MBR explicitly trades off diversity and task-relevant loss, yielding outputs that are more typical of the posterior and better calibrated to the downstream metric.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]