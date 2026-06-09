---
aliases: []
also_type: []
applies:
- density-estimation
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- rule-ensembles
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
id: pkis:technique:association-rules-apriori
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch14
tags:
- unsupervised-learning
- data-mining
- rule-induction
- mode-finding
title: Association Rules and the Apriori Algorithm
understanding: 0
uses:
- decision-trees
---

## Definition
A data-mining technique for discovering frequently co-occurring joint values in very high-dimensional binary ("market basket") data. The goal is reframed from finding modes of Pr(X) to finding *item sets* K — subsets of binary dummy variables Z_k — whose **support** T(K) = (1/N)Σ_i ∏_{k∈K} z_{ik} (the empirical Pr[∩_{k∈K} Z_k=1]) exceeds a threshold t. The **Apriori algorithm** (Agrawal et al., 1995) solves this with a small number of passes over data too large for memory, exploiting the monotonicity property L⊆K ⇒ T(L) ≥ T(K): an item set of size m is a candidate only if all m of its size-(m−1) subsets are frequent, so each pass over the data adds one item to the surviving sets. Each high-support item set is then split into antecedent A and consequent B to form a rule A⇒B characterized by support T(A⇒B), **confidence** C(A⇒B)=T(A⇒B)/T(A) ≈ Pr(B|A), and **lift** = C/T(B) ≈ Pr(A,B)/(Pr(A)Pr(B)). Limitations: applies only to dummy-coded data, references the uniform distribution (so high-marginal items dominate and high-confidence/low-support rules like vodka⇒caviar are missed), and rule count grows explosively as t decreases.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[rule-ensembles]] — contrasts-with: both build conjunctive rules; Apriori is exhaustive over binary data, PRIM/RuleFit are greedy and handle general variables
- [[decision-trees]] — uses: CART terminal nodes give generalized item sets of the conjunctive-rule form (14.18)
- [[density-estimation]] — applies: recasts mode-finding / high-density-region discovery as a tractable frequent-itemset search
[To be populated during integration]