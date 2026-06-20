import { useEffect, useState } from 'react'
import { getHealth, getFrontier, getReadingQueue, getStagedNodes, getIndex } from '../lib/api'
import type {
  HealthMetrics, FrontierNode, QueueItem, NodeType, View, StagedNode, IndexNode, SearchResult,
} from '../types'
import NodeCard from '../components/NodeCard'

interface Props {
  typeFilter: NodeType | 'all'
  domainFilter: string
  clusterFilter: string
  onSelectNode: (iri: string) => void
  onNavigate: (v: View) => void
  isOwner: boolean
}

const TYPE_ORDER = ['concept', 'technique', 'result', 'framework', 'problem',
  'principle', 'hypothesis', 'research-cluster', 'source', 'asset']

function asCard(n: IndexNode): SearchResult {
  return {
    iri: n.iri, canonical_title: n.canonical_title, domain: n.domain,
    node_type: n.node_type, coverage: n.coverage, understanding: n.understanding,
    one_line_summary: '',
  }
}

export default function BrowseView({ typeFilter, domainFilter, clusterFilter, onSelectNode, onNavigate, isOwner }: Props) {
  const [health, setHealth]   = useState<HealthMetrics | null>(null)
  const [frontier, setFrontier] = useState<FrontierNode[]>([])
  const [queue, setQueue]     = useState<QueueItem[]>([])
  const [stagedCount, setStagedCount] = useState(0)
  const [loadingMain, setLoadingMain] = useState(true)
  const [loadErr, setLoadErr] = useState(false)
  const [indexNodes, setIndexNodes] = useState<IndexNode[]>([])
  const [loadingIndex, setLoadingIndex] = useState(false)

  const faceted = typeFilter !== 'all' || domainFilter !== 'all' || clusterFilter !== 'all'

  useEffect(() => {
    let cancelled = false
    setLoadingMain(true)
    Promise.all([getHealth(), getFrontier(), getReadingQueue(), getStagedNodes({ limit: 500 })])
      .then(([h, f, q, s]: [HealthMetrics, FrontierNode[], QueueItem[], StagedNode[]]) => {
        if (cancelled) return
        setHealth(h); setFrontier(f); setQueue(q); setStagedCount(s.length)
        setLoadingMain(false)
      })
      .catch(() => { if (!cancelled) { setLoadErr(true); setLoadingMain(false) } })
    return () => { cancelled = true }
  }, [])

  // Faceted browse: all nodes matching the active type, domain, and/or cluster.
  useEffect(() => {
    if (!faceted) { setIndexNodes([]); return }
    let cancelled = false
    setLoadingIndex(true)
    getIndex(
      typeFilter === 'all' ? undefined : typeFilter,
      domainFilter === 'all' ? undefined : domainFilter,
      clusterFilter === 'all' ? undefined : clusterFilter,
    )
      .then((nodes) => { if (!cancelled) { setIndexNodes(nodes); setLoadingIndex(false) } })
      .catch(() => { if (!cancelled) setLoadingIndex(false) })
    return () => { cancelled = true }
  }, [typeFilter, domainFilter, clusterFilter, faceted])

  // ── Faceted mode ────────────────────────────────────────────────────────
  if (faceted) {
    const label = [
      clusterFilter !== 'all' ? clusterFilter : null,
      domainFilter !== 'all' ? domainFilter : null,
      typeFilter !== 'all' ? typeFilter : null,
    ].filter(Boolean).join(' / ') || 'all'

    // Group by type when a domain/cluster is selected with no specific type chosen.
    const groupByType = (domainFilter !== 'all' || clusterFilter !== 'all') && typeFilter === 'all'
    const groups: [string, IndexNode[]][] = groupByType
      ? TYPE_ORDER
          .map((t) => [t, indexNodes.filter((n) => n.node_type === t)] as [string, IndexNode[]])
          .filter(([, ns]) => ns.length > 0)
      : [['', indexNodes]]

    return (
      <div>
        <div className="section-label">{label} · {loadingIndex ? '…' : indexNodes.length}</div>
        {loadingIndex ? (
          <div className="loading-row"><div className="loading-spinner" /> loading…</div>
        ) : indexNodes.length === 0 ? (
          <div className="empty-state">no matching nodes</div>
        ) : (
          groups.map(([type, ns]) => (
            <div key={type || 'flat'}>
              {type && <div className="group-label">{type} · {ns.length}</div>}
              {ns.map((n) => <NodeCard key={n.iri} node={asCard(n)} onClick={onSelectNode} />)}
            </div>
          ))
        )}
      </div>
    )
  }

  // ── Default (home) mode: frontier + queue ───────────────────────────────
  // B10: the backend already orders the queue by frontier priority_score, so just
  // take the top of the returned order (no manual high/normal re-sort).
  const prioritizedQueue = queue.slice(0, 5)

  return (
    <div>
      {isOwner && stagedCount > 0 && (
        <div className="staged-badge" onClick={() => onNavigate('inbox')}>
          <div className="staged-dot" />
          {stagedCount} item{stagedCount > 1 ? 's' : ''} to review — open inbox
        </div>
      )}

      {loadingMain ? (
        <div className="loading-row"><div className="loading-spinner" /> loading stats…</div>
      ) : loadErr ? (
        <div className="empty-state">couldn’t reach the server — pull to refresh</div>
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

      <div className="browse-hint">tap a type or domain chip above to browse all matching nodes</div>

      {prioritizedQueue.length > 0 && (
        <>
          <div className="section-label">reading queue</div>
          {prioritizedQueue.map((item, i) => (
            <div key={i} className="queue-item" onClick={() => onNavigate('priority')}>
              <div className={`queue-priority prio-${item.hint ?? 'normal'}`} />
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
