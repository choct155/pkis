---
title: "An Introduction to Variational Inference"
knowledge_type: source
source_type: paper
authors: ["Ankush Ganguly", "Samuel W. F. Earp"]
year: 2021
domain: [bayesian-stats, deep-learning, optimization]
tags: [variational-methods, probability-theory, generative-models, approximate-inference]
source_url: "https://arxiv.org/abs/2108.13083"
drive_id: "1b4RTgoc1cQ-Z2UZUWzVXHtizlrOhQLec"
drive_path: "PKIS/sources/papers/ganguly-intro-vi.pdf"
status: unread
date_added: 2026-05-20
date_updated: 2026-05-20
concepts: ["[[variational-inference]]", "[[elbo]]", "[[mean-field-approximation]]", "[[kl-divergence]]", "[[variational-autoencoder]]"]
---

Accessible introduction to Variational Inference (VI) aimed at practitioners entering the field. The paper frames VI as an optimization reformulation of Bayesian posterior inference: rather than compute the intractable posterior p(Z|X) directly, one selects the member of a tractable family Q that minimizes KL divergence to the true posterior. The key object is the Evidence Lower Bound (ELBO), which lower-bounds the log-evidence and is equivalent to maximizing the reverse KL. The paper introduces the mean-field variational family — where latent variables are assumed mutually independent — and demonstrates the Coordinate Ascent Variational Inference (CAVI) algorithm on a Gaussian mixture toy problem. The second half extends VI to deep learning applications: Variational Autoencoders (VAE) using the reparameterization trick for gradient-based ELBO optimization, and VAE-GANs that replace pixel-level reconstruction loss with a GAN discriminator feature-space loss. The paper clearly distinguishes forward KL (zero-avoiding, mean-seeking) from reverse KL (zero-forcing, mode-seeking) divergence, connecting this asymmetry to known VAE image blur artifacts.

## Key Knowledge Objects

- [[variational-inference]] (technique, high) — the core framework: approximate posterior via KL-minimization cast as optimization
- [[elbo]] (concept, high) — Evidence Lower Bound; the tractable objective maximized in VI; equals log-evidence minus KL gap
- [[mean-field-approximation]] (technique, high) — fully factorized variational family; each latent variable governed by an independent factor
- [[kl-divergence]] (concept, high) — asymmetric divergence between distributions; reverse KL used as VI objective
- [[variational-autoencoder]] (technique, high) — neural network architecture using reparameterization trick to optimize the ELBO; encoder approximates posterior, decoder models likelihood

## Key Extractions

1. **ELBO derivation**: ELBO(Q) = E[log p(z,x)] − E[log q(z)] = E[log p(x|z)] − KL(Q(Z) ‖ P(Z)). Maximizing ELBO is equivalent to minimizing reverse KL divergence; the gap between log-evidence and ELBO is exactly KL(Q‖P).
2. **Forward vs. reverse KL asymmetry**: Forward KL (M-projection) is zero-avoiding — forces q > 0 wherever p > 0, leading to over-disperse approximations. Reverse KL (I-projection) is zero-forcing — forces q = 0 wherever p = 0, causing mode-seeking and explaining VAE image blurring.
3. **Mean-field CAVI updates**: For Gaussian mixture with K components, the optimal variational parameters are closed-form: φ*_ij ∝ exp(−½(m²_j + s²_j) + x_i m_j). Iterating these updates until ELBO convergence is the CAVI algorithm.
4. **Reparameterization trick (VAE)**: Express z ~ q_φ(z|x) as z = g_φ(ε,x) where ε ~ p(ε), moving randomness outside the network. This makes the ELBO gradient computable by standard backpropagation, yielding the SGVB estimator.
5. **VAE-GAN hybrid**: Replace VAE's pixel-level reconstruction loss with a GAN discriminator's hidden-layer feature distance (Larsen et al. 2016). Combined objective: L = L_prior + L_Dis_llike + L_GAN. Encoder updates on L_prior + L_Dis_llike; decoder balances reconstruction against GAN adversarial loss.

## Connection Candidates

- [[em-algorithm]] — extends: VI generalizes EM; the E-step computes an exact posterior while VI optimizes an approximate one; both maximize a lower bound on log-likelihood
- [[gaussian-mixture-models]] — uses: the toy CAVI example demonstrates VI applied directly to a Gaussian mixture model
- [[directed-graphical-models]] — uses: VAE generative model p(x,z) is naturally expressed as a directed graphical model with z → x
- [[neural-networks]] — uses: VAE encoder and decoder are neural networks; backprop through reparameterization enables joint training
