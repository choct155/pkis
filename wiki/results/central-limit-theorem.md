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
- bayesian-stats
- statistical-learning
id: pkis:result:central-limit-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch07
tags:
- probability-theory
- convolution
- asymptotics
title: Central Limit Theorem
understanding: 0
---

## Definition
The central limit theorem states that the (suitably centered and scaled) sum of a large number of independent contributions tends to a Gaussian distribution, essentially independent of the distributions of the individual terms. It is the most famous instance of the general 'gravitation' of probability distributions toward the Gaussian form.

## Statement (Jaynes' characteristic-function derivation)
The density of a sum $y = x_1 + \cdots + x_n$ of independent variables is the multiple convolution $h_n = f_1 * \cdots * f_n$. Convolution becomes multiplication under the Fourier transform (characteristic function) $\varphi_k(\alpha) = \langle e^{i\alpha x}\rangle$, so $h_n(q) = \frac{1}{2\pi}\int d\alpha\, \varphi_1(\alpha)\cdots\varphi_n(\alpha) e^{-i\alpha q}$. Writing $\log\varphi(\alpha)$ as a cumulant expansion $C_0 + \alpha C_1 - \tfrac{1}{2}\alpha^2 C_2 + \cdots$ and retaining only cumulants through $C_2$ (mean and variance), the $n$-fold transform $[\varphi(\alpha)]^n$ inverts to a Gaussian with variance $n\sigma^2$ centered at $n\langle x\rangle$. The higher cumulants are discarded in the limit, which is precisely why only the first two moments survive.

## Information-theoretic reading (Jaynes)
Repeated convolution is an operation that conserves the first two moments while discarding finer information; a Gaussian has higher entropy than any other distribution with the same variance, so each convolution drives the distribution inexorably closer to the maximum-entropy (Gaussian) form. The CLT is thus the best-known case of distributions gravitating to the central distribution under information-discarding, variance-conserving operations.

## Practical consequence ($\sqrt{N}$ rule)
When $N$ independent errors each of magnitude $\sim\epsilon$ are summed, mutual cancellation makes the net error grow only as $\sqrt{N}$ rather than $N$ — the failure to see this was 'Euler's mistake'. Jaynes uses this to derive numerical-accuracy rules: to get four-figure accuracy in a sum of $N=100$ terms one needs only three-figure accuracy per term.

## Exception
The theorem requires the second moment to exist. The Cauchy distribution is the unique non-Gaussian stable law for which the sample mean has the same distribution as a single observation; its characteristic function $\exp\{i\alpha\theta - k|\alpha|\}$ has no finite variance, so the CLT does not apply.

## Connections
- [[convolution-of-distributions]] — uses: the CLT is the limit of repeated convolution
- [[gaussian-distribution]] — the limiting form
- [[entropy]] — the limit is the maximum-entropy distribution for fixed variance

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]