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
id: pkis:concept:joint-entropy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch08
specializes:
- entropy
tags:
- entropy
- joint-ensemble
- uncertainty
- mackay
title: Joint Entropy
understanding: 0
---

## Definition
The total average uncertainty in a pair of (possibly dependent) random variables, treating the pair $(x,y)$ as a single outcome:
$$H(X, Y) = \sum_{xy \in A_X A_Y} P(x, y) \log \frac{1}{P(x, y)}.$$
It is the entropy of the joint ensemble $XY$. Intuitively, it is the average number of bits needed to specify *both* outcomes at once.

### Additivity for independence
Joint entropy is additive exactly when the variables are independent:
$$H(X, Y) = H(X) + H(Y) \iff P(x, y) = P(x)P(y).$$
When $X$ and $Y$ are dependent, $H(X,Y) < H(X) + H(Y)$: the shared structure means the pair carries less surprise than the sum of the parts. The deficit is exactly the mutual information.

### Decomposition
The joint entropy splits via the [[chain-rule-for-entropy]] into a marginal plus a conditional term: $H(X,Y) = H(X) + H(Y \mid X)$.

### Why it matters
Noisy channels define a joint ensemble of input $x$ and output $y$ that are *dependent* (if they were independent, no communication would be possible). Compression of correlated data and all of channel-coding theory are phrased in terms of the entropies of such joint ensembles, with $H(X,Y)$ the anchoring quantity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[entropy]] — specializes: Joint entropy is the entropy of the joint ensemble XY.
[To be populated during integration]