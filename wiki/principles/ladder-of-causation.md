---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
id: pkis:principle:ladder-of-causation
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch01
tags:
- causality
- causal-hierarchy
- prediction
- intervention
- counterfactuals
- do-operator
title: Ladder of Causation
understanding: 0
---

## Definition
Causal reasoning tasks form a strict three-level hierarchy of increasing refinement, each rung demanding strictly more knowledge than the one below it.

One-line intuition: seeing, doing, and imagining are three different questions, and answering each requires a more detailed model than the last.

### The three rungs
1. **Prediction / association** — "Would the pavement be slippery if we *find* the sprinkler off?" Requires only a joint distribution function $P(v)$.
2. **Intervention** — "Would the pavement be slippery if we *make* the sprinkler off?" Requires a causal structure in addition to $P(v)$, so that $P(y \mid \mathrm{do}(x))$ can be computed via the truncated factorization.
3. **Counterfactuals** — "Would the pavement be slippery *had* the sprinkler been off, given that it is in fact not slippery and the sprinkler is on?" Requires functional relationships $f_i$ and/or the distribution of the omitted factors $P(u)$.

### Why the rungs are strict
A lower rung cannot answer a higher-rung query: $P(y \mid \mathrm{do}(x))$ cannot be deduced from $P(v)$ alone (intervention $>$ prediction), and counterfactual quantities like $Q$ = "would a treated-and-deceased patient have recovered untreated" cannot be deduced from a causal Bayesian network alone, because two functional models can share the same interventional distribution yet disagree on $Q$ (counterfactual $>$ intervention).

### Why it matters
The hierarchy organizes the entire theory of causal inference — and Pearl's book itself — by clarifying exactly which assumptions any given causal question demands. It warns that purely statistical (rung-1) machinery is structurally incapable of answering interventional or counterfactual questions, no matter how much data is collected.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]