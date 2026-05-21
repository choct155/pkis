---
title: "The Term Structure of Interest Rates in a DSGE Model with Recursive Preferences"
authors: "Jules H. van Binsbergen, Jesús Fernández-Villaverde, Ralph S.J. Koijen, Juan F. Rubio-Ramírez"
year: 2011
type: paper
domain: [macroeconomics, bayesian-stats, time-series, state-space-models]
tags: [dsge, recursive-preferences, epstein-zin, yield-curve, particle-filter, perturbation-methods, maximum-likelihood, asset-pricing, bond-pricing, macro-finance]
source_url: "https://ssrn.com/abstract=1569916"
drive_id: "1-6gavtJlmE0Hs15cgRkn_BZEl_PZhcLs"
drive_path: "PKIS/sources/papers/term-structure-dsge-recursive-prefs.pdf"
status: unread
date_added: 2026-05-20
concepts:
  - "[[recursive-preferences]]"
  - "[[dsge-models]]"
  - "[[perturbation-methods-dsge]]"
  - "[[particle-filter]]"
  - "[[stochastic-discount-factor]]"
  - "[[bond-risk-premium]]"
  - "[[intertemporal-elasticity-of-substitution]]"
  - "[[adjustment-costs-of-capital]]"
  - "[[term-structure-of-interest-rates]]"
  - "[[welfare-cost-of-business-cycles]]"
---

## Summary

Van Binsbergen, Fernández-Villaverde, Koijen, and Rubio-Ramírez study whether a Dynamic Stochastic General Equilibrium (DSGE) model in which a representative household holds Epstein-Zin (EZ) recursive preferences can jointly match macroeconomic data and the yield curve. The paper makes three interconnected contributions.

The first contribution is methodological: the authors solve the model using perturbation methods applied to the value function, obtaining a third-order Taylor approximation to equilibrium dynamics. This choice is motivated by the need for time-varying risk premia (which require at least a third-order solution), computational speed sufficient to support likelihood estimation, and the ability to handle arbitrary values of the intertemporal elasticity of substitution (IES) — unlike methods that linearize around IES = 1. Key insight from the perturbation: the first-order approximation is certainty equivalent and does not depend on risk aversion; risk aversion appears only at second order (as a constant shifting the ergodic distribution of capital) and at third order (through state-dependent coefficients).

The second contribution is estimation: the authors embed the perturbation solution into a state-space representation and evaluate the likelihood via a particle filter (sequential importance resampling), then maximize using a derivative-free evolutionary algorithm (CMA-ES). This imposes all cross-equation restrictions implied by the equilibrium model — contrasting with the calibration approach common in asset pricing.

The third contribution is empirical: using US data (1953Q1–2008Q4) on consumption growth, output growth, five bond yields (1–5 year), and inflation, the model estimates a high risk aversion coefficient (~79), IES well above one (~1.73), and substantial capital adjustment costs. The model matches the level and autocorrelation of yields reasonably well but substantially underestimates the term spread (17 vs 59 basis points) and yield volatility. The tension is traced to inflation dynamics: relaxing inflation discipline (omitting inflation from estimation) dramatically improves yield-curve fit at the cost of unrealistically high inflation volatility. This illustrates a fundamental tension in jointly fitting macro aggregates and the nominal yield curve within a production economy DSGE framework.

## Key Knowledge Objects

- [[recursive-preferences]] (concept, high) — Epstein-Zin utility that separates risk aversion from the intertemporal elasticity of substitution; the paper's defining preference specification
- [[dsge-models]] (framework, high) — Dynamic Stochastic General Equilibrium modeling: the structural macro framework used to derive and estimate all equilibrium dynamics and asset prices
- [[perturbation-methods-dsge]] (technique, high) — higher-order Taylor approximation of DSGE equilibrium conditions around the deterministic steady state; enables fast, accurate solution needed for ML estimation
- [[particle-filter]] (technique, high) — sequential Monte Carlo method for evaluating the likelihood of nonlinear state-space models; key tool for estimation given the model's nonlinear solution
- [[stochastic-discount-factor]] (concept, high) — the pricing kernel derived from the EZ household's optimality conditions, which prices all assets including nominal bonds at any maturity
- [[bond-risk-premium]] (concept, high) — the compensation demanded by investors for holding longer-duration nominal bonds rather than rolling over short-term bonds; the paper attempts to match this empirically
- [[intertemporal-elasticity-of-substitution]] (concept, high) — the parameter governing willingness to substitute consumption across time; estimated at ~1.73, well above one, and identified separately from risk aversion under EZ preferences
- [[adjustment-costs-of-capital]] (concept, moderate — could be technique) — the Jermann (1998) specification of convex installation costs that reduce how quickly capital responds to shocks; identified from yield-curve data
- [[term-structure-of-interest-rates]] (concept, high) — existing node; this paper provides a structural, production-economy, ML-estimated perspective on the nominal yield curve
- [[welfare-cost-of-business-cycles]] (result, moderate — could be concept) — the consumption-equivalent cost of eliminating aggregate productivity uncertainty, calculated from the second-order perturbation term; estimated at ~25% of consumption under the estimated risk aversion

## Key Extractions

1. **Separation of risk aversion and IES is the key EZ advantage.** Under standard CRRA preferences, risk aversion (γ) and the IES (ψ) are linked by ψ = 1/γ. EZ preferences break this link, allowing the authors to estimate γ ≈ 79 and ψ ≈ 1.73 independently — a combination that is quantitatively important for matching both macro dynamics and asset prices.

2. **Risk aversion is not identified at first order.** "A linear approximation to the decision rules does not depend on the risk aversion parameter or on the variance level of the productivity shock." Risk aversion first appears in the second-order approximation as a constant shift to the ergodic distribution of capital (affecting average yield levels and slopes), and in third-order coefficients (affecting yield responses to state variables). This explains why earlier methods that linearize the model cannot identify γ.

3. **Fundamental macro-finance tension.** The model fails to jointly reproduce both the term premium and inflation dynamics: "while we can match inflation volatility the model is barely able to generate an upward-sloping term structure." When inflation data are omitted from estimation, the bond risk premium and yield volatility improve dramatically but inflation volatility is overestimated by 60%. This identifies the core tension as residing in the constraints that observed inflation places on the correlation structure between the SDF and inflation innovations.

4. **Yield data are highly informative about structural parameters.** Re-estimating with only bond yields produces estimates (γ ≈ 97, ψ ≈ 1.77) remarkably similar to estimates using macro data as well. This confirms Hall's (1988) intuition that "a cross-section of asset yields is highly informative about the values of preference parameters" and motivates incorporating finance data into DSGE estimation.

5. **Third-order perturbation enables time-varying risk premia.** Third-order terms introduce state-dependent coefficients multiplied by γ², allowing risk premia to vary with the state of the economy. This feature is absent in first- and second-order approximations.

6. **Preference for early resolution of uncertainty.** Since the estimated ψ > 1, the household prefers early resolution of uncertainty (the reciprocal of ψ is less than 1 and less than 1/γ in the EZ framework). The estimated parameters imply θ = (1 − γ)/(1 − 1/ψ) ≈ −185, a large negative value signaling very different attitudes toward intertemporal and across-state substitution.

7. **Perturbation vs. value function iteration.** The authors argue perturbation's main advantage over projection methods (value function iteration, Chebyshev) is speed: the model can be solved in "a trivial amount of time" for each parameter candidate, making the 100-replication bootstrap for standard errors computationally feasible.

## Connection Candidates

- [[term-structure-of-interest-rates]] — extends: provides a full structural, ML-estimated DSGE account of the nominal yield curve, explaining it as an equilibrium outcome of preferences (EZ), technology shocks, and inflation dynamics
- [[stochastic-discount-factor]] — uses: bond prices at all maturities are computed recursively using the EZ-derived SDF; the SDF is the central object connecting preferences to asset prices
- [[recursive-preferences]] — grounds: the entire paper is an empirical investigation of what EZ preferences imply for macro dynamics and the yield curve; the estimated parameters sharpen the literature's understanding of EZ
- [[particle-filter]] — uses: likelihood evaluation for the nonlinear state-space representation requires the particle filter (rather than the Kalman filter, which assumes linearity)
- [[dsge-models]] — uses: the DSGE framework provides all structural equilibrium conditions that discipline the estimation and create cross-equation restrictions the model must satisfy
- [[state-space-models]] — uses: the perturbation solution is cast as a nonlinear state-space system (transition + measurement equations) to enable likelihood-based estimation
- [[kalman-filter]] — contrasts-with: the paper explicitly notes that the Kalman filter cannot be applied because the third-order perturbation solution is inherently nonlinear; particle filter is the necessary substitute
- [[mcmc]] — contrasts-with: while the authors note Metropolis-Hastings could provide Bayesian inference, they focus on ML via CMA-ES; both approaches must contend with the simulation-approximated likelihood
- [[maximum-likelihood-estimation]] — uses: structural parameter estimation is performed by maximizing the particle-filter-approximated likelihood using the CMA-ES evolutionary algorithm
- [[no-arbitrage-pricing]] — uses: nominal bond prices are derived from the Euler equation (no-arbitrage condition) recursively using the SDF and the bond pricing formula

## Awaiting Classification

- **adjustment-costs-of-capital** — candidate types: concept or technique
  - Case for concept: it is a modeling assumption (a specific functional form due to Jermann, 1998) with a clear definition and boundary; the paper treats it as a structural parameter to estimate
  - Case for technique: from a calibration standpoint, one "applies" adjustment costs to a model as a modeling device; it has inputs (investment rate, steady-state parameters) and outputs (effective capital accumulation)
  - What makes this hard: adjustment costs straddle an idea (the notion that capital installation is costly) and a modeling tool (the specific functional form used in quantitative work)

- **welfare-cost-of-business-cycles** — candidate types: result or concept
  - Case for result: it is a derived quantity — a proven formula from the second-order perturbation term — and the estimated value (~25% of consumption) is an empirical finding
  - Case for concept: the welfare cost of the business cycle is a well-defined theoretical construct studied independently of this paper (Lucas 1987); it has definitional content separate from any one calculation
  - What makes this hard: the paper both defines and quantifies this object, blurring the line between the concept and its instantiation as a result
