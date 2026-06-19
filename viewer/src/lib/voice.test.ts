import { describe, it, expect } from 'vitest'
import { cleanForSpeech } from './voice'

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
