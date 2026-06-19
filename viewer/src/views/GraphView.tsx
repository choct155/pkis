import { useEffect, useRef, useState } from 'react'
import type { RelatedEntry } from '../types'
import { getRelated, getClusters } from '../lib/api'

// Lazy-load Cytoscape to avoid bundling it on initial load
// eslint-disable-next-line @typescript-eslint/no-explicit-any
type CyFactory = (opts: any) => any
let cytoscapeLib: CyFactory | null = null

const TYPE_COLORS: Record<string, string> = {
  concept:        '#4f8ef7',
  technique:      '#34c97a',
  result:         '#f5a623',
  framework:      '#b06af5',
  problem:        '#e85c5c',
  principle:      '#4ecdc4',
  source:         '#a8b3be',
  'research-cluster': '#eef0f2',
  hypothesis:     '#e8c15c',
}

function typeFromIri(iri: string): string {
  const p = iri.split(':')
  return p.length >= 2 ? p[1] : 'concept'
}
function shortLabel(t: string): string {
  return t.split(' ').slice(0, 2).join('\n')
}

const EDGE_PREDICATES = [
  'all', 'uses', 'generalizes', 'contrasts-with',
  'prerequisite-of', 'grounds', 'extends',
]

const CY_STYLE = [
  {
    selector: 'node',
    style: {
      'background-color': 'data(color)',
      'background-opacity': 0.15,
      'border-width': 1.5,
      'border-color': 'data(color)',
      'label': 'data(label)',
      'color': '#d4d8dd',
      'font-size': '9px',
      'font-family': "'IBM Plex Mono', monospace",
      'text-valign': 'center',
      'text-halign': 'center',
      'text-wrap': 'wrap',
      'text-max-width': '50px',
      'width': 'data(size)',
      'height': 'data(size)',
    },
  },
  {
    selector: 'node:selected',
    style: {
      'background-opacity': 0.3,
      'border-width': 2.5,
    },
  },
  {
    selector: 'node.focus',
    style: {
      'background-opacity': 0.25,
      'border-width': 2.5,
      'width': 44,
      'height': 44,
    },
  },
  {
    selector: 'edge',
    style: {
      'line-color': '#3a3f45',
      'target-arrow-color': '#3a3f45',
      'target-arrow-shape': 'triangle',
      'curve-style': 'bezier',
      'width': 1,
      'opacity': 0.6,
      'label': 'data(label)',
      'font-size': '7px',
      'color': '#6b7280',
      'font-family': "'IBM Plex Mono', monospace",
      'text-rotation': 'autorotate',
    },
  },
]

interface Props {
  focusIri: string | null
  onSelectNode: (iri: string) => void
}

export default function GraphView({ focusIri, onSelectNode }: Props) {
  const containerRef = useRef<HTMLDivElement>(null)
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const cyRef = useRef<any>(null)
  const [edgeFilter, setEdgeFilter] = useState('all')
  const [loading, setLoading] = useState(true)
  const [loadError, setLoadError] = useState(false)

  useEffect(() => {
    let cancelled = false

    const initCy = async () => {
      if (!cytoscapeLib) {
        const cyMod = await import('cytoscape')
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        cytoscapeLib = (cyMod.default ?? cyMod) as unknown as CyFactory
      }

      setLoading(true); setLoadError(false)

      const elements: { data: Record<string, unknown> }[] = []
      const nodeSet = new Set<string>()
      const addNode = (id: string, label: string, color: string, size: number, type: string) => {
        if (nodeSet.has(id)) return
        nodeSet.add(id)
        elements.push({ data: { id, label, color, size, type } })
      }
      try {
        if (focusIri) {
          // Ego-network: the focused node + its 1-hop neighbourhood.
          const ft = typeFromIri(focusIri)
          addNode(focusIri, shortLabel(focusIri.split(':').pop() ?? focusIri),
                  TYPE_COLORS[ft] ?? '#6b7280', 44, ft)
          const related = await getRelated(focusIri, { max_hops: 1 })
          related.forEach((r: RelatedEntry) => {
            const rt = typeFromIri(r.iri)
            addNode(r.iri, shortLabel(r.canonical_title), TYPE_COLORS[rt] ?? '#6b7280', 28, rt)
            elements.push({ data: {
              id: `${focusIri}-${r.iri}`,
              source: r.direction === 'outbound' ? focusIri : r.iri,
              target: r.direction === 'outbound' ? r.iri : focusIri,
              label: r.edge_type, edgeType: r.edge_type,
            } })
          })
        } else {
          // Default: the research-program graph — clusters → frontier hypotheses + concept deps.
          const clusters = await getClusters()
          clusters.forEach((c) => {
            addNode(c.iri, shortLabel(c.title), TYPE_COLORS['research-cluster'], 40, 'research-cluster')
            c.hypotheses.filter((h) => h.iri && h.is_frontier).forEach((h) => {
              addNode(h.iri!, shortLabel(h.title), TYPE_COLORS.hypothesis, 26, 'hypothesis')
              elements.push({ data: { id: `${c.iri}-${h.iri}`, source: c.iri, target: h.iri, label: 'tests', edgeType: 'tests' } })
            })
            c.deps.forEach((d) => {
              addNode(d.iri, shortLabel(d.title), TYPE_COLORS[d.type] ?? '#6b7280', 26, d.type)
              elements.push({ data: { id: `${c.iri}-${d.iri}`, source: c.iri, target: d.iri, label: d.predicate, edgeType: d.predicate } })
            })
          })
        }
      } catch {
        if (!cancelled) setLoadError(true)
      }

      if (cancelled || !containerRef.current) return

      // Destroy existing instance
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      if (cyRef.current) (cyRef.current as any).destroy()

      const cy = cytoscapeLib!({
        container: containerRef.current,
        elements,
        style: CY_STYLE,
        layout: { name: 'cose', padding: 20, animate: false },
        userZoomingEnabled: true,
        userPanningEnabled: true,
        minZoom: 0.3,
        maxZoom: 3,
      })

      if (focusIri) cy.getElementById(focusIri)?.addClass('focus')

      cy.on('tap', 'node', (e: { target: { id: () => string } }) => {
        onSelectNode(e.target.id())
      })

      cyRef.current = cy
      setLoading(false)

      // The container can have zero dimensions at mount (esp. on mobile / when the
      // tab was hidden), leaving Cytoscape's canvas blank. Re-measure and refit once
      // layout settles, and again shortly after as a fallback.
      const refit = () => {
        try { cy.resize(); cy.fit(undefined, 30) } catch { /* noop */ }
      }
      requestAnimationFrame(refit)
      setTimeout(refit, 250)
    }

    initCy()
    return () => { cancelled = true }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [focusIri])

  // Keep the canvas sized to its container (orientation change, viewport resize,
  // late layout). Without this the graph renders empty when dims were 0 at mount.
  useEffect(() => {
    const el = containerRef.current
    if (!el || typeof ResizeObserver === 'undefined') return
    const ro = new ResizeObserver(() => {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      const cy = cyRef.current as any
      if (!cy) return
      try { cy.resize(); cy.fit(undefined, 30) } catch { /* noop */ }
    })
    ro.observe(el)
    return () => ro.disconnect()
  }, [])

  // Apply edge filter
  useEffect(() => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const cy = cyRef.current as any
    if (!cy) return
    if (edgeFilter === 'all') {
      cy.edges().show()
    } else {
      cy.edges().show()
      cy.edges(`[edgeType != "${edgeFilter}"]`).hide()
    }
  }, [edgeFilter])

  return (
    <div className="graph-view-wrap">
      <div className="graph-edge-filter">
        {EDGE_PREDICATES.map((p) => (
          <div
            key={p}
            className={`edge-chip${edgeFilter === p ? ' active' : ''}`}
            onClick={() => setEdgeFilter(p)}
          >
            {p}
          </div>
        ))}
      </div>
      {loading && (
        <div
          style={{
            position: 'absolute', inset: 0, display: 'flex',
            alignItems: 'center', justifyContent: 'center', zIndex: 5,
          }}
        >
          <div className="loading-row">
            <div className="loading-spinner" /> building graph…
          </div>
        </div>
      )}
      {!loading && loadError && (
        <div style={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center',
                      justifyContent: 'center', zIndex: 5 }}>
          <div className="empty-state">couldn’t load the graph — pull to refresh</div>
        </div>
      )}
      <div ref={containerRef} id="cy" style={{ width: '100%', height: '100%' }} />
    </div>
  )
}
