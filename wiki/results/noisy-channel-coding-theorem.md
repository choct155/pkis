---
aliases: []
also_type: []
applies:
- binary-symmetric-channel
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
contrasts-with:
- repetition-codes
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- information-theory
id: pkis:result:noisy-channel-coding-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- typical-set
related_concepts: []
sources:
- mackay-itila-ch01
tags:
- shannon
- capacity
- channel-coding
- fundamental-limit
- reliable-communication
title: Noisy-Channel Coding Theorem
understanding: 0
uses:
- channel-capacity
- random-coding-argument
- fanos-inequality
---

## Definition
Shannon's central theorem (1948): for any noisy channel there exist codes permitting communication with **arbitrarily small** error probability $p_b$ at any rate $R$ below the channel **capacity** $C$, and reliable communication at rates above $C$ is impossible.
$$R<C \;\Rightarrow\; p_b \text{ can be made} \to 0; \qquad R>C \;\Rightarrow\; \text{reliable communication impossible.}$$

The intuition: the achievable boundary in the $(R,p_b)$ plane meets the rate axis at the *non-zero* value $R=C$, not at the origin — you can have both finite rate and vanishing error.

### Limitations and possibilities
The theorem is two-sided: a **converse** (no scheme beats capacity) and an **achievability** result (capacity is reachable). It is non-constructive — it proves good codes exist without exhibiting practical ones, a gap that coding theory spent decades closing.

### Why it matters
This result created information theory and overturned the prevailing 'no pain, no gain' belief. It is the destination of the first half of MacKay's book: entropy, typical sets, and source coding are all developed to prove and exploit it.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[fanos-inequality]] — uses: The converse combines Fano's inequality with the data processing inequality.
- [[random-coding-argument]] — uses: Achievability is proved by averaging error over a random ensemble of codes.
- [[typical-set]] — prerequisite-of: MacKay develops typical sets to prove the coding theorem in later chapters.
- [[binary-symmetric-channel]] — applies: The theorem holds for any channel, including the binary symmetric channel used throughout the chapter.
- [[repetition-codes]] — contrasts-with: Repetition codes need rate to vanish for small error; the theorem proves finite rate at vanishing error is achievable.
- [[channel-capacity]] — uses: The theorem states reliable communication is possible exactly for rates below the channel capacity C.
[To be populated during integration]

## ## Proof: achievability and converse
MacKay's proof has two halves built from typical-set machinery.

**Achievability (rate $R<C$ is reachable).** Use a [[random-coding-argument]]: fix the optimal input distribution $P(x)$, draw $2^{NR'}$ codewords i.i.d., transmit, and decode by [[joint-typicality-decoding]]. Averaging over all codes, an error occurs only if (a) the sent pair is not jointly typical (probability $\delta\to0$) or (b) a rival codeword is jointly typical with $\mathbf{y}$ (each $\le 2^{-N(I(X;Y)-3\beta)}$). A union bound over the $2^{NR'}-1$ rivals gives
$$\langle p_B\rangle\le\delta+2^{-N(I(X;Y)-R'-3\beta)},$$
which vanishes whenever $R'<I(X;Y)-3\beta$. Choosing $P(x)$ optimal makes $I(X;Y)=C$; existence of one good code follows from the average; expurgating the worst half of codewords converts small *average* error into small *maximal* error at a negligible rate cost. Setting $R'=(R+C)/2$ and $N$ large completes part 1.

**Extending to non-zero $p_b$.** Running a capacity-achieving code's decoder *backwards* as a lossy compressor proves the achievability of the whole region $R=C/(1-H_2(p_b))$ (rate-distortion).

**Converse (rates above the boundary are impossible).** The chain $s\to x\to y\to\hat{s}$ obeys the data processing inequality, so $I(s;\hat{s})\le I(x;y)\le NC$. [[fanos-inequality]] gives $I(s;\hat{s})\ge NR(1-H_2(p_b))$. Together they force $R\le C/(1-H_2(p_b))$ — anything beyond is unachievable. $\square$

## ## Finite-blocklength refinement and the reliability function
The basic theorem is general but silent on *how large* $N$ must be for a target $(R,\epsilon)$. A sharper version bounds the error exponentially in blocklength:
$$p_B\le \exp[-N E_r(R)],$$
where $E_r(R)$, the **random-coding exponent** (or reliability function), is a convex $\smile$, decreasing, positive function of $R$ on $0\le R<C$, vanishing as $R\to C$. A matching lower bound,
$$p_B\gtrsim \exp[-N E_{sp}(R)],$$
uses the **sphere-packing exponent** $E_{sp}(R)$. These exponents say error decays exponentially in $N$ for any fixed $R<C$, but the closer $R$ is to $C$ the slower the decay. Even for the binary symmetric channel there is no closed form for $E_r(R)$, and a random code of large $N$ costs exponentially to implement — which is why practical coding theory matters.