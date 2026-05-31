import { useEffect, useRef, useState } from 'react'
import type { RelatedEntry } from '../types'
import { getRelated, getFrontier } from '../lib/api'

// Lazy-load Cytoscape to avoid bundling it on initial load
// eslint-disable-next-line @typescript-eslint/no-explicit-any
type CyFactory = (opts: any) => any
let cytoscapeLib: CyFactory | null = null

const TYPE_COLORS: Record<string, string> = {
  concept:   '#4f8ef7',
  technique: '#34c97a',
  result:    '#f5a623',
  framework: '#b06af5',
  problem:   '#e85c5c',
  principle: '#4ecdc4',
  source:    '#a8b3be',
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

  useEffect(() => {
    let cancelled = false

    const initCy = async () => {
      if (!cytoscapeLib) {
        const cyMod = await import('cytoscape')
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        cytoscapeLib = (cyMod.default ?? cyMod) as unknown as CyFactory
      }

      setLoading(true)

      // Load graph data: frontier nodes + their edges
      let elements: { data: Record<string, unknown> }[] = []
      try {
        const frontier = await getFrontier()
        const nodeSet = new Set<string>()

        frontier.slice(0, 30).forEach((n) => {
          if (!nodeSet.has(n.iri)) {
            nodeSet.add(n.iri)
            elements.push({
              data: {
                id: n.iri,
                label: n.canonical_title.split(' ').slice(0, 2).join('\n'),
                color: TYPE_COLORS[n.node_type ?? 'concept'] ?? '#6b7280',
                size: 30 + (n.inbound_refs ?? 0) * 2,
                type: n.node_type ?? 'concept',
              },
            })
          }
        })

        // If we have a focusIri, also load its neighborhood
        if (focusIri) {
          const related = await getRelated(focusIri, { max_hops: 1 })
          related.forEach((r) => {
            if (!nodeSet.has(r.iri)) {
              nodeSet.add(r.iri)
              elements.push({
                data: {
                  id: r.iri,
                  label: r.canonical_title.split(' ').slice(0, 2).join('\n'),
                  color: '#6b7280',
                  size: 26,
                  type: 'concept',
                },
              })
            }
            elements.push({
              data: {
                id: `${focusIri}-${r.iri}`,
                source: r.direction === 'outbound' ? focusIri : r.iri,
                target: r.direction === 'outbound' ? r.iri : focusIri,
                label: r.edge_type,
                edgeType: r.edge_type,
              },
            })
          })
        }
      } catch {
        // fallback — empty graph
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
    }

    initCy()
    return () => { cancelled = true }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [focusIri])

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
      <div ref={containerRef} id="cy" style={{ width: '100%', height: '100%' }} />
    </div>
  )
}
