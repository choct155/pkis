---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
generalizes:
- linear-discriminant-analysis
id: pkis:technique:mixture-discriminant-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch12
tags:
- classification
- mixture-models
- em-algorithm
title: Mixture Discriminant Analysis (MDA)
understanding: 0
uses:
- em-algorithm
- k-means-clustering
- gaussian-mixture-models
- optimal-scoring
---

## Definition
A generalization of LDA that models each class by a Gaussian *mixture* of R_k prototype components (with mixing proportions pi_kr) rather than a single centroid, while sharing one common covariance matrix Sigma across all components of all classes. This captures irregularly shaped / inhomogeneous classes and, by substituting subclasses for classes, permits low-dimensional subspace views even for K=2 classes (where LDA allows none). Parameters are fit by maximum likelihood via the EM algorithm; rank restrictions on the sum_k R_k subclass centroids inherit LDA's reduced-rank property.

## Operational Mechanism
EM alternates: E-step computes responsibilities W(c_kr | x_i, g_i) of subclass r within the observation's own class k; M-step computes weighted MLEs of the component Gaussians. With a common Sigma the M-step is a weighted LDA over R = sum_k R_k 'classes', solvable by weighted optimal scoring -- so the M-step can itself use FDA or PDA, adding flexibility or smoothness. Crucially, with linear smoothers the enlarged indicator matrix collapses to a *blurred* response matrix Z whose rows hold the subclass responsibilities, so the problem size does not blow up. Initialization is by k-means clustering within each class (multiple random starts), important because mixture likelihoods are multimodal.

## Connections
- [[optimal-scoring]] — uses: the MDA M-step is a weighted LDA solved by optimal scoring
- [[gaussian-mixture-models]] — uses: MDA models each class density as a Gaussian mixture
- [[k-means-clustering]] — uses: MDA initializes subclass responsibilities by within-class k-means
- [[em-algorithm]] — uses: MDA fits mixture parameters by EM
- [[linear-discriminant-analysis]] — generalizes: MDA replaces a single class prototype with a Gaussian mixture of prototypes
- Generalizes [[linear-discriminant-analysis]] (single prototype -> mixture of prototypes)
- Uses [[em-algorithm]] for fitting and [[k-means-clustering]] for initialization
- Uses [[gaussian-mixture-models]] as the class-density model
- Can embed [[flexible-discriminant-analysis]] or [[penalized-discriminant-analysis]] in the M-step

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]