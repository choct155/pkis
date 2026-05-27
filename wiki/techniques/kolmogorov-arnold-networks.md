---
id: "pkis:technique:kolmogorov-arnold-networks"
aliases: ["KANs"]
title: "Kolmogorov-Arnold Networks (KANs)"
knowledge_type: technique
also_type: [framework]
domain: [deep-learning, optimization]
tags: [neural-networks, approximation-theory, splines, interpretability]
related_concepts: ["[[kolmogorov-arnold-theorem]]", "[[neural-scaling-laws]]", "[[spline-approximation]]", "[[universal-approximation-theorem]]", "[[backpropagation]]", "[[bias-variance-tradeoff]]"]
sources: ["[[liu-kan-2024]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

Neural network architecture where learnable univariate B-spline functions are placed on edges (replacing weight matrices), and nodes perform only summation — grounded in the Kolmogorov-Arnold representation theorem; achieves faster neural scaling laws (α=4) than MLPs and supports interpretability via sparsification, pruning, and symbolification. Classification note: assigned as technique but may be framework because KAN generalizes the depth-2 KA representation to arbitrary depth/width and defines a complete model-building paradigm with its own training, regularization, and interpretability workflow.

## Reading Path
- [[liu-kan-2024]] (unread) — primary source; full architecture, scaling law theory, grid extension, and scientific discovery applications
