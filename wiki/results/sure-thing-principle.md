---
aliases: []
also_type: []
applies:
- simpsons-paradox
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- bayesian-stats
id: pkis:result:sure-thing-principle
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch06
tags:
- causality
- decision-theory
- simpsons-paradox
- do-operator
- subpopulations
title: Sure-Thing Principle
understanding: 0
uses:
- do-calculus
---

## Definition
An action C that increases the probability of an event E in each subpopulation must also increase the probability of E in the population as a whole—*provided the action does not change the distribution of the subpopulations* (Theorem 6.1.1). Formally, if P(E|do(C),F) > P(E|do(¬C),F) for every stratum F and P(F|do(C)) = P(F|do(¬C)) = P(F), then P(E|do(C)) > P(E|do(¬C)).

The proof expands P(E|do(C)) over the strata, substitutes the invariance condition P(F|do(C))=P(F), and notes every term dominates the corresponding do(¬C) term. The decisive premise is the *invariance of the partition under the action* (the drug does not affect gender, equation 6.7). This is precisely why our causal intuition forbids the 'miracle drug' of Simpson's paradox and why the intuition flips when the stratifier is an intermediate variable affected by C: if F depends on the action, the expansion fails and P(E|do(C)) − P(E|do(¬C)) can take either sign. The principle thus furnishes the formal, do-operator-based logic underlying the resolution of Simpson's reversal.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[do-calculus]] — uses: stated and proved in terms of the do-operator and subpopulation invariance
- [[simpsons-paradox]] — applies: Theorem 6.1.1 formally precludes the 'miracle drug', resolving the paradox
[To be populated during integration]