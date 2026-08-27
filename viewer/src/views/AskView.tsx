import { useEffect, useRef, useState } from 'react'
import type { AskMessage, AskResponse, AskTurn, Citation, ConversationSummary } from '../types'
import {
  askStream, resolveSlug, ApiError,
  listConversations, getConversation, saveConversation, deleteConversation, renameConversation,
  createShare, revokeShare,
} from '../lib/api'
import { shareLink } from '../lib/share'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'
import { useSpeech, useSpeechInput } from '../lib/voice'

// A chat turn carries the wire fields (role, content) plus, for assistant turns,
// streaming state, structured citations, and a small meta line.
interface Turn extends AskMessage {
  citations?: Citation[]
  meta?: { model: string; turns: number }
  streaming?: boolean
  status?: string
  error?: boolean
  interrupted?: boolean   // connection dropped (e.g. app backgrounded) — offer retry
  startedAt?: number      // when this answer started streaming, for an elapsed timer
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

function Thinking({ label, since }: { label: string; since?: number }) {
  // Tick every second so the label carries a live elapsed count — the ask can take
  // ~20s, and a moving timer is the difference between "working" and "frozen".
  const [, setTick] = useState(0)
  useEffect(() => {
    if (!since) return
    const iv = setInterval(() => setTick((t) => t + 1), 1000)
    return () => clearInterval(iv)
  }, [since])
  const secs = since ? Math.floor((Date.now() - since) / 1000) : 0
  return (
    <div className="ask-thinking">
      <span className="ask-dot" /><span className="ask-dot" /><span className="ask-dot" />
      <span className="ask-thinking-label">{label}{since && secs >= 2 ? ` · ${secs}s` : ''}</span>
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
  const [autoRead, setAutoRead] = useState(false)
  const [speakingIdx, setSpeakingIdx] = useState<number | null>(null)
  const scrollRef = useRef<HTMLDivElement>(null)
  const inputRef = useRef<HTMLTextAreaElement>(null)

  // Auto-grow the composer with its content (typed or dictated), up to a cap;
  // beyond that it scrolls internally. Runs on every input change incl. clears.
  useEffect(() => {
    const el = inputRef.current
    if (!el) return
    el.style.height = 'auto'
    el.style.height = `${Math.min(el.scrollHeight, 200)}px`
  }, [input])

  // Voice out (readout) + voice in (dictation). Both browser-native; the buttons
  // hide themselves where unsupported.
  const speech = useSpeech()
  useEffect(() => { if (!speech.speaking) setSpeakingIdx(null) }, [speech.speaking])
  const inputBaseRef = useRef('')
  const voice = useSpeechInput((t) =>
    setInput((inputBaseRef.current ? inputBaseRef.current + ' ' : '') + t))
  const toggleMic = () => {
    if (voice.listening) { voice.stop(); return }
    inputBaseRef.current = input
    voice.start()
  }
  const toggleListen = (idx: number, text: string) => {
    if (speakingIdx === idx) { speech.stop(); setSpeakingIdx(null); return }
    speech.speak(text); setSpeakingIdx(idx)
  }

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

  // A dropped SSE — the app was backgrounded, the tab was hidden, or the network
  // blipped — surfaces as a socket/abort error, not a server failure. Detect it so
  // we can show a calm "interrupted, tap retry" instead of a raw "Software caused
  // connection abort". hiddenRef records whether the page went hidden mid-stream.
  const hiddenRef = useRef(false)
  const isInterrupt = (msg: string) =>
    hiddenRef.current || /abort|connection|network|failed to fetch|load failed|the operation was/i.test(msg)

  // Stream an answer for a conversation whose LAST turn is the user question.
  // Shared by send() and retry() so retry re-runs without duplicating the bubble.
  const streamAnswer = async (base: Turn[]) => {
    hiddenRef.current = false
    setTurns([...base, { role: 'assistant', content: '', streaming: true, startedAt: Date.now() }])
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
          persist([
            ...base.map(({ role, content, citations, meta }) => ({ role, content, citations, meta })),
            { role: 'assistant', content: res.answer, citations: res.citations,
              meta: { model: res.model, turns: res.turns } },
          ])
          if (autoRead && speech.supported) { speech.speak(res.answer); setSpeakingIdx(base.length) }
        },
        onError: (msg) => patchLast((t) => ({ ...t, content: msg, error: true, interrupted: isInterrupt(msg), streaming: false })),
      })
    } catch (e) {
      const msg = e instanceof ApiError && e.status === 429
        ? 'You’ve hit the rate limit — give it a minute and try again.'
        : e instanceof Error ? e.message : 'Something went wrong.'
      const rateLimited = e instanceof ApiError && e.status === 429
      patchLast((t) => ({ ...t, content: msg, error: true, interrupted: !rateLimited && isInterrupt(msg), streaming: false }))
    } finally {
      setLoading(false)
    }
  }

  const send = (text: string) => {
    const q = text.trim()
    if (!q || loading) return
    setInput('')
    streamAnswer([...turns, { role: 'user', content: q } as Turn])
  }

  // Re-run the last question in place: drop the failed assistant turn, keep the
  // conversation through the user's question, and stream a fresh answer.
  const retry = () => {
    if (loading) return
    let base = turns
    if (base.length && base[base.length - 1].role === 'assistant') base = base.slice(0, -1)
    if (!base.length || base[base.length - 1].role !== 'user') return
    streamAnswer(base)
  }

  // If the page is hidden while a stream is in flight, remember it — the abort that
  // follows is a navigation/background drop, not a server error.
  useEffect(() => {
    const onVis = () => { if (document.hidden && loading) hiddenRef.current = true }
    document.addEventListener('visibilitychange', onVis)
    return () => document.removeEventListener('visibilitychange', onVis)
  }, [loading])

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

  const [shareMsg, setShareMsg] = useState<string | null>(null)
  const doShareConversation = async (id: string, title: string) => {
    try {
      const { url } = await createShare('conversation', id)
      const r = await shareLink(url, title)                 // native sheet → clipboard fallback
      if (r === 'cancelled') return
      setShareMsg(r === 'copied' ? 'Link copied' : r === 'shared' ? 'Shared' : 'Share failed')
    } catch {
      setShareMsg('Share failed')
    }
    setTimeout(() => setShareMsg(null), 2200)
    refreshHistory()   // pick up the now-shared badge
  }
  const shareConversation = (c: ConversationSummary) => doShareConversation(c.id, c.title)
  // Title for the share sheet when sharing the open chat: its first question.
  const currentTitle = () =>
    turns.find((t) => t.role === 'user')?.content?.slice(0, 70) || 'PKIS conversation'
  const revokeConversationShare = async (c: ConversationSummary) => {
    if (!c.share_token || !window.confirm('Revoke this link? Anyone who has it will lose access.')) return
    await revokeShare(c.share_token).catch(() => {})
    setShareMsg('Link revoked')
    setTimeout(() => setShareMsg(null), 2200)
    refreshHistory()
  }

  const onKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(input) }
  }

  const empty = turns.length === 0

  return (
    <div className="ask-view">
      {shareMsg && <div className="ask-toast">{shareMsg}</div>}
      {(signedIn || speech.supported) && (
        <div className="ask-toolbar">
          <div className="ask-toolbar-grp">
            {signedIn && (
              <button className="ask-tool-btn" onClick={() => setHistoryOpen(true)} aria-label="History">
                ☰ history
              </button>
            )}
            {signedIn && !empty && (
              <button className="ask-tool-btn" onClick={newChat} aria-label="New chat">
                ＋ new
              </button>
            )}
            {signedIn && convId && (
              <button className="ask-tool-btn" onClick={() => doShareConversation(convId, currentTitle())}
                aria-label="Share this conversation" title="Share this conversation">
                ↗ share
              </button>
            )}
          </div>
          {speech.supported && (
            <button
              className={`ask-tool-btn${autoRead ? ' active' : ''}`}
              onClick={() => { const n = !autoRead; setAutoRead(n); if (!n) { speech.stop(); setSpeakingIdx(null) } }}
              aria-label="Auto-read responses"
            >
              🔊 {autoRead ? 'auto-read on' : 'auto-read'}
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
                  <div className={`ask-error${t.interrupted ? ' ask-interrupted' : ''}`}>
                    <div>{t.interrupted
                      ? 'Connection interrupted — you may have switched away or lost signal. Your question is still here.'
                      : t.content}</div>
                    <button className="ask-retry" onClick={retry} disabled={loading}>↻ retry</button>
                  </div>
                ) : t.streaming ? (
                  <>
                    {t.status && <Thinking label={t.status} since={t.startedAt} />}
                    {t.content
                      ? <div className="ask-streaming body-text">{t.content}</div>
                      : !t.status && <Thinking label="searching the graph…" since={t.startedAt} />}
                  </>
                ) : (
                  <>
                    <Answer md={t.content} onOpen={onSelectNode} />
                    <div className="ask-answer-foot">
                      {t.citations && t.citations.length > 0 && (
                        <div className="ask-citations">
                          <span className="ask-cite-label">sources</span>
                          {t.citations.map((c) => (
                            <button key={c.iri} className="ask-cite" title={c.iri}
                              onClick={() => onSelectNode(c.iri)}>{c.title}</button>
                          ))}
                        </div>
                      )}
                      {speech.supported && t.content && (
                        <button className="ask-listen" onClick={() => toggleListen(i, t.content)}>
                          {speakingIdx === i ? '■ stop' : '▶ listen'}
                        </button>
                      )}
                    </div>
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
                  <button className={`ask-history-act${c.shared ? ' shared' : ''}`}
                    title={c.shared ? 'Shared — tap to share again' : 'Share'}
                    onClick={() => shareConversation(c)}>↗</button>
                  {c.shared && (
                    <button className="ask-history-act revoke" title="Revoke link"
                      onClick={() => revokeConversationShare(c)}>⊘</button>
                  )}
                  <button className="ask-history-act" title="Rename" onClick={() => renameConv(c)}>✎</button>
                  <button className="ask-history-act" title="Delete" onClick={() => removeConversation(c.id)}>✕</button>
                </div>
              ))
            )}
          </div>
        </>
      )}

      <div className="ask-composer">
        {voice.supported && (
          <button
            className={`ask-mic${voice.listening ? ' listening' : ''}`}
            onClick={toggleMic}
            aria-label={voice.listening ? 'Stop dictation' : 'Dictate'}
            title={voice.listening ? 'Stop' : 'Speak your question'}
          >🎤</button>
        )}
        <textarea
          ref={inputRef}
          className="ask-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={onKeyDown}
          placeholder={voice.listening ? 'Listening…' : 'Ask anything about your knowledge…'}
          rows={2}
        />
        <button className="ask-send" disabled={!input.trim() || loading}
          onClick={() => send(input)} aria-label="Send">↑</button>
      </div>
    </div>
  )
}
