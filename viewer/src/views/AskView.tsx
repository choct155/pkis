import { useEffect, useRef, useState } from 'react'
import type { AskMessage, Citation } from '../types'
import { ask, resolveSlug } from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'

// A chat turn carries the wire fields (role, content) plus, for assistant turns,
// the structured citations and a small meta line. We strip the extras before
// sending the conversation back to the stateless /ask endpoint.
interface Turn extends AskMessage {
  citations?: Citation[]
  meta?: { model: string; turns: number }
  error?: boolean
}

const EXAMPLES = [
  'What is the relationship between mutual information and KL divergence?',
  'How does do-calculus connect to the backdoor criterion?',
  'What do I need to understand before tackling variational inference?',
]

// Render an assistant answer: markdown + KaTeX, with [[wikilinks]] wired to open
// the referenced node (resolve slug → IRI → DetailSheet). Mirrors DetailSheet's
// MarkdownBody so cited nodes behave identically everywhere.
function Answer({ md, onOpen }: { md: string; onOpen: (iri: string) => void }) {
  const ref = useRef<HTMLDivElement>(null)
  const html = renderMarkdown(md)
  useEffect(() => {
    renderMath(ref.current)
    ref.current?.querySelectorAll('a[href]').forEach((a) => {
      a.setAttribute('target', '_blank')
      a.setAttribute('rel', 'noreferrer')
    })
    const cleanups: Array<() => void> = []
    const wikis = Array.from(ref.current?.querySelectorAll('a.wikilink') ?? []) as HTMLElement[]
    wikis.forEach((a) => {
      const handler = async (e: Event) => {
        e.preventDefault()
        const slug = a.dataset.slug
        if (!slug) return
        const iri = await resolveSlug(slug).catch(() => null)
        if (iri) onOpen(iri)
      }
      a.addEventListener('click', handler)
      cleanups.push(() => a.removeEventListener('click', handler))
    })
    return () => cleanups.forEach((fn) => fn())
  }, [md, onOpen])
  return <div ref={ref} className="body-text" dangerouslySetInnerHTML={{ __html: html }} />
}

interface Props {
  onSelectNode: (iri: string) => void
}

export default function AskView({ onSelectNode }: Props) {
  const [turns, setTurns] = useState<Turn[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const scrollRef = useRef<HTMLDivElement>(null)

  // Keep the latest turn in view as the conversation grows.
  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: 'smooth' })
  }, [turns, loading])

  const send = async (text: string) => {
    const q = text.trim()
    if (!q || loading) return
    const userTurn: Turn = { role: 'user', content: q }
    const next = [...turns, userTurn]
    setTurns(next)
    setInput('')
    setLoading(true)
    try {
      // Send only the wire fields; the server is stateless and re-reads history.
      const wire: AskMessage[] = next.map(({ role, content }) => ({ role, content }))
      const res = await ask(wire)
      setTurns((t) => [...t, {
        role: 'assistant',
        content: res.answer,
        citations: res.citations,
        meta: { model: res.model, turns: res.turns },
      }])
    } catch (e) {
      setTurns((t) => [...t, {
        role: 'assistant',
        content: e instanceof Error ? e.message : 'Something went wrong.',
        error: true,
      }])
    } finally {
      setLoading(false)
    }
  }

  const onKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      send(input)
    }
  }

  const empty = turns.length === 0

  return (
    <div className="ask-view">
      <div className="ask-scroll" ref={scrollRef}>
        {empty ? (
          <div className="ask-empty">
            <div className="ask-empty-glyph">✧</div>
            <h2 className="ask-empty-title">Ask the graph</h2>
            <p className="ask-empty-sub">
              Natural-language questions answered from your knowledge graph — grounded in
              specific nodes, with live links to every source.
            </p>
            <div className="ask-examples">
              {EXAMPLES.map((ex) => (
                <button key={ex} className="ask-example" onClick={() => send(ex)}>
                  {ex}
                </button>
              ))}
            </div>
          </div>
        ) : (
          turns.map((t, i) =>
            t.role === 'user' ? (
              <div key={i} className="ask-turn ask-user">
                <div className="ask-bubble">{t.content}</div>
              </div>
            ) : (
              <div key={i} className="ask-turn ask-assistant">
                {t.error ? (
                  <div className="ask-error">{t.content}</div>
                ) : (
                  <>
                    <Answer md={t.content} onOpen={onSelectNode} />
                    {t.citations && t.citations.length > 0 && (
                      <div className="ask-citations">
                        <span className="ask-cite-label">sources</span>
                        {t.citations.map((c) => (
                          <button
                            key={c.iri}
                            className="ask-cite"
                            title={c.iri}
                            onClick={() => onSelectNode(c.iri)}
                          >
                            {c.title}
                          </button>
                        ))}
                      </div>
                    )}
                  </>
                )}
              </div>
            )
          )
        )}
        {loading && (
          <div className="ask-turn ask-assistant">
            <div className="ask-thinking">
              <span className="ask-dot" /><span className="ask-dot" /><span className="ask-dot" />
              <span className="ask-thinking-label">searching the graph…</span>
            </div>
          </div>
        )}
      </div>

      <div className="ask-composer">
        <textarea
          className="ask-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={onKeyDown}
          placeholder="Ask anything about your knowledge…"
          rows={1}
        />
        <button
          className="ask-send"
          disabled={!input.trim() || loading}
          onClick={() => send(input)}
          aria-label="Send"
        >
          ↑
        </button>
      </div>
    </div>
  )
}
