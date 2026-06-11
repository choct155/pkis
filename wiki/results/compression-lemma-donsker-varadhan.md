---
aliases: []
also_type: []
applies:
- mutual-information
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- information-theory
- machine-learning
- statistics
id: pkis:result:compression-lemma-donsker-varadhan
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch05
tags:
- kl-divergence
- pac-bayes
- variational
- bounds
- donsker-varadhan
title: Compression Lemma (Donsker-Varadhan Representation)
understanding: 0
uses:
- kl-divergence
- information-inequality
- jensens-inequality
---

## Definition
For any distributions $P$ and $Q$ and any measurable function $\phi$:

$$\mathbb{E}_P[\phi] \leq \log \mathbb{E}_Q\left[e^\phi\right] + D_{\mathrm{KL}}(P \| Q)$$

Equivalently, the KL divergence admits the variational representation:

$$D_{\mathrm{KL}}(P \| Q) = \sup_\phi \,\mathbb{E}_P[\phi] - \log \mathbb{E}_Q\left[e^\phi\right]$$

The supremum is achieved when $\phi(x) = \log(p(x)/q(x))$. The bound follows from non-negativity of $D_{\mathrm{KL}}(P \| G)$ where $G \propto Q e^\phi$.

### Why it matters
The compression lemma is a workhorse for deriving PAC-Bayes generalization bounds, free-energy bounds in statistical physics, and mutual information estimators. It converts an expectation bound into a KL-regularized variational problem, enabling tractable optimization over function classes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mutual-information]] — applies: Provides variational lower bounds on mutual information
- [[jensens-inequality]] — uses
- [[information-inequality]] — uses
- [[kl-divergence]] — uses
[To be populated during integration]