/**
 * renderMarkdown — math-placeholder restore + wikilink transform.
 *
 * Regression: inline math beginning with `$1` (e.g. `$1\times0.25$`) was corrupted
 * to `INLINE\times0.25` because the restore passed the math as a String.replace
 * replacement, where `$1` means "capture group 1". The fix uses a replacement
 * function so math is inserted verbatim.
 */
import { describe, expect, it } from 'vitest';
import { renderMarkdown } from './markdown';

describe('renderMarkdown math restore', () => {
  it('preserves inline math beginning with $1 (no $-group corruption)', () => {
    const html = renderMarkdown('posterior odds are $1\\times0.25=0.25$, prob $0.2$.');
    expect(html).toContain('1\\times0.25=0.25');
    expect(html).not.toContain('INLINE');
    expect(html).not.toContain('BLOCK');
  });

  it('preserves a display math block verbatim', () => {
    const html = renderMarkdown('$$\\frac{a}{b}$$');
    expect(html).toContain('$$\\frac{a}{b}$$');
  });
});

describe('renderMarkdown wikilinks', () => {
  it('turns [[slug]] and [[slug|label]] into in-app anchors', () => {
    const html = renderMarkdown('see [[entropy]] and [[bayesian-inference|Bayes]]');
    expect(html).toContain('<a class="wikilink" data-slug="entropy">entropy</a>');
    expect(html).toContain('<a class="wikilink" data-slug="bayesian-inference">Bayes</a>');
  });
});
