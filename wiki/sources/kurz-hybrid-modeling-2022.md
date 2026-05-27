---
id: "pkis:source:kurz-hybrid-modeling-2022"
aliases: []
title: "Hybrid Modeling: Towards the Next Level of Scientific Computing in Engineering"
authors: "Stefan Kurz, Herbert De Gersem, Armin Galetzka, Andreas Klaedtke, Melvin Liebsch, Dimitrios Loukrezis, Stephan Russenschuck, Manuel Schmidt"
year: 2022
type: paper
domain: [deep-learning, bayesian-stats, optimization]
tags: [physics-informed-ml, scientific-computing, gaussian-processes, bayesian-optimization, gibbs-sampling]
source_url: "https://doi.org/10.1186/s13362-022-00123-0"
drive_id: "10oEML0OOwjNvDUHhMNw0vpP7n1ZPuUhs"
drive_path: "PKIS/sources/papers/Hybrid Modeling.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[hybrid-modeling]]", "[[physics-informed-neural-networks]]", "[[bayesian-optimization]]", "[[gaussian-process-regression]]", "[[gibbs-sampler]]", "[[gaussian-distribution]]"]
---

## Summary

Kurz et al. (Robert Bosch GmbH / TU Darmstadt / CERN) survey and demonstrate three paradigms of hybrid modeling — architectures that combine first-principle physics (the "Newtonian paradigm") with data-driven learning (the "Keplerian paradigm"). The core argument is that neither pure simulation nor pure data-driven learning alone achieves the accuracy-cost Pareto tradeoff required for industrial scientific computing; hybrid models combining both offer enhanced robustness and interpretability.

Three case studies are presented in detail. First, blending data with physics for CERN magnet characterization: field reconstruction via Boundary Element Method (BEM) combined with Bayesian inference for sensor positioning uncertainty — modeled as Gibbs sampling from a joint posterior p(ν,d|y) where ν is the BEM state vector and d encodes mechanical perturbations. Second, data-driven field simulation without an explicit constitutive material law: finding fields that satisfy Maxwell's equations (known exactly from first principles) while being closest to measured (B,H) material data points — a constrained optimization formulation. Third, Bayesian free-shape optimization of trace pairs on printed circuit boards using Gaussian Process surrogates within a multi-objective Bayesian optimization (BO) framework.

The paper situates hybrid modeling in relation to Kalman filtering (recognized as recursive Bayesian estimation — a classical hybrid), Physics-Informed Neural Networks (PINNs), SPINNs, and Field Inversion and Machine Learning (FIML). The key insight across all three cases is that physics constraints reduce the effective search space and permit much more data-efficient learning.

## Key Knowledge Objects

- [[hybrid-modeling]] (framework, high) — combining first-principle (physics/statistics) models with data-driven models into a joint architecture; the defining feature is that both components are active during inference, not just training
- [[physics-informed-neural-networks]] (technique, high) — neural networks that incorporate PDE constraints by minimizing physics residuals in the loss (Deep Ritz, PINNs/Raissi et al. 2019); mentioned as a related approach
- [[bayesian-optimization]] (technique, high) — sequential optimization of expensive black-box functions using a surrogate (GP) model + acquisition function (Expected Improvement); used here for free-shape multi-objective trace-pair optimization
- [[gaussian-process-regression]] (technique, high) — already likely exists; used here as the surrogate model for Bayesian optimization, providing mean predictions and uncertainty estimates
- [[gibbs-sampler]] (technique, high) — already exists; used to sample from joint posterior p(ν,d|y) by alternating conditional sampling p(ν|d,y) and p(d|ν,y) in the magnet characterization case
- [[gaussian-distribution]] (concept, high) — already exists; Gaussian prior p(ν) ~ N(ν_0, L_ν^{-1}) and Gaussian sensor noise model underpin the BEM Bayesian update

## Key Extractions

1. **Hybrid model definition**: "Hybrid models combine first principle-based models with data-based models into a joint architecture, supporting enhanced model qualities, such as robustness and explainability." First principles may be physics, statistics (probabilistic graphical models), or discourse (ontologies).

2. **Kalman filter as canonical hybrid**: "Kálmán filtering can be recognized as recursive Bayesian estimation." It embeds physics state-transition dynamics as the Newtonian prior and updates with data measurements — the prototype of structured Bayesian filtering.

3. **BEM + Bayesian update**: BEM discretizes field as state vector ν ∈ R^N; measurement y = H(ν) + perturbations d. Gibbs sampling from p(ν,d|y) ∝ p(y|ν,d)·p(ν)·p(d) recovers both field coefficients and mechanical sensor displacements. Solution efficiency via stochastic linear equation: (H^T R^{-1} H + L_ν)ν_k = H^T R^{-1} y + L_ν ν_0 + noise.

4. **Data-driven field simulation (no material law)**: The hybrid solver finds S := argmin d(z, D) subject to z ∈ M (Maxwell-conforming). Alternates between: (1) finite element solver projecting into physics manifold M; (2) discrete optimization selecting closest measured material data points. Local weighting factors (tangent to current operating point) reduce iterations from ~1300 to ~55 regardless of data set size.

5. **Bayesian optimization for free-shape**: Multi-objective BO with GP surrogates; auxiliary optimization problems restricted to 2D affine subspaces spanned by adjoint-based gradients (maximum objective variance direction); converges Pareto front in ~100 design evaluations for a ~200-dimensional design space.

6. **Epistemic uncertainty**: "by circumventing the demand for a fixed material model, no epistemic uncertainties arise." The data-driven approach avoids model-form error (wrong constitutive relation) at the cost of requiring sufficient data coverage.

## Connection Candidates

- [[gaussian-distribution]] — uses (framework→concept): Gaussian priors and noise models enable analytic conditional posteriors in the BEM Bayesian update
- [[gibbs-sampler]] — uses (framework→technique): Gibbs sampling from p(ν,d|y) is the core inference procedure in the magnet characterization case
- [[gaussian-process-regression]] — uses (technique→technique): GP is the surrogate model in Bayesian optimization
- [[bayesian-linear-regression]] — uses: the BEM state estimation under Gaussian prior and Gaussian likelihood is exactly a Bayesian linear regression problem in disguise
- [[directed-graphical-models]] — uses: the joint model p(ν,d|y) ∝ p(y|ν,d)·p(ν)·p(d) is a simple three-node DGM
- [[kalman-filter]] — equivalent-in-context (technique→technique): the BEM + Bayesian update is a form of recursive Bayesian estimation analogous to Kalman filtering with non-standard observation operators
