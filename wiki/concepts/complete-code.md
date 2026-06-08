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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:concept:complete-code
instantiates:
- kraft-inequality
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch05
specializes:
- uniquely-decodable-codes
tags:
- symbol-codes
- kraft-inequality
- complete-tree
- implicit-probabilities
- source-coding
title: Complete Code
understanding: 0
---

## Definition
A uniquely decodable code is **complete** if it satisfies the Kraft inequality with equality:
$$\sum_{i=1}^{I} 2^{-l_i} = 1.$$
Equivalently, a complete prefix code corresponds to a binary tree with no unused branches — the full coding 'budget' of size 1 is spent.

### Implicit probabilities
Any set of codelengths defines implicit probabilities $q_i \equiv 2^{-l_i}/z$ with $z=\sum_{i'}2^{-l_{i'}}$, the distribution for which those lengths would be optimal. For a complete code $z=1$, so $q_i = 2^{-l_i}$ form a genuine normalized distribution.

### Why it matters
Completeness is the condition under which a code can be optimal: the lower bound $L(C,X)\ge H(X)$ is met with equality only when the code is complete *and* $l_i=\log_2(1/p_i)$. Incompleteness signals wasted budget and hence suboptimality — the diagnostic used to show that a greedy 'metacode' is suboptimal because its Kraft sum is strictly less than 1.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kraft-inequality]] — instantiates: Completeness is exactly the equality case of the Kraft inequality.
- [[uniquely-decodable-codes]] — specializes: A complete code is a uniquely decodable code meeting Kraft with equality.
[To be populated during integration]