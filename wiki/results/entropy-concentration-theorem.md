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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- information-theory
- bayesian-stats
- statistical-learning
id: pkis:result:entropy-concentration-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch11
tags:
- maximum-entropy
- frequency
- multinomial-coefficient
- concentration
- jaynes
- statistical-mechanics
- large-deviations
title: Entropy Concentration Theorem
understanding: 0
---

## Definition
The maximum-entropy frequency distribution is the one realizable in overwhelmingly the greatest number of ways. For N trials over n outcomes, the number of sequences giving sample frequencies {f_i} is the multinomial coefficient W = N!/prod(Nf_i)!, and (1/N)log W -> H_f = -sum f_i log f_i. The ratio of realization counts for two frequency sets grows like exp{N(H_f - H_f')}, so as N -> infinity the maxent frequencies dominate all others satisfying the same constraints by an unbounded factor.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]