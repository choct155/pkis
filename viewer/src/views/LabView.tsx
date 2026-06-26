import { useEffect, useState } from 'react'
import type { CompareResponse, AskCompareResponse, QueryLogItem, PathResponse } from '../types'
import { searchCompare, askCompare, sendFeedback, listQueries, pathBetween } from '../lib/api'

// The isolation/standing profiles the lab compares.
const PROFILES: { key: string; label: string; color: string }[] = [
  { key: 'lexical_only', label: 'lexical', color: 'var(--concept)' },
  { key: 'dense_only', label: 'dense', color: 'var(--technique)' },
  { key: 'default', label: 'hybrid', color: 'var(--framework)' },
  { key: 'rerank', label: '+rerank', color: 'var(--result)' },
  { key: 'graph_rerank', label: '+graph', color: 'var(--principle)' },
]
const ASK_CAP = 3  // answer mode fires one LLM call per profile

const pct = (x?: number | null) => (x == null ? '—' : `${Math.round(x * 100)}%`)
const ms = (x?: number) => (x == null ? '—' : `${Math.round(x)}ms`)
const usd = (x?: number | null) => (x == null ? '—' : `$${x.toFixed(4)}`)

type Mode = 'retrieve' | 'answer' | 'path'

export default function LabView({ onSelectNode }: { onSelectNode: (iri: string) => void }) {
  const [query, setQuery] = useState('')
  const [queryB, setQueryB] = useState('')        // path mode: the second endpoint
  const [mode, setMode] = useState<Mode>('retrieve')
  const [selected, setSelected] = useState<Set<string>>(new Set(['default', 'rerank']))
  const [maxResults, setMaxResults] = useState(8)
  const [deep, setDeep] = useState(false)         // C(q) deep metrics (one LLM call)
  const [loading, setLoading] = useState(false)
  const [data, setData] = useState<CompareResponse | null>(null)
  const [askData, setAskData] = useState<AskCompareResponse | null>(null)
  const [pathData, setPathData] = useState<PathResponse | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [chosen, setChosen] = useState<string | null>(null)
  const [recent, setRecent] = useState<QueryLogItem[]>([])

  const loadRecent = () => listQueries(30).then(setRecent).catch(() => setRecent([]))
  useEffect(() => { loadRecent() }, [])

  const profileList = PROFILES.filter((p) => selected.has(p.key)).map((p) => p.key)
  const tooMany = mode === 'answer' && profileList.length > ASK_CAP

  const toggle = (key: string) =>
    setSelected((s) => {
      const next = new Set(s)
      next.has(key) ? next.delete(key) : next.add(key)
      return next
    })

  const clearResults = () => { setData(null); setAskData(null); setPathData(null); setChosen(null) }

  const run = async (q = query) => {
    if (loading) return
    if (mode === 'path') {
      if (!q.trim() || !queryB.trim()) return
      setLoading(true); setError(null); clearResults()
      try { setPathData(await pathBetween(q.trim(), queryB.trim())) }
      catch (e) { setError(e instanceof Error ? e.message : 'path failed') }
      finally { setLoading(false) }
      return
    }
    if (!q.trim() || profileList.length === 0) return
    setLoading(true); setError(null); clearResults()
    try {
      if (mode === 'answer') {
        setAskData(await askCompare(q.trim(), profileList.slice(0, ASK_CAP)))
      } else {
        setData(await searchCompare(q.trim(), profileList, { max_results: maxResults, deep }))
      }
      loadRecent()
    } catch (e) {
      setError(e instanceof Error ? e.message : 'run failed')
    } finally {
      setLoading(false)
    }
  }

  const markBest = async (profile: string) => {
    const cid = mode === 'answer' ? askData?.comparison_id : data?.comparison_id
    const q = mode === 'answer' ? askData?.query : data?.query
    if (!cid) return
    setChosen(profile)
    try {
      await sendFeedback({ query: q, comparison_id: cid, paradigm: mode === 'answer' ? 'ask' : 'search', chosen_profile: profile, rating: 'best' })
    } catch {
      setError('sign in as owner to record feedback'); setChosen(null)
    }
  }

  return (
    <div className="lab-view">
      <div className="lab-head">
        <div className="lab-title">retrieval lab</div>
        <div className="lab-sub">compare regimes · every run becomes a test case · winner held until you mark it</div>
      </div>

      <div className="lab-controls">
        <div className="lab-mode">
          {(['retrieve', 'answer', 'path'] as Mode[]).map((m) => (
            <button key={m} className={`lab-mode-btn${mode === m ? ' on' : ''}`} onClick={() => { setMode(m); clearResults() }}>
              {m}
            </button>
          ))}
          {mode === 'answer' && <span className="lab-mode-note">one LLM call per regime · max {ASK_CAP}</span>}
          {mode === 'path' && <span className="lab-mode-note">how do two nodes connect?</span>}
        </div>
        <div className="lab-query-row">
          <input
            className="lab-input"
            placeholder={mode === 'answer' ? 'question to answer…' : mode === 'path' ? 'from node…' : 'query to compare…'}
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && run()}
          />
          {mode === 'path' && (
            <input
              className="lab-input"
              placeholder="to node…"
              value={queryB}
              onChange={(e) => setQueryB(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && run()}
            />
          )}
          <button className="lab-run" disabled={loading || !query.trim() || (mode === 'path' ? !queryB.trim() : profileList.length === 0 || tooMany)} onClick={() => run()}>
            {loading ? '⟳' : 'run'}
          </button>
        </div>
        {mode !== 'path' && (
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
            {mode === 'retrieve' && (
              <>
                <span className="lab-spacer" />
                <label className="lab-deep" title="estimate the query's concept set C(q) via one LLM call, then score coverage / concision / structural relevance">
                  <input type="checkbox" checked={deep} onChange={(e) => setDeep(e.target.checked)} />
                  deep
                </label>
                <label className="lab-k">
                  top
                  <select value={maxResults} onChange={(e) => setMaxResults(Number(e.target.value))}>
                    {[5, 8, 10, 15].map((n) => <option key={n} value={n}>{n}</option>)}
                  </select>
                </label>
              </>
            )}
          </div>
        )}
        {tooMany && <div className="lab-error">answer mode compares at most {ASK_CAP} regimes — deselect some.</div>}
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
      {loading && mode === 'answer' && <div className="lab-hint">answering under {profileList.slice(0, ASK_CAP).length} regimes — this runs the model once each…</div>}

      {/* retrieve columns */}
      {data && (
        <div className="lab-cols">
          {data.columns.map((col) => {
            const won = chosen === col.profile_name
            return (
              <div key={col.profile_name} className={`lab-col${won ? ' won' : ''}`}>
                <div className="lab-col-head">
                  <span className="lab-col-name">{col.profile_name}</span>
                  <button className={`lab-best${won ? ' on' : ''}`} onClick={() => markBest(col.profile_name)}>{won ? '★ best' : '☆ best'}</button>
                </div>
                <div className="lab-metrics">
                  <div className="lab-metric"><span>coherence</span><b>{pct(col.metrics.coherence)}</b></div>
                  <div className="lab-metric"><span>diversity</span><b>{pct(col.metrics.diversity)}</b></div>
                  <div className="lab-metric"><span>retrieval</span><b>{ms(col.retrieval_ms)}</b></div>
                  <div className="lab-metric"><span>eval</span><b>{ms(col.eval_ms)}</b></div>
                  {col.metrics.coverage != null && <>
                    <div className="lab-metric deep"><span>coverage</span><b>{pct(col.metrics.coverage)}</b></div>
                    <div className="lab-metric deep"><span>relevance</span><b>{pct(col.metrics.structural_relevance)}</b></div>
                    <div className="lab-metric deep"><span>concision</span><b>{col.metrics.concision_per_1k?.toFixed(2)}</b></div>
                    <div className="lab-metric deep"><span>|C(q)|</span><b>{col.metrics.cq_size}</b></div>
                  </>}
                </div>
                <div className="lab-trace">
                  {(col.trace?.stages ?? []).map((s) => (
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

      {/* answer columns */}
      {askData && (
        <div className="lab-cols">
          {askData.columns.map((col) => {
            const won = chosen === col.profile_name
            return (
              <div key={col.profile_name} className={`lab-col${won ? ' won' : ''}`}>
                <div className="lab-col-head">
                  <span className="lab-col-name">{col.profile_name}</span>
                  <button className={`lab-best${won ? ' on' : ''}`} onClick={() => markBest(col.profile_name)}>{won ? '★ best' : '☆ best'}</button>
                </div>
                <div className="lab-metrics">
                  <div className="lab-metric"><span>grounded</span><b>{pct(col.metrics.groundedness)}</b></div>
                  <div className="lab-metric"><span>latency</span><b>{ms(col.latency_ms)}</b></div>
                  <div className="lab-metric"><span>cost</span><b>{usd(col.cost_usd)}</b></div>
                  <div className="lab-metric"><span>turns</span><b>{col.turns ?? '—'}</b></div>
                </div>
                <div className="lab-answer">{col.answer || <span className="lab-empty">no answer</span>}</div>
                {col.citations.length > 0 && (
                  <div className="lab-cites">
                    {col.citations.map((c) => (
                      <button key={c.iri} className="lab-cite" onClick={() => onSelectNode(c.iri)}>{c.title}</button>
                    ))}
                  </div>
                )}
              </div>
            )
          })}
        </div>
      )}

      {/* path result */}
      {pathData && (
        <div className="lab-path">
          {pathData.error && <div className="lab-error">{pathData.error}</div>}
          {!pathData.error && (
            <>
              <div className="lab-path-head">
                <button className="lab-cite" onClick={() => onSelectNode(pathData.a.iri)}>{pathData.a.title}</button>
                <span className="lab-path-arrow">↔</span>
                <button className="lab-cite" onClick={() => onSelectNode(pathData.b.iri)}>{pathData.b.title}</button>
                <span className={`lab-path-status ${pathData.connected ? 'ok' : 'no'}`}>
                  {pathData.connected ? `connected · ${pathData.paths[0] ? pathData.paths[0].length - 1 : 0} hop(s)` : 'no typed-edge path'}
                </span>
              </div>
              {pathData.paths.map((p, pi) => (
                <div key={pi} className="lab-path-chain">
                  {p.map((n, ni) => (
                    <span key={n.iri} className="lab-path-step">
                      <button className="lab-result lab-path-node" onClick={() => onSelectNode(n.iri)}>{n.title}</button>
                      {ni < p.length - 1 && <span className="lab-path-sep">→</span>}
                    </span>
                  ))}
                </div>
              ))}
              {pathData.common.length > 0 && (
                <div className="lab-path-common">
                  <span className="lab-recent-label">common neighbours</span>
                  {pathData.common.map((n) => (
                    <button key={n.iri} className="lab-cite" onClick={() => onSelectNode(n.iri)}>{n.title}</button>
                  ))}
                </div>
              )}
            </>
          )}
        </div>
      )}

      {!data && !askData && !pathData && !loading && !error && (
        <div className="lab-hint">Pick regimes, then <b>retrieve</b> (ranked nodes; add <b>deep</b> for C(q) coverage), <b>answer</b> (synthesized + grounded), or <b>path</b> (how two nodes connect). Type, run, and columns land side by side — every query is logged for the nightly sweep.</div>
      )}
    </div>
  )
}
