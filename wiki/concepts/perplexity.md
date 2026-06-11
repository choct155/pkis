---
aliases: []
also_type: []
applies:
- language-model
- n-gram-language-model
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
- natural-language-processing
id: pkis:concept:perplexity
instantiates:
- cross-entropy-loss
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch06
- murphy-pml2-advanced-ch05
tags:
- language-model
- evaluation
- cross-entropy
- branching-factor
title: Perplexity
understanding: 0
uses:
- cross-entropy
- entropy
- binary-entropy-function
- cross-entropy-loss
---

## Definition
$$\text{perplexity}(p) \triangleq 2^{\mathbb{H}(p)}$$

For evaluating a model $p$ against data $\mathcal{D}$, the cross-entropy perplexity is
$$\text{perplexity}(p_{\mathcal{D}}, p) \triangleq 2^{\mathbb{H}_{ce}(p_{\mathcal{D}},p)} = \sqrt[N]{\prod_{n=1}^{N}\frac{1}{p(x_n)}}$$
the geometric mean of the inverse predictive probabilities, interpretable as the **effective branching factor** of the model.

### Why it matters
Perplexity is the standard evaluation metric for language models: a model with perplexity $K$ behaves as if it is equally uncertain among $K$ outcomes at each step. Because $\mathbb{H}(p^*)\le\mathbb{H}_{ce}(p^*,p)$, the perplexity of any model is bounded below by the entropy of the true process, giving a meaningful theoretical floor. Lower perplexity implies higher predictive accuracy and, via source coding, shorter expected code length.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[cross-entropy-loss]] — uses
- [[binary-entropy-function]] — uses
- [[cross-entropy-loss]] — instantiates
- [[n-gram-language-model]] — applies
- [[language-model]] — applies
- [[entropy]] — uses
- [[cross-entropy]] — uses
[To be populated during integration]