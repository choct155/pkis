import { useEffect, useRef, useState } from 'react'
import { getInbox, resolveSlug, ApiError } from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import StagedSection from './StagedSection'
import DiscoverView from './DiscoverView'

interface Lane { title: string; body: string; open: number; done: number }

function parseLanes(md: string): Lane[] {
  return md
    .split(/\n(?=## )/)
    .filter((p) => p.startsWith('## '))
    .map((p) => {
      const nl = p.indexOf('\n')
      const title = p.slice(3, nl < 0 ? undefined : nl).trim()
      const body = (nl < 0 ? '' : p.slice(nl + 1)).trim()
      return {
        title,
        body,
        open: (body.match(/^- \[ \]/gm) || []).length,
        done: (body.match(/^- \[x\]/gim) || []).length,
      }
    })
}

// Render one lane's markdown with live [[wikilinks]] (resolve → navigate in-app).
function LaneBody({ md, onSelectNode }: { md: string; onSelectNode: (iri: string) => void }) {
  const ref = useRef<HTMLDivElement>(null)
  const html = renderMarkdown(md)
  useEffect(() => {
    const cleanups: Array<() => void> = []
    ref.current?.querySelectorAll('a[href]').forEach((a) => {
      a.setAttribute('target', '_blank'); a.setAttribute('rel', 'noreferrer')
    })
    ref.current?.querySelectorAll('a.wikilink').forEach((a) => {
      const h = (e: Event) => {
        e.preventDefault()
        const slug = (a as HTMLElement).dataset.slug
        if (slug) resolveSlug(slug).then((iri) => iri && onSelectNode(iri))
      }
      a.addEventListener('click', h); cleanups.push(() => a.removeEventListener('click', h))
    })
    return () => cleanups.forEach((fn) => fn())
  }, [md, onSelectNode])
  return <div ref={ref} className="inbox-lane-body body-text" dangerouslySetInnerHTML={{ __html: html }} />
}

// The consolidated review hub: LIVE staged (bridge notes/stubs) + LIVE discovery
// candidates, plus the agent-written inbox.md swim-lanes (proposals, gaps, …).
// Everything that needs the owner's attention in one place.
export default function InboxView({ onSelectNode }: { onSelectNode: (iri: string) => void }) {
  const [lanes, setLanes] = useState<Lane[] | null>(null)
  const [err, setErr] = useState<string | null>(null)
  const [toast, setToast] = useState<string | null>(null)
  const showToast = (m: string) => { setToast(m); setTimeout(() => setToast(null), 2200) }

  useEffect(() => {
    let cancelled = false
    getInbox()
      .then((d) => { if (!cancelled) setLanes(parseLanes(d.markdown)) })
      .catch((e) => {
        if (cancelled) return
        setErr(e instanceof ApiError && e.status === 401 ? 'sign in as the owner to view the inbox'
          : e instanceof ApiError && e.status === 403 ? 'the inbox is owner-only (administrative)'
          : String(e))
      })
    return () => { cancelled = true }
  }, [])

  if (err) return <div className="empty-state">{err}</div>

  // The md lanes are the slowest; render the live sections immediately and let
  // the lanes fill in. (Auth errors short-circuit above.)
  const liveLanes = (lanes || []).filter((l) => l.open > 0)
  return (
    <div className="inbox-view">
      <div className="inbox-head">
        <span className="inbox-title">Inbox</span>
        <span className="inbox-count">review · owner</span>
      </div>

      {/* Live review queues */}
      <StagedSection onSelectNode={onSelectNode} onToast={showToast} />
      <DiscoverView onSelectNode={onSelectNode} embedded />

      {/* Agent-written swim-lanes (only the non-empty ones). */}
      {lanes === null
        ? <div className="loading-row"><div className="loading-spinner" /> loading lanes…</div>
        : liveLanes.map((l) => (
          <div key={l.title} className="inbox-section">
            <div className="inbox-section-head">
              <span className="inbox-section-title">{l.title}</span>
              <span className="inbox-section-count">{l.open}</span>
            </div>
            <LaneBody md={l.body} onSelectNode={onSelectNode} />
          </div>
        ))}

      {toast && <div className="toast">{toast}</div>}
    </div>
  )
}
