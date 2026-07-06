# PKIS Style Guide

The PKIS front end is **one product, three surfaces**, each with its own aesthetic,
unified by a single red through-line (`#E5484D`). The aesthetic maps to the
*activity*: dark to scan, dark-ruled to read, light to study.

| Surface | Skin | Activity | Token class |
|---|---|---|---|
| Browse / app shell | **Floply** — dark, dense, red | scanning | `.pkis-floply` |
| Node detail (`.sheet`) | **Technical Manuscript** — dark, ruled, mono metadata | focused reading | `.pkis-technical` |
| Explainer | **Hex Notebook** — light, dot-grid | deep study | `.pkis-hex` |

Canonical token values: [`design/tokens.css`](./tokens.css). Live reference (all three
assembled): `pkis.clowderpack.dev/app/composed.html` (source: `design/pkis_composed.html`).

## The red through-line

`#E5484D` is the **interactive / brand** color — focus rings, active states, primary
buttons, links, the explainer's viz highlight. It is loud in Floply (the brand
surface), restrained in the node detail (accent on headings/buttons), and a single
pop in the explainer.

**It does not replace the semantic node-type colors** (`--concept` blue,
`--technique` green, `--result` amber, `--framework` purple, `--problem` red,
`--principle` teal, `--source` slate, `--asset` orchid). Those are *functional* —
they encode node type and stay across all three skins. Red is interaction; type
colors are taxonomy. Never collapse one into the other.

## Surface characters

### Floply (browse / app shell)
- Ground `#111`, surface `#1A1A1A`, elevation by **background step** (`--raised #222`)
  rather than borders. Cards lean on elevation, not outlines.
- Dense: tight leading (~1.4), heavy Inter (600–800) for headings/values.
- Sans throughout (Inter). Reserve `--mono` for genuinely tabular data only.
- Radius `10px`. Red on active chips, focus, primary actions.

### Technical Manuscript (node detail / `.sheet`)
- Ground `#141417` (a hair warmer/darker than Floply) — signals "you've entered one
  thing."
- **Ruled**: section dividers are 1px borders, no shadows. Metadata (IRI,
  `coverage 4/5`, predicate labels) is **monospace** (`IBM Plex Mono`).
- Radius `5px` (tighter than Floply). Medium leading (~1.6) for readability.
- Red accent on section headings, the type chip, connection predicates, the
  "Open explainer" button.

### Hex Notebook (explainer)
- **The only light surface.** Ground `#F7F7F5` with a **dot-grid** texture, surface
  white. Easier on the eyes for long-form study.
- Prominent code blocks (`--code-bg #F3F3F0`, mono). Generous reading leading (~1.65),
  measure ≤ 62ch.
- Red on the viz highlight, links, the active stepper dot.
- **Viz panels may be dark** when the content needs it (canvas instruments like the
  HMC dynamics figures) — a dark "instrument card" embedded in the light page is a
  sanctioned pattern, not a violation.
- **Exception — full-dark instrument explainers.** `hmc.html` is an end-to-end
  canvas instrument whose visualizations rely on a tightly-coupled semantic palette
  (cyan = HMC path, red = random-walk, green/amber for diagnostics). It stays dark
  with its native palette rather than being forced light/red — recoloring would break
  the legend↔canvas correspondence. New explainers should follow Hex-red; reach for a
  full-dark instrument only when the piece is essentially all-simulation like hmc.

## Type
- One family, **Inter**, across all surfaces (weights 400–800). Headings are heavy
  and tight; body is 400.
- **IBM Plex Mono** is the single mono face, used for: IRIs, numeric/tabular data,
  coverage/score readouts, connection predicates, and code.
- No other display faces (the brutalist/terminal experiments are retired).

## Where the tokens live
- **Live viewer:** `viewer/src/index.css` `:root` = the Floply set; `.sheet` scopes
  the Technical set. Everything flows through `var(--…)`, so a token change reskins
  the app.
- **Explainers:** `wiki/assets/viz/*.html` carry the Hex set inline.
- Keep both in sync with `design/tokens.css`. When a token changes, change it in the
  source of truth first, then propagate.

## Authoring a new explainer
1. Start from `wiki/assets/viz/typical-sets.html` (the reference Hex-red explainer).
2. Light ground + dot-grid, Inter body, IBM Plex Mono for data/code, red accent.
3. Keep the asset-node contract: an `asset` node with `viz: <slug>` + `kind`
   (`explainer` → full-screen, `visualization` → inline). See `SCHEMA.md`.
4. SVG/interactive viz: recolor via `var(--accent)` so it stays on-palette. A dark
   canvas instrument panel is fine when the content is dynamics/simulation.
