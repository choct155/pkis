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
contrasts-with:
- deconvolution
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- computer-vision
- deep-learning
id: pkis:concept:image-formation-model
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- edge-detection
- stereo-and-depth
related_concepts: []
sources:
- russell-norvig-aima-ch25
tags:
- computer-vision
- geometry
- optics
- perspective-projection
- lambert
title: Image Formation Model
understanding: 0
---

## Definition
The geometric and photometric account of how a 3D scene gives rise to a 2D image, comprising (1) a geometric projection model and (2) a photometric/reflectance model. The simplest geometry is the pinhole camera: a scene point (X,Y,Z) projects to image coordinates x = -fX/Z, y = -fY/Z (perspective projection), where f is the focal length. The Z in the denominator means distant objects appear smaller and parallel lines converge to a vanishing point P_inf = (fU/W, fV/W) determined only by line direction (U,V,W). When scene depth varies little relative to its distance (DeltaZ << Z0), perspective is approximated by scaled orthographic projection x = sX, y = sY with constant scale s = f/Z0. Real cameras replace the pinhole with a lens system to admit more light while keeping the image focused over a depth of field around the focal plane. Photometrically, pixel brightness follows a reflectance model: diffuse (Lambertian) surfaces obey Lambert's cosine law I = rho * I0 * cos(theta), where rho is the diffuse albedo, I0 the source intensity, and theta the angle between surface normal and light direction; specular surfaces add bright specularities. Trichromacy lets color be modeled with three (RGB) albedos and source intensities. Computer vision is the inverse of this forward (graphics) model: recovering 3D scene structure from images, which is ill-posed and ambiguous, requiring priors and constraints to resolve.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[deconvolution]] — contrasts-with: Recovering scene structure from images is an inverse problem akin to deconvolution; image formation is the forward model.
- [[stereo-and-depth]] — prerequisite-of: Perspective projection geometry is the basis for relating disparity to depth.
- [[edge-detection]] — prerequisite-of: Edges arise from scene effects (depth, normal, reflectance, shadow) modeled by image formation.
[To be populated during integration]