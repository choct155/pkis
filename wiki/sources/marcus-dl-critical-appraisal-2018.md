---
id: "pkis:source:marcus-dl-critical-appraisal-2018"
aliases: []
title: "Deep Learning: A Critical Appraisal"
authors: "Gary Marcus"
year: 2018
type: paper
domain: [deep-learning, symbolic-subsymbolic]
tags: [deep-learning, neural-networks, transfer-learning, compositionality, agi, symbolic-ai, limitations, critique]
source_url: ""
drive_id: "1iAKSSVWmpjyzOaQ8wfEAN_MwIgiqaY9C"
drive_path: "PKIS/sources/papers/Deep Learning - A Critical Appraisal - Marcus.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[transfer-learning]]", "[[data-hunger]]", "[[adversarial-examples]]", "[[compositionality]]", "[[inductive-bias]]"]
---

## Summary

Written at the five-year anniversary of the deep learning resurgence (triggered by Krizhevsky et al.'s 2012 ImageNet paper), this paper offers a structured critique of deep learning's limitations while arguing it should be supplemented rather than replaced. Marcus organizes the critique around ten specific concerns: (1) data hunger — the need for massive labeled datasets, contrasting with humans' few-shot abstraction; (2) shallow transfer — deep learning learns brittle correlations that fail on minor distributional shifts; (3) lack of hierarchical structure representation — sentences are "flat" for most architectures; (4) failure at open-ended inference — multi-hop and knowledge-integration reasoning remain unsolved; (5) opacity/black box problem; (6) poor integration of prior knowledge — deliberate minimization of inductive bias; (7) inability to distinguish causation from correlation; (8) fragility in non-stable worlds; (9) adversarial vulnerability; (10) engineering difficulty and lack of guarantees.

The paper argues these limitations trace to a fundamental problem: deep learning learns correlations within a training space and interpolates well within it, but fails to extrapolate. This is illustrated by Marcus's 1997 identity-function experiments on odd numbers. The paper concludes by pointing toward four promising directions: unsupervised learning, hybrid symbolic-neural systems, insights from cognitive/developmental psychology, and bolder challenge problems (comprehension tests, embodied robotics, game transfer).

The paper explicitly calls for integrating deep learning with classical symbolic AI — positioning itself as an argument for what Marcus would later call "neuro-symbolic" AI — and cites the "atoms of neural computation" framework (Marcus, Marblestone, & Dean, 2014) as pointing toward what such hybrid systems might look like.

## Key Knowledge Objects

- [[transfer-learning]] (technique, high) — learning representations or policies that generalize to new tasks; paper argues current DL's transfer is severely limited
- [[adversarial-examples]] (concept, high) — inputs to ML models that cause incorrect classification through small, sometimes imperceptible perturbations; documented as a fundamental DL vulnerability
- [[compositionality]] (concept, high) — the property that meaning of complex expressions derives from their structure; Marcus argues DL lacks this for hierarchical language structure
- [[inductive-bias]] (concept, high) — prior assumptions encoded in an architecture; Marcus argues DL's deliberate minimization of inductive bias is a design flaw for real-world problems
- [[data-hunger]] (problem, high) — the requirement for massive training datasets before generalizing, contrasted with humans' few-shot concept learning

## Key Extractions

1. "The core problem, at least at present, is that deep learning learns correlations between sets of features that are themselves 'flat' or nonhierarchical … Hierarchical structure (e.g., syntactic trees that distinguish between main clauses and embedded clauses in a sentence) are not inherently or directly represented."

2. On transfer: Vicarious's demonstrations that DeepMind's A3C "failed on a variety of minor perturbations to Breakout … such as moving the Y coordinate of the paddle, or inserting a wall midscreen" show that credit for learning "wall" or "paddle" is "overattribution."

3. "Deep learning systems are quite good at some large fraction of a given domain, yet easily fooled" — stop signs defaced by stickers misclassified as speed limits, 3D-printed turtles as rifles.

4. On data hunger: "If I told you that a schmister was a sister over the age of 10 but under the age of 21 … you could immediately infer whether you had any schmisters … Humans can learn such abstractions … even 7-month old infants can do so … in just two minutes."

5. "The dominant approach in deep learning is hermeneutic, in the sense of being self-contained and isolated from other, potentially useful knowledge … prior knowledge is often deliberately minimized."

6. "We need to reconceptualize [deep learning]: not as a universal solvent, but simply as one tool among many, a power screwdriver in a world in which we also need hammers, wrenches, and pliers."

7. On hybrid systems: "The right move today may be to integrate deep learning, which excels at perceptual classification, with symbolic systems, which excel at inference and abstraction."

## Connection Candidates

- [[neurosymbolic-ai]] — grounds: the paper is an explicit argument for supplementing deep learning with symbolic systems; it is a foundational motivation text for neuro-symbolic AI
- [[inductive-bias]] — grounds: Marcus's critique centers on the costs of minimizing inductive bias; the paper grounds why strong priors from cognitive science and symbolic AI are needed
- [[backpropagation]] — contrasts-with: Hinton's own expressed doubt about backpropagation appears in the epigraph; Marcus cites the mismatch between BP and human learning mechanisms
- [[convolutional-neural-networks]] — specializes: CNNs are offered as a partial exception (convolution embeds translational invariance as inductive bias) but still limited to perceptual classification
- [[universal-approximation-theorem]] — contrasts-with: UAT shows networks can represent any function given enough capacity, but Marcus argues this says nothing about learnability or robustness
- [[marcus-atoms-neural-computation-2014]] — extends: the "atoms" paper provides the constructive alternative that the 2018 critique motivates
- [[dentella-ai-language-comprehension-2024]] — extends: the empirical evidence in Dentella et al. confirms the language-understanding failures predicted here
