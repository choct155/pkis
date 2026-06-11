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
- statistics
- frequentist-statistics
- hypothesis-testing
id: pkis:concept:p-value-nhst
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch03
tags:
- p-value
- NHST
- hypothesis-testing
- frequentist
- significance
title: p-value and Null Hypothesis Significance Testing (NHST)
understanding: 0
---

## Definition
The **p-value** for a test statistic $t(D)$ is the tail probability under the null hypothesis $H_0$:
$$\text{pval}(t(D)) \triangleq \Pr\bigl(t(\tilde{D})\geq t(D)\mid \tilde{D}\sim H_0\bigr)$$

**NHST** (null hypothesis significance testing) rejects $H_0$ when $\text{pval}<\alpha$ (typically $0.05$). A small p-value means the observed statistic is unlikely *under $H_0$*, but does **not** equal the probability that $H_0$ is false: it ignores $p(D|H_1)$ and the prior $p(H_0)$.

### Why it matters
The p-value conflates $\Pr(\text{data}|H_0)$ with $\Pr(H_0|\text{data})$; the latter requires Bayes' rule and knowledge of $p(D|H_1)$. This modus-tollens fallacy leads to widespread misinterpretation. Proper Bayesian hypothesis testing uses the Bayes factor $p(D|H_0)/p(D|H_1)$ together with prior odds, yielding a posterior probability of each hypothesis. Several journals have restricted or banned p-values in response to reproducibility concerns.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]