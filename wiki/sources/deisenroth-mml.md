---
title: "Mathematics for Machine Learning"
authors: "Marc Peter Deisenroth, A. Aldo Faisal, Cheng Soon Ong"
year: 2020
type: book
domain: [statistical-learning, bayesian-stats, optimization]
tags: [linear-algebra, probability-theory, calculus, optimization, dimensionality-reduction, mathematical-foundations]
source_url: "https://mml-book.com"
drive_id: "1pd0ziFWZBYPaAGefEewmYZqhGcD5udYV"
drive_path: "PKIS/sources/books/Mathematics for Machine Learning - Deisenroth Faisal Ong.pdf"
status: unread
date_added: 2026-05-20
concepts:
  - "[[linear-algebra]]"
  - "[[analytic-geometry]]"
  - "[[matrix-decompositions]]"
  - "[[singular-value-decomposition]]"
  - "[[eigendecomposition]]"
  - "[[vector-calculus]]"
  - "[[automatic-differentiation]]"
  - "[[probability-theory]]"
  - "[[gaussian-distribution]]"
  - "[[conjugate-prior]]"
  - "[[continuous-optimization]]"
  - "[[gradient-descent]]"
  - "[[convex-optimization]]"
  - "[[lagrange-multipliers]]"
  - "[[empirical-risk-minimization]]"
  - "[[directed-graphical-models]]"
  - "[[bayesian-linear-regression]]"
  - "[[principal-component-analysis]]"
  - "[[gaussian-mixture-models]]"
  - "[[support-vector-machines]]"
  - "[[backpropagation]]"
---

## Summary

MML provides a unified mathematical treatment of the foundations underlying modern machine learning. Unlike ESL, which organizes around statistical methods, MML organizes around the mathematics itself — linear algebra, analytic geometry, matrix decompositions, vector calculus, probability theory, and optimization — then shows how each piece connects to core ML problems in Part II.

Part I (Chs 1–7) builds the mathematical substrate systematically. Chapter 2 develops linear algebra from first principles (vector spaces, linear independence, mappings). Chapter 3 adds geometric structure (inner products, norms, projections). Chapter 4 covers matrix decompositions including eigendecomposition and SVD, with a "matrix phylogeny" showing how all decompositions relate. Chapter 5 covers vector calculus with an explicit treatment of backpropagation as reverse-mode automatic differentiation — making the calculus underpinning neural network training precise. Chapter 6 builds probability theory from measure-theoretic foundations through the Gaussian, conjugate priors, and exponential families. Chapter 7 covers continuous optimization including gradient descent, Lagrange multipliers, and convex optimization.

Part II (Chs 8–12) applies this mathematics to five ML problems: the general learning framework (empirical risk minimization, MLE, probabilistic modeling, directed graphical models), linear regression (including Bayesian linear regression), PCA (derived from first principles via the variance maximization and minimum reconstruction error perspectives), density estimation with Gaussian mixture models, and classification via SVMs. Each chapter is deliberately sparse: it uses only the mathematical machinery from Part I, making the connections explicit.

The book is complementary to ESL — where ESL gives broad coverage of methods, MML gives deep coverage of the mathematics that justifies them.

## Key Knowledge Objects

**Part I — Mathematical Foundations (tag → node graduations):**
- [[linear-algebra]] (concept, high) — Ch 2: vector spaces, linear maps, affine spaces; foundational substrate
- [[analytic-geometry]] (concept, high) — Ch 3: inner products, norms, projections, orthogonality
- [[matrix-decompositions]] (concept, high) — Ch 4: organizing framework for eigendecomp, Cholesky, SVD
- [[singular-value-decomposition]] (technique, high) — Ch 4.5: dedicated treatment; geometric interpretation and matrix approximation
- [[eigendecomposition]] (technique, high) — Ch 4.4: diagonalization, connection to SVD
- [[vector-calculus]] (concept, high) — Ch 5: gradients, Jacobians, Hessians; foundation for optimization and backprop
- [[automatic-differentiation]] (technique, high) — Ch 5.6: backprop as a special case of reverse-mode AD; distinct from numerical differentiation
- [[probability-theory]] (concept, high) — Ch 6: measure-theoretic foundation, Bayes' theorem, independence
- [[gaussian-distribution]] (concept, high) — Ch 6.5: dedicated treatment; central to ML
- [[conjugate-prior]] (concept, high) — Ch 6.6: Bayesian updating with closed-form posteriors; exponential family
- [[continuous-optimization]] (concept, high) — Ch 7: unifying framing of gradient descent, constrained optimization, convex problems
- [[gradient-descent]] (technique, high) — Ch 7.1: steepest descent, step size, convergence
- [[convex-optimization]] (concept, high) — Ch 7.3: convexity, duality, KKT conditions
- [[lagrange-multipliers]] (technique, high) — Ch 7.2: constrained optimization via duality

**Part II — ML Applications:**
- [[empirical-risk-minimization]] (framework, high) — Ch 8.2: formal unification of supervised learning objectives
- [[directed-graphical-models]] (framework, high) — Ch 8.5: Bayesian networks, d-separation; complement to [[undirected-graphical-models]]
- [[bayesian-linear-regression]] (technique, high) — Ch 9.3: full posterior over weights; predictive distribution
- [[principal-component-analysis]] (technique, high) — Ch 10: derived from variance maximization AND minimum reconstruction error; connects to SVD
- [[gaussian-mixture-models]] (technique, high) — Ch 11: density estimation via EM; soft clustering
- [[support-vector-machines]] (technique, high) — Ch 12: derived rigorously from dual problem, KKT, kernel trick

**Cross-source updates (existing stubs):**
- [[backpropagation]] — Ch 5.6 treats backprop as reverse-mode AD; adds mathematical sources: [[vector-calculus]], [[automatic-differentiation]]

## Key Extractions

1. SVD generalizes eigendecomposition to non-square matrices. Every matrix $A \in \mathbb{R}^{m \times n}$ can be decomposed as $A = U\Sigma V^T$ where $U, V$ are orthogonal and $\Sigma$ is diagonal with non-negative entries (singular values). The rank-$k$ truncated SVD is the best rank-$k$ approximation in Frobenius norm. (Ch 4.5–4.6)

2. Backpropagation is the chain rule applied in reverse through a computational graph. The forward pass computes function values; the backward pass propagates gradients from output to input. Automatic differentiation generalizes this to arbitrary differentiable programs, not just neural networks. Symbolic differentiation and numerical differentiation are distinct and inferior approaches. (Ch 5.6)

3. The exponential family unifies Gaussian, Bernoulli, Poisson, Gamma and others under a single form $p(x|\theta) = h(x)\exp(\theta^T\phi(x) - A(\theta))$. Conjugate priors arise naturally: the prior and posterior have the same functional form when the prior is conjugate to the likelihood. (Ch 6.6)

4. PCA can be derived two ways: (a) find directions of maximum variance in the data; (b) find the subspace that minimizes reconstruction error. Both derivations yield the same answer — the top eigenvectors of the data covariance matrix — and the connection to SVD makes computation efficient. (Ch 10)

5. The SVM dual problem reveals the kernel trick: the decision boundary depends on the data only through inner products $\langle x_i, x_j \rangle$, which can be replaced by any positive definite kernel $k(x_i, x_j)$. This implicitly maps data to a high-dimensional feature space without computing the mapping explicitly. (Ch 12)

6. Empirical risk minimization (ERM) is the formal framework underlying supervised learning: minimize the empirical loss over training data as a surrogate for true risk (expected loss). The choice of loss function and hypothesis class determines the method. (Ch 8.2)

## Chapters

| Ch. | Title | Key topics |
|---|---|---|
| 1 | Introduction and Motivation | Two reading paths: bottom-up (math first) vs top-down (ML first) |
| 2 | Linear Algebra | Vector spaces, linear independence, basis, linear maps, affine spaces |
| 3 | Analytic Geometry | Norms, inner products, projections, orthogonality, rotations |
| 4 | Matrix Decompositions | Eigenvalues/vectors, Cholesky, eigendecomposition, SVD, matrix approximation |
| 5 | Vector Calculus | Gradients, Jacobians, Hessians, backprop as reverse-mode AD, Taylor series |
| 6 | Probability and Distributions | Probability spaces, Bayes' theorem, Gaussian, conjugate priors, exponential family |
| 7 | Continuous Optimization | Gradient descent, Lagrange multipliers, convex optimization, KKT |
| 8 | When Models Meet Data | ERM, MLE, probabilistic modeling, directed graphical models, model selection |
| 9 | Linear Regression | OLS, MLE as orthogonal projection, Bayesian linear regression |
| 10 | Dimensionality Reduction with PCA | Variance maximization and reconstruction error views; SVD connection |
| 11 | Density Estimation with Gaussian Mixture Models | EM for GMMs; soft assignment; model selection |
| 12 | Classification with Support Vector Machines | Margin maximization, dual problem, kernel trick, KKT conditions |

## Connection Candidates

- [[hastie-esl]] — strongly complementary: MML provides the mathematical justification for methods ESL describes. Synthesizer should draw explicit `grounds` edges from MML's math nodes to ESL's method nodes.
- [[backpropagation]] — Ch 5.6 deepens this existing stub substantially; `automatic-differentiation` `generalizes` `backpropagation`
- [[undirected-graphical-models]] — Ch 8.5 develops directed graphical models, the counterpart; `contrasts-with` edge
- [[em-algorithm]] — Ch 11 applies EM to GMMs; adds source to existing stub
- [[principal-component-analysis]] — Ch 10 gives mathematical derivation from first principles; adds source to existing stub
- [[support-vector-machines]] — Ch 12 derives SVMs rigorously from duality; adds source to existing stub
