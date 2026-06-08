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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:result:chain-rule-for-entropy
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch08
tags:
- entropy
- chain-rule
- decomposition
- mackay
title: Chain Rule for Entropy
understanding: 0
uses:
- joint-entropy
- conditional-entropy
- shannon-information-content
---

## Definition
The joint, conditional, and marginal entropies of a pair of variables are related by
$$H(X, Y) = H(X) + H(Y \mid X) = H(Y) + H(X \mid Y).$$
In words: the uncertainty of $X$ and $Y$ together is the uncertainty of $X$ plus the uncertainty of $Y$ once $X$ is known. It is the ensemble-average of the chain rule for [[shannon-information-content]], $h(x,y) = h(x) + h(y\mid x)$.

### Proof
Apply the product rule $P(x,y)=P(x)P(y\mid x)$ inside the joint-entropy sum:
$$H(X,Y) = \sum_{xy} P(x)P(y\mid x)\Big[\log\tfrac{1}{P(x)} + \log\tfrac{1}{P(y\mid x)}\Big] = H(X) + H(Y\mid X).$$

### Mutual-information chain rule
The analogous decomposition for dependence is
$$I(X; Y, Z) = I(X; Y) + I(X; Z \mid Y),$$
which generalizes to arbitrarily many variables and is the workhorse for proving the [[data-processing-inequality]].

### Why it matters
The chain rule is the algebraic glue of information theory: combined with $I(X;Y)=H(X)-H(X\mid Y)$ it yields every relationship in MacKay's entropy-decomposition diagram, lets joint quantities be built incrementally, and underlies the analysis of sequences and Markov processes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[shannon-information-content]] — uses: Entropy chain rule is the ensemble average of the chain rule for information content h(x,y)=h(x)+h(y|x).
- [[conditional-entropy]] — uses: The conditional term H(Y|X) is the bridge in the decomposition.
- [[joint-entropy]] — uses: The chain rule decomposes joint entropy into marginal plus conditional terms.
[To be populated during integration]