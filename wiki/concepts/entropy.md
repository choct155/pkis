---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- information-theory
- bayesian-stats
id: pkis:concept:entropy
knowledge_type: concept
maturity: settled
related_concepts:
- '[[kl-divergence]]'
- '[[probability-theory]]'
- '[[elbo]]'
sources:
- '[[lange-applied-probability]]'
- cote-visual-intro-information-theory-2022
tags:
- information-theory
- shannon-entropy
- maximum-entropy
- thermodynamics
title: Entropy
understanding: 0
uses:
- shannon-information-content
- self-information
---

Shannon entropy H(X) = −∑ p_i log p_i measures the average uncertainty (or information content) of a random variable; maximum entropy distributions under moment constraints are exponential families, and entropy connects information theory, statistical mechanics, and Bayesian inference.

## Connections
- [[self-information]] — uses
- [[shannon-information-content]] — uses: Entropy is the expected Shannon information content of an outcome.
- [[kl-divergence]] — uses: KL divergence generalizes entropy as a measure of distributional difference; relative entropy
- [[elbo]] — uses: the ELBO objective involves an entropy term for the variational distribution

## Reading Path
- [[lange-applied-probability-ch16]] (unread) — Shannon entropy, maximum entropy, applications, EM reinterpretation from information-theoretic perspective

## Decomposability (chain rule)
The entropy obeys a recursive **decomposability** property: revealing an outcome in stages gives
$$H(\mathbf{p}) = H(p_1, 1-p_1) + (1-p_1)\,H\!\left(\tfrac{p_2}{1-p_1},\ldots,\tfrac{p_I}{1-p_1}\right),$$
and more generally splitting the alphabet into groups adds the group-selection entropy plus the probability-weighted within-group entropies. This is the discrete root of the chain rule $H(X,Y)=H(X)+H(Y\mid X)$ and makes many entropy computations easy.

## Maximum-entropy bound
Entropy is bounded: $0 \le H(X) \le \log|A_X|$. The lower bound is attained iff one outcome has probability 1; the **upper bound is attained iff $\mathbf{p}$ is uniform**. The uniform-maximum result follows from Jensen's inequality applied to the concave $\log$, and the gap from the maximum defines the **redundancy** $1 - H(X)/\log|A_X|$. Entropy is additive over independent variables: $H(X,Y)=H(X)+H(Y)$ iff $P(x,y)=P(x)P(y)$.

## MacKay: decomposing joint entropy
For dependent variables, MacKay (ITILA ch. 8) decomposes the joint entropy via the chain rule $H(X,Y) = H(X) + H(Y\mid X)$ and defines the [[mutual-information]] $I(X;Y) = H(X) - H(X\mid Y) \geq 0$ as the average reduction in uncertainty about $X$ from learning $Y$. Conditioning reduces entropy on average, $H(X\mid Y) \leq H(X)$, with equality iff $X \perp Y$ — though for a single observed value $H(X\mid y=b_k)$ can exceed $H(X)$. See [[joint-entropy]], [[conditional-entropy]], [[chain-rule-for-entropy]].

## MacKay: information content, surprise, and the units of evidence
MacKay (ITILA ch. 18) stresses that the Shannon information content $h(x)=\log\tfrac{1}{P(x)}$ of which entropy is the average is the *same quantity* as 'surprise value' and as log evidence: $\log P(D\mid H_i)$ is exactly the negative information content of the data under a hypothesis. Data with high information content are surprising to a hypothesis and so erode it; a hypothesis less surprised by the data gains probability. Because all of these are (weighted sums of) log-probabilities, they share units — **bits** ($\log_2$), **nats** ($\log_e$), or **bans/decibans** ($\log_{10}$) — making entropy, surprise, and weight of evidence interconvertible measures on one scale.