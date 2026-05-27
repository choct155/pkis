---
id: "pkis:technique:support-vector-machines"
aliases: []
title: "Support Vector Machines"
knowledge_type: technique
also_type: [framework]
domain: [statistical-learning]
tags: [optimization, linear-algebra, regularization]
related_concepts: ["[[regularization]]", "[[convex-optimization]]", "[[lagrange-multipliers]]", "[[analytic-geometry]]"]
sources: ["[[hastie-esl]]", "[[deisenroth-mml]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

Kernel-based classification (and regression) method that finds the maximum-margin separating hyperplane in a transformed feature space, where the kernel trick avoids explicit computation of the high-dimensional mapping. Classification note: assigned as technique but also functions as a framework because SVMs encompass kernel selection, the kernel trick, regularization via the margin, and connections to RKHS theory.
