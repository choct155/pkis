import { useEffect, useRef, useState } from 'react'
import { getReader, saveReaderAnnotation, buildReader, getReaderStatus } from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'
import type { ReaderPayload } from '../types'

interface Props {
  slug: string
  onClose: () => void
}

function fmt(t: number): string {
  const m = Math.floor(t / 60), s = Math.floor(t % 60)
  return `${m}:${s.toString().padStart(2, '0')}`
}

export default function ReaderView({ slug, onClose }: Props) {
  const [payload, setPayload] = useState<ReaderPayload | null>(null)
  const [phase, setPhase] = useState<'loading' | 'ready' | 'absent' | 'building' | 'error'>('loading')
  const [curId, setCurId] = useState('')
  const [playing, setPlaying] = useState(false)
  const [rate, setRate] = useState(1)
  const [time, setTime] = useState(0)
  const [audioSrc, setAudioSrc] = useState('')
  const [toast, setToast] = useState<string | null>(null)
  const [sel, setSel] = useState<{ section_id: string; text: string } | null>(null)
  const audioRef = useRef<HTMLAudioElement>(null)
  const bodyRef = useRef<HTMLDivElement>(null)

  const showToast = (m: string) => { setToast(m); setTimeout(() => setToast(null), 1800) }

  const loadPayload = async () => {
    try {
      const p = await getReader(slug)
      setPayload(p)
      localStorage.setItem(`reader:${slug}`, JSON.stringify(p))
      setPhase('ready')
      return true
    } catch { return false }
  }

  // Load payload; if absent, check build status; fall back to a localStorage copy offline.
  useEffect(() => {
    let cancelled = false
    ;(async () => {
      if (await loadPayload()) return
      const s = await getReaderStatus(slug)
      if (cancelled) return
      if (s.state === 'building') setPhase('building')
      else if (s.state === 'error') setPhase('error')
      else {
        const c = localStorage.getItem(`reader:${slug}`)
        if (c) { setPayload(JSON.parse(c)); setPhase('ready') }
        else setPhase('absent')
      }
    })()
    return () => { cancelled = true }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [slug])

  // Poll while a build is in progress.
  useEffect(() => {
    if (phase !== 'building') return
    let cancelled = false
    const iv = setInterval(async () => {
      const s = await getReaderStatus(slug)
      if (cancelled) return
      if (s.state === 'ready') { clearInterval(iv); await loadPayload() }
      else if (s.state === 'error') { clearInterval(iv); setPhase('error') }
    }, 4000)
    return () => { cancelled = true; clearInterval(iv) }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [phase, slug])

  const startBuild = async () => {
    setPhase('building')
    try { await buildReader(slug) } catch { setPhase('error') }
  }

  // Resolve audio source: prefer a cached blob (offline), else stream from the network.
  useEffect(() => {
    if (!payload) return
    let obj = ''
    let cancelled = false
    ;(async () => {
      try {
        const cache = await caches.open('pkis-reader-audio')
        const hit = await cache.match(payload.audio_url)
        if (hit) {
          const b = await hit.blob()
          obj = URL.createObjectURL(b)
          if (!cancelled) setAudioSrc(obj)
          return
        }
      } catch { /* no cache API */ }
      if (!cancelled) setAudioSrc(payload.audio_url)
    })()
    return () => { cancelled = true; if (obj) URL.revokeObjectURL(obj) }
  }, [payload])

  // Render KaTeX after the sections mount.
  useEffect(() => { if (payload) renderMath(bodyRef.current) }, [payload])

  // Lock-screen / background controls.
  useEffect(() => {
    if (!payload || !('mediaSession' in navigator)) return
    try {
      navigator.mediaSession.metadata = new MediaMetadata({ title: payload.title, artist: 'PKIS narration' })
      navigator.mediaSession.setActionHandler('play', () => audioRef.current?.play())
      navigator.mediaSession.setActionHandler('pause', () => audioRef.current?.pause())
      navigator.mediaSession.setActionHandler('seekbackward', () => seek((audioRef.current?.currentTime ?? 0) - 15))
      navigator.mediaSession.setActionHandler('seekforward', () => seek((audioRef.current?.currentTime ?? 0) + 15))
    } catch { /* unsupported actions */ }
  }, [payload])

  useEffect(() => { if (audioRef.current) audioRef.current.playbackRate = rate }, [rate, audioSrc])

  const onTime = () => {
    const a = audioRef.current; if (!a || !payload) return
    setTime(a.currentTime)
    const cur = payload.sections.find((s) => a.currentTime >= s.t_start && a.currentTime < s.t_end)
      ?? payload.sections[payload.sections.length - 1]
    if (cur && cur.id !== curId) {
      setCurId(cur.id)
      document.getElementById(`sec-${cur.id}`)?.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }

  const seek = (t: number) => { const a = audioRef.current; if (a) { a.currentTime = Math.max(0, t); a.play() } }
  const toggle = () => { const a = audioRef.current; if (a) { a.paused ? a.play() : a.pause() } }

  const saveOffline = async () => {
    if (!payload) return
    showToast('saving for offline…')
    try { const c = await caches.open('pkis-reader-audio'); await c.add(payload.audio_url); showToast('saved for offline ✓') }
    catch { showToast('offline save failed') }
  }

  const onSelect = () => {
    const s = window.getSelection?.()
    const text = s?.toString().trim()
    if (!text || !s) return
    let node: HTMLElement | null = (s.anchorNode as HTMLElement) ?? null
    let secId = ''
    while (node) {
      if (node.dataset && node.dataset.sec) { secId = node.dataset.sec; break }
      node = node.parentElement
    }
    if (secId) setSel({ section_id: secId, text })
  }

  const annotate = async (kind: 'note' | 'bridge', note: string) => {
    if (!sel) return
    try {
      await saveReaderAnnotation({ slug, section_id: sel.section_id, text: sel.text, note, kind })
      showToast(kind === 'bridge' ? 'flagged → bridge note staged' : 'annotation saved')
    } catch { showToast('save failed') }
    setSel(null); window.getSelection?.()?.removeAllRanges()
  }

  if (phase !== 'ready' || !payload) {
    return (
      <div className="reader-overlay">
        <div className="reader-bar">
          <span className="reader-back" onClick={onClose}>← back</span>
          <span className="reader-title">{slug}</span>
        </div>
        <div className="reader-gate">
          {phase === 'loading' && <div className="loading-row"><div className="loading-spinner" /> loading…</div>}
          {phase === 'building' && (
            <>
              <div className="loading-row"><div className="loading-spinner" /> generating narration…</div>
              <div className="reader-gate-note">
                This paper is being narrated (a few minutes — Claude writes it, then it's voiced).
                It'll appear here when ready; you can leave and come back.
              </div>
            </>
          )}
          {phase === 'absent' && (
            <>
              <div className="reader-gate-note">This paper hasn't been narrated yet.</div>
              <button className="cap-submit" onClick={startBuild}>build narration →</button>
            </>
          )}
          {phase === 'error' && (
            <>
              <div className="reader-gate-note">Narration build failed (is this an arXiv source?).</div>
              <button className="cap-submit" onClick={startBuild}>retry build →</button>
            </>
          )}
        </div>
      </div>
    )
  }

  return (
    <div className="reader-overlay">
      <div className="reader-bar">
        <span className="reader-back" onClick={onClose}>← back</span>
        <span className="reader-title">{payload.title}</span>
        <span className="reader-save" onClick={saveOffline}>⤓ offline</span>
      </div>

      <div className="reader-body" ref={bodyRef} onMouseUp={onSelect} onTouchEnd={onSelect}>
        {payload.sections.map((s) => (
          <div key={s.id} id={`sec-${s.id}`} data-sec={s.id} className={`reader-section${curId === s.id ? ' active' : ''}`}>
            <div className="reader-sec-head" onClick={() => seek(s.t_start)}>
              <span className="reader-sec-title">{s.title}</span>
              <span className="reader-sec-time">{fmt(s.t_start)}</span>
            </div>
            <div className="reader-sec-body prose" dangerouslySetInnerHTML={{ __html: renderMarkdown(s.paper_md) }} />
          </div>
        ))}
        <div className="reader-foot">narration is the listening track; the paper is on screen — select any text to annotate or flag</div>
      </div>

      <div className="reader-controls">
        <audio
          ref={audioRef}
          src={audioSrc}
          onTimeUpdate={onTime}
          onPlay={() => setPlaying(true)}
          onPause={() => setPlaying(false)}
          preload="auto"
        />
        <button className="reader-play" onClick={toggle}>{playing ? '⏸' : '▶'}</button>
        <span className="reader-time">{fmt(time)}</span>
        <input
          className="reader-scrub" type="range" min={0} max={payload.total_duration} step={1}
          value={time} onChange={(e) => seek(Number(e.target.value))}
        />
        <span className="reader-time">{fmt(payload.total_duration)}</span>
        <button className="reader-rate" onClick={() => setRate((r) => (r >= 2 ? 0.75 : Math.round((r + 0.25) * 100) / 100))}>{rate}×</button>
      </div>

      {sel && (
        <div className="reader-annot">
          <div className="reader-annot-text">“{sel.text.slice(0, 140)}{sel.text.length > 140 ? '…' : ''}”</div>
          <AnnotInput onNote={(n) => annotate('note', n)} onFlag={(n) => annotate('bridge', n)} onCancel={() => setSel(null)} />
        </div>
      )}
      {toast && <div className="toast">{toast}</div>}
    </div>
  )
}

function AnnotInput({ onNote, onFlag, onCancel }: {
  onNote: (n: string) => void; onFlag: (n: string) => void; onCancel: () => void
}) {
  const [note, setNote] = useState('')
  return (
    <div className="reader-annot-row">
      <input
        className="cap-input" type="text" placeholder="note (optional)…"
        value={note} onChange={(e) => setNote(e.target.value)}
      />
      <button className="action-btn primary" onClick={() => onNote(note)}>✓ note</button>
      <button className="action-btn" onClick={() => onFlag(note)}>⚑ flag</button>
      <button className="action-btn" onClick={onCancel}>✕</button>
    </div>
  )
}
