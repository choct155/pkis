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
date_updated: '2026-06-20'
domain:
- information-theory
id: pkis:concept:channel-capacity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- noisy-channel-coding-theorem
related_concepts: []
sources:
- mackay-itila-ch01
- cote-visual-intro-information-theory-2022
tags:
- capacity
- noisy-channel
- rate
- mutual-information
- shannon
title: Channel Capacity
understanding: 0
uses:
- information-theory
- mutual-information
---

## Definition
The **capacity** $C$ of a noisy channel is the maximum rate at which information can be communicated with arbitrarily small probability of error. Formally it is the maximum, over input distributions, of the mutual information between channel input and output:
$$C=\max_{p(x)} I(X;Y).$$
It is the point where the boundary between achievable and non-achievable $(R,p_b)$ points meets the rate axis.

The intuition: every channel, however noisy, has a hard ceiling on reliable throughput — and that ceiling is strictly positive.

### The surprise
It was widely believed the achievable boundary passed through the origin, so vanishing error would demand vanishing rate ('no pain, no gain'). Capacity says otherwise: reliable communication is possible at *every* rate $R<C$, and impossible for $R>C$.

### Why it matters
Capacity is the central quantity of information theory: it sets the fundamental limit that no encoder/decoder can beat and the target that good codes approach. It connects coding (channel side) to entropy and mutual information (the measurement side), unifying compression and communication.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mutual-information]] — uses: C = max over input distributions of mutual information.
- [[information-theory]] — uses: Capacity is defined via mutual information, a core information-theoretic quantity.
- [[noisy-channel-coding-theorem]] — prerequisite-of: Capacity is the threshold quantity whose existence and value the coding theorem establishes.
[To be populated during integration]

## Optimal input distribution and the extended-channel sketch
The maximizer of $I(X;Y)$ in $C=\max_{P_X}I(X;Y)$ is the **optimal input distribution** $P_X^*$ (it need not be unique). For symmetric channels symmetry forces $P_X^*$ uniform, but for asymmetric channels like the Z channel it is genuinely skewed (e.g. $p_1^*\approx 0.445$), so capacity is a real optimization, not just a noise property.

MacKay's intuitive justification for *why* $C$ is the right number uses the **extended channel** $Q^N$ ($N$ uses at once). A typical input produces roughly $2^{NH(Y\mid X)}$ probable outputs, while the whole typical output set has size $2^{NH(Y)}$. Packing non-overlapping output 'spheres' gives at most
$$\frac{2^{NH(Y)}}{2^{NH(Y\mid X)}} = 2^{NI(X;Y)} \le 2^{NC}$$
non-confusable inputs. For large $N$ the extended channel behaves like a noisy typewriter with a non-confusable sub-alphabet, so up to $C$ bits per use — and no more — can be sent with vanishing error.

## Capacity of continuous channels and the cost constraint
For real-valued channels the capacity $C=\max_{p(x)}I(X;Y)$ must be defined via the **mutual information**, the one information measure with a well-behaved continuous limit (joint/marginal entropies diverge as the discretization granularity shrinks). Because the integrand is a ratio of densities over the same space, $I(X;Y)=\int dx\,dy\,P(x,y)\log\tfrac{P(x,y)}{P(x)P(y)}$ is well defined. An unconstrained real input can carry unbounded information per use, so a **cost function** $v(x)$ (e.g. power $x^2$) is imposed, yielding a capacity-cost function $C(\bar v)$. For the Gaussian channel the maximizing input is Gaussian and $C=\tfrac12\log(1+v/\sigma^2)$.

## Noiseless Constrained Channels
Capacity also has meaning for **noiseless** channels that merely forbid certain strings. Here the mutual-information maximisation is replaced by a counting limit,
$$C=\lim_{N\to\infty}\frac1N\log_2 M_N,$$
with $M_N$ the number of legal length-$N$ strings. Modelling the transmitter as a finite-state machine, $M_N$ grows as $\lambda_1^N$ where $\lambda_1$ is the leading eigenvalue of the connection matrix, so $C=\log_2\lambda_1$. See [[constrained-noiseless-channel]] and [[constrained-channel-capacity-eigenvalue]].

## Analogy: Capacity of a Learning Machine
MacKay applies the channel-capacity lens to *learning*: adapted weights $\mathbf{w}$ act as a channel carrying information about training data $D_N$ to a future user. Constraining the receiver to observe the neuron only at the $N$ training inputs, the relevant 'capacity' is the largest $N$ for which almost any labelling is reproducible. For a $K$-weight linear threshold neuron this is $N=2K$, i.e. **two bits per weight** (a slight departure from the Ch. 9 $\max_{p(x)} I(X;Y)$ definition). See [[capacity-of-a-single-neuron]].