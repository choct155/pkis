---
aliases: []
also_type: []
coverage: 4
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- bayesian-stats
- information-theory
id: pkis:concept:kl-divergence
knowledge_type: concept
maturity: settled
related_concepts:
- '[[probability-theory]]'
- '[[elbo]]'
- '[[variational-inference]]'
sources:
- '[[blei-vi-review]]'
- '[[ganguly-intro-vi]]'
- '[[yellapragada-variational-bayes]]'
- '[[lange-applied-probability]]'
tags:
- probability-theory
- information-theory
- variational-methods
title: Kullback-Leibler Divergence
understanding: 0
uses:
- gibbs-inequality
---

An asymmetric non-negative measure of the "extra information" required to encode samples from distribution P using a code optimized for distribution Q: DKL(P‖Q) = E_P[log(P/Q)] ≥ 0, with equality iff P = Q; in variational inference, the reverse KL(q‖p) is minimized (zero-forcing, mode-seeking) while the forward KL(p‖q) would be zero-avoiding but requires access to p.

## Connections
- [[gibbs-inequality]] — uses: Gibbs' inequality establishes the defining non-negativity of KL divergence.

- [[variational-inference]] — used-by: VI minimizes reverse KL(q‖p(z|x)) as its objective; the ELBO equals log p(x) minus this KL
- [[elbo]] — used-by: ELBO = log p(x) − KL(q‖p(z|x)); the KL gap is what ELBO maximization implicitly closes
- [[probability-theory]] — prerequisite-of: understanding KL requires measure-theoretic probability and information theory

## Reading Path

- [[blei-vi-review]] (unread) — Section 2.1; KL as the VI objective; discussion of why forward KL is intractable and reverse KL is tractable
- [[ganguly-intro-vi]] (unread) — Section 2; KL derivation; Figure 2 illustrates forward vs. reverse KL on bimodal distribution; zero-avoiding vs. zero-forcing behavior
- [[yellapragada-variational-bayes]] (unread) — Section 2.2; entropy and KL definitions; role in MDL loss formulation
- [[lange-applied-probability-ch16]] (unread) — entropy chapter grounds KL divergence in information-theoretic context

## Relative entropy and Gibbs' inequality
In MacKay's information-theoretic framing the KL divergence is the **relative entropy** $D_{KL}(P\|Q)=\sum_x P(x)\log\frac{P(x)}{Q(x)}$ — the expected extra number of bits incurred by coding for $Q$ when the true distribution is $P$. **Gibbs' inequality** guarantees $D_{KL}(P\|Q)\ge0$ with equality iff $P=Q$, proved via Jensen's inequality. It is generally **asymmetric** ($D_{KL}(P\|Q)\ne D_{KL}(Q\|P)$), so despite the nickname 'KL distance' it is not a metric.

## MacKay: mutual information as a KL divergence
Mutual information is a special case of relative entropy: $I(X;Y) = D_{KL}\big(P(x,y)\,\|\,P(x)P(y)\big) \geq 0$, measuring how far the joint distribution sits from the independent product. Non-negativity of $I(X;Y)$ is therefore exactly [[gibbs-inequality]]. See [[mutual-information]].