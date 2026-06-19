import { useEffect, useRef, useState } from 'react'
import type { SharedContent } from '../types'
import { getShared, ApiError } from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'

// Public, read-only view behind a capability link (/app/?s=<token>). No auth, no
// app chrome, no composer — just the shared conversation, rendered like the Ask
// view, with a gentle invite to explore PKIS.

function Answer({ md }: { md: string }) {
  const ref = useRef<HTMLDivElement>(null)
  const html = renderMarkdown(md)
  useEffect(() => {
    renderMath(ref.current)
    // Body links open in a new tab; wikilinks/citations are inert here (no app
    // context to navigate within) — they read as emphasis, which is fine.
    ref.current?.querySelectorAll('a[href]').forEach((a) => {
      a.setAttribute('target', '_blank'); a.setAttribute('rel', 'noreferrer')
    })
  }, [md])
  return <div ref={ref} className="body-text" dangerouslySetInnerHTML={{ __html: html }} />
}

export default function ShareView({ token }: { token: string }) {
  const [content, setContent] = useState<SharedContent | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    getShared(token)
      .then(setContent)
      .catch((e) =>
        setError(e instanceof ApiError && e.status === 404
          ? 'This link is no longer available — it may have been revoked or deleted.'
          : 'Could not load this shared conversation.'))
  }, [token])

  return (
    <div className="share-view">
      <header className="share-head">
        <a className="share-brand" href="/app/">PKIS</a>
        <span className="share-tag">shared conversation · read-only</span>
      </header>

      <div className="share-scroll">
        {error ? (
          <div className="share-error">{error}</div>
        ) : !content ? (
          <div className="share-loading">Loading…</div>
        ) : (
          <>
            <h1 className="share-title">{content.title}</h1>
            {content.messages.map((t, i) =>
              t.role === 'user' ? (
                <div key={i} className="ask-turn ask-user">
                  <div className="ask-bubble">{t.content}</div>
                </div>
              ) : (
                <div key={i} className="ask-turn ask-assistant">
                  <Answer md={t.content} />
                  {t.citations && t.citations.length > 0 && (
                    <div className="ask-citations">
                      <span className="ask-cite-label">sources</span>
                      {t.citations.map((c) => (
                        <span key={c.iri} className="ask-cite share-cite">{c.title}</span>
                      ))}
                    </div>
                  )}
                </div>
              )
            )}
            <a className="share-cta" href="/app/">Explore PKIS — ask your own questions →</a>
          </>
        )}
      </div>
    </div>
  )
}
