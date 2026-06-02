import { useEffect, useState } from 'react'
import { getHealth, getFrontier, getReadingQueue, getStagedNodes, getIndex } from '../lib/api'
import type {
  HealthMetrics, FrontierNode, QueueItem, NodeType, View, StagedNode, IndexNode, SearchResult,
} from '../types'
import NodeCard from '../components/NodeCard'

interface Props {
  typeFilter: NodeType | 'all'
  onSelectNode: (iri: string) => void
  onNavigate: (v: View) => void
}

// Adapt an IndexNode to the SearchResult shape NodeCard renders.
function asCard(n: IndexNode): SearchResult {
  return {
    iri: n.iri,
    canonical_title: n.canonical_title,
    domain: n.domain,
    node_type: n.node_type,
    coverage: n.coverage,
    understanding: n.understanding,
    one_line_summary: '',
  }
}

export default function BrowseView({ typeFilter, onSelectNode, onNavigate }: Props) {
  const [health, setHealth]   = useState<HealthMetrics | null>(null)
  const [frontier, setFrontier] = useState<FrontierNode[]>([])
  const [queue, setQueue]     = useState<QueueItem[]>([])
  const [stagedCount, setStagedCount] = useState(0)
  const [loadingMain, setLoadingMain] = useState(true)
  const [indexNodes, setIndexNodes] = useState<IndexNode[]>([])
  const [loadingIndex, setLoadingIndex] = useState(false)

  useEffect(() => {
    let cancelled = false
    setLoadingMain(true)
    Promise.all([getHealth(), getFrontier(), getReadingQueue(), getStagedNodes({ limit: 500 })])
      .then(([h, f, q, s]: [HealthMetrics, FrontierNode[], QueueItem[], StagedNode[]]) => {
        if (cancelled) return
        setHealth(h); setFrontier(f); setQueue(q); setStagedCount(s.length)
        setLoadingMain(false)
      })
      .catch(() => { if (!cancelled) setLoadingMain(false) })
    return () => { cancelled = true }
  }, [])

  // When a type filter is active, browse ALL nodes of that type (not just the frontier).
  useEffect(() => {
    if (typeFilter === 'all') { setIndexNodes([]); return }
    let cancelled = false
    setLoadingIndex(true)
    getIndex(typeFilter)
      .then((nodes) => { if (!cancelled) { setIndexNodes(nodes); setLoadingIndex(false) } })
      .catch(() => { if (!cancelled) setLoadingIndex(false) })
    return () => { cancelled = true }
  }, [typeFilter])

  // ── Filtered (browse-all) mode ──────────────────────────────────────────
  if (typeFilter !== 'all') {
    return (
      <div>
        <div className="section-label">
          {typeFilter} · {loadingIndex ? '…' : indexNodes.length}
        </div>
        {loadingIndex ? (
          <div className="loading-row"><div className="loading-spinner" /> loading {typeFilter}s…</div>
        ) : indexNodes.length === 0 ? (
          <div className="empty-state">no {typeFilter} nodes</div>
        ) : (
          indexNodes.map((n) => <NodeCard key={n.iri} node={asCard(n)} onClick={onSelectNode} />)
        )}
      </div>
    )
  }

  // ── Default (all) mode: frontier + queue ────────────────────────────────
  const prioritizedQueue = [...queue].sort((a, b) =>
    a.priority === 'high' && b.priority !== 'high' ? -1 :
    b.priority === 'high' && a.priority !== 'high' ? 1 : 0
  ).slice(0, 5)

  return (
    <div>
      {stagedCount > 0 && (
        <div className="staged-badge" onClick={() => onNavigate('staged')}>
          <div className="staged-dot" />
          {stagedCount} staged node{stagedCount > 1 ? 's' : ''} awaiting review
        </div>
      )}

      {loadingMain ? (
        <div className="loading-row"><div className="loading-spinner" /> loading stats…</div>
      ) : health && (
        <div className="stats-row">
          <div className="stat-card"><span className="stat-value">{health.total_nodes}</span><span className="stat-label">nodes</span></div>
          <div className="stat-card"><span className="stat-value">{health.total_sources}</span><span className="stat-label">sources</span></div>
          <div className="stat-card"><span className="stat-value">{health.queue_depth}</span><span className="stat-label">queue</span></div>
        </div>
      )}

      <div className="section-label">frontier — needs attention</div>
      {frontier.length === 0 ? (
        <div className="empty-state">nothing on the frontier</div>
      ) : (
        frontier.slice(0, 8).map((n) => <NodeCard key={n.iri} node={n} onClick={onSelectNode} />)
      )}

      <div className="browse-hint">tap a type chip above to browse all nodes of that type</div>

      {prioritizedQueue.length > 0 && (
        <>
          <div className="section-label">reading queue</div>
          {prioritizedQueue.map((item, i) => (
            <div key={i} className="queue-item" onClick={() => onNavigate('priority')}>
              <div className={`queue-priority prio-${item.priority}`} />
              <div className="queue-info">
                <div className="queue-title">{item.slug}</div>
                {item.reason && <div className="queue-reason">{item.reason}</div>}
              </div>
              <div className="queue-action">read →</div>
            </div>
          ))}
        </>
      )}
    </div>
  )
}
