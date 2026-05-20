---
title: "Adversarial Examples"
knowledge_type: concept
also_type: []
domain: [deep-learning]
tags: [robustness, neural-networks, security, fooling, vulnerability, perturbations]
related_concepts: ["[[inductive-bias]]", "[[transfer-learning]]", "[[neural-networks]]"]
sources: ["[[marcus-dl-critical-appraisal-2018]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

Inputs to machine learning models that cause incorrect predictions through small, often imperceptible perturbations crafted to exploit the geometry of the model's learned decision boundary. Szegedy et al. (2013) first noted their existence; Marcus (2018) uses them as evidence of deep learning's fundamental brittleness — stop signs defaced by stickers misclassified as speed limits, 3D-printed turtles misclassified as rifles. Despite extensive research since 2013, no robust general solution exists, and adversarial vulnerability is cited as a barrier to high-stakes deployment.

## Reading Path
- [[marcus-dl-critical-appraisal-2018]] (unread) — §3.9 surveys adversarial examples as a fundamental DL vulnerability; documents real-world cases and their implications for engineering robustness
