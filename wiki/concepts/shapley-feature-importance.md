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
- machine-learning
- interpretability
- game-theory
id: pkis:concept:shapley-feature-importance
instantiates:
- shapley-value
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch33
specializes:
- post-hoc-explanation
tags:
- SHAP
- feature-importance
- Shapley-value
- interpretability
- attribution
title: Shapley Feature Importance
understanding: 0
uses:
- explanation-fidelity
- cooperative-game
---

## Definition
**Shapley feature importance** (SHAP) assigns to each feature $i$ of a prediction $f(x)$ a value $\phi_i$ derived from cooperative game theory:
$$\phi_i = \sum_{S \subseteq [d]\setminus\{i\}} \frac{|S|!(d-|S|-1)!}{d!}\bigl[v(S\cup\{i\}) - v(S)\bigr]$$
where $v(S) = \mathbb{E}[f(X) \mid X_S = x_S]$ is the expected model output conditioned on the coalition $S$ of observed features.

The scores satisfy **efficiency** ($\sum_i \phi_i = f(x) - \mathbb{E}[f(X)]$), **symmetry**, **dummy**, and **linearity** axioms.

### Why it matters
Shapley values are the unique additive attribution satisfying the four axioms above, grounding feature importance in a rigorous game-theoretic framework. SHAP provides both local explanations (per-instance attributions) and global summaries (mean absolute SHAP values across the dataset). Key limitations: (1) computing exact Shapley values is exponential in $d$; (2) the expectation over missing features requires modeling the data distribution, and independent-feature approximations can produce unrealistic inputs; (3) Shapley values attribute linear shares but cannot capture interactions between features without higher-order extensions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[cooperative-game]] — uses: SHAP formulates feature attribution as a cooperative game where features are players.
- [[explanation-fidelity]] — uses
- [[post-hoc-explanation]] — specializes
- [[shapley-value]] — instantiates: SHAP applies the cooperative game theory Shapley value to the feature attribution problem.
[To be populated during integration]