// KaTeX auto-render integration.
// NOTE: the previous version used `import(/* @vite-ignore */ 'katex/dist/contrib/auto-render.js')`,
// a bare specifier the browser can't resolve at runtime — so math never rendered. Import the
// auto-render contrib statically so Vite bundles it; the KaTeX CSS is imported globally in index.css.
import renderMathInElement from 'katex/contrib/auto-render'

const KATEX_OPTS = {
  delimiters: [
    { left: '$$', right: '$$', display: true },
    { left: '\\[', right: '\\]', display: true },
    { left: '$', right: '$', display: false },
    { left: '\\(', right: '\\)', display: false },
  ],
  throwOnError: false,
}

export function renderMath(el: HTMLElement | null): void {
  if (!el) return
  try {
    renderMathInElement(el, KATEX_OPTS)
  } catch {
    /* best effort */
  }
}
