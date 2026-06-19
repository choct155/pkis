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

// Rebuild the full transcript from a SpeechRecognition results list. Stateless by
// design (called fresh each event, never accumulating across events) AND tolerant
// of Android Chrome, which emits the in-progress utterance as MULTIPLE cumulative
// interim entries ("so", "so I", "so I have", …). The rule that handles both the
// well-behaved case and Android's: concatenate only the FINALIZED segments, and
// for the interim take just the latest entry (overwrite, never append). Appending
// the interim entries is what produced the "soso Iso I have…" recursion.
export function assembleTranscript(results: ArrayLike<any>): string {
  let final = ''
  let interim = ''
  for (let i = 0; i < results.length; i++) {
    const seg = results[i][0].transcript
    if (results[i].isFinal) final += seg + ' '
    else interim = seg
  }
  return (final + interim).replace(/\s+/g, ' ').trim()
}

// ── Voice input (speech-to-text) ───────────────────────────────────────────
// onTranscript fires with the full transcript so far (final + interim) so the
// caller can live-fill the composer; we never auto-send (STT errs, user edits).
export function useSpeechInput(onTranscript: (text: string) => void) {
  const SR = typeof window !== 'undefined'
    ? ((window as any).SpeechRecognition || (window as any).webkitSpeechRecognition)
    : null
  const supported = !!SR
  const [listening, setListening] = useState(false)
  const recRef = useRef<any>(null)
  const cbRef = useRef(onTranscript)
  cbRef.current = onTranscript

  const stop = useCallback(() => { try { recRef.current?.stop() } catch { /* ignore */ } }, [])

  const start = useCallback(() => {
    if (!supported || recRef.current) return
    const rec = new SR()
    rec.lang = 'en-US'
    rec.interimResults = true
    rec.continuous = true
    // Rebuild the FULL transcript from e.results every event (it's the cumulative
    // source of truth). Never accumulate across events with +=: Android Chrome
    // re-fires already-finalized results, and appending them produces the classic
    // "so so I so I have…" recursion.
    rec.onresult = (e: any) => { cbRef.current(assembleTranscript(e.results)) }
    rec.onerror = () => { setListening(false) }
    rec.onend = () => { setListening(false); recRef.current = null }
    recRef.current = rec
    setListening(true)
    try { rec.start() } catch { setListening(false); recRef.current = null }
  }, [SR, supported])

  useEffect(() => () => { try { recRef.current?.abort?.() } catch { /* ignore */ } }, [])
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
