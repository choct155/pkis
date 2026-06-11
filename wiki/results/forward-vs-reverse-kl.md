---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- information-theory
- machine-learning
- probabilistic-inference
id: pkis:result:forward-vs-reverse-kl
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch06
tags:
- KL-divergence
- variational-inference
- mode-seeking
- mode-covering
title: Forward vs Reverse KL Divergence Asymmetry
understanding: 0
---

## Definition
Let $q$ be a tractable approximation to a target $p$.

- **Forward (inclusive) KL** $D_{\mathrm{KL}}(p\|q)$: minimisation forces $q(x)>0$ wherever $p(x)>0$ (*zero-avoiding / mode-covering*); $q$ tends to over-estimate the support of $p$.
- **Reverse (exclusive) KL** $D_{\mathrm{KL}}(q\|p)$: minimisation forces $q(x)=0$ wherever $p(x)=0$ (*zero-forcing / mode-seeking*); $q$ locks onto a single mode and under-estimates the support.

When $p$ is multimodal and $q$ is constrained to be unimodal, minimising the forward KL produces an approximation that spans all modes (high variance), while minimising the reverse KL selects one mode (low variance).

### Why it matters
This asymmetry drives the difference between variational EM / mean-field VI (reverse KL, mode-seeking) and score-based / energy-based models trained with forward KL (mode-covering). Understanding it is essential for choosing the right objective in approximate inference and generative modelling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]