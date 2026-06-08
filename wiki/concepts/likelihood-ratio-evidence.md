---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
id: pkis:concept:likelihood-ratio-evidence
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch03
tags:
- likelihood-ratio
- bayes-factor
- prosecutors-fallacy
- base-rate
- weight-of-evidence
title: Likelihood Ratio as Evidence
understanding: 0
uses:
- bayesian-inference
---

## Definition
The contribution of a single body of data $D$ to a binary question $S$ vs. $\bar S$ is exactly the likelihood ratio $P(D\mid S)/P(D\mid \bar S)$, which multiplies the prior odds to give the posterior odds. Evidence is *relative*: data that raise the probability of one hypothesis must lower that of some other.

### Why it matters
It separates the data's contribution from the prior, which is essential in forensic and diagnostic reasoning. In MacKay's blood-trace example, type-O blood (60% frequent) found at the scene gives ratio $1/(2p_O)=0.83$ — *weak evidence against* the type-O suspect, not for him, because common evidence is expected anyway.

### The prosecutor's fallacy
Confusing $P(D\mid H)$ with $P(H\mid D)$ corrupts this reasoning. The wife-beater lawyer cites $P(\text{murder}\mid \text{beating})=1/1000$, but the relevant quantity is $P(\text{guilty}\mid \text{murdered \& beaten})\approx 95\%$. The likelihood ratio, applied correctly, is the antidote.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-inference]] — uses: posterior odds = likelihood ratio x prior odds, a direct application of Bayes' theorem
[To be populated during integration]

## Bitwise Confirmation of a Hash Hit
When a hash table returns a candidate record $s$, comparing the stored $\mathbf{x}^{(s)}$ against the query $\mathbf{x}$ bit by bit accumulates Bayesian evidence. Under $H_0: \mathbf{x}^{(s)}=\mathbf{x}$ versus $H_1: \mathbf{x}^{(s)}\neq\mathbf{x}$ (random strings), each matching bit contributes likelihood ratio $\frac{P(\text{match}\mid H_0)}{P(\text{match}\mid H_1)} = \frac{1}{1/2} = 2$. After $r$ matching bits the odds are $2^r:1$, so just 30 matching bits give billion-to-one confidence that the correct entry was retrieved — long before checking all $N$ bits. The same logic scores a casting-out-nines check (one digit match $\Rightarrow$ 9:1 evidence the addition is correct).

## Bans, Decibans, and Banburismus
Weights of evidence inherit units from the logarithm base: $\log_2$ gives **bits** (a.k.a. shannons), $\log_e$ gives **nats**, and $\log_{10}$ gives **bans**, with one tenth of a ban being a **deciban** — named for Banbury, where the tally sheets for Bletchley Park's *Banburismus* were printed, and judged the smallest weight of evidence a human can discern.

The codebreaking application mirrors the bitwise hash-hit logic above. To test whether two Enigma cyphertexts share a machine state, each synchronized character match contributes $\log mA$ in favour of the 'same-state' hypothesis (with match probability $m=\sum_i p_i^2 \approx 2/26$ for English), each non-match a small amount against it. Summed over a few hundred characters, this weak per-symbol signal accumulates to decisive odds — about 20 decibans (100:1) per 400 characters. See [[bayesian-codebreaking]].