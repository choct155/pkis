import { useEffect, useMemo, useState } from 'react'
import type { Asset } from '../types'
import { getAssets } from '../lib/api'

interface Props {
  onSelectNode: (iri: string) => void
  onOpenExplainer: (slug: string, title?: string) => void
  onOpenWriting: (iri: string, title?: string) => void
}

const GLYPH: Record<string, string> = {
  visualization: '◳',
  explainer: '◈',
  'position-paper': '✎',
}

// The Assets gallery: anything the owner authors. Cards route by `format` —
// interactive explainers open full-screen, visualizations open inline, and
// `writing` assets (papers, notes) open the prose reader. The genre filter is
// derived from the assets actually present, so new kinds appear automatically.
export default function ExplainersView({ onSelectNode, onOpenExplainer, onOpenWriting }: Props) {
  const [items, setItems] = useState<Asset[] | null>(null)
  const [err, setErr] = useState<string | null>(null)
  const [kind, setKind] = useState<string>('all')

  useEffect(() => {
    getAssets().then(setItems).catch((e) => setErr(String(e)))
  }, [])

  const kinds = useMemo(() => {
    const ks = Array.from(new Set((items ?? []).map((x) => x.kind))).sort()
    return ['all', ...ks]
  }, [items])

  const shown = useMemo(
    () => (items ?? []).filter((x) => kind === 'all' || x.kind === kind),
    [items, kind],
  )

  if (err) return <div className="empty-state">Couldn’t load assets: {err}</div>

  const openAsset = (x: Asset) => {
    if (x.format === 'writing') onOpenWriting(x.iri, x.viz_title)
    else if (x.kind === 'visualization') onSelectNode(x.iri)
    else onOpenExplainer(x.viz, x.viz_title)
  }

  return (
    <div className="explainers-view">
      <div className="filter-strip">
        {kinds.map((k) => (
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
      ) : shown.length === 0 ? (
        <div className="empty-state">
          No assets yet. An <code>asset</code> is anything you author — an interactive
          explainer/visualization (<code>viz:</code> HTML) or a <code>writing</code>
          piece (markdown body), tagged with a <code>kind</code> from <code>asset_kinds.json</code>.
        </div>
      ) : (
        <div className="explainer-grid">
          {shown.map((x) => (
            <div key={x.iri} className="explainer-card node-card asset" onClick={() => openAsset(x)}>
              <div className="explainer-thumb">
                <span className="explainer-thumb-glyph">{GLYPH[x.kind] ?? (x.format === 'writing' ? '✎' : '◈')}</span>
              </div>
              <div className="explainer-body">
                <div className="explainer-title">{x.viz_title}</div>
                <div className="explainer-backing">
                  <span className="card-type">{x.kind}</span>
                  {x.illustrates > 0 && <span className="explainer-node">illustrates {x.illustrates}</span>}
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
          ))}
        </div>
      )}
    </div>
  )
}
