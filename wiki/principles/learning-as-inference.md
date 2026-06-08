---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
contrasts-with:
- maxima-are-atypical
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- deep-learning
- bayesian-stats
id: pkis:principle:learning-as-inference
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- bayesian-neural-networks
related_concepts: []
sources:
- mackay-itila-ch41
specializes:
- bayesian-inference
tags:
- map-estimation
- regularization
- log-likelihood
- neural-networks
- probabilistic-interpretation
title: Learning as Inference
understanding: 0
uses:
- maximum-likelihood-estimation
---

## Definition
Training a model by minimizing a regularized objective is *identical* to Bayesian inference of its parameters. For a neural-network classifier MacKay writes the objective
$$M(w) = G(w) + \alpha E_W(w),$$
with data-fit term $G$ and regularizer $E_W$. Reading the network output as a probability, $y(x;w)\equiv P(t=1\mid x,w)$, the per-example likelihood is $P(t\mid w,x)=y^t(1-y)^{1-t}$, so the error term is *minus the log likelihood*, $P(D\mid w)=e^{-G(w)}$. The regularizer is *minus a log prior*, $P(w\mid\alpha)=\tfrac{1}{Z_W}e^{-\alpha E_W}$. Hence
$$P(w\mid D,\alpha)=\tfrac{1}{Z_M}e^{-M(w)},$$
and the minimizer $w^*$ is exactly the most-probable parameter vector $w_{MP}$ (the MAP estimate).

### Why the log map is natural
Error functions are *additive* (a sum of per-datum information contents plus a sum of squared weights); probabilities of independent events are *multiplicative*. The logarithm is the unique map carrying multiplication to addition, so any additive objective is, up to constants, a log-probability. This is why almost every loss function admits a probabilistic reading.

### Why it matters
The equivalence turns a heuristic recipe (pick a loss, add a penalty, descend) into a falsifiable modelling statement: the loss *is* a noise model and the penalty *is* a prior, each open to scrutiny and improvement. It also exposes what point optimization throws away — the spread of the posterior — motivating marginalization for prediction and the evidence framework for setting $\alpha$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[maxima-are-atypical]] — contrasts-with: Identifies training output as the mode w_MP, which the typical-set argument shows is unrepresentative.
- [[bayesian-neural-networks]] — prerequisite-of: Reinterpreting NN training as inference is the conceptual entry point to placing distributions over weights.
- [[maximum-likelihood-estimation]] — uses: The data-fit term is minus the log likelihood; minimizing it alone is MLE, and adding the prior makes it MAP.
- [[bayesian-inference]] — specializes: Learning-as-inference is the application of Bayesian parameter inference to the model-training objective.
[To be populated during integration]