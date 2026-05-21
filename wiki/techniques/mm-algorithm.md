---
title: "MM Algorithm"
knowledge_type: technique
also_type: [framework]
domain: [optimization, bayesian-stats]
tags: [optimization, em-algorithm, majorization, convex-optimization]
related_concepts:
  - "[[convex-optimization]]"
  - "[[em-algorithm]]"
  - "[[continuous-optimization]]"
sources:
  - "[[lange-applied-probability]]"
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The majorization-minimization (MM) algorithm is an iterative optimization framework that constructs a tangent majorant function at the current iterate and minimizes it instead of the original objective; EM is the special case where Jensen's inequality provides the majorant for a log-likelihood.

Classification note: assigned as technique but also_type framework because MM is both a specific procedure and an organizing paradigm for deriving new algorithms (including EM, proximal gradient, and others).

## Connections
- [[em-algorithm]] — generalizes: EM is the MM algorithm applied to log-likelihoods with Jensen's inequality as the majorization device

## Reading Path
- [[lange-applied-probability-ch03]] (unread) — MM algorithm derivation, connection to convexity, moment inequalities
