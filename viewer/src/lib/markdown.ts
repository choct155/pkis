import { marked } from 'marked'

marked.setOptions({
  gfm: true,
  breaks: true,
})

export function renderMarkdown(md: string): string {
  if (!md) return ''
  // Protect display math blocks from marked's escaping
  const placeholders: string[] = []
  let protected_ = md.replace(/\$\$[\s\S]+?\$\$/g, (m) => {
    placeholders.push(m)
    return `%%MATH_BLOCK_${placeholders.length - 1}%%`
  })
  protected_ = protected_.replace(/\$[^$\n]+?\$/g, (m) => {
    placeholders.push(m)
    return `%%MATH_INLINE_${placeholders.length - 1}%%`
  })

  let html = marked.parse(protected_) as string
  placeholders.forEach((p, i) => {
    html = html.replace(
      new RegExp(`%%MATH_(BLOCK|INLINE)_${i}%%`, 'g'),
      p
    )
  })
  return html
}
