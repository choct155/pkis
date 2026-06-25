import { useEffect, useState } from 'react'
import type { CompareResponse, QueryLogItem } from '../types'
import { searchCompare, sendFeedback, listQueries } from '../lib/api'

// The four isolation/standing profiles the lab compares. graph_rerank is held
// back until the graph reranker lands (P5) so it isn't an inert duplicate of hybrid.
const PROFILES: { key: string; label: string; color: string }[] = [
  { key: 'lexical_only', label: 'lexical', color: 'var(--concept)' },
  { key: 'dense_only', label: 'dense', color: 'var(--technique)' },
  { key: 'default', label: 'hybrid', color: 'var(--framework)' },
  { key: 'rerank', label: '+rerank', color: 'var(--result)' },
]

const pct = (x?: number) => (x == null ? '—' : `${Math.round(x * 100)}%`)
const ms = (x?: number) => (x == null ? '—' : `${Math.round(x)}ms`)

export default function LabView({ onSelectNode }: { onSelectNode: (iri: string) => void }) {
  const [query, setQuery] = useState('')
  const [selected, setSelected] = useState<Set<string>>(new Set(['default', 'rerank']))
  const [maxResults, setMaxResults] = useState(8)
  const [loading, setLoading] = useState(false)
  const [data, setData] = useState<CompareResponse | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [chosen, setChosen] = useState<string | null>(null)
  const [recent, setRecent] = useState<QueryLogItem[]>([])

  const loadRecent = () => listQueries(30).then(setRecent).catch(() => setRecent([]))
  useEffect(() => { loadRecent() }, [])

  const toggle = (key: string) =>
    setSelected((s) => {
      const next = new Set(s)
      next.has(key) ? next.delete(key) : next.add(key)
      return next
    })

  const run = async (q = query) => {
    const profiles = PROFILES.filter((p) => selected.has(p.key)).map((p) => p.key)
    if (!q.trim() || profiles.length === 0 || loading) return
    setLoading(true); setError(null); setChosen(null)
    try {
      const res = await searchCompare(q.trim(), profiles, { max_results: maxResults })
      setData(res)
      loadRecent()  // this query is now a captured test case
    } catch (e) {
      setError(e instanceof Error ? e.message : 'compare failed')
    } finally {
      setLoading(false)
    }
  }

  const markBest = async (profile: string) => {
    if (!data) return
    setChosen(profile)
    try {
      await sendFeedback({
        query: data.query, comparison_id: data.comparison_id,
        paradigm: 'search', chosen_profile: profile, rating: 'best',
      })
    } catch {
      setError('sign in as owner to record feedback')
      setChosen(null)
    }
  }

  return (
    <div className="lab-view">
      <div className="lab-head">
        <div className="lab-title">retrieval lab</div>
        <div className="lab-sub">compare search regimes · every run becomes a test case · winner held until you mark it</div>
      </div>

      <div className="lab-controls">
        <div className="lab-query-row">
          <input
            className="lab-input"
            placeholder="query to compare…"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && run()}
          />
          <button className="lab-run" disabled={loading || !query.trim() || selected.size === 0} onClick={() => run()}>
            {loading ? '⟳' : 'run'}
          </button>
        </div>
        <div className="lab-chips">
          {PROFILES.map((p) => (
            <button
              key={p.key}
              className={`lab-chip${selected.has(p.key) ? ' on' : ''}`}
              style={selected.has(p.key) ? { borderColor: p.color, color: p.color } : undefined}
              onClick={() => toggle(p.key)}
            >
              {p.label}
            </button>
          ))}
          <span className="lab-spacer" />
          <label className="lab-k">
            top
            <select value={maxResults} onChange={(e) => setMaxResults(Number(e.target.value))}>
              {[5, 8, 10, 15].map((n) => <option key={n} value={n}>{n}</option>)}
            </select>
          </label>
        </div>
      </div>

      {recent.length > 0 && (
        <div className="lab-recent">
          <span className="lab-recent-label">test set</span>
          {recent.map((q) => (
            <button key={q.query_norm} className="lab-recent-chip" onClick={() => { setQuery(q.query); run(q.query) }}>
              {q.query}{q.count > 1 ? ` ·${q.count}` : ''}
            </button>
          ))}
        </div>
      )}

      {error && <div className="lab-error">{error}</div>}

      {data && (
        <div className="lab-cols">
          {data.columns.map((col) => {
            const won = chosen === col.profile_name
            const stages = col.trace?.stages ?? []
            return (
              <div key={col.profile_name} className={`lab-col${won ? ' won' : ''}`}>
                <div className="lab-col-head">
                  <span className="lab-col-name">{col.profile_name}</span>
                  <button className={`lab-best${won ? ' on' : ''}`} onClick={() => markBest(col.profile_name)} title="mark this regime best for this query">
                    {won ? '★ best' : '☆ best'}
                  </button>
                </div>
                <div className="lab-metrics">
                  <div className="lab-metric"><span>coherence</span><b>{pct(col.metrics.coherence)}</b></div>
                  <div className="lab-metric"><span>diversity</span><b>{pct(col.metrics.diversity)}</b></div>
                  <div className="lab-metric"><span>retrieval</span><b>{ms(col.retrieval_ms)}</b></div>
                  <div className="lab-metric"><span>eval</span><b>{ms(col.eval_ms)}</b></div>
                </div>
                <div className="lab-trace">
                  {stages.map((s) => (
                    <span key={s.name} className="lab-stage">{s.name.split(':').pop()} {Math.round(s.ms)}ms</span>
                  ))}
                </div>
                <div className="lab-results">
                  {col.results.length === 0 && <div className="lab-empty">no results</div>}
                  {col.results.map((r, i) => (
                    <button key={r.iri} className="lab-result" onClick={() => onSelectNode(r.iri)}>
                      <span className="lab-rank">{i + 1}</span>
                      <span className="lab-rtitle">{r.canonical_title}</span>
                      <span className={`lab-rtype t-${r.node_type}`}>{r.node_type}</span>
                    </button>
                  ))}
                </div>
              </div>
            )
          })}
        </div>
      )}

      {!data && !loading && !error && (
        <div className="lab-hint">Pick regimes to compare, type a query, and run. Results land side by side with their coherence, diversity, and latency — and every query is logged for the nightly sweep.</div>
      )}
    </div>
  )
}
