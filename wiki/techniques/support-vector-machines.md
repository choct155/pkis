---
aliases: []
also_type:
- framework
coverage: 2
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
extends:
- optimal-separating-hyperplane
id: pkis:technique:support-vector-machines
instantiates:
- reproducing-kernel-hilbert-space
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
- hinge-loss
- representer-theorem
- margin-maximum-margin-classifier
---

Kernel-based classification (and regression) method that finds the maximum-margin separating hyperplane in a transformed feature space, where the kernel trick avoids explicit computation of the high-dimensional mapping. Classification note: assigned as technique but also functions as a framework because SVMs encompass kernel selection, the kernel trick, regularization via the margin, and connections to RKHS theory.

## Connections
- [[margin-maximum-margin-classifier]] — uses: the SVM maximizes the margin of the separating hyperplane
- [[representer-theorem]] — uses: the RKHS representer theorem guarantees the finite-dimensional SVM solution
- [[hinge-loss]] — uses: the SVM is the hinge-loss + ridge-penalty function-fitting problem
- [[reproducing-kernel-hilbert-space]] — instantiates: hinge-loss RKHS problem f=α_0+Σα_i K(x,x_i)
- [[optimal-separating-hyperplane]] — extends: SVM generalizes the optimal separating hyperplane to the non-separable case via margin overlap
- [[pac-learning]] — prerequisite-of
- [[the-kernel-trick]] — uses