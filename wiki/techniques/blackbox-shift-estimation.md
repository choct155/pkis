---
aliases: []
also_type: []
applies:
- label-shift
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- importance-weighted-erm
- maximum-likelihood-estimation
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:technique:blackbox-shift-estimation
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
tags:
- label-shift
- unsupervised-adaptation
- confusion-matrix
- moment-matching
title: Blackbox Shift Estimation
understanding: 0
---

## Definition
$$\boldsymbol{\mu} = C\,\mathbf{q} \;\Longrightarrow\; \hat{\mathbf{q}} = C^{-1}\boldsymbol{\mu}$$

Blackbox shift estimation (BBSE) estimates the target label distribution $q(y)$ under the label-shift assumption by inverting the confusion matrix $C_{ij}=p(\hat{y}=i|y=j)$—estimated on the source—against the vector $\mu_i = q(\hat{y}=i)$ of empirical prediction frequencies on the unlabeled target set.

### Why it matters
No target labels are needed; only the marginal prediction frequencies on the target data and the source-domain confusion matrix are required. Once $\hat{\mathbf{q}}$ is obtained, a discriminative classifier trained on the source can be corrected by reweighting its posteriors: $q(y|x) \propto p(y|x)\,\hat{q}(y)/p(y)$. The method is also useful for *detecting* label shift.

### Requirements
The confusion matrix $C$ must be invertible (strongly-diagonal classifiers satisfy this), no novel labels may appear at test time, and the label-shift assumption $q(x|y)=p(x|y)$ must hold.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[maximum-likelihood-estimation]] — contrasts-with
- [[importance-weighted-erm]] — contrasts-with
- [[label-shift]] — applies
[To be populated during integration]