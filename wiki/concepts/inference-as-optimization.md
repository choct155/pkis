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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- probabilistic-inference
- information-theory
id: pkis:concept:inference-as-optimization
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch19
tags:
- ELBO
- KL-divergence
- variational-inference
- lower-bound
- approximate-inference
title: Inference as Optimization (ELBO Perspective)
understanding: 0
---

## Definition
$$\mathcal{L}(v, \theta, q) = \log p(v; \theta) - D_{\mathrm{KL}}(q(h|v) \| p(h|v; \theta)) = \mathbb{E}_{h\sim q}[\log p(h,v)] + H(q)$$

Since $D_{\mathrm{KL}} \geq 0$, $\mathcal{L} \leq \log p(v; \theta)$ always, with equality iff $q = p(h|v)$. Posterior inference is recast as the optimization problem $q^* = \arg\max_q \mathcal{L}(v, \theta, q)$, which is solved exactly only when the search family contains the true posterior. Approximate inference restricts the family (mean field, Dirac) or uses imperfect optimizers.

### Why it matters
This perspective unifies EM, MAP inference, mean field VI, and amortized VI under a single mathematical framework: all are strategies for maximizing $\mathcal{L}$ under different constraints on $q$. It also makes explicit the direction of the KL divergence used in variational inference ($D_{\mathrm{KL}}(q \| p)$, mode-seeking) versus maximum likelihood ($D_{\mathrm{KL}}(p_{\text{data}} \| p_{\text{model}}}$, mass-covering).

### KL Direction Consequences
Minimizing $D_{\mathrm{KL}}(q \| p)$ encourages $q$ to concentrate on modes of $p(h|v)$, potentially ignoring other modes. This contributes to the self-reinforcing effect: variational training biases the learned model toward posteriors well-approximated by the chosen $q$ family.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]