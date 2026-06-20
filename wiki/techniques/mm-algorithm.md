---
aliases: []
also_type:
- framework
applies:
- logistic-regression
contrasts-with:
- iteratively-reweighted-least-squares
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- optimization
- bayesian-stats
generalizes:
- em-algorithm
id: pkis:technique:mm-algorithm
knowledge_type: technique
maturity: settled
related_concepts:
- '[[convex-optimization]]'
- '[[em-algorithm]]'
- '[[continuous-optimization]]'
sources:
- '[[lange-applied-probability]]'
- lange-applied-probability-ch03
tags:
- optimization
- em-algorithm
- majorization
- convex-optimization
title: MM Algorithm
understanding: 0
uses:
- convex-optimization
- jensens-inequality
---

The majorization-minimization (MM) algorithm is an iterative optimization framework that constructs a tangent majorant function at the current iterate and minimizes it instead of the original objective; EM is the special case where Jensen's inequality provides the majorant for a log-likelihood.

Classification note: assigned as technique but also_type framework because MM is both a specific procedure and an organizing paradigm for deriving new algorithms (including EM, proximal gradient, and others).

## Connections
- [[iteratively-reweighted-least-squares]] — contrasts-with: MM logistic update uses fixed Hessian bound vs IRLS exact Hessian
- [[jensens-inequality]] — uses
- [[logistic-regression]] — applies
- [[convex-optimization]] — uses
- [[em-algorithm]] — generalizes
- [[em-algorithm]] — generalizes: EM is the MM algorithm applied to log-likelihoods with Jensen's inequality as the majorization device

## Reading Path
- [[lange-applied-probability-ch03]] (unread) — MM algorithm derivation, connection to convexity, moment inequalities