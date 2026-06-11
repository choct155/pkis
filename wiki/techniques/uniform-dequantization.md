---
aliases: []
also_type: []
applies:
- normalizing-flows
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- language-model-perplexity
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- generative-models
- information-theory
id: pkis:technique:uniform-dequantization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch20
tags:
- dequantization
- log-likelihood
- image-modeling
- normalizing-flows
- discrete-data
title: Uniform Dequantization
understanding: 0
uses:
- elbo
- jensens-inequality
---

## Definition
**Uniform dequantization** converts a discrete generative modeling problem into a continuous one by adding uniform noise to integer-valued data before computing log-likelihoods. For data $x \in \{0,\ldots,255\}^D$ (e.g., pixel intensities), define the dequantized variable $z = x + u$ where $u \sim \operatorname{Uniform}([0,1)^D)$. The log-likelihood of the continuous model on $z$ provides a valid lower bound on the log-likelihood of a discrete model on $x$:
$$\log p(x) \geq \mathbb{E}_{q(z|x)}[\log p(z) - \log q(z|x)].$$

This prevents the pdf from becoming arbitrarily large by concentrating on the discrete support.

### Why it matters
Without dequantization, a continuous density model can achieve unbounded log-likelihood on discrete data by placing infinitely sharp peaks at observed values — a degenerate solution. Uniform dequantization is a simple, standard fix that allows fair comparison of likelihoods across image models. Variational dequantization (using a learned $q(z|x)$) provides a tighter lower bound.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[language-model-perplexity]] — contrasts-with: Discrete data needs dequantization for continuous models; perplexity used instead for text
- [[jensens-inequality]] — uses
- [[normalizing-flows]] — applies
- [[elbo]] — uses: Dequantization lower bound is derived via Jensen's inequality / ELBO
[To be populated during integration]