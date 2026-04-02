/**
 * Parses studio.edn at build time and returns plain JS objects.
 * Uses edn-data with mapAs:'object' + keywordAs:'string' which handles
 * keywords -> strings, maps -> objects, vectors -> arrays natively.
 */

import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { parseEDNString } from 'edn-data';

export function getStudio(): any {
  const ednPath = resolve(
    import.meta.dirname ?? new URL('.', import.meta.url).pathname,
    '../../../studio.edn'
  );
  const raw = readFileSync(ednPath, 'utf-8');
  return parseEDNString(raw, { mapAs: 'object', keywordAs: 'string' });
}
