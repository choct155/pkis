---
id: "pkis:source:yellapragada-variational-bayes"
aliases: []
title: "Variational Bayes: A Report on Approaches and Applications"
knowledge_type: source
source_type: paper
authors: ["Manikanta Srikar Yellapragada", "Chandra Prakash Konkimalla"]
year: 2019
domain: [bayesian-stats, deep-learning, reinforcement-learning]
tags: [variational-methods, approximate-inference, bayesian-neural-networks, normalizing-flows, continual-learning]
source_url: "https://arxiv.org/abs/1905.10744"
drive_id: "1B5w0Mo7bL62uBjJk65seX4VxnCdv62Zh"
drive_path: "PKIS/sources/papers/yellapragada-variational-bayes.pdf"
status: unread
date_added: 2026-05-20
date_updated: 2026-05-20
concepts: ["[[variational-inference]]", "[[elbo]]", "[[bayesian-neural-networks]]", "[[normalizing-flows]]", "[[reparameterization-trick]]"]
---

Survey and application report reviewing major variational Bayesian methods as applied to deep neural networks, with emphasis on uncertainty quantification in neural network weights. The central motivation is that deterministic neural networks fail to represent predictive uncertainty, while Bayesian Neural Networks (BNNs) learn distributions over weights. The paper reviews five approaches to approximate BNN inference via VI: (1) Graves (2011) — MDL-loss reformulation of VI; (2) Auto-Encoding Variational Bayes (AEVB/VAE, Kingma & Welling 2013) — reparameterization trick and SGVB estimator; (3) Bayes by Backprop (Blundell et al. 2015) — scale-mixture Gaussian priors, generalizes reparameterization; (4) Multiplicative Normalizing Flows (Louizos & Welling 2017) — normalizing flows applied to BNN posteriors via auxiliary distribution; (5) Bayesian Hypernetworks (Krueger et al. 2017) — invertible hypernetwork generates approximate posterior. Applications to RL are then reviewed: Noisy Networks (exploration via learned weight perturbations), Bootstrapped DQN (posterior sampling via bootstrap heads), and UCB Q-Ensembles. The paper concludes with Variational Continual Learning, where the VI objective is updated sequentially over tasks, using a small coreset to prevent catastrophic forgetting.

## Key Knowledge Objects

- [[variational-inference]] (technique, high) — core inference framework; applied to BNN weight posteriors throughout
- [[elbo]] (concept, high) — ELBO = E_q[log p(x,z)] + H(q); energy term encourages data fit, entropy term prevents collapse
- [[bayesian-neural-networks]] (concept, high) — neural networks that place distributions over weights rather than point estimates; provide calibrated uncertainty
- [[normalizing-flows]] (technique, high) — series of invertible mappings transforming simple distribution to complex one; used to enrich posterior approximations
- [[reparameterization-trick]] (technique, high) — z = g_φ(ε, x) reformulation enabling backprop through stochastic nodes; central to AEVB

## Key Extractions

1. **ELBO decomposition (energy + entropy)**: L(x) = E_q[log p(x,z)] + H(q). The energy term drives q to place mass where the joint model has high probability; the entropy term prevents q from collapsing to a point mass. This trade-off is explicit in the MDL formulation: L(α,β,D) = L_E(β,D) + L_C(α,β).
2. **Graves (2011) MDL reformulation**: Practical VI for NNs via Minimum Description Length loss: F = L_N(x,y,w)|_{w~q(β)} + KL(q(β)‖P(α)). For diagonal Gaussian posteriors, this separates into per-weight KL terms, enabling scalable gradient computation.
3. **Bayes by Backprop parameterization**: σ = log(1 + exp(ρ)) ensures positivity; weights w = μ + σ·ε, ε~N(0,I). Gradient flows through μ and ρ; no closed-form KL required (only sampling needed). Scale-mixture prior P(w) = ∏_j[πN(w_j;0,σ²_1) + (1−π)N(w_j;0,σ²_2)] provides spike-and-slab flexibility.
4. **Multiplicative Normalizing Flows**: Avoids full NF cost on weights by factorizing q_φ(w,z) = q_φ(w|z)q_φ(z) where z is low-dimensional. Uses auxiliary distribution r(z|W) to make the lower bound tractable; parameterizes r with inverse normalizing flows.
5. **Variational Continual Learning (VCL)**: Sequential ELBO update q_t(θ) = argmin_{q} KL(q(θ) ‖ q_{t−1}(θ)·p(D_t|θ)/Z_t). Previous posterior becomes next prior; coreset of K representative points prevents catastrophic forgetting. Evaluated on Permuted/Split MNIST.

## Connection Candidates

- [[neural-networks]] — uses: all methods reviewed apply VI to neural network weight inference
- [[variational-autoencoder]] — uses: AEVB/VAE is reviewed as a central VI method; reparameterization trick is the connecting mechanism
- [[em-algorithm]] — extends: VI for BNNs can be viewed as stochastic EM where the E-step is approximate and the M-step updates generative parameters
- [[directed-graphical-models]] — uses: Bayesian NN model structure is a directed graphical model; the variational approximation factorizes to match this structure
