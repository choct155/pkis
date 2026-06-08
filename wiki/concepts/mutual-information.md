---
aliases: []
also_type: []
applies:
- binary-symmetric-channel
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- conditional-independence
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:concept:mutual-information
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- channel-capacity
- noisy-channel-coding-theorem
related_concepts: []
sources:
- mackay-itila-ch08
- mackay-itila-ch09
specializes:
- kl-divergence
tags:
- mutual-information
- dependence
- channel
- mackay
title: Mutual Information
understanding: 0
uses:
- conditional-entropy
- gibbs-inequality
- entropy
---

## Definition
The average reduction in uncertainty about $X$ that results from learning $Y$ (equivalently, how much $X$ tells you about $Y$):
$$I(X; Y) \equiv H(X) - H(X \mid Y).$$
It is the central measure of statistical dependence in information theory.

### Properties
Mutual information is symmetric and non-negative:
$$I(X; Y) = I(Y; X) \geq 0,$$
with $I(X;Y) = 0$ iff $X$ and $Y$ are independent. Both facts follow from the relative-entropy form
$$I(X; Y) = \sum_{xy} P(x, y) \log \frac{P(x, y)}{P(x)P(y)} = D_{KL}\big(P(x,y) \,\|\, P(x)P(y)\big),$$
so non-negativity is just [[gibbs-inequality]] (or Jensen's inequality).

### Conditional mutual information
Conditioning on a third variable gives $I(X; Y \mid Z) = H(X \mid Z) - H(X \mid Y, Z)$. Crucially, conditioning can *increase* dependence: for $z = x + y \bmod 2$ with independent $x,y$ we have $I(X;Y)=0$ but $I(X;Y\mid Z)=1$ bit. This is why a Venn-diagram picture of three-variable entropies is misleading — some 'areas' are negative.

### Why it matters
The capacity of a noisy channel is $C = \max_{p(x)} I(X;Y)$ — mutual information is the quantity optimized in [[channel-capacity]] and the foundation of the [[noisy-channel-coding-theorem]].

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[entropy]] — uses: Mutual information is a difference of (marginal and conditional) entropies.
- [[binary-symmetric-channel]] — applies: MacKay computes I(Z;X) for z=x+y mod 2, the BSC with input x and noise y.
- [[noisy-channel-coding-theorem]] — prerequisite-of: The coding theorem is stated in terms of mutual information / capacity of the joint ensemble.
- [[channel-capacity]] — prerequisite-of: Channel capacity is the maximum of mutual information over input distributions.
- [[conditional-independence]] — contrasts-with: I(X;Y)=0 iff X and Y are independent; conditioning on Z can break or create dependence.
- [[gibbs-inequality]] — uses: Non-negativity of mutual information follows directly from Gibbs' inequality.
- [[kl-divergence]] — specializes: I(X;Y) = D_KL(P(x,y) || P(x)P(y)) is a KL divergence between joint and product distributions.
- [[conditional-entropy]] — uses: I(X;Y) = H(X) - H(X|Y) is defined via conditional entropy.
[To be populated during integration]