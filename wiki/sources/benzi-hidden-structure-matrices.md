---
id: "pkis:source:benzi-hidden-structure-matrices"
aliases: []
title: "Exploiting Hidden Structure in Matrix Computations: Algorithms and Applications"
authors: ["Michele Benzi", "Dario Bini", "Daniel Kressner", "Hans Munthe-Kaas", "Charles Van Loan"]
year: 2016
type: book
domain: [optimization, statistical-learning]
tags: [linear-algebra, numerical-methods, tensors, structured-matrices, low-rank, toeplitz, hierarchical-matrices, group-theory, fourier-analysis]
source_url: ""
drive_id: "1V5uun0WcpF_OYywk2h14SA1Nwb1KK44C"
drive_path: "PKIS/sources/papers/benzi-hidden-structure-matrices.pdf"
isbn: "978-3-319-49886-7"
toc_source: "manual"
status: unread
date_added: 2026-05-20
concepts: ["[[structured-matrices]]", "[[tensor-decompositions]]", "[[hierarchical-low-rank-matrices]]", "[[toeplitz-matrices]]", "[[matrix-decompositions]]", "[[singular-value-decomposition]]"]
---

## Summary

This CIME Summer Course volume (Lecture Notes in Mathematics 2173, Springer 2016) collects lecture notes from five leading researchers on exploiting hidden and approximate structure in matrices for efficient computation. The unifying theme is that matrices arising in scientific computing often possess non-obvious structural properties — low-rank off-diagonal blocks, decay patterns, symmetries under group actions, displacement-rank representations — that can be exploited for dramatic algorithmic speedups.

Charles Van Loan covers structured matrix computations arising from tensors: Kronecker product structure, Tucker and CP decompositions, tensor train SVD, and how the curse of dimensionality motivates these representations. Dario Bini treats Toeplitz and Toeplitz-like matrices with displacement-rank characterizations, with applications to Markov modeling and queueing theory. Daniel Kressner (with Jonas Ballani) covers hierarchical low-rank matrices (H-matrices) and their application to the numerical solution of elliptic PDEs. Michele Benzi addresses matrices with off-diagonal decay, exponential localization in matrix functions, with applications to quantum physics and network science. Hans Munthe-Kaas covers group-theoretic methods in numerical linear algebra, including representation theory, the fast Fourier transform as harmonic analysis on finite groups, and geometric integration on Lie groups.

Together the chapters provide a systematic survey of how structure — Toeplitz, Hankel, low-rank, hierarchical, symmetric, group-equivariant — can be detected and exploited in algorithms for matrix equations, eigenproblems, and function evaluations.

## Chapters

| Ch | Stub | Title |
|---|---|---|
| 1 | [[benzi-hidden-structure-matrices-ch01]] | Structured Matrix Problems from Tensors (Van Loan) |
| 2 | [[benzi-hidden-structure-matrices-ch02]] | Matrix Structures in Queuing Models (Bini) |
| 3 | [[benzi-hidden-structure-matrices-ch03]] | Matrices with Hierarchical Low-Rank Structures (Ballani & Kressner) |
| 4 | [[benzi-hidden-structure-matrices-ch04]] | Localization in Matrix Computations: Theory and Applications (Benzi) |
| 5 | [[benzi-hidden-structure-matrices-ch05]] | Groups and Symmetries in Numerical Linear Algebra (Munthe-Kaas) |

## Key Knowledge Objects

- [[structured-matrices]] (concept, high) — matrices with non-obvious structural properties enabling sub-quadratic algorithms; includes Toeplitz, low-rank, hierarchical, displacement-rank types
- [[tensor-decompositions]] (technique, high) — Tucker, CP, tensor train SVD; generalizations of matrix SVD to multi-dimensional arrays
- [[hierarchical-low-rank-matrices]] (concept, high) — H-matrices: matrices with low-rank off-diagonal blocks enabling O(n log n) matrix-vector products for PDE applications
- [[toeplitz-matrices]] (concept, high) — constant-diagonal matrices; displacement-rank representation enables O(n log n) LU factorization via FFT
- [[matrix-decompositions]] (concept, high) — the broader framework this book enriches with structured variants
- [[singular-value-decomposition]] (technique, high) — the foundational decomposition extended and generalized throughout; Tucker decomposition generalizes SVD to tensors

## Key Extractions

1. **DFT as data-sparse structured factorization**: The n×n DFT matrix F_n is dense but can be factored into a product of O(log n) sparse matrices via Kronecker product structure, enabling the O(n log n) FFT. This is the canonical example of hidden structure enabling algorithmic efficiency.

2. **Displacement rank as a unified framework**: A matrix A has displacement rank r with respect to operators Ω and Γ if ΩA − AΓ has rank r. Toeplitz matrices have displacement rank 1; this characterization enables O(n²) arithmetic for Toeplitz LU rather than O(n³), since the displacement structure is preserved through Gaussian elimination steps.

3. **Hierarchical matrices for PDE applications**: For matrices arising from boundary element methods and elliptic PDEs, off-diagonal blocks have low numerical rank due to smoothness of the kernel. H-matrices represent these blocks in low-rank form, enabling O(n log² n) complexity for matrix-vector products and approximate factorizations.

4. **Tensor computations beat the curse of dimensionality**: A d-dimensional tensor with n entries per mode requires storing n^d entries naively. Tucker and tensor train decompositions represent it with O(d·n·r) parameters where r is the rank, making high-dimensional problems tractable when intrinsic dimensionality is low.

5. **Group-equivariant structure enables fast algorithms**: The FFT is an instance of harmonic analysis on finite groups (Z_n under addition). For other symmetry groups, representation theory provides analogous fast algorithms. This connects group theory to numerical linear algebra via structured factorizations that respect symmetry.

## Connection Candidates

- [[matrix-decompositions]] — extends: the book provides structured variants of classical decompositions (SVD → Tucker/CP/tensor train; LU → structured LU for Toeplitz)
- [[singular-value-decomposition]] — specializes: tensor decompositions generalize SVD; Tucker is the multi-mode SVD
- [[principal-component-analysis]] — uses: Tucker decomposition applied to data tensors generalizes PCA to multi-way data
- [[curse-of-dimensionality]] — contrasts-with: tensor decompositions provide a principled route around the curse when the target has low intrinsic rank
- [[eigendecomposition]] — extends: Hamiltonian matrix structure yields structured Schur decomposition exploiting plus-minus eigenvalue pairing
