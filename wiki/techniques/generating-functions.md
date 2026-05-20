---
title: "Generating Functions"
knowledge_type: technique
also_type: [concept]
domain: [bayesian-stats]
tags: [probability-theory, moment-generating-functions, probability-generating-functions, analytic-methods]
related_concepts:
  - "[[probability-theory]]"
  - "[[branching-processes]]"
sources:
  - "[[lange-applied-probability]]"
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Analytic tools that encode the distribution of a random variable as coefficients of a power series; probability generating functions (PGFs), moment generating functions (MGFs), and cumulant generating functions (CGFs) each enable computation of moments, convolutions, and limit theorems via analytic manipulation.

Classification note: assigned as technique but also_type concept because generating functions are both a computational procedure and a mathematical object with intrinsic properties; the boundary is genuinely blurry.

## Connections
- [[branching-processes]] — uses: extinction probability in branching processes is the fixed point of the offspring probability generating function
- [[laplace-approximation]] — uses: the CGF is the central object in Laplace/saddlepoint approximations

## Reading Path
- [[lange-applied-probability-ch02]] (unread) — moment transforms and generating functions for expectations
- [[lange-applied-probability-ch12]] (unread) — asymptotics of generating functions; saddlepoint approximations via CGF
