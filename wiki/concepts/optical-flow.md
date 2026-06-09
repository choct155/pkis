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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- computer-vision
- deep-learning
id: pkis:concept:optical-flow
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch25
tags:
- computer-vision
- motion
- video
- correspondence
- structure-from-motion
title: Optical Flow
understanding: 0
---

## Definition
The apparent motion field of image features induced by relative movement between camera and scene, represented as a vector field (v_x(x,y), v_y(x,y)) of velocities in the image. Optical flow encodes scene structure and motion: distant objects flow slower than near ones, so flow rate cues depth, and the field separates moving foreground from static background. The simplest estimator finds, for a pixel block centered at (x0,y0) at time t, the displacement (Dx,Dy) to time t+Dt that minimizes the sum of squared differences SSD = sum (I(x,y,t) - I(x+Dx,y+Dy,t+Dt))^2, giving flow (Dx/Dt, Dy/Dt). This requires textured windows; on uniform regions SSD is flat and the estimate degenerates (the aperture problem), so robust methods add smoothness and other constraints. For a translating camera with velocity T and focal length 1, flow is v_x = (-T_x + x*T_z)/Z, v_y = (-T_y + y*T_z)/Z; flow vanishes at the focus of expansion (x = T_x/T_z, y = T_y/T_z). There is a scale-factor ambiguity: doubling speed, object size, and distance leaves the flow field unchanged. Optical flow is the moving-camera analogue of stereo disparity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]