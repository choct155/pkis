---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:result:benfords-law
instantiates:
- proportionality-postulate
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch35
tags:
- benfords-law
- scale-invariance
- ignorance-prior
- first-digit
- logarithmic-prior
- improper-prior
title: Benford's Law
understanding: 0
uses:
- automatic-priors
---

## Definition
**Benford's law** states that for a quantity about whose scale one is wholly ignorant, the leading significant digit $d \in \{1,\dots,9\}$ is *not* uniformly distributed but follows

$$P(\text{first digit} = d) = \log_{10}\!\left(1 + \frac{1}{d}\right).$$

So a leading $1$ occurs with probability $\log_{10} 2 \approx 0.301$, while a leading $9$ occurs with probability $\log_{10}(10/9) \approx 0.046$ — nearly seven times rarer.

### Derivation from scale invariance
If you do not know the *units* in which a positive quantity $x$ is measured (seconds vs. years, metres vs. fortnights), your beliefs about $x$ should be unchanged when $x$ is multiplied by any positive constant. This scale invariance forces a prior that is uniform on the *logarithmic* axis: $P(\log x) \propto \text{const}$, equivalently $P(x) \propto 1/x$ (an improper, Jeffreys-type prior). The probability of a leading digit is then proportional to the length of logarithmic scale it occupies between $\log_{10} d$ and $\log_{10}(d{+}1)$, giving the law above. A handy mental check: $2^{10}=1024\approx 10^3$, so $10\log_{10}2 \approx 3$ and $P(1)\approx 3/10$.

### Why it matters
Benford's law is the canonical demonstration that **"knowing nothing" is not the same as a uniform distribution**. The correct ignorance prior is dictated by the symmetry (here, scale invariance) of the problem, an instance of constructing automatic/transformation-group priors. Empirically the law holds across physical constants, financial figures, and population counts, and its violation is used as a forensic test for fabricated data (fraud detection in accounting and election returns).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[automatic-priors]] — uses: The log-uniform first-digit distribution is derived as a transformation-group (scale-invariant) automatic prior.
- [[proportionality-postulate]] — instantiates: Benford's law is what 'ignorance' actually looks like: the scale-invariant ignorance prior, not a uniform one.
[To be populated during integration]