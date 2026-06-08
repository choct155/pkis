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
id: pkis:concept:conditional-entropy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- mutual-information
related_concepts: []
sources:
- mackay-itila-ch08
- mackay-itila-ch09
specializes:
- entropy
tags:
- entropy
- conditioning
- uncertainty
- mackay
title: Conditional Entropy
understanding: 0
---

## Definition
The average uncertainty that remains about $X$ once $Y$ is known, averaged over the values of $Y$:
$$H(X \mid Y) \equiv \sum_{y \in A_Y} P(y) \Big[ \sum_{x \in A_X} P(x \mid y) \log \frac{1}{P(x \mid y)} \Big] = \sum_{xy} P(x, y) \log \frac{1}{P(x \mid y)}.$$
The inner bracket is $H(X \mid y = b_k)$, the entropy of the conditional distribution $P(x \mid y = b_k)$ for a fixed observed value.

### Conditioning reduces uncertainty on average
For a *specific* outcome it is possible that $H(X \mid y=b_k) > H(X)$ — a particular observation can be misleading. But the average never increases:
$$H(X \mid Y) \leq H(X),$$
with equality iff $X$ and $Y$ are independent. The proof rewrites the gap as a sum of relative entropies and invokes [[gibbs-inequality]]. So data are helpful: they do not increase uncertainty on average.

### Why it matters
Conditional entropy is the residual uncertainty after observation, making it the natural measure of equivocation in a noisy channel. It is the bridge term in the [[chain-rule-for-entropy]] and the subtracted quantity in [[mutual-information]]: $I(X;Y) = H(X) - H(X \mid Y)$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mutual-information]] — prerequisite-of: I(X;Y)=H(X)-H(X|Y) is defined via conditional entropy.
- [[entropy]] — specializes: Conditional entropy is the entropy of conditional distributions, averaged over the conditioning variable.
[To be populated during integration]