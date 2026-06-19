import { useEffect, useRef, useState } from 'react'
import type { AskMessage, AskResponse, AskTurn, Citation, ConversationSummary } from '../types'
import {
  askStream, resolveSlug, ApiError,
  listConversations, getConversation, saveConversation, deleteConversation, renameConversation,
} from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'

// A chat turn carries the wire fields (role, content) plus, for assistant turns,
// streaming state, structured citations, and a small meta line.
interface Turn extends AskMessage {
  citations?: Citation[]
  meta?: { model: string; turns: number }
  streaming?: boolean
  status?: string
  error?: boolean
}

const EXAMPLES = [
  'What is the relationship between mutual information and KL divergence?',
  'How does do-calculus connect to the backdoor criterion?',
  'What do I need to understand before tackling variational inference?',
]

function relTime(iso: string): string {
  const d = (Date.now() - new Date(iso).getTime()) / 1000
  if (d < 60) return 'just now'
  if (d < 3600) return `${Math.floor(d / 60)}m ago`
  if (d < 86400) return `${Math.floor(d / 3600)}h ago`
  if (d < 604800) return `${Math.floor(d / 86400)}d ago`
  return new Date(iso).toLocaleDateString()
}

// Render a FINAL assistant answer: markdown + KaTeX, [[wikilinks]] open the node.
// (While streaming we render plain text — re-parsing markdown per token flickers.)
function Answer({ md, onOpen }: { md: string; onOpen: (iri: string) => void }) {
  const ref = useRef<HTMLDivElement>(null)
  const html = renderMarkdown(md)
  useEffect(() => {
    renderMath(ref.current)
    ref.current?.querySelectorAll('a[href]').forEach((a) => {
      a.setAttribute('target', '_blank'); a.setAttribute('rel', 'noreferrer')
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

function Thinking({ label }: { label: string }) {
  return (
    <div className="ask-thinking">
      <span className="ask-dot" /><span className="ask-dot" /><span className="ask-dot" />
      <span className="ask-thinking-label">{label}</span>
    </div>
  )
}

interface Props {
  onSelectNode: (iri: string) => void
  signedIn: boolean
  onSignIn: () => void
}

export default function AskView({ onSelectNode, signedIn, onSignIn }: Props) {
  const [turns, setTurns] = useState<Turn[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [convId, setConvId] = useState<string | null>(null)
  const [history, setHistory] = useState<ConversationSummary[]>([])
  const [historyOpen, setHistoryOpen] = useState(false)
  const scrollRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: 'smooth' })
  }, [turns])

  const refreshHistory = () => {
    if (signedIn) listConversations().then(setHistory).catch(() => { /* leave as-is */ })
  }
  useEffect(() => { if (historyOpen) refreshHistory() }, [historyOpen]) // eslint-disable-line

  const patchLast = (fn: (t: Turn) => Turn) =>
    setTurns((prev) => {
      const copy = [...prev]
      copy[copy.length - 1] = fn(copy[copy.length - 1])
      return copy
    })

  // Auto-save the completed exchange (signed-in only). Creates the conversation
  // on first save, then updates in place; the server keeps the latest state.
  const persist = (clean: AskTurn[]) => {
    if (!signedIn || !clean.length) return
    saveConversation(clean, convId)
      .then((r) => { if (!convId) setConvId(r.id); refreshHistory() })
      .catch(() => { /* a failed save never blocks the chat */ })
  }

  const send = async (text: string) => {
    const q = text.trim()
    if (!q || loading) return
    const base = [...turns, { role: 'user', content: q } as Turn]
    setTurns([...base, { role: 'assistant', content: '', streaming: true }])
    setInput('')
    setLoading(true)
    const wire: AskMessage[] = base.map(({ role, content }) => ({ role, content }))
    try {
      await askStream(wire, {
        onStatus: (status) => patchLast((t) => ({ ...t, status, content: '' })),
        onDelta: (chunk) => patchLast((t) => ({ ...t, status: undefined, content: t.content + chunk })),
        onDone: (res: AskResponse) => {
          patchLast((t) => ({
            ...t, content: res.answer, citations: res.citations,
            meta: { model: res.model, turns: res.turns }, streaming: false, status: undefined,
          }))
          // Persist the finalized exchange (strip streaming-only fields).
          persist([
            ...base.map(({ role, content, citations, meta }) => ({ role, content, citations, meta })),
            { role: 'assistant', content: res.answer, citations: res.citations,
              meta: { model: res.model, turns: res.turns } },
          ])
        },
        onError: (msg) => patchLast((t) => ({ ...t, content: msg, error: true, streaming: false })),
      })
    } catch (e) {
      const msg = e instanceof ApiError && e.status === 429
        ? 'You’ve hit the rate limit — give it a minute and try again.'
        : e instanceof Error ? e.message : 'Something went wrong.'
      patchLast((t) => ({ ...t, content: msg, error: true, streaming: false }))
    } finally {
      setLoading(false)
    }
  }

  const newChat = () => { setTurns([]); setConvId(null); setHistoryOpen(false) }

  const openConversation = async (id: string) => {
    try {
      const c = await getConversation(id)
      setTurns(c.messages.map((m) => ({ ...m })))
      setConvId(id)
      setHistoryOpen(false)
    } catch { /* ignore */ }
  }

  const removeConversation = async (id: string) => {
    await deleteConversation(id).catch(() => {})
    if (id === convId) newChat()
    refreshHistory()
  }

  const renameConv = async (c: ConversationSummary) => {
    const t = window.prompt('Rename conversation', c.title)
    if (t == null) return
    await renameConversation(c.id, t.trim() || 'Untitled').catch(() => {})
    refreshHistory()
  }

  const onKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(input) }
  }

  const empty = turns.length === 0

  return (
    <div className="ask-view">
      {signedIn && (
        <div className="ask-toolbar">
          <button className="ask-tool-btn" onClick={() => setHistoryOpen(true)} aria-label="History">
            ☰ history
          </button>
          {!empty && (
            <button className="ask-tool-btn" onClick={newChat} aria-label="New chat">
              ＋ new
            </button>
          )}
        </div>
      )}

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
                <button key={ex} className="ask-example" onClick={() => send(ex)}>{ex}</button>
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
                ) : t.streaming ? (
                  <>
                    {t.status && <Thinking label={t.status} />}
                    {t.content
                      ? <div className="ask-streaming body-text">{t.content}</div>
                      : !t.status && <Thinking label="searching the graph…" />}
                  </>
                ) : (
                  <>
                    <Answer md={t.content} onOpen={onSelectNode} />
                    {t.citations && t.citations.length > 0 && (
                      <div className="ask-citations">
                        <span className="ask-cite-label">sources</span>
                        {t.citations.map((c) => (
                          <button key={c.iri} className="ask-cite" title={c.iri}
                            onClick={() => onSelectNode(c.iri)}>{c.title}</button>
                        ))}
                      </div>
                    )}
                  </>
                )}
              </div>
            )
          )
        )}
        {/* Sign-in nudge: only once there's something worth saving. */}
        {!signedIn && !empty && (
          <button className="ask-signin-hint" onClick={onSignIn}>
            Sign in to save this conversation →
          </button>
        )}
      </div>

      {historyOpen && (
        <>
          <div className="ask-history-backdrop" onClick={() => setHistoryOpen(false)} />
          <div className="ask-history">
            <div className="ask-history-head">
              <span>Conversations</span>
              <button className="ask-tool-btn" onClick={() => setHistoryOpen(false)}>✕</button>
            </div>
            {history.length === 0 ? (
              <div className="ask-history-empty">No saved conversations yet.</div>
            ) : (
              history.map((c) => (
                <div key={c.id} className={`ask-history-item${c.id === convId ? ' active' : ''}`}>
                  <button className="ask-history-open" onClick={() => openConversation(c.id)}>
                    <div className="ask-history-title">{c.title}</div>
                    <div className="ask-history-meta">{c.turn_count} · {relTime(c.updated_at)}</div>
                  </button>
                  <button className="ask-history-act" title="Rename" onClick={() => renameConv(c)}>✎</button>
                  <button className="ask-history-act" title="Delete" onClick={() => removeConversation(c.id)}>✕</button>
                </div>
              ))
            )}
          </div>
        </>
      )}

      <div className="ask-composer">
        <textarea
          className="ask-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={onKeyDown}
          placeholder="Ask anything about your knowledge…"
          rows={1}
        />
        <button className="ask-send" disabled={!input.trim() || loading}
          onClick={() => send(input)} aria-label="Send">↑</button>
      </div>
    </div>
  )
}
