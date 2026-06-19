import { useCallback, useEffect, useRef, useState } from 'react'

// Browser-native voice in/out for the Ask view. No backend, no cost. Best on
// Chrome (esp. Android Chrome — the primary device); callers feature-detect via
// the returned `supported` flag and hide the affordance where it's false.

// ── Strip markdown / math / wikilinks so TTS speaks prose, not syntax ──────
export function cleanForSpeech(md: string): string {
  let t = md || ''
  t = t.replace(/```[\s\S]*?```/g, ' ')                 // code fences
  t = t.replace(/`([^`]+)`/g, '$1')                     // inline code
  t = t.replace(/\$\$[\s\S]*?\$\$/g, '. equation. ')    // display math → a beat
  t = t.replace(/\$[^$\n]+?\$/g, ' ')                    // inline math → drop
  // [[slug|label]] / [[slug]] → spoken words (dashes → spaces)
  t = t.replace(/\[\[([^\]|#]+)(?:\|([^\]]+))?\]\]/g, (_m, s, l) => String(l || s).replace(/-/g, ' '))
  t = t.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')          // [text](url) → text
  t = t.replace(/^#{1,6}\s*/gm, '')                      // headings
  t = t.replace(/[*_]{1,3}([^*_]+)[*_]{1,3}/g, '$1')     // bold / italic
  t = t.replace(/^\s*[-*+]\s+/gm, '')                    // bullet markers
  t = t.replace(/\|/g, ' ')                              // table pipes
  t = t.replace(/[#>`]/g, ' ')
  t = t.replace(/[ \t]+/g, ' ').replace(/\n{2,}/g, '. ').trim()
  return t
}

// The current utterance's text from a SpeechRecognition results list.
//
// Hard-won: Android Chrome emits ONE spoken utterance as many cumulative
// snapshots ("okay", "okay I", "okay I have", …) AND marks each FINAL. So any
// strategy that concatenates results — whether all of them, or just the finalized
// ones — sums those snapshots into the "okay okay I okay I have…" pile-up. The
// only robust rule is to NEVER concatenate: each result is a cumulative snapshot,
// so the LAST one is the most complete. Paired with single-utterance recognition
// (continuous=false in the hook), the last result is always the right answer; the
// caller appends across mic taps for longer input.
export function assembleTranscript(results: ArrayLike<any>): string {
  if (!results || !results.length) return ''
  const last = results[results.length - 1]
  return String((last && last[0] && last[0].transcript) || '').replace(/\s+/g, ' ').trim()
}

// ── Voice input (speech-to-text) ───────────────────────────────────────────
// "Hold-to-dictate": records until the user stops OR a long silence elapses.
//
// We keep recognition SINGLE-utterance (continuous=false) — the only mode where
// "latest result" survives Android's snapshot-finalization — and AUTO-RESTART it
// on each end. Each session yields one clean utterance (assembleTranscript), which
// we COMMIT once to an accumulator; the live transcript is committed + current.
// Short speaking pauses just trigger a restart; SILENCE_MS of true quiet (or a
// tap) ends it. onTranscript fires with the full dictation; we never auto-send.
const SILENCE_MS = 8000

export function useSpeechInput(onTranscript: (text: string) => void) {
  const SR = typeof window !== 'undefined'
    ? ((window as any).SpeechRecognition || (window as any).webkitSpeechRecognition)
    : null
  const supported = !!SR
  const [listening, setListening] = useState(false)
  const recRef = useRef<any>(null)
  const committedRef = useRef('')   // finalized utterances this dictation
  const currentRef = useRef('')     // current session's latest snapshot
  const stoppingRef = useRef(false) // user (or silence) asked to end
  const silenceRef = useRef<any>(null)
  const cbRef = useRef(onTranscript)
  cbRef.current = onTranscript

  const emit = () =>
    cbRef.current((committedRef.current + ' ' + currentRef.current).replace(/\s+/g, ' ').trim())
  const clearSilence = () => { if (silenceRef.current) { clearTimeout(silenceRef.current); silenceRef.current = null } }

  // stop() and startSession() reference each other via refs so they stay stable
  // and never capture stale state across the auto-restart cycle.
  const stopRef = useRef<() => void>(() => {})
  const startRef = useRef<() => void>(() => {})

  stopRef.current = () => {
    stoppingRef.current = true
    clearSilence()
    if (recRef.current) { try { recRef.current.stop() } catch { /* ignore */ } }
    else { setListening(false); emit() }   // ended during the restart gap
  }
  const armSilence = () => { clearSilence(); silenceRef.current = setTimeout(() => stopRef.current(), SILENCE_MS) }

  startRef.current = () => {
    if (!SR) return
    const rec = new SR()
    rec.lang = 'en-US'
    rec.interimResults = true
    rec.continuous = false
    rec.onresult = (e: any) => { currentRef.current = assembleTranscript(e.results); emit(); armSilence() }
    rec.onerror = () => { /* onend decides: restart or stop */ }
    rec.onend = () => {
      if (currentRef.current) {
        committedRef.current = (committedRef.current + ' ' + currentRef.current).replace(/\s+/g, ' ').trim()
        currentRef.current = ''
      }
      recRef.current = null
      if (stoppingRef.current) { clearSilence(); setListening(false); emit() }
      else setTimeout(() => { if (!stoppingRef.current) startRef.current() }, 250) // let Android tear down first
    }
    recRef.current = rec
    try { rec.start() } catch { recRef.current = null }
  }

  const start = useCallback(() => {
    if (!supported || recRef.current || listening) return
    committedRef.current = ''
    currentRef.current = ''
    stoppingRef.current = false
    setListening(true)
    armSilence()
    startRef.current()
  }, [supported, listening])

  const stop = useCallback(() => stopRef.current(), [])

  useEffect(() => () => {
    stoppingRef.current = true
    clearSilence()
    try { recRef.current?.abort?.() } catch { /* ignore */ }
  }, [])

  return { supported, listening, start, stop }
}

// ── Readout (text-to-speech) ───────────────────────────────────────────────
// speak() chunks into sentences and queues them — this both reads cleanly and
// dodges Chrome's ~15s long-utterance cutoff. stop() cancels the whole queue.
export function useSpeech() {
  const supported = typeof window !== 'undefined' && 'speechSynthesis' in window
  const [speaking, setSpeaking] = useState(false)

  const stop = useCallback(() => {
    if (supported) window.speechSynthesis.cancel()
    setSpeaking(false)
  }, [supported])

  const speak = useCallback((text: string) => {
    if (!supported) return
    window.speechSynthesis.cancel()
    const clean = cleanForSpeech(text)
    const chunks = clean.match(/[^.!?…]+[.!?…]*\s*/g) || (clean ? [clean] : [])
    if (!chunks.length) return
    setSpeaking(true)
    chunks.forEach((c, i) => {
      const u = new SpeechSynthesisUtterance(c.trim())
      u.rate = 1.0
      if (i === chunks.length - 1) {
        u.onend = () => setSpeaking(false)
        u.onerror = () => setSpeaking(false)
      }
      window.speechSynthesis.speak(u)
    })
  }, [supported])

  useEffect(() => () => { if (supported) window.speechSynthesis.cancel() }, [supported])
  return { supported, speaking, speak, stop }
}
