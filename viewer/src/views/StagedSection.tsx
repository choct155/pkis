import { useEffect, useState } from 'react'
import type { StagedNode, StagedLink, SearchResult } from '../types'
import { getStagedNodes, commitStaged, searchWiki, ApiError } from '../lib/api'

// The "staged" lane of the consolidated inbox: bridge notes + stubs awaiting
// review, with the FULL context the old Staged tab dropped — the rationale (why
// it exists), the nodes it connects (each resolved exists/missing), and the
// proposed edge — reviewed INLINE (never opening a not-yet-committed graph node).
// Missing links get a resolution picker that feeds confirmed_links to commit.

function relTime(iso: string): string {
  if (!iso) return ''
  const d = (Date.now() - new Date(iso).getTime()) / 1000
  if (d < 3600) return `${Math.max(1, Math.floor(d / 60))}m ago`
  if (d < 86400) return `${Math.floor(d / 3600)}h ago`
  return `${Math.floor(d / 86400)}d ago`
}

// One missing ref → search candidates → user picks the canonical node (or leaves
// it unlinked). Reports the chosen IRI (or null) up to the card.
function ResolveRow({ refName, onPick }: { refName: string; onPick: (iri: string | null) => void }) {
  const [cands, setCands] = useState<SearchResult[]>([])
  const [picked, setPicked] = useState<string | null | undefined>(undefined)
  useEffect(() => { searchWiki(refName, { max_results: 5 }).then(setCands).catch(() => {}) }, [refName])
  const choose = (iri: string | null) => { setPicked(iri); onPick(iri) }
  return (
    <div className="resolve-row">
      <div className="resolve-ref">⚠ {refName}</div>
      <div className="resolve-cands">
        {cands.map((c) => (
          <button key={c.iri} className={`resolve-cand${picked === c.iri ? ' on' : ''}`}
            onClick={() => choose(c.iri)}>{c.canonical_title}</button>
        ))}
        <button className={`resolve-cand unlink${picked === null ? ' on' : ''}`}
          onClick={() => choose(null)}>leave unlinked</button>
      </div>
    </div>
  )
}

function StagedCard({ n, onSelectNode, onActed, onToast }: {
  n: StagedNode
  onSelectNode: (iri: string) => void
  onActed: () => void
  onToast: (m: string) => void
}) {
  const [busy, setBusy] = useState(false)
  const [resolving, setResolving] = useState(false)
  const [confirmed, setConfirmed] = useState<Record<string, string>>({})
  const links: StagedLink[] = n.links ?? []
  const missing = links.filter((l) => !l.exists)

  const commit = async (action: 'accept' | 'discard', confirmedLinks?: Record<string, string>) => {
    setBusy(true)
    try {
      await commitStaged(n.staged_id, action, undefined, confirmedLinks)
      onToast(action === 'accept' ? 'committed to the graph' : 'discarded')
      onActed()
    } catch (e) {
      onToast(e instanceof ApiError && e.status === 401 ? 'sign in to review'
        : e instanceof ApiError && e.status === 403 ? 'write access required' : 'action failed')
    } finally {
      setBusy(false); setResolving(false)
    }
  }

  const onAccept = () => {
    if (missing.length === 0) commit('accept')
    else setResolving(true)   // resolve missing links before committing
  }

  return (
    <div className="staged-card">
      <div className="staged-card-head">
        <span className={`type-badge badge-${n.node_type}`}>{n.node_type}</span>
        <span className="staged-card-title">{n.title}</span>
      </div>
      <div className="staged-card-meta">{n.staged_by} · {relTime(n.staged_at)}</div>

      {n.rationale && <div className="staged-rationale">{n.rationale}</div>}

      {links.length > 0 && (
        <div className="staged-links">
          <span className="staged-links-label">connects</span>
          {links.map((l) => (
            l.exists
              ? <button key={l.ref} className="staged-link ok" title={l.iri || ''}
                  onClick={() => l.iri && onSelectNode(l.iri)}>✓ {l.ref}</button>
              : <span key={l.ref} className="staged-link missing">⚠ {l.ref}</span>
          ))}
          <span className="staged-edge">— {n.proposed_edge_type} →</span>
        </div>
      )}

      {resolving ? (
        <div className="staged-resolve">
          <div className="staged-resolve-head">
            {missing.length} link{missing.length > 1 ? 's' : ''} not in the graph — pick the right node, or leave unlinked:
          </div>
          {missing.map((l) => (
            <ResolveRow key={l.ref} refName={l.ref}
              onPick={(iri) => setConfirmed((p) => {
                const next = { ...p }
                if (iri) next[l.ref] = iri; else delete next[l.ref]
                return next
              })} />
          ))}
          <div className="staged-actions">
            <button className="action-btn primary" disabled={busy} onClick={() => commit('accept', confirmed)}>
              ✓ commit{Object.keys(confirmed).length ? ` (${Object.keys(confirmed).length} resolved)` : ''}
            </button>
            <button className="action-btn" disabled={busy} onClick={() => setResolving(false)}>cancel</button>
          </div>
        </div>
      ) : (
        <div className="staged-actions">
          <button className="action-btn primary" disabled={busy} onClick={onAccept}>
            ✓ accept{missing.length ? ` · ${missing.length} to resolve` : ''}
          </button>
          <button className="action-btn" disabled={busy}
            onClick={() => { if (window.confirm('Discard this staged item?')) commit('discard') }}>✕ discard</button>
          <a className="action-btn" href={n.review_url} target="_blank" rel="noreferrer">↗ source</a>
        </div>
      )}
    </div>
  )
}

export default function StagedSection({ onSelectNode, onToast }: {
  onSelectNode: (iri: string) => void
  onToast: (m: string) => void
}) {
  const [items, setItems] = useState<StagedNode[] | null>(null)
  const load = () => getStagedNodes({ limit: 200 }).then(setItems).catch(() => setItems([]))
  useEffect(() => { load() }, [])

  if (!items) return null
  if (items.length === 0) return null   // hide the lane entirely when empty

  return (
    <div className="inbox-section">
      <div className="inbox-section-head">
        <span className="inbox-section-title">Staged</span>
        <span className="inbox-section-count">{items.length}</span>
      </div>
      {items.map((n) => (
        <StagedCard key={n.staged_id} n={n} onSelectNode={onSelectNode}
          onActed={load} onToast={onToast} />
      ))}
    </div>
  )
}
