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
contrasts-with:
- selection-bias
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- causality
id: pkis:concept:covariate-shift
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
specializes:
- distribution-shift
tags:
- distribution-shift
- domain-adaptation
- importance-weighting
- robustness
title: Covariate Shift
understanding: 0
uses:
- causal-vs-anticausal-prediction
---

## Definition
$$q(x, y) = q(x)\,p(y|x), \quad q(x) \neq p(x)$$

Covariate shift (also called **domain shift**) occurs in a causal/discriminative model when the marginal distribution of inputs $p(x)$ changes between source and target, while the conditional $p(y|x)$ remains the same.

### Why it matters
Even though the conditional $p(y|x)$ is unchanged, a model trained on $p(x)$ will implicitly rely on features that are predictive *within* the training support; when $q(x)$ shifts that support, accuracy can degrade sharply. Correcting for covariate shift requires re-weighting training samples by the density ratio $w(x) = q(x)/p(x)$, or employing domain adaptation.

### Relation to other shifts
Covariate shift is one of four canonical shift types: the other three are concept shift (change in $p(y|x)$), label shift (change in $p(y)$), and manifestation shift (change in $p(x|y)$). Under covariate shift, importance-weighted ERM and domain adversarial learning are standard remedies.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[selection-bias]] — contrasts-with
- [[causal-vs-anticausal-prediction]] — uses
- [[distribution-shift]] — specializes
[To be populated during integration]