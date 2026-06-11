import { useEffect, useState } from 'react'
import type { Asset } from '../types'
import { getAssets } from '../lib/api'

interface Props {
  onSelectNode: (iri: string) => void
  onOpenExplainer: (slug: string, title?: string) => void
}

type KindFilter = 'all' | 'explainer' | 'visualization'
const KINDS: KindFilter[] = ['all', 'explainer', 'visualization']

// Gallery of assets (interactive explainers + self-contained visualizations).
// explainer cards open the full-screen overlay; visualization cards open the
// asset node (which renders the widget inline). `illustrates N` shows reach.
export default function ExplainersView({ onSelectNode, onOpenExplainer }: Props) {
  const [items, setItems] = useState<Asset[] | null>(null)
  const [err, setErr] = useState<string | null>(null)
  const [kind, setKind] = useState<KindFilter>('all')

  useEffect(() => {
    setItems(null)
    getAssets(kind === 'all' ? undefined : kind)
      .then(setItems)
      .catch((e) => setErr(String(e)))
  }, [kind])

  if (err) return <div className="empty-state">Couldn’t load assets: {err}</div>

  return (
    <div className="explainers-view">
      <div className="filter-strip">
        {KINDS.map((k) => (
          <div
            key={k}
            className={`filter-chip chip-all${kind === k ? '' : ' inactive'}`}
            onClick={() => setKind(k)}
          >
            {k}
          </div>
        ))}
      </div>

      {!items ? (
        <div className="empty-state">Loading…</div>
      ) : items.length === 0 ? (
        <div className="empty-state">
          No assets yet. Create an <code>asset</code> node with a <code>viz:</code> slug
          and link it from nodes via <code>illustrated-by</code>.
        </div>
      ) : (
        <div className="explainer-grid">
          {items.map((x) => {
            const open = () =>
              x.kind === 'visualization' ? onSelectNode(x.iri) : onOpenExplainer(x.viz, x.viz_title)
            return (
              <div key={x.iri} className="explainer-card node-card asset" onClick={open}>
                <div className="explainer-thumb">
                  <span className="explainer-thumb-glyph">{x.kind === 'visualization' ? '◳' : '◈'}</span>
                </div>
                <div className="explainer-body">
                  <div className="explainer-title">{x.viz_title}</div>
                  <div className="explainer-backing">
                    <span className="card-type">{x.kind}</span>
                    <span className="explainer-node">illustrates {x.illustrates}</span>
                  </div>
                  <div className="card-meta">
                    {x.domain.slice(0, 3).map((d) => (
                      <span key={d} className="domain-tag">{d}</span>
                    ))}
                  </div>
                </div>
                {x.viz_url && (
                  <a
                    className="explainer-open"
                    href={x.viz_url}
                    target="_blank"
                    rel="noreferrer"
                    onClick={(e) => e.stopPropagation()}
                    title="Open in new tab"
                  >
                    ↗
                  </a>
                )}
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}
