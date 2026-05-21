---
title: "Applied Probability (Third Edition)"
authors: "Kenneth Lange"
year: 2024
type: book
domain: [bayesian-stats, optimization, information-theory]
tags: [probability-theory, stochastic-processes, combinatorics, markov-chains, measure-theory, simulation, information-theory]
source_url: "https://doi.org/10.1007/978-1-0716-4172-9"
drive_id: "1wZuwtmVeq5cZcvd-QiSPVsMIzMoWaCld"
drive_path: "PKIS/sources/books/Applied Probability - Lange.pdf"
isbn: "978-1-0716-4171-2"
toc_source: "manual"
status: unread
date_added: 2026-05-20
concepts:
  - "[[probability-theory]]"
  - "[[markov-chains]]"
  - "[[poisson-process]]"
  - "[[martingales]]"
  - "[[diffusion-processes]]"
  - "[[branching-processes]]"
  - "[[entropy]]"
  - "[[convex-optimization]]"
  - "[[continuous-optimization]]"
  - "[[mm-algorithm]]"
  - "[[mcmc]]"
  - "[[gibbs-sampler]]"
  - "[[metropolis-algorithm]]"
  - "[[em-algorithm]]"
  - "[[generating-functions]]"
  - "[[importance-sampling]]"
---

## Summary

Applied Probability is a graduate-level textbook by Kenneth Lange (UCLA) aimed at students in applied mathematics, biostatistics, computational biology, computer science, physics, and statistics. Now in its third edition (2024), the book seeks a balance between mathematical rigor and practical motivation, covering both classical probability theory and its computational extensions.

The book is organized in three broad movements. The first (Ch. 1–5) builds the theoretical and combinatorial substrate: basic probability axioms and the multivariate normal distribution, techniques for computing expectations, convexity and optimization including the MM algorithm, and two chapters on combinatorics and combinatorial algorithms. The second movement (Ch. 6–11) covers core stochastic processes: Poisson processes, discrete- and continuous-time Markov chains (including MCMC and simulated annealing), branching processes, martingales, and diffusion processes. This block alone provides sufficient material for a traditional semester-long stochastic processes course. The third movement (Ch. 12–16) covers asymptotic methods, numerical methods for stochastic computations, Poisson approximation via the Chen-Stein method, an unconventional chapter applying probability to number theory, and a new chapter on entropy and its mathematical applications (added in the third edition).

The book is notable for its emphasis on computation: Julia code is provided, stochastic simulation appears throughout, and numerical methods for Markov chains and diffusion processes receive dedicated coverage. The third edition added sections on the Chinese Restaurant Process, the Infinite Alleles Model, saddlepoint approximations, recurrence relations, and the new chapter on Shannon entropy and EM algorithms from an information-theoretic perspective.

## Key Knowledge Objects

- [[probability-theory]] (concept, high) — formal axiomatic foundation; σ-fields, probability measures, expectations, conditional probability
- [[markov-chains]] (concept, high) — discrete- and continuous-time Markov chains; central stochastic process object of the book
- [[poisson-process]] (concept, high) — counting process with independent increments; core model for random event arrivals
- [[martingales]] (concept, high) — fair-game processes; convergence theorems, optional stopping, large deviation bounds
- [[diffusion-processes]] (concept, high) — continuous-time, continuous-state processes; Brownian motion, Itô-type equations, first passage
- [[branching-processes]] (concept, high) — models of population growth; extinction theory, multitype processes, applications to epidemiology and genetics
- [[entropy]] (concept, high) — Shannon entropy and information-theoretic applications; maximum entropy, EM connection
- [[mm-algorithm]] (technique, high) — majorization-minimization optimization framework; generalization of EM
- [[mcmc]] (technique, high) — Markov chain Monte Carlo; Hastings-Metropolis and Gibbs sampling treated in Ch. 7
- [[generating-functions]] (technique, moderate — could be concept) — probability generating functions, moment generating functions, and cumulant generating functions as analytic tools
- [[convex-optimization]] (concept, high) — convex functions, Jensen's inequality, MM algorithm framing; Ch. 3
- [[em-algorithm]] (technique, high) — appears in Ch. 16 from an entropy perspective; EM as entropy maximization
- [[gibbs-sampler]] (technique, high) — MCMC via full conditionals; treated as special case of Hastings-Metropolis in Ch. 7
- [[metropolis-algorithm]] (technique, high) — Hastings-Metropolis acceptance-rejection MCMC; Ch. 7
- [[importance-sampling]] (technique, high) — covered in context of numerical methods and approximation
- poisson-approximation (low — technique or result?) — Chen-Stein bounds; could be a result (theorem) or a technique (estimation method)

## Key Extractions

1. The MM (majorization-minimization) algorithm generalizes EM: any algorithm that finds a tangent majorant and minimizes it is an MM algorithm. EM is the special case where the majorant is constructed using Jensen's inequality on the log-likelihood. (Ch. 3.4)

2. "Coupling" is a key probabilistic technique for proving convergence of Markov chains: construct two chains sharing a probability space and bound the total variation distance by the probability they have not yet met. (Ch. 7.4)

3. Branching processes provide the mathematical foundation for basic reproduction numbers: a population survives iff the expected offspring per individual R₀ > 1; extinction probability is the smallest fixed point of the probability generating function. (Ch. 9)

4. The martingale optional stopping theorem: if a stopping time T satisfies regularity conditions (e.g., bounded or integrable), then E[M_T] = E[M_0]. This underlies many gambling-ruin and random walk results. (Ch. 10.4)

5. The Chen-Stein method gives quantitative Poisson approximation bounds: for rare events with weak dependencies, the total variation distance between the distribution of the count and a Poisson is bounded by sums of pairwise probabilities. (Ch. 14)

6. Shannon entropy H(X) = −∑ p_i log p_i measures average uncertainty; the maximum entropy distribution subject to moment constraints is the exponential family. This connects entropy to statistical mechanics and Bayesian priors. (Ch. 16)

7. Saddlepoint approximations provide highly accurate tail probability estimates by exploiting the cumulant generating function; they outperform normal approximations even in small samples. (Ch. 12.7)

## Connection Candidates

- [[probability-theory]] — this book is the primary applied treatment; `prerequisite-of` edge to virtually all stochastic process concepts
- [[em-algorithm]] (technique, existing) — Ch. 16 provides an entropy-based perspective on EM distinct from the likelihood-based view in Tanner and ESL; `extends` edge
- [[gibbs-sampler]] (technique, existing) — Ch. 7 positions Gibbs as a special case of Hastings-Metropolis; `specializes` edge
- [[metropolis-algorithm]] (technique, existing) — Ch. 7 gives foundational MCMC treatment; `extends` edge to general MCMC
- [[convex-optimization]] (concept, existing) — Ch. 3 contributes the MM algorithm and majorization framing, extending the concept; `extends` edge
- [[importance-sampling]] (technique, existing) — asymptotic methods chapter connects to Monte Carlo importance sampling
- [[state-space-models]] (framework, existing) — continuous-time Markov chains and diffusion processes are the continuous-state counterpart; `generalizes` edge candidate

## Awaiting Classification

- **poisson-approximation** — candidate types: result or technique
  - Case for result: the Chen-Stein bounds are theorems (proven claims about approximation error)
  - Case for technique: the Chen-Stein method is a procedure applied to bounding rare-event probabilities
  - What makes this hard: the chapter covers both the theorem and its application as an estimation strategy

## Chapters

| Ch | Stub | Title |
|---|---|---|
| 1 | [[lange-applied-probability-ch01]] | Basic Notions of Probability Theory |
| 2 | [[lange-applied-probability-ch02]] | Calculation of Expectations |
| 3 | [[lange-applied-probability-ch03]] | Convexity, Optimization, and Inequalities |
| 4 | [[lange-applied-probability-ch04]] | Combinatorics |
| 5 | [[lange-applied-probability-ch05]] | Combinatorial Optimization |
| 6 | [[lange-applied-probability-ch06]] | Poisson Processes |
| 7 | [[lange-applied-probability-ch07]] | Discrete-Time Markov Chains |
| 8 | [[lange-applied-probability-ch08]] | Continuous-Time Markov Chains |
| 9 | [[lange-applied-probability-ch09]] | Branching Processes |
| 10 | [[lange-applied-probability-ch10]] | Martingales |
| 11 | [[lange-applied-probability-ch11]] | Diffusion Processes |
| 12 | [[lange-applied-probability-ch12]] | Asymptotic Methods |
| 13 | [[lange-applied-probability-ch13]] | Numerical Methods |
| 14 | [[lange-applied-probability-ch14]] | Poisson Approximation |
| 15 | [[lange-applied-probability-ch15]] | Number Theory |
| 16 | [[lange-applied-probability-ch16]] | Entropy |
