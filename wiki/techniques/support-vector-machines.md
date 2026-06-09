---
aliases: []
also_type:
- framework
coverage: 2
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
id: pkis:technique:support-vector-machines
knowledge_type: technique
maturity: settled
prerequisite-of:
- pac-learning
related_concepts:
- '[[regularization]]'
- '[[convex-optimization]]'
- '[[lagrange-multipliers]]'
- '[[analytic-geometry]]'
sources:
- '[[hastie-esl]]'
- '[[deisenroth-mml]]'
tags:
- optimization
- linear-algebra
- regularization
title: Support Vector Machines
understanding: 0
uses:
- the-kernel-trick
---

Kernel-based classification (and regression) method that finds the maximum-margin separating hyperplane in a transformed feature space, where the kernel trick avoids explicit computation of the high-dimensional mapping. Classification note: assigned as technique but also functions as a framework because SVMs encompass kernel selection, the kernel trick, regularization via the margin, and connections to RKHS theory.

## Connections
- [[pac-learning]] — prerequisite-of
- [[the-kernel-trick]] — uses