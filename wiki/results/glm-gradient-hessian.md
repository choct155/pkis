---
aliases: []
also_type: []
applies:
- generalized-linear-models
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-20'
domain:
- statistics
- machine-learning
- optimization
id: pkis:result:glm-gradient-hessian
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- iteratively-reweighted-least-squares
related_concepts: []
sources:
- murphy-pml1-intro-ch12
- kroese-statistical-modeling-ch10
tags:
- GLM
- convexity
- MLE
- gradient
- Hessian
- IRLS
title: GLM Gradient and Hessian of NLL
understanding: 0
uses:
- gradient-descent
- fisher-information
---

## Definition
For a GLM with $\eta_n = w^T x_n$ and inverse-link $f = \ell^{-1}$, the per-sample gradient and full Hessian of the negative log-likelihood are:
$$\nabla_w \ell_n = (y_n - \mu_n)\,x_n, \qquad \mathbf{H} = \sum_{n=1}^N f'(\eta_n)\,x_n x_n^T$$
where $\mu_n = f(\eta_n) = A'(\eta_n)$.

Since $f'(\eta_n) > 0$ for all standard GLMs, $\mathbf{H}$ is positive semi-definite, and the NLL is **convex**, guaranteeing a unique MLE.

### Why it matters
This single formula covers linear regression ($f(\eta)=\eta$, $f'=1$), logistic regression ($f=\sigma$, $f'=\sigma(1-\sigma)$), and Poisson regression ($f=\exp$, $f'=\exp$). It shows that the same SGD or Newton-IRLS machinery applies uniformly across all GLMs, with the only difference being the weight $f'(\eta_n)$ in the Hessian — exactly the weight matrix in iteratively reweighted least squares.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[fisher-information]] — uses: Hessian equals Fisher information for canonical link GLMs
- [[gradient-descent]] — uses
- [[iteratively-reweighted-least-squares]] — prerequisite-of
- [[generalized-linear-models]] — applies
[To be populated during integration]