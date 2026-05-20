---
title: "KAN: Kolmogorov-Arnold Networks"
authors: "Ziming Liu, Yixuan Wang, Sachin Vaidya, Fabian Ruehle, James Halverson, Marin Soljacic, Thomas Y. Hou, Max Tegmark"
year: 2024
type: paper
domain: [deep-learning, optimization]
tags: [neural-networks, approximation-theory, splines, interpretability, symbolic-regression]
source_url: "https://arxiv.org/abs/2404.19756"
drive_id: "1xpJBEohvHtUtxkiZZz9QTaePHLBaVuQh"
drive_path: "PKIS/sources/papers/KAN - Kolmogorov-Arnold Networks - Liu, Wang, Vaidya et al.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[kolmogorov-arnold-networks]]", "[[kolmogorov-arnold-theorem]]", "[[neural-scaling-laws]]", "[[spline-approximation]]", "[[universal-approximation-theorem]]", "[[backpropagation]]", "[[gradient-descent]]"]
---

## Summary

Liu et al. propose Kolmogorov-Arnold Networks (KANs) as an alternative to Multi-Layer Perceptrons (MLPs). While MLPs place fixed activation functions on nodes and learn linear weights on edges, KANs place learnable univariate functions (parameterized as B-splines) on edges and perform only summation at nodes — eliminating weight matrices entirely. This design is grounded in the Kolmogorov-Arnold representation theorem, which states that any multivariate continuous function can be expressed as a finite composition of univariate functions and addition.

The paper makes four principal claims: (1) KANs can achieve comparable or better accuracy than larger MLPs on small-scale function fitting tasks; (2) KANs exhibit faster neural scaling laws — test RMSE scales as N^{-4} with parameter count for smooth functions, versus slower and plateauing MLP scaling; (3) KANs naturally support grid extension for progressive refinement without full retraining; and (4) KANs offer superior interpretability, supporting sparsification, pruning, and symbolification workflows where learned activation functions can be interactively assigned known symbolic forms.

Two scientific applications are demonstrated: rediscovering knot invariant relationships in algebraic topology, and identifying localization transitions in Anderson localization physics. KANs are positioned as especially useful for AI+Science tasks where the model should be both accurate and human-interpretable, though the paper acknowledges KANs are slower to train than MLPs and most advantages are demonstrated at small scale.

## Key Knowledge Objects

- [[kolmogorov-arnold-networks]] (technique, high) — novel neural architecture placing learnable spline functions on edges instead of fixed activations on nodes
- [[kolmogorov-arnold-theorem]] (result, high) — every multivariate continuous function decomposes into compositions of univariate functions and addition
- [[neural-scaling-laws]] (concept, high) — empirical relationship between model parameter count and test loss, typically ℓ ∝ N^{-α}
- [[spline-approximation]] (technique, high) — piecewise polynomial function approximation with learnable B-spline coefficients, parameterizing KAN activation edges
- [[universal-approximation-theorem]] (result, high) — MLPs with sufficient width can approximate any continuous function; KAT is the KAN analogue
- [[backpropagation]] (technique, high) — used to train KANs since all operations are differentiable; the paper uses LBFGS and Adam variants
- [[gradient-descent]] (technique, high) — optimization procedure for training KANs; continuous search in function space is described as an advantage over discrete symbolic regression

## Key Extractions

1. **KAN architecture**: "KANs have no linear weights at all — every weight parameter is replaced by a univariate function parametrized as a spline." Each activation is ϕ(x) = w_b · silu(x) + w_s · spline(x), combining a residual basis function with a trainable B-spline.

2. **Kolmogorov-Arnold theorem**: For smooth f: [0,1]^n → R, f(x) = Σ_{q=1}^{2n+1} Φ_q(Σ_{p=1}^n ϕ_{q,p}(x_p)). The paper generalizes this from the fixed 2-layer depth-(2n+1) form to arbitrary width and depth.

3. **Scaling law theorem (KAT)**: If f admits a smooth KA representation, there exist B-spline functions with grid size G such that ‖f - KAN_G‖_{C^m} ≤ C·G^{−k−1+m}. For cubic splines (k=3), test RMSE scales as G^{-4}, giving scaling exponent α = 4 — better than MLPs.

4. **Grid extension**: KANs can be progressively fine-grained by fitting new fine-grained spline parameters to existing coarse ones, enabling a continual refinement workflow without full retraining. Loss curves show staircase drops at each grid extension step.

5. **Interpretability workflow**: sparsification (L1 + entropy regularization) → pruning (node-level scoring) → symbolification (fix_symbolic interface to assign named functions) → symbolic formula extraction via SymPy. Users can interactively "debug" the network's activation shapes.

6. **Bias-variance tradeoff in KANs**: The interpolation threshold (where train parameters ≈ data count) is the optimal grid size; too fine a grid overfits, too coarse underfits. For [2,5,1] KAN on 1000 samples, threshold is G ≈ 50.

7. **Curse of dimensionality claim**: KANs beat COD when functions have compositional/KA structure, because splines only approximate 1D functions. However, this requires knowing or discovering the compositional structure.

## Connection Candidates

- [[universal-approximation-theorem]] — contrasts-with (result→result): KAT provides the same role for KANs as UAT for MLPs but with explicit dimensionality-beating scaling bounds
- [[backpropagation]] — uses: KANs are trained via backpropagation since all operations are differentiable
- [[gradient-descent]] — uses: LBFGS and stochastic gradient methods used for KAN training
- [[bias-variance-tradeoff]] — uses: grid extension displays classic U-shaped test loss, directly instantiating the bias-variance tradeoff
- [[empirical-risk-minimization]] — uses: KAN training minimizes prediction loss plus sparsification/entropy regularization terms

## Awaiting Classification

- **symbolic-regression** — candidate types: technique or framework
  - Case for technique: it is a procedure (search over symbolic expressions) applied as a comparison point
  - Case for framework: genetic programming / SR encompasses a family of methods
  - What makes this hard: the paper treats it mainly as a contrast point, not a primary subject
