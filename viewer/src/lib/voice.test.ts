import { describe, it, expect } from 'vitest'
import { cleanForSpeech, assembleTranscript } from './voice'

// Simulate a SpeechRecognition results list: each result is [{transcript}] + isFinal.
const R = (...segs: Array<[string, boolean]>) =>
  segs.map(([transcript, isFinal]) => ({ 0: { transcript }, isFinal, length: 1 }))

describe('assembleTranscript (accumulation-bug regression)', () => {
  it('returns the transcript verbatim for a single interim result', () => {
    expect(assembleTranscript(R(['so', false]))).toBe('so')
  })

  it('is stateless across events — re-firing the SAME results does not double', () => {
    const ev = R(['so I have a question', true])
    // Android Chrome re-fires finalized results; calling repeatedly must not grow.
    expect(assembleTranscript(ev)).toBe('so I have a question')
    expect(assembleTranscript(ev)).toBe('so I have a question')
  })

  it('concatenates a finalized segment with the following interim cleanly', () => {
    expect(assembleTranscript(R(['so I have a question', true], [' about entropy', false])))
      .toBe('so I have a question about entropy')
  })

  it('collapses whitespace from segment joins', () => {
    expect(assembleTranscript(R(['hello  ', true], ['  world', false]))).toBe('hello world')
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
