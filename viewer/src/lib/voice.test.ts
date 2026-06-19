import { describe, it, expect } from 'vitest'
import { cleanForSpeech, assembleTranscript } from './voice'

// Simulate a SpeechRecognition results list: each result is [{transcript}] + isFinal.
const R = (...segs: Array<[string, boolean]>) =>
  segs.map(([transcript, isFinal]) => ({ 0: { transcript }, isFinal, length: 1 }))

describe('assembleTranscript (takes the latest snapshot, never concatenates)', () => {
  it('returns a single result verbatim', () => {
    expect(assembleTranscript(R(['so', false]))).toBe('so')
  })

  it('THE BUG: cumulative snapshots marked final must NOT pile up — latest wins', () => {
    // Android Chrome's real emission for one utterance: growing snapshots, each
    // flagged final. Must return "okay I have a question", not "okay okay I okay…".
    const results = R(
      ['okay', true], ['okay I', true], ['okay I have', true],
      ['okay I have a', true], ['okay I have a question', true],
    )
    expect(assembleTranscript(results)).toBe('okay I have a question')
  })

  it('same with interim snapshots', () => {
    const results = R(['so', false], ['so I', false], ['so I have a question', false])
    expect(assembleTranscript(results)).toBe('so I have a question')
  })

  it('is stateless — re-firing the same results does not change the answer', () => {
    const ev = R(['so I have a question', true])
    expect(assembleTranscript(ev)).toBe('so I have a question')
    expect(assembleTranscript(ev)).toBe('so I have a question')
  })

  it('trims and collapses whitespace of the latest snapshot', () => {
    expect(assembleTranscript(R(['  okay   I  have a question  ', true]))).toBe('okay I have a question')
  })

  it('returns empty string for an empty list', () => {
    expect(assembleTranscript([])).toBe('')
  })
})

describe('cleanForSpeech', () => {
  it('humanizes wikilinks (dashes → spaces, label wins)', () => {
    expect(cleanForSpeech('rests on [[mutual-information]] and [[kl-divergence|KL]].'))
      .toBe('rests on mutual information and KL.')
  })

  it('drops inline math and turns display math into a beat', () => {
    const out = cleanForSpeech('MI is $I(X;Y)$ and $$D_{KL}(p\\|q)$$ matters.')
    expect(out).not.toContain('$')
    expect(out).not.toContain('D_{KL}')
    expect(out).toContain('equation')
  })

  it('strips headings, bold, bullets, code, and table pipes', () => {
    const md = '## Heading\n- **bold** point\n`code`\n| a | b |'
    const out = cleanForSpeech(md)
    expect(out).not.toMatch(/[#*`|]/)
    expect(out).toContain('bold point')
  })

  it('keeps plain prose intact and collapses whitespace', () => {
    expect(cleanForSpeech('Just   plain   text.')).toBe('Just plain text.')
  })

  it('never throws on empty / undefined-ish input', () => {
    expect(cleanForSpeech('')).toBe('')
  })
})
