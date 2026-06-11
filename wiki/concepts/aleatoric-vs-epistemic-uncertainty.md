---
aliases: []
also_type: []
applies:
- exploration-exploitation-tradeoff
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
- conformal-prediction
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- bayesian-methods
id: pkis:concept:aleatoric-vs-epistemic-uncertainty
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch03
- murphy-pml2-advanced-ch14
specializes:
- uncertainty-quantification
tags:
- uncertainty
- epistemic
- aleatoric
- bayesian-prediction
- active-learning
title: Aleatoric vs Epistemic Uncertainty
understanding: 0
uses:
- bayesian-posterior-predictive
- bayesian-inference
- law-of-total-variance
---

## Definition
$$\text{Total uncertainty} = \underbrace{\text{Epistemic uncertainty}}_{\text{reducible, from lack of knowledge}} + \underbrace{\text{Aleatoric uncertainty}}_{\text{irreducible, intrinsic noise}}$$

**Aleatoric (intrinsic) uncertainty** is the variance in outcomes that persists even if the true model and parameters were known — it is the irreducible noise in the data-generating process. **Epistemic (knowledge) uncertainty** arises because we have limited data and thus imprecise knowledge of the parameters; it can in principle be reduced by collecting more data.

In Bayesian predictive inference the posterior predictive distribution $$p(y|x,D)=\int p(y|x,\theta)p(\theta|D)\,d\theta$$ captures both sources, whereas the plug-in approximation $p(y|x,\hat{\theta})$ captures only aleatoric uncertainty.

### Why it matters
Disentangling the two types is critical for active learning (query where epistemic uncertainty is highest), safe / risk-sensitive decision-making, and model diagnostics. Bayesian models whose error bars widen away from training data exhibit this decomposition naturally, while plugin / MLE models do not.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[conformal-prediction]] — contrasts-with
- [[law-of-total-variance]] — uses
- [[exploration-exploitation-tradeoff]] — applies
- [[bayesian-inference]] — uses
- [[uncertainty-quantification]] — specializes
- [[bayesian-posterior-predictive]] — uses
[To be populated during integration]