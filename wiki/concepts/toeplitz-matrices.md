---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- optimization
id: pkis:concept:toeplitz-matrices
knowledge_type: concept
maturity: settled
related_concepts:
- '[[structured-matrices]]'
- '[[matrix-decompositions]]'
- '[[linear-algebra]]'
sources:
- '[[benzi-hidden-structure-matrices]]'
- benzi-hidden-structure-matrices-ch02
tags:
- linear-algebra
- structured-matrices
- displacement-rank
- fft
- time-series
- signal-processing
- convolution
title: Toeplitz Matrices
understanding: 0
---

Matrices in which each descending diagonal from left to right is constant: T_{ij} = t_{i-j}. A Toeplitz matrix has displacement rank 1 with respect to the shift operators Ω = diag(ω_i) and Γ = diag(γ_i), meaning ΩT − TΓ = rs^T for vectors r, s ∈ R^n. This displacement-rank characterization is preserved through Gaussian elimination steps, enabling the LU factorization to be computed in O(n²) operations rather than O(n³). Multiplication of a Toeplitz matrix by a vector is a convolution, computable in O(n log n) via FFT.

Toeplitz structure arises naturally in stationary time series covariance matrices, convolutional neural networks, and signal processing applications.

## Reading Path
- [[benzi-hidden-structure-matrices]] (unread) — Ch. 2 (Bini): displacement rank framework, structured LU, Toeplitz-like matrices, queueing theory applications
- [[benzi-hidden-structure-matrices-ch02]] (unread) — primary chapter