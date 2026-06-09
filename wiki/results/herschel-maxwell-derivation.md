---
aliases: []
also_type: []
applies:
- gaussian-distribution
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:result:herschel-maxwell-derivation
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch07
tags:
- probability-theory
- invariance
- kinetic-theory
title: Herschel–Maxwell Derivation of the Gaussian
understanding: 0
---

## Definition
A derivation of the Gaussian distribution from two purely geometric invariance postulates, due to John Herschel (1850) for 2-D star-position errors and James Clerk Maxwell (1860) for 3-D molecular velocities. It is notable for using no probability theory beyond geometric invariance, yet uniquely determining the Gaussian form.

## The two postulates
For a joint error density $\rho(x,y)$ in orthogonal directions:
- **(P1) Independence of orthogonal components:** knowledge of $x$ tells nothing about $y$, so $\rho(x,y) = f(x)f(y)$.
- **(P2) Rotational invariance:** in polar form $\rho = g(r,\theta)$ the density is independent of angle, $g(r,\theta)=g(r)$.

## The argument
Equating the two forms gives the functional equation $f(x)f(y) = g(\sqrt{x^2+y^2})$. Taking logarithms, a function of $x$ plus a function of $y$ can equal a function of $x^2+y^2$ only if $\log[f(x)/f(0)] = a x^2$. Normalizability forces $a<0$, giving the unique circularly symmetric Gaussian $\rho(x,y) = (\alpha/\pi)\exp\{-\alpha(x^2+y^2)\}$. Maxwell's 3-D version yields the Maxwellian velocity distribution $\rho(\mathbf v)\propto \exp\{-\alpha(v_x^2+v_y^2+v_z^2)\}$ fundamental to kinetic theory.

## Why it is beautiful
Two qualitative conditions that are incompatible for general distributions become compatible for exactly one quantitative family, which they therefore uniquely determine. Einstein used the same style of argument to deduce the Lorentz transformation from his two relativity postulates. The derivation reveals the Gaussian as a unique object for purely mathematical (geometric-invariance) reasons, independent of any frequency interpretation.

## Connections
- [[gaussian-distribution]] — applies: derives the Gaussian uniquely from geometric invariance
- [[gaussian-distribution]] — the unique distribution satisfying the invariance postulates
- the Maxwellian velocity distribution is its 3-D instance, basis of kinetic theory and statistical mechanics

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]