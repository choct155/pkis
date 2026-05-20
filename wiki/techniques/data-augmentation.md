---
title: "Data Augmentation"
knowledge_type: technique
also_type: []
domain: [bayesian-stats]
tags: [posterior-sampling, latent-variables, missing-data, mcmc, imputation, bayesian-computation]
related_concepts: ["[[gibbs-sampler]]", "[[em-algorithm]]", "[[importance-sampling]]", "[[directed-graphical-models]]", "[[conjugate-prior]]"]
sources: ["[[tanner-tools-statistical-inference]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

An iterative posterior sampling algorithm that introduces latent variables Z to augment observed data Y, replacing a single intractable simulation from p(θ|Y) with an iterative series of tractable simulations: (I-step) draw Z from p(Z|θ^{(t)}, Y); (P-step) draw θ from p(θ|Z^{(t+1)}, Y). Under regularity conditions, the marginal distribution of the θ-draws converges to the target posterior p(θ|Y).

Data augmentation is the two-component special case of the Gibbs sampler. The EM algorithm is its deterministic analog (E-step computes E[Z|θ, Y]; M-step maximizes). The same augmentation strategy that makes EM tractable makes data augmentation tractable. Variants include Poor Man's Data Augmentation (PMDA), which approximates the P-step with a normal distribution, and Sampling/Importance Resampling (SIR), which resamples from a large proposal draw.

## Reading Path
- [[tanner-tools-statistical-inference]] (unread) — primary book-length treatment; Chapters 4-5 cover EM and data augmentation in parallel; convergence theory, PMDA variants, SIR, worked examples
- [[tanner-tools-statistical-inference-ch05]] (unread) — primary chapter
