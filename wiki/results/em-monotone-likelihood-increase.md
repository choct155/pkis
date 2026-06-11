---
aliases: []
also_type: []
applies:
- em-algorithm
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- information-theory
id: pkis:result:em-monotone-likelihood-increase
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- variational-inference
related_concepts: []
sources:
- bishop-prml-ch09
tags:
- EM
- convergence
- ELBO
- KL-divergence
- variational-inference
title: EM Monotone Increase of Log-Likelihood
understanding: 0
uses:
- kl-divergence
- elbo
- jensens-inequality
---

## Definition
For any joint model $p(\mathbf{X},\mathbf{Z}\mid\boldsymbol{\theta})$, define
$$\ln p(\mathbf{X}\mid\boldsymbol{\theta}) = \mathcal{L}(q,\boldsymbol{\theta}) + \mathrm{KL}(q\|p)$$
where
$$\mathcal{L}(q,\boldsymbol{\theta}) = \sum_{\mathbf{Z}} q(\mathbf{Z})\ln\frac{p(\mathbf{X},\mathbf{Z}\mid\boldsymbol{\theta})}{q(\mathbf{Z})}, \qquad \mathrm{KL}(q\|p) = -\sum_{\mathbf{Z}} q(\mathbf{Z})\ln\frac{p(\mathbf{Z}\mid\mathbf{X},\boldsymbol{\theta})}{q(\mathbf{Z})}.$$
At the E step, setting $q(\mathbf{Z})=p(\mathbf{Z}\mid\mathbf{X},\boldsymbol{\theta}^{\text{old}})$ makes $\mathrm{KL}=0$ so $\mathcal{L}=\ln p(\mathbf{X}\mid\boldsymbol{\theta}^{\text{old}})$. At the M step, $q$ is frozen and $\boldsymbol{\theta}^{\text{new}}=\arg\max_{\boldsymbol{\theta}}\mathcal{L}$; since $\mathrm{KL}\geq 0$, we have $\ln p(\mathbf{X}\mid\boldsymbol{\theta}^{\text{new}})\geq\mathcal{L}(q,\boldsymbol{\theta}^{\text{new}})\geq\mathcal{L}(q,\boldsymbol{\theta}^{\text{old}})=\ln p(\mathbf{X}\mid\boldsymbol{\theta}^{\text{old}})$.

Every complete EM cycle is guaranteed to increase the incomplete-data log likelihood (or leave it unchanged at a stationary point).

### Why it matters
This result provides the formal convergence guarantee for EM. It also reveals EM as coordinate ascent on $\mathcal{L}(q,\boldsymbol{\theta})$: the E step maximises over $q$ and the M step maximises over $\boldsymbol{\theta}$. The decomposition directly motivates variational inference, where the E step is replaced by an approximate posterior.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[jensens-inequality]] — uses
- [[variational-inference]] — prerequisite-of
- [[elbo]] — uses: L(q,theta) is the ELBO; EM convergence follows from KL >= 0
- [[kl-divergence]] — uses
- [[em-algorithm]] — applies
[To be populated during integration]