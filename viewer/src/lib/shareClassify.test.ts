import { describe, it, expect } from 'vitest'
import { classifyShare } from './shareClassify'

describe('classifyShare', () => {
  it('routes code hosts to resource with an inferred type', () => {
    expect(classifyShare({ url: 'https://github.com/langchain-ai/openwiki' }))
      .toMatchObject({ kind: 'resource', resourceType: 'tool' })
    expect(classifyShare({ url: 'https://pypi.org/project/numpy' }))
      .toMatchObject({ kind: 'resource', resourceType: 'library' })
    expect(classifyShare({ url: 'https://huggingface.co/datasets/x' }))
      .toMatchObject({ kind: 'resource', resourceType: 'dataset' })
  })

  it('routes academic hosts and PDFs to source', () => {
    expect(classifyShare({ url: 'https://arxiv.org/abs/1706.03762' }).kind).toBe('source')
    expect(classifyShare({ url: 'https://example.com/paper.pdf' }).kind).toBe('source')
    expect(classifyShare({ type: 'application/pdf', url: 'file:///x/y' }).kind).toBe('source')
  })

  it('defaults a generic URL to source, and bare text to capture', () => {
    expect(classifyShare({ url: 'https://someblog.example/post' }).kind).toBe('source')
    expect(classifyShare({ text: 'just a thought, no link' }).kind).toBe('capture')
  })

  it('extracts a trailing URL out of shared text', () => {
    const c = classifyShare({ text: 'cool repo https://github.com/foo/bar check it' })
    expect(c.kind).toBe('resource')
    expect(c.url).toBe('https://github.com/foo/bar')
  })
})
