import { useEffect, useState } from 'react'
import type { Explainer } from '../types'
import { getExplainers } from '../lib/api'

interface Props {
  onSelectNode: (iri: string) => void
}

// Gallery of interactive explainers. Each card is backed by a concept/technique
// node (the `viz:` frontmatter binding); tapping opens that node's DetailSheet —
// which renders the live visualization inline — while ↗ opens the explainer
// standalone, full-screen. Makes assets discoverable on their own rather than
// only by knowing which concept they hang off.
export default function ExplainersView({ onSelectNode }: Props) {
  const [items, setItems] = useState<Explainer[] | null>(null)
  const [err, setErr] = useState<string | null>(null)

  useEffect(() => {
    getExplainers()
      .then(setItems)
      .catch((e) => setErr(String(e)))
  }, [])

  if (err) return <div className="empty-state">Couldn’t load explainers: {err}</div>
  if (!items) return <div className="empty-state">Loading…</div>
  if (items.length === 0)
    return (
      <div className="empty-state">
        No explainers yet. Add <code>viz: &lt;slug&gt;</code> to a node’s
        frontmatter to surface its visualization here.
      </div>
    )

  return (
    <div className="explainers-view">
      <div className="view-intro">
        {items.length} interactive explainer{items.length === 1 ? '' : 's'}. Tap a
        card to open the concept with its visualization inline, or ↗ to view the
        explainer full-screen.
      </div>
      <div className="explainer-grid">
        {items.map((x) => (
          <div
            key={x.viz}
            className={`explainer-card node-card ${x.node_type}`}
            onClick={() => onSelectNode(x.iri)}
          >
            <div className="explainer-thumb">
              <span className="explainer-thumb-glyph">◈</span>
            </div>
            <div className="explainer-body">
              <div className="explainer-title">{x.viz_title}</div>
              <div className="explainer-backing">
                <span className="card-type">{x.node_type}</span>
                <span className="explainer-node">{x.node_title}</span>
              </div>
              <div className="card-meta">
                {x.domain.slice(0, 3).map((d) => (
                  <span key={d} className="domain-tag">{d}</span>
                ))}
              </div>
            </div>
            <a
              className="explainer-open"
              href={`/pkis-api/viz/${x.viz}.html`}
              target="_blank"
              rel="noreferrer"
              onClick={(e) => e.stopPropagation()}
              title="Open full-screen"
            >
              ↗
            </a>
          </div>
        ))}
      </div>
    </div>
  )
}
