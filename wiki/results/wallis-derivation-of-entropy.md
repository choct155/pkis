---
aliases: []
also_type: []
applies:
- maximum-entropy-principle
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
contrasts-with:
- gibbs-inequality
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- information-theory
- bayesian-stats
id: pkis:result:wallis-derivation-of-entropy
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch11
tags:
- maximum-entropy
- combinatorial
- multinomial
- stirling-approximation
- jaynes
- wallis
- entropy-justification
title: Wallis Derivation of Entropy
understanding: 0
uses:
- entropy
---

## Definition
A combinatorial justification of the maximum entropy principle, due to a 1962 suggestion by Graham Wallis: scatter n indistinguishable probability 'quanta' at random into m boxes, accept an allocation only if it satisfies the information I, and ask which distribution is most likely to result. Maximizing the multinomial probability and taking n to infinity via Stirling gives exactly the maximum-entropy distribution, with no appeal to 'amount of uncertainty' or to any frequency interpretation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gibbs-inequality]] — contrasts-with: Two independent justifications of maxent: combinatorial (Wallis) vs. inequality-based rigorous proof.
- [[maximum-entropy-principle]] — applies: The combinatorial game derives the maxent prescription without any uncertainty axiom.
- [[entropy]] — uses: The Stirling limit of the multinomial probability recovers the entropy functional.
[To be populated during integration]