---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
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
tags:
- information-theory
- shannon-entropy
- maximum-entropy
- thermodynamics
title: Entropy
understanding: 0
uses:
- shannon-information-content
---

Shannon entropy H(X) = −∑ p_i log p_i measures the average uncertainty (or information content) of a random variable; maximum entropy distributions under moment constraints are exponential families, and entropy connects information theory, statistical mechanics, and Bayesian inference.

## Connections
- [[shannon-information-content]] — uses: Entropy is the expected Shannon information content of an outcome.
- [[kl-divergence]] — uses: KL divergence generalizes entropy as a measure of distributional difference; relative entropy
- [[elbo]] — uses: the ELBO objective involves an entropy term for the variational distribution

## Reading Path
- [[lange-applied-probability-ch16]] (unread) — Shannon entropy, maximum entropy, applications, EM reinterpretation from information-theoretic perspective