/**
 * Smoke tests for the viewer ↔ backend contract (B8).
 *
 * api.ts is the single coupling point between the React app and the Flask
 * /pkis-api/* surface — if its paths or request shapes drift, the whole app breaks
 * silently. These tests mock fetch and pin: the base path, that POST helpers send
 * JSON to the right endpoint with the right body, that GET endpoints hit the right
 * URL, and that a non-ok response surfaces as ApiError(status, server-message).
 */

import { afterEach, describe, expect, it, vi } from 'vitest';
import {
  ApiError, searchWiki, getNode, getRelated, getReaderStatus, discoveryAct,
} from './api';

function mockFetch(payload: unknown, ok = true, status = 200) {
  const fn = vi.fn(async () => ({
    ok,
    status,
    statusText: ok ? 'OK' : 'ERR',
    json: async () => payload,
  })) as unknown as typeof fetch;
  globalThis.fetch = fn;
  return fn as unknown as ReturnType<typeof vi.fn>;
}

afterEach(() => {
  vi.restoreAllMocks();
});

describe('api.ts POST contract', () => {
  it('searchWiki posts query + options to /pkis-api/search as JSON', async () => {
    const fetchMock = mockFetch([]);
    await searchWiki('entropy', { max_results: 5 });
    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe('/pkis-api/search');
    expect(init.method).toBe('POST');
    expect(init.headers['Content-Type']).toBe('application/json');
    expect(JSON.parse(init.body)).toEqual({ query: 'entropy', max_results: 5 });
  });

  it('getNode posts the iri to /pkis-api/node', async () => {
    const fetchMock = mockFetch({ id: 'pkis:concept:x' });
    await getNode('pkis:concept:x');
    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe('/pkis-api/node');
    expect(JSON.parse(init.body)).toEqual({ iri: 'pkis:concept:x' });
  });

  it('getRelated merges iri + options into the body', async () => {
    const fetchMock = mockFetch([]);
    await getRelated('pkis:concept:x', { direction: 'out', max_hops: 2 });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body))
      .toEqual({ iri: 'pkis:concept:x', direction: 'out', max_hops: 2 });
  });

  it('discoveryAct posts to /pkis-api/discovery/act', async () => {
    const fetchMock = mockFetch({ ok: true });
    await discoveryAct('W123', 'accept');
    expect(fetchMock.mock.calls[0][0]).toBe('/pkis-api/discovery/act');
  });
});

describe('api.ts GET contract', () => {
  it('getReaderStatus GETs /pkis-api/reader/<slug>/status', async () => {
    const fetchMock = mockFetch({ state: 'ready' });
    await getReaderStatus('mackay-itila');
    expect(fetchMock.mock.calls[0][0]).toBe('/pkis-api/reader/mackay-itila/status');
  });
});

describe('api.ts error handling', () => {
  it('throws ApiError carrying the server message + status on non-ok', async () => {
    mockFetch({ error: 'no such node' }, false, 404);
    await expect(getNode('pkis:concept:missing')).rejects.toMatchObject({
      name: 'ApiError',
      status: 404,
      message: 'no such node',
    });
    // And it is the exported ApiError type.
    const caught = await getNode('x').catch((e) => e);
    expect(caught).toBeInstanceOf(ApiError);
  });
});
